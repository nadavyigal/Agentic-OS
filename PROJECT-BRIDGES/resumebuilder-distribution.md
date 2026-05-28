# Project Bridge: ResumeBuilder Distribution

Bridge from the global Agentic OS into ResumeBuilder AI's distribution work. Companion to `resumebuilder-ai.md` and `resumebuilder-ios.md`. The ResumeBuilder repo's local Agent OS remains the source of truth for product implementation.

## 1. Where The Project Lives

- ResumeBuilder Web: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`
- ResumeBuilder iOS (future): `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`

## 2. What Distribution Files Should Exist In The Project

Inside ResumeBuilder's web repo at `.agent-os/distribution/`:

- `product-positioning.md` (mirrored to `.agents/product-marketing.md`)
- `audience.md`
- `channels.md`
- `messaging.md`
- `competitors.md`
- `seo-program.md`
- `lifecycle-program.md`
- `directories.md`
- `experiment-backlog.md`
- `weekly-plan.md`
- `metrics.md`
- `assets-needed.md`
- `lessons.md`
- `hebrew-program.md` (optional)

Scaffold: `distribution-os/projects/resumebuilder/scaffold/`. Install instructions in that folder's `README.md`.

## 3. What The Distribution OS Can Read From The Project

- All `.agent-os/distribution/*.md` files
- `.agents/product-marketing.md`
- Public web pages and free tool URLs
- Search Console exports
- PostHog exports
- Stripe (monetization) exports

## 4. What The Distribution OS Can Update Inside The Project

Same rule as RunSmart: drafts under `distribution-os/projects/resumebuilder/scaffold/drafts/`; founder copies across.

## 5. What Requires Founder Approval

- Live web page deploys
- Programmatic SEO template rollouts (founder reviews template + 5 sample renders before full set goes live)
- Email triggers in production
- Pricing copy changes
- Free tool launches
- Directory submissions (founder presses submit)
- Hebrew variant publishing
- Partnership outreach to a specific person

## 6. How To Run A Weekly Distribution Cycle For ResumeBuilder

1. Set the command center to "Focused product: ResumeBuilder"
2. Pick the theme from the highest-tier A channel without active work this month
3. Run `distribution-os/workflows/00-weekly-distribution-cycle.md`
4. Draft assets in the right Drive folder + experiment rows
5. Stop at founder review

Common weekly themes for ResumeBuilder:

- SEO opportunity mining + bespoke Tier 1 page
- Programmatic SEO template build (with 30+ entries)
- Free ATS tool MVP brief
- Directory submission batch (5 per week)
- Lifecycle email backbone draft
- Conversion review on the editor / export funnel
- Career coach partnership outreach
- Hebrew landing draft

## 7. Constraints This Bridge Inherits

- All `GLOBAL-AGENT-RULES.md` rules
- All `distribution-os/operating-principles.md`
- The ResumeBuilder-specific constraints in `distribution-os/projects/resumebuilder.md`

## 8. Token Efficiency

For ResumeBuilder distribution work, load:

- `distribution-os/distribution-context.md`
- `distribution-os/operating-principles.md`
- `distribution-os/projects/resumebuilder.md`
- This bridge
- The specific workflow + skill the task needs

Do not load RunSmart bridges or files unless cross-product context matters.
