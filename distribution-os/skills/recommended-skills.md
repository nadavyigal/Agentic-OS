# Recommended Skills Per Product

Curated subset to install into each project repo under `.agents/skills/` or to symlink from `marketingskills/skills/`. Keep installation small to avoid context bloat — each project pulls only what its weekly cycle needs.

## RunSmart Recommended Set

Foundations (always):

- `product-marketing`
- `customer-research`
- `marketing-psychology`

Acquisition:

- `aso` — App Store optimization is the primary lever
- `copywriting` — App Store and landing page copy
- `cro` — Landing page and pricing page optimization
- `competitors` — Compare-to-Runna and alternative pages
- `competitor-profiling` — Ongoing competitive intelligence
- `social` — LinkedIn founder cadence only
- `community-marketing` — Reddit / running forum observation
- `co-marketing` — Coach / club / podcast partnerships

Activation and retention:

- `launch` — Feature and version launches
- `onboarding` — First-run experience
- `churn-prevention` — Plan abandonment, recovery
- `emails` — Onboarding, weekly digest, lifecycle
- `paywalls` — When paid tier launches
- `pricing` — Paid tier design

Measurement:

- `analytics`
- `ab-testing`

Skip for RunSmart: `programmatic-seo`, `directory-submissions` (low fit for an iOS-first app), `free-tools` (the app is the tool), `prospecting`, `cold-email`, `ads`, `sms`, `video`.

## ResumeBuilder Recommended Set

Foundations (always):

- `product-marketing`
- `customer-research`
- `marketing-psychology`

Acquisition:

- `seo-audit` — Baseline SEO health
- `ai-seo` — AI overview citation
- `programmatic-seo` — Role / industry pages
- `schema` — Structured data for resume examples
- `site-architecture` — URL and internal-link plan
- `content-strategy` — Topic and example planning
- `competitors` — Compare-to alternatives
- `competitor-profiling`
- `free-tools` — Free ATS / resume scoring tool
- `lead-magnets` — Resume guides, ATS checklists
- `directory-submissions` — AI tool + career directories
- `co-marketing` — Career coach + HR partnerships
- `copywriting` — Landing, role pages, pricing
- `cro` — Editor, pricing, signup
- `signup` — Activation funnel
- `popups` — Exit intent and inline help, sparingly

Activation and retention:

- `onboarding`
- `emails` — Lifecycle for job seekers
- `paywalls`
- `pricing` — Credit-system messaging
- `sales-enablement` — Only if partnerships scale to real outreach

Measurement:

- `analytics`
- `ab-testing`

Skip for ResumeBuilder: `aso` (until iOS app), `community-marketing` (job seekers don't gather in product communities the same way), `prospecting`, `cold-email`, `ads`, `sms`, `video`, `referrals` (defer until monetization is steady).

## Installation Notes

The marketingskills repo is already cloned at `marketingskills/`. Two reasonable patterns:

1. **Reference-only (current default)**: workflows load skills by path from `../../marketingskills/skills/{name}/SKILL.md`. Nothing is copied.
2. **Project-local install**: in each project repo, copy or symlink the recommended set into `.agents/skills/`. This is useful when running agents directly inside the project repo without access to this folder.

Either works. Pick one per repo. Document the choice in the project's `.agent-os/distribution/README.md`.

## Skill Update Policy

- Pull `marketingskills/` quarterly or whenever a new skill ships that fits the recommended set
- Re-read `installed-skills.md` after each pull
- If a skill is replaced or renamed, update `skills-index.md` and any workflow that references it
