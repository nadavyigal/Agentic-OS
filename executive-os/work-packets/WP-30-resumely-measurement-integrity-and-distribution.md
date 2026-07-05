# Work Packet WP-30 - Resumely: Measurement Integrity + Distribution Ignition (Demo 3)

- Status: **READY** (created 2026-07-03, not started)
- Created: 2026-07-03
- Source: Demo 3 live PostHog read (2026-07-03, project 270848 + 171597, all claims from SQL against live events, founder+QA excluded). Vault note: `02-Products/ResumeBuilder/2026-07-03-resumely-usage-goals-baseline.md`
- Mode: Builder + one HUMAN gate
- Workflow pattern: one story at a time (implement → verify with a live PostHog query → next)
- Outcome loop: Resumely 20% real activation / 30 days (founder decision 2026-07-02)
- Related: WP-29 (funnel fixed, DONE 2026-07-03), NEXT-MOVES "Hebrew-first distribution playbook" Shaping entry (2026-07-01)
- Success signal: (1) web `$pageview` events with `$lib='web'` flowing again on production, verified by a live query; (2) ~~zero new `com.runsmart.lite` events in project 270848~~ already true, confirmed 2026-07-04 (see S2 closure); (3) a distribution decision made and the first channel live; (4) next weekly readout computes both platform funnels from clean data without manual caveats

## The evidence (live SQL, 2026-07-03, founder+QA excluded)

**The funnel is no longer the constraint. Distribution is.**

- iOS weekly unique people launching (last 5 weeks): **4 → 7 → 15 → 28 → 4**. The 06-22 launch-push week brought 28 people and **64% of them started a fit check** — motivated traffic converts. The current week has 4 people. 20% of ~nothing is nothing.
- iOS 30d funnel: 49 launched → 18 fit check started → 18 completed → 9 uploaded resume → 3 optimization completed → 3 exported.
- Web 30d: ~15 pageview-people total, then client-side capture died entirely (below).
- Interpretation flip worth recording: the "63% bounce before the core action" from the 07-02 read is a *cold/mixed-traffic average*. The launch-week cohort bounced only 36%. First-screen UX is not the primary lever at this traffic level — getting sustained motivated traffic is.

**Three data-integrity defects found (all verified live):**

1. **P0 — Web client-side capture dead since 2026-07-01 03:05 UTC.** posthog-js initializes on production (config.js + /flags requests fire, SDK v1.310.1) but issues zero capture requests; `window.posthog` is undefined. Last `$lib='web'` event: 07-01 03:05. The entire WP-29 walkthrough (today) produced no client events; only server-side `posthog-node` events recorded it. Timing correlates with PR #98 "Add PostHog LLM observability" (merged 06-30 20:02 +03; touched `.env.example` + server analytics paths).
2. ~~**P1 — RunSmart iOS double-sends its full event stream into the ResumeBuilder project.**~~ **RETRACTED 2026-07-04 — see Progress log.** Originally claimed every `com.runsmart.lite` event (app_launched, garmin_sync_completed, run_completed, etc.) appeared in BOTH project 171597 (Running coach) and 270848 (ResumeBuilder AI) with identical counts since ~06-07. A 2026-07-04 live query found zero RunSmart-lib events in project 270848 over 90 days, and a RunSmart iOS repo audit (Codex) found only one PostHog token wired (`phc_2Rcj...`, matching project 171597) with no trace of the ResumeBuilder token in current code or git history since 06-01. Most likely explanation: the original 07-03 finding came from a misattributed query, not an actual double-send. Closed as non-issue — no code change made or needed.
3. **P2 — Server-side duplicate event pairs.** `posthog-node` emits both `expert_mode_run_started` AND `expert_run_started` (68/68 identical), same for `_completed` and `_apply` pairs — double instrumentation, half of it legacy names.

## Model Routing (per GLOBAL-TOOL-USAGE.md tiers)

| Story | Work type | Route |
|---|---|---|
| S1 web capture restore | Debugging a silent client-side failure, correctness-critical for all measurement | **Opus/Fable** (Claude Code) or founder-run Cursor with the diagnosis below |
| ~~S2 RunSmart token unwire~~ | **CLOSED — non-issue, 2026-07-04** | ~~Codex/Cursor (RunSmart iOS repo)~~ |
| S3 server event dedupe | Mechanical rename/removal, well-specified | **Haiku/Codex** |
| S4 PostHog hygiene (exclusion cohort + annotations) | Config via PostHog MCP, low risk | **Sonnet** |
| S5 distribution decision | Founder judgment | **HUMAN gate** |

## Project(s)

- ResumeBuilder Web: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-` (S1, S3)
- RunSmart iOS: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app` (S2)
- PostHog org `Nadav Yigal AI advisory` (S4)

## Task

### S1 — Restore web client-side capture (P0) — **Opus/Fable**
Diagnosis so far: SDK initializes (config/flags fire) but no `/e/` or `/i/v0/e/` capture requests ever leave the browser; `$pageview` stopped 07-01 03:05 UTC; PR #98 (merged 06-30 evening) is the prime suspect — it touched analytics paths and `.env.example`. Start there: diff #98 for anything affecting `src/lib/posthog.ts` / `src/components/providers/posthog-provider.tsx` import paths or env names; verify `NEXT_PUBLIC_POSTHOG_KEY` still exists in Vercel production env (an env rename during #98's new server-key addition is the classic cause); check whether the provider still mounts after the layout changes. Acceptance: a fresh production visit produces a `$pageview` with `$lib='web'` visible in PostHog within minutes, verified by live query, plus a regression test or CI check that fails when the provider stops capturing (e.g. an e2e asserting a capture request fires).

### S2 — CLOSED, non-issue (2026-07-04)
Originally: stop RunSmart iOS sending to the ResumeBuilder project. Codex audit of the RunSmart iOS repo (`RunSmartConfig.xcconfig`, `RunSmartInfo.plist`, `project.pbxproj` Debug+Release, `RunSmartLiteAppShell.swift`, `AnalyticsService.swift`) found exactly one PostHog token wired end-to-end (`phc_2Rcj...`, project 171597) with no trace of `phc_UmPZ...` in current files or git history since 06-01. No commit since 06-07 touched PostHog config. Combined with the 07-04 live query (zero RunSmart-lib events in project 270848 over 90 days), the double-send never existed in this repo as described — closing without a code change.

### S3 — Dedupe server-side expert events (P2) — **Haiku/Codex**
In the web repo's server analytics, `expert_mode_run_started`/`expert_run_started` (and `_completed`, `_apply` pairs) are captured twice per action under legacy + new names. Pick the canonical name (match whatever dashboards/insights reference), delete the other capture call. Acceptance: one event per action in a live test; note which name was kept in the packet.

### S4 — PostHog hygiene — **Sonnet**
1. Create a reusable exclusion cohort in project 270848: founder person(s) (nadav.yigal@gmail.com) + all `+fable-qa*` aliases, so every insight/funnel filters by cohort instead of ad-hoc email clauses.
2. Add PostHog annotations: 2026-07-01 03:05 "web client capture blackout begins", the S1 fix date "web capture restored", and ~2026-06-07 "RunSmart double-send pollution begins" / S2 fix date end.
3. Re-check the Founder Daily Readout dashboard's insights for the two `app_launched` sources — add `$lib` filters where missing.
Acceptance: cohort exists and is referenced by the daily-readout insights; annotations visible on trends.

### S5 — Distribution decision (HUMAN gate) — **Founder**
The data says the constraint is traffic: best week ever was 28 people (a one-off push), current week is 4. The Hebrew-first distribution playbook has been drafted since 06-22 (`distribution-os/projects/runsmart/scaffold/hebrew-first-playbook.md` — written for RunSmart but the channel thesis is the Israeli job-seeker community, which fits Resumely at least as well) and sits unapproved in NEXT-MOVES Shaping. Decide: (a) adapt the Hebrew-first playbook to Resumely and ship the first channel this week, (b) different channel (ASO push, LinkedIn/job-seeker communities, content), or (c) explicitly park distribution and accept the activation goal slips. Whatever the choice, promote it to its own work packet — this packet only carries the decision.

## Constraints

- One story at a time; every acceptance criterion is a **live PostHog query or production check**, not a code-level claim (WP-29's S1 lesson).
- Do not modify PostHog project settings beyond S4's scope; no project deletions or merges without the founder.
- QA traffic exclusions per memory `resumely-qa-test-account` and `posthog-founder-account-exclusion`.
- No new npm/Swift dependencies without asking. No secrets in code.

## Validation

- S1-S3: before/after live SQL snapshots in this packet's Progress log.
- S4: cohort + annotations linked.
- Weekly readout after S1 lands is the first trustworthy full-funnel read; compare against the 2026-07-03 baseline in the vault note.

## Progress

- 2026-07-03: Packet created from Demo 3 live data read. Not started.
- 2026-07-03: S1 handed to Cursor (founder-run) in the ResumeBuilder web repo with the PR #98 diagnosis. S5 decided: (a) adapt Hebrew-first playbook to Resumely — drafted at `distribution-os/projects/resumebuilder/scaffold/hebrew-first-playbook.md` (status: draft, approved: no). `rb-he-aso-001` (Hebrew ASO, no S1 dependency) is the first channel to promote to its own work packet; `rb-he-web-001` stays blocked on S1 verification.
- 2026-07-03/04: **S1 finding corrected.** Cursor traced PR #98 and cleared it — no touch to the client capture path, `NEXT_PUBLIC_POSTHOG_KEY` intact in Vercel prod, provider still mounts. Live PostHog data (project 270848, `$pageview` by `$lib`, 06-23 to 07-03) shows capture was never a full blackout — it was sparse/low-volume throughout, with a drop from 12 (06-29) to near-zero starting 06-30, a day before the originally-suspected 07-01 03:05 UTC timestamp. Root cause was never conclusively isolated to a single break event; contributing factors identified: no `posthog.identify()` wired, automatic + manual pageview double-counting, no init idempotency guard (React Strict Mode double-fires). Incognito live test 2026-07-03 confirmed `/e/` returns 200 and `$pageview` lands — capture itself works when a real visit happens; the "blackout" framing in this packet's original evidence section is superseded by this finding.
- 2026-07-04: [PR #109](https://github.com/nadavyigal/new-ResumeBuilder-ai-/pull/109) (`fix/posthog-client-hygiene`) merged 05:17:59 UTC and deployed to Vercel production: `capture_pageview: false` (avoids duplicate with manual SPA tracking already in `posthog-provider.tsx`), `posthog.__loaded` init guard, `posthog.identify()`/`reset()` wired to Supabase auth state. Code-reviewed before merge — safe, scoped (19+/2- lines, 2 files). Post-deploy production-visit verification pending (only post-merge `$pageview` seen so far was from a Vercel preview URL, not production).
- 2026-07-04: **S4 done.** Created `Founder + QA exclusion` cohort (id 394227, project 270848) matching founder email + `+fable-qa*` aliases. Added 3 PostHog annotations: 06-30 (pageview drop, corrected framing), 07-04 05:17:59 (PR #109 deploy), 06-07 (RunSmart double-send pollution start, approximate). Updated both Founder Daily Readout insights (`Weekly active users`, `30d activation funnel steps`) to filter by the new cohort instead of the ad-hoc founder-email-only filter.
- 2026-07-04: **P1/S2 finding could not be reproduced live.** Queried project 270848 events over the last 90 days for any RunSmart-lib traffic (`$lib` values other than `resumely-ios-urlsession`/`web`/`posthog-node`, and events named `garmin_sync_completed`/`run_completed`) — zero results. `app_launched` in this project is 100% `resumely-ios-urlsession` over the last 30 days. Did not add a speculative `$lib` filter to the funnel insight without evidence.
- 2026-07-04: **S2 closed as non-issue.** Codex audited the RunSmart iOS repo (config files, build settings for both Debug and Release targets, analytics init code, git history since 2026-05-26). Found a single PostHog token (`phc_2Rcj...`) wired everywhere, matching RunSmart's own project 171597; no trace of the ResumeBuilder token (`phc_UmPZ...`) anywhere in current code or reachable git history, and no PostHog-config commit since 06-07 (the claimed contamination start date). Combined with the live-query result above, the original P1 finding is retracted — most likely a misattributed query in the 07-03 evidence-gathering session, not an actual double-send. No code change made. P1 struck through in the Evidence section; Model Routing table updated.
- 2026-07-04: **S5 promoted.** [WP-31](WP-31-resumely-hebrew-aso-pass.md) created for `rb-he-aso-001` (Hebrew ASO pass) — no S1 dependency, founder publish gate, 21-day measurement window per the playbook.
