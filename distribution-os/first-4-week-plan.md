# First 4-Week Plan

Starting from the day the Distribution OS is installed. Two products in scope: RunSmart and ResumeBuilder. The first month gets the system into working order without over-promising output.

Default split: 2 weeks RunSmart focus, 2 weeks ResumeBuilder focus. Adjust at the end of week 2 based on what actually shipped.

## Week 1 — Set Up

### Goals

- Distribution OS operational
- Positioning current for both products
- Channels scored for both products
- Measurement baseline established
- First experiment backlog populated

### Inputs Needed

- Founder confirms / edits `projects/runsmart.md` and `projects/resumebuilder.md`
- Founder copies scaffolds into project repos (or confirms the scaffold versions are the working draft)
- Access to PostHog, Search Console, App Store Connect, Vercel, Stripe (where relevant)
- Notion workspace created (databases per `data/notion-map.md`)
- Google Drive folder tree created (per `data/google-drive-map.md`)

### Agent Tasks

1. Read all root distribution-os files
2. Confirm scaffold positioning matches the founder's current view of each product
3. Score channels for both products in `channel-backlog.md`
4. Establish baseline metrics in each product's `metrics.md` and the Notion Metrics Log
5. Populate `experiment-log.md` with 10 candidate experiments per product (proposed status, scored)

### Founder Review Tasks

- Confirm positioning drafts
- Confirm channel tiers (move anything from B to A or A to B if needed)
- Confirm baseline metric definitions
- Approve top 6 candidate experiments per product (3 to run, 3 in queue)

### Outputs

- `distribution-command-center.md` filled
- `channel-backlog.md` filled
- `experiment-log.md` with 20 candidate experiments
- Notion databases populated
- Drive folder tree exists
- Week-of-week-1 entry in `weekly-growth-review.md`

### Metrics To Check

- (none yet; week 1 establishes the baseline)

## Week 2 — First RunSmart Experiments

### Goals

- Run 3 RunSmart experiments end-to-end (or to first founder approval)
- Maintain ResumeBuilder

### Inputs Needed

- Approved experiments from week 1
- App Store Connect access for ASO experiment
- A specific running coach / club / podcast prospect list (founder seeds 5 names) for partnerships

### Agent Tasks

1. ASO audit and listing rewrite (load `marketingskills/skills/aso/SKILL.md`)
2. Runna comparison page draft (load `marketingskills/skills/competitors/SKILL.md` + `competitor-profiling/SKILL.md`)
3. Lifecycle email backbone draft: welcome + plan-generated nudge + week-1 adherence digest (load `marketingskills/skills/emails/SKILL.md`)
4. LinkedIn founder cadence: one post draft (load `marketingskills/skills/social/SKILL.md`, LinkedIn sections only)
5. ResumeBuilder: SEO opportunity mining pass; pick 3 Tier-1 SEO pages to draft next week

### Founder Review Tasks

- Approve ASO copy before App Store submission
- Approve Runna comparison draft
- Approve 3 lifecycle email drafts
- Approve LinkedIn post (or post it manually)

### Outputs

- ASO rewrite saved to Drive `03 Campaigns/RunSmart/asoaudit-{date}/`
- Runna page draft in Drive
- 3 email drafts in Drive
- LinkedIn post in Drive
- Updated `experiment-log.md`
- Week 2 report in `weekly-growth-review.md`

### Metrics To Check

- Last week's baseline confirmed and stable
- App Store impressions and install rate logged
- LinkedIn impressions for any prior posts (if any)

## Week 3 — First ResumeBuilder Push

### Goals

- Run 3 ResumeBuilder experiments end-to-end (or to first founder approval)
- Maintain RunSmart (monitor week-2 launches)

### Inputs Needed

- Search Console export
- Existing site URLs and current pricing page
- Founder confirms whether free ATS tool MVP is approved for scope

### Agent Tasks

1. Build 3 Tier-1 SEO briefs (one for `ats-resume-builder`, one comparison page, one `ai-resume-tailoring` — adjust based on Search Console signals)
2. Free ATS / resume scoring tool brief (load `marketingskills/skills/free-tools/SKILL.md` + `lead-magnets/SKILL.md`)
3. Directory submission pack v1 (all length variants + screenshots) using `marketingskills/skills/directory-submissions/SKILL.md`
4. Conversion review on signup → editor → export funnel (load `marketingskills/skills/cro/SKILL.md`)
5. Lifecycle email backbone draft: welcome + didn't-start + activation-hit
6. RunSmart maintenance: monitor week-2 experiments, log results so far

### Founder Review Tasks

- Approve 3 SEO briefs
- Approve free tool scope
- Approve directory submission pack
- Approve conversion review changes
- Approve lifecycle emails

### Outputs

- 3 SEO briefs in Drive `04 Content Assets/SEO Briefs/ResumeBuilder/`
- Free tool brief in Drive `03 Campaigns/ResumeBuilder/free-tools/`
- Directory pack in Drive `04 Content Assets/Directory Submissions/ResumeBuilder/pack/`
- Conversion review in Drive `03 Campaigns/ResumeBuilder/{page}/`
- 3 email drafts in Drive
- Updated logs

### Metrics To Check

- RunSmart App Store install rate vs week 1 baseline (early signal)
- LinkedIn post performance (week 2's post)
- ResumeBuilder current signups, indexed pages, organic clicks
- Funnel: signup → export rate

## Week 4 — Measure And Decide

### Goals

- Measure the cumulative effect of weeks 2 and 3 experiments
- Capture lessons
- Decide month 2 focus pattern
- Produce the next 4-week experiment backlog

### Inputs Needed

- All metrics current
- All week-2 and week-3 experiments at decisional stage (target hit / missed / pending)

### Agent Tasks

1. Run `prompts/analyze-growth-results.md` for the full 4-week window across both products
2. Run `prompts/update-distribution-memory.md`
3. Run `workflows/12-monthly-strategy-review.md` (this replaces the standard weekly cycle for this week)
4. Re-score channels in `channel-backlog.md`
5. Propose month 2 focus pattern (default 3-1 or 2-2)
6. Generate next 4-week experiment backlog (5 to 8 candidates per product, scored)

### Founder Review Tasks

- Confirm month 2 focus pattern
- Approve next 4-week experiment backlog
- Confirm any positioning or messaging changes that emerged from week-2 / week-3 results
- Decide what to kill from the active list

### Outputs

- Monthly review entry at top of `weekly-growth-review.md`
- Updated `channel-backlog.md`
- Updated `experiment-log.md` with month-2 candidates
- Updated `lessons.md`
- Possible promotions to `~/.claude/LEARNINGS.md` and `~/.claude/ERRORS.md`
- Notion Command Center cleared for month 2

### Metrics To Check

- Week 4 vs week 1 baseline for both products
- Any channel showing >= 20% relative movement
- Which experiments hit, missed, or were inconclusive
- Founder's time spent per channel (effort-to-result ratio)

## Anti-Patterns To Watch For During The First Month

- Running too many experiments at once (cap at 3 per product per week)
- Treating Drive or Notion as authoritative — project repos and `distribution-os/` are
- Letting the lifecycle emails draft without measurement plans
- Publishing the Runna comparison page or any external asset without founder explicit go-ahead
- Spending week 1 on tooling instead of getting one real experiment moving by end of week 2
