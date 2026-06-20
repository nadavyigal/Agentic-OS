# Installed Skills

Master inventory of skills installed in this OS. Skills live under `.agents/skills/<domain>/<name>/SKILL.md` (the cross-agent standard home). This file is the source of truth for what is actually present; update it when a domain changes.

> **Path note (2026-06-20):** Earlier versions of this catalog pointed at `marketingskills/skills/`. That full clone was removed from the working tree. The curated marketing skills now live in `.agents/skills/marketing/`; the full upstream pack is retained for reference only under `archive/marketingskills/skills/` (not loaded by agents).

Last verified: 2026-06-20.

## Domains

| Domain | Location | Count | Source | License |
|---|---|---|---|---|
| marketing | `.agents/skills/marketing/` | 12 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT |
| product-management | `.agents/skills/product-management/` | 8 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | MIT |
| engineering | `.agents/skills/engineering/` | 3 + 1 agent | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| vault tooling | `.claude/skills/` | 2 | obsidian-markdown, json-canvas | MIT |

All slices were security-scanned with SkillSpector before install (0/100 SAFE each). See each domain's `README.md`.

## Marketing (12 active — `.agents/skills/marketing/`)

| Skill | Category | Primary product |
|---|---|---|
| ai-seo | SEO | ResumeBuilder |
| analytics | Measurement | Both |
| aso | App Store | RunSmart |
| competitor-profiling | Research | Both |
| competitors | SEO + sales | Both |
| onboarding | Conversion | Both |
| paywalls | Conversion | Both (when paid live) |
| pricing | Monetization | Both |
| product-marketing | Foundation | Both (mandatory) |
| programmatic-seo | SEO at scale | ResumeBuilder |
| seo-audit | SEO | ResumeBuilder |
| site-architecture | SEO | ResumeBuilder |

The remaining ~30 upstream marketing skills (ads, cold-email, emails, launch, social, churn-prevention, etc.) are **not installed**. They are archived at `archive/marketingskills/skills/` for reference; promote one into `.agents/skills/marketing/` only when a workflow needs it.

## Product Management (8 active — `.agents/skills/product-management/`)

create-prd, user-stories, prioritization-frameworks, pre-mortem, outcome-roadmap, analyze-feature-requests, prioritize-assumptions, interview-script. See `.agents/skills/product-management/README.md`.

## Engineering (3 + 1 agent — `.agents/skills/engineering/`)

frontend-ui-engineering, performance-optimization, observability-and-instrumentation, and the `web-performance-auditor` subagent. See `.agents/skills/engineering/README.md`.

## Skill File Convention

Each skill is a directory with `SKILL.md` (primary instructions, < 500 lines). Some upstream skills also ship `references/`, `scripts/`, or `assets/`; this OS installs **`SKILL.md` only** to keep context lean and avoid pulling executable helpers.

Marketing skills look for a product marketing context file, in this order:

```
.agents/product-marketing.md
.claude/product-marketing.md            (fallback)
.claude/product-marketing-context.md    (legacy fallback)
```

This OS writes that file into each project repo from `distribution-os/projects/{name}/scaffold/`.

## Update Process

When adopting or refreshing a slice:

1. Clone the upstream repo to a temp dir.
2. **Security gate:** `docker run --rm -v "$TMP:/scan" skillspector scan ./ --no-llm`. If the slice you want scores risky, scan it in isolation before trusting the verdict.
3. Copy `SKILL.md` files only into `.agents/skills/<domain>/`.
4. Update this file and the domain `README.md`.
5. Pin to the adoption date; do not chase upstream on a schedule.
