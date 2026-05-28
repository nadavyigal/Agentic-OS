# Channel Backlog

A scored list of channels per product. Used by `workflows/03-channel-prioritization.md` and the weekly cycle. Channel scores are reviewed monthly (see `workflows/12-monthly-strategy-review.md`).

Scoring uses the same 1–5 dimensions as experiments but at the channel level:

```
ChannelScore = Reach + Conviction + LeverageOverTime + FounderFit + StrategicFit - OngoingEffort
```

| Dimension | What it asks |
|---|---|
| Reach | Realistic ceiling of qualified attention this channel can produce |
| Conviction | Evidence (own or industry) that this channel converts for our segment |
| LeverageOverTime | Does effort spent today compound (SEO, free tools) or evaporate (a single post) |
| FounderFit | Will the founder actually maintain this without resentment |
| StrategicFit | Does this strengthen the moat or just chase volume |
| OngoingEffort | Weekly time required to keep the channel alive once set up |

## RunSmart Channels (iOS-first)

| Channel | Reach | Conv | Lev | FF | SF | OE | Score | Tier | Notes |
|---|---|---|---|---|---|---|---|---|---|
| ASO | 5 | 4 | 5 | 4 | 5 | 2 | 21 | A | iOS app primary acquisition surface |
| Product-led landing pages | 4 | 4 | 5 | 4 | 5 | 2 | 20 | A | High compounding |
| LinkedIn founder updates | 3 | 3 | 4 | 4 | 4 | 2 | 16 | B | One repeatable cadence only |
| Running SEO content | 4 | 3 | 5 | 3 | 4 | 4 | 15 | B | Heavier content load |
| Runna comparison page | 3 | 4 | 4 | 4 | 4 | 1 | 18 | A | One-time write, long-tail traffic |
| Garmin / Strava content | 3 | 3 | 4 | 3 | 4 | 3 | 14 | B | Tie to integration work |
| Beginner challenges | 3 | 3 | 3 | 3 | 3 | 3 | 12 | C | Only if challenge feature ships |
| Coach / club partnerships | 3 | 4 | 5 | 3 | 5 | 3 | 17 | A | Relationship-driven, slow |
| Lifecycle email | 3 | 4 | 5 | 4 | 5 | 2 | 19 | A | Compounds with every signup |
| Community research | 2 | 3 | 3 | 4 | 3 | 2 | 13 | C | Observation only, never spam |

## ResumeBuilder Channels (iOS-first)

| Channel | Reach | Conv | Lev | FF | SF | OE | Score | Tier | Notes |
|---|---|---|---|---|---|---|---|---|---|
| ASO | 5 | 4 | 5 | 4 | 5 | 2 | 21 | A | iOS App Store is the primary conversion target |
| Web landing → App Store CTA | 4 | 4 | 5 | 4 | 5 | 2 | 20 | A | Bespoke pages built to send mobile traffic to App Store |
| Free ATS / resume tool (web → app) | 4 | 4 | 5 | 4 | 5 | 2 | 20 | A | Engineering-as-marketing; result page CTAs to App Store |
| Directory submissions (with App Store URL) | 3 | 3 | 4 | 5 | 3 | 1 | 17 | A | AI tool + career directories; include both URLs |
| Lifecycle email (post-install) | 4 | 4 | 5 | 4 | 5 | 2 | 20 | A | Activation + retention after install |
| Conversion optimization (app + web) | 4 | 4 | 5 | 4 | 5 | 2 | 20 | A | App onboarding is highest leverage |
| Hebrew market (ASO + landing) | 3 | 4 | 4 | 4 | 5 | 3 | 17 | A | Authored Hebrew, both App Store metadata and web |
| Programmatic SEO (App Store CTA) | 5 | 3 | 5 | 4 | 4 | 3 | 18 | B | Now a feeder; demote from A until ASO + landings prove conversion to install |
| Career coach partnerships | 3 | 4 | 4 | 3 | 5 | 3 | 16 | B | Slow burn, high conviction |
| iOS launch campaign | 3 | 4 | 3 | 4 | 4 | 2 | 16 | B | Activates on major version ships |
| Resume examples library | 4 | 4 | 5 | 3 | 4 | 4 | 16 | C | Pair with programmatic SEO; secondary |
| LinkedIn job-seeker content | 3 | 3 | 3 | 3 | 3 | 3 | 12 | C | Optional, low priority |

## Tier Definitions

- **A**: invest now. At least one A channel must have an active experiment any week the product is in focus.
- **B**: invest when the relevant trigger fires (feature ships, partnership lands, founder has bandwidth).
- **C**: keep on the list, do not invest unless rescored. Re-evaluate monthly.

## Kill / Pause Rules

Pause a channel if:

- It has had >= 3 failed experiments in a row
- OngoingEffort is consistently underestimated and founder is resentful
- A higher-scored channel needs the time
- Industry signal has shifted (algorithm change, platform shutdown, audience drift)

Killed channels go to the bottom of this file with a one-line reason and date.

## Channel History

Pinned record of channel decisions over time (newest first):

- YYYY-MM-DD: initial scoring set
