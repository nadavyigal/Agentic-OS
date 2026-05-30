# Workflow: Monthly Finance Review

Produces the monthly financial picture from available data only. Run by the CFO Agent.

## Purpose

Give a clear, honest financial snapshot: revenue, costs, margin, net result, runway,
and product-level profitability — with missing data flagged, never invented.

## When To Use

Monthly. Run via `PROMPTS/cfo-monthly-review.md`.

## Inputs

- App Store / RevenueCat / payment data **if available**.
- PostHog activation data **if available**.
- Manual cost list (owner-maintained).
- Marketing spend, AI/API costs.
- `EXECUTIVE-METRICS.md`, `../distribution-os/metrics-dashboard.md`,
  `../distribution-os/data/source-of-truth-policy.md`.

## Steps

1. Collect all available financial data.
2. Separate **known numbers** from **missing numbers** (`unknown — need: <source>`).
3. Compute derived figures (gross margin, net, runway) only from known inputs; show
   the inputs.
4. Update the financial snapshot in `EXECUTIVE-DASHBOARD.md` and
   `EXECUTIVE-METRICS.md`.
5. Identify budget risks.
6. Recommend financial actions.

## Output Format

```
## Monthly Finance Review — YYYY-MM
- Revenue (by product / platform) [known | Needs Data]
- Costs (by line) [known | Needs Data]
- Gross margin [derived, inputs shown]
- Net profit / loss [derived]
- Runway [derived, inputs shown]
- Product-level profitability
- What changed since last month
- Budget risks
- Recommended decisions
```

## Evidence Requirements

- Source per figure or `Needs Data`.
- Derived numbers show inputs.
- No claimed automated sync.

## Completion Checklist

- [ ] Known vs missing numbers clearly separated.
- [ ] Derived figures show inputs.
- [ ] Risks + recommended actions included.
- [ ] Dashboard + metrics updated; budget decisions logged.

## Updates

- Dashboard: `EXECUTIVE-DASHBOARD.md` (Financial Snapshot, Monthly CFO Review).
- Metrics: `EXECUTIVE-METRICS.md`.
- Decisions: `EXECUTIVE-DECISIONS.md` for any budget/pricing choice.
