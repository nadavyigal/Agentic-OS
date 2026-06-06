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

Plus a thin operations layer (not a sub-OS): **COO OS** (`COO-OS.md`): execution sequencing, bottlenecks, work packets, QA order, and escalation routing; run via `PROMPTS/coo-operating-review.md`.

The current portfolio plan is `BUSINESS-GTM-PLAN-V0.md` (Business + GTM Plan v0 for RunSmart iOS and Resumely iOS); its open CEO decisions are logged in `EXECUTIVE-DECISIONS.md` and its work packets are tracked in `work-packets/`.

## Daily vs executive depth

- **Every work day:** `../DAILY.md` (Tier 0 morning loop). Executive files below are **not** deleted; open them when Tier 2 or weekly rhythm says so.
- **This folder** remains the full Layer 8 library (CEO, COO, CFO, Analysis, research, decisions, work packets).

## Read Order

1. `EXECUTIVE-RHYTHM.md` — the operating cadence; start here for weekly/monthly work.
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
| Context Extraction | `workflows/context-extraction.md`, `templates/context-checkpoint-template.md`, `../brainstorms/` |

## Folder Map

- `agents/` — single-responsibility executive agent role definitions.
- `workflows/` — step-by-step executive workflows.
- `templates/` — blank templates for research, decisions, OKRs, finance.
- `../brainstorms/` — durable founder-interview checkpoints before promotion.
- `context/` — historical founder-interview checkpoints retained for reference.
- `loops/` — lightweight outcome loops that connect strategy to evidence.
- Root docs — the three sub-OS, dashboard, decisions, metrics, rhythm, lessons,
  backlog.

## Copy-Ready Prompts

Run these from `PROMPTS/` (root of the Agentic OS):

- `PROMPTS/executive-weekly-review.md` — run the Weekly CEO Review.
- `PROMPTS/cfo-monthly-review.md` — run the Monthly Finance Review.
- `PROMPTS/analysis-research-sprint.md` — run a research brief → evidence →
  opportunities.
- `PROMPTS/context-extraction.md` — run a one-question-at-a-time founder
  interview and save a durable checkpoint.

## What This Is Not

- Not an automation platform. No App Store / RevenueCat / PostHog / GitHub sync
  exists unless explicitly implemented.
- Not a replacement for the product, distribution, or QA layers.
- Not a place for invented financial numbers.

## Status

Phase 1 (this spine) is live. Phase 2 (remaining agents, workflows, templates,
prompts) and Phase 3 (visual dashboard cards) are tracked in `EXECUTIVE-BACKLOG.md`
and built only on real use.
