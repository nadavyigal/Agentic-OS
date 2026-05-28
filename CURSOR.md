# CURSOR.md — Global Agentic OS

> Cursor-native router. Follow `AGENTS.md` for all cross-cutting rules.
> `CLAUDE.md` is for Claude Code; `CODEX.md` is for Codex. Use them as parity references only.

## Session Start

1. Read `~/.claude/MEMORY.md` — global decisions. Never contradict a logged decision without flagging it first.
2. Read `~/.claude/ERRORS.md` — global failed approaches. Never propose an approach already logged here.
3. Read `tasks/MEMORY.md` if it exists in the current project.
4. Read `tasks/ERRORS.md` if it exists in the current project.
5. State the objective in one sentence before planning anything.
6. Write a 5-step plan maximum before touching any file.

## Before Executing Any Task

1. Restate what you understood: the action, the deliverable, and what success looks like.
2. List the 3 rules from the memory files that matter most for this specific task.
3. Write your execution plan in 5 steps maximum.
4. If anything is unclear, ask before proceeding.

## Working Inside a Product Repo

Open the product repo as the Cursor workspace root. Read the local `AGENTS.md` and `tasks/*` files. Load `PROJECT-BRIDGES/` only for cross-project work.

## Cursor-Specific Notes

- Use **plan mode** for multi-file structural changes.
- Use **subagents** (Task tool) for parallel exploration of large codebases.
- `.cursor/rules/*.mdc` files in each repo enforce session rituals automatically.
- Memory lives at `~/.claude/MEMORY.md` and `~/.claude/ERRORS.md` (shared with Claude Code and Codex).

## ERRORS.md Gate

Before proposing any fix or approach, read `tasks/ERRORS.md` and `~/.claude/ERRORS.md`. If a similar approach is already logged as failed, surface the failure and propose a different path.

## Session End

When Nadav says "session end", "done for now", "wrapping up", or "let's stop here":

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

## File Map

| File | Role |
|---|---|
| `AGENTS.md` | Canonical rules for all agents (read this first) |
| `CURSOR.md` | This file; Cursor-specific routing |
| `CLAUDE.md` | Claude Code routing; parity reference |
| `GLOBAL-AGENT-RULES.md` | Detailed agent rules |
| `GLOBAL-STANDARDS.md` | Product, engineering, UI, and QA standards |
| `PROJECT-BRIDGES/` | Per-product bridge files for cross-project context |
| `TEMPLATES/` | Starter files for new repos, rules, and memory entries |
| `PROMPTS/` | Reusable prompts for common workflows |
| `docs/cursor-setup.md` | How to set up Cursor with this Agent OS |
