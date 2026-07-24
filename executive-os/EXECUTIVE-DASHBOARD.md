# Executive Dashboard

Manual source-of-truth dashboard for the Executive Intelligence OS. Financial cells stay `Needs Data` until a real source exists.

Last updated: 2026-07-24 IDT

## Executive Summary

Resumely is primary through the 2026-08-01 activation window. Both apps are live on new builds since 2026-07-22: RunSmart 1.1.2 (27) and Resumely 1.4.5 (15), store-verified 2026-07-24. Today's arrival check passed for both (non-founder events carry the new version strings), so build-keyed reads are trustworthy subject to two integrity caveats: Resumely's activation milestone event is unnamed (`export_success` no longer fires), and 76% of RunSmart non-founder event volume is unversioned. The RunSmart sign-in P0 was refuted 2026-07-22 (fails for some, not all; cause unnamed). RunSmart 1.1.3 (28, route feature) is merged and awaiting founder archive; Resumely 1.4.6 (WP-53 recovery fix + review prompt) is in App Store review. Sources: Apple lookup API and PostHog 171597/270848 (2026-07-24); `EXECUTIVE-DECISIONS.md`; `EXECUTIVE-METRICS.md`.

## Top 3 Priorities

1. Take the two reads that decide the next moves, and not before their windows: Resumely activation on/after 2026-07-25 (pin the milestone event first, count toward EXD-022's 20); RunSmart `has_underlying_error` on the first real 1.1.2 `sign_in_failed` (EXD-023 checkpoint 2026-07-28).
2. Ship the two builds already made: archive + submit RunSmart 1.1.3 (28); get Resumely 1.4.6 through App Store review.
3. Fix RunSmart's null-`app_version` tail (554 events / 17 persons vs 164 / 5 on 1.1.2) before trusting any RunSmart build-split, including the sign-in read denominator.

Source: `executive-os/reviews/2026-07-24-weekly-ceo-review.md`.

## Financial Snapshot

Revenue, costs, margin, burn, and runway are `unknown - need: App Store Connect/RevenueCat, provider billing, cash on hand, and a manual cost list`. Marketing spend is the only known figure at `$0`. Source: `executive-os/reviews/2026-07-09-monthly-finance-review.md`.

## Decision Board

- Open executive decisions: 0. Two Decided rows carry live checkpoints.
- EXD-022 (checkpoint 2026-08-01): activation gate = ≥20 clean activations on a working milestone, no calendar deadline. Pin the milestone event; it is currently unmeasurable, not zero.
- EXD-023 (checkpoint 2026-07-28): sign-in regression framing refuted; WP-53 stays conditional on the first live `has_underlying_error` read. Do not change sign-in code before it.
- EXD-015 (Resumely primary), EXD-021 (Garmin tri-track → HealthKit focus), EXD-016 (Hebrew parked to 08-01), EXD-009/Gate A (monetization closed): all in force, carried forward.
- Proposed EXD-024 (awaiting founder confirmation): no further RunSmart feature expansion before 2026-08-01; the 1.1.3 route feature was a maintenance repair, not a re-entry into RunSmart product investment.

## Plan Board

- `BUSINESS-GTM-PLAN-V0.md`: COO drafts one post-cohort packet after the 2026-07-25 Resumely read and the 2026-07-28 RunSmart sign-in read.
- RunSmart Hebrew-first playbook: parked under EXD-016; 2026-08-01 revisit packet only.
- RunSmart iOS GTM plan: stays sign-in-and-cohort-gated, not a volume packet.
- Resumely FTUX/activation: get 1.4.6 through review; pin the activation milestone; take the 2026-07-25 read.
- Seven research briefs remain `research_only`; no execution assignment this week.

Source: `dashboard/status.json` `planExecution`.

## Risk Board

- Resumely activation is unmeasurable, not zero: the milestone event is unnamed (`export_success` no longer fires).
- RunSmart build attribution is unreliable: 76% of non-founder event volume is unversioned.
- The 1.4.5 failure cluster (`optimization_state_recovery_failed`, 10 persons) reaches real users; the WP-53 fix is stuck in App Store review inside 1.4.6.
- Focus dilution: RunSmart consumed a route build + release during Resumely's primary window (bounded by proposed EXD-024).
- Finance: revenue, costs, burn, and runway remain unknown.

## Weekly Review

- Current review: `executive-os/reviews/2026-07-24-weekly-ceo-review.md`.
- Prior review preserved: `executive-os/reviews/2026-07-17-weekly-ceo-review.md`.
- No new row written to `EXECUTIVE-DECISIONS.md` this session. One decision recommended (EXD-024) and left for founder confirmation rather than logged as Decided.

## Next Actions

1. Founder: archive + submit RunSmart 1.1.3 (28); get Resumely 1.4.6 through App Store review.
2. Analytics: pin the Resumely activation milestone event, then run the 2026-07-25 founder-excluded read.
3. Analytics: read RunSmart `has_underlying_error` on the first real 1.1.2 `sign_in_failed` (2026-07-28/29); decide WP-53 on it.
4. Eng: investigate the 554 null-`app_version` RunSmart events before trusting any RunSmart build cohort.
5. Founder: confirm or reject proposed EXD-024.
6. Founder: build the one-time manual recurring-cost list before the next CFO review.
