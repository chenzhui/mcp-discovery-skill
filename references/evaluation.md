# Candidate Evaluation

Score each candidate on these dimensions:

## Fit

- Does it solve the exact capability gap?
- Does it reduce repeated effort rather than merely repackage manual work?
- Is it the smallest tool that closes the gap?

## Maintenance

- Recent commits or releases
- Clear install instructions
- Working examples or screenshots
- Signs the repository is not abandoned

## Safety and Friction

- Requires secrets, privileged access, or invasive install steps
- Writes to global config unexpectedly
- Depends on fragile local paths or undocumented binaries
- Requires a restart before becoming usable

## Codex Compatibility

- Can it run headless or from the shell?
- Can Codex install and validate it with available tools?
- Is the output deterministic enough to be useful in automation?

## Decision Rules

- Prefer one strong candidate over many marginal ones.
- Prefer simpler local skills over MCPs when runtime integration is unnecessary.
- Reject tools that add complexity without reducing future cost.
- If no candidate clears the bar, keep the task in the current toolchain and say so explicitly.
