# Project Paths

Last checked: 2026-06-02 IDT

Canonical local folders for the projects shown on the Agentic OS dashboard. The refresh
pipeline (`scripts/agentic_os/cli.py`) discovers a project only when its row name matches a
known alias and its path cell contains a backtick path, so keep the Name column stable.
Update this file when a repo moves.

## Active Dashboard Projects

| Project | Local Path | Status Source | Notes |
| --- | --- | --- | --- |
| RunSmart iOS | `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app` | `tasks/todo.md`, `tasks/session-log.md`, `tasks/MEMORY.md`, `tasks/lessons.md` | No `tasks/progress.md`; status is derived from todo + latest session-log + MEMORY. |
| ResumeBuilder iOS | `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP` | `tasks/progress.md` (preferred), `tasks/todo.md`, `tasks/session-log.md`, `tasks/MEMORY.md`, `tasks/lessons.md` | Shown as "Resumely iOS". `tasks/progress.md` is the canonical structured status source. |
| RunSmart Web | `/Users/nadavyigal/Documents/RunSmart` | `tasks/MEMORY.md`, `tasks/ERRORS.md`, `tasks/lessons.md` | No `tasks/progress.md` or `tasks/todo.md`; derived status only. Support/backend repo. |
| ResumeBuilder Web | `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-` | `tasks/MEMORY.md`, `tasks/ERRORS.md`, `tasks/lessons.md` | Shown as "ResumeBuilder AI (Web)". No `tasks/progress.md`; derived status only. |
| Global Agentic OS | `/Users/nadavyigal/Documents/Projects /Agentic OS` | `tasks/MEMORY.md` | This dashboard workspace. Shown as "Agentic OS". |

## Conceptual / Path Unknown

| Project | Local Path | Notes |
| --- | --- | --- |
| Atlas | Unknown | Future orchestration layer. No repo path confirmed; stays a curated concept entry with Unknown source confidence until a path exists. |

## Source Confidence Reference

The refresh assigns a confidence to each project based on what it could actually read:

- **High** - a local task file was parsed and validation evidence (passed build/tests/QA) was found.
- **Medium** - a local task file was parsed but validation evidence was unclear.
- **Low** - no local task files were found; only the existing dashboard narrative was available.
- **Unknown** - no reliable source (missing path or no task files and no narrative).
