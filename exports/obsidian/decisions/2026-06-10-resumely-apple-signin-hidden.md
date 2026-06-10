# Decision: Hide Resumely Sign in with Apple Behind Feature Flag

Date: 2026-06-10
Project: Resumely iOS
Status: Accepted
Owner: Nadav Yigal

## Decision

Ship Resumely iOS build 3 without Sign in with Apple. The button is hidden behind `BackendConfig.isAppleSignInEnabled = false`. Email/password is the only auth path until the flag is flipped.

## Why Now

Apple rejected build 2 for Guideline 2.1(a): Sign in with Apple exhibited an error during review. Root cause confirmed in Supabase auth logs (project `brtdyamysfmctrhuankn`): `error_code: provider_disabled` — the Apple provider is disabled in the Supabase dashboard. The resubmission deadline is immediate (both guidelines require a fix before resubmission).

## Context

- Apple's rejection message said the app "exhibited one or more bugs" and showed the Sign in with Apple flow failing.
- Supabase auth logs showed `error_code: provider_disabled` at exactly the time the Apple reviewer attempted sign-in.
- The fix is: Supabase dashboard → Authentication → Providers → Apple → enable, add bundle ID `Resumebuilder-IOS.ResumeBuilder-IOS-APP` to Authorized Client IDs.
- The founder could not complete Supabase Apple provider setup during this session. The provider form requires the App Store Connect Service ID and Apple private key; this is not a Zoho email configuration — no email account is involved.

## Options Considered

1. **Enable Apple provider in Supabase dashboard before resubmitting** — requires Service ID + private key from Apple Developer. Founder could not complete this in-session.
2. **Hide the button behind a feature flag and ship email-only** — accepted. No dashboard change needed; resubmission can proceed immediately. Re-enable path is clear.
3. **Remove Sign in with Apple entirely** — rejected. The feature is valuable and Apple requires it for apps with any social sign-in. Hiding it preserves the code.

## Recommendation

Option 2. Ship email-only now, re-enable after Supabase Apple provider is configured.

## Risks

- Users who saw Sign in with Apple in the previous rejected build will not see it in build 3. Minimal since build 2 was never publicly available (rejected before going live).
- If the Supabase Apple provider setup is never completed, Apple sign-in stays hidden indefinitely.
- Apple may notice the button was removed and ask why — this is unlikely for a new app that was never live.

## Mitigations

- Flag is a single static constant; re-enable is a one-line code change + new build. No backend work needed.
- Supabase Apple provider setup steps documented: Dashboard → Auth → Providers → Apple → enable + add bundle ID. Only requires Apple Developer account (already exists).
- ASC demo account (`nadav.yigal@runsmart-ai.com`) provides Apple reviewer a working sign-in path via email.

## Next Actions

- [ ] Add demo email/password account to ASC App Review Information.
- [ ] Complete Supabase Apple provider setup (Service ID `com.runsmart.ResumeBuilder-IOS-APP` + private key from Apple Developer).
- [ ] After provider is active, flip `BackendConfig.isAppleSignInEnabled = true`, bump build, archive, resubmit.

## Links

- [[ResumeBuilder]]
- [[2026-06-10 App Store Rejections Fixed]]
- WP-5: `executive-os/work-packets/WP-5-resumely-resubmission-build3-apple-signin-deletion.md`
