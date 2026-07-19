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

## P0 escalation (added 2026-07-19 evening) — RunSmart's wall may be broken, not just unpersuasive

Re-examining two people the first pass discarded as a "QA pair" reversed the priority order. **Every fresh install that actually tapped Sign in with Apple failed:** 7 non-cancel `ASAuthorizationError` code-1000 events across 3 devices and 2 builds (iPhone99,7 and iPhone12,1 on public 1.0.9 on 07-15; iPhone17,2 on build 24 today), **0 successes on any of them**. The only `sign_in_completed` on 1.0.9 is the founder's already-provisioned iPhone 13.

Supabase `auth` logs covering today's 11:03-11:04 UTC failures contain **no `/token` request at all** — the failure happens on-device, before Supabase is contacted, which rules out `provider_disabled` for that window. Not proven as an outage: code 1000 is also produced by a device with no iCloud account and by locally-installed builds lacking the SIWA capability, and build 24 was not an App Store install. The 07-19 device test meant to settle this is BLOCKED (device went `unavailable` before SignInView was reached).

**Sequencing consequence:** a new **S0** — one clean SIWA attempt on the public binary from an iCloud-signed device, ~20 minutes, founder-only — now precedes RunSmart S1/S2, because a broken door invalidates S2's premise. Detail: RunSmart repo `docs/plans/2026-07-19-activation-cliff-fix-plan.md`.

## Decisions implied (with options and costs)

1. **RunSmart S0 first (20 minutes, founder-only):** settle whether sign-in works for new users. Fails → production outage, outranks everything in the portfolio. Succeeds → the wall is persuasion and the order below stands.
2. **Resumely S2 telemetry (recommended engineering slot this week):** the top fix (tappable "Sign in to Optimize" + diagnosis persistence) already shipped in 1.4.3; half a day of `score_screen_signin_tapped` + picker outcome events + `job_source` makes the post-approval read attributable. Highest lift-per-hour, and Resumely is primary with a window closing 2026-08-01.
3. **RunSmart: instrument, then de-wall.** S1 = wall telemetry (1 day) in **1.1.1**, now also attaching `error_domain`/`error_code` so S0's question self-answers for every future user; session replay only behind privacy guardrails. S2 = value-preview or guest onboarding (2-3 days). Cost of skipping: another month of ~25 installs poured into a 95.7% first-screen loss.
3. **Build-21 question: closed as unverifiable.** Zero organic users have generated a plan on 1.0.9+, so plan->run has no denominator. The sheet works mechanically (founder-suspect device chose "Remind me", which correctly schedules a reminder instead of starting a run).
4. **Do not buy traffic for either app** until the respective gate fix ships. Both funnels destroy installs before value.

## Measurement hygiene (portfolio-wide, act on next readout)

- Resumely: always exclude founder email, `+fable-qa*`/`+export-wall*`, `is_internal_tester=true` (45 persons, 1,216 events in 90d), and QA burst chains (>=3 events/sec; suites ran 06-23..27 and repeatedly through 07-18). Raw dashboard numbers (26 optimizations, 5 exports) are ~90% non-organic.
- RunSmart: no `is_internal_tester` flag exists; add it (S5 in plan). Behavioral heuristics (>=6 sessions / >=3 versions) remain mandatory meanwhile.
- Instrumentation debt is itself an activation blocker: RunSmart has no event at its kill screen and useless `$screen` names. Both apps have session replay off. (Corrected: Resumely's `free_ats_completed` **does** carry `score_bucket` — see the same-day correction above; the missing Resumely telemetry is the sign-in CTA tap, picker outcomes, and job source.)
- Tooling gotcha (cost us an hour today): the PostHog MCP session started with its banner claiming project 171597 while actually serving 270848. Explicitly `switch-project` and fingerprint (total events/people) before trusting any cross-project read.

## What was NOT concluded

- Whether RunSmart bouncing is "unwilling to sign in" vs "unable to sign in". **Partly advanced, not closed:** for the 3 fresh installs that did tap, sign-in failed 100% of the time (see P0 escalation). For the other ~19 who emitted nothing at all, the question is still open — S0 settles the mechanism, S1 settles it for every future user.
- Whether Resumely's low scores additionally depress optimize-intent. Score data now exists and is unflattering (every real free-ATS user scored <=60, half <=40), but scrape quality cannot yet be separated from resume quality — the `job_source` property in S2 resolves it.
- One clean Resumely person (`712cf425`) did fully activate once (06-14 cohort); lifetime organic activation is 0 or 1 depending on that classification. Either way it rounds to zero.
