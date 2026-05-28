# RunSmart — Distribution OS View

The global distribution view of RunSmart. The product repo at `/Users/nadavyigal/Documents/RunSmart` (web + iOS) is the source of truth for product facts. This file is the bridge into distribution.

## Identity

- Name: RunSmart
- Product type: AI running coach
- Surfaces: native iOS app + web presence
- Status: active, primary product focus

## Audience

- Beginner to intermediate runners
- People who own a Garmin, Apple Watch, or use Strava
- Goal-anchored (5K, 10K, half, marathon) or habit-anchored (consistency, recovery)
- Triggered by: signed up for a race, returning from injury, restarting after a break, frustrated by static plans

## Wedge

The wedge is adaptive coaching that responds to the user's actual life, not a one-size plan. The product makes this concrete via:

- Adaptive plan generation
- Post-run debrief
- Readiness check
- Race strategy
- Free benchmark / route content as a warm wedge

## Distribution Surfaces (Tier A First)

See `../channel-backlog.md` for current scores.

| Tier | Channel | This OS Workflow |
|---|---|---|
| A | App Store Optimization | n/a (use `marketingskills/skills/aso/SKILL.md` directly) |
| A | Product-led landing pages | `workflows/09-conversion-review.md` |
| A | Runna comparison page (one-time, long tail) | `workflows/04-seo-opportunity-mining.md` |
| A | Coach / club / podcast partnerships | `workflows/11-partnerships.md` |
| A | Lifecycle email | `workflows/08-lifecycle-email.md` |
| B | LinkedIn founder updates | `workflows/05-linkedin-distribution.md` |
| B | Running SEO content | `workflows/04-seo-opportunity-mining.md` |
| B | Garmin / Strava integration content | `workflows/04-seo-opportunity-mining.md` |
| C | Beginner challenges | conditional on challenge feature shipping |
| C | Community research | observation only |

## What The Distribution OS Owns For RunSmart

- Cross-channel weekly plan
- Asset templates and drafts
- Experiment log and scoring
- Lessons promoted across products
- Bridge to the Notion Command Center

## What The Project Repo Owns For RunSmart

Inside RunSmart's `.agent-os/distribution/` (scaffold under `scaffold/`):

- `product-positioning.md`
- `audience.md`
- `channels.md` (project-specific channel detail)
- `messaging.md`
- `competitors.md`
- `seo-program.md`
- `app-store-program.md`
- `lifecycle-program.md`
- `experiment-backlog.md` (project-level rows)
- `weekly-plan.md`
- `metrics.md`
- `assets-needed.md`
- `lessons.md`

The product repo's own AGENTS.md / CLAUDE.md remain the operating rules for repo work; this OS does not edit product code.

## Constraints Specific To RunSmart

- App Store guidelines apply to ASO assets
- Health and running claims must be defensible
- Garmin and Apple integration messaging must match what the product actually does (no implied background GPS unless implemented)
- No fake review pushes, no community spam
- TestFlight / App Store reviews can have lag; expect 24–48h for re-review on listing changes

## First Distribution Bets To Run

The first 4-week plan (`../README.md` → first 4 weeks) provides specifics. The current concrete bets:

1. ASO audit and listing rewrite (load `marketingskills/skills/aso/SKILL.md`, produce as a single experiment with measurable target on `runsmart.acquisition.app_store_install_rate`)
2. Runna comparison page (load `marketingskills/skills/competitors/SKILL.md` + `competitor-profiling`)
3. Lifecycle email backbone: 3 emails (welcome, plan-generated nudge, week-1 adherence digest)
4. LinkedIn founder cadence: one post per focus week with the "lesson learned" or "behind the scenes" angle

## Founder Review Default

- ASO copy changes: founder must approve before App Store submission
- Web landing changes: founder approves before deploy
- Emails: founder approves before the trigger is enabled in production
- LinkedIn: founder posts manually

## Open Questions

- When does the paid tier (if any) go live? This shifts pricing / paywall / referral workflows from deferred to active.
- Are Garmin and Strava integrations active enough to anchor SEO?
- Is the Hebrew market relevant for RunSmart, or English-only?
