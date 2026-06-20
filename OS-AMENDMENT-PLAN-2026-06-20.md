# OS Amendment Plan — One Home Per Data Type

**Date:** 2026-06-20
**Author:** Nadav (with Claude)
**Status:** Proposed — not yet executed
**Goal:** Collapse Agentic OS from an accreted multi-silo system into one slim Company OS with a hard line between what is *generated*, *written*, and *invisible*.

---

## Why (evidence from week of 2026-06-13)

- **75% feeding:** 12 of 16 Agentic OS commits last week were "refresh dashboard." Six refreshes on 2026-06-18 alone.
- **8 status surfaces:** DASHBOARD.md, PROJECT-STATUS.md, status.json, + 6 dashboard HTML files, + 2 executive/distribution dashboards.
- **3 nested mini-OSes:** executive-os, distribution-os, clarity-funnel — each re-implements dashboard/decisions/lessons/review/metrics.
- **Decisions in 4 homes, reviews in 4 homes** — across Agentic OS and the vault. No single source, so none is trusted.

Net: the leverage layer spends most of its energy maintaining itself, and duplicates the vault. Result: it gets skipped.

---

## The Hard Line (the one rule)

Every artifact is exactly one of three kinds, and that kind decides where it lives and who touches it:

| Kind | Definition | Who edits | Home |
|---|---|---|---|
| **GENERATED** | Machine state. Derived from git + repo files. | Nobody by hand — the CLI/brief writes it | `Agentic OS/state/` |
| **WRITTEN** | Human judgment: decisions, lessons, backlog. Terse, durable. | You, rarely | `Agentic OS/` (record) + vault (narrative) |
| **INVISIBLE** | Set-once infra: rules, skills, prompts, templates, CLI. | You, almost never | `Agentic OS/rules,skills,prompts,templates` |

**Rule to pin at top of README:**
> Machine state is GENERATED, never written by hand. Thinking is WRITTEN in the vault, never duplicated into the OS. Infra is INVISIBLE — set once. If you are about to create a second dashboard or a third decisions file, stop.

---

## Target Structure

```
PROJECT LAYER       repos (RunSmart, ResumeBuilder, iOS) — untouched

COMPANY OS  (Agentic OS, slimmed)
  state/            GENERATED  → status.json (canonical) + current-focus.md. Read-only.
  DECISIONS.md      WRITTEN    → one-line records; each links to vault narrative
  BACKLOG.md        WRITTEN    → single backlog
  LESSONS.md        WRITTEN    → single lessons log
  rules/            INVISIBLE  → consolidated GLOBAL-* + role lenses (CEO/CFO/COO/RISK)
  skills/           INVISIBLE  → all skills merged
  prompts/          INVISIBLE  → review + role prompts
  templates/        INVISIBLE  → all templates
  agentic-os, scripts/  INVISIBLE → CLI + generators
  archive/          dead silos parked, reversible

AGENT CAPABILITIES  skills + MCP + CLI — invisible infra, lives with Claude config

BUILDER OS VAULT    human thinking — weekly reviews, decision *narrative*, synthesis
```

**Data-type → single home map:**

| Data type | Kind | ONE home | Absorbs / deletes |
|---|---|---|---|
| Status / metrics | GENERATED | `state/status.json` (+ one rendered `index.html` derived from it) | DASHBOARD.md, PROJECT-STATUS.md, EXECUTIVE-DASHBOARD.md, EXECUTIVE-METRICS.md, distribution metrics-dashboard.md + command-center.md, 5 of 6 dashboard HTMLs |
| Decision record | WRITTEN | `DECISIONS.md` | EXECUTIVE-DECISIONS.md |
| Decision narrative | WRITTEN | vault `05-Decisions/` | — (OS keeps only the one-line record + link) |
| Weekly review | WRITTEN | vault `07-Weekly-Reviews/` | COO-LATEST-REVIEW.md, WEEKLY-CEO-LATEST.md, weekly-growth-review.md, PROJECT-BRIDGES/exec-reviews |
| Lessons | WRITTEN | `LESSONS.md` (+ per-repo tasks/lessons.md) | EXECUTIVE-LESSONS.md, distribution lessons.md |
| Backlog / next moves | WRITTEN | `BACKLOG.md` | EXECUTIVE-BACKLOG.md, NEXT-MOVES.md, channel-backlog.md, work-packets |
| Rules / standards / taste | INVISIBLE | `rules/` | GLOBAL-AGENT-RULES, GLOBAL-QA-RULES, GLOBAL-SELF-IMPROVEMENT, GLOBAL-STANDARDS, GLOBAL-TASTE, GLOBAL-WORKFLOWS, operating-principles.md, per-OS AGENTS/CLAUDE/CURSOR.md |
| Role lenses (CEO/CFO/COO/RISK/ANALYSIS) | INVISIBLE | `rules/roles/` | CEO-OS, CFO-OS, COO-OS, RISK-OS, ANALYSIS-OS.md |
| Skills | INVISIBLE | `skills/` | SKILLS/, marketingskills/, distribution-os/skills, clarity-funnel SKILL.md |
| Prompts | INVISIBLE | `prompts/` | PROMPTS/, distribution-os/prompts |
| Templates | INVISIBLE | `templates/` | TEMPLATES/, per-OS templates |

---

## Phased Migration (reversible, lowest-risk first)

Each phase: a git branch, an explicit move-list, a verification step, and a one-command rollback (`git checkout main -- .` / delete branch). Nothing is `rm`'d — everything dead goes to `archive/` so it's recoverable.

### Phase 0 — Safety net (5 min)
- `git -C "Agentic OS" checkout -b os-amend-2026-06-20`
- Confirm clean tree, tag current state: `git tag pre-amend-2026-06-20`.
- **Verify:** `git status` clean, tag exists.

### Phase 1 — Kill the dashboard treadmill (solves issue #2: feeding)
This is the highest-leverage cut. Do it first and live with it for a week before anything else.
- Designate `state/status.json` as the **only** canonical status surface. `mkdir state`, `git mv dashboard/status.json state/status.json`.
- Keep one rendered view: `git mv dashboard/index.html state/index.html`, rewire it to read `state/status.json`. Move the other 5 HTMLs (command-center, data-flow, executive, orchestration, project-status) to `archive/dashboard/`.
- Archive the prose dashboards: `DASHBOARD.md`, `PROJECT-STATUS.md` → `archive/`. Leave a 2-line stub in each pointing to `state/`.
- Update `scripts/daily-refresh.sh` and the morning-brief skill to write only `state/status.json`.
- **Stop committing "refresh dashboard."** Status is generated on demand by the brief.
- **Verify:** run the morning brief → it produces status from `state/status.json` with no hand-editing. Grep confirms nothing else writes a status file.
- **Live with it one week.** If the skip-instinct fades, continue. If not, stop and re-diagnose.

### Phase 2 — One decisions home, vault holds the narrative (solves issue #1: duplication)
- Merge `executive-os/EXECUTIVE-DECISIONS.md` entries into root `DECISIONS.md` as one-line records (what / when / reversible y-n / link).
- For each decision with real reasoning, the *narrative* lives in vault `05-Decisions/`; the OS record links to it. No reasoning duplicated in the OS.
- Archive `EXECUTIVE-DECISIONS.md`.
- **Verify:** exactly one DECISIONS.md in the repo (`find . -iname "*decision*" -not -path "*/archive/*"` returns only root + template). Each record links out or is self-contained.

### Phase 3 — Reviews live only in the vault (solves issue #1)
- Move the latest content of `COO-LATEST-REVIEW.md`, `WEEKLY-CEO-LATEST.md`, `distribution-os/weekly-growth-review.md`, `PROJECT-BRIDGES/exec-reviews` into vault `07-Weekly-Reviews/` (one note per review, dated).
- Replace each in the OS with a one-line pointer to the vault, then archive the originals.
- **Verify:** Agentic OS holds zero review bodies; vault `07-Weekly-Reviews/` is the only review home.

### Phase 4 — Consolidate WRITTEN logs (backlog + lessons)
- Merge `EXECUTIVE-BACKLOG.md`, `NEXT-MOVES.md`, `channel-backlog.md`, work-packets → `BACKLOG.md` (sectioned by area).
- Merge `EXECUTIVE-LESSONS.md`, `distribution-os/lessons.md` → `LESSONS.md`.
- Archive the absorbed files.
- **Verify:** one BACKLOG.md, one LESSONS.md outside archive.

### Phase 5 — Fold INVISIBLE infra into 4 folders
- `mkdir rules skills prompts templates` (skills/prompts/templates may already exist — merge into them).
- Move GLOBAL-*.md + operating-principles.md + per-OS AGENTS/CLAUDE/CURSOR.md → `rules/`.
- Move CEO/CFO/COO/RISK/ANALYSIS-OS.md → `rules/roles/`.
- Merge marketingskills/, distribution-os/skills, clarity-funnel SKILL.md → `skills/`.
- Merge PROMPTS/ + distribution-os/prompts → `prompts/`; TEMPLATES/ + per-OS templates → `templates/`.
- **Verify:** root has at most ~8 markdown files + 4 infra folders + state/ + archive/. `ls *.md` count drops from ~23 to ≤8.

### Phase 6 — Retire the mini-OS shells
- `executive-os/`, `distribution-os/`, `clarity-funnel/` are now emptied of unique content. Move the shells to `archive/`.
- Update root `README.md` with the new map + the Hard Line rule. Update `CLAUDE.md`, `AGENTS.md` to point at the new homes.
- Update `PROJECT-PATHS.md` / any skill that referenced moved paths.
- **Verify:** grep the repo + the morning-brief/sync skills for old paths (`executive-os`, `distribution-os`, `DASHBOARD.md`, `PROJECT-STATUS.md`) → zero live references outside `archive/`.

### Phase 7 — Land it
- Run the morning brief end-to-end one more time. It must produce status, find decisions, and find the latest review (in the vault) with no errors.
- Commit per phase (already done) and open a PR: "Amend OS — one home per data type."
- Two-week archive check: if nothing in `archive/` was reached for, delete it in a follow-up.

---

## Definition of Done

- [ ] One status surface (`state/status.json`), generated, never hand-edited. Zero "refresh dashboard" commits in the following week.
- [ ] One DECISIONS.md; reasoning narrative only in vault `05-Decisions/`.
- [ ] Reviews only in vault `07-Weekly-Reviews/`; OS holds pointers.
- [ ] One BACKLOG.md, one LESSONS.md.
- [ ] Root ≤8 markdown files + 4 infra folders (rules/skills/prompts/templates) + state/ + archive/.
- [ ] Morning brief runs green against the new layout.
- [ ] README carries the Hard Line rule.

## Rollback
Any phase: `git checkout main -- .` then delete the branch, or `git reset --hard pre-amend-2026-06-20`. Nothing deleted, all dead content in `archive/`.

## Open questions for Nadav
1. Keep one rendered `index.html` view, or kill all HTML and rely purely on the text morning brief?
2. Role lenses (CEO/CFO/COO/RISK) — keep as prompts you invoke, or are any of them actually dead?
3. The TCC-blocked launchd auto-refresh: revive it once status is single-source, or stay manual-on-demand?
