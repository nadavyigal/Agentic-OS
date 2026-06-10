# Work Packet WP-5

- Status: Open
- Created: 2026-06-10
- Source: Apple App Review rejection 2026-06-10, submission e157ff28-671e-4f54-9b19-c9d6bddab25f, version 1.0 (2)
- Workflow pattern: normal
- Input trust: trusted
- Outcome loop: resumely-submission
- Success signal: New build 1.0 (3) uploaded with working Sign in with Apple and in-app account deletion, screen recording attached, submission accepted.
- Escalation: none

# Work Packet

## Owner Role
Release Manager / iOS (local)

## Project
Resumely iOS (ResumeBuilder IOS APP)
Path: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`
Branch: `main` (fix committed as f7e5948)

## Goal
Resubmit Resumely iOS so it passes both rejection points: Guideline 2.1(a) (Sign in with Apple error) and Guideline 5.1.1(v) (account deletion).

## Root cause — Sign in with Apple (2.1a)
**Confirmed from Supabase auth logs** (project brtdyamysfmctrhuankn, 2026-06-10T02:36:05Z, the reviewer's attempt from an Apple IP):
`400: Provider (issuer "https://appleid.apple.com") is not enabled` — error_code `provider_disabled`.
The Apple provider is disabled in the Supabase project. The iOS code (native id_token grant with nonce) is correct. No code change needed.

**Fix (founder, Supabase dashboard — cannot be done via API):**
1. Supabase → project brtdyamysfmctrhuankn → Authentication → Sign In / Providers → Apple → Enable.
2. In "Authorized Client IDs" add the iOS bundle ID `Resumebuilder-IOS.ResumeBuilder-IOS-APP` (and the web Service ID if the website also offers Apple sign-in).
3. Native id_token flow needs no client secret; the secret is only required for the web redirect flow.
4. Verify in App Store Connect / developer portal that the app ID has the Sign in with Apple capability (the entitlement is already in the project).

## Already done (2026-06-10, commit f7e5948)
- `supabase/functions/delete_account/index.ts` — edge function: validates JWT, wipes all user-owned rows (resumes, optimizations, job_descriptions, applications, chat_sessions, expert runs, credits, device tokens, profile; children cascade), then deletes the auth user.
- `AuthService.deleteAccount(accessToken:)` + `AppState.deleteAccount()` with one token-refresh retry; `account_deleted` analytics event.
- Profile → Account: Delete Account row with destructive confirmation alert and error alert.
- Build number bumped to 3.
- Simulator build passes with 0 errors.

## Remaining Task
1. Founder: enable the Apple provider in Supabase (steps above). This is the 2.1(a) fix.
2. Deploy the edge function (needs founder yes — production change):
   `supabase functions deploy delete_account` from the repo root (project brtdyamysfmctrhuankn).
3. Device QA on a physical iPhone AND an iPad (or iPad simulator at minimum — the reviewer used iPad Air 11-inch):
   - Sign in with Apple completes and lands signed-in.
   - Profile → Delete Account → confirm → returns to signed-out state; auth user gone in Supabase.
4. Record on a physical device: create account / sign in → navigate to deletion → complete deletion. Put the recording link in ASC → App Review Information → Notes.
5. Archive and upload build 1.0 (3).
6. Reply to the rejection in App Store Connect describing both fixes, and resubmit.

## Constraints
- Test Sign in with Apple on iPad form factor before resubmitting — that is the device class Apple used.
- Do not touch unrelated files.
- Do not invent validation results; attach evidence per GLOBAL-QA-RULES.md.

## Validation
- Supabase auth logs show a successful `grant_type=id_token` login with provider apple (no provider_disabled).
- Deleting a test account returns 200 and removes the auth user + all user rows.
- Screen recording captured and linked in ASC notes.
- Build 3 processed in ASC.
