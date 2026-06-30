# Distribution Command Center

The single page that answers: what is this week about, what is shipping, what is blocked. Update at the start and end of every distribution cycle. The Notion Command Center database mirrors this — Notion is the dashboard, this file is the source the agent reads.

## This Week

- **Week of**: 2026-06-30
- **Focused product**: RunSmart iOS (post-launch ASO + first-run activation)
- **Other product status**: ResumeBuilder iOS — maintenance / D7 readout follow-up; directory submissions remain founder-action work
- **Theme**: Turn the 2026-06-20 RunSmart distribution-cycle findings into founder-reviewable next actions.
- **Top 3 experiments** (link to rows in `experiment-log.md`):
  1. rs-onboarding-001 (score 21) — first-run commitment + local reminder after plan generation
  2. rs-aso-003 (score 20) — post-launch ASO cleanup: first-review prompt, subtitle/keyword review, screenshot captions, metadata sync
  3. rs-aso-002 (score 18) — screenshot caption overlays for the live listing
- **Assets in flight**:
  - `distribution-os/projects/runsmart/scaffold/drafts/2026-06-20-rs-onboarding-review/onboarding-review.md` — reviewed, needs founder approval before product work
  - `distribution-os/projects/runsmart/scaffold/drafts/2026-06-20-rs-aso-003-listing-audit/aso-review.md` — reviewed, needs founder approval before ASC / app changes
- **Awaiting founder action**:
  - Choose whether `rs-onboarding-001` becomes the next RunSmart iOS work packet.
  - Export App Store Connect baseline for RunSmart product page views, conversion, keyword impressions, and ratings count.
  - Approve or reject ASC metadata edits, screenshot caption work, and first-review prompt timing.
- **Awaiting external response**:
  - App Store Connect metrics export for the live RunSmart listing.
  - PostHog volume increase before D7 retention can be evaluated.
- **Blocked**:
  - D7 retention gate is not statistically useful at current RunSmart volume.
  - No App Store metadata, screenshot, notification, or review-prompt change should publish without explicit founder approval.

## Current Channel Status

### RunSmart

| Channel | Status | Owner Of Next Step | Notes |
|---|---|---|---|
| ASO | reviewed | Founder — approve metadata/screenshot/review-prompt next steps | rs-aso-003 audit found stale repo metadata vs live ASC, zero ratings, and missing screenshot captions |
| Onboarding / activation | reviewed | Founder — approve iOS work packet | rs-onboarding-001 found onboarding completion healthy, but app launch → onboarding start and plan → run are the leaks |
| Landing pages (PLG) | paused | Agent — later focus week | Resume after ASO baseline and first-run activation path are clearer |
| LinkedIn founder updates | draft | Founder — review existing launch post when useful | Not the binding constraint this week |
| Running SEO | not started | Agent — next focus week | |
| Runna comparison | not started | Agent — plan next | |
| Garmin / Strava content | not started | Agent — plan next | |
| Beginner challenges | paused | — | Conditional on challenge feature ship |
| Partnerships | paused | Agent — next focus week | Wait for conversion baseline before outreach |
| Lifecycle email | planned | Product session | Revisit after first-run reminder path is approved |
| Community research | not started | — | Observation only |

### ResumeBuilder

| Channel | Status | Owner Of Next Step | Notes |
|---|---|---|---|
| ASO | awaiting review | Founder — review rb-aso-001 listing copy + rb-aso-002 screenshot brief | Listing copy v1 drafted 2026-05-28; subtitle/keywords/description ready for review |
| Web landing pages with App Store CTA | not started | Agent — next focus week | iOS-first model; every mobile CTA points to App Store |
| Free ATS tool (web → app) | not started | Agent — confirm scope with founder | Web tool result page hands off to App Store install |
| Directories | awaiting review | Founder — review directory pack; press submit after App Store live | rb-dir-001 pack drafted for 5 directories; blocked on App Store URL |
| Lifecycle email | not started | Agent — next focus week | Needs analytics instrumentation first |
| Conversion optimization | not started | Agent — next focus week | Signup → editor → export funnel |
| Hebrew market | planned | Agent — after English listing is approved | Approach confirmed (single listing + locale); in-app RTL not yet built; Hebrew metadata deferred to T+30 after App Store live |
| Programmatic SEO | not started | Agent — after ASO proves | Demoted to Tier B until ASO + landings prove install |
| Career coach partnerships | not started | Agent — next focus week | |
| LinkedIn job-seeker content | not started | Deferred | Tier C |

Status values: `not started` · `planned` · `in progress` · `awaiting review` · `approved` · `published` · `measuring` · `learned` · `paused` · `killed`

## Last Week's Decisions

- 2026-05-27: Screenshot A variants approved for all 5 slots (rs-aso-002 ready to render)
- 2026-05-27: Garmin description sentence approved; full description draft filed (rs-aso-001 ready to apply)
- 2026-05-27: v1.0 ships free; paid tier TBD
- 2026-05-27: Android out of scope for 2026; Hebrew ASO in scope
- 2026-05-27: Email platform = Resend via Supabase Edge Functions (free 3K/mo)
- 2026-05-28: Distribution scaffold installed in both product repos — RunSmart iOS (missing scaffold files added; curated files preserved) and ResumeBuilder Web (full scaffold v1)

## This Week's Done Definition

A week is done when:

1. The weekly cycle workflow has been run end to end
2. The top 3 experiments either have approved assets or are explicitly deferred
3. `weekly-growth-review.md` has the week's report appended
4. `experiment-log.md` and `metrics-dashboard.md` are current
5. The Notion Command Center is synced with this file
