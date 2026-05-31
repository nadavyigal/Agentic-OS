# Executive Backlog

Deferred Executive OS work. Build each item only when a real run needs it, so the
layer stays lightweight. Phase 1 (the spine) is already live.

## Phase 2 — Expand on use

### Agents (`executive-os/agents/`)
- research-analyst — finds, evaluates, synthesizes sources.
- opportunity-analyst — turns research into scored opportunities.
- product-strategist — connects user problems, direction, roadmap.
- consultant-agent — structured consultancy-style recommendations.
- monetization-agent — pricing, packaging, revenue experiments.
- pricing-agent — price points, plans, trials, value metric.
- unit-economics-agent — CAC, LTV, margin, AI cost per action, payback.
- risk-review-agent — root causes, mitigations, monitoring signals (reuse
  `PROMPTS/risk-review.md`).

### Workflows (`executive-os/workflows/`)
- market-research
- competitor-research
- reddit-github-scan
- ideation-sprint
- feature-opportunity-review
- business-case-review
- pricing-packaging-review
- monetization-experiment
- quarterly-okr-review
- executive-decision-review
- portfolio-prioritization
- risk-review

### Templates (`executive-os/templates/`)
- source-quality-template
- feature-business-case-template
- pricing-experiment-template
- monetization-scorecard-template
- ceo-weekly-review-template
- risk-register-template

### Prompts (`PROMPTS/`)
- monetization-review
- pricing-packaging-review
- ceo-decision-review
- opportunity-ranking
- executive-decision-review

## Phase 3 — Visualize / automate

- Add an `executiveLayer` block to `dashboard/status.json` and render Layer 8 cards
  in `dashboard/index.html` (CEO OS / CFO OS / Analysis OS / Decision Board /
  Executive Metrics). Touch the generated visual map only after Phase 1 content is
  stable.
- Real data hooks (App Store Connect / RevenueCat / PostHog / provider billing) only
  if and when actually implemented. No claimed sync until real.

## Open Executive Work

Items surfaced by the second Weekly CEO Review (2026-05-31).

---

### analytics-sprint-001 — RunSmart iOS: Verify PostHog event receipt

**Status:** Ready to start  
**Effort:** ~2 hours  
**Decision:** EXD-002  
**Why:** RunSmart iOS has a comprehensive `Analytics` wrapper (`AnalyticsEvents.swift`) wiring
app_launched, sign_in, onboarding_started/completed, plan_generated, run_started, run_completed,
run_abandoned, post_run_card, coach_thread, plan_viewed, plan_workout_tapped, route_selected,
benchmark_viewed, route_saved, tab_viewed, garmin_sync, healthkit_sync. The SDK is initialized
in `RunSmartLiteAppShell.swift:302` via `Analytics.setup(projectToken:host:)`. What is UNKNOWN is
whether these events appear in the PostHog dashboard (token might not be set in CI / production
config).

**Scope:**
- Verify the PostHog project token and host are set in the production / App Store build config.
- Log into PostHog and confirm at least `app_launched` appears for a test run.
- If token is missing: add it to the build config (not hardcoded).
- Do not add new events — the funnel is already wired.

**Files likely touched:**
- `IOS RunSmart app/App/RunSmartLiteAppShell.swift` (token config check)
- Build config / xcconfig file that holds the PostHog token
- `tasks/todo.md` (validation evidence)

**Estimated effort:** 1–2 hours  
**Cap:** 2 hours. If token is correctly set and events appear in PostHog, close this item.

---

### analytics-sprint-002 — Resumely iOS: Integrate PostHog SDK (minimal)

**Status:** Ready to start  
**Effort:** 1–2 days  
**Decision:** EXD-002 + EXD-004  
**Why:** Resumely iOS has zero analytics. No PostHog SDK is present. Shipping with zero
instrumentation means post-launch decisions will be fully blind.

**Scope (strict cap — do not expand):**
- Add PostHog iOS SDK via Swift Package Manager (`PostHog/posthog-ios`).
- Create `AnalyticsService.swift` in `Services/` with a minimal event enum and `setup(token:host:)`.
- Wire `app_launched` in `ResumeBuilderApp.swift` (or equivalent app entry point).
- Wire `optimize_completed` in `TailorViewModel` or the optimize success handler.
- Wire `export_success` (PDF/copy export) in the export handler.
- Do NOT add more than 5 events in this sprint — scope risk is real.
- Token and host must come from build config / xcconfig, never hardcoded.

**Files to create/touch:**
- `ResumeBuilder IOS APP/Services/AnalyticsService.swift` (new)
- `ResumeBuilder IOS APP/App/ResumeBuilderApp.swift` (wire setup + app_launched)
- `ResumeBuilder IOS APP/ViewModels/TailorViewModel.swift` (wire optimize_completed)
- Export handler file (wire export_success)
- `ResumeBuilder IOS APP.xcodeproj` (add SPM dependency)
- `tasks/todo.md` + `tasks/session-log.md`

**Estimated effort:** 1 day (SDK add + AnalyticsService + 3 events)  
**Cap:** 2 days. If it takes longer, descope to app_launched + optimize_completed only and
treat export_success as a post-submission follow-up.

---

### analytics-sprint-003 — Both apps: Define PostHog funnel in dashboard

**Status:** Deferred — do after both apps are live  
**Effort:** 2 hours  
**Why:** Once both apps have events firing, create a PostHog funnel showing
install → app_launched → sign_in / optimize_started → run_completed / optimize_completed.
This is the activation funnel that informs whether acquisition is working.  
**Prerequisite:** analytics-sprint-001 and analytics-sprint-002 must be verified in PostHog first.
