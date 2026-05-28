# Market Research Workflow

Run when starting on a product, when entering a new segment, or quarterly as a refresh. Not weekly.

Goal: produce a current-state snapshot of users, competitors, and category that informs positioning and channel choice.

## Inputs

- `distribution-os/projects/{product}.md`
- Project repo's product positioning, if it exists
- Any existing user interviews, support tickets, or feedback in Drive `02 Market Research/`
- Industry reports if available

## Steps

### 1. Define the segment

Write the segment in one sentence: who, doing what, in what context, with what trigger. Example:

- RunSmart: a beginner runner training for their first 5K who needs an adaptive plan because life keeps disrupting their training.
- ResumeBuilder: a mid-career professional applying to roles in a new function who needs to tailor their resume to ATS scans without losing voice.

### 2. Pull existing customer-research material

Load `marketingskills/skills/customer-research/SKILL.md`. Look for:

- Pains
- Workarounds they use today
- Words they use (not jargon)
- Triggers (events that move them from passive to active)

If no material exists, run a lightweight pass: 5 to 10 sources (support threads, app reviews, Reddit posts) and capture quotes verbatim.

### 3. Identify direct and adjacent competitors

Load `marketingskills/skills/competitor-profiling/SKILL.md`. List:

- Direct competitors (same job, same target)
- Adjacent competitors (similar tools, broader job)
- Free / DIY alternatives the user might pick instead

For RunSmart this includes Runna, Garmin Coach, Strava plans, free Reddit plans, generic running calculators. For ResumeBuilder this includes Teal, Rezi, Kickresume, ChatGPT-as-resume-tool, free templates, and career coaches.

### 4. Score each competitor

For each: brand strength, product strength, distribution strength, monetization strength, vulnerability to disruption (1–5 each). Pick the top 3 most useful to compare against on landing pages. Defer the rest.

### 5. Identify category narratives

What story is the category telling? What is missing? Where is the founder narrative more credible than the incumbent?

### 6. Identify channel signals

For each major competitor, observe (do not engage):

- Where they show up (App Store keywords, SEO topics, LinkedIn, podcasts, partnerships)
- What works (top pages by traffic, top ASO terms)
- What looks performative versus what actually moves users

### 7. Output

Produce `Google Drive > 02 Market Research/{product}/{YYYY-MM-DD}-snapshot.md` with:

- Segment definition
- Customer-research quotes and themes
- Competitor scorecard
- Category narrative observation
- Channel signal summary
- 5 implications for distribution (each one tied to a channel or experiment)

Add the snapshot link to `distribution-os/projects/{product}.md` under the "Current research" section.

### 8. Decide implications

The agent does not silently update positioning. Surface the 5 implications and ask the founder to confirm which become updates to:

- `.agent-os/distribution/product-positioning.md`
- `channel-backlog.md`
- `experiment-log.md`
