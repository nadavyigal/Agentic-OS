# Claude Code Setup Overhaul — Design Spec

**Date:** 2026-05-20  
**Status:** Approved  
**Problem:** Claude loses context between sessions, re-proposes already-failed approaches, and has no enforced workflow from prompt to QA.  
**Goal:** A structurally enforced system where memory persists, decisions are logged, failed approaches are never repeated, and every task follows a consistent prompt → plan → implement → test → QA workflow.

---

## 1. Memory & Learning Architecture

Three persistent files at two scopes (global + per-project):

### Global (`~/.claude/`)

| File | Purpose |
|------|---------|
| `MEMORY.md` | Cross-project decision log. What was decided, why, what was rejected. |
| `ERRORS.md` | Cross-project failed approaches. What was tried, why it failed, what finally worked. |
| `LEARNINGS.md` | Cross-project positive patterns. Approaches that worked especially well, reusable shortcuts. |

### Per-project (`[project]/tasks/`)

| File | Purpose |
|------|---------|
| `tasks/MEMORY.md` | Project-specific decision log (same format as global). |
| `tasks/ERRORS.md` | Project-specific failed approaches (same format as global). |
| `tasks/lessons.md` | Already exists — recurring bugs and their fix paths. Keep as-is. |

**Rule:** Global files hold cross-project wisdom. Project files hold project-specific history. Claude reads both scopes at session start.

### MEMORY.md Entry Format
```markdown
## 2026-05-20 — [Decision title]
**Decided:** [What was chosen]
**Why:** [The reasoning]
**Rejected:** [Alternatives considered and why ruled out]
```

### ERRORS.md Entry Format
```markdown
## 2026-05-20 — [Task/issue description]
**Tried:** [Approaches that failed and why]
**Worked:** [The approach that finally succeeded]
**Next time:** [Key insight to carry forward]
```

### LEARNINGS.md Entry Format
```markdown
## 2026-05-20 — [Pattern title]
**Pattern:** [What worked well]
**Context:** [When to apply it]
**Evidence:** [Why we know it works]
```

---

## 2. .claude Folder Structure

### Global (`~/.claude/`) — never committed to git

```
~/.claude/
├── CLAUDE.md                    ← global instructions (upgraded per Section 3)
├── MEMORY.md                    ← NEW: global decision log
├── ERRORS.md                    ← NEW: global failed approaches
├── LEARNINGS.md                 ← NEW: global positive patterns
├── settings.json                ← updated with hooks (per Section 4)
├── skills/                      ← existing custom skills (unchanged)
└── agents/
    ├── investigator.md          ← NEW: debug specialist subagent
    └── code-reviewer.md         ← NEW: read-only review subagent
```

### Per-project (`[project]/.claude/`) — can be committed to git

```
[project]/.claude/
├── settings.json                ← project-level permissions + hooks
└── hooks/
    └── bash-firewall.sh         ← blocks destructive shell commands
```

Per-project memory lives in `tasks/` (already exists in RunSmart and ResumeBuilder):
```
[project]/tasks/
├── MEMORY.md                    ← NEW: project decisions
├── ERRORS.md                    ← NEW: project failed approaches
└── lessons.md                   ← existing (unchanged)
```

---

## 3. Global CLAUDE.md Upgrades

Four blocks added to the existing global `~/.claude/CLAUDE.md`. These are appended — nothing existing is removed.

### Block 1 — Session Start Ritual (upgraded)

Replace the existing Session Start Ritual section with:

```markdown
## Session Start Ritual (Every Project, Every Time)

Before doing anything each session:
1. Read ~/.claude/MEMORY.md — never contradict a logged decision without flagging it first
2. Read ~/.claude/ERRORS.md — never propose an approach already logged as failed
3. Read ~/.claude/LEARNINGS.md — prefer patterns logged as working well
4. If working inside a project: read tasks/MEMORY.md and tasks/ERRORS.md
5. Read the project CLAUDE.md (auto-loaded)
6. Read docs/agent-os/project-context.md if it exists
7. Read tasks/lessons.md if it exists
8. State the objective in one sentence before planning anything
9. Follow docs/agent-os/planning-protocol.md for any task touching more than 2 files
```

### Block 2 — Never Do List (new)

```markdown
## Never Do

- Never open responses with: "Great question!", "Of course!", "Certainly!", "Absolutely!", 
  "Sure!", "Happy to help", or any warmup phrase. Start with the answer.
- Never use em dashes (—).
- Never use: "dive into", "it's worth noting", "in today's world", "let's explore".
- Never ask "would you like me to continue?" — just continue.
- Never give generic advice — be specific to this project and codebase.
- Never propose an approach that already appears in ERRORS.md as failed.
- Never declare a task done without evidence (lint pass, test pass, or explicit QA).
```

### Block 3 — Permanent Facts (new)

```markdown
## Permanent Facts

These are always true. If any task conflicts with one of these, flag it before proceeding:

- Solo founder — no team to coordinate with. Speed and clarity matter more than ceremony.
- RunSmart is primary; ResumeBuilder is secondary.
- Mac-based (moved from Windows March 2026).
- Never suggest new npm dependencies without asking first.
- Never deploy or run migrations without explicit yes in the current message.
- Scope gate: if a fix expands to touch >3 unexpected files, stop and surface it.
- No secrets in code — no hardcoded API keys, URLs, or env-specific values.
```

### Block 4 — Session End Trigger (new)

```markdown
## Session End

When I say "session end", "wrapping up", "done for now", or "let's stop here":

1. Write a session summary to tasks/MEMORY.md (or ~/.claude/MEMORY.md if cross-project):
   ## [Date] Session — [Brief title]
   **Worked on:** [what we focused on]
   **Completed:** [what's finished]
   **In progress:** [what's started but not done]
   **Decisions:** [key choices made this session]
   **Next:** [what to pick up first next session]

2. If any approach failed more than once this session, append it to tasks/ERRORS.md.
3. If a pattern worked especially well, append it to ~/.claude/LEARNINGS.md.
4. List files changed, tests run, open questions, and what was NOT done.
```

---

## 4. Hooks Configuration

Added to `~/.claude/settings.json` under the `"hooks"` key.

### Hook 1 — Bash Firewall (PreToolUse)

Intercepts every Bash tool call before execution. Blocks patterns:
- `rm -rf`
- `git push --force` / `git push -f`
- `DROP TABLE` / `TRUNCATE`
- Any command containing `production` combined with a destructive verb
- `git reset --hard`

Implementation: a shell script at `~/.claude/hooks/bash-firewall.sh` that reads the command from stdin JSON, pattern-matches, and exits 1 with a descriptive error message if blocked.

### Hook 2 — ERRORS.md Auto-Prompt (Stop)

Fires when Claude finishes a session (Stop event). Sends a prompt:
> "Review this session. Did any approach fail more than once? If yes, append it to tasks/ERRORS.md (or ~/.claude/ERRORS.md if cross-project) using the standard format before stopping."

### Hook 3 — Session Summary (Stop)

Fires alongside Hook 2 on session end. Sends a prompt:
> "Write a session summary to tasks/MEMORY.md using the standard format: worked on, completed, in progress, decisions, next session priorities."

**Important boundary:** Hooks enforce outputs (what Claude writes at the end). The CLAUDE.md session start ritual enforces inputs (what Claude reads at the start). Both are required for the system to work.

### settings.json hooks structure

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/bash-firewall.sh"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review this session. Did any approach fail more than once? If yes, append it to tasks/ERRORS.md using the ERRORS.md format (## Date — Title / Tried / Worked / Next time). If working cross-project, use ~/.claude/ERRORS.md."
          },
          {
            "type": "prompt",
            "prompt": "Write a session summary to tasks/MEMORY.md (or ~/.claude/MEMORY.md if cross-project): ## [Date] Session — [title] / Worked on / Completed / In progress / Decisions / Next session."
          }
        ]
      }
    ]
  }
}
```

---

## 5. Optimal Workflow: Prompt → Plan → Implement → Test → QA

Every task follows this workflow regardless of size. The plan can be short (a few lines for small tasks) or detailed (full spec for multi-file features), but the sequence never changes.

```
User prompt
    │
    ▼
Read MEMORY.md + ERRORS.md + LEARNINGS.md (session start ritual)
    │
    ▼
Triage: Bug fix or new feature?
    │
    ├── Bug ──► invoke `investigate` skill
    │           • Read ERRORS.md first — skip to what worked if pattern exists
    │           • Find root cause before writing any code
    │           • Document hypothesis before implementing
    │           • Log outcome to ERRORS.md when done
    │
    └── Feature ──► invoke `superpowers:brainstorming`
                    • Explore intent and constraints
                    • Propose 2–3 approaches with tradeoffs
                    • Get direction approved before planning
    │
    ▼
invoke `superpowers:writing-plans`
    • Output: spec in docs/superpowers/specs/YYYY-MM-DD-[topic]-design.md
    • Includes: acceptance criteria, files to touch, test plan
    • You review and approve spec before any code is written
    │
    ▼
invoke `superpowers:executing-plans`
    • One story at a time
    • After each story: lint passes + tests pass + evidence reported
    • Scope gate: if >3 unexpected files need touching, stop and surface it
    │
    ▼
invoke `superpowers:verification-before-completion`
    • Every acceptance criterion checked against actual output
    • No "done" declaration without this step
    │
    ▼
invoke `qa` skill
    • Edge cases, regressions, visual QA for UI changes
    │
    ▼
Session end trigger
    • MEMORY.md updated
    • ERRORS.md updated (if anything failed)
    • LEARNINGS.md updated (if something worked especially well)
```

### Workflow Rules

- The `investigate` skill is always invoked for bugs — never skip to implementation
- The spec is always approved by the user before implementation begins
- "Done" requires evidence: lint pass, test pass, or QA report
- If a fix is attempted and the issue persists, the approach is logged to ERRORS.md immediately — not at session end

---

## 6. Specialized Subagents

Stored in `~/.claude/agents/`. These are invoked automatically by the workflow skills.

### `investigator.md`

```markdown
---
name: investigator
model: sonnet
tools: Read, Grep, Glob, Bash
---

You are a systematic debugger. Your only job is to find root causes.

Before doing anything:
1. Read tasks/ERRORS.md — if this failure pattern exists, skip to what worked last time
2. State what you already know from ERRORS.md before starting investigation

Investigation rules:
- State your root cause hypothesis before writing any code
- Rule out at least 2 alternative causes before committing to a hypothesis
- Never propose a fix that appears in ERRORS.md as already-failed
- If you implement a fix and the issue persists, log it to ERRORS.md immediately

When done:
- Append outcome to tasks/ERRORS.md whether the fix succeeded or failed
- If succeeded: log what worked and why under "Worked"
- If failed: log what was tried and why it didn't work under "Tried"
```

### `code-reviewer.md`

```markdown
---
name: code-reviewer
model: sonnet
tools: Read, Grep, Glob
---

You are a read-only code reviewer. You cannot edit files.

Review checklist for every task:
1. Scope: Did the implementation touch files outside the stated scope?
2. Spec match: Does the output match every acceptance criterion in the spec?
3. Bugs: Are there edge cases, null checks, or error paths missing?
4. Regressions: Does anything changed here break an existing flow?
5. Security: Any hardcoded secrets, SQL injection risk, or exposed internals?

Output format:
- PASS / FAIL per checklist item
- One sentence per finding
- If FAIL on any item: list specific file and line number
- Never suggest refactoring outside the current task scope
```

---

## Implementation Plan (high level)

This spec is implemented in the following order to minimize risk:

1. Create `~/.claude/MEMORY.md`, `ERRORS.md`, `LEARNINGS.md` with headers and format templates
2. Create `~/.claude/agents/investigator.md` and `code-reviewer.md`
3. Create `~/.claude/hooks/bash-firewall.sh`
4. Update `~/.claude/settings.json` with hooks
5. Update `~/.claude/CLAUDE.md` with the 4 new blocks
6. Create `tasks/MEMORY.md` and `tasks/ERRORS.md` in RunSmart
7. Create `tasks/MEMORY.md` and `tasks/ERRORS.md` in ResumeBuilder
8. Create per-project `.claude/settings.json` and `.claude/hooks/` in each project

Each step is independently testable. Steps 1–3 have zero risk (new files). Steps 4–5 have low risk (config changes). Steps 6–8 are purely additive.

---

## Out of Scope

- Vector database / RAG memory (overkill for solo founder at current scale)
- Claude.ai web app Projects / custom instructions (CLI focus)
- Modular `.claude/rules/` per-project (can be added later if CLAUDE.md grows unwieldy)
- Scheduled routines / cron jobs (future phase)
- The 4-file context architecture (identity/audience/standards/project) for dynamic loading (future phase)
