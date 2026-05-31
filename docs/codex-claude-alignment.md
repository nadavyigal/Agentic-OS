# Codex, Claude Code, and Cursor Alignment

`AGENTS.md` is the shared source of truth for this repo. Tool-specific files should be adapters, not duplicate rule libraries.

## Source Of Truth

- `AGENTS.md`: shared behavior, gates, file map, and session ritual.
- `CLAUDE.md`: Claude Code adapter. It imports `AGENTS.md` and keeps repo-specific Claude routing.
- `CURSOR.md`: Cursor adapter. It points to `AGENTS.md` and `.cursor/rules/`.
- `.codex/`: Codex-only hooks and command rules.
- `tasks/MEMORY.md` and `tasks/ERRORS.md`: repo-local auditable memory and failed approaches.

## Guardrail Layers

Markdown instructions state intent. Hooks, rules, sandboxing, CI, and withheld credentials provide stronger protection.

- Codex hook: `.codex/hooks/pre_tool_use_policy.py`
- Codex hook config: `.codex/hooks.json`
- Codex command rules: `.codex/rules/default.rules`
- Cursor rules: `.cursor/rules/*.mdc`
- Claude Code global config: managed outside this repo and not edited by Codex

## What Codex Should Block Or Prompt

- Block destructive local commands such as `rm -rf`, `git reset --hard`, force push, destructive SQL, and inline secrets.
- Prompt before pushes, deploys, migrations, dependency installs, production writes, or external publishing.
- Stop and ask when scope expands beyond the stated task.

## Security Note

Do not put API keys, bearer tokens, or customer data in repo files, shell commands, allowlists, docs, or examples. If a token appears in a config file, rotate it in the provider dashboard and remove the allowlist entry manually.
