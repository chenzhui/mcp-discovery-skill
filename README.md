# MCP Discovery Skill

[简体中文](./README.zh-CN.md)

A Codex skill for deciding when a task should stay manual, when it should be solved with a Codex skill, and when it is worth installing an MCP server.

This skill is designed for two trigger patterns:

- Codex is missing a capability that would materially help complete the task.
- Codex can complete the task today, but the workflow is high-frequency, repetitive, or inefficient enough that a specialized MCP or skill should be considered.

## Quick Start

1. Clone the repository.
2. Copy the `mcp-discovery-skill` folder into your Codex skills directory.
3. Restart Codex.
4. Invoke `$mcp-discovery-skill` when you hit a capability gap or a repetitive low-efficiency workflow.

Windows example:

```powershell
git clone https://github.com/chenzhui/mcp-discovery-skill.git
Copy-Item -Recurse .\mcp-discovery-skill "C:\Users\<you>\.codex\skills\public\"
```

## What It Does

- Identifies missing or low-efficiency capabilities.
- Searches public MCP discovery surfaces and GitHub.
- Evaluates candidate MCPs and skills.
- Recommends the smallest useful tool instead of installing tools by default.
- Helps decide whether the right answer is `manual`, `skill`, or `MCP`.

## Repository Layout

```text
mcp-discovery-skill/
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── evaluation.md
│   └── markets.md
└── scripts/
    └── discover_candidates.py
```

## Included Files

- `SKILL.md`: the skill definition and operating workflow.
- `agents/openai.yaml`: UI-facing skill metadata.
- `references/markets.md`: the default MCP marketplaces and search starting points.
- `references/evaluation.md`: the candidate scoring checklist.
- `scripts/discover_candidates.py`: helper script for searching GitHub and MCP discovery sites.

## Default MCP Market Sources

The skill starts with these public discovery surfaces:

- `https://www.mcpworld.com`
- `https://smithery.ai`
- `https://glama.ai/mcp`

These are starting points, not hard-coded authority rankings.

## Installation

### Install as a local Codex skill

1. Locate your Codex skills directory.
   Typical path on Windows:
   `C:\Users\<you>\.codex\skills\public\`
2. Copy this entire `mcp-discovery-skill` folder into that directory.
3. Restart Codex or start a new session.

The final layout should look like this:

```text
$CODEX_HOME/skills/public/mcp-discovery-skill/
```

### Install from Git

```bash
git clone https://github.com/chenzhui/mcp-discovery-skill.git
```

Then copy the folder into your Codex skills directory and restart Codex.

## Usage

Invoke it explicitly when needed:

```text
$mcp-discovery-skill
```

Typical prompts:

- `Use $mcp-discovery-skill to find an MCP for VMware Workstation screenshots.`
- `Use $mcp-discovery-skill to decide whether this repetitive browser workflow should stay manual or become a skill.`
- `Use $mcp-discovery-skill to search for a tool that can reduce repeated Android emulator setup work.`

## Search Helper Script

Example:

```bash
python scripts/discover_candidates.py "vmware workstation screenshot mcp" --limit 5
```

The script is a discovery helper. It does not auto-install third-party tools by itself.

## Design Choice

This repository deliberately does not force automatic MCP installation.

Reason:

- Strong agents can usually read installation documentation and install the selected tool directly.
- The harder problem is deciding whether a new tool is justified.
- Defaulting to discovery and evaluation keeps the skill smaller, safer, and easier to reuse.

## License

MIT. See [LICENSE](./LICENSE).
