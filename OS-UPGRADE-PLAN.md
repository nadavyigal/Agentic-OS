# Agentic OS Top-Tier Plan

Created: 2026-06-02

The jump from "good" to "top tier" is not more files. It is making the system more
**truthful** (status matches the repo), **current** (status reflects today, not a past
refresh), and **operational** (the dashboard drives action, not just reading). This plan
builds on the task-file parser and source-confidence work shipped on 2026-06-02.

Each phase is independently shippable, one story at a time, with verification.

## Phase 0 - Source-backed status (DONE 2026-06-02)

Shipped: local task-file parser in `scripts/agentic_os/cli.py`; per-project `taskParse`
block and `sourceConfidence` (High/Medium/Low/Unknown); confidence columns in
`PROJECT-STATUS.md`, `DASHBOARD.md`, `executive-os/EXECUTIVE-DASHBOARD.md`; the Dashboard
Trust Rule in `DECISIONS.md`. This is the foundation every later phase depends on.

## Phase 1 - Freshness and staleness enforcement (DONE 2026-06-02)

Problem: `status.json.metadata.freshnessRule` defined fresh/needsReview/stale/unknown but
nothing computed it. Status could be confidently wrong because it was old.

Shipped:
- `compute_freshness` derives a per-project freshness label (Fresh <= 2d, Needs Review <= 7d,
  Stale > 7d, Unknown when no date) from the newest of parsed `lastUpdated` and the last git
  commit date; set on `projectHealth[].freshness` and `freshestDate`.
- Stale evidence downgrades `sourceConfidence` one level (High->Medium->Low->Unknown) via
  `CONFIDENCE_DOWNGRADE`, so an old repo cannot keep a High rating.
- `executiveOverview` now carries `staleProjectCount`/`staleProjects` and `lowTrustProjects`;
  `PROJECT-STATUS.md` and `DASHBOARD.md` gained a Freshness column; `verify` validates the
  freshness vocabulary. Boundary cases unit-checked (today/2d/5d/20d/none/newest-wins).

## Phase 2 - Standardize the status schema so Medium becomes High

Problem: RunSmart Web, ResumeBuilder Web, and Agentic OS sit at Medium because they have no
`tasks/progress.md` and no validation block. The ceiling is the input format, not the parser.

Story 2.1: Add `TEMPLATES/progress-template.md` matching the keyed format the parser already
reads best (the Resumely iOS `tasks/progress.md` shape: Status, Current Phase, Active Story,
Last Completed Story, Next Recommended Story, Blockers, Risks, Last Validation, Last Updated).
Story 2.2: Add `STATUS-SCHEMA.md` documenting the exact keys and the validation-evidence
vocabulary the parser scores. Story 2.3: Seed `tasks/progress.md` in the three web/OS repos
(in those repos, not from here) so they can reach High.

## Phase 3 - Validation evidence linking

Problem: "Last Validation" is free text. Top tier proves it.

Story 3.1: Extend the parser to detect and capture structured evidence: test counts
(`53 XCTest + 5 Swift Testing`), build result, and links to `docs/qa/*` files. Surface as
`taskParse.evidence` with an `evidenceDate`. Story 3.2: Flag "evidence older than the last
commit" as a trust gap (code moved since the last proof). Verify: a repo whose last commit
post-dates its validation shows the gap.

## Phase 4 - Drift detection (truthful)

Problem: Curated `summary` / `dailyRunResult` narrative can silently contradict parsed High
status. Today they coexist; top tier flags the contradiction.

Story 4.1: After refresh, diff the curated `summary.bestNextAction` against each High-confidence
`taskParse.nextRecommendedStory`. When they disagree, emit a `driftWarnings` list and print it
in the refresh output. Story 4.2: Add a `verify` check that fails if a project is High
confidence but its curated narrative was hand-edited to something the parser does not support.

## Phase 5 - Operational: confidence-gated delegation

Problem: The agent queue and project prompts treat all projects equally regardless of trust.

Story 5.1: In `build_project_prompts`, inject a confidence preamble: Low/Unknown prompts must
start by re-reading the local repo before acting; High prompts can proceed from parsed state.
Story 5.2: Build `decisionBoard` and an Open Questions panel from parsed `decisionsNeeded` and
`openQuestions` instead of hand-maintained lists, so decisions come from the repos.

## Phase 6 - Make the pipeline itself trustworthy

Problem: The refresh script has no tests. A parser regression would silently corrupt status.

Story 6.1: Add `scripts/agentic_os/test_cli.py` (stdlib `unittest`) with fixtures for the three
real shapes: progress.md present, derived (todo + session-log), and missing path. Assert
confidence, preferred source, and key fields. Story 6.2: Add a `./agentic-os test` subcommand
and run it inside `verify`. Story 6.3: Optional pre-commit hook that runs `./agentic-os refresh
--no-serve` and fails on dirty drift so committed status is always current.

## Operating principles for this plan

- One story at a time; lint/compile + `./agentic-os verify` green before "done".
- Never invent status. When a source is missing, lower confidence and say what is missing.
- Do not edit product repos from here. Schema seeding (Phase 2.3) happens inside each repo.
- Keep `dashboard/status.json` the single contract; HTML and markdown stay generated from it.
