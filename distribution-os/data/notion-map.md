# Notion Map

Notion is the planning and status layer for the Distribution OS. Git is the operating system, Drive is the document store, project repos hold product facts, Notion holds the plan and the live state.

## Workspace Layout

```
Notion/
├── Distribution OS/                            (parent page, created by OS)
│   ├── Distribution Command Center (database)
│   ├── Experiment Backlog (database)
│   ├── Campaign Calendar (database)
│   ├── Content / Asset Pipeline (database)
│   ├── Metrics Log (database)
│   └── Lessons Learned (database)
└── 🗓️ Social Media Calendar                    (existing, separate)
    — pre-existing database the founder uses for the LinkedIn cadence.
      The Content / Asset Pipeline database is the OS source of truth;
      the Social Media Calendar can be linked to a LinkedIn-only view if useful.
```

## 1. Distribution Command Center

The dashboard the founder opens first.

Properties:

| Property | Type | Notes |
|---|---|---|
| Week of | Date | Monday of the week |
| Product | Select | RunSmart, ResumeBuilder |
| Current focus | Text | Theme of the week |
| Active channels | Multi-select | Channels named in `channel-backlog.md` |
| This week's goals | Text | Short |
| Status | Select | planning, in progress, review, done |
| Owner | Person | Always founder |
| Last updated | Last edited time | Auto |
| Weekly plan link | URL | Link to Drive weekly report or `weekly-growth-review.md` entry |

One row per product per week. The active row is filtered by `Status != done` and `Week of >= today - 7 days`.

## 2. Experiment Backlog

Properties:

| Property | Type | Notes |
|---|---|---|
| ID | Text | Matches `experiment-log.md` IDs |
| Product | Select | RunSmart, ResumeBuilder |
| Experiment name | Title | |
| Channel | Select | |
| Hypothesis | Text | |
| Impact | Number 1–5 | |
| Confidence | Number 1–5 | |
| Effort | Number 1–5 | Subtracted |
| Speed | Number 1–5 | |
| Founder fit | Number 1–5 | |
| Strategic fit | Number 1–5 | |
| Score | Formula | I + C + S + FF + SF − E |
| Status | Select | proposed, approved, queued, running, paused, done-worked, done-failed, rejected |
| Start date | Date | |
| End date | Date | |
| Result | Text | Filled when complete |
| Learning | Text | Filled when complete |
| Next action | Text | |

Views:

- Active (`Status = running`)
- Queue (`Status = approved`)
- Scoreboard (`Status in done-*`)

## 3. Campaign Calendar

Properties:

| Property | Type | Notes |
|---|---|---|
| Product | Select | |
| Campaign | Title | |
| Channel | Multi-select | |
| Asset type | Multi-select | |
| Status | Select | drafting, awaiting review, approved, scheduled, live, complete |
| Target publish date | Date | |
| Approval status | Select | not yet, founder reviewed, approved, rejected |
| Draft link | URL | Drive folder |
| Published link | URL | After publish |

Views:

- Calendar (by target publish date)
- Per product
- Awaiting review (`Approval status = founder reviewed`)

## 4. Content / Asset Pipeline

Per-asset granular tracking (sometimes a campaign has many assets).

Properties:

| Property | Type | Notes |
|---|---|---|
| Product | Select | |
| Asset title | Title | |
| Channel | Select | |
| Funnel stage | Select | acquisition, activation, retention, monetization |
| Status | Select | draft, in review, approved, scheduled, published, archived |
| Draft link | URL | |
| Review notes | Text | |
| Approved? | Checkbox | |
| Published URL | URL | |
| Performance notes | Text | After publish |

## 5. Metrics Log

Time series.

Properties:

| Property | Type | Notes |
|---|---|---|
| Product | Select | |
| Date | Date | |
| Source | Select | PostHog, App Store Connect, Search Console, Vercel, Stripe, Manual |
| Metric | Select | Use canonical names in `metrics-dashboard.md` |
| Value | Number | |
| Segment | Text | Optional (e.g., role, country) |
| Notes | Text | |

Views:

- Per metric over time
- Latest snapshot (rollup)
- Anomalies (`abs(diff from 4-wk avg) > X%`)

## 6. Lessons Learned

Properties:

| Property | Type | Notes |
|---|---|---|
| Product | Select | RunSmart, ResumeBuilder, Both |
| Channel | Select | |
| Lesson | Title | A rule, not an observation |
| Evidence | Text | Reference experiment IDs or metrics |
| Confidence | Number 1–5 | |
| Reuse recommendation | Text | When future-you should apply this |
| Date | Date | |
| Promoted to global? | Checkbox | If yes, mirrored in `~/.claude/LEARNINGS.md` |

## How Agents Use Notion

If a Notion connector is present:

- Read Command Center first when starting a weekly cycle
- Read Experiment Backlog to know what is already running
- Read Lessons Learned for the focused product before drafting
- Write rows after producing a draft (so the founder can scan in Notion without opening Drive)
- Never publish to Notion's public-share links without explicit founder go-ahead

If no Notion connector:

- Update the equivalent markdown files (`experiment-log.md`, `distribution-command-center.md`, `lessons.md`) and note that Notion sync is pending

## Conflict Resolution

If Notion disagrees with markdown:

- Status: Notion wins (live state)
- Hypothesis content: markdown wins (versioned source)
- Lessons: whichever was written later, with a note in the older copy
