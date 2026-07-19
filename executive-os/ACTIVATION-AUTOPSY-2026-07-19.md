# Portfolio Activation Autopsy: 2026-07-19

One page. Source: live PostHog reads this session (projects 171597 + 270848, 90d, founder/QA/bot-excluded). Full evidence + backlogs:
- RunSmart iOS repo: `docs/plans/2026-07-19-activation-cliff-fix-plan.md`
- Resumely iOS repo: `docs/plans/2026-07-19-activation-cliff-fix-plan.md`

## Same-day update: both apps submitted to ASC (2026-07-19 evening)

- **RunSmart 1.1.0 (24) Waiting for Review** (public 1.0.9 (23)): ships Adaptive Coach Phase 1 flag-ON; contains **none** of the wall fixes. The Adaptive Coach Phase 2 gate (2 weeks live + >=20 real `adaptive_coach_shown` users) is arithmetically unfillable while ~96% of installs die on the wall (~25 organic installs/month x 4% past the wall = ~1 real user/month reaching Today). S1 (wall instrumentation) should be the first content of 1.1.1.
- **Resumely 1.4.3 (13) Waiting for Review** (public 1.4.2 (12)): WP-46 Release C **partially ships the top fix** (tappable "Sign in to Optimize" under the guest score card + diagnosis persistence across sign-in). Remaining: the CTA tap is uninstrumented. Judge the fix on the post-1.4.3 cohort: >=20 clean uploaders, win at >=30% optimization_started (baseline 12.5%).
- **Correction to the original read:** `free_ats_completed` DOES carry `score_bucket` (first query used wrong names). Live 90d: 5 events "0-40", 5 events "41-60" — every real free-ATS user saw <=60, half <=40. Low score + (pre-1.4.3) dead-end screen hit at the same moment.

## The two numbers that matter

| Product | Biggest cliff | Clean number |
|---|---|---|
| RunSmart iOS | Install -> sign-in wall (first screen) | **22/23 organic App Store users (95.7%) quit before starting onboarding.** 0/23 ever started a run. D7 activation 0/19 mature. |
| Resumely (iOS+web) | Upload -> optimization | **14/16 real uploaders (87.5%) never start an optimization.** Clean: 145 reached -> 16 uploaded -> 2 optimized -> 1 exported. D7 ~0%. |

## Same disease, both apps

Both products put a **hard gate before the moment of felt value**, and both are **analytically blind at exactly that gate**:

- RunSmart: Sign-in-with-Apple wall as the literal first screen (`RunSmartLiteAppShell.swift:184`), no guest mode, no event fires between app-launch and a sign-in attempt. Result: 95.7% silent bounce.
- Resumely: guests can upload and get a free score, but optimization requires auth and the score screen's only path forward is a **non-tappable caption** "Sign in to unlock full resume optimization." (`ScoreResultView.swift:111`). Motivated users retried for weeks (one: 8 uploads, 6 free scores, 0 optimizations) and then quit.

Resumely is structurally healthier: 14% of reachers attempt upload (vs 4% of RunSmart installs starting onboarding). Its wall sits AFTER users demonstrate intent, so fixing it pays immediately. RunSmart's wall sits before any value is shown, so nothing downstream (plans, first-run sheet, Garmin) can matter until it moves.

## Decisions implied (with options and costs)

1. **Resumely S1 first (recommended this week):** tappable inline sign-in on the score screen + anonymous-session carryover. Effort S/M. Moves uploaded->optimization_started (12.5% -> target 40%). This is the single highest lift-per-effort item in the portfolio and aligns with Resumely-primary.
2. **RunSmart: instrument, then de-wall.** S1 = wall telemetry + session replay (1 day) in 1.0.10; S2 = value-preview or guest onboarding (2-3 days). Without S1, every future RunSmart debate stays faith-based. Cost of skipping: another month of ~25 installs poured into a 95.7% first-screen loss.
3. **Build-21 question: closed as unverifiable.** Zero organic users have generated a plan on 1.0.9+, so plan->run has no denominator. The sheet works mechanically (founder-suspect device chose "Remind me", which correctly schedules a reminder instead of starting a run).
4. **Do not buy traffic for either app** until the respective gate fix ships. Both funnels destroy installs before value.

## Measurement hygiene (portfolio-wide, act on next readout)

- Resumely: always exclude founder email, `+fable-qa*`/`+export-wall*`, `is_internal_tester=true` (45 persons, 1,216 events in 90d), and QA burst chains (>=3 events/sec; suites ran 06-23..27 and repeatedly through 07-18). Raw dashboard numbers (26 optimizations, 5 exports) are ~90% non-organic.
- RunSmart: no `is_internal_tester` flag exists; add it (S5 in plan). Behavioral heuristics (>=6 sessions / >=3 versions) remain mandatory meanwhile.
- Instrumentation debt is itself an activation blocker: RunSmart has no event at its kill screen and useless `$screen` names; Resumely's `free_ats_completed` carries a null score. Both apps have session replay off.
- Tooling gotcha (cost us an hour today): the PostHog MCP session started with its banner claiming project 171597 while actually serving 270848. Explicitly `switch-project` and fingerprint (total events/people) before trusting any cross-project read.

## What was NOT concluded

- Whether RunSmart bouncing is "unwilling to sign in" vs "sign-in silently failing" (blind screen; S1 resolves).
- Whether Resumely's low scores (scrape quality) additionally depress optimize-intent (score telemetry null; S2 resolves).
- One clean Resumely person (`712cf425`) did fully activate once (06-14 cohort); lifetime organic activation is 0 or 1 depending on that classification. Either way it rounds to zero.
