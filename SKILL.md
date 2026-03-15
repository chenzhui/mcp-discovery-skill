---
name: mcp-discovery-skill
description: Discover and install MCP servers or Codex skills when Codex lacks a needed system capability, when an existing approach is too manual or low-efficiency for a high-frequency task, or when a specialized tool integration would materially reduce repeated effort. Use for capability gaps, repetitive low-leverage workflows, tool-market research, MCP/skill evaluation, and installation/configuration of promising candidates.
---

# MCP Discovery Skill

Use this skill to decide whether a missing or inefficient workflow should be solved by:

- installing an MCP server
- installing a Codex skill
- keeping the task in the current toolchain

## Trigger Conditions

Invoke this skill when any of the following is true:

- A task requires a capability not currently available in the tool list.
- A task is possible with existing tools but would be slow, repetitive, or fragile if repeated.
- A workflow is recurring often enough that manual execution is no longer justified.
- The task would benefit from a specialized integration such as VM control, browser automation, package registries, cloud providers, databases, OCR, GUI automation, or device access.
- The user explicitly asks to find, evaluate, install, or compare MCPs or skills.

## Default Workflow

1. Define the missing or inefficient capability in one sentence.
2. Decide the desired acquisition target:
   - prefer an `MCP` when the gap is access to an external system, API, desktop capability, hardware, or runtime integration
   - prefer a `skill` when the gap is procedural knowledge, repeatable workflow guidance, lightweight helper scripts, or repo-local scaffolding
3. Search public discovery sources. Start with [references/markets.md](./references/markets.md).
4. Rank candidates using [references/evaluation.md](./references/evaluation.md).
5. Prefer the smallest tool that closes the gap.
6. Install or configure only after verifying:
   - the candidate matches the actual need
   - the repository appears maintained
   - the install path fits the current environment
7. After installation, validate the new capability with one real task.

## Search Procedure

Run [discover_candidates.py](./scripts/discover_candidates.py) first. It searches:

- `mcpworld.com`
- GitHub repositories

Use queries built from:

- the missing capability
- the target system
- the user-facing action
- the expected transport or tool family

Examples:

- `vmware workstation screenshot mcp`
- `ocr desktop automation mcp`
- `codex skill install github repo`
- `android emulator mcp`
- `database schema exploration skill`

If the first pass is noisy, rerun with one of:

- a product name
- an API or protocol name
- `mcp`
- `codex skill`

## Acquisition Rules

### Install an MCP

Choose an MCP when the solution needs runtime access to systems or capabilities that Codex does not already possess, such as:

- virtualization platforms
- browsers or desktop apps
- mobile devices
- SSH targets
- cloud services
- databases
- package registries
- OCR or local GUI control

After selection:

1. inspect the upstream install instructions
2. install dependencies
3. add or update the MCP entry in the Codex config
4. note whether a restart is required
5. validate with a minimal live call

### Install a Skill

Choose a skill when the solution is mostly reasoning workflow, repeatable decision logic, helper scripts, templates, or domain-specific guidance.

After selection:

1. prefer the local `skill-installer` workflow when the repo already contains a valid Codex skill
2. otherwise clone or inspect the repo and verify the skill folder layout
3. install into `$CODEX_HOME/skills`
4. validate with one explicit invocation

## Efficiency Trigger

Do not wait for a total capability gap. Trigger this skill proactively when:

- the same shell sequence is being repeated across turns
- a workflow repeatedly requires manual page inspection or repetitive configuration edits
- the task can be completed today, but only with brittle glue code or many manual steps
- the task is likely to recur and a specialized tool would save time across future runs

The threshold is qualitative: if a specialized integration would likely pay back within a few future uses, search for an MCP or skill.

## Validation

Before closing the task:

1. state why the chosen MCP or skill is a better fit than the current manual path
2. confirm installation/configuration success
3. verify the new capability on one concrete example
4. note restart requirements or remaining limits

## Resources

- Market list and search starting points: [references/markets.md](./references/markets.md)
- Candidate scoring checklist: [references/evaluation.md](./references/evaluation.md)
- Candidate discovery helper: [scripts/discover_candidates.py](./scripts/discover_candidates.py)
