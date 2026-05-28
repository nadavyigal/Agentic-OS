# Skill Usage Guide

How agents invoke marketing skills from inside a distribution workflow.

## When To Invoke A Skill

Skills are loaded by the agent (Claude Code, Codex, Cursor) when a workflow says to. The agent then follows the skill's instructions. A skill is content, not code. Loading means: read the file, apply its rules to this specific task.

## Pattern 1 — Direct Load

From a workflow:

```
Load: marketingskills/skills/cro/SKILL.md
```

The agent reads the file, identifies the relevant section for the current task, and uses it as the working method. It does not paste the skill back to the user.

## Pattern 2 — Foundation + Specialist

Many skills (cro, aso, programmatic-seo, free-tools, onboarding) look for a product marketing context first. The chain:

1. Read project repo's `.agent-os/distribution/product-positioning.md` (or scaffold)
2. Mirror that file into `.agents/product-marketing.md` if the skill expects that path
3. Load the specialist skill
4. Apply

## Pattern 3 — Compose Skills

A workflow can chain skills. Example for a ResumeBuilder programmatic SEO push:

1. `marketingskills/skills/customer-research/SKILL.md` — confirm the role pages match real user search intent
2. `marketingskills/skills/programmatic-seo/SKILL.md` — design the templated page system
3. `marketingskills/skills/site-architecture/SKILL.md` — confirm URL structure and internal linking
4. `marketingskills/skills/schema/SKILL.md` — pick the right structured data
5. `marketingskills/skills/copywriting/SKILL.md` — write the page module copy
6. `marketingskills/skills/cro/SKILL.md` — verify the CTA logic

Each step produces one artifact. The workflow names them.

## Inputs Each Skill Expects

| Skill | Typical Inputs |
|---|---|
| `product-marketing` | Founder interview answers or existing positioning |
| `seo-audit` | Live site URL, Search Console access or export |
| `programmatic-seo` | Template idea + data source for pages |
| `ai-seo` | Pages or topics to optimize for AI overview citation |
| `aso` | App Store / Google Play URL |
| `cro` | Page URL, screenshot, traffic + conversion data |
| `directory-submissions` | Product summary, screenshot pack, founder info |
| `free-tools` | Problem space + user job description |
| `competitors` | List of competitors with URLs |
| `competitor-profiling` | URLs and product context |
| `emails` | Lifecycle funnel definition + product context |
| `launch` | Launch goal, date, asset list |
| `co-marketing` | Target partner type + product positioning |
| `social` | Channel (LinkedIn only here) + tone reference |
| `onboarding` | Current onboarding flow definition |
| `pricing` | Current pricing + customer segments + cost data |
| `analytics` | Existing tracking + business model |
| `ab-testing` | Page or flow + traffic baseline |
| `copywriting` | Audience + offer + page purpose |

## Outputs Each Skill Should Produce

Every skill output, when produced through this OS, should arrive as:

- A draft file named after the asset (`runsmart-aso-audit-YYYY-MM-DD.md`)
- A header block: product, channel, hypothesis or goal, status (`draft` / `reviewed` / `approved`), founder review needed yes / no
- A short "what would make this better next time" note for the lessons file
- A link or path to where the asset will live once approved (Drive folder, project repo path, or Notion)

## Token Discipline

- Never load multiple skills in parallel unless the workflow requires it
- Never paste skill instructions back to the founder. Use them.
- After applying, summarize only what was decided and what asset was produced

## When A Skill Conflicts With This OS

If a marketing skill recommends a practice that conflicts with this OS's principles (for example, recommending cold outreach blasts when the founder has set a "no spam" rule), follow this OS. Add a row in `lessons.md` noting the conflict and which side won.
