# AGENTS.md - Global Agentic OS

You are working with Nadav Yigal across a suite of products: RunSmart (web + iOS) and ResumeBuilder (iOS). This file is the global rule layer. When working inside a specific product repo, also read that repo's AGENTS.md.

## What This Repo Is

This repo is the Global Agentic OS: a cross-project reference layer, command center, and shared workflow library for Claude Code, Codex, Cursor, and future agents. It is not a software product. There are no app build, lint, or test commands here unless a specific subfolder documents one.

Use this repo for cross-project planning, shared standards, reusable prompts, bridge files, distribution OS work, executive OS work, and agent configuration. Do daily product implementation inside the relevant product repo.

## Who You're Working With

Solo founder. Two apps in parallel. RunSmart is primary; ResumeBuilder is secondary. Mac-based. Speed and clarity matter more than ceremony.

## Project Paths

| Project | Local Path |
|---|---|
| RunSmart Web | `/Users/nadavyigal/Documents/RunSmart` |
| RunSmart iOS | `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app` |
| ResumeBuilder iOS | `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP` |
| Agentic OS | `/Users/nadavyigal/Documents/Projects /Agentic OS` |

## Session Start Ritual (Every Session, Every Project)

Before doing anything — in this order:

1. Read `~/.claude/MEMORY.md` - global decisions. Never contradict a logged decision without flagging it first.
2. Read `~/.claude/ERRORS.md` - global failed approaches. Never propose an approach already logged here.
3. Read `tasks/MEMORY.md` if it exists in the current project - project-specific decisions.
4. Read `tasks/ERRORS.md` if it exists in the current project - project-specific failed approaches.
5. State the objective in one sentence before planning anything.
6. Write a 5-step plan maximum before touching any file.

## Global Work Rules

1. Read before planning. Never plan from memory about file content. Read the actual files.
2. State the objective first. One sentence. If you cannot write it, the task is ambiguous — ask.
3. One story at a time. Implement, verify, report, then ask before the next.
4. Lint and tests must pass before any "done" declaration.
5. No unrelated file changes. If a file was not in scope, do not touch it.
6. No new dependencies without asking first.
7. Scope gate: if a fix expands to touch more than 3 unexpected files, stop and surface it.
8. No secrets in code. No hardcoded API keys, URLs, or env-specific values.
9. End every session with: files changed, tests run, open questions, what was NOT done.
10. Update lessons. If a new recurring bug is found and fixed, add it to `tasks/lessons.md`.

## Definition of Done

Before claiming done:

1. Run checks that exist for the touched files. For this markdown-first repo, use `git diff --check`, targeted file reads, and any documented script for the changed subfolder.
2. If editing agent routing files, verify line count stays lean and the relevant router still points to `AGENTS.md`.
3. If editing dashboards or status, name the source files used and do not invent status from memory.
4. Report files changed, checks run with results, checks not run with reason, open questions, and what was NOT done.

## Before Executing Any Task

1. Restate what you understood: the action, the deliverable, and what success looks like.
2. List the 3 rules from the memory files that matter most for this specific task.
3. Write your execution plan in 5 steps maximum.
4. If anything is unclear, ask before proceeding — never fill gaps silently.

Then execute. Go beyond the basics. Deliver like a real production build.

## Do NOT Introduce Unless Asked

- New dependencies, plugins, MCP servers, package managers, or background services.
- Duplicate full instruction sources such as a separate `CODEX.md` that repeats `AGENTS.md`.
- New process layers when an existing `GLOBAL-*`, `PROMPTS/`, `TEMPLATES/`, `distribution-os/`, or `executive-os/` file can carry the work.
- Production credentials, API keys, bearer tokens, customer data, or env-specific secrets.
- Broad product-repo edits from this global repo. Switch to the product repo and its local instructions.
- External publishing, deploys, App Store actions, migrations, or paid tool actions.

## Stop And Ask Before

- Changing public architecture, project paths, repo ownership, cross-project status policy, or durable decisions.
- Editing auth, billing, permissions, migrations, production data, deployment config, or external service config.
- Installing dependencies or tools.
- Touching more than 3 unexpected files, or expanding beyond the stated task scope.
- Editing tests, dashboards, or memory files just to make a result look green.
- Running any command that could write to production, billing, users, App Store, email, ads, or public channels.

## ERRORS.md Gate

Before proposing any fix or approach:
- Read `tasks/ERRORS.md` (project-specific)
- Read `~/.claude/ERRORS.md` (global)

If a similar approach is already logged as failed, do not re-propose it. Surface the logged failure instead and propose a different path.

## Never Do

- Open with warmup phrases ("Great question", "Of course", "Certainly", "Absolutely", "Sure")
- Use em dashes, use commas or rewrite the sentence
- Say "dive into", "it's worth noting", "let's explore", "in conclusion"
- Ask "would you like me to continue?" — just continue
- Propose an approach already in ERRORS.md as failed
- Declare done without evidence (lint pass, test pass, or manual QA confirmed)
- Deploy or run migrations without explicit "yes" in the current message
- Suggest new npm/SPM dependencies without asking first
- Touch files outside the stated task scope

## Session End

When I say "session end", "done for now", "wrapping up", or "let's stop here":

1. Write a session summary to `tasks/MEMORY.md` (or `~/.claude/MEMORY.md` if cross-project):
```
## YYYY-MM-DD — [Brief session title]
Worked on: [what we focused on]
Completed: [what is finished and verified]
In progress: [what was started but not finished]
Decisions: [key choices made]
Next session: [what to pick up first, with enough context to resume cold]
```
2. If any approach failed more than once this session, append it to `tasks/ERRORS.md`.
3. List: files changed, tests run, open questions, what was NOT done.

## Cross-Project Decisions

All durable architectural decisions are logged in `DECISIONS.md`. Read it before making any architectural recommendation. Add to it when a new cross-project decision is made.

## Agent Routing

- `AGENTS.md` is the canonical source for shared agent behavior.
- `CLAUDE.md` may import this file and keep Claude Code specific routing only.
- `CURSOR.md` and `.cursor/rules/` are Cursor adapters for this same contract.
- `.codex/` contains Codex-only guardrail configuration. Treat hooks and rules as safety aids, not as a replacement for careful review.

## File Map

| File | Role |
|---|---|
| `DECISIONS.md` | Cross-project architectural decisions, read before architecture work |
| `LESSONS.md` | Global lessons, repeated, expensive, or easy-to-forget issues |
| `GLOBAL-AGENT-RULES.md` | Detailed agent rules if more context is needed |
| `GLOBAL-STANDARDS.md` | Product, engineering, UI, and QA standards |
| `GLOBAL-QA-RULES.md` | Completion evidence, visual QA, and risky-change checklist |
| `GLOBAL-WORKFLOWS.md` | Universal idea-to-shipping and planning workflows |
| `PROJECT-STATUS.md` | Current status per project |
| `PROJECT-PATHS.md` | Canonical paths and source of truth for project locations |
| `CURSOR.md` | Cursor-native router; Cursor reads `AGENTS.md` via this file + `.cursor/rules/` |
| `distribution-os/` | Cross-product distribution system. Read `distribution-os/AGENTS.md` before distribution work |
| `executive-os/` | Layer 8, Executive Intelligence OS. Read `executive-os/AGENTS.md` before strategy, finance, research, and weekly/monthly executive reviews |
