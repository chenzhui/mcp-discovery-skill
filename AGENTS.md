# Repository Guidelines

## Project Structure

- `SKILL.md`: the skill's core behavior and trigger logic.
- `README.md`: English user-facing documentation.
- `README.zh-CN.md`: Chinese user-facing documentation.
- `agents/openai.yaml`: UI metadata for the skill.
- `references/`: supporting reference material used by the skill.
- `scripts/`: helper scripts used for discovery workflows.
- `assets/`: icons and example decision files.

## Editing Rules

- Keep the skill lightweight. Prefer shorter workflows and stronger stop conditions over more analysis steps.
- Do not turn this repository into an automatic installer by default.
- Preserve the rejection-memory behavior. If a change would make the skill re-suggest previously rejected plugin paths, treat that as a regression.
- Keep `SKILL.md` focused on routing and decision-making. Put detailed examples or supporting material in `README` or `references/`.

## Documentation Rules

- When behavior changes, update both `README.md` and `README.zh-CN.md`.
- Keep English and Chinese docs aligned in meaning, not necessarily word-for-word.
- If installation instructions change, update all platform examples together: Windows, macOS, and Linux.

## Validation

- Run the skill validator after editing `SKILL.md`:
  - `python C:/Users/25192/.codex/skills/.system/skill-creator/scripts/quick_validate.py C:\All\AI\2026\codex_workspace\mcp-discovery-skill`
- If `agents/openai.yaml` changes, verify referenced asset paths still exist.
- If `scripts/` change, run at least one real example query before committing.

## Change Priorities

Prefer this order:

1. reduce repeated bad suggestions
2. reduce token waste
3. improve install clarity
4. improve discovery quality
5. add new behavior only if it does not make the skill heavier by default

## Git Conventions

- Use concise commit messages with direct intent, for example:
  - `Add rejection registry workflow`
  - `Simplify skill workflow to reduce token overhead`
  - `Add bilingual README for easier installation`
