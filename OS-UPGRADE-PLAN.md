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

## Phase 2 - Standardize the status schema so Medium becomes High (IN PROGRESS 2026-06-02)

Problem: RunSmart Web, ResumeBuilder Web, and Agentic OS sit at Medium because they have no
`tasks/progress.md` and no validation block. The ceiling is the input format, not the parser.

- Story 2.1 (DONE): `TEMPLATES/progress-template.md` — the keyed format the parser reads best.
- Story 2.2 (DONE): `STATUS-SCHEMA.md` — exact keys, preference order, validation-evidence
  vocabulary, confidence levels, and the freshness/downgrade rule. Registered in the File Map.
- Story 2.3 (PARTIAL): seeded `tasks/progress.md` in the Agentic OS repo (parses to High).
  RunSmart Web and ResumeBuilder Web are product repos and must be seeded inside those repos
  with owner approval, not from here; they stay Medium until a real `Last Validation` is
  recorded there.

## Phase 3 - Validation evidence linking (DONE 2026-06-02)

Problem: "Last Validation" was free text. Top tier proves it.

Shipped:
- Story 3.1: `extract_evidence` captures test counts (`53 XCTest`, `5 Swift Testing`), build
  result, and `docs/` QA links from the validation text, plus an `evidenceDate` (latest date
  in the text, else Last Updated). Surfaced under `taskParse.evidence` and on `projectHealth`.
- Story 3.2: `evidenceGap` flags when the last git commit post-dates `evidenceDate` (code moved
  since the last proof). Listed in the `## Evidence Gaps` section of `PROJECT-STATUS.md` and
  `DASHBOARD.md`, counted in `executiveOverview.evidenceGapCount`, validated in `verify`.
  Confirmed live: Resumely iOS shows a gap (validated 2026-06-01, commit 2026-06-02).

## Phase 4 - Drift detection (DONE 2026-06-02)

Problem: Curated per-project narrative could silently contradict the parsed High-confidence
source. They coexisted; top tier flags the contradiction.

Shipped:
- Story 4.1: `compute_drift_warnings` compares curated `projects[]` fields (currentPhase,
  nextRecommendedStory, lastValidation) against the parsed `taskParse` values for
  High-confidence projects, using `texts_disagree` (normalized, substring-tolerant to avoid
  punctuation noise). Emits `status.driftWarnings` + `executiveOverview.driftWarningCount`,
  printed in the refresh output and shown in a `## Drift Warnings` section of
  `PROJECT-STATUS.md` and `DASHBOARD.md`.
- Story 4.2 (adjusted): `verify` checks `driftWarnings` is well-formed but does **not** hard-fail
  on the presence of drift. Reason: a curated phase is human synthesis that can legitimately
  differ from a parsed session title, so blocking the dashboard on every divergence would be
  wrong. Drift is surfaced for reconciliation, not treated as a build break. A future
  `verify --strict` or a `refresh --reconcile` (Phase 5+) can enforce or auto-heal.
- Confirmed live: 6 warnings across RunSmart iOS and Resumely iOS (curated narrative for both
  High projects had drifted from their repos).

## Phase 5 - Operational: confidence-gated delegation (DONE 2026-06-02)

Problem: The project prompts treated all projects equally regardless of trust, and decisions
were only ever hand-maintained.

Shipped:
- Story 5.1: `confidence_directive` injects a trust preamble into every generated project prompt.
  High may proceed from parsed state; Medium must verify in the repo; Low/Unknown must re-read
  the repo first; an evidence gap adds a re-validate note. Surfaced as
  `projectPrompts[].trustDirective` + `sourceConfidence` and validated in `verify`.
- Story 5.2: `## Open Questions` and `## Decisions Needed` sections in any task file are parsed
  (via `section_bullets`) and aggregated into `status.openQuestionsBoard` / `status.repoDecisions`,
  shown in `PROJECT-STATUS.md` and counted in `executiveOverview`. The curated `decisionBoard` is
  preserved (human synthesis); the repo-sourced board is additive, so decisions can flow up from
  the repos. The loose open-question line scan was dropped after it produced a false positive;
  extraction is section-based. Convention documented in `STATUS-SCHEMA.md` and dogfooded in the
  Agentic OS `tasks/progress.md`.

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
