# ResumeBuilder — Distribution OS View

The global distribution view of ResumeBuilder AI. The product repo is the source of truth for product facts. This file is the bridge into distribution.

## Identity

- Name: ResumeBuilder AI
- Product type: AI resume optimization + builder
- Surfaces: **iOS app (primary)** + web (funnel)
- Status: active, secondary product focus

## iOS-First Distribution Model

Web exists and matters, but every web surface should treat App Store install as the primary conversion. Web signup remains a fallback. The funnel:

```
SEO / programmatic page / directory / partnership / free tool
  → web landing (mobile-detect)
    → App Store CTA (iOS) | web signup (desktop)
      → App Store listing
        → install
          → first resume started → exported → returned
```

## Audience

- Active job seekers (mobile during commute, lunch, between interviews)
- Career switchers
- People polishing an existing resume for a specific role
- English primary; Hebrew secondary (authored, not translated)

## Wedge

ATS-aware optimization plus job-tailored output plus templates that actually parse. On iOS this becomes: paste-a-posting, tailor in minutes, export from your phone.

## Distribution Surfaces (Tier A First)

See `../channel-backlog.md` for current scores.

| Tier | Channel | This OS Workflow |
|---|---|---|
| A | **App Store Optimization** | use `marketingskills/skills/aso/SKILL.md` directly |
| A | Web landing pages → App Store CTA | `workflows/09-conversion-review.md` |
| A | Free ATS / resume scoring tool (web → app) | `workflows/07-free-tool-strategy.md` |
| A | Directory submissions (with App Store URL) | `workflows/06-directory-submissions.md` |
| A | Lifecycle email (post-install) | `workflows/08-lifecycle-email.md` |
| A | Conversion optimization (signup, editor, paywall) | `workflows/09-conversion-review.md` |
| A | Hebrew market (App Store + landing) | `workflows/02-positioning-review.md` + ASO Hebrew metadata |
| B | Programmatic SEO with App Store CTA | `workflows/04-seo-opportunity-mining.md` |
| B | Career coach + HR partnerships | `workflows/11-partnerships.md` |
| B | iOS launch campaign (when major versions ship) | `workflows/10-launch-campaign.md` |
| C | Resume examples library | `workflows/04-seo-opportunity-mining.md` |
| C | LinkedIn job-seeker content | optional |

## What The Distribution OS Owns For ResumeBuilder

- Cross-channel weekly plan
- ASO programs and listing audits
- Programmatic SEO scaffolding with App Store CTA logic
- Free-tool strategy and post-result iOS handoff
- Lifecycle email designs (post-install)
- Bridge to Notion Command Center

## What The Project Repo Owns For ResumeBuilder

Inside ResumeBuilder's iOS repo `.agent-os/distribution/` (scaffold under `scaffold/`):

- `product-positioning.md`
- `audience.md`
- `channels.md`
- `messaging.md`
- `competitors.md`
- `app-store-program.md` (primary)
- `seo-program.md` (web funnel)
- `lifecycle-program.md`
- `directories.md`
- `experiment-backlog.md`
- `weekly-plan.md`
- `metrics.md`
- `assets-needed.md`
- `lessons.md`
- `hebrew-program.md`

## Constraints Specific To ResumeBuilder iOS

- App Store guidelines apply to all ASO assets
- ATS claims must reflect actual parser behavior on the iOS app
- Hebrew variants must be authored, not auto-translated (App Store metadata + landing copy + in-app strings)
- Programmatic SEO pages must clear thin-content bar AND make the App Store install path obvious on mobile
- Paid features require clear pricing copy in App Store + in-app paywall, no dark patterns
- Apple Search Ads is a paid channel — out of scope by default per founder constraint
- TestFlight / App Store reviews can have lag; expect 24–48h for re-review on listing changes
- Web is no longer the conversion target by default — pages that only optimize for web signup miss the goal

## First Distribution Bets To Run

1. **ASO audit and listing setup** for the ResumeBuilder iOS App Store listing (English first, Hebrew metadata variant prepared)
2. Web `ats-resume-builder` landing and `ai-resume-tailoring` landing both with App Store CTA prominent on mobile
3. Free ATS / resume scoring tool MVP on web, result page handoff to App Store
4. Directory submission pack v1 with both web URL and App Store URL included
5. Lifecycle email backbone: welcome (post-install), didn't-start-in-24h, activation-hit, 14-day return
6. Conversion review on the iOS app onboarding (first-run → first export) — the most leveraged surface for activation

## Founder Review Default

- App Store metadata changes: founder approves before App Store submission
- Web landing changes: founder approves before deploy
- Emails: founder approves before trigger enabled in production
- Programmatic SEO templates: founder reviews template + 5 sample rendered pages before turning on the full set
- Free tool launch: founder approves the lead-capture moment + App Store handoff design
- Directories: founder approves the pack once; per-directory submissions founder presses submit
- Hebrew App Store metadata: founder reviews authored Hebrew copy

## Open Questions

- ~~Is the iOS app in TestFlight, soft-launch, or App Store live?~~ **Answered 2026-06-29: LIVE on the App Store, v1.2 (7).** Real link: `https://apps.apple.com/app/resume-ai-cv-builder/id6776752349`. Canonical positioning (Fit/Match, Resumely Match Score, no paid acquisition until funnel readable) locked in `.agents/product-marketing.md` in the iOS repo, 2026-06-28. All ASO/outreach work should be live now, not pre-launch.
- What is the current paid tier on iOS (in-app purchase, subscription, credit system)? This shapes paywall + pricing copy.
- Hebrew App Store: same Apple ID account or separate region listing? Same metadata language flag?
- Web → App Store install attribution: are we tagging with `at=` and `ct=` parameters? Required to measure web feeder channels.
- Is there an Android version planned? If yes, ASO workflow expands to Google Play.
- Apple Search Ads: explicitly out of scope until organic ASO proves, confirm?
