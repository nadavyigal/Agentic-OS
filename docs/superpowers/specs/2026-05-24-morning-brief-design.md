# Design: Morning Brief Prompt
**Date:** 2026-05-24
**Status:** Approved

## Problem
Nadav stops work mid-session without time for session-end rituals across multiple projects. Next morning: no clear picture of where each project stands, what was left mid-flight, or what to work on first.

## Solution
A prompt file at `PROMPTS/morning-brief.md` that Claude reads and executes when asked for a morning brief. Reads 5 source types per project (git log, tasks/MEMORY.md, tasks/todo.md, docs/agent-os/project-context.md, plus Agentic OS dashboard), synthesizes into 5 output sections delivered in chat.

## Design Decisions

| Decision | Choice | Reason |
|---|---|---|
| Output destination | Chat only, no file writes | Simpler; no maintenance burden |
| Storage location | `PROMPTS/` directory | Fits existing Agentic OS pattern; consistent with other prompts |
| Git window | 96 hours | Catches work across a weekend, not just 24h |
| Read strategy | All projects in parallel | Speed; Claude handles parallel reads naturally |
| Output sections | 5 fixed sections | Consistent enough to scan quickly each morning |

## Output Sections

1. **Header** — date + one-line overall status
2. **What You Left Off** — retroactive session close per project (from git + memory + todo)
3. **Current State vs Plan** — phase, active story, progress %, gap
4. **Blockers & Decisions Needed** — only real blockers, not hypothetical risks
5. **Today's Action Plan** — 2-3 specific actions per project + time-limited recommendation

## Projects Covered

- RunSmart Web (`/Users/nadavyigal/Documents/RunSmart`)
- RunSmart iOS (`/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`)
- ResumeBuilder AI (`/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`)
- ResumeBuilder iOS (`/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`)
- Agentic OS (cross-project context only)

## Files Created

- `PROMPTS/morning-brief.md` — the deliverable
- `docs/superpowers/specs/2026-05-24-morning-brief-design.md` — this file

## Invocation

Open Agentic OS in Claude Code. Type "morning brief" (or "give me my morning brief").
