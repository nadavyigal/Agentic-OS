# Project Bridge: RunSmart Distribution

Bridge from the global Agentic OS into RunSmart's distribution work. Companion to `runsmart-web.md` and `runsmart-ios.md`. The RunSmart repo's local Agent OS remains the source of truth for product implementation. This bridge governs what the Distribution OS may read and write.

## 1. Where The Project Lives

- RunSmart Web: `/Users/nadavyigal/Documents/RunSmart`
- RunSmart iOS: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

Distribution work crosses both: ASO + iOS launch material flows through iOS; web landing pages and SEO flow through Web. The product positioning lives once and is referenced by both.

## 2. What Distribution Files Should Exist In The Project

Inside RunSmart's web repo (or wherever positioning is canonical) at `.agent-os/distribution/`:

- `product-positioning.md` (mirrored to `.agents/product-marketing.md`)
- `audience.md`
- `channels.md`
- `messaging.md`
- `competitors.md`
- `seo-program.md`
- `app-store-program.md`
- `lifecycle-program.md`
- `experiment-backlog.md`
- `weekly-plan.md`
- `metrics.md`
- `assets-needed.md`
- `lessons.md`

Scaffold: `distribution-os/projects/runsmart/scaffold/`. Install instructions are in that folder's `README.md`.

## 3. What The Distribution OS Can Read From The Project

- All `.agent-os/distribution/*.md` files
- `.agents/product-marketing.md`
- Public web pages (live URLs, screenshots)
- App Store listing data via the founder's exports
- PostHog and other analytics via the founder's exports

## 4. What The Distribution OS Can Update Inside The Project

Update only with founder approval. Default writes happen at the global level (in `distribution-os/`) and Drive / Notion. When an update belongs inside the project repo (e.g., updated `.agent-os/distribution/seo-program.md`), the agent produces a draft inside `distribution-os/projects/runsmart/scaffold/drafts/` and asks the founder to copy it across.

## 5. What Requires Founder Approval

- App Store listing changes (any submitted field)
- Web landing or homepage hero changes
- Email triggers being enabled in production
- LinkedIn posts (founder posts manually)
- Partnership outreach to a specific person
- Public comparison page wording (Runna, Garmin Coach, Strava)
- Anything that affects monetization

## 6. How To Run A Weekly Distribution Cycle For RunSmart

1. Set the command center to "Focused product: RunSmart"
2. Pick the theme from the highest-tier A channel without active work this month
3. Run `distribution-os/workflows/00-weekly-distribution-cycle.md`
4. Draft assets in the right Drive folder + experiment rows
5. Stop at founder review

Common weekly themes for RunSmart:

- ASO listing refresh
- Web landing rewrite (one page)
- Runna comparison page draft
- Lifecycle email backbone draft
- Coach partnership outreach (3 to 5 specific people)
- Garmin / Strava integration content
- LinkedIn founder cadence

## 7. Constraints This Bridge Inherits

- All `GLOBAL-AGENT-RULES.md` rules
- All `distribution-os/operating-principles.md`
- The RunSmart-specific constraints in `distribution-os/projects/runsmart.md`

## 8. Token Efficiency

For RunSmart distribution work, load:

- `distribution-os/distribution-context.md`
- `distribution-os/operating-principles.md`
- `distribution-os/projects/runsmart.md`
- This bridge
- The specific workflow + skill the task needs

Do not load ResumeBuilder bridges or files unless cross-product context matters.
