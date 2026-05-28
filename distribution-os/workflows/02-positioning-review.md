# Positioning Review Workflow

Quarterly or whenever the product evolves significantly. Confirms that the words the product uses match the way users think and the way the channels reward.

## Inputs

- `distribution-os/projects/{product}.md`
- Project repo's `.agent-os/distribution/product-positioning.md` (or scaffold)
- Latest market research snapshot from `workflows/01-market-research.md`
- Top performing pages and ASO terms (from `metrics-dashboard.md`)

## Steps

### 1. Load skill

`marketingskills/skills/product-marketing/SKILL.md`

If a positioning file already exists, treat the skill as a critique tool, not a from-scratch generator.

### 2. Restate current positioning

Pull out:

- One-line positioning
- Target user
- The job-to-be-done
- The before / after state
- The category
- The differentiators (named and earned)
- The proof points

Write each in the user's words where possible (from `customer-research`).

### 3. Compare against three reference points

- The market research snapshot
- The top 3 competitors' positioning
- The current top-performing pages and ASO terms

For each, note alignment / drift / gap.

### 4. Decide what changes

For each gap, propose a specific change:

- Wording change (where: page, ASO field, email)
- New asset (what kind, which channel)
- Decision to leave as is (with reason)

### 5. Output

Produce two files:

- An updated draft of `.agent-os/distribution/product-positioning.md` (do not overwrite the live file; produce as `.draft.md`)
- A `positioning-review-{YYYY-MM-DD}.md` change summary in Drive `02 Market Research/{product}/`

### 6. Approval and rollout

Founder reviews the draft. On approval:

1. Replace the live positioning file
2. Mirror it to `.agents/product-marketing.md` so marketingskills can find it
3. Add a `DECISIONS.md` entry at the Agentic OS root if the change is durable
4. Flag any in-flight assets that need rewriting

### 7. Cadence

This workflow runs:

- Quarterly by default
- When a major product change ships
- When weekly cycle results suggest user language has shifted (>= 2 lessons pointing at messaging)
