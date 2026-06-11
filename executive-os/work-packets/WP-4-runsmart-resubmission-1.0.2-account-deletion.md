# Work Packet WP-4

- Status: Open
- Created: 2026-06-10
- Source: Apple App Review rejection 2026-06-10, submission 63f48069-3f6c-4279-8f7f-447d9d082a10, version 1.0.1 (12)
- Workflow pattern: normal
- Input trust: trusted
- Outcome loop: runsmart-submission
- Success signal: New build 1.0.2 (14) uploaded with working in-app account deletion and WP-6 aha moments, screen recording attached in App Review notes, submission accepted.
- Escalation: none

# Work Packet

## Owner Role
Release Manager / iOS (local)

## Project
RunSmart iOS
Path: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`
Branch: `codex/app-review-rejection-recovery` (contains the fix; merge to main before archive)

## Goal
Resubmit RunSmart iOS with in-app account deletion so it passes Guideline 5.1.1(v).

## Context — what Apple rejected
Guideline 5.1.1(v): app supports account creation (Sign in with Apple) but offers no in-app way to initiate account deletion. Apple requires the full deletion flow in-app, a screen recording from a physical device in the App Review notes, and that deletion is real (not deactivation).

## Already done (2026-06-10, commit f0908c1)
- `supabase/functions/delete_account/index.ts` — edge function: validates the caller's JWT, deletes all user-owned rows across the RunSmart Supabase project (uuid + legacy bigint keys), then deletes the auth user via the admin API.
- `SupabaseSession.deleteAccount()` — calls the function, clears the local session.
- Account screen (Profile → Account): Delete Account section with destructive confirmation alert and error alert.
- Version bumped 1.0.1 (12) → 1.0.2 (13).
- Simulator build passes with 0 errors; unit test suite passes.

## Remaining Task
1. ~~Deploy the edge function~~ DONE 2026-06-10: `delete_account` v1 ACTIVE on project dxqglotcyirxzyqaxqln (founder approved). Smoke-tested: 401 without auth, 401 JSON for non-user tokens.
2. Merge `codex/app-review-rejection-recovery` to `main` (it also carries the HealthKit-disclosure and sign-in-flow fixes from the prior rejection).
3. Device QA on a physical iPhone: sign in with Apple → Profile → Account → Delete Account → confirm → app returns to sign-in. Verify in Supabase that the auth user and profile rows are gone.
4. Record the flow on a physical device: sign in (or create account) → navigate to deletion → complete deletion. Upload the recording link in App Store Connect → App Review Information → Notes.
5. Archive and upload build 1.0.2 (14 — after WP-6 aha moments land; was 13) per `docs/qa/2026-06-08-build12-submission-readiness-runbook.md`.
6. Reply to the rejection message in App Store Connect noting account deletion is now in-app, and resubmit.

## Constraints
- Deletion must be reachable in at most 2-3 taps from Profile. Do not hide it behind support email.
- Do not touch unrelated files.
- Do not invent validation results; attach evidence per GLOBAL-QA-RULES.md.

## Validation
- Edge function returns 200 and the auth user disappears from Supabase Auth users list.
- Deleting a test account leaves zero rows for that user in: profiles, runs, plans, workouts, conversations, garmin_*, user_streaks, wellness_checkins, run_debriefs.
- Screen recording captured on a physical device and linked in ASC notes.
- Build 14 processed in ASC with no missing-compliance warnings.
