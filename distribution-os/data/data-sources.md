# Data Sources

Authoritative list of where each kind of data comes from. Used to decide which tool to read first and what to do when sources disagree.

## Quantitative

| Data | Source | Access | Notes |
|---|---|---|---|
| RunSmart app events, activation, retention | PostHog | App + web | Define events centrally in project repo |
| ResumeBuilder app events, signup, export | PostHog | Web | Same |
| RunSmart App Store impressions, install, conversion, keyword rank | App Store Connect | Apple ID login | Export weekly to Drive `05 Metrics Exports/App Store Connect/` |
| ResumeBuilder organic search impressions, clicks, position | Google Search Console | Property verified | Export weekly to Drive `05 Metrics Exports/Search Console/` |
| ResumeBuilder web traffic, deploy info | Vercel + PostHog | Vercel project | |
| Stripe revenue, churn, MRR | Stripe Dashboard | Per product account | Export monthly to Drive `05 Metrics Exports/Stripe or Payments/` |
| Supabase user growth, edge data | Supabase Dashboard | Per project | Query via SQL if needed; cache exports |
| Garmin, Strava integration usage (RunSmart) | Internal logs | App backend | Privacy-aware aggregates only |

## Qualitative

| Data | Source | Access | Notes |
|---|---|---|---|
| App reviews (RunSmart) | App Store + Google Play | Public | Export monthly to Drive `02 Market Research/RunSmart/reviews/` |
| Support tickets | TBD per product | Internal | Anonymize before quoting |
| User interviews | Drive `02 Market Research/{product}/interviews/` | Drive | |
| Public running forums (Reddit, Strava forums) | Public | Observe only | Reference, never copy verbatim into product |
| Job-seeker forums | Public | Observe only | Same |
| Founder DMs / partner conversations | Drive `02 Market Research/{product}/partnerships/` | Manual | Capture consent before logging |

## Planning

| Data | Source |
|---|---|
| Current focus, this week status | Notion Distribution Command Center |
| Experiment backlog, scoring, status | Notion Experiment Backlog + `experiment-log.md` |
| Campaigns | Notion Campaign Calendar |
| Asset pipeline | Notion Content / Asset Pipeline |
| Lessons | `distribution-os/lessons.md` + Notion Lessons Learned + `~/.claude/LEARNINGS.md` |

## Documents

| Data | Source |
|---|---|
| Product docs | Google Drive `01 Product Docs/{product}/` |
| Market research | Google Drive `02 Market Research/{product}/` |
| Campaign briefs | Google Drive `03 Campaigns/{product}/` |
| Asset drafts | Google Drive `04 Content Assets/{type}/{product}/` |
| Weekly reports | Google Drive `06 Weekly Reports/` |
| Source materials (founder notes, interview transcripts, external articles) | Google Drive `00 Source Material/` |

## When Sources Disagree

See `source-of-truth-policy.md`.

## Refresh Cadence

| Source | Cadence |
|---|---|
| PostHog | Weekly (in cycle) |
| App Store Connect | Weekly |
| Search Console | Weekly |
| Vercel | Ad hoc |
| Stripe | Monthly |
| App reviews | Monthly |
| Drive exports | Manual / on demand |
| Notion sync | Each weekly cycle |

## Privacy Rules

- No raw user PII in any file in this OS
- No personal training data, run GPS traces, or résumé content stored in this OS
- Quoting an interview requires interviewee consent; anonymize otherwise
- No exporting Stripe customer IDs into Drive without minimization
