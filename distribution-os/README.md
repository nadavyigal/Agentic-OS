# Distribution OS

Cross-product distribution operating system for RunSmart and ResumeBuilder AI. Sits inside the Agentic OS. Drives a disciplined cycle:

> research → plan → prioritize → create → review → publish-ready assets → measure → learn → update memory

This is not a content factory. It is a small set of repeatable workflows the founder runs (or asks Codex / Claude Code to run) on a weekly cadence.

## What This Is

- A library of distribution workflows, prompts, templates, and channel playbooks
- A planning skeleton that pulls product context from the local project repos
- A bridge between the global Agentic OS, Google Drive (documents), and Notion (planning)
- A skill router that maps founder intent to specific skills in `marketingskills/`

## What This Is Not

- An automation platform (no n8n, Zapier, Make, Activepieces)
- A publisher (agents prepare drafts; the founder approves and publishes)
- A replacement for product-specific positioning that lives inside each repo

## Read Order

1. `distribution-context.md` — products, audiences, constraints
2. `operating-principles.md` — non-negotiables for any agent doing distribution work
3. `distribution-command-center.md` — current focus, this-week status
4. `workflows/00-weekly-distribution-cycle.md` — the master loop
5. `skills/skills-index.md` — what skills exist and when to use them
6. `data/source-of-truth-policy.md` — where each kind of fact lives
7. The project file relevant to today's work: `projects/runsmart.md` or `projects/resumebuilder.md`

## Where Different Things Live

| Layer | Lives In | Examples |
|---|---|---|
| Operating system + workflows + prompts | This folder | Weekly cycle, SEO brief workflow, prompts |
| Marketing skills library | `../marketingskills/skills/` | `cro`, `aso`, `programmatic-seo`, `directory-submissions` |
| Product-specific positioning + channels + backlog | Inside each project repo under `.agent-os/distribution/` (scaffold in `projects/{name}/scaffold/`) | RunSmart channel list, ResumeBuilder SEO program |
| Planning + status + experiment log | Notion (see `data/notion-map.md`) | Command Center, Experiment Backlog, Campaign Calendar |
| Source documents + drafts + assets + metrics exports | Google Drive (see `data/google-drive-map.md`) | Product docs, campaign briefs, weekly reports |
| Lessons learned (cross-product) | `lessons.md` here + `~/.claude/LEARNINGS.md` | Patterns that pay off twice |

## How To Use This Weekly

Run the prompt at `prompts/weekly-distribution-run.md` in Codex or Claude Code. The agent will load this folder, the relevant project bridge, and pull whatever Notion / Drive context is available. It produces draft assets and an updated weekly report. Nothing publishes without founder approval.

## How To Use This For A Single Campaign

Run `prompts/create-campaign.md` with one product + one channel + one goal. The agent produces a campaign brief, asset drafts, and a measurement plan. You review, edit, approve, then publish.

## Constraints Built In

- Free / low-cost channels first
- Product-led distribution before paid acquisition
- SEO, LinkedIn, partnerships, directories, free tools, lifecycle email are the default surfaces
- No paid ads as a default
- No mass content; quality and reuse over volume
- Founder is not a heavy content creator; minimize manual channel maintenance
