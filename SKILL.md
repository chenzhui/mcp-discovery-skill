---
name: mcp-discovery-skill
description: Decide whether a missing capability or a repetitive low-efficiency workflow is worth solving with an MCP server or a Codex skill. Use when Codex lacks an important system capability, when the same manual workflow keeps recurring, or when the user explicitly asks to find or compare MCPs or skills.
---

# MCP Discovery Skill

Use this skill as a lightweight router to decide between: `manual`, `skill`, or `MCP`.

## Trigger

Invoke only when:
- Codex is missing a critical capability.
- A manual workflow is repetitive and inefficient.
- The user explicitly asks to find/compare tools.

## Stop Conditions (Do Not Search)

1. **Rejected**: User previously rejected this tool (check `.mcp-discovery-decisions.json`).
2. **Cheap**: Workflow is rare or easy enough to stay manual.
3. **Solved**: Existing tools already cover the need.

## Rejection Registry

Check for `.mcp-discovery-decisions.json` in the workspace. If a matching rejection exists:
- Stop immediately.
- Do not search again unless explicitly requested.

## Minimal Workflow

1. **Decide Target**:
   - `MCP`: runtime/system integrations.
   - `Skill`: workflow templates/logic.
2. **Search**: Run `scripts/discover_candidates.py` once.
3. **Select**: Keep max 3 candidates.
4. **Decide**: Recommend `stay manual`, `install skill`, or `install MCP`.

## Search Limits

- Default to one search round.
- Refine query only if results are very poor.
- Do not produce long comparisons unless asked.

## Output Format

Return a short result:

- **Decision**: `stay manual` | `install skill` | `install MCP`
- **Reason**: (1 sentence)
- **Next Action**: (e.g. "None", "Ask user to install X")

## Resources

- [references/markets.md](./references/markets.md)
- [scripts/discover_candidates.py](./scripts/discover_candidates.py)
