# Monthly Finance Review — 2026-07

Known numbers only. Anything not actually known is `unknown — need: <source>`.
Derived numbers show their inputs.

## Revenue

| Line | Amount | Source / Status |
|---|---|---|
| Revenue — RunSmart | unknown — need: App Store Connect / RevenueCat | Needs Data |
| Revenue — Resumely | unknown — need: App Store Connect / RevenueCat | Needs Data |
| Subscription revenue | unknown — need: RevenueCat / Stripe | Needs Data |
| One-time payments | unknown — need: Stripe | Needs Data |
| Refunds | unknown — need: store / Stripe | Needs Data |
| Apple fees | derived from proceeds | Needs Data |
| **Total revenue** | derived | Needs Data |

## Costs

| Line | Amount | Source / Status |
|---|---|---|
| AI / API | unknown — need: provider billing | Needs Data |
| Hosting | unknown — need: provider billing | Needs Data |
| Supabase | unknown — need: Supabase billing | Needs Data |
| Vercel | unknown — need: Vercel billing | Needs Data |
| PostHog | unknown — need: PostHog billing | Needs Data |
| Design / tooling | unknown — need: manual list | Needs Data |
| Contractor / freelancer | unknown — need: manual list | Needs Data |
| Marketing spend | $0 (default, no paid ads per `EXECUTIVE-METRICS.md`) | Tracked |
| **Total cost** | derived | Needs Data — only marketing spend line is known ($0) |

## Result

- **Gross margin:** unknown — need: revenue and direct-cost figures above
- **Net profit / loss:** unknown — need: revenue and total-cost figures above
- **Burn:** unknown — need: total cost and cash on hand
- **Runway:** unknown — need: cash on hand ÷ burn; cash on hand: unknown — need: owner

## Product-Level Profitability

| Product | Revenue | Direct cost | Result | Status |
|---|---|---|---|---|
| RunSmart | unknown | unknown | unknown | Needs Data |
| Resumely | unknown | unknown | unknown | Needs Data |

## What Changed Since Last Month

- No prior Monthly Finance Review exists in `executive-os/reviews/` to diff against — this is the first run of this workflow.
- No change in instrumentation status: revenue, cost, and cash figures remain fully unwired across both products, same as the `EXECUTIVE-DASHBOARD.md` Financial Snapshot recorded on 2026-07-09 ("Needs Data - no revenue/cost instrumentation wired").

## Budget Risks

- **No visibility into burn or runway.** Neither product has RevenueCat/App Store Connect revenue sync, provider billing pulls, or a maintained manual cost list. The founder could be running at an unknown burn rate with no early-warning signal before a cash problem becomes urgent.
- **AI/API cost is unmeasured** for both RunSmart (OpenAI, Garmin) and Resumely (OpenAI), the most likely variable-cost driver as usage grows — there is currently no way to catch a cost spike before the provider invoice arrives.
- **Monetization is not live** for either product (per `EXECUTIVE-METRICS.md` Financial Metrics, all rows `Needs Data`; ResumeBuilder AI Web Gate A is explicitly closed per `EXECUTIVE-DASHBOARD.md` Risk Board) — there is no revenue line to offset whatever costs exist.

## Recommended Decisions

- **Build the manual cost list first.** Before any provider-API automation, the founder should compile a one-time snapshot of current recurring costs (OpenAI, Supabase, Vercel, PostHog, Apple Developer, any contractor/tooling spend) so this review has at least one real number next month. This is the single highest-leverage unblock — every other financial metric depends on it or on RevenueCat/App Store Connect access.
- **Do not commit to a monetization or pricing decision** until activation is validated — this is already the standing position per EXD-013/EXD-015 and the 2026-07-12 activation re-read gate; this review finds no new financial information that would change that.
- No budget/pricing decision was made in this review — nothing to log in `EXECUTIVE-DECISIONS.md`.
