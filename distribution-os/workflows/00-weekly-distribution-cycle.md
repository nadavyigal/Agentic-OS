# Weekly Distribution Cycle

The master loop. Runs once a week. Total agent time: 45 to 90 minutes when nothing is on fire. Founder review time: 30 to 60 minutes.

Inputs:

- This folder (`distribution-os/`)
- The focused product's bridge file (`PROJECT-BRIDGES/{product}-distribution.md`)
- The focused project repo's `.agent-os/distribution/` (or scaffold under `projects/{product}/scaffold/`)
- Latest metrics (Notion Metrics Log + Drive `05 Metrics Exports/`)
- Notion Distribution Command Center + Experiment Backlog
- Google Drive `00 Source Material/` and `01 Product Docs/` if relevant

Output:

- Updated `distribution-command-center.md`
- New row in `weekly-growth-review.md` (and Drive copy in `06 Weekly Reports/`)
- 1 to 3 draft assets in `Google Drive > 03 Campaigns/{product}/` or `04 Content Assets/`
- Updated `experiment-log.md`, `channel-backlog.md`, `metrics-dashboard.md`, `lessons.md`
- Notion sync: command center row updated, experiment rows current, campaign tasks created

## Steps

### Step 1 — Load context

Read in order:

1. `distribution-os/distribution-context.md`
2. `distribution-os/operating-principles.md`
3. `distribution-os/distribution-command-center.md`
4. `distribution-os/projects/{focused-product}.md`
5. `distribution-os/lessons.md`
6. Last 4 entries in `weekly-growth-review.md`

State the focused product, the theme, and the constraint of the week in one paragraph.

### Step 2 — Pull metrics

Read `distribution-os/metrics-dashboard.md`. For each north-star metric, get the current value and the diff vs last week. Sources:

- PostHog (web + app events)
- Vercel (web traffic, deploys)
- App Store Connect (RunSmart)
- Search Console (ResumeBuilder)
- Stripe (when monetization is live)
- Notion Metrics Log if it has fresher numbers than your raw exports

If a number cannot be retrieved, write `unknown` and continue. Do not invent.

### Step 3 — Review lessons and ERRORS

Read `distribution-os/lessons.md`, project-level `.agent-os/distribution/lessons.md`, `~/.claude/LEARNINGS.md`, and `~/.claude/ERRORS.md`. Block any experiment that repeats a logged failure.

### Step 4 — Identify bottlenecks

Where is the funnel weakest? Use the funnel map in `metrics-dashboard.md` for the focused product. The biggest weekly diff or the lowest conversion step is usually the right place to focus.

### Step 5 — Generate candidate experiments

Pull from:

- The product's `experiment-backlog.md` (scaffold or project repo)
- The channels in `channel-backlog.md` rated tier A for the product
- The bottleneck identified in step 4
- New ideas from `marketingskills/skills/marketing-ideas/SKILL.md` if needed

Generate at least 5 candidates. For each: a one-line hypothesis, channel, and rough effort.

### Step 6 — Score and pick top 3

Score every candidate with the formula in `experiment-log.md`. Apply the founder fit and effort dimensions ruthlessly. Pick the top 3 by score, with at most one experiment >= 3 days of effort.

If fewer than 3 score >= 15, pick fewer experiments. Quality over filling slots.

### Step 7 — Draft assets for the top 3

For each chosen experiment:

1. Identify the right skill (`distribution-os/skills/skills-index.md`)
2. Load the skill
3. Produce the draft using the matching template in `distribution-os/templates/`
4. Save the draft to `Google Drive > 03 Campaigns/{product}/{date}-{slug}/` (or to the project repo if it is a page change)
5. Add an entry in `experiment-log.md` with status `awaiting review`

### Step 8 — Update logs and Notion

- Append to `experiment-log.md`
- Update channel statuses in `distribution-command-center.md`
- Append to `metrics-dashboard.md`-linked Notion Metrics Log
- Update Notion: Command Center row, Experiment Backlog rows, Campaign Calendar entries
- Update Notion Content / Asset Pipeline with each draft

### Step 9 — Founder review checklist

Produce a single message to the founder containing:

- Theme and focused product
- Top 3 experiments (one line each) with score
- Drafts ready for review (file paths or Drive links)
- Open questions
- What requires explicit approval before any external publish

Stop here. Do not publish anything.

### Step 10 — After founder review

When the founder marks an asset `approved`:

1. Update the asset header from `reviewed` to `approved`
2. Update `experiment-log.md` status to `running`
3. Set the experiment's start date
4. Schedule a measurement check (next week's cycle)

When the founder rejects an asset:

1. Move it to a `rejected/` folder in Drive
2. Add a one-line note in `lessons.md` if the rejection reveals a reusable rule

### Step 11 — Write the weekly report

Fill `templates/weekly-report-template.md`. Append to `weekly-growth-review.md`. Copy to Drive `06 Weekly Reports/`. Update Notion Command Center with link.

## Failure Modes

| Symptom | Fix |
|---|---|
| Same channel chosen 4 weeks running with no results | Force a channel switch; rescore in `channel-backlog.md` |
| Drafts never become approved | Founder is the bottleneck; cut to 1 experiment / week |
| Metrics are mostly `unknown` | Spend a week wiring measurement (an `analytics` skill task) before more experiments |
| Lessons file is empty after 4 cycles | Lower the bar for capturing or revisit the format |
| Both products being touched every week | Pick one. The principle exists for a reason. |
