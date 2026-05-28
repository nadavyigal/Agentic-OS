# Cursor Setup Guide

How to configure Cursor IDE to work with the Global Agentic OS.

## How Cursor Loads Context

Cursor uses three mechanisms to give the AI agent context:

1. **`.cursor/rules/*.mdc` files** — YAML-frontmatter markdown files in the repo. Can be `alwaysApply: true` (every session) or glob-scoped (only when matching files are open).
2. **`AGENTS.md`** — Automatically loaded as a workspace rule when present at the repo root.
3. **User-level rules** — Set in Cursor Settings for rules that apply across all workspaces.

## Mapping Claude Code Concepts to Cursor

| Claude Code | Cursor equivalent |
|---|---|
| `CLAUDE.md` (auto-loaded) | `AGENTS.md` (auto-loaded) + `.cursor/rules/*.mdc` |
| `~/.claude/settings.json` hooks | `.cursor/rules/agent-os-core.mdc` with `alwaysApply: true` |
| Claude Stop hook (writes MEMORY) | Manual: agent writes to MEMORY on "session end" phrase |
| `~/.claude/MEMORY.md` | Same file, shared — Cursor reads it via session-start rule |
| `~/.claude/ERRORS.md` | Same file, shared — Cursor reads it via ERRORS gate rule |

## Recommended Setup Per Repo

1. Copy `TEMPLATES/cursor-rules-core.mdc` to `.cursor/rules/agent-os-core.mdc`
2. Add stack-specific rules (e.g., `swift-ios.mdc`, `nextjs-ts.mdc`)
3. Create a thin `CURSOR.md` router (use `TEMPLATES/cursor-router-template.md`)
4. Ensure `tasks/MEMORY.md` and `tasks/ERRORS.md` exist

## Optional: User-Level Rule

In Cursor Settings > Rules, add this as an always-on user rule for safety across all Nadav workspaces:

```
At session start for any project:
1. Read ~/.claude/MEMORY.md for cross-project decisions
2. Read ~/.claude/ERRORS.md and never re-propose failed approaches
3. State the objective in one sentence before planning
```

This is a safety net for repos that do not yet have `.cursor/rules/agent-os-core.mdc`.

## Memory Architecture

All agents (Claude Code, Codex, Cursor) share the same memory stores:

```
~/.claude/MEMORY.md     — cross-project decisions and session history
~/.claude/ERRORS.md     — failed approaches (global)
tasks/MEMORY.md         — per-project session history (in each repo)
tasks/ERRORS.md         — per-project failed approaches
tasks/lessons.md        — recurring bugs and patterns
```

Cursor does not get its own memory files. This prevents drift between tools.

## Desktop (Brain) + Cursor (Hands) Workflow

Same as the Claude Desktop + CLI pattern:

- **Desktop** = planning, spec, QA review (Claude Desktop Projects)
- **Cursor** = implementation, git, tests, multi-file refactors

Handoff Desktop to Cursor: share the plan file path or paste the spec.
Handoff Cursor to Desktop: paste the session summary for QA review.

## Bootstrapping a New Repo

Use the prompt at `PROMPTS/bootstrap-cursor-os.md`:

1. Provide the repo path
2. The prompt generates `CURSOR.md` + `.cursor/rules/agent-os-core.mdc`
3. It respects existing `AGENTS.md` and `tasks/` structure
4. No duplication of content already in `AGENTS.md`
