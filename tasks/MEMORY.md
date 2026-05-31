# Agentic OS Memory

Repo-local decisions and session history for `/Users/nadavyigal/Documents/Projects /Agentic OS`.

Use this file for durable Agentic OS learnings that are likely to matter again. Keep entries concise and auditable. Do not store secrets, credentials, customer data, or one-off preferences.

## 2026-05-31 - Codex, Cursor, Claude Code Alignment
Worked on: Aligning repo-local agent routing so Codex, Cursor, and Claude Code share `AGENTS.md` as the source of truth while keeping tool-specific adapters lean.
Completed: Added Codex guardrails, repo-local memory/error files, Cursor routing updates, Claude `@AGENTS.md` import while preserving Claude-specific repo context, executive-os local instructions, and alignment docs.
In progress: Manual cleanup remains outside this repo: rotate the exposed Resend token and remove the matching allowlist entry from `~/.claude/settings.json`.
Decisions: Do not modify files under `~/.claude/` from Codex. The known Resend token cleanup is a manual Claude/global-config task.
Next session: Re-check alignment files before changing agent behavior again.
