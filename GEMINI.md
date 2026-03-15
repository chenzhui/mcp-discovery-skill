# mcp-discovery-skill

## Project Overview

`mcp-discovery-skill` is a specialized **Codex skill** designed to help the agent decide whether a task requires a new **MCP (Model Context Protocol) server**, a new **skill**, or if it should remain a **manual workflow**.

It acts as a lightweight decision-making router that:
- Identifies capability gaps or inefficient repetitive workflows.
- Searches for existing solutions (MCPs or skills) via public directories and GitHub.
- Recommends the "smallest" useful step (Manual > Skill > MCP).
- Respects user decisions via a local "rejection registry" to avoid nagging.

## Installation & Usage

### Installation
This skill is installed by copying the directory into the Codex skills folder.

**Windows:**
```powershell
Copy-Item -Recurse . "C:\Users\<you>\.codex\skills\public\mcp-discovery-skill"
```

**macOS/Linux:**
```bash
cp -R . "$HOME/.codex/skills/public/mcp-discovery-skill"
```

### Usage
Invoke the skill within a Codex session using natural language or the explicit trigger:
> "Use $mcp-discovery-skill to find an MCP for [task]."
> "Use $mcp-discovery-skill to decide if I need a tool for [workflow]."

### Helper Script
The project includes a standalone Python script for discovery, which can be run manually:

```bash
# Search for an MCP
python scripts/discover_candidates.py "vmware workstation screenshot" --kind mcp

# Search for a skill
python scripts/discover_candidates.py "android emulator automation" --kind skill
```

## Structure

- **`SKILL.md`**: The core definition file containing the skill's logic, triggers, and workflow.
- **`agents/openai.yaml`**: Metadata for the skill's UI presentation.
- **`scripts/discover_candidates.py`**: A dependency-free Python 3 script for searching MCPs and skills on GitHub and MCP registries.
- **`references/`**: Documentation and checklists used by the skill during execution.
- **`assets/`**: Contains the rejection registry template (`mcp-discovery-decisions.example.json`).

## Development Conventions

- **Lightweight Design**: The skill is a router, not a heavy researcher. It should fail fast and default to "manual" if no clear gain is found.
- **Rejection Registry**: Strictly adhere to the `mcp-discovery-decisions.json` logic. Never re-suggest a tool the user has explicitly rejected.
- **Multilingual Docs**: Maintain parity between `README.md` (English) and `README.zh-CN.md` (Chinese).
- **Validation**:
  - Run validation scripts before committing changes to `SKILL.md`.
  - Verify `scripts/discover_candidates.py` with real queries after modification.
- **Token Efficiency**: `scripts/discover_candidates.py` defaults to limit=5 and truncates summaries to save context.
