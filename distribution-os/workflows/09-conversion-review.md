# Conversion Review Workflow

Run on any high-traffic page that converts poorly, any new landing page before launch, and the pricing page quarterly.

## Inputs

- Page URL or local file path
- Traffic and conversion data (PostHog / GA)
- Customer-research quotes
- Competitor versions of the same kind of page

## Steps

### 1. Load skills

In order:

1. `marketingskills/skills/cro/SKILL.md` — primary
2. `marketingskills/skills/copywriting/SKILL.md` — for headline / above-fold rewrites
3. `marketingskills/skills/marketing-psychology/SKILL.md` — for framing checks
4. `marketingskills/skills/signup/SKILL.md` — if the page is a signup / activation flow
5. `marketingskills/skills/popups/SKILL.md` — only if a popup is on the table

### 2. Establish the baseline

- Visits / week (last 4 weeks)
- Conversion rate
- Top traffic sources
- Top devices
- Average session duration
- Common drop-off points (heatmap or event funnel)

### 3. Apply the page review template

Use `templates/landing-page-review-template.md`. Walk every section:

- Above the fold: hero, headline, subhead, CTA
- Social proof
- Body sections (one per major idea)
- Objections handled
- CTA repetition and clarity
- Page weight / speed
- Mobile rendering

For each, note: keep / change / replace, and a one-line reason.

### 4. Identify the top 3 changes

Rank changes by expected impact on conversion versus effort. Pick the top 3. Avoid bundling.

### 5. Produce the rewrite

Produce a draft of the new page (markdown for static pages, copy block for components). Include:

- Two headline candidates
- One subhead
- Restructured sections
- Specific CTA wording

### 6. Plan measurement

Decide whether to deploy directly or A/B test (`marketingskills/skills/ab-testing/SKILL.md`). For thin traffic, deploy directly and compare pre / post over 2 to 4 weeks.

### 7. Output

- Rewrite saved to Drive `03 Campaigns/{product}/{date}-{page}/`
- `experiment-log.md` row with hypothesis and measurement plan
- Notion Campaign Calendar entry

### 8. Approval and rollout

Founder reviews. On approval, page changes ship via the product repo planning protocol. After 2 weeks, measure and log result.
