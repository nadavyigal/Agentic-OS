# Agentic OS — User Manual

Last updated: 2026-06-02

---

## The one-command daily workflow

```bash
cd "/Users/nadavyigal/Documents/Projects /Agentic OS"
./agentic-os morning
```

That single command: runs the unit tests, parses the local project repos, refreshes all
dashboards, verifies everything, and opens the Command Center in your browser at
`http://127.0.0.1:8787/index.html`.

**Run it once a day, or any time you want a fresh picture of where things stand.**

---

## The four commands

| Command | What it does | When to use |
|---|---|---|
| `./agentic-os morning` | refresh + verify + open browser | Start of day |
| `./agentic-os refresh` | update all status files, no browser | Mid-session status update |
| `./agentic-os verify` | check JSON, sync, links, tests, whitespace | Before committing anything |
| `./agentic-os test` | run the 18-test parser suite (verbose) | After editing `cli.py` |

---

## Reading the dashboard

### Source confidence — the most important column

Every project is rated on how trustworthy its status is:

| Rating | Meaning | What to do |
|---|---|---|
| **High** | Local task file parsed + validation evidence found | Trust it; still confirm specifics in the repo |
| **Medium** | Parsed but validation is unclear | Verify in the repo before acting |
| **Low** | No task files; narrative only | Re-read the repo before doing anything |
| **Unknown** | No path or no files at all | Confirm the path, then re-read |

**Right now:** Resumely iOS and RunSmart iOS are High. RunSmart Web, ResumeBuilder Web, and
Agentic OS are Medium (they have no `tasks/progress.md` — see below to fix this).

### Freshness

Freshness is the age of the newest signal (parsed `Last Updated` or last git commit):

- **Fresh** — updated in the last 2 days
- **Needs Review** — 3–7 days old
- **Stale** — older than 7 days → confidence is automatically downgraded one level

If a project goes Stale, its status is still shown but the confidence drops. You don't need
to do anything — the next `./agentic-os refresh` after you work in that repo will update it.

### Evidence gaps

An evidence gap means code was committed after the last recorded validation.  
It appears in the `## Evidence Gaps` section of `PROJECT-STATUS.md`.  
To clear it: re-run your validation (build/tests/QA) and update `Last Validation` in
`tasks/progress.md` with a date at or after the latest commit.

### Drift warnings

Drift warnings appear when a project's curated narrative in `dashboard/status.json` disagrees
with what the parser read from the repo. They're **informational** — the dashboard still works.  
To clear one: update the curated field in `dashboard/status.json` to match the repo, or
consciously leave the narrative if it's intentionally different.

---

## How the parser decides what to trust

For each project, `./agentic-os refresh` reads (in preference order):

1. `tasks/progress.md` — structured `Key: Value` format, best source
2. `tasks/todo.md` + latest `tasks/session-log.md` + `tasks/MEMORY.md` — derived when no `progress.md`
3. `tasks/ERRORS.md`, `tasks/lessons.md` — for blockers and decisions
4. Nothing → **Unknown** confidence; the project entry notes what is missing

---

## How to make a project reach High confidence

A project reaches High when it has a `tasks/progress.md` with:
- A `Current Phase` line
- A `Next Recommended Story` line
- A `Last Validation` line with evidence words (`passed`, `succeeded`, `verified`, etc.)
- A `Last Updated: YYYY-MM-DD` within the last 7 days

Copy `TEMPLATES/progress-template.md` into the project's `tasks/` folder and fill in the
keyed block. The full key list and validation vocabulary are in `STATUS-SCHEMA.md`.

**Three projects are currently Medium because they have no `tasks/progress.md`:**
- RunSmart Web (`/Users/nadavyigal/Documents/RunSmart/tasks/`)
- ResumeBuilder Web (`/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-/tasks/`)
- Agentic OS (will flip to High after PR #6 is merged and you `git pull` the canonical checkout)

---

## Using the generated project prompts

The dashboard generates a ready-to-paste agent prompt for each project. Find them in:

- `dashboard/status.json` → `projectPrompts[]` → `copyPrompt`
- The Command Center HTML dashboard → project card → copy prompt button

Each prompt opens with a **trust directive** based on source confidence:
- **High:** the agent may proceed from the parsed state
- **Medium:** the agent must verify in the repo first
- **Low/Unknown:** the agent must re-read the repo before doing anything

Paste the prompt into Claude Code inside the relevant product repo.

---

## Surfacing decisions and open questions from repos

Add a `## Decisions Needed` or `## Open Questions` section with bullet items to any task file
(e.g. `tasks/progress.md`). After the next `./agentic-os refresh`, they appear in the
`## Open Questions & Decisions (from repos)` section of `PROJECT-STATUS.md`.

The Agentic OS `tasks/progress.md` already has two real open decisions logged.

---

## Keeping status current (the minimal discipline)

The system is self-maintaining as long as you:

1. Run `./agentic-os morning` (or `refresh`) when you want a current picture
2. Update `Last Validation` and `Last Updated` in `tasks/progress.md` after a significant
   validation (build pass, QA run, smoke test)
3. Update `Active Story` and `Next Recommended Story` when the work shifts

That is the full ongoing commitment. Nothing else needs manual maintenance.

---

## Files changed by `./agentic-os refresh`

All of these are generated — do not hand-edit them:

| File | What it contains |
|---|---|
| `dashboard/status.json` | The single source-of-truth contract |
| `PROJECT-STATUS.md` | Human-readable status table |
| `DASHBOARD.md` | Portfolio dashboard markdown |
| `executive-os/EXECUTIVE-DASHBOARD.md` | Executive summary |
| `dashboard/*.html` | Browser dashboards (served locally) |

Files you should hand-edit when needed:

| File | What it is |
|---|---|
| `DECISIONS.md` | Durable cross-project decisions |
| `LESSONS.md` | Global repeated/expensive lessons |
| `BACKLOG.md` | Cross-project work items |
| `INTENT-LOG.md` | Demand-side request/intent log (audit 2026-06-16) |
| `tasks/progress.md` (in each repo) | Per-project structured status |

---

## Full pipeline at a glance

```
./agentic-os refresh
│
├── parse_project_paths()     reads PROJECT-PATHS.md
├── collect_evidence()        git status/log per repo
├── parse_task_files()        reads tasks/progress.md (preferred)
│                             or derives from todo + session-log + MEMORY
│
├── sourceConfidence          High / Medium / Low / Unknown
├── freshness                 Fresh / Needs Review / Stale / Unknown
│                             Stale downgrades confidence one level
├── extract_evidence()        test counts, build result, QA docs, evidenceDate
├── evidenceGap               commit newer than evidenceDate?
├── compute_drift_warnings()  curated narrative vs parsed source (High only)
├── openQuestionsBoard        from ## Open Questions sections in task files
├── repoDecisions             from ## Decisions Needed sections in task files
├── confidence_directive()    gates agent prompts by trust level
│
└── writes:  dashboard/status.json
             PROJECT-STATUS.md
             DASHBOARD.md
             executive-os/EXECUTIVE-DASHBOARD.md
             dashboard/*.html (embedded JSON synced)
```

---

## Quick reference: what each confidence level means in practice

When you paste a **High** prompt into Claude Code:  
> The agent can act on the parsed state. It still opens the repo but does not need to re-derive everything from scratch.

When you paste a **Medium** prompt:  
> The agent will say "verify in the repo before acting." That is correct — `tasks/progress.md` is missing or has no validation evidence.

When you see **Low** or **Unknown**:  
> The project path may be wrong, or no task files exist. Fix the path in `PROJECT-PATHS.md` or seed `tasks/progress.md`.
