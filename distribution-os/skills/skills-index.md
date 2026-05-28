# Skills Index

Map from distribution intent to the skill (or skills) in `marketingskills/skills/` to load. This is the agent's lookup table.

Companion files:

- `installed-skills.md` — what is present in the cloned `marketingskills/` repo
- `recommended-skills.md` — which subset to install per product, with rationale
- `skill-usage-guide.md` — how to invoke a skill from inside a workflow

## How To Use This Index

1. Identify the task (intent column)
2. Load only the skill(s) named in `primary skill`
3. If positioning is missing, load `product-marketing` first
4. If the task spans multiple skills, chain them in the listed order

## Cross-Cutting Foundations

Every workflow loads at most one foundation skill first.

| Intent | Primary Skill | When |
|---|---|---|
| Establish or read product positioning | `marketingskills/skills/product-marketing` | First time per product, or when positioning is stale |
| Plan content broadly | `marketingskills/skills/content-strategy` | Before any SEO or social push |
| Apply persuasion / framing | `marketingskills/skills/marketing-psychology` | When refining copy |
| Brainstorm | `marketingskills/skills/marketing-ideas` | Stuck or starting a new channel |

## RunSmart-Heavy Intents

| Intent | Primary | Optional Add-On |
|---|---|---|
| Audit App Store listing | `aso` | `competitor-profiling` |
| Plan launch (feature, update) | `launch` | `aso`, `social` |
| Optimize onboarding | `onboarding` | `cro` |
| Reduce churn / improve retention | `churn-prevention` | `emails`, `paywalls` |
| Community research and presence | `community-marketing` | `customer-research` |
| Find coach / club partners | `co-marketing` | |
| Founder LinkedIn cadence | `social` | `copywriting` |
| Compare to Runna and similar | `competitors` | `competitor-profiling` |
| Build referral motion (when ready) | `referrals` | |
| Pricing experiments (paid tier) | `pricing` | `paywalls` |

## ResumeBuilder-Heavy Intents

| Intent | Primary | Optional Add-On |
|---|---|---|
| SEO audit | `seo-audit` | `schema`, `site-architecture` |
| AI search optimization | `ai-seo` | |
| Build pages at scale (role, industry, location) | `programmatic-seo` | `schema`, `content-strategy` |
| Compete with other resume / ATS tools | `competitors` | `competitor-profiling` |
| Build free ATS or scoring tool | `free-tools` | `lead-magnets` |
| Submit to directories | `directory-submissions` | |
| Job-seeker lead magnets | `lead-magnets` | |
| Lifecycle email | `emails` | `onboarding` |
| Pricing for credit system | `pricing` | `paywalls` |
| Landing page CRO | `cro` | `copywriting`, `popups` |
| Signup flow | `signup` | `cro` |
| Career coach partnerships | `co-marketing` | |
| Sales collateral (when partnerships scale) | `sales-enablement` | |

## Cross-Product Intents

| Intent | Primary |
|---|---|
| Conversion review of any page | `cro` |
| Write or rewrite copy | `copywriting` |
| Edit existing copy | `copy-editing` |
| A/B test design | `ab-testing` |
| Set up tracking | `analytics` |
| Customer / user research | `customer-research` |
| Find marketing ideas | `marketing-ideas` |
| Apply psychology to a flow | `marketing-psychology` |

## Intentionally Deferred Skills

Skills not used by default for this OS. Re-evaluate when conditions change.

| Skill | Why deferred |
|---|---|
| `ads` | Free / low-cost first principle |
| `ad-creative` | Only relevant when ads run |
| `cold-email` | Founder constraint: no mass cold outreach |
| `prospecting` | Same as above |
| `revops` | Premature for solo-founder stage |
| `sms` | Not aligned with current audiences |
| `video` | Founder is not a heavy content creator |
| `image` | Use ad hoc; no dedicated workflow |
