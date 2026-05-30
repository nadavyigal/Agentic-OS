# Executive Backlog

Deferred Executive OS work. Build each item only when a real run needs it, so the
layer stays lightweight. Phase 1 (the spine) is already live.

## Phase 2 — Expand on use

### Agents (`executive-os/agents/`)
- research-analyst — finds, evaluates, synthesizes sources.
- opportunity-analyst — turns research into scored opportunities.
- product-strategist — connects user problems, direction, roadmap.
- consultant-agent — structured consultancy-style recommendations.
- monetization-agent — pricing, packaging, revenue experiments.
- pricing-agent — price points, plans, trials, value metric.
- unit-economics-agent — CAC, LTV, margin, AI cost per action, payback.
- risk-review-agent — root causes, mitigations, monitoring signals (reuse
  `PROMPTS/risk-review.md`).

### Workflows (`executive-os/workflows/`)
- market-research
- competitor-research
- reddit-github-scan
- ideation-sprint
- feature-opportunity-review
- business-case-review
- pricing-packaging-review
- monetization-experiment
- quarterly-okr-review
- executive-decision-review
- portfolio-prioritization
- risk-review

### Templates (`executive-os/templates/`)
- source-quality-template
- feature-business-case-template
- pricing-experiment-template
- monetization-scorecard-template
- ceo-weekly-review-template
- risk-register-template

### Prompts (`PROMPTS/`)
- monetization-review
- pricing-packaging-review
- ceo-decision-review
- opportunity-ranking
- executive-decision-review

## Phase 3 — Visualize / automate

- Add an `executiveLayer` block to `dashboard/status.json` and render Layer 8 cards
  in `dashboard/index.html` (CEO OS / CFO OS / Analysis OS / Decision Board /
  Executive Metrics). Touch the generated visual map only after Phase 1 content is
  stable.
- Real data hooks (App Store Connect / RevenueCat / PostHog / provider billing) only
  if and when actually implemented. No claimed sync until real.

## Open Executive Work

(add items surfaced by Weekly CEO Reviews here)
