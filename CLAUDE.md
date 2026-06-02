@AGENTS.md

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

This folder is the **Global Agentic OS** — a cross-project reference library and command center for AI agents (Claude Code, Codex, Cursor) working across all of Nadav's products. It is not a software product. There are no build commands, tests, or lint tools.

Daily implementation work happens inside individual product repos, not here. Use this folder selectively, only when:

- Work spans multiple products
- You need shared standards, templates, or prompts
- You are creating or updating bridge files
- You are doing cross-project planning or reviewing global strategy

## Local Project Paths

| Project | Local Path |
|---|---|
| RunSmart Web | `/Users/nadavyigal/Documents/RunSmart` |
| RunSmart iOS | `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app` |
| ResumeBuilder iOS | `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP` |
| Global Agentic OS | `/Users/nadavyigal/Documents/Projects /Agentic OS` (here) |

See `PROJECT-PATHS.md` for the authoritative list and `PROJECT-STATUS.md` for current status per project.

## File Map

| File / Dir | Role |
|---|---|
| `OWNER.md` | Owner work style and communication preferences — read first for any new session |
| `GLOBAL-AGENT-RULES.md` | Core rules for all agents across all projects |
| `GLOBAL-STANDARDS.md` | Product, engineering, UI, and QA standards |
| `GLOBAL-TASTE.md` | Taste & craft layer; pass/revise/reject judgment that protects products from generic AI output, overbuild, and weak UX. Paired with `SKILLS/taste-reviewer.md` |
| `GLOBAL-WORKFLOWS.md` | Universal idea-to-shipping workflow; cross-project planning workflow |
| `GLOBAL-QA-RULES.md` | Completion evidence requirements, visual QA, risky-change checklist |
| `GLOBAL-SELF-IMPROVEMENT.md` | Protocol for capturing and applying cross-project lessons |
| `PROJECTS.md` | Brief registry of active and future products |
| `PROJECT-STATUS.md` | Generated status table; update when pulling fresh status from project repos |
| `PROJECT-PATHS.md` | Canonical local filesystem paths; update when a repo moves |
| `DECISIONS.md` | Durable cross-project architectural decisions |
| `LESSONS.md` | Global lessons — repeated, expensive, or easy-to-forget issues only |
| `BACKLOG.md` | Cross-project and global OS work items only |
| `DASHBOARD.md` | Detailed narrative dashboard; companion to `dashboard/status.json` |
| `STATUS-SCHEMA.md` | Contract the refresh parser reads from `tasks/progress.md` (keys, validation vocabulary, confidence + freshness rules). Follow it so a project can reach High confidence. Paired with `TEMPLATES/progress-template.md` |
| `CURSOR.md` | Cursor-native router; points to `AGENTS.md` with Cursor-specific notes |
| `docs/cursor-setup.md` | How to set up Cursor with the Agent OS (rules, memory mapping, bootstrapping) |
| `PROMPTS/` | Reusable agent prompts: `plan-feature`, `risk-review`, `implement-story`, `qa-review`, `bug-fix`, `pr-summary`, `ui-review`, `repo-onboarding`, `update-lessons`, `create-project-bridge`, `morning-brief`, `exec-review`, `bootstrap-cursor-os` |
| `TEMPLATES/` | Blank templates: brief, spec, story, QA report, PR summary, decision, lesson, bridge, cursor-rules-core, cursor-router, session-summary, errors-entry |
| `SKILLS/` | Agent role definitions for multi-agent work: architect, director, growth, product-manager, QA, release-manager, UI/UX |
| `PROJECT-BRIDGES/` | One bridge file per product; connects global strategy to local repo context |
| `dashboard/` | Static HTML dashboard (`index.html`, `status.json`, `styles.css`) — update `status.json` when project states change |
| `executive-os/` | **Layer 8 — Executive Intelligence OS.** CEO OS (strategy, OKRs, decisions), CFO/Monetization OS (budget, revenue, pricing, runway), Analysis OS (research, opportunities). Markdown-first; reuses `distribution-os/`, `morning-brief`, and `exec-review`; invents no financial data. Start at `executive-os/README.md` |

## How Agents Should Use This Folder

**For a task inside a product repo:**
1. Go to the product repo. Do not load this folder by default.
2. Read the local `CLAUDE.md`, `AGENTS.md`, and `tasks/lessons.md`.
3. Read the relevant bridge file from `PROJECT-BRIDGES/` only if cross-project context is needed.

**For cross-project or global OS work:**
1. Read `PROJECTS.md` and the relevant bridge files.
2. Read `GLOBAL-AGENT-RULES.md` and `GLOBAL-STANDARDS.md`.
3. Use `PROMPTS/` and `TEMPLATES/` as scaffolding — do not duplicate their content into chat.
4. Update `LESSONS.md`, `DECISIONS.md`, or `BACKLOG.md` when appropriate; keep entries concise.

## Updating the Dashboard

When project status changes, update `dashboard/status.json` directly. To regenerate the full `PROJECT-STATUS.md` and `DASHBOARD.md`, read the canonical task files inside each product repo (`tasks/todo.md`, `tasks/session-log.md`, `tasks/lessons.md`) and synthesize — do not invent status from memory.
