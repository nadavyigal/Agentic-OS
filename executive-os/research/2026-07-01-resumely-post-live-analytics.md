# Resumely Post-Live Analytics Readout - 2026-07-01

- Status: current
- Reviewed: 2026-07-01
- Source: live PostHog project `270848` (`ResumeBuilder AI`), UTC timezone, plus `PROJECT-STATUS.md`, `tasks/progress.md`, and `executive-os/WEEKLY-CEO-LATEST.md`
- Dashboard: `Resumely iOS - Operating Dashboard`, PostHog dashboard `1775579`, pinned and tagged `ios`, `operating`, `resumely`, `founder`
- Constraint: no product code touched; no paid-growth recommendation made

## Summary

Resumely production analytics are live in PostHog, and the founder-facing operating dashboard already exists. Do not create a duplicate dashboard.

The dashboard covers the requested loop: event health, daily active users/auth mix, activation, upload journey, fit-first funnel, optimization-to-export, submit package saves, and failure events. The strongest current signal is that `fit_check_*` and the upload-funnel events are firing in production as of 2026-07-01 UTC.

The main event-health gap is build attribution. `app_launched` has one observed `app_version = 1.2` / `build_number = 7` event, but the custom upload, fit-check, and optimization events mostly have `app_version` and `build_number` unset. This means the OS can say the events are live now, but cannot cleanly prove every funnel event came from v1.2 (7) by event-level version metadata.

## Live Evidence

PostHog event taxonomy in project `270848` includes:

- Upload funnel: `resume_upload_cta_tapped`, `resume_file_picker_opened`, `resume_file_selected`, `resume_upload_started`, `resume_upload_succeeded`, `resume_upload_failed`, `resume_uploaded`
- Fit check: `fit_check_started`, `fit_check_completed`, `fit_check_skipped`, `fit_check_optimize_tapped`
- Optimize/export: `optimization_started`, `optimization_completed`, `export_pdf_tapped`, `export_started`, `export_success`, `export_failed`, `submit_package_saved`
- Onboarding/auth context: `app_launched`, `guest_mode_started`, `sign_in_completed`

Fresh dashboard run on 2026-07-01 returned:

| Signal | Count | Users | Latest event |
|---|---:|---:|---|
| `app_launched` | 174 | 49 | 2026-07-01 04:43:09 UTC |
| `guest_mode_started` | 118 | 47 | 2026-06-30 13:11:48 UTC |
| `resume_upload_cta_tapped` | 21 | 3 | 2026-07-01 04:43:14 UTC |
| `resume_file_picker_opened` | 14 | 2 | 2026-07-01 04:43:18 UTC |
| `resume_file_selected` | 12 | 1 | 2026-07-01 04:43:22 UTC |
| `resume_upload_started` | 21 | 1 | 2026-07-01 04:46:47 UTC |
| `resume_upload_succeeded` | 12 | 1 | 2026-07-01 04:46:49 UTC |
| `resume_uploaded` | 85 | 10 | 2026-07-01 04:46:49 UTC |
| `fit_check_started` | 127 | 19 | 2026-07-01 04:48:23 UTC |
| `fit_check_completed` | 103 | 19 | 2026-07-01 04:48:41 UTC |
| `fit_check_optimize_tapped` | 40 | 19 | 2026-07-01 04:48:43 UTC |
| `optimization_started` | 46 | 3 | 2026-07-01 04:48:43 UTC |
| `optimization_completed` | 32 | 4 | 2026-07-01 04:50:03 UTC |

Dashboard funnel readouts:

- D7 activation: 49 app launchers -> 43 guest starters -> 6 resume uploads -> 4 job adds -> 1 optimization completed -> 1 export success.
- Upload journey: 3 upload CTA users -> 2 file picker users -> 1 file selected -> 1 upload started -> 1 upload succeeded -> 1 job added.
- Fit-first: 19 fit-check starters -> 19 completed -> 18 optimize taps.
- Optimization to export: 3 optimization starters -> 3 completed -> 1 export PDF tap -> 1 export started -> 1 export success.

## Event-Health Gaps

- Version/build attribution is incomplete. A targeted query found one `app_launched` event with `app_version = 1.2` and `build_number = 7`, but the upload, fit-check, and optimization events returned `None` for those fields.
- Event freshness is good. Upload, fit-check, optimization, and diagnosis events were observed on 2026-07-01 UTC.
- Failure volume is currently low in the dashboard window: `resume_upload_failed` had 3 events from 1 user, latest 2026-06-25; `export_failed` had 2 events from 1 user, latest 2026-06-11.
- Some dashboard events listed for health monitoring are not present in taxonomy yet, including `resume_file_picker_cancelled`, `resume_upload_preflight_rejected`, and `resume_upload_error_shown`.

## Recommendation

Next action: use dashboard `1775579` as the canonical Resumely operating dashboard, then run one founder real-device pass on the App Store v1.2 (7) build through upload -> fit check -> optimize. After the pass, confirm the same events appear with `app_version = 1.2` and `build_number = 7`; if not, log a future analytics instrumentation packet for version/build propagation before making activation, lifecycle, monetization, or ASO-volume decisions from version-specific cohorts.

Do not start paid growth from this readout. The evidence gate is event attribution quality, not acquisition volume.
