# Metrics Dashboard

Pointers to where each metric lives. This file is the index, not the data store. Numbers go in Notion's Metrics Log database and in Google Drive metrics exports.

Schema: see `data/metrics-schema.md`.

## North Star Metrics Per Product

### RunSmart

| Metric | Source | Cadence | Notes |
|---|---|---|---|
| Weekly active runners | PostHog / app analytics | Weekly | Define: opened app + interacted in last 7 days |
| New user activation | PostHog | Weekly | Completed onboarding + first plan generated |
| Plan adherence (week 1) | App data | Monthly | Sessions completed vs prescribed in first week |
| App Store conversion rate | App Store Connect | Weekly | Product page → install |
| App Store impressions by keyword | App Store Connect | Weekly | Top 20 tracked keywords |
| LinkedIn impressions / clicks | LinkedIn analytics | Weekly | Founder profile + posts |
| Web landing page conversion | Vercel / PostHog | Weekly | Landing → app store click |
| MRR / paid users | Stripe or App Store | Monthly | Only when monetization is live |

### ResumeBuilder

| Metric | Source | Cadence | Notes |
|---|---|---|---|
| Signups | Supabase / PostHog | Weekly | Distinct accounts created |
| Activation (first resume created) | PostHog | Weekly | Account → completed resume export |
| SEO organic traffic | Search Console | Weekly | Total + per-page top pages |
| SEO indexed pages | Search Console | Weekly | Programmatic SEO health check |
| Free tool usage | PostHog | Weekly | If free tool is live |
| Email signup → activation | Supabase / PostHog | Weekly | Sequence step completion |
| Editor → export rate | PostHog | Weekly | Funnel: signup → edit → export |
| Paid conversion rate | Stripe + PostHog | Monthly | Visitor → paid |
| MRR / ARR | Stripe | Monthly | |

## Funnel Maps

### RunSmart Acquisition Funnel

```
App Store impression / web landing
  → product page view
  → install
  → first open
  → onboarding complete
  → first plan generated
  → first run logged
  → second run logged (retention signal)
  → week-1 plan adherence
  → continued use (week 4)
  → paid conversion (when live)
```

### ResumeBuilder Acquisition Funnel

```
SEO impression / directory referral / free tool use
  → landing visit
  → signup
  → first resume started
  → first resume exported
  → returned within 14 days
  → paid conversion
  → second resume / referral
```

## Where Numbers Get Logged

- Per-week snapshot: append a row in Notion Metrics Log
- Weekly report: include the diff vs prior week in `weekly-growth-review.md`
- Raw exports: dropped into `Google Drive > 05 Metrics Exports > {tool}`
- Anomalies: flagged in the next weekly cycle's investigation step

## Anti-Pattern Watch

- Reporting cumulative numbers when comparative numbers are more useful
- Reporting vanity metrics (impressions) without conversion follow-through
- Reporting before data is at least 7 days old for weekly cohorts
- Letting one strong week become the new baseline without confirming repeatability
