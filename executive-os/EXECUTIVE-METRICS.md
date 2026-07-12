# Executive Metrics

The strategic and financial scorecard. This file defines **which** metrics matter and
**where each one comes from**. It does not invent values. Every metric carries a
status: `Tracked` (real source live), `Needs Data` (source not yet wired), or
`N/A yet` (not relevant at this stage).

Data-source policy is reused from `../distribution-os/data/source-of-truth-policy.md`
— do not restate it here.

## North-Star Metrics

| Metric | Current | Target | Source | Status |
|---|---|---|---|---|
| Weekly active users (per product) | unknown | TBD | PostHog | Needs Data |
| Paying users (per product) | unknown | TBD | RevenueCat / App Store | Needs Data |

## Product Metrics

| Metric | Current | Target | Source | Status |
|---|---|---|---|---|
| RunSmart iOS D7 activation (physical App Store install → `run_completed`) | 0% (0/13 mature clean cohort) | ≥30% | PostHog 171597, readout #3 2026-07-12 | Tracked |
| Resumely D7 activation (first seen → `export_success`) | 0% (0/73 mature founder/test-excluded cohort) | ≥20% by 2026-08-01 | PostHog 270848, readout #3 2026-07-12 | Tracked; EXD-015 primary outcome |
| RunSmart leading funnel (D7) | 13 installs → 1 onboarding → 1 plan → 0 run starts/completions | — | PostHog 171597, readout #3 2026-07-12 | Tracked; WP-20 shipped, measuring |
| Resumely leading funnel (D7) | 73 first seen → 9 uploaded → 0 optimized → 0 exported | — | PostHog 270848, readout #3 2026-07-12 | Tracked; first seen→upload→optimization is current observed wall |
| Resumely cumulative clean export | under review — manual dashboard says 1; saved 2026-07-06 clean report says 0 | — | needs reproducible PostHog query with the current exclusion contract | Contradictory; do not cite as confirmed |
| Retention (D7 / D30) | unknown | TBD | PostHog | Needs Data |

> Readout #3 caveats (2026-07-12): RunSmart excludes emulator, TestFlight, sideloaded, and known founder identities. Resumely excludes internal testers plus the four established founder/QA/bot prefixes; its web-inclusive denominator may still contain unattributed automation because the virtual-bot property was unavailable. The result keeps gates closed but does not justify a new product story. Re-read the 1.4.1 picker cohort on 2026-07-18 minimum / 2026-07-25 preferred. Full method: `executive-os/reviews/2026-07-12-activation-reread.md`.

## Financial Metrics

| Metric | Current | Target | Source | Status |
|---|---|---|---|---|
| Revenue by product | unknown | TBD | App Store Connect / RevenueCat | Needs Data |
| Subscription revenue | unknown | TBD | RevenueCat / Stripe | Needs Data |
| Gross margin | derived | TBD | revenue − direct cost | Needs Data |
| Net profit / loss | derived | break-even | revenue − total cost | Needs Data |
| Runway | derived | extend | cash on hand ÷ burn | Needs Data |

## Growth Metrics

| Metric | Current | Target | Source | Status |
|---|---|---|---|---|
| Trial-to-paid rate | unknown | TBD | RevenueCat / PostHog | Needs Data |
| Churn | unknown | TBD | RevenueCat | Needs Data |
| CAC | N/A | N/A | paid channels | N/A yet |
| LTV | N/A | N/A | needs cohort data | N/A yet |

## Cost Metrics

| Metric | Current | Target | Source | Status |
|---|---|---|---|---|
| AI / API cost | unknown | minimize | provider billing | Needs Data |
| Hosting / Supabase / Vercel | unknown | minimize | provider billing | Needs Data |
| PostHog | unknown | free tier | PostHog billing | Needs Data |
| Tooling / contractor | unknown | minimize | manual cost list | Needs Data |
| Marketing spend | $0 (default, no paid ads) | $0 | manual | Tracked |

## Risk Metrics

| Metric | Current | Source | Status |
|---|---|---|---|
| Open high-severity risks | see `EXECUTIVE-DASHBOARD.md` Risk Board | manual | Tracked |
| Apps blocked on approval | Resumely v1.1 (5) in review; RunSmart live | App Store Connect / Resumely iOS tasks/progress.md | Tracked |

## Monthly CFO Review Log

- 2026-07-09: First run of `executive-os/workflows/monthly-finance-review.md`. All revenue, cost (except $0 marketing spend), margin, and runway figures remain `Needs Data` — no App Store Connect / RevenueCat / provider billing / manual cost list was available. Full report: `executive-os/reviews/2026-07-09-monthly-finance-review.md`.

## Current Manual Data Sources

- Project status: `../DASHBOARD.md`, `../PROJECT-STATUS.md`, local repo `tasks/`.
- Distribution: `../distribution-os/metrics-dashboard.md`.
- Costs: manual cost list (owner-maintained), provider billing pages.

## Future Automated Data Sources

Not yet implemented. Do not claim any of these are live until built:

- App Store Connect / RevenueCat → revenue, proceeds, subscriptions, churn.
- PostHog → activation, retention, funnels.
- Provider billing APIs → cost lines.
