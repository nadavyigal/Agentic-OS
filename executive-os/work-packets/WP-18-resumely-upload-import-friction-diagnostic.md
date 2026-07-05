# Work Packet WP-18 - Resumely Upload / Import Friction Diagnostic

- Status: In Review (diagnosis complete; instrumentation shipped to branch, PR open)
- Created: 2026-06-24
- Execution (2026-06-24): Root cause = upload journey was a measurement black box (only the terminal `resume_uploaded` fired; in Home it fires on local file-pick, so ~21/26 guests never completed a pick). Prime friction = `.fileImporter` was `.pdf`-only while preflight/backend already accept `.docx`. Shipped 9 PII-safe upload-journey events via shared `TailorViewModel` + HomeTabView/TailorView, widened both pickers to PDF+DOCX+DOC. `AnalyticsServiceTests` 9/9 pass; app compiles. Scan flow deferred. Resumely iOS PR: https://github.com/nadavyigal/ResumeBuilder-IOS-APP/pull/80
- Source: WP-16; EXD-013; `docs/qa/reports/wp-16-activation-attribution-funnel-2026-06-24.md`
- Workflow pattern: feature-diagnostic
- Input trust: trusted WP-16 PostHog readout; continue excluding founder, QA, and automation traffic before quoting activation numbers
- Outcome loop: Resumely D7 activation / Gate A
- Related decision: EXD-013
- Success signal: the guest/app-open -> resume upload drop-off has a named root cause, missing upload/import events are instrumented, and the next clean cohort can measure file-picker start -> file selected -> upload success/failure -> job_added

## Owner Role

Resumely iOS product engineer + product analyst

## Project

Resumely iOS, with optional ResumeBuilder Web comparison if event taxonomy or upload behavior differs.

Paths:

- `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`
- `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`
- `/Users/nadavyigal/Documents/Projects /Agentic OS`

## Goal

Diagnose and instrument the largest measurable Resumely activation drop-off: users launch or enter guest mode, but most do not reach `resume_uploaded`.

## Context

WP-16 found **0 confirmed real-organic D7 activation**. The unresolved person `067544b5` is automation / bot-like traffic, not organic activation. The saved iOS ordered funnel for 2026-06-10 through 2026-06-24 shows:

| Stage | Users | Drop-off |
|---|---:|---:|
| `app_launched` | 30 | baseline |
| `guest_mode_started` | 26 | -4 |
| `resume_uploaded` | 5 | -21 |
| `job_added` | 4 | -1 |
| `optimization_completed` | 1 | -3 |
| `export_success` | 1 | 0 |

The first major leak is before upload/import. Fit-First can remain visible if already shipped, but it is not the primary activation fix until enough real users reach `job_added`.

## Read First

- Resumely iOS `AGENTS.md`
- Resumely iOS `tasks/lessons.md`
- Resumely iOS `tasks/progress.md`
- Resumely iOS `tasks/session-log.md`
- Resumely iOS `tasks/ERRORS.md`
- Resumely iOS `docs/qa/reports/wp-16-activation-attribution-funnel-2026-06-24.md`
- Agentic OS `executive-os/EXECUTIVE-METRICS.md`
- Agentic OS `executive-os/EXECUTIVE-DECISIONS.md` EXD-013
- Agentic OS `executive-os/work-packets/WP-16-resumely-activation-attribution-funnel-diagnostic.md`

## Task

1. Audit the current upload/import path from first app open through `resume_uploaded`:
   - Home/Tailor first action
   - guest mode entry
   - file picker opened
   - file picker cancelled
   - file selected
   - local preflight started
   - preflight rejected
   - upload started
   - upload success
   - upload failure
   - parser fallback used
   - user-facing error shown
2. Map the current analytics taxonomy and identify which events already exist and which are missing.
3. Add the smallest useful instrumentation set so the next read can distinguish:
   - users who never tap upload/import
   - users who open the picker but cancel
   - users who select a file that preflight rejects
   - users whose upload fails server-side
   - users who upload successfully but do not add a job
4. Review Home/Tailor first-action copy and empty states. If copy or CTA hierarchy is clearly blocking resume import, make a minimal copy/CTA adjustment. If it needs design, write a follow-up `plan-feature` instead of broad UI work.
5. If iOS and web have different upload/import event names, document a normalized funnel vocabulary for Agentic OS.
6. Update Resumely iOS `tasks/progress.md`, `tasks/session-log.md`, and, if a new reusable analytics rule is learned, `tasks/lessons.md`.

## Suggested Event Names

Use existing project naming conventions if they differ, but preserve these meanings:

- `resume_upload_cta_tapped`
- `resume_file_picker_opened`
- `resume_file_picker_cancelled`
- `resume_file_selected`
- `resume_upload_preflight_rejected`
- `resume_upload_started`
- `resume_upload_failed`
- `resume_upload_succeeded`
- `resume_upload_error_shown`

Useful properties:

- `source` (`home`, `tailor`, `guest_onboarding`, etc.)
- `file_type`
- `file_size_bucket`
- `failure_stage`
- `error_code`
- `is_guest`
- `parser_fallback_used`

Do not send resume text, filenames, email addresses, phone numbers, job descriptions, or other PII.

## Constraints

- No monetization, paywall, RevenueCat, StoreKit, pricing, paid acquisition, or ASO volume work.
- No scoring logic changes.
- No App Store submission or metadata changes without explicit founder approval.
- No new dependencies.
- Keep the implementation focused on upload/import diagnosis and the smallest friction fix.
- If the fix expands beyond 3 unexpected files, stop and report the scope expansion.

## Validation

- `rg` audit documents current upload/import analytics before and after.
- Build succeeds with the local required Xcode command.
- Relevant analytics contract tests are updated or added.
- Simulator or device smoke reaches at least:
  - app launch / guest start
  - upload CTA tap
  - file picker path or mocked equivalent
  - one success or one controlled failure path
- `git diff --check` passes.

## Completion Gate

Report:

- Root cause hypothesis for the pre-upload drop-off.
- Events added or confirmed, with event names and properties.
- Files changed.
- Build/test/smoke evidence.
- Whether a product copy/CTA change shipped or was deferred.
- Next metric to watch: `guest_mode_started -> resume_upload_cta_tapped -> resume_file_selected -> resume_upload_succeeded -> job_added`.
- What was NOT done.

## Note — 2026-07-05 (found while correcting D7 Activation Readout #2)

Readout #2 mistakenly queried `resume_upload_succeeded` (this packet's new event, PR #80 still in review) as if it were the established terminal upload event — it isn't live for most users yet (13 events / 1 person all-time), so it read as a near-total upload wall. The actual established event, `resume_uploaded` (confirmed by this packet's own 2026-06-24 diagnosis as the one terminal event that fires), shows 90 events / 11 people all-time (8 after founder/QA/bot exclusion) — real, if modest, upload activity. Corrected downstream funnel: uploaded 8 → optimized 2 → **exported 0** (all 3 all-time exports are founder-pattern accounts). Once PR #80 merges and `resume_upload_succeeded` accumulates real traffic, re-verify this packet's new events line up with `resume_uploaded` counts (they should track closely) — and consider whether this packet's scope should extend to the optimization→export step, since that's now the more severe gap. Full correction: `executive-os/reviews/2026-07-05-activation-reread.md`.

