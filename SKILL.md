---
name: mcp-discovery-skill
description: Decide whether a missing capability or a repetitive low-efficiency workflow is worth solving with an MCP server or a Codex skill. Use when Codex lacks an important system capability, when the same manual workflow keeps recurring, or when the user explicitly asks to find or compare MCPs or skills. Do not use for one-off tasks that are already cheap to complete manually.
---

# MCP Discovery Skill

Use this skill as a lightweight router, not a research project.

Goal:

- decide whether to stay manual
- decide whether to look for a skill
- decide whether to look for an MCP

## Trigger

Invoke this skill only when at least one is true:

- Codex is missing a capability that matters for the task.
- The same manual workflow is repeating and is no longer cheap.
- The user explicitly asks to find, compare, or install an MCP or skill.

Do not invoke this skill for one-off work that is already easy.

## Stop Conditions

Check these before searching:

1. If the user already rejected tool acquisition for this workflow, stop.
2. If the workflow is cheap enough to keep manual, stop.
3. If existing tools already solve the problem well enough, stop.

If any stop condition applies, do not search for plugins.

## Rejection Registry

Look for a local file such as `.mcp-discovery-decisions.json` in the workspace or task root.

If it contains a matching rejection entry:

- do not search again automatically
- continue with the manual path
- only reopen the search if the user explicitly asks to revisit the decision

Use [assets/mcp-discovery-decisions.example.json](./assets/mcp-discovery-decisions.example.json) as the schema template.

Matching priority:

1. exact capability
2. keyword overlap
3. broad category match

## Minimal Workflow

1. Compress the problem into one sentence.
2. Decide the target:
   - prefer `MCP` for runtime/system/external integrations
   - prefer `skill` for workflow knowledge, templates, or lightweight helper logic
3. Run one search pass using [scripts/discover_candidates.py](./scripts/discover_candidates.py) or a direct web search.
4. Keep at most 3 candidates.
5. Pick one of these outputs:
   - `stay manual`
   - `install a skill`
   - `install an MCP`

Default to the smallest next step.

## Search Limits

To avoid wasting tokens:

- do one search round by default
- only refine the query once if results are obviously noisy
- do not produce long comparisons unless the user asks
- do not keep searching after you already have one good candidate

## Output Format

Return a short result in this shape:

1. decision
2. brief reason
3. next action

Example:

- decision: `stay manual`
- reason: `the workflow is rare and current tools already cover it`
- next action: `do not search again unless the user reopens the decision`

## Resources

- Markets: [references/markets.md](./references/markets.md)
- Evaluation checklist: [references/evaluation.md](./references/evaluation.md)
- Discovery helper: [scripts/discover_candidates.py](./scripts/discover_candidates.py)
- Rejection registry template: [assets/mcp-discovery-decisions.example.json](./assets/mcp-discovery-decisions.example.json)
