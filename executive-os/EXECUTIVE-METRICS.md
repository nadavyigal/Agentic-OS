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
| RunSmart iOS D7 activation (install → run_completed) | 0% (0/10 real users) | ≥30% | PostHog 171597, readout 2026-06-24 | Tracked (beta cohort) |
| Resumely D7 activation (first-seen → optimization_completed) | 0% confirmed real organic (3/35 prior raw all excluded; `067544b5` automation/bot-like) | ≥40% | PostHog 270848, WP-16 live read 2026-06-24 | Tracked |
| RunSmart onboarding→plan funnel (D7) | onboarding 50%, plan_generated 30% (n=10) | — | PostHog 171597, 2026-06-24 | Tracked (beta cohort) |
| Retention (D7 / D30) | unknown | TBD | PostHog | Needs Data |

> Readout caveats (2026-06-24): RunSmart cohort (installs ≤2026-06-17) predates the first live App Store build (1.0.3, live 2026-06-19) — it is a TestFlight/dogfood signal, not a market rate. Both readouts exclude the founder's own account and QA/bot bursts per the founder-exclusion rule; raw RunSmart cohort 42 → 10 real users. Resumely WP-16 resolved person `067544b5` as automation/bot-like backend traffic, so no raw Resumely completer is confirmed organic. First true organic RunSmart D7 lands ~2026-06-26. Full readouts: vault `02-Products/*/Metrics/2026-06-24-*-d7-activation-readout.md`; Resumely WP-16 product report: `ResumeBuilder IOS APP/docs/qa/reports/wp-16-activation-attribution-funnel-2026-06-24.md`.

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

## Current Manual Data Sources

- Project status: `../DASHBOARD.md`, `../PROJECT-STATUS.md`, local repo `tasks/`.
- Distribution: `../distribution-os/metrics-dashboard.md`.
- Costs: manual cost list (owner-maintained), provider billing pages.

## Future Automated Data Sources

Not yet implemented. Do not claim any of these are live until built:

- App Store Connect / RevenueCat → revenue, proceeds, subscriptions, churn.
- PostHog → activation, retention, funnels.
- Provider billing APIs → cost lines.
