# Project Status

Last updated: 2026-05-31 IDT

Source policy: local folder mode only. No GitHub status was used. Status is based on
local task files (`tasks/todo.md`, `tasks/session-log.md`) read directly on 2026-05-31.

## Status Table

| Project | Freshness | Status | Current Phase | Active Story | Last Completed Story | Next Recommended Story | Estimated Completion | Last Validation | Last Updated | Blockers | Risks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RunSmart iOS | Fresh | Submit-ready (build 6 uploaded); portal tasks are the only remaining gate | App Store submission sprint | App Store Connect portal close-out (human-only) | Garmin freshness fix Stories 1+2; GPS/battery QA passed twice (5/27, 5/30); E7 Garmin/Wearable Depth; Flex Week Analytics (Story 8+9, PR #34) | Select processed build in ASC, add screenshots, enter demo credentials, confirm privacy questionnaire / age rating | 2026-06-01 target | GPS QA run 1: 7.23 km 2026-05-27 PASS; GPS QA run 2: 9.10 km 2026-05-30 PASS; simulator build and all focused tests passing | 2026-05-30 | App Store Connect portal tasks are human-only (cannot be automated): select build 6, upload screenshots, enter demo credentials, confirm privacy/age rating | App Store approval delay; Garmin webhook audit (Story 4) is backend/human investigation |
| Resumely iOS | Fresh | Pre-submission; screenshots rendered (rb-aso-002 DONE); PostHog not yet integrated | Pre-submission sprint | Integrate PostHog + submit to App Store Connect | rb-aso-002 screenshots rendered; 55/55 tests passing; live optimize/design/expert flow stable | Integrate PostHog SDK; upload screenshots to ASC (needs credentials); submit for review | Unknown | XcodeBuildMCP build + test 55/55 passing on 2026-05-26; rb-aso-002 screenshots rendered 2026-05-28 | 2026-05-28 | App Store Connect upload blocked (no Fastlane config / ASC API key locally); PostHog SDK not yet integrated | Backend Resume Library endpoints not live; WKWebView PDF fragility; no Hebrew/RTL support |

## RunSmart iOS Detail

Source path: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

Source files read:

- `tasks/todo.md` (read 2026-05-31)
- `tasks/session-log.md` (read 2026-05-31)

### Completed (since last status — 2026-05-15)

- **GPS/battery QA**: two physical-device outdoor runs passed.
  - Run 1 (2026-05-27): 7.23 km, 39:51, 1,135 GPS pts, no drift, background tracking held. PASS.
  - Run 2 (2026-05-30): 9.10 km, 52:39, 5:47 avg pace, 1,432 GPS pts, route map rendered, RPE logged. Battery 52%→45% (7% drain). PASS.
- **Garmin freshness fix (T2)**: Story 1 (proactive freshness UI) and Story 2 (widened 2-day window) DONE 2026-05-30.
- **E7 Garmin/Wearable Depth**: 7-day HRV/recovery sparklines and Striver persona gating COMPLETE 2026-05-28. Focused tests: StriverPersonaGateTests (3/3), WellnessTrendMapperTests (4/4).
- **App Store launch prep Phase 2+3** (2026-05-26): cross-user FlexWeek cache fix, FlexWeekCacheTests 4/4, screenshot regeneration with real WeeklyProgressCard data.
- **Flex Week Stories 8+9** (2026-05-27): PostHog analytics for flex_week_triggered/confirmed/cancelled/intervention_shown/action. PR #34 open.
- **PostHog PR #21** merge-conflict resolution DONE.

### Analytics Status

- PostHog SDK: **integrated** in `RunSmartLiteAppShell.swift`.
- Events wired: `app_launched`, `tab_viewed`, `sign_in_completed`, `flex_week_triggered`, `flex_week_confirmed`, `flex_week_cancelled`, `flex_week_intervention_shown`, `flex_week_intervention_action`.
- Missing from activation funnel: `run_started`, `run_completed`, `plan_created`, `onboarding_completed`. These are not yet tracked.

### Active

- App Store Connect portal close-out: select build 6 (once processed), upload screenshots, enter demo credentials, confirm privacy questionnaire / age rating / category.

### Blocked

- T2 Garmin freshness Story 4 (webhook audit) is backend/human investigation — cannot be automated.
- All remaining App Store Connect portal tasks are human-only; no agent action required.

### Validation

- GPS QA run 2 evidence: 9.10 km, 52:39, 1,432 GPS pts, battery 7% drain, route map + Coach Analysis rendered. 2026-05-30.
- All focused tests green (see entries above).

### Next 3 Actions

1. Human: open App Store Connect, select processed build 6, upload 6.9" and 6.1" screenshots from `build/AppStoreExportClean`.
2. Human: enter demo credentials in ASC portal; confirm privacy questionnaire, age rating (4+), category (Health & Fitness).
3. Human: submit for review.

## Resumely iOS Detail

Source path: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`

Source files read:

- `tasks/todo.md` (read 2026-05-31)
- `tasks/session-log.md` (read 2026-05-31)

### Completed (since last status — 2026-05-15)

- End-to-end live stabilization: optimize/design/expert/preview flow stable through 2026-05-26.
- 55/55 XCTest + Swift Testing passing as of 2026-05-26.
- rb-aso-002: 5 screenshot slots rendered for iPhone 6.7" and 6.5". Upload blocked by missing ASC credentials/Fastlane config.
- Backend expert prompts tightened; backend focused Jest contracts 24/24 passing.

### Analytics Status

- PostHog SDK: **not integrated**. No Swift file references PostHog.
- There is no `AnalyticsService` or event tracking in the iOS codebase.
- Required before submission: at minimum `app_launched`, `optimize_started`, `optimize_completed` (activation proxy).

### Active

- Integrate PostHog SDK and wire core events.
- Upload screenshots to App Store Connect (blocked on ASC credentials / Fastlane config).
- Submit for review.

### Blocked

- Resume Library backend (`/api/v1/resumes` list/save/rename/delete) not live; mock service active.
- `/api/v1/styles/history` returning 500 — working around by not calling it.
- App Store Connect upload credentials / ASC API key not found locally (no Fastlane config present).
- Real-device smoke test with live account not yet run.

### Validation

- XcodeBuildMCP test_sim: 55/55 passing (2026-05-26 most recent).
- rb-aso-002 screenshot PNGs rendered and saved under `dist/app-store-screenshots/rb-aso-002/`.

### Next 3 Actions

1. Integrate PostHog SDK (add to SPM, create minimal AnalyticsService, wire app_launched + optimize_completed).
2. Set up Fastlane / ASC API key so screenshot upload can be automated.
3. Submit Resumely to App Store for review.

## Data Quality Notes

- RunSmart iOS source-of-truth files are in the app repo; outer wrapper stubs point here.
- PostHog token and host are read from environment / build config in RunSmartLiteAppShell — not hardcoded. Actual token value not read here (not needed for status).
- Resumely iOS: local checkout confirmed on latest `main` as of 2026-05-26.
