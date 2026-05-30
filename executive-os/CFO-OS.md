# CFO / Monetization OS

## Purpose

The CFO / Monetization OS is responsible for financial visibility, budgeting,
revenue tracking, pricing, monetization experiments, unit economics, cost control,
runway, and financial reporting. It exists so financial decisions are made on
visible numbers, not vibes.

It is run by `agents/cfo-agent.md`. The cardinal rule: **it never invents a number.**
Any figure that is not actually known is written as `unknown — need: <source>`.

## What It Tracks

Each line carries its current data source. No automatic App Store / RevenueCat /
PostHog / payment sync exists yet, so most start as `Needs Data`.

### Revenue
- Revenue by product — `unknown — need: App Store Connect / RevenueCat export`
- Revenue by platform (iOS / web) — `unknown — need: source per platform`
- App Store proceeds (after Apple fee) — `unknown — need: App Store Connect`
- Subscription revenue — `unknown — need: RevenueCat / Stripe`
- One-time payments (if relevant) — `unknown — need: Stripe`
- Refunds — `unknown — need: App Store Connect / Stripe`
- Apple fees — `derived once proceeds are known`

### Costs
- AI / API costs (OpenAI etc.) — `unknown — need: provider billing`
- Hosting — `unknown — need: provider billing`
- Supabase — `unknown — need: Supabase billing`
- Vercel — `unknown — need: Vercel billing`
- PostHog — `unknown — need: PostHog billing`
- Design / tooling — `unknown — need: manual cost list`
- Contractor / freelancer — `unknown — need: manual cost list`
- Marketing spend — `unknown — need: manual; default $0 (no paid ads)`

### Unit economics & funnel
- CAC (only when paid acquisition starts) — `not applicable yet`
- Conversion rate — `unknown — need: PostHog`
- Activation rate — `unknown — need: PostHog`
- Trial-to-paid rate — `unknown — need: RevenueCat / PostHog`
- Churn — `unknown — need: RevenueCat`
- LTV (only with enough data) — `not enough data yet`
- Gross margin — `derived from revenue and direct costs`
- Burn — `derived from costs minus revenue`
- Runway — `derived from cash on hand and burn (cash on hand: unknown — need: owner)`
- Monthly net profit / loss — `derived`

## Workflows

Phase 1 (live):

- Monthly Finance Review — `workflows/monthly-finance-review.md`

Phase 2 (tracked in `EXECUTIVE-BACKLOG.md`):

- Pricing & Packaging Review
- Monetization Experiment

## Metrics & Templates

- Schema and data sources: `EXECUTIVE-METRICS.md` (financial + cost sections).
- Report template: `templates/monthly-finance-report-template.md`.
- Data-source policy reused from `../distribution-os/data/source-of-truth-policy.md`.

## Rules

- Never invent numbers. Separate known figures from `Needs Data`.
- Derived numbers must show their inputs.
- Every monetization recommendation must include risks and a validation plan.
- Big pricing / budget choices are logged in `EXECUTIVE-DECISIONS.md`.
- Free / low-cost-first and product-led distribution before paid acquisition (carried
  over from `../distribution-os/operating-principles.md`).
