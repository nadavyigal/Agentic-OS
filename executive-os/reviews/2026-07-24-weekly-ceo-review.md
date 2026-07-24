# Weekly Executive Summary - 2026-07-24

- Status: current, with explicit immaturity and data-integrity caveats
- Reviewed: 2026-07-24 (Friday)
- Portfolio trust: `Refresh required` (dashboard prose lags live git + store; both apps are further along than the banner reads). Source: `dashboard/status.json` `portfolioTrust`, reconciled against Apple lookup API and live git this session.
- Open executive decisions: 0 rows with Status `Open` in `EXECUTIVE-DECISIONS.md`. Two Decided rows carry live review checkpoints: EXD-022 (2026-08-01) and EXD-023 (2026-07-28).
- Sources: Apple lookup API (2026-07-24, store ground truth); live PostHog reads projects 171597 + 270848 (2026-07-24, this session, founder + `nadav.yigal` QA excluded); live git across five repos; `EXECUTIVE-DECISIONS.md` (EXD-022/023, both 2026-07-21, EXD-023 updated 2026-07-22); `EXECUTIVE-METRICS.md`; the 2026-07-21 weekly review; the 2026-07-17 CEO review.

## Operating Read

The last CEO review (2026-07-17) opened on an unresolved RunSmart sign-in P0 and both apps on older builds. Both premises have moved. On 2026-07-22 both apps went live on new builds: **RunSmart 1.1.2 (27)** and **Resumely 1.4.5 (15)**, store-verified today. The sign-in P0 was **refuted** the same day (EXD-023 update, 2026-07-22): first-time Sign in with Apple works; it fails for *some* users on 3 real devices with a bare `ASAuthorizationError 1000`, cause still unnamed. This week's RunSmart work shipped the repaired route feature as **1.1.3 (28)** (merged today, awaiting founder archive), and Resumely shipped its first `requestReview` prompt, now packaged as **1.4.6** and sitting in App Store review.

The measurement contract held. Today's arrival check (the gate carried since 2026-07-22) **passed for both apps**: non-founder events are landing carrying the new version strings. RunSmart 1.1.2 shows 164 events across 5 non-founder persons since release; Resumely 1.4.5 shows 457 events across 15. The pipeline works, so build-keyed reads are now trustworthy to take, subject to the two integrity caveats below.

Two things the arrival check surfaced that matter more than the pass:

1. **Resumely's funnel is no longer dead at optimization.** On 1.4.5 (founder-excluded, 6-day window): ~12 persons launched, `optimization_completed` reached 10 persons, `submit_package_saved` 5. The historical wall was "first seen → 0 exported" (`EXECUTIVE-METRICS.md`, 2026-07-12: 0/73). This is the first evidence the funnel moves past optimization. It is also only 2 days old and n≈12, so it is a directional signal, not a verdict. Preferred read window is 2026-07-25+ per the metrics file.
2. **The activation milestone event has changed and is not yet pinned.** `export_success` does not fire at all on 1.4.5; the working milestone is now one of `optimization_completed` / `submit_package_saved` / `save_success`. Until the exact milestone is named, EXD-022's "≥20 clean activations" gate cannot be counted. This is a WP-50/WP-51 follow-through, not a new problem.

Alongside the movement, a real failure cluster is visible on 1.4.5: `optimization_state_recovery_failed` (10 persons), `optimization_apply_failed` (4), `save_failed` (5). This is exactly what today's WP-53 fix targets, and WP-53 is in 1.4.6, which is stuck in Apple review. So the fix exists but is not yet in users' hands.

## Plan Progress

| Plan | Index status | Milestone progress | CEO recommendation |
|---|---|---|---|
| `executive-os/BUSINESS-GTM-PLAN-V0.md` | needs_next_packet | Both apps live; measurement now trustworthy but cohorts immature | COO drafts one post-cohort packet after the 2026-07-25 Resumely read and the 2026-07-28 RunSmart sign-in read; no monetization/GTM-volume before evidence changes |
| RunSmart Hebrew-first playbook | needs_next_packet | Parked by EXD-016 until 2026-08-01 | COO holds; dated 2026-08-01 revisit packet only |
| RunSmart iOS GTM plan | needs_next_packet | Live, but sign-in cause unnamed and version-tagging unreliable | Stays sign-in-and-cohort-gated; not a volume packet |
| Resumely FTUX / activation | current execution track | 1.4.5 live with a moving funnel; 1.4.6 (WP-53 + review prompt) in App Store review | Get 1.4.6 through review; pin the activation milestone; take the 2026-07-25 read |
| RunSmart route feature | shipped this week | 1.1.3 (28) merged; route creator, reachable detail, cloud persistence | Founder archive + submit; then no further RunSmart feature expansion before 2026-08-01 (see proposed EXD-024) |

Source: `dashboard/status.json` `planExecution`; EXD-016; this session's git + PostHog reads.

## Top 3 Priorities

1. **Take the two reads that decide the next moves, and not before their windows.** Resumely: on/after 2026-07-25, pin the activation milestone event and count clean activations toward EXD-022's 20. RunSmart: on the first real 1.1.2 `sign_in_failed` (EXD-023 checkpoint 2026-07-28, T+7 2026-07-29), read `has_underlying_error` — `true` names the precondition and fixes with copy plus a check; `false` opens WP-53. Source: EXD-022, EXD-023, `EXECUTIVE-METRICS.md`.
2. **Ship the two builds already made.** RunSmart 1.1.3 (28) is merged and build-verified (device-smoke waived by founder); archive + submit. Resumely 1.4.6 carries the WP-53 recovery fix that addresses the 1.4.5 failure cluster plus the review prompt; get it through App Store review. Both are founder-only from here. Source: this session; `RunSmart iOS tasks/progress.md`.
3. **Fix RunSmart's analytics version-tagging tail before trusting any RunSmart build-split.** Today's read shows 554 events across 17 non-founder persons with **null** `app_version` versus 164 / 5 on 1.1.2. A majority of RunSmart event volume is unversioned, so any build-split cohort (including the sign-in read's denominator) is unreliable. Either the 1.1.1 "app_version after fresh install" fix is incomplete or lifecycle/autocapture events dominate the tail. Source: PostHog 171597, 2026-07-24.

## Key Decisions

No `Open`-status rows exist in `EXECUTIVE-DECISIONS.md`. Recommendation for each live checkpoint and standing decision:

| Decision | Status | Recommendation this week |
|---|---|---|
| **EXD-022** (activation target = ≥20 clean activations, no deadline; 08-01 checkpoint) | Decided 2026-07-21 | Hold. Treat 2026-08-01 as a written progress read, not a verdict. Pin the activation milestone event first; the 1.4.5 funnel now moves but the milestone is unnamed, so the count is currently unmeasurable, not zero. |
| **EXD-023** (sign-in verdict; regression framing refuted 2026-07-22) | Decided 2026-07-21, updated 2026-07-22 | Keep WP-53 conditional. Do not open the guest/email fallback or touch sign-in code before the 2026-07-28 `has_underlying_error` read. The refutation stands: it fails for some, not all. |
| EXD-015 (Resumely primary; RunSmart Garmin maintenance) | In force | Carry forward. Resumely stays primary through the 08-01 window. |
| EXD-021 (Garmin tri-track; RunSmart focus → HealthKit) | In force | Carry forward; no Garmin relaunch engineering this week. |
| EXD-016 (RunSmart Hebrew distribution parked) | In force | Parked until 2026-08-01. |
| EXD-009 / Gate A (monetization closed) | In force | Keep closed until activation evidence supports reopening. |

**Proposed new decision for founder confirmation — EXD-024 (not logged as Decided):** RunSmart 1.1.3's route feature shipped as a *maintenance repair* of a broken existing differentiator during Resumely's primary window, which is defensible. Recommend recording an explicit boundary: **no further RunSmart feature expansion (routes, HealthKit build-out, or otherwise) before the 2026-08-01 checkpoint**, so the route fix does not become a re-entry into RunSmart product investment while Resumely is primary. This needs the founder's yes before it is written into `EXECUTIVE-DECISIONS.md`.

## Stop-Doing List

- Do not convert the 1.4.5 or 1.1.2 cohorts into an activation *rate* before their read windows (Resumely 2026-07-25, RunSmart sign-in 2026-07-28) and before the Resumely activation milestone event is pinned.
- Do not open WP-53 or change RunSmart sign-in code before the `has_underlying_error` read.
- Do not start new RunSmart feature work beyond archiving the shipped 1.1.3 route fix.
- Do not trust any RunSmart build-split number until the null-`app_version` tail is explained.
- Keep Gate A / monetization closed; Garmin relaunch and Hebrew distribution parked.

## Delegation List

| Priority | Owner / workflow | Assignment |
|---|---|---|
| Resumely activation read | Analytics / CEO OS | Pin the milestone event, then run the 2026-07-25 founder-excluded read; report count toward EXD-022's 20 |
| RunSmart sign-in read | Analytics / CEO OS | On first real 1.1.2 `sign_in_failed` (2026-07-28/29), read `has_underlying_error`; decide WP-53 on it |
| RunSmart 1.1.3 (28) | Founder | Archive → upload → submit (device-smoke waived) |
| Resumely 1.4.6 | Founder | Merge / get through App Store review; it carries the WP-53 fix for the 1.4.5 failure cluster |
| RunSmart version-tagging tail | Eng session | Investigate the 554 null-`app_version` events; confirm whether the 1.1.1 fresh-install fix is incomplete |
| Three needs_next_packet plans | COO OS | Keep gated; draft post-read packets only after 2026-07-25/28 |
| Finance cost list | Founder | Build the one-time manual recurring-cost list before the next CFO review (carried from 2026-07-17, still open) |

## Top Risks

1. **Resumely activation is currently unmeasurable, not zero.** `export_success` no longer fires and the replacement milestone is unnamed, so EXD-022's gate cannot be counted until it is pinned. Same class as the WP-51 milestone defect. Source: PostHog 270848, 2026-07-24.
2. **RunSmart build attribution is unreliable.** 76% of non-founder RunSmart event volume this week is unversioned (554 vs 164). The sign-in read's denominator inherits this. Source: PostHog 171597, 2026-07-24.
3. **The 1.4.5 failure cluster reaches real users and the fix is stuck in review.** `optimization_state_recovery_failed` hit 10 persons; the WP-53 remedy is in 1.4.6, which Apple has not yet approved. Source: PostHog 270848, 2026-07-24; RunSmart/Resumely iOS `tasks/`.
4. **Focus dilution toward the secondary product.** RunSmart consumed a route-feature build and a release this week during Resumely's primary window. Defensible as maintenance, but unbounded without EXD-024. Source: this session's git.
5. **Financial visibility remains zero.** Revenue, cost, burn, and runway are still `Needs Data`; only `$0` marketing spend is tracked. Source: `EXECUTIVE-METRICS.md`; 2026-07-09 finance review.

## Recommended Next Actions

1. Founder: archive + submit RunSmart 1.1.3 (28); get Resumely 1.4.6 through review.
2. Analytics: pin the Resumely activation milestone event, then take the 2026-07-25 read counting toward EXD-022's 20.
3. Analytics: read RunSmart `has_underlying_error` on the first real 1.1.2 `sign_in_failed` (2026-07-28/29); decide WP-53 on the value.
4. Eng: investigate the 554 null-`app_version` RunSmart events; confirm whether the 1.1.1 fresh-install fix is incomplete before trusting any RunSmart build cohort.
5. Founder: confirm or reject proposed EXD-024 (RunSmart feature-expansion boundary through 2026-08-01).
6. Founder: build the one-time manual recurring-cost list before the next CFO review.

## Dashboard Updates Applied

- Replaced the stale 1.0.9 / 1.4.2 / unresolved-P0 view with the current 1.1.2 / 1.4.5 live state, the refuted sign-in framing, and today's arrival-check pass.
- Replaced the 2026-07-12 mature baseline framing with the 1.4.5 funnel movement plus the activation-milestone and version-tagging integrity caveats.
- Recorded the two live decision checkpoints (EXD-022 08-01, EXD-023 07-28) and the proposed EXD-024.
- Preserved the 2026-07-17 review as history.
