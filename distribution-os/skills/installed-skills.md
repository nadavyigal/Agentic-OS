# Installed Skills

Inventory of what is present in the cloned `marketingskills/` repository, from `coreyhaines31/marketingskills`. Update this file when the repo is pulled.

Last verified: load the agent on the date noted below.

- Location: `../../marketingskills/skills/`
- Repo: https://github.com/coreyhaines31/marketingskills
- License: MIT
- Spec: https://agentskills.io/specification.md

## Skill Inventory

All skills are loaded from `marketingskills/skills/{name}/SKILL.md`.

| Skill | Category | Used By This OS |
|---|---|---|
| ab-testing | Measurement | Yes |
| ad-creative | Paid | No (deferred) |
| ads | Paid | No (deferred) |
| ai-seo | SEO | Yes (ResumeBuilder primarily) |
| analytics | Measurement | Yes |
| aso | App Store | Yes (RunSmart primarily) |
| churn-prevention | Retention | Yes (when monetization live) |
| co-marketing | Partnerships | Yes |
| cold-email | Outreach | No (founder constraint) |
| community-marketing | Community | Yes (RunSmart, observation only) |
| competitor-profiling | Research | Yes |
| competitors | SEO + sales | Yes |
| content-strategy | Strategy | Yes |
| copy-editing | Copy | Yes |
| copywriting | Copy | Yes |
| cro | Conversion | Yes |
| customer-research | Research | Yes |
| directory-submissions | Distribution | Yes |
| emails | Lifecycle | Yes |
| free-tools | Engineering-as-marketing | Yes (ResumeBuilder primarily) |
| image | Asset gen | Ad hoc |
| launch | GTM | Yes (RunSmart) |
| lead-magnets | Lead gen | Yes |
| marketing-ideas | Strategy | Yes |
| marketing-psychology | Strategy | Yes |
| onboarding | Conversion | Yes |
| paywalls | Conversion | Yes (when paid live) |
| popups | Conversion | Yes (sparingly) |
| pricing | Monetization | Yes |
| product-marketing | Foundation | Yes (mandatory) |
| programmatic-seo | SEO at scale | Yes (ResumeBuilder primarily) |
| prospecting | Outreach | No (deferred) |
| referrals | Growth | Yes (when monetization live) |
| revops | Sales | No (deferred) |
| sales-enablement | Sales | Optional (partnerships) |
| schema | SEO | Yes |
| seo-audit | SEO | Yes |
| signup | Conversion | Yes |
| site-architecture | SEO | Yes |
| sms | Messaging | No |
| social | Content | Yes (LinkedIn only) |
| video | Content | No |

## Skill File Convention

Each skill has:

- `SKILL.md` — primary instructions, < 500 lines
- `references/` (sometimes) — deep-dive references
- `scripts/` (sometimes) — executable helpers
- `assets/` (sometimes) — templates and example data

Most skills look for a product marketing context file at:

```
.agents/product-marketing.md
.claude/product-marketing.md   (fallback)
.claude/product-marketing-context.md   (legacy fallback)
```

This OS writes that file into each project repo. See `projects/{name}/scaffold/product-marketing.md`.

## Update Process

When the repo updates:

1. Pull from the repo home (`cd marketingskills && git pull`)
2. Re-read this file's table against new contents
3. If new skills appeared, decide whether to add them to `skills-index.md`
4. Update the verification date below

Verification date: pending first run.
