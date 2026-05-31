# Executive Dashboard

Manual source-of-truth dashboard for the Executive Intelligence OS. Updated by the
Weekly CEO Review and Monthly Finance Review workflows. No invented data: financial
cells stay `Needs Data` until a real source exists.

Last updated: 2026-05-31 (second Weekly CEO Review)

Status indicators: `Active` · `Watch` · `Blocked` · `Needs Decision` · `Needs Data`
· `Ready`

## Executive Summary

Two-app App Store submission sprint. RunSmart iOS is submit-ready (build 6 uploaded);
only App Store Connect portal tasks remain — those are human-only. Resumely iOS is in
the final pre-submission gate: PostHog is not integrated and screenshot upload needs
Fastlane / ASC credentials. Analytics is the highest-leverage unresolved risk for both
apps: RunSmart has SDK + core events but is missing the activation funnel; Resumely has
zero instrumentation. Financial picture remains fully `Needs Data`.

## CEO Focus

- **Primary:** RunSmart iOS — open App Store Connect portal and submit build 6.
- **Secondary:** Resumely iOS — integrate PostHog (2-day cap), then submit.
- **Hold:** no new feature scope until both apps clear submission review.

## Top 3 Priorities

1. RunSmart iOS — App Store Connect portal close-out: select build 6, upload 6.9" + 6.1"
   screenshots, enter demo credentials, confirm privacy / age rating, submit for review. `Active`
2. Resumely iOS — integrate PostHog SDK (2-day cap: `app_launched` + `optimize_completed`), then
   submit to App Store. `Active`
3. Analytics scope (EXD-002) — define and cap the instrumentation work for both apps so the
   decision to "instrument first" is operationalized, not just declared. `Needs Decision`

## Financial Snapshot

| Metric | Value | Status |
|---|---|---|
| Revenue (all products) | unknown — need: App Store Connect / RevenueCat | Needs Data |
| Total monthly cost | unknown — need: provider billing + manual list | Needs Data |
| Gross margin | derived once revenue + direct cost known | Needs Data |
| Net profit / loss | derived | Needs Data |
| Runway | unknown — need: cash on hand + burn | Needs Data |

See `CFO-OS.md` and `EXECUTIVE-METRICS.md` for the full schema.

## Product Portfolio Health

| Product | Health | Note |
|---|---|---|
| RunSmart iOS | Active | Submit-ready, build 6 uploaded; ASC portal close-out is the only gate |
| RunSmart Web | Watch | Source of product logic; steady |
| Resumely iOS | Active | Pre-submission; PostHog missing; screenshots need ASC credentials |
| ResumeBuilder Web | Watch | Output quality focus before monetization |
| Atlas | Watch | Future orchestration layer; not active |

## Monetization Board

| Item | Status | Next step |
|---|---|---|
| Pricing model per product | Needs Data | Run Pricing & Packaging Review (Phase 2) once apps are live |
| Trial / free boundary | Needs Decision | Defer until post-approval |
| Revenue instrumentation | Needs Data | Define RevenueCat / App Store source |

## Research / Opportunity Board

| Opportunity | Product | Score | Status |
|---|---|---|---|
| (none yet) | — | — | Run `analysis-research-sprint` after both apps are live |

## Decision Board

Open executive decisions live in `EXECUTIVE-DECISIONS.md`.

| ID | Status | Summary |
|---|---|---|
| EXD-001 | Decided | Layer 8 Executive Intelligence OS — markdown-first, phased spine. Done. |
| EXD-002 | Open | Analytics instrumentation scope. Recommendation: 2-day cap, activation events only. Decide and assign. |
| EXD-003 | Decided | Portfolio status refreshed 2026-05-31 from local task files. |

## Risk Board

| Risk | Area | Severity | Status |
|---|---|---|---|
| App Store approval delay blocks both apps | Release | High | Active |
| Resumely iOS ships with zero analytics (PostHog not wired) | Growth | High | Active — integrate before submit |
| RunSmart iOS activation funnel incomplete (run_started/completed missing) | Growth | Medium | Active — post-submission follow-up |
| No financial / activation visibility | Finance / Growth | High | Needs Data |

## Weekly Review

**Latest: 2026-05-31 (second run).** Status pulled fresh from local task files.

Summary vs. first review (2026-05-30):
- RunSmart iOS advanced from "submit-ready (orchestration map)" to confirmed via GPS QA evidence
  (two physical-device outdoor runs on 2026-05-27 and 2026-05-30). Portal tasks are the only gate.
- Resumely iOS confirmed at pre-submission: 55/55 tests passing, rb-aso-002 screenshots rendered.
  PostHog still absent — unchanged from last week. This is now the highest-priority technical task.
- EXD-003 resolved: stale 2026-05-15 status replaced with 2026-05-31 actuals.
- EXD-002 still open: analytics scope needs explicit operationalization.

Top 3 this week:
1. RunSmart iOS: App Store Connect portal close-out (human). Target: submit by 2026-06-01.
2. Resumely iOS: PostHog integration (2-day cap: `app_launched` + `optimize_completed`). Then submit.
3. Analytics sprint definition (EXD-002): write task cards, cap to 2 days, start.

Busy or productive: productive on product depth (E7, Flex Week, live stabilization). Still absent
on distribution execution (portal close-out, Fastlane credentials, PostHog).

Stop-doing list this week:
- Do not start new features (GPS enhancements, new Expert workflows, etc.) until both apps are submitted.
- Do not expand analytics scope beyond activation + export-success (risk of analytics sprint bloating).

Delegation list:
- Analytics instrumentation — agent (post EXD-002 task cards are written in EXECUTIVE-BACKLOG.md).
- Fastlane / ASC API key setup — founder action (human), no delegation available.
- ASC portal close-out — founder action (human), no delegation available.

New decisions this review: EXD-004 (see EXECUTIVE-DECISIONS.md).

## Monthly CFO Review

Latest Monthly Finance Review: not yet run. Run `PROMPTS/cfo-monthly-review.md`.

## Quarterly OKRs

First draft set 2026-05-31 in `CEO-OS.md` → Quarterly OKRs section.

| OKR | Quarter | Objective | Key Results |
|---|---|---|---|
| OKR-1 | Q2 2026 | Both iOS apps approved and live on App Store | (1) RunSmart iOS approved + live; (2) Resumely iOS submitted; (3) PostHog receiving events from both apps before day 1 |
| OKR-2 | Q3 2026 | First-wave users complete core action (activation) | (1) RunSmart D7 activation ≥ 30% (unknown baseline); (2) Resumely D7 activation ≥ 40% (unknown baseline); (3) ≥ 1 paid subscriber |

Review: weekly check / monthly score / quarterly close. Activation targets are directional
until post-launch data is available.

## Next Recommended Actions

1. Human: open App Store Connect, select build 6, upload screenshots, enter demo credentials,
   submit RunSmart iOS for review.
2. Agent: integrate PostHog SDK in Resumely iOS (task card in EXECUTIVE-BACKLOG.md).
3. Agent: wire `run_started` + `run_completed` in RunSmart iOS (task card in EXECUTIVE-BACKLOG.md).
4. Human: set up Fastlane / ASC API key for Resumely iOS screenshot upload.
5. Founder: review Q2/Q3 OKRs in `CEO-OS.md` and adjust if needed.
