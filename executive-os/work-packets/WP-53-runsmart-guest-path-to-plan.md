# Work Packet WP-53 — RunSmart guest path to plan generation

- Status: Conditional — opens on WP-52's verdict
- Mode: Builder
- Source: COO Operating Review 2026-07-21 §10 (CEO decision (a)); Builder OS `2026-07-21-apple-signin-cross-product-pattern`; `2026-07-19-activation-cliff-autopsy`
- Workflow pattern: normal
- Input trust: trusted
- Loop: RunSmart activation gate loop
- Signal: 95.7% of organic App Store users quit at the first screen (22/23, 90d clean read), and the reason is now confirmed to be a hard Apple error rather than persuasion. Resumely, which has no auth gate before value, is the only product in the portfolio with a readable activation funnel.
- Memory update: `tasks/lessons.md` (RunSmart iOS) + `EXECUTIVE-DECISIONS.md`
- Success signal: A user who has never signed in reaches a generated plan, and `plan_generated` fires with no `sign_in_completed` for that person
- Model route: Opus 4.8 for the state/persistence design; Sonnet 5 for implementation
- Rollback: Ship behind a feature flag (`RUNSMART_GUEST_MODE_ENABLED`, default off), flip on after device QA. Rollback is flipping the flag off — no data migration, no submission dependency.

## Owner Role
RunSmart iOS engineer

## Project
RunSmart iOS — `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

## Trigger Condition — Do Not Start Before This Is Met

Start this packet when **either**:
- WP-52 returns "all five links confirmed correct" (the failure is not configuration), **or**
- WP-52 identifies a broken link whose fix is not available to the founder in one session, **or**
- WP-52 exhausts its timebox without a verdict.

If WP-52 finds a one-session portal fix, **apply that first and re-measure before starting this packet.** A working Apple sign-in plus the existing wall may be enough, and this packet is materially more expensive.

## Why This Is Worth Doing Even If Apple Gets Fixed

Stated plainly so the decision is made on merit rather than frustration: repairing the Apple chain fixes one gate and leaves activation permanently dependent on a third party whose failure mode this portfolio has now hit twice. A guest path removes Apple from the activation critical path entirely.

Resumely is the evidence. Its guest architecture was not designed as a growth strategy — it was a June workaround to this same Apple problem — and it is the reason Resumely's funnel is measurable today while RunSmart's is not. That is the cleanest natural experiment the portfolio has produced, and nobody planned it.

The counter-argument, which deserves an honest hearing: RunSmart is **secondary** under EXD-015, and this is not a small packet. It touches onboarding, plan persistence, and the account-linking path. If the CEO judgement is that RunSmart should not absorb this while Resumely's window is open, deferring is defensible — but then the RunSmart activation numbers should be formally marked "not measurable" rather than continuing to be read as product signal.

## Scope

1. **Guest onboarding.** A user reaching the first screen can proceed without an account. The sign-in wall (`RunSmartLiteAppShell.swift:184`) becomes skippable, not mandatory.
2. **Guest plan generation.** Goal capture through generated plan works with local-only state. No account required to see the core value.
3. **Local persistence.** Plan and onboarding answers survive app restart without a backend user row.
4. **Deferred account linking.** Prompt for an account at the point where it genuinely buys something (sync, history, multi-device), not before. When they do sign in, the guest plan migrates to the account rather than being discarded.
5. **Instrumentation.** `guest_mode_started` mirroring Resumely's naming, so the two products' funnels become directly comparable. This is a deliberate portfolio-level choice — same event name, same semantics.

## Out of Scope

- Removing Sign in with Apple. It stays; it stops being mandatory.
- Any Apple portal or Supabase configuration change — that is WP-52's territory.
- Garmin, HealthKit, or Adaptive Coach surfaces.
- Backend guest-session storage. Local-only for v1; a server-side guest identity is a later question if the pattern proves out.

## Validation

- Full test suite green (baseline: 317 passed)
- Device QA on a **never-authorized Apple ID**: install, skip sign-in, reach a generated plan
- Restart persistence verified
- Account-linking path verified: guest plan survives sign-in
- `guest_mode_started` and `plan_generated` both confirmed in PostHog project 171597 with `app_version` attribution

## Risk To Name Up Front

Plan generation costs an OpenAI call. Removing the auth gate removes the natural abuse limiter. Add a per-device rate limit before shipping, and confirm the cost envelope at expected volume (~10-15 installs/week today, so this is not urgent at current scale — but it is the thing that breaks if the packet succeeds and traffic grows).
