# Workflow: Research Brief

The core Analysis OS workflow. Turns a question into evidence, then into scored
opportunities and a recommended next step. Run by the Analysis Director.

## Purpose

Structured research with separated facts, sources, assumptions, insights,
opportunities, risks, and recommendations — ending in confidence + next step.

## When To Use

Whenever a decision needs evidence, or an idea needs to become a scored opportunity.
Run via `PROMPTS/analysis-research-sprint.md`.

## Inputs

- The research question.
- Web search / fetch tools if available (else note unavailability).
- Product context from `PROJECT-BRIDGES/` or local repos.
- `templates/research-brief-template.md`, `templates/evidence-table-template.md`,
  `templates/opportunity-card-template.md`.

## Steps

1. State the research question and why it matters now.
2. Gather sources. Build an evidence table (Claim / Source / Type / Reliability /
   Date / Summary / Contradictions / Confidence / Implication).
3. Separate Facts / Sources / Assumptions / Insights.
4. Derive Opportunities; write an opportunity card for each material one.
5. Score opportunities (impact, confidence, effort, revenue potential, strategic fit,
   risk).
6. List Risks and Open questions.
7. State the Decision needed (if any), confidence level, and the single recommended
   next step.

## Output Format

Use `templates/research-brief-template.md` — the nine-section Analysis OS structure,
plus the evidence table and any opportunity cards.

## Evidence Requirements

- Every fact has a source with type and reliability.
- Unverified claims (no tools) are labeled as such.
- Opportunities scored before recommended.

## Completion Checklist

- [ ] Evidence table complete.
- [ ] Facts vs assumptions separated.
- [ ] Opportunities scored.
- [ ] Confidence + single next step stated.

## Updates

- Opportunities worth pursuing → `EXECUTIVE-DASHBOARD.md` Research/Opportunity Board.
- Decisions surfaced → `EXECUTIVE-DECISIONS.md`.
- Reusable lessons → `EXECUTIVE-LESSONS.md`.
