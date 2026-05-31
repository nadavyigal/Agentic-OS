# Distribution Command Center

The single page that answers: what is this week about, what is shipping, what is blocked. Update at the start and end of every distribution cycle. The Notion Command Center database mirrors this — Notion is the dashboard, this file is the source the agent reads.

## This Week

- **Week of**: 2026-05-28
- **Focused product**: ResumeBuilder iOS (first distribution cycle — ASO v1)
- **Other product status**: RunSmart — rs-aso-001, rs-aso-002, rs-analytics-001 awaiting founder action; App Store submission target 2026-06-01
- **Theme**: ASO listing v1 (English) — write and file Resumely App Store listing copy before submission
- **Top 3 experiments** (link to rows in `experiment-log.md`):
  1. rb-aso-001 (score 21) — App Store listing copy v1 (subtitle, keywords, description)
  2. rb-aso-002 (score 20) — Screenshot brief (5-slot sequence + copy overlays)
  3. rb-dir-001 (score 15) — Directory submission pack v1 (5 directories; pending App Store URL)
- **Assets in flight**:
  - `distribution-os/projects/resumebuilder/scaffold/drafts/2026-05-28-rb-aso-001/listing-copy-v1.md` — **APPROVED, ready to file in App Store Connect**
  - `distribution-os/projects/resumebuilder/scaffold/drafts/2026-05-28-rb-aso-002/screenshot-brief-v1.md` — **APPROVED; screenshots rendered + exported; PR #34 ready to merge; upload to ASC is next**
  - `distribution-os/projects/resumebuilder/scaffold/drafts/2026-05-28-rb-dir-001/directory-pack-v1.md` — draft, awaiting App Store URL + founder review
- **Awaiting founder action**:
  - rb-aso-001 + rb-aso-002: **merge PR #34 → upload screenshots to App Store Connect → file listing copy → submit for review**
  - rb-dir-001: confirm App Store URL when live; founder presses submit on each directory
- **Awaiting external response**:
  - Resumely App Store submission — listing copy approved + screenshots ready; pending founder upload + submit action
  - RunSmart App Store review — target submit 2026-06-01
- **Blocked**:
  - rb-dir-001 submissions blocked on App Store URL (pre-submission)
  - All Resumely acquisition metrics blocked until App Store listing is live
  - ATS tool result page iOS CTA — confirmed missing; web repo fix needed before web feeder channel contributes installs

## Current Channel Status

### RunSmart

| Channel | Status | Owner Of Next Step | Notes |
|---|---|---|---|
| ASO | in progress | Founder — copy description.txt, render overlays, submit | Build uploaded 2026-05-19; rs-aso-001 + rs-aso-002 assets ready |
| Landing pages (PLG) | not started | Agent — next focus week | Blocked on App Store submission first |
| LinkedIn founder updates | not started | Founder — write + post | Deferred to launch week |
| Running SEO | not started | Agent — next focus week | |
| Runna comparison | not started | Agent — plan next | |
| Garmin / Strava content | not started | Agent — plan next | |
| Beginner challenges | paused | — | Conditional on challenge feature ship |
| Partnerships | not started | Agent — next focus week | |
| Lifecycle email | planned | Product session | 3 email drafts ready; Resend + Supabase spec ready |
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
