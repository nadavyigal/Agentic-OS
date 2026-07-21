# Session Prompts — 2026-07-21

Copy-ready prompts derived from the Weekly Review 2026-07-21 and COO Operating Review 2026-07-21. **Launch each from its own repo**, not from the vault or Agentic OS — the usage collector bins spend by launch directory.

Order matters. Prompt 1 is the only one on the critical path to 2026-08-01.

---

## 1. Resumely iOS — WP-51: repair the activation milestone

**Repo:** `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`
**Model:** Sonnet 5
**Urgency:** High — this is the bottleneck. 1.4.4 is under ASC review and does not contain this fix.

```
Execute WP-51 (Agentic OS executive-os/work-packets/WP-51-resumely-fix-activation-milestone.md).

Context: the 2026-07-21 live PostHog read on the canonical WP-50 contract returned a
non-monotonic funnel over 30 days, project 270848, is_internal_tester persons excluded:
  resume_file_selected   12
  optimization_completed   7
  optimized_preview_rendered  1   <-- the activation milestone
  export_success           3

More people exported than rendered a preview, which is impossible if the milestone fired
reliably. optimized_preview_rendered has only 3 people across 60 days.

Per the WP-46 Story 10 contract it should fire "once per optimization only after WKWebView
reports a successful visible HTML navigation and the optimized resume has visible applied
changes." Find which of those two conditions is suppressing it.

Work against main. 1.4.4 (14) is already under App Store review and contains no measurement
fix, so this repair ships as 1.4.5 immediately after 1.4.4 approves. Do not wait for the
approval to start.

Do NOT change the WP-50 denominator (resume_file_selected) - that decision is settled.
Do NOT touch the is_internal_tester classifier defect - tracked separately, not on the
critical path.

Deliver: a red-then-green regression test proving the event fires on a successful preview
render, the full suite passing (baseline 205 passed / 1 intentional skip), and an answer to
this question - was the under-firing introduced by the Story 10 commits (31b73b6 / 8277cba)
that shipped in 1.4.3, or has this event never worked? That determines whether the 12.5%
historical baseline was ever measured on a working event.
```

---

## 2. RunSmart iOS — WP-52: diagnose the Apple sign-in chain (timeboxed, diagnosis only)

**Repo:** `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`
**Model:** Sonnet 5
**Urgency:** High, but **timeboxed to one session.** Requires founder Apple Developer portal access.

```
Execute WP-52 (Agentic OS executive-os/work-packets/WP-52-runsmart-apple-signin-chain-diagnosis.md).

This is DIAGNOSIS ONLY. Do not change any portal setting, Supabase setting, or app code
during this session. A silent config change mid-investigation destroys attribution.

Context: on the live 1.1.1 (25) App Store binary, a genuine App Store install
($is_testflight, $is_sideloaded, $is_emulator all false) on iPhone17,1 produced 5 consecutive
ASAuthorizationError code 1000 events at screen=sign_in_wall between 12:22 and 12:25 UTC on
2026-07-20, with 0 sign_in_completed. Cumulative: 12 code-1000 events, 4 distinct devices,
3 builds. Every sign_in_completed on record belongs to an Apple ID that had already
authorized RunSmart.

Critical prior art: this portfolio hit this same chain in June with Resumely. See Builder OS
05-Decisions/2026-06-10-resumely-apple-signin-hidden.md - root cause was that the Apple
provider setup requires an App Store Connect Service ID and private key, and that step was
never completed. Treat this as the leading hypothesis, not a coincidence.

Inspect these five links in order. Links 1-3 fail on-device before any network request, which
matches RunSmart's signature (no /token request in Supabase auth logs during failures), so
start there:
  1. App ID has Sign In with Apple capability enabled
  2. The App Store distribution provisioning profile actually carries the SIWA entitlement,
     and the shipped 1.1.1 build was signed with it
  3. Services ID exists and is associated with the primary App ID
  4. Private key (.p8) + Key ID generated and registered
  5. Supabase Apple provider enabled, Authorized Client IDs contains exactly com.runsmart.lite

Verify link 2 against the shipped binary, not the project settings:
  codesign -d --entitlements :- <path-to-.app>

Timebox: one working session. If you cannot identify the broken link by the end of it, that
outcome IS the answer - stop and report it, which opens WP-53 (guest path).

Do not test on a device that has previously authorized RunSmart. It will succeed and prove
nothing - that is exactly what produced the misleading 2026-07-20 clean-install result.

Deliver: the state of each of the five links, the entitlements present in the shipped binary,
and a verdict naming the broken link or explicitly clearing all five.
```

---

## 3. RunSmart iOS — WP-53: guest path (CONDITIONAL — do not start yet)

**Repo:** `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`
**Model:** Opus 4.8 for the state/persistence design, Sonnet 5 for implementation
**Urgency:** Blocked on WP-52's verdict.

> **Do not run this prompt until WP-52 returns one of:** all five links confirmed correct; a broken link whose fix is not available in one session; or an exhausted timebox with no verdict. If WP-52 finds a one-session portal fix, apply it and re-measure first — this packet is materially more expensive.

```
Execute WP-53 (Agentic OS executive-os/work-packets/WP-53-runsmart-guest-path-to-plan.md).

WP-52 has returned its verdict and the Apple chain is not a one-session fix. Ship a guest path
so a user reaches a generated plan with no account, removing Apple from the activation
critical path entirely.

Scope: skippable sign-in wall (RunSmartLiteAppShell.swift:184), guest plan generation with
local-only state, persistence across restart, deferred account linking that migrates the guest
plan rather than discarding it, and a guest_mode_started event named identically to Resumely's
so the two products' funnels become directly comparable.

Ship behind RUNSMART_GUEST_MODE_ENABLED, default off. Rollback is flipping the flag.

Sign in with Apple stays in the app. It stops being mandatory.

Before shipping, add a per-device rate limit on plan generation - removing the auth gate
removes the natural abuse limiter on an OpenAI-backed call.

Validation: full suite (baseline 317 passed), device QA on a NEVER-authorized Apple ID
reaching a generated plan, restart persistence, account-linking preserving the guest plan,
and guest_mode_started + plan_generated confirmed in PostHog project 171597 with app_version
attribution.
```

---

## 4. Agentic OS — WP-54: measurement integrity guardrails

**Repo:** `/Users/nadavyigal/Documents/Projects /Agentic OS`
**Model:** Sonnet 5
**Urgency:** Medium. Not on the 08-01 critical path, but this class of defect has now been the binding constraint three reviews running.

```
Create WP-54 and implement the measurement-integrity guardrails identified by the 2026-07-21
weekly review. Four instances of the same failure class are now on record:

  1. marketing_version - referenced by RunSmart plan docs, does not exist in project 171597's
     taxonomy. Queries return null for every row and read as "no data" rather than "wrong
     property name." Correct property is $app_version / app_build.
  2. resume_uploaded - production call site removed by WP-46 Story 10 in Resumely 1.4.3, which
     silently zeroed every dashboard series built on it.
  3. resume_upload_succeeded - sits behind the sign-in guard, so it can never exceed
     sign_in_completed. Used as a denominator anyway (WP-48 Defect B).
  4. optimized_preview_rendered - under-fires, producing a non-monotonic funnel (WP-51).

Build:
  a. A pre-flight check that any event or property named in a dashboard series or a plan doc
     actually exists in the target PostHog project's taxonomy. Fail loudly, not silently.
  b. A monotonicity assertion on any ordered funnel the dashboard renders - a later step
     exceeding an earlier one is a defect, not a datapoint, and should surface as a drift
     warning.
  c. A rule (and a check) that retiring an event requires updating every series built on it.

Also: register an "activation measurement integrity" outcome loop under executive-os/loops/.
This has been handled as a series of one-off packets across three consecutive reviews, which
is the signature of a missing loop.
```

---

## What not to touch this cycle

Applies to every session above:

- **No GTM, distribution, ASO, or acquisition work.** All three `needs_next_packet` plans stay unpacketized while both funnels are broken.
- **No RunSmart FTUX copy, onboarding polish, or E1 assignment work.** All sit downstream of a gate that returns a hard Apple error; they cannot produce a readable result.
- **No Adaptive Coach Phase 2.** Its gate (2 weeks live AND ≥20 real `adaptive_coach_shown` users) is arithmetically unfillable at current entry volume.
- **No changes to the WP-50 denominator.** Settled.
- **RunSmart Web and ResumeBuilder Web get no packet this cycle.** Both have clean recent work (eval harnesses green, PR #116 merged); neither is on the critical path. ResumeBuilder Web PR #117 remains blocked on the read-path fallback described in its existing review comment — that is unchanged and still correct.
