# Work Packet WP-20 - RunSmart First-Run Activation Build

- Status: Open
- Created: 2026-06-30
- Source: `rs-onboarding-001`; RunSmart onboarding review `distribution-os/projects/runsmart/scaffold/drafts/2026-06-20-rs-onboarding-review/onboarding-review.md`; current founder note that a Report/Activity `device_name` fallback fix is already in progress
- Workflow pattern: normal
- Input trust: trusted
- Outcome loop: RunSmart D7 activation
- Related decision: EXD-013
- Signal: RunSmart's current acquisition/activation data shows onboarding completion is healthy once started, but `plan_generated -> run_completed` is the immediate activation gap; a small iOS/backend build is already open, so the first-run intervention can be folded into the same ASC train if it stays small.
- Memory update: RunSmart iOS `tasks/progress.md`, `tasks/session-log.md`, and `tasks/MEMORY.md`
- Success signal: Report/Activity consistently displays a device name via activity row value or connection fallback, and a newly onboarded user gets a concrete first-run commitment/reminder path after plan generation.

## Owner Role

RunSmart iOS product engineer

## Project

RunSmart iOS

Path: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

## Goal

Ship one small, App Store-submittable RunSmart iOS/backend build that covers the current Report/Activity `device_name` fallback fix and the smallest `rs-onboarding-001` first-run activation intervention.

## Context

Nadav is already building a small iOS/backend fix so Report/Activity uses the connection `device_name` fallback when an individual activity row lacks it. If the activation work remains small, fold it into this same build and submit to App Store Connect together.

The RunSmart onboarding review found that the 5-step onboarding flow itself is not the main issue: users who start it mostly complete it. The activation leak is around it, especially `plan_generated -> run_completed`. Before D7 retention can be evaluated, the product needs a concrete path from generated plan to first run.

Current release context from RunSmart iOS `tasks/progress.md`: live App Store version is `1.0.4`; `1.0.5 (18)` local archive/export passed on 2026-06-29 but upload/submission/live confirmation is founder-only. If this packet changes the app before upload, use the next valid build number/train based on current App Store Connect state.

## Read First

- `AGENTS.md`
- `CLAUDE.md`
- `tasks/MEMORY.md`
- `tasks/ERRORS.md`
- `tasks/progress.md`
- `tasks/todo.md`
- `tasks/session-log.md`
- `tasks/lessons.md`
- Agentic OS `executive-os/work-packets/WP-15-runsmart-plan-to-run-activation-diagnostic.md`
- Agentic OS `distribution-os/projects/runsmart/scaffold/drafts/2026-06-20-rs-onboarding-review/onboarding-review.md`
- Relevant RunSmart iOS files for Report, Activity, onboarding completion, notification scheduling, analytics events, and App Store review prompt behavior

## Task

1. Finish the current Report/Activity device attribution fix:
   - When an individual activity row lacks `device_name`, display the connected Garmin/Apple Health connection `device_name` fallback where that relationship is available.
   - Keep the fallback display-only unless the existing backend model already expects persisted denormalization.
   - Ensure Report and Activity surfaces agree on the same fallback behavior.

2. Implement the smallest first-run activation intervention from `rs-onboarding-001`:
   - After plan generation/onboarding completion, give the user a concrete first-run commitment path, not a vague "come back later" ending.
   - Prefer a small UI intervention such as a first-run CTA, "start now" / "remind me" choice, or a local reminder scheduling path if the existing notification infrastructure supports it.
   - Default "Smart return reminders" toward activation only if it is consistent with existing consent, notification permission, and local reminder behavior.
   - Do not redesign onboarding, training science, plan generation, auth, Garmin, or Today architecture.

3. Add the App Store first-review prompt only if it is tiny and naturally fits this build:
   - Trigger after a genuinely positive moment, preferably first `run_completed`.
   - Respect Apple's prompt limits and never show it on failure/error screens.
   - If this expands scope, leave it to WP-9 and document why it was deferred.

4. Preserve analytics visibility:
   - Confirm or add analytics for the activation path: plan generated/onboarding completed, first-run CTA viewed/tapped, reminder scheduled if applicable, run started, run completed.
   - Do not rename existing canonical events unless unavoidable.

5. Prepare ASC-ready validation evidence:
   - Build/test locally per RunSmart iOS instructions.
   - If code changes are App Store-bound, update build/version only after confirming the current ASC train constraints.
   - Update RunSmart iOS task memory/progress with exact version/build, validation, and remaining founder-only ASC steps.

## Constraints

- Keep this to one focused build. The packet is not a broad onboarding redesign.
- Do not add dependencies.
- Do not change Garmin OAuth, training science, paywall, monetization, or external production service config unless directly required for the `device_name` fallback and approved in the current session.
- Do not publish App Store metadata, screenshots, notifications, email, Garmin replies, or public assets without explicit founder approval.
- Do not submit to App Store Connect from Codex unless Nadav explicitly authorizes ASC upload/submission in the current message and credentials/device access are available.
- If the activation intervention touches more than 3 unexpected files beyond the already-open device fallback work, stop and report scope expansion.

## Validation

- `git diff --check`.
- RunSmart iOS build/check commands required by local `AGENTS.md` / `CLAUDE.md`.
- Targeted tests or simulator smoke proving:
  - Report/Activity shows activity-level `device_name` when present.
  - Report/Activity falls back to connection `device_name` when activity-level value is missing.
  - New onboarding/plan-generated path shows the first-run activation CTA/reminder path.
  - Existing plan generation still completes.
- If review prompt is added: local or code-level validation that it can only fire after a positive completion moment and is gated.
- If a release archive/export is produced: record archive path, export path, bundle id, version/build, entitlements, and known warnings.

## Completion Gate

Before final response, update or report:

- `tasks/progress.md`
- `tasks/todo.md`
- `tasks/session-log.md`
- `tasks/MEMORY.md`
- `tasks/lessons.md` only if a reusable lesson was learned

## Final Output

- What changed
- Files changed
- Commands run
- Validation evidence
- Version/build state
- Founder-only App Store Connect steps remaining
- Remaining risks
- What was NOT done
