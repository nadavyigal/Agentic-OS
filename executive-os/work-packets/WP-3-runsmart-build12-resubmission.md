# Work Packet WP-3 - RunSmart Build 12 Resubmission

- Status: Active
- Created: 2026-06-09
- Source: RunSmart iOS `tasks/progress.md`; `PROJECT-STATUS.md`; `dashboard/status.json`; COO Operating Review 2026-06-09
- Workflow pattern: normal
- Input trust: trusted
- Outcome loop: none
- Loop: RunSmart App Review recovery
- Signal: RunSmart 1.0.1 build 11 was rejected on 2026-06-08 for Sign in with Apple name/email collection and unclear HealthKit/CareKit UI identification.
- Memory update: RunSmart iOS `tasks/progress.md` and `tasks/session-log.md`
- Success signal: Build 12 is distribution-archived/exported, provenance inspected as `1.0.1 (12)`, reviewer-device SIWA/HealthKit evidence is captured, and App Store Connect resubmission status is recorded.

## Owner Role

Release Manager / QA for RunSmart iOS.

## Project

RunSmart iOS

Path: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

## Goal

Prepare and complete the RunSmart iOS build 12 App Review response without expanding release scope beyond the June 08 rejection reasons.

## Context

RunSmart is the primary product. Build 11 was rejected for requiring name/email after Sign in with Apple and for unclear HealthKit/CareKit UI identification. Local fixes exist and a local Release archive was inspected as `1.0.1 (12)`, but the archive was development-signed with `get-task-allow=true`. Distribution archive/export/upload and reviewer-facing evidence remain open.

## Read First

- `AGENTS.md`
- `CLAUDE.md` or repo-local agent router if present
- `tasks/MEMORY.md`
- `tasks/ERRORS.md`
- `tasks/progress.md`
- `tasks/session-log.md`
- `tasks/todo.md`
- `docs/superpowers/plans/2026-06-08-app-review-rejection-recovery.md`
- `docs/superpowers/plans/2026-06-08-app-review-rejection-external-research-prompt.md`

## Task

1. Confirm the current branch and dirty tree before editing or archiving.
2. Re-read the June 08 rejection recovery plan and current `tasks/progress.md`.
3. Verify the reviewer-visible Sign in with Apple flow no longer asks for name/email after SIWA.
4. Verify HealthKit disclosure is visible on sign-in, onboarding, Profile, and HealthKit detail surfaces, and that no app-code CareKit claim remains.
5. Produce or validate a distribution-signed archive/export for build 12.
6. Inspect archive provenance and entitlement state, including bundle version `1.0.1 (12)` and no development-only signing on the upload artifact.
7. Prepare the App Review response text using only the implemented rejection fixes.
8. Record exact validation evidence in `tasks/progress.md` and `tasks/session-log.md`.

## Constraints

- Do not touch unrelated files.
- Do not add features, redesign flows, or expand beyond the App Review rejection reasons.
- Do not implement monetization, paywall, pricing, StoreKit, RevenueCat, or paid acquisition.
- Do not submit to App Store Connect unless the founder explicitly performs or authorizes the submission in the current session.
- Do not invent validation results. If a device, account, keychain, or signing step is blocked, report the blocker exactly.

## Validation

- Static scan for removed name/email prompt after Sign in with Apple.
- Static scan for HealthKit disclosure text and no app-code CareKit references.
- Simulator visual QA for the reviewer device classes named in the recovery plan, where available.
- Xcode archive/export evidence for distribution signing.
- Archive inspection showing `1.0.1 (12)` and upload-safe entitlements.
- App Review response text prepared and reviewed against the actual rejection reasons.

## Completion Gate

Before final response, update or report:

- `tasks/todo.md`
- `tasks/progress.md`
- `tasks/session-log.md`
- `tasks/lessons.md` only if a reusable lesson was learned

## Final Output

- What changed
- Files changed
- Commands run
- Validation evidence
- App Store Connect status
- Remaining risks
- Next recommended action
