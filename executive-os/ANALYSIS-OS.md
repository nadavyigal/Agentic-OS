# Analysis OS

## Purpose

The Analysis OS is responsible for structured thinking, research, ideation, evidence
gathering, competitor research, market scans, GitHub/Reddit scans, feature
opportunity discovery, and consultancy-style recommendations. It turns raw questions
into evidence, evidence into scored opportunities, and opportunities into a
recommended next step.

It is run by `agents/analysis-director.md`, which routes work and (in Phase 2)
dispatches specialist analysts.

## Workflows

Phase 1 (live):

- Research Brief — `workflows/research-brief.md`

Phase 2 (tracked in `EXECUTIVE-BACKLOG.md`, built on first real use):

- Market Research
- Competitor Research
- Reddit / GitHub Scan
- Ideation Sprint
- Feature Opportunity Review
- Business Case Review
- Risk Review (reuses `PROMPTS/risk-review.md`)

## Required Output Structure

Every Analysis OS output must separate, in this order:

1. **Facts** — verifiable, with a source.
2. **Sources** — where each fact came from; label source type and reliability.
3. **Assumptions** — what we are taking as true without proof.
4. **Insights** — what the facts mean.
5. **Opportunities** — concrete things we could do.
6. **Risks** — what could go wrong.
7. **Recommendations** — what to do, ranked.
8. **Open questions** — what we still do not know.
9. **Decision needed** — the single decision this analysis is asking for, if any.

Every output ends with an explicit **confidence level** and a **recommended next
step**. If a claim has no source, label it an assumption, not a fact.

## Templates

- `templates/research-brief-template.md`
- `templates/evidence-table-template.md`
- `templates/opportunity-card-template.md`

## Rules

- Cite or label source quality for every research claim. Web search / fetch tools
  are used when available; if not available, say so and mark claims as unverified.
- Do not present opinions as facts.
- Opportunities must be scored before they are recommended (impact, confidence,
  effort, revenue potential, strategic fit, risk).
- If an analysis surfaces a strategy/product decision, record it in
  `EXECUTIVE-DECISIONS.md`. If it surfaces a reusable lesson, record it in
  `EXECUTIVE-LESSONS.md`.
