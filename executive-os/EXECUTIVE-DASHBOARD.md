# Executive Dashboard

Manual source-of-truth dashboard for the Executive Intelligence OS. Updated by the
Weekly CEO Review and Monthly Finance Review workflows. No invented data: financial
cells stay `Needs Data` until a real source exists.

Last updated: 2026-05-30 (first Weekly CEO Review)

Status indicators: `Active` · `Watch` · `Blocked` · `Needs Decision` · `Needs Data`
· `Ready`

## Executive Summary

Two-app App Store submission sprint. RunSmart iOS is submit-ready (build 6). Resumely
iOS is pre-submission with copy and analytics pending. App Store approval and
analytics visibility are the current bottlenecks. Financial picture is not yet
instrumented — all revenue/cost figures are `Needs Data`.

## CEO Focus

- Primary: get RunSmart iOS through App Store approval.
- Secondary: finish Resumely iOS copy + analytics, then submit.
- Hold: no new feature scope until the sprint clears.

## Top 3 Priorities

1. RunSmart iOS — App Store approval. `Active`
2. Resumely iOS — finish copy + analytics, then submit. `Active`
3. Stand up minimal financial + activation visibility (define sources). `Needs Data`

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
| RunSmart iOS | Active | Submit-ready, build 6; awaiting approval |
| RunSmart Web | Watch | Source of product logic; steady |
| Resumely iOS | Active | Pre-submission; copy + analytics pending |
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
| (none yet) | — | — | Run `analysis-research-sprint` to populate |

## Decision Board

Open executive decisions live in `EXECUTIVE-DECISIONS.md`. Current open count: 0
(seed). Surface new ones from the Weekly CEO Review.

## Risk Board

| Risk | Area | Severity | Status |
|---|---|---|---|
| App Store approval delay blocks both apps | Release | High | Active |
| No financial/activation visibility | Finance / Growth | High | Needs Data |
| Resumely analytics not wired before submit | Growth | Medium | Active |

## Weekly Review

**Latest: 2026-05-30.** Both apps are in the submission sprint and product work is well
ahead of distribution and analytics. Freshest cross-portfolio source is the 2026-05-29
orchestration map: RunSmart iOS submit-ready (build 6), Resumely iOS pre-submission
(rb-aso-001 copy awaiting approval, PostHog not yet integrated). No revenue or
activation data exists for any product. Note: `DASHBOARD.md` / `PROJECT-STATUS.md`
(2026-05-15) are stale relative to this and should be refreshed.

- **Top 3 this week:** (1) RunSmart iOS - finish App Store Connect portal and Submit
  for Review; (2) Resumely iOS - approve rb-aso-001 copy and integrate PostHog, then
  archive build 1; (3) confirm activation/export analytics actually fire before any
  new feature work.
- **Busy or productive:** productive on product, absent on distribution/analytics.
- New decisions logged this review: EXD-002, EXD-003 in `EXECUTIVE-DECISIONS.md`.

## Monthly CFO Review

Latest Monthly Finance Review: not yet run. Run `PROMPTS/cfo-monthly-review.md`.

## Quarterly OKRs

No OKRs set yet. Draft with `templates/okr-template.md` in the next Weekly CEO Review.

## Next Recommended Actions

1. Run the first Weekly CEO Review to set top-3 priorities and seed OKRs.
2. Define the real data sources for revenue, cost, and activation (no values yet —
   just the source per line).
3. Keep both apps in the submission sprint; no new feature scope.
