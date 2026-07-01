# AGENTS.md — Distribution OS

Rules for any agent (Claude Code, Codex, Cursor) doing distribution work. Sits under the global Agentic OS AGENTS.md — that file's rules still apply.

## Session Start Ritual (Distribution Work)

Before producing anything:

1. Read `distribution-os/distribution-context.md`
2. Read `distribution-os/operating-principles.md`
3. Read `distribution-os/distribution-command-center.md` for current focus
4. Read `distribution-os/data/connectors.md` for Notion + Drive IDs
5. Read `distribution-os/lessons.md`
6. Read the relevant `distribution-os/projects/{product}.md`
7. If the work needs a specific skill, read `distribution-os/skills/skills-index.md` and load the chosen skill from `marketingskills/skills/{skill}/SKILL.md`
8. If product positioning is needed, read the project repo's `.agent-os/distribution/product-positioning.md` (or the scaffold under `distribution-os/projects/{product}/scaffold/`)
9. State the objective in one sentence before producing anything

## Promoting Work to the Daily Pipeline

When a channel or experiment from this folder becomes a work packet (`executive-os/work-packets/`) or a `BACKLOG.md` line, tag it `Mode: Grower` — see `AGENTS.md` Mode Contracts. This folder stays the scoring source; the tag is only added at the point work leaves here and enters daily execution.

## What An Agent Can Do Without Asking

- Draft any asset (SEO brief, LinkedIn post, email, landing page copy, directory submission, campaign brief)
- Score experiments
- Score channels
- Update local files inside `distribution-os/` and `distribution-os/projects/`
- Append rows to `experiment-log.md`, `channel-backlog.md`, `lessons.md`
- Generate weekly reports

## What An Agent Must Ask Before Doing

- Publishing anything externally (post, email send, public page deploy, App Store listing change)
- Paying for anything (ads, tools, subscriptions)
- Sending outreach to a real person not in the founder's existing relationship
- Editing files inside a product repo's source code
- Adding new dependencies anywhere

## What An Agent Must Never Do

- Generate content for its own sake. Every asset must connect to a hypothesis in `experiment-log.md` or a campaign in the command center
- Treat Notion or Google Drive as authoritative for product facts — those live in the project repo and `projects/{product}.md`
- Run cold outreach campaigns that resemble spam. Partnerships only, with clear personal context
- Add paid ads to a plan unless the founder explicitly asks
- Manufacture metrics. If a metric is not in `metrics-dashboard.md` or a real source, mark it `unknown` and stop
- Recommend an experiment already logged as a failure in `lessons.md`
- Publish to App Store, web, LinkedIn, email, or any external channel without explicit "yes, publish this" in the current message

## Asset Quality Bar

Every draft an agent produces must:

- Cite the hypothesis it supports (or be marked exploration only)
- Name the channel and target audience
- Include a success metric and how it will be measured
- Pass the `templates/landing-page-review-template.md` heuristics if it is a page or post
- Be labeled `draft`, `reviewed`, or `approved` in the filename header

## Founder Approval Checklist (Before Anything Publishes)

1. Hypothesis is clear and falsifiable
2. Asset is on-brand for the product
3. Measurement plan exists and is realistic
4. No claims that cannot be backed up
5. No external sends or deploys without explicit founder go-ahead
6. Rollback path is obvious if the experiment goes wrong

## Output Format

When the agent finishes a distribution task it should return:

- What it understood (one line per: product, channel, hypothesis)
- What it produced (file paths, draft links)
- What it updated (rows in logs, status changes)
- What requires founder review before publishing
- Open questions

## Token-Efficiency

- Do not load every marketingskills SKILL.md by default — only the one(s) the task needs
- Do not duplicate product positioning from the project repo into this folder
- Summaries over copies. If a Drive doc is 20 pages, ask for a summary or skim
- For weekly runs, the agent only needs: this folder + one project + 1–2 skills
