# Portfolio Dashboard

Last updated: 2026-05-31 IDT

Source policy: local folder mode only. No GitHub status was used. The dashboard does not
infer progress beyond local Agent OS files and targeted file reads.

## 1. Executive Summary

Overall portfolio status: both iOS apps are in the final pre-submission gate.

Main progress since last dashboard update (2026-05-15 → 2026-05-31):

- RunSmart iOS promoted to **submit-ready** (build 6 uploaded). Two GPS/battery QA passes
  recorded (2026-05-27 and 2026-05-30). PostHog is integrated and firing events. Flex
  Week analytics, Garmin freshness fix, and E7 Wearable Depth are all complete.
- Resumely iOS live stabilization and expert flow are complete; 55/55 tests pass.
  rb-aso-002 screenshots rendered. PostHog **not yet integrated** — this is the last
  technical gate before submission.
- Executive Intelligence OS (Layer 8) was added to the Agentic OS on 2026-05-30
  and the Weekly CEO Review was run for the first time.

Biggest blockers:

- RunSmart iOS: App Store Connect portal tasks are human-only (select build 6, upload
  screenshots, enter demo credentials, confirm privacy / age rating). No agent blocker.
- Resumely iOS: PostHog SDK integration not started. App Store Connect upload blocked
  (no local Fastlane config / ASC API key).

Projects needing QA:

- RunSmart iOS: none remaining for submission readiness — GPS QA passed twice. Portal
  tasks only.
- Resumely iOS: real-device smoke test with live account remains undone.

Projects needing my decision:

- EXD-002: scope and cap for analytics instrumentation work (2-day cap recommended).
- Resumely iOS: whether to integrate PostHog before or after first submission (sequential
  vs. parallel).

Best next action: **RunSmart iOS** — open App Store Connect portal, select build 6,
upload screenshots from `build/AppStoreExportClean`, submit for review. **Resumely iOS**
— integrate PostHog (minimal: app_launched + optimize_completed), then submit.

## 2. Project Status Table

| Project | Status | Current phase | Active story | Last completed story | Next recommended story | Estimated completion | Last validation | Last updated | Blockers | Risks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RunSmart iOS | Submit-ready (build 6 uploaded); portal tasks remaining | App Store submission sprint | App Store Connect portal close-out (human-only) | GPS/battery QA ×2; Garmin freshness fix Stories 1+2; E7 Wearable Depth; Flex Week Analytics | Select build in ASC, upload screenshots, enter demo credentials, submit for review | 2026-06-01 target | GPS QA run 2: 9.10 km 2026-05-30 PASS; focused tests all green | 2026-05-30 | ASC portal tasks are human-only (no agent action available) | App Store approval delay; Garmin webhook audit is backend/human only |
| Resumely iOS | Pre-submission; screenshots ready; PostHog not integrated | Pre-submission sprint | Integrate PostHog SDK; upload screenshots to ASC | rb-aso-002 screenshots rendered; 55/55 tests passing; live expert flow stable | Integrate PostHog; upload screenshots (needs ASC credentials); submit | Unknown | test_sim 55/55 passing 2026-05-26; screenshots rendered 2026-05-28 | 2026-05-28 | PostHog not integrated; no ASC credentials locally | Backend Resume Library not live; WKWebView PDF fragility; no Hebrew/RTL |

Freshness rule:

- Fresh: updated in the last 48 hours.
- Needs Review: updated in the last 3-7 days.
- Stale: older than 7 days.
- Unknown: no reliable updated date found.

## 3. RunSmart iOS Detailed Status

### Completed (since 2026-05-15)

- GPS/battery QA: two physical-device outdoor runs (2026-05-27 7.23 km, 2026-05-30 9.10 km). Both PASS.
- Garmin freshness fix Stories 1 + 2 DONE (2026-05-30): proactive freshness UI + 2-day window.
- E7 Garmin/Wearable Depth DONE (2026-05-28): 7-day HRV/recovery, Striver persona gating.
- App Store launch prep Phase 2+3 (2026-05-26): cross-user FlexWeek cache fix, screenshot regeneration.
- Flex Week Stories 8+9 (2026-05-27): PostHog analytics for flex_week events, PR #34 open.
- PostHog PR #21 conflict resolution DONE.

### Currently Active

- App Store Connect portal close-out (human-only).

### Blocked

- Garmin freshness Story 4 (webhook audit) is backend/human investigation.
- All remaining ASC portal tasks are human-only.

### Validation Done

- GPS QA run 2: 9.10 km, 52:39, 1,432 GPS pts, 7% battery drain, route map rendered. 2026-05-30 PASS.
- StriverPersonaGateTests 3/3, WellnessTrendMapperTests 4/4, FlexWeekCacheTests 4/4. All green.

### Risks Remaining

- App Store approval delay could block launch.
- Garmin webhook subscription (Story 4) not yet audited.

### Recommended Next 3 Actions

1. Human: open App Store Connect, select processed build 6, upload 6.9" and 6.1" screenshots.
2. Human: enter demo credentials in ASC; confirm privacy questionnaire, age rating (4+), category.
3. Human: submit for review.

## 4. Resumely iOS Detailed Status

### Completed (since 2026-05-15)

- Live optimize/design/expert/preview flow stable end-to-end.
- 55/55 XCTest + Swift Testing passing (most recent 2026-05-26).
- rb-aso-002: 5 screenshot slots rendered for iPhone 6.7" + 6.5" (2026-05-28). Upload blocked.
- Backend expert prompts tightened; 24/24 Jest contracts passing.

### Currently Active

- PostHog SDK integration.
- App Store Connect credentials / Fastlane setup.

### Blocked

- Resume Library backend (`/api/v1/resumes`) not live; mock service active.
- `/api/v1/styles/history` returning 500.
- App Store Connect upload needs local Fastlane config / ASC API key.
- Real-device smoke test with live account not done.

### Validation Done

- XcodeBuildMCP test_sim: 55/55 passing 2026-05-26.
- rb-aso-002 screenshots rendered and saved to `dist/app-store-screenshots/rb-aso-002/`.

### Risks Remaining

- Swift 6 concurrency strictness.
- WKWebView PDF render fragility on real device.
- No Hebrew/RTL support.
- No activation/export-success events firing (zero funnel visibility).

### Recommended Next 3 Actions

1. Integrate PostHog SDK: add via SPM, create minimal AnalyticsService, wire `app_launched` + `optimize_completed`.
2. Set up Fastlane / ASC API key; run `deliver` to upload screenshots.
3. Submit Resumely for App Store review.

## 5. Cross-Project Priority Board

### Now

- RunSmart iOS: App Store Connect portal close-out (select build 6, screenshots, demo credentials, submit).
- Resumely iOS: integrate PostHog SDK (minimal scope — see EXECUTIVE-BACKLOG.md analytics sprint).

### Next

- Resumely iOS: App Store Connect upload + submit for review.
- Both apps: post-launch activation monitoring once live.

### Later

- RunSmart iOS: analytics coverage for run_started, run_completed, plan_created.
- Resumely iOS: Resume Library backend integration, PDF/export device QA, Hebrew/RTL.
- Both: revenue / cost instrumentation (CFO OS, Phase 2).

### Blocked

- Resumely iOS real Resume Library integration until `/api/v1/resumes` ships.
- Resumely iOS screenshots upload until ASC credentials / Fastlane config are available.

### Needs QA

- Resumely iOS: real-device smoke test with live account.

### Needs My Decision

- EXD-002: analytics scope and cap (see EXECUTIVE-DECISIONS.md for recommendation).
- Resumely iOS: set up Fastlane ASC credentials locally (human task).

## 6. Validation Board

| Project | Build status | Test status | Manual QA status | App Store submission readiness | Latest validation date | Missing validation |
| --- | --- | --- | --- | --- | --- | --- |
| RunSmart iOS | Simulator build clean; all focused tests green | StriverPersonaGateTests 3/3, WellnessTrendMapperTests 4/4, FlexWeekCacheTests 4/4 | GPS/battery QA passed ×2 | Portal tasks only (human) | 2026-05-30 | ASC portal close-out (human) |
| Resumely iOS | XcodeBuildMCP build clean | test_sim 55/55 passing | No real-device smoke test | Not yet ready (PostHog missing; no ASC credentials) | 2026-05-26 | Real-device smoke, PostHog integration, ASC credentials |

## 7. Decision Board

| Decision | Project | Why it matters | Options | Recommended option | Urgency |
| --- | --- | --- | --- | --- | --- |
| Analytics instrumentation scope (EXD-002) | Both apps | No funnel visibility before launch; risk of shipping blind | Instrument first / ship features first / do both | Instrument first, cap at 2 days, scope to activation + export-success only | High |
| Resumely PostHog: before or after first submission? | Resumely iOS | PostHog not wired = no activation data post-launch | Integrate before submit (1-2 days) / submit now and wire post-launch | Integrate before submit (2-day cap); data from day 1 is worth 2 days | High |
| Fastlane / ASC credentials setup | Resumely iOS | Screenshots and metadata cannot be uploaded without credentials | Manual upload in ASC web UI / Fastlane with API key | Fastlane with ASC API key (founder action) | High |

## 8. Risks And Blockers

### Technical Blockers

- Resumely iOS: PostHog SDK not integrated; no analytics events.
- Resumely iOS: Resume Library backend endpoints not live.

### QA Blockers

- Resumely iOS: real-device smoke test not complete.

### Apple/App Store Blockers

- RunSmart iOS: App Store Connect portal is human-only (agent cannot submit).
- Resumely iOS: no Fastlane config / ASC API key locally.

### Unknowns Caused By Missing Data

- No revenue, cost, or activation data for any product (all `Needs Data`).
- RunSmart iOS: Garmin webhook subscription health (Story 4 webhook audit pending).

## 9. Lessons / Repeated Patterns

- RunSmart iOS: app repo task memory is canonical; outer wrapper task files point here.
- PostHog SDK in iOS requires `Analytics.setup(projectToken:host:)` — token and host come from build config, not hardcoded.
- Screenshots must be generated with the screenshot mode (`--marketing-screenshot` launch arg) before ASC upload.
- Real-device GPS QA takes at minimum a 7 km outdoor run with the phone locked for 5 min.

## 10. Recommended Next Steps

Best next action for RunSmart iOS:

1. Human: App Store Connect portal close-out (select build 6, upload screenshots, enter demo credentials, submit).

Best next action for Resumely iOS:

1. Integrate PostHog SDK (2-day cap; minimal: `app_launched` + `optimize_completed`).
2. Set up Fastlane ASC API key to enable screenshot / metadata upload.

Best cross-project action:

1. Keep both apps in the submission sprint; do not start new feature work.

## 11. Executive Intelligence OS

Layer 8 summary. Source of truth: `executive-os/EXECUTIVE-DASHBOARD.md`. Financial
figures are `Needs Data` until a real source is wired; no numbers are invented here.

| Sub-OS | Status | Note |
| --- | --- | --- |
| CEO OS | Active | Submission sprint; second CEO review run 2026-05-31 |
| CFO / Monetization OS | Needs Data | No revenue/cost instrumentation yet |
| Analysis OS | Ready | No active research sprint running |

- **Current CEO priority:** RunSmart iOS portal close-out → submit; Resumely iOS
  PostHog integration → submit.
- **Top executive risks:** App Store approval delay; Resumely analytics not wired;
  no financial/activation visibility.
- **Open executive decisions:** EXD-002 (analytics scope) — see
  `executive-os/EXECUTIVE-DECISIONS.md`.

Run cadence: `executive-os/EXECUTIVE-RHYTHM.md`.
