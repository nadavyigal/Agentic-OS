# Work Packet WP-52a — Instrument `sign_in_failed`, then reproduce under revoked authorization

- Status: Open — next RunSmart action
- Mode: Builder
- Source: EXD-023 (WP-52 verdict, 2026-07-21); WP-52 closed same day with "all five chain links correct"
- Workflow pattern: normal
- Input trust: trusted
- Loop: RunSmart activation gate loop
- Signal: The Apple configuration chain is proven correct, yet June converted 7 of 40 launchers (17.5%) and July converted **0 of ~26** non-founder launchers (p ≈ 0.7% if the June rate held). Outcomes partition perfectly across 13 devices. Auth code unchanged across builds 17-22. Every success on record is an already-authorized Apple ID.
- Memory update: `tasks/lessons.md` (RunSmart iOS); EXD-023 status cell
- Success signal: a `sign_in_failed` event carrying a populated `NSUnderlyingErrorKey`, **or** a controlled reproduction of bare code 1000 under revoked authorization
- Model route: Sonnet 5
- Rollback: Instrumentation is additive on an existing event. Revert the commit.

## Owner Role
RunSmart iOS engineer + founder (device required for the repro)

## Project
RunSmart iOS — `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

## Do Not Redo WP-52's Work

The Apple configuration chain is **cleared with artifacts**. Do not re-inspect it:

- The distribution profile for `com.runsmart.lite` (issued 2026-07-19, one day before the 1.1.1 archive) carries `com.apple.developer.applesignin: [Default]`, confirmed by `codesign -d --entitlements` on the shipped archive. Apple only issues that entitlement when the App ID capability is enabled, so this proves links 1 and 2 together.
- On 2026-07-21 the shipped App Store binary completed a **full native Apple sign-in through Supabase**: `user_signedup`, `provider: apple`, `grant_type: id_token`, status 200 at 07:27:34Z, matched to a PostHog `sign_in_completed` from build 25, `$is_testflight=false`, at 07:27:35.9Z.
- Services ID and `.p8` are the **web OAuth** path. They are not in the causal chain for native `signInWithIdToken` and cannot raise an on-device `ASAuthorizationError`.

Also do not "fix" `sign_in_failed`'s existing properties. `error_code` (=1000), `error_domain` and `screen` are all populated. A same-day PostHog AI audit claimed otherwise by querying property names that do not exist; that claim is false.

## Step 1 — Capture the underlying error

Code 1000 (`ASAuthorizationError.unknown`) is a wrapper. The actionable detail, when it exists, is in the `NSError`'s `userInfo[NSUnderlyingErrorKey]`.

Add to the `sign_in_failed` emission:

- `underlying_error_domain` and `underlying_error_code` from `NSUnderlyingErrorKey`
- `underlying_error_description` — the localized description, **provided it carries no user identifier or token**
- `has_underlying_error` boolean, so "genuinely bare" is distinguishable from "we failed to read it"

That last property matters: a bare 1000 and a 1000-we-did-not-unwrap look identical in the data today, and they imply opposite next steps.

## Step 2 — Reproduce under revoked authorization

This needs **no new device and no new Apple ID**, which is why it runs before anything expensive.

1. On the founder's iPhone (the one whose Apple ID has already authorized RunSmart): **Settings → Apple ID → Sign in with Apple → RunSmart → Stop Using Apple ID.** This returns that Apple ID to the never-authorized state for this app.
2. Delete and reinstall RunSmart from the App Store.
3. Attempt Sign in with Apple **once**. Record the UTC timestamp.
4. Read the resulting event in PostHog project 171597 and report `error_code`, `has_underlying_error`, and the underlying domain/code if present.

**Interpretation, decided in advance so the result cannot be rationalized:**

| Result | Meaning | Next |
|---|---|---|
| Sign-in **succeeds** | First-time authorization is not broken. The July run of failures has another cause — most likely a device/iOS-version correlate. Pivot to the device breakdown | Re-scope |
| Fails, **underlying error present** | The actionable cause. Fix it directly | New packet |
| Fails, **genuinely bare 1000** | Not diagnosable from the app side. **Escalate to WP-53 (guest path)** per EXD-023's own escalation rule | Open WP-53 |

## Step 3 — Settle the regression-versus-constant question

EXD-023 frames this as a *regression*. Auth code was unchanged across builds 17-22, which makes a regression harder to explain and leaves a competing reading open:

> If June's 7 successes were **also** already-authorized Apple IDs, then nothing regressed. First-time sign-in may have been broken all along, and June simply had a higher share of returning users.

Constant failure and a July regression produce identical July numbers, so the July data cannot distinguish them. **June's data can.** While in PostHog, check whether the June successes were first-time authorizations or returning ones.

This matters because "regression" points at a change (of which there was none) and would send the next session hunting a diff that does not exist. Settle it cheaply now.

## Out of Scope

- Re-inspecting the Apple configuration chain. Closed.
- Building the guest path. That is WP-53 and it opens only on the bare-1000 outcome.
- Any FTUX, copy, or onboarding change downstream of the wall.
