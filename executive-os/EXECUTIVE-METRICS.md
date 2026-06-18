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
| Activation rate | unknown | TBD | PostHog | Needs Data |
| Retention (D7 / D30) | unknown | TBD | PostHog | Needs Data |
| Core action completion | unknown | TBD | PostHog | Needs Data |

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
