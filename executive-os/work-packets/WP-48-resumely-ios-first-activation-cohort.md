# Work Packet

- Status: Ready
- Mode: Grower
- Source: docs/plans/2026-07-19-activation-cliff-fix-plan.md (S2); 2026-07-20 morning brief
- Workflow pattern: normal
- Input trust: trusted
- Success signal: a stated, dated read of the post-1.4.3 cohort — or an explicit "not mature until DATE"
- Model route: Claude Opus (analytics judgment)

## Owner Role
Growth engineer

## Project
Resumely iOS — `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`

## Goal
Read the first real activation cohort produced by 1.4.3, then scope S2 instrumentation for 1.4.4.

## Context
1.4.3 (13) went live 2026-07-19T21:47:02Z. It is the first build that partially fixes the activation cliff (tappable "Sign in to Optimize" + diagnosis persistence across sign-in) **and** the first where saved-resume reuse works at all — the `optimization_id` fix (iOS `c02089e` + backend PR #116) revealed that reuse had never worked in production for any user. WP-46 is closed. The cohort window opened 2026-07-19.

Do not start 1.5.0 engineering before reading what this release actually did.

## Read First
- AGENTS.md, CLAUDE.md
- docs/plans/2026-07-19-activation-cliff-fix-plan.md
- docs/qa/reports/wp46-story10-activation-funnel-2026-07-18.md (the reproducible HogQL)
- tasks/progress.md (top entry: 1.4.3 LIVE)

## Task
1. Confirm in PostHog (project 270848) that the Stories 10-12 events actually fire from a clean 1.4.3 install: `resume_file_selected`, `resume_upload_succeeded`, `optimization_completed`, `export_success`. If they do not fire, stop and report that — everything downstream is void.
2. Read the cohort against the stated rule: **>=20 clean uploaders**, win at **>=30% optimization_started** vs the 12.5% baseline. If the sample is not mature, say so and name the date it will be. Do not read it early.
3. Scope S2 for 1.4.4: `score_screen_signin_tapped`, file-picker outcome events, `job_source` property.

## Constraints
- Analysis and scoping only. No release, no version bump, no ASC action.
- Exclude founder/QA, but per `~/.claude/ERRORS.md` 2026-07-19: list what each excluded person did, and individually re-examine anyone carrying an ERROR or FAILURE event.
- Reconcile against Portfolio HQ before publishing; if they disagree, resolve it rather than assuming the fresh read wins.

## Validation
Content-free HogQL committed to `docs/qa/reports/`, reproducible, with the exact cohort cutoff date stated.

## Completion Gate
Update tasks/todo.md, tasks/progress.md, tasks/session-log.md.

## Final Output
What changed, files changed, commands run, validation evidence, remaining risks, next recommended action.
