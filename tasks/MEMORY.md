# Agentic OS Memory

Repo-local decisions and session history for `/Users/nadavyigal/Documents/Projects /Agentic OS`.

Use this file for durable Agentic OS learnings that are likely to matter again. Keep entries concise and auditable. Do not store secrets, credentials, customer data, or one-off preferences.

## 2026-05-31 - OS Command Center + Orchestration Map refresh
Worked on: Centralized dashboard to talk to each OS directly, plus refreshing the Orchestration Map after iOS + Agentic OS progress.
Completed: Built `dashboard/command-center.html` (new) — a static launcher with one card per OS (CEO, CFO, Analysis, Director, Distribution, Growth, Architect, PM, QA, Release Manager, UI/UX). Each card has a status dot, a "Copy conversation starter" button (clipboard, with file:// fallback) that pastes a context-loaded prompt into Claude Code/Cursor, deep links into that OS's docs/prompts, and a live keyword filter. Refreshed `dashboard/orchestration.html` (stamp 2026-05-31; RunSmart PostHog/activation events now wired+firing; rs-analytics-001 done; EXD-002/003 resolved + Q2/Q3 OKRs drafted). Cross-linked all three dashboards (index + status.json nav now include Command Center + Orchestration Map). Documented the new file in `dashboard/README.md`.
Verified: All 4 embedded/JSON blocks parse; all 34 deep-link targets exist on disk; `git diff --check` clean. No live browser screenshot (no server; reuses orchestration.html's proven CSS).
Decisions: Interaction model = "launcher + deep links" (user choice). Live embedded chat rejected — would break dashboard guardrails (no backend, no API key in code, no paid service). To add an OS: append to a group's `items` array in the `cc-data` JSON block; `{date}` auto-fills the generated date.
Next session: If new OSes/agents are added under SKILLS/ or executive-os/, add matching cards. Consider a `gen` note in README for keeping the Command Center status dots in sync with status.json.

## 2026-05-31 - Codex, Cursor, Claude Code Alignment
Worked on: Aligning repo-local agent routing so Codex, Cursor, and Claude Code share `AGENTS.md` as the source of truth while keeping tool-specific adapters lean.
Completed: Added Codex guardrails, repo-local memory/error files, Cursor routing updates, Claude `@AGENTS.md` import while preserving Claude-specific repo context, executive-os local instructions, and alignment docs.
In progress: Manual cleanup remains outside this repo: rotate the exposed Resend token and remove the matching allowlist entry from `~/.claude/settings.json`.
Decisions: Do not modify files under `~/.claude/` from Codex. The known Resend token cleanup is a manual Claude/global-config task.
Next session: Re-check alignment files before changing agent behavior again.
