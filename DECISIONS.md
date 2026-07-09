# Global Decisions

Record durable cross-project decisions here. Use `TEMPLATES/decision-template.md`.

## 2026-05-12: Global OS Is A Reference Layer

Decision: The Global Agentic OS is a lightweight reference library and cross-project command center, not a full project operating system.

Reason: Daily coding should happen inside product repos using their local Agent OS files to avoid token waste and stale duplicated context.

Impact:

- Bridge files connect global strategy to local repos.
- Project-specific implementation docs stay local.
- Agents load this folder selectively.

## 2026-06-01: Vet Third-Party Skills Before Install

Decision: Treat any third-party Claude skill as untrusted until reviewed. A skill runs with our tools and credentials, so it is a supply-chain surface.

Reason: The skills ecosystem is growing fast (see `external-resources/06-claude-skills-ecosystem-map.md`). Convenience installs are a real risk.

Impact:

- Read a skill's source before installing; never paste-install on hype.
- Prefer official (`anthropics/skills`) and already-trusted plugins (superpowers, gstack, vercel, supabase, frontend-design).
- Use gstack `cso` skill supply-chain scanning for periodic review of installed skills.

## 2026-06-02: Dashboard Trust Rule

Decision: Global status must be parsed from local project task files when available. Existing `dashboard/status.json` narratives are fallback context, not proof of current status.

Reason: The refresh previously leaned on curated narrative fields that could drift from reality. Parsing local task files (`tasks/progress.md`, then `tasks/todo.md` + latest `tasks/session-log.md` + `tasks/MEMORY.md`) ties each project's state to source evidence and exposes how trustworthy that state is.

Impact:

- The refresh parses local task files and attaches a `taskParse` block plus a `sourceConfidence` rating (High / Medium / Low / Unknown) to every project.
- `tasks/progress.md` is the preferred status source; when absent, status is derived from todo + latest session-log + MEMORY; when no task files exist, the project is marked Low (narrative only) or Unknown (no source).
- High confidence requires parsed validation evidence (passed build/tests/QA). Without it, confidence caps at Medium.
- `PROJECT-STATUS.md`, `DASHBOARD.md`, and `executive-os/EXECUTIVE-DASHBOARD.md` surface the confidence column so a reader can tell parsed truth from narrative.
- Agents must not treat a narrative-only (Low) status as confirmed; re-read the local repo before acting on it.

## 2026-06-05: Escalation Patterns Stay Optional And Outcome-Led

Decision: Keep normal work-packet execution as the default. Use only three
optional workflow patterns (`parallel-research`, `independent-review`,
`evaluator-loop`), treat input trust as a separate security property, and pilot
one evidence-backed outcome loop before creating more.

Reason: The daily OS is intentionally simple. Additional orchestration is useful
only when it improves research coverage, independent review, measurable revision,
or continuity across a real multi-session business outcome.

Impact:

- `Workflow pattern` does not replace Execution mode.
- Untrusted external content is reduced to structured, source-linked facts before
  it can drive actions; session separation alone is not a security boundary.
- Context extraction remains an on-demand founder interview with an approval gate
  before durable promotion.
- Additional outcome-loop cards require two successful COO reviews of the pilot
  without status duplication.

## 2026-06-20: Resumely ATS Claims — Branded "Match Score", Process Claims Only

Decision: Resumely's score is a self-defined "Resumely Match Score", not a representation of any external ATS vendor's score. All ATS-related copy (App Store metadata, paywall, /ats-checker, public share posts) must be process-descriptive, never outcome-guaranteeing.

Reason: The product computes a numeric "ATS score" (free score -> paid export, the core monetization frame) and substitutes it into public LinkedIn posts via LinkedInShareComposer.swift. Real ATS systems (Workday/Greenhouse/Taleo) are proprietary and do not expose scoring, so "your ATS score" is unverifiable and exposes the app to Apple 2.3.1 (misleading) review risk and FTC unsubstantiated-claims risk.

Impact:

- Allowed: "ATS-friendly formatting", "checks against common ATS parsing rules", "match score vs the job you paste", a branded "Resumely Match Score".
- Forbidden: "your ATS score" as an external number, "guaranteed to pass ATS"/"beat the bots", interview/hire outcome stats, named ATS vendors.
- Pending product work (iOS + web repos): rename in-product "ATS score" label to "Resumely Match Score"; update LinkedInShareComposer.swift share copy; audit App Store metadata (en+he); add "not affiliated with any ATS vendor" microcopy.
- Human-readable record: Nadav Builder OS vault 05-Decisions/2026-06-20-resumely-ats-claim-defensibility.md.

## 2026-06-23: Fit-First Triage — Verdict Thresholds + Resume-Input Contract

Decision: For the Fit-First Triage wedge (WP-12), the verdict band is `≥75 = Strong / 50–74 = Stretch / <50 = Skip`, derived server-side from `score.overall` and kept tunable post-ship. iOS sends the resume to `POST /api/public/ats-check` via the existing **PDF re-upload** contract (no `resume_id` change in Story 0).

Reason: Both are the spec's recommended defaults (PR #73). The 75/50 bands are balanced and server-owned so they retune without a client release once real score distributions are visible. PDF re-upload is the smallest change — zero new server work in Story 0 and no contract break for the live public ATS path; a stored `resume_id` is a later optimization, not a launch blocker.

Impact:

- Story 0 (web `/api/public/ats-check`) implements the additive `fit` block with these exact bands; existing `score`/`preview`/`quickWins`/`checksRemaining` unchanged.
- iOS `FitCheckService` builds against the PDF-upload contract; `resume_id` swap is a flagged follow-up, not in scope for WP-12.
- WP-12 DECISION GATE is now resolved; the build sequence is unblocked.

## 2026-06-23: Fit-First Triage — Flag Flip Deferred to D7 Readout (2026-06-24)

Decision: **Defer** flipping `isFitCheckEnabled` to production until after the D7 Gate A readout on **2026-06-24**. Build **1.1 (6)** ships with the Fit-First code path **dark** (`isFitCheckEnabled=false`). Internal validation used branch `feat/wp-13-fit-check-internal` with the flag ON against the live `/api/public/ats-check` endpoint.

Reason: WP-13 Step 2 internal validation passed cleanly — live endpoint HTTP 200, verdict decode + optimize handoff, all four `fit_check_*` analytics events, Hebrew RTL strings resolved, EXD-012 score note remains process-descriptive. However, `RuntimeFeatures` has no percentage/cohort rollout gate; the practical options are 100% day-one exposure or a timed defer. The D7 activation readout (dashboard 1720819) is already scheduled for 2026-06-24 and is the right gate before turning on a brand-new Tailor front door.

Impact:

- **Public submission:** v1.1 build 6, flag OFF — Fit-First unreachable until a follow-up flip PR merges after D7.
- **Internal soak:** `feat/wp-13-fit-check-internal` (flag ON + live smoke tests) is the internal-only TestFlight candidate; distribute to internal testers only, not App Store review.
- **Flip trigger (2026-06-24):** If D7 Gate A baseline is stable, open a PR flipping `isFitCheckEnabled=true` on `main` for the next build (1.1 build 7 or post-approval build 6 re-release). If D7 shows activation regression or open issues, extend defer and re-evaluate.
- **Not chosen:** Full 100% flip on day one (too much exposure before D7 baseline). Staged percentage rollout (no server-side/client percentage gate exists today).
- Evidence: `docs/qa/reports/wp-13-fit-check-live-smoke-2026-06-23.md` in the iOS repo.

## 2026-07-02: Priority Reset — Resumely Primary, RunSmart Garmin to Maintenance

Decision: ResumeBuilder/Resumely becomes the primary product, with a target of 20% real (founder-excluded) activation — defined as launch → export — within 30 days (by 2026-08-01). RunSmart's Garmin integration drops to pure maintenance: no new Developer Portal applications, no Production re-submission, no relaunch push. RunSmart's core focus shifts explicitly to non-wearable runners (the Phone-Only-Runner persona).

Reason: A same-session cross-layer audit (vault + Agentic OS status + both repos' live git/task state) plus a live PostHog query on both products' real 30-day funnels showed both products at ~0% real activation once measured honestly (founder account excluded). Resumely: 49 reached the app, 2 exported (4% launch-to-export), with the biggest cliff at launch→fit-check-start (63% bounce). RunSmart: 48 reached the app, 3 completed a run (6% launch-to-run), with the biggest cliff at launch→onboarding-start (73% never begin). RunSmart's own activation threshold ("≥20% plan-to-run") was measuring the wrong step — of the 8 users who got a plan, 3 ran (37%, above threshold), but only 8 of 48 ever reached that step. Garmin has consumed disproportionate founder attention (3 Gate-4 brand rejections, a full app deactivation, a "start all over" instruction from Garmin, two new required portal applications) while serving only 5 users (`garmin_sync_completed`, 30d) — a sunk-cost pattern, not a growth lever. Resumely has the shorter, more tractable activation funnel (upload → optimize → export vs. onboard → plan → run → habit) and no active platform-relationship fire.

Impact:

- RunSmart's prior "gets priority over ResumeBuilder in a conflict" default (2026-06-07) is reversed for the duration of this push.
- RunSmart: keep the 5 currently Garmin-synced users working; fix only breakage, do not expand scope. Revisit the Garmin track at day 30 based on Resumely's result.
- Resumely: weekly focus is fixing funnel cliffs in order (launch→fit-check-start, then fit-check-complete→upload, then optimize→export), re-measuring the founder-excluded 30-day funnel weekly against the 20% target.
- Gate A (paywall) on Resumely stays held until the 20% target is hit or clearly abandoned.
- Full plan and reasoning: Nadav Builder OS vault `05-Decisions/2026-07-02-priority-reset-resumely-primary.md`; living pages `RunSmart.md` and `ResumeBuilder.md` updated in place.

## 2026-07-03: Resumely Gate A — Disable Premium CTAs Until Activation Gate Opens

Decision: Choose WP-29 S4 option A. Premium upgrade CTAs must be hidden or disabled while Gate A is closed; do not route signed-in users to Stripe, checkout, or a signup redirect presented as an upgrade. Keep the monetization gate closed until the Resumely activation decision is revisited.

Reason: The signed-in `/pricing` Premium CTA currently creates a silent dead end by redirecting back to `/dashboard`, and wiring real checkout would contradict the 2026-07-02 Gate A hold. A disabled/non-actionable CTA is honest and reversible.

Impact:

- Web implementation should show Premium as unavailable/coming later instead of a clickable upgrade action.
- `/api/upgrade` should not create checkout sessions while the gate is closed.
- Re-opening Premium requires an explicit founder decision updating this gate record and the product code gate.

## 2026-07-09: Founder Queue Clearance — Voice Coach Deferred, Michal Pivots to OpenAI/Codex, Librarian Bot Rejected

Decision: In a founder decision session (three founder-only queue items plus one new OS proposal), the founder made four calls:

1. **RunSmart voice coach — defer, do not flip.** `VOICE_COACH_ENABLED` stays `false`. Review at the 2026-07-12 activation re-read, or after WP-40 (HealthKit activation) lands — whichever gives a clearer read on RunSmart's plan→run wall. This closes a ~1-month-old open loop without flipping.
2. **Michal / AI Audit Toolkit pilot — park, then rebuild on OpenAI/Codex.** Michal is migrating from Gemini to OpenAI. The pilot waits until she completes that move; then she is set up on Codex and we build "Michal's OS" (a Codex-based operating layer for her) rather than the previously-drafted Gemini-Gems path. The existing Gemini Track-C drafts (4 Gems, voice doc, privacy rules) are now superseded as the delivery vehicle, though the underlying audit framing carries over.
3. **RunSmart legal entity (EXD-017/WP-35) — no change.** Keep the existing 2026-07-22 reminder; investigation decision already made, only the accountant call remains and it is not urgent.
4. **"Librarian" auto-updater bot — rejected.** Do not build an autonomous cheap-model routine that edits docs unattended on a schedule.

Reason:

- Voice coach: RunSmart is maintenance-only (2026-07-02 priority reset); its wall is activation (plan→run, 0 runs), not missing features. Flipping an unverified voice feature adds surface area and splits focus; deferring with a real date ends the indecision.
- Michal: the delivery platform changed under the drafted plan. Waiting for her platform migration and rebuilding on Codex avoids shipping onto a stack she's leaving, and aligns her toolkit with the OS's own primary tooling.
- Librarian: the OS's entire value is *trustworthy parsed truth* with confidence ratings and evidence citations (2026-06-02 Dashboard Trust Rule). An unreviewed cheap-model editor running every ~2h introduces exactly the drift/churn that rule exists to prevent; `ERRORS.md` (2026-06-12) already warns against automation nobody reviews and favors attaching checks to a ritual that demonstrably runs (the daily refresh); and macOS TCC blocks scheduled runs on this Mac anyway (see auto-memory `agentic-os-launchd-tcc`). The recommended lighter alternative — a read-only staleness auditor wired into `./agentic-os refresh` — was offered and also declined for now; existing `refresh` + `verify` + morning-brief staleness checks stay the safeguard.

Impact:

- Portfolio HQ founder queue (`dashboard/portfolio-hq-manual.json`) updated: voice-coach + legal-entity items resolved/annotated; the Michal track rewritten to the OpenAI→Codex "Michal's OS" plan; `asOf` bumped.
- Auto-memory `voice-coach-flag-pending` updated from "remind every session" to "deferred with review date 2026-07-12" so it stops nagging.
- No librarian workflow, cron, or autonomous editor is to be added. If the read-only auditor is reconsidered later, it must land as a `refresh`-invoked, edits-nothing check, not a scheduler.
- `status.json` decision board is stale (still references the build-8 era: "if build 8 is rejected", "Resumely device smoke before archive", the old voice-flag framing). Flagged for cleanup in RunSmart iOS / Resumely task files — it is not a portfolio-hq bug.
