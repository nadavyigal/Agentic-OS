# Executive Intelligence OS (Layer 8)

The executive layer that sits on top of the Global Agentic OS. It does not replace
anything. It answers founder-level questions the product and distribution layers do
not:

- What should I research, and what opportunities are worth pursuing?
- What features should be built next?
- What should I monetize, and what is the financial picture?
- What should I stop doing?
- What should I decide this week?
- What should the agents work on next?

This is a thin operating rhythm, not an automation platform. Manual dashboards
first. No invented data. Every unknown number is written as `unknown — need:
<source>`.

## The Three Sub-OS

- **Analysis OS** (`ANALYSIS-OS.md`) — research, ideation, competitor/market scans,
  GitHub/Reddit scans, opportunity discovery, consultancy-style recommendations.
- **CFO / Monetization OS** (`CFO-OS.md`) — budgets, revenue, pricing, unit
  economics, cost control, runway, financial reporting.
- **CEO OS** (`CEO-OS.md`) — strategy, OKRs, weekly priorities, decisions, operating
  cadence, portfolio tradeoffs.

## Read Order

1. `EXECUTIVE-RHYTHM.md` — the operating cadence; start here.
2. The sub-OS doc relevant to today's work: `CEO-OS.md`, `CFO-OS.md`, or
   `ANALYSIS-OS.md`.
3. `EXECUTIVE-DASHBOARD.md` — the manual source-of-truth dashboard.
4. The workflow for the task in `workflows/`.
5. `EXECUTIVE-DECISIONS.md` before recording any strategy/pricing/product/budget
   decision.

## Reuse Map (do not duplicate these — consume them)

| Executive workflow | Consumes (existing files) |
|---|---|
| Weekly CEO Review | `../DASHBOARD.md`, `../PROJECT-STATUS.md`, `PROMPTS/morning-brief.md` output, `PROMPTS/exec-review.md` output, `../distribution-os/weekly-growth-review.md`, `EXECUTIVE-DASHBOARD.md`, `EXECUTIVE-DECISIONS.md`, `EXECUTIVE-METRICS.md` |
| Monthly Finance Review | `../distribution-os/metrics-dashboard.md`, `../distribution-os/data/source-of-truth-policy.md`, `EXECUTIVE-METRICS.md` |
| Research Brief | `templates/evidence-table-template.md`, `templates/opportunity-card-template.md`, web/search tools when available |

## Folder Map

- `agents/` — single-responsibility executive agent role definitions.
- `workflows/` — step-by-step executive workflows.
- `templates/` — blank templates for research, decisions, OKRs, finance.
- Root docs — the three sub-OS, dashboard, decisions, metrics, rhythm, lessons,
  backlog.

## Copy-Ready Prompts

Run these from `PROMPTS/` (root of the Agentic OS):

- `PROMPTS/executive-weekly-review.md` — run the Weekly CEO Review.
- `PROMPTS/cfo-monthly-review.md` — run the Monthly Finance Review.
- `PROMPTS/analysis-research-sprint.md` — run a research brief → evidence →
  opportunities.

## What This Is Not

- Not an automation platform. No App Store / RevenueCat / PostHog / GitHub sync
  exists unless explicitly implemented.
- Not a replacement for the product, distribution, or QA layers.
- Not a place for invented financial numbers.

## Status

Phase 1 (this spine) is live. Phase 2 (remaining agents, workflows, templates,
prompts) and Phase 3 (visual dashboard cards) are tracked in `EXECUTIVE-BACKLOG.md`
and built only on real use.
