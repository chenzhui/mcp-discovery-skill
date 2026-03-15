#!/usr/bin/env python3
"""
Search MCP discovery sources and GitHub repositories for MCPs or Codex skills.

Examples:
  python scripts/discover_candidates.py "vmware workstation screenshot mcp"
  python scripts/discover_candidates.py "desktop OCR automation" --kind mcp
  python scripts/discover_candidates.py "install codex skill from github" --kind skill --limit 5
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from typing import Iterable, List


USER_AGENT = "mcp-discovery-skill/1.0 (+https://github.com/)"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


@dataclass
class Candidate:
    source: str
    kind: str
    name: str
    url: str
    summary: str
    score_hint: int


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=20) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def github_repo_search(query: str, limit: int, kind: str) -> List[Candidate]:
    q = query
    if kind == "mcp":
        q = f"{query} mcp in:name,description,readme"
    elif kind == "skill":
        q = f'{query} ("SKILL.md" OR "Codex skill") in:readme,description'

    url = (
        "https://api.github.com/search/repositories?"
        + urllib.parse.urlencode(
            {
                "q": q,
                "sort": "stars",
                "order": "desc",
                "per_page": str(limit),
            }
        )
    )
    payload = json.loads(fetch(url))
    results: List[Candidate] = []
    query_terms = [term for term in re.split(r"[^a-z0-9]+", query.lower()) if len(term) >= 3]
    for item in payload.get("items", []):
        desc = item.get("description") or ""
        stars = item.get("stargazers_count", 0)
        topics = item.get("topics", [])
        haystack = " ".join(
            [
                item.get("name", ""),
                item.get("full_name", ""),
                desc,
                " ".join(topics),
            ]
        ).lower()
        overlap = sum(1 for term in query_terms if term in haystack)
        if query_terms and overlap == 0:
            continue
        hint = min(
            100,
            25
            + min(stars, 5000) // 120
            + (12 if "mcp" in topics or "mcp" in haystack else 0)
            + overlap * 10,
        )
        results.append(
            Candidate(
                source="github",
                kind=kind,
                name=item["full_name"],
                url=item["html_url"],
                summary=desc.strip(),
                score_hint=hint,
            )
        )
    return results


def mcpworld_search(query: str, limit: int) -> List[Candidate]:
    url = "https://www.mcpworld.com/?q=" + urllib.parse.quote_plus(query) + "&type=normal"
    html_text = fetch(url)
    matches = re.finditer(
        r'/zh/detail/[^"]+".*?<img[^>]+alt="([^"]+)".*?服务详情：[^<]*</a>.*?<img[^>]+github icon".*?</a>.*?<[^>]*>(.*?)</',
        html_text,
        re.S,
    )
    results: List[Candidate] = []
    for match in matches:
        detail_href = re.search(r'/zh/detail/[^"]+', match.group(0))
        if not detail_href:
            continue
        name = html.unescape(match.group(1)).strip()
        summary = re.sub(r"\s+", " ", html.unescape(match.group(2))).strip()
        results.append(
            Candidate(
                source="mcpworld",
                kind="mcp",
                name=name,
                url="https://www.mcpworld.com" + detail_href.group(0),
                summary=summary,
                score_hint=55,
            )
        )
        if len(results) >= limit:
            break
    return results


def dedupe(items: Iterable[Candidate]) -> List[Candidate]:
    seen = set()
    out: List[Candidate] = []
    for item in items:
        key = (item.url.lower(), item.name.lower())
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="Capability gap or inefficient workflow description")
    parser.add_argument(
        "--kind",
        choices=["auto", "mcp", "skill"],
        default="auto",
        help="Target acquisition type",
    )
    parser.add_argument("--limit", type=int, default=5, help="Max results per source")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    return parser.parse_args()


def infer_kind(query: str) -> str:
    lowered = query.lower()
    skill_terms = ("skill", "workflow", "template", "playbook", "guidance")
    if any(term in lowered for term in skill_terms):
        return "skill"
    return "mcp"


def rank(results: List[Candidate]) -> List[Candidate]:
    return sorted(results, key=lambda item: (-item.score_hint, item.source, item.name.lower()))


def render_markdown(results: List[Candidate], query: str, kind: str) -> str:
    lines = [
        f"# Discovery Results",
        "",
        f"- query: `{query}`",
        f"- target: `{kind}`",
        "",
        "| source | kind | score | name | url | summary |",
        "|---|---:|---:|---|---|---|",
    ]
    for item in results:
        raw_summary = item.summary
        if len(raw_summary) > 180:
            raw_summary = raw_summary[:179] + "…"
        summary = raw_summary.replace("|", "\\|")
        lines.append(
            f"| {item.source} | {item.kind} | {item.score_hint} | {item.name} | {item.url} | {summary} |"
        )
    if len(lines) == 6:
        lines.append("| - | - | - | no results | - | refine the query and rerun |")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    kind = args.kind if args.kind != "auto" else infer_kind(args.query)

    results: List[Candidate] = []
    try:
        if kind == "mcp":
            results.extend(mcpworld_search(args.query, args.limit))
        results.extend(github_repo_search(args.query, args.limit, kind))
    except Exception as exc:
        print(f"error: discovery failed: {exc}", file=sys.stderr)
        return 1

    ranked = rank(dedupe(results))
    if args.json:
        print(json.dumps([asdict(item) for item in ranked], ensure_ascii=False, indent=2))
    else:
        print(render_markdown(ranked, args.query, kind))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
