# Portfolio Activation Strategy Synthesis — 2026-07-11

Single prioritized plan across RunSmart iOS and Resumely iOS, synthesized from every activation input generated 2026-07-11: the WP-41/WP-42 raw HogQL funnel autopsies (Codex), the Resumely web export-instrumentation fix (Cursor, PR #114 merged), the competitor activation teardown (Cursor/Grok), the upgraded right-user demand-mining brief (Cursor/Grok, primary sources), and two ready-to-execute activation packets (WP-43 web, WP-44 iOS) authored from live product walkthroughs. Filed to close the loop the founder opened by running the "6 model-task examples" exercise this session.

## The honest starting point

Neither app has a proven activation number yet. Both targets are still aspirational, not directional:

| App | Priority (EXD-015) | Target | Last read | Verdict |
|---|---|---|---|---|
| Resumely iOS | **Primary** | 20% real, founder-excluded, launch→export, within 30d (by 2026-08-01) | WP-41 (2026-07-11): **0 clean cohort** — 1.4.1 (11) went live today; no post-live cohort exists yet | Too early to read. Re-read gate: 2026-07-18 minimum, 2026-07-25 definitive |
| RunSmart iOS | Secondary (Garmin parked, HealthKit-redirected per EXD-021) | D7 activation ≥30% | WP-42 (2026-07-11): **0 clean cohort** — WP-40 S1+S2 merged today; the 1 disclosure-viewer found is TestFlight/sideload-contaminated | Re-read gate: **2026-07-12** (tomorrow) when the pre-WP-40 cohort matures — but this will almost certainly still read as "too early," since WP-40 itself only shipped hours ago |

Both apps also sit under EXD-013: no monetization, paywall, or paid-acquisition work until activation is understood. That gate is still active — nothing below proposes touching it.

Live engagement right now: Resumely 55 users/7d (real, growing base — this is the more valuable surface to protect), RunSmart 9 users/7d (thin; the 07-12 re-read cohort predates today's WP-40 ship, so a null result there is not evidence WP-40 failed).

## The 3 highest-leverage moves

### 1. Ship WP-43 (web) + WP-44 S1 (iOS) before the 07-18 minimum-check window

Both are sitting as open, unmerged PRs right now — [#115](https://github.com/nadavyigal/new-ResumeBuilder-ai-/pull/115) and [#92](https://github.com/nadavyigal/ResumeBuilder-IOS-APP/pull/92). This is the single highest-leverage action in the entire portfolio this week, for one reason: **the 07-18/07-25 Resumely funnel re-read will grade whatever entry funnel is live at that time.** If these packets ship this week, the re-read measures the fixed funnel. If they slip past 07-18, the founder pays for a full re-read cycle (the next one isn't until 08-01, which is also the hard activation-window deadline) against a funnel already known to be broken.

Both are low-risk: WP-43 is copy/design/client-only, no backend touch. WP-44 S1 is an app-only picker-directory fix, no backend dependency. Neither needs the founder to decide anything first — they're ready-to-execute stories with acceptance criteria already written.

WP-44 S2 (paste-resume-text, the actual root-cause fix for "no file on phone") has a real backend dependency that must be confirmed before building — don't let it block S1's ship.

### 2. Ship the two ASO/positioning copy fixes this week — copy-only, zero engineering dependency, doesn't wait for any cohort

This is the direct output of the demand-mining research, and it's uniquely valuable because it requires **no funnel data and no cohort to mature** — it can ship in parallel with everything else, today:

- **RunSmart:** fold the primary-sourced stat bank into the App Store description / ASO copy — Relph 2023's 27.3% C25K completion rate, Frandsen BJSM 2025's single-run->10%-of-30-day-longest injury mechanism, and the right-fit language bank ("too hard," "felt like a failure," "can't run a minute," "need walk breaks"). This directly targets wrong-fit traffic (race-aggressive users bouncing off a readiness-first product) as one candidate explanation for the 94.7% onboarding drop — cheap to test, doesn't touch the plan→run engineering problem, and is evidence-backed rather than a guess.
- **Resumely:** the TeamBlind-sourced "sounds like ChatGPT wrote it" complaint is a direct, low-cost copy angle ("sound like you, not generic AI") to pair with the already-shipped Match Score defensibility work. Both findings converge on the same message: Resumely's positioning should lean into *not* being another generic-AI, gameable-score tool.

Neither of these requires founder sign-off beyond approving the actual copy draft — which is explicitly still open per the demand-mining brief's own "decision needed" line.

### 3. Let the 07-12 RunSmart re-read run and land as a deliberate non-event — don't scramble to beat it

WP-40 S1+S2 merged today (2026-07-11); the 07-12 re-read cohort was defined before that merge, so it cannot reflect WP-40's impact. The correct move is to **let it read as "too early," document why in one line, and set the real WP-40 read for whenever the next mature cohort forms** — not to treat 07-12 as a deadline requiring new engineering. Treating it as a real deadline risks exactly the kind of rushed, unvalidated ship the portfolio's git-safety and verification norms exist to prevent. This costs nothing and prevents a wrong reaction to a known-uninformative data point.

## What to explicitly NOT build right now

- **Monetization, paywall, or paid acquisition on either app** — EXD-013 gate is still open; neither app has a proven activation number.
- **Garmin relaunch work** — EXD-015/EXD-020/EXD-021 park stands until 2026-08-01 or the עוסק מורשה registration lands, whichever comes first. Not a scheduling note, a standing decision.
- **RunSmart Hebrew-first distribution playbook** — EXD-016, parked until 2026-08-01, re-confirmed 2026-07-08. A second distribution lane before activation is understood is explicitly the risk this decision heads off.
- **RunSmart S13 (live calories/steps)** — gated on a HealthKit accuracy research spike that has not been run. Do not start UI work.
- **WP-44 S2 (paste-text) or S3 (OCR scan) before confirming the backend text-endpoint exists** — building the client half of a feature whose backend half is unconfirmed produces a UI that silently can't work. Verify first.
- **A LinkedIn-profile-as-resume import path** — already explicitly rejected in WP-44 (ToS violation, same datacenter-IP thin-scrape failure already documented for job-description scraping).
- **DOCX support on Resumely's free web path, or a resume-only first score** — both real, higher-leverage ideas (Tier B in WP-43), but both need backend work and should wait until the Tier A copy/UX fixes are measured first. Don't parallel-path backend scope before the cheap fix is even shipped.

## Sequencing: now → 2026-08-01

| When | Action | Who |
|---|---|---|
| This week (before 2026-07-18) | Merge WP-43 (web) + WP-44 S1 (iOS picker fix); ship RunSmart + Resumely ASO copy drafts | Codex/Cursor execution, founder approves copy |
| 2026-07-12 | RunSmart re-read runs, documented as "too early, WP-40 postdates this cohort" — no new engineering triggered by this date | Automated/Codex |
| 2026-07-18 | Minimum-check Resumely funnel re-read against the shipped WP-43/44 fixes — first real signal on whether the entry-funnel work moved the needle | Codex (HogQL autopsy, same methodology as WP-41) |
| 2026-07-25 | Definitive Resumely funnel re-read, 14-day clean cohort | Codex |
| Whenever the next mature post-WP-40 cohort forms | Re-run WP-42 for RunSmart's real HealthKit-onboarding read | Codex |
| 2026-08-01 | EXD-015's 30-day activation window closes; EXD-016/019/020/021 Garmin and Hebrew parks all come up for reconsideration in the same review | Founder + COO review |

## Confidence and caveats

This plan is built on two null-result autopsies (honest "no cohort yet," not fabricated percentages) and two research briefs that explicitly flag their own evidence gaps (no live Reddit/X scrape access this session; some quotes are secondary-aggregator-sourced, labeled as such). The 3 moves above are chosen specifically because none of them depend on resolving those gaps — they are actionable regardless of whether the demand-mining brief's weaker citations hold up under further scrutiny.

## Updates logged

- Filed: `executive-os/reviews/2026-07-11-activation-strategy-synthesis.md`
- No EXD change — this synthesizes existing decisions (EXD-013/015/016/019/020/021), does not open a new one
- Feeds the next COO operating review as the current best-next-action synthesis, superseding the 2026-07-09 review's "founder submits 1.4.1" framing (now stale — 1.4.1 is live)
