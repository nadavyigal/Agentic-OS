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

## 2026-07-10: Model Routing Refresh For The July 2026 Lineup

Decision: Update the model-routing policy to the July 2026 model lineup (GPT-5.6 Sol/Terra/Luna, Claude Fable 5 / Opus 4.8 / Sonnet 5 / Haiku 4.5, Grok 4.5, Cursor Composer 2.5) and make every work packet carry an explicit model recommendation. The router stays what it has always been for this OS — a markdown policy plus subagent `model:` frontmatter plus a per-packet Model route field. We deliberately did **not** build the routing software system (scoring engine, feature flags, shadow mode, observability, eval harness) proposed in the source research's "Codex implementation brief"; that is over-engineered for a solo-founder markdown OS.

Reason: Anthropic, OpenAI, xAI, and Cursor all shipped new models within days of each other (2026-07-08/09). The prior routing table was Claude-only, used a stale Sonnet ID (`claude-sonnet-4-6`), and had no place for Codex GPT-5.6 or Composer as first-class cost-optimized executors. The founder wants each WP/task to name the model that should run it so routing is a decision made at packet-authoring time, not improvised per session.

Impact:

- `GLOBAL-TOOL-USAGE.md` "Model routing" rewritten: July 2026 lineup table, a task→primary→reviewer matrix, a 0–10+ risk-score escalation ladder with auto-escalate triggers, and a cross-vendor review rule (implementer ≠ reviewer vendor for high-risk changes). Grok 4.5 is listed as optional ("only if wired into the harness") since it is not currently in the toolchain.
- `executive-os/templates/work-packet-template.md` now has a required **Model route** field; multi-story packets use a per-story Model route column (WP-40 is the reference pattern).
- Subagent `model:` frontmatter refreshed to current IDs in RunSmart and ResumeBuilder (`claude-sonnet-4-6` → `claude-sonnet-5`; Opus already `claude-opus-4-8`, Haiku already `claude-haiku-4-5-20251001`). Role→tier mapping unchanged — only stale IDs were updated. Product-repo changes ship as isolated branches + PRs; this Agentic OS change lands on `main` per AGENTS.md rule 1.
- Source research (ChatGPT capability review) was treated as a draft: model facts adopted, the software-router build rejected, vendor list narrowed to tools actually in use. Prices/benchmarks in the doc are launch-window claims; our own repo evals override them.
- Deeper per-agent re-routing (e.g. promoting `code-reviewer` to Opus, or adding a cross-vendor GPT-5.6 Sol reviewer step) is a separate follow-up, not part of this change.

## 2026-07-10: Model Routing — Tracking, Verified Pricing, Tool-Agnostic Git (follow-up)

Decision: Extend the same-day routing refresh with three things the founder asked for: (1) surface the whole model lineup, pricing, routing and real spend on Portfolio HQ; (2) treat model selection explicitly as a recommendation, not a rule; (3) make the git workflow (commit / push / open PR / review PR / merge) equally available to Codex and Cursor, not Claude Code only. Also fixed a real cost-tracking bug found in passing.

Reason: Routing that lives only in a markdown doc is easy to forget; putting it on the dashboard (with actual spend next to the recommendation) makes it a live operating surface. The founder runs across Claude Code, Codex, and Cursor and wanted it unambiguous that a route names a suggested model but any tool can execute it and do the full git cycle.

Impact:

- New `dashboard/model-registry.json` — machine-readable lineup (10 models, 4 harnesses/utilities, 13-row routing matrix, cross-vendor rule). Single source the dashboard reads; mirrors GLOBAL-TOOL-USAGE.md.
- New Portfolio HQ **Models** tab (`dashboard/portfolio-hq.html` + `scripts/portfolio_hq/refresh_portfolio_hq.py`): utilities, the lineup + verified pricing, the routing matrix, and "where the money actually went" (spend by tool + by Claude model family from `usage.json`). Rendered and verified in-browser.
- **Cost-tracking bug fixed:** `scripts/usage/collect_usage.py` priced Opus at the Claude-3-era $15/$75; Opus 4.x is $5/$25. That inflated the Opus cost line ~3x (most of the dashboard total). Corrected to $5/$25 (+ cache rates) and re-ran the collector — 30-day Claude Code spend now reads ~$4.4k (opus $2.36k / sonnet $2.0k), not the old ~$8.6k. Prior cost figures in memory/notes were overstated for that reason.
- Pricing independently verified 2026-07-10 (Claude via claude-api skill; GPT-5.6 / Grok 4.5 / Composer 2.5 via web search) — every figure in the source draft confirmed, nothing corrected.
- GLOBAL-TOOL-USAGE.md now states routes are "a recommendation, not a rule" and lists model-registry.json as the fourth router surface. AGENTS.md now states the git workflow is tool-agnostic (Claude Code / Codex / Cursor may all commit, push, PR, review, merge), with cross-vendor review for high-risk changes.

## 2026-07-12: Resumely iOS — Remove the Pre-Optimization Fit Gate

Decision: When an iOS user has already supplied a resume plus a job link or job description and taps Analyze, start the existing optimization flow directly. Do not present `FitCheckView`, ask for the job input again, require a second "Check Fit" tap, or make a low pre-optimization score a decision gate. Compute trustworthy fit guidance in the background and surface it inside the resulting diagnosis/optimization experience. If job extraction is unreliable, recover inline on the original input screen by asking for the missing job description; do not manufacture a score.

Reason: The current Fit-First screen repeats intent the user already expressed and adds a network call, a second CTA, and a discouraging exit immediately before the product's core value. The 2026-07-12 score audit also found that the displayed number is the general ATS composite rather than a dedicated job-fit score: 31 of 47 stored rows over 60 days were below 50, no row reached the locked Strong threshold of 75, and the screenshot's 25 was reduced by resume-hygiene factors and penalties despite semantic relevance of 68. PostHog's 17 recorded iOS Fit Check completions were all internal tests, so the old thresholds are not validated on an organic iOS cohort.

Impact:

- This supersedes the 2026-06-23 Fit-First decision only for the authenticated iOS activation path and its pre-optimization `Strong / Stretch / Skip` gate. The public web checker may continue using `/api/public/ats-check` while its scoring contract is repaired.
- Remove `FitCheckView` from Home/Tailor routing and deprecate `fit_check_optimize_tapped`; preserve the user's existing resume and job inputs through the direct optimize call.
- Do not show a numeric fit score or hard verdict when extraction confidence is low or before the dedicated fit score is calibrated.
- Keep the current general Resumely Match/ATS-readiness score for post-optimization guidance, but separate it from a future job-only fit score.
- Success is measured against `job_added -> optimization_started -> optimization_completed -> export_success`, supporting the existing 20% founder-excluded launch-to-export activation target.
- Execution plan: `executive-os/work-packets/WP-45-resumely-direct-optimize-and-score-calibration.md`.

## 2026-07-15: Morning Reads EOD And Active Worktrees

Decision: Extend the Dashboard Trust Rule so `./agentic-os morning` reads the previous Builder OS EOD handoff and selects the freshest validated task status and saved plans across every active product worktree, while leaving product primary checkouts untouched.

Reason: Product implementation deliberately runs in isolated worktrees. Reading only the primary checkout made completed FTUX stories and plans invisible until merge, while the EOD note could record the work without feeding it back into Portfolio HQ.

Impact:

- EOD git evidence scans all refs, so commits made on worktree branches appear in the evening close.
- Morning surfaces the latest EOD Moved / Didn't / Carry handoff as dated evidence.
- Task status chooses the freshest dated source across the primary checkout and active worktrees, with the selected branch labeled in Portfolio HQ.
- Saved-plan discovery includes active worktrees and `docs/specs/drafts/`, de-duplicated by plan path and title.
- Portfolio HQ keeps founder-excluded mature D7 numbers as the decision snapshot and provides authenticated PostHog links as differently-windowed operational drill-downs.

## 2026-07-15: Resumely FTUX Releases B Then C As One Push

Decision: After Release A shipped to App Store Connect as 1.4.2 (12), Resumely continues straight through **Release B (Stories 7-10)** and then **Release C (Stories 11-13)** as a single FTUX push, in that order. Release B is the active lane; Release C is queued behind it, not skipped and not started early.

Reason: The founder initially named Release C's three items (localization/accessibility, second-job loop, release-candidate journey audit) as "the 2nd release" — those are Stories 11-13, while the plan's second release is B. On clarification the founder chose both, in plan order. Release B is the half that attacks the measured D7 wall (guest context lost at auth, duplicated Fit work, missing canonical activation instrumentation); Release C is reach and retention polish, which is lower value while D7 activation reads 0/73.

Impact:

- Active lane is Release B, Stories 7-10, in order, per `docs/specs/drafts/release-b-initiation-prompt.md`.
- **Story 9 stays hard-blocked** until the backend recommendation-evidence metadata contract has a named owner, schema, delivery plan and fallback. Do not start it on the assumption the contract will land.
- Release B branches from the Release A merge point once Release A lands on `main` — see the separate defect below.
- Release C (Stories 11-13) is queued, not cancelled.

## 2026-07-15: Artifacts Are Indexed With Their Storage State

Decision: Portfolio HQ carries an **Artifacts** tab indexing durable artifacts across Builder OS, Agentic OS and the product repos. Each entry records its real storage state — `on main`, `branch-only`, or `local-only` — which is storage truth, not a quality rating. The registry lives in `dashboard/portfolio-hq-manual.json` and is **never** included in any hosted site payload, because every entry names a branch and a local path that the payload contract forbids (enforced by `test_artifact_registry_is_never_hosted`).

Reason: Both first-time-user journey audits — the evidence base for all 13 Resumely stories and all three RunSmart work packets — were invisible from `main`. The Resumely one was untracked in **every** branch and existed only on one disk; any `git clean -fd` would have destroyed it (rescued 2026-07-15, ResumeBuilder-IOS-APP PR #96). A dashboard link to an untracked file protects nothing, so the index has to state where the file actually lives.

Impact:

- 9 of 19 registered artifacts are not on `main` as of 2026-07-15.
- Treat `branch-only` as one branch-cleanup away from invisible; re-verify links after any cleanup.
- **Related defect to fix:** Resumely 1.4.2 (12) was submitted to Apple from `codex/first-time-journey-release-a`. `origin/main` has neither Stories 1-6 nor the version bump, so main cannot rebuild the shipped binary. Resumely `tasks/progress.md` also still reads "ASC archive attempt BLOCKED (2026-07-15)", contradicting the founder's submission statement — Apple-state changes leave no commit, so the repo record cannot self-correct.
