# Work Packet WP-36 - Resumely Export Friction Diagnostic

- Status: In Progress
- Created: 2026-07-05
- Source: D7 Activation Readout #2 correction + Codex/PostHog implementation pass, project 270848
- Mode: Builder
- Workflow pattern: one story at a time (diagnose -> implement smallest fix -> verify with live PostHog)
- Outcome loop: Resumely 20% real activation / 30 days
- Related: WP-18, WP-30, EXD-013, `executive-os/reviews/2026-07-05-activation-reread.md`
- Success signal: at least one non-founder optimized user reaches an explicit export-intent event (`export_pdf_tapped` or equivalent) and the next weekly read can distinguish "never saw export", "saw but did not tap", "tap failed", and "export succeeded"

## Project

Resumely iOS:

`/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`

PostHog:

- Project `270848` (`ResumeBuilder AI`)
- Canonical dashboard: `Resumely — Activation + Export Diagnostic`
- Dashboard URL: `https://us.posthog.com/project/270848/dashboard/1801425`
- Canonical activation insight: `3NiBhRDP`
- Export diagnostic insight: `lVFdiDCs`

## Goal

Diagnose and reduce the next Resumely activation wall: users can upload and some can optimize, but no confirmed real non-founder user has exported.

## Evidence

Live PostHog read on 2026-07-05, 60-day window, excluding known founder/QA/bot person prefixes `067544b5`, `761e5b1b`, `a6441489`, and `712cf425`:

| Step | People | Share of first seen |
|---|---:|---:|
| First seen in project | 133 | 100% |
| Entry: launch/pageview/guest | 120 | 90.2% |
| Fit check started | 18 | 13.5% |
| Resume uploaded (`resume_uploaded`, canonical) | 9 | 6.8% |
| Optimization completed | 2 | 1.5% |
| Export success | 0 | 0% |

Export diagnostic read, same exclusions/window:

| Step | People |
|---|---:|
| Optimization completed | 2 |
| Diagnosis viewed | 0 |
| ATS improve tapped | 0 |
| Export PDF tapped | 0 |
| Export started | 0 |
| Export success | 0 |
| Export failed | 0 |
| Submit package saved | 12 |

Interpretation: current data does not yet show whether the export wall is visibility, intent, auth/session, PDF generation, or product understanding. There are zero clean export-intent/failure events after optimization.

## Progress

2026-07-05 Codex/PostHog implementation pass:

- Created the canonical PostHog dashboard `Resumely — Activation + Export Diagnostic` (`1801425`) with cleaned SQL cards for canonical activation and export friction.
- Marked `resume_uploaded` as the canonical historical upload/import completion event in PostHog and marked `resume_upload_succeeded` as a v1.2+ diagnostic event only.
- Added iOS analytics contract coverage for `optimized_viewed` and `export_cta_seen`.
- Added one-shot optimized-result visibility tracking in `OptimizedResumeView` when an optimization identifier is available.
- Validation run: focused `AnalyticsServiceTests` passed, 9 tests / 0 failures.
- Still pending: simulator/live smoke that reaches the optimized result screen and confirms the new events in PostHog dashboard `1801425`.

## Read First

- Resumely iOS `AGENTS.md`
- Resumely iOS `tasks/lessons.md`
- Resumely iOS `tasks/progress.md`
- Resumely iOS `tasks/session-log.md`
- Resumely iOS `tasks/ERRORS.md`
- Agentic OS `executive-os/reviews/2026-07-05-activation-reread.md`
- Agentic OS `executive-os/work-packets/WP-18-resumely-upload-import-friction-diagnostic.md`

## Task

1. Audit the optimized-result surfaces and export affordances:
   - result/diagnosis screen after optimization
   - Optimized tab
   - export/share CTA visibility
   - auth/session requirements
   - PDF export and fallback path
   - Submit Package path, because `submit_package_saved` currently appears without matching clean export success
2. Confirm existing export analytics call sites and identify gaps:
   - `export_cta_seen` or equivalent visibility event
   - `export_pdf_tapped`
   - `export_started`
   - `export_success`
   - `export_failed`
   - blocked states such as unauthenticated, no optimization id, preview unavailable, PDF render timeout, backend fallback failed
3. Add the smallest useful missing instrumentation so the dashboard can separate:
   - user never reaches export-visible screen
   - user reaches screen but never sees export CTA
   - user sees export CTA but never taps
   - user taps and export starts
   - export fails with a stable non-PII error code
   - export succeeds
4. If the export CTA is visibly buried, disabled without explanation, or confusing, make the smallest copy/placement fix. If the fix requires redesign, write a follow-up plan instead of broad UI work.
5. Re-run the live PostHog dashboard after a smoke test and record whether the new event path appears.

## Constraints

- Do not change scoring logic, resume rewriting logic, pricing, monetization, paywalls, App Store metadata, or distribution.
- No new dependencies.
- No PII in analytics. Do not send resume text, filenames, job descriptions, emails, names, phone numbers, or raw URLs.
- Use stable categorical error codes, not localized user-facing strings.
- If the implementation touches more than 3 unexpected files, stop and report the scope expansion.

## Validation

- `rg` audit documents current export analytics before and after.
- Relevant analytics contract tests are updated.
- Build succeeds with the documented local Xcode command for the touched files.
- Simulator or device smoke reaches one of:
  - optimized screen with export CTA visible
  - export tap -> started -> success
  - export tap -> started -> controlled failure with stable error code
- Live PostHog verification checks dashboard `1801425`, especially insight `lVFdiDCs`.
- `git diff --check` passes.

## Completion Gate

Report:

- Root cause hypothesis for zero clean exports.
- Events added or confirmed, with event names and properties.
- UI/copy change shipped or deferred.
- Build/test/smoke evidence.
- Live PostHog verification result.
- Files changed.
- What was NOT done.
