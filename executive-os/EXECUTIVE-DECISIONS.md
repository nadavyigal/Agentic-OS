# Executive Decisions

Durable log of important strategy, product, pricing, growth, technical, and release
decisions made at the executive level. Small decisions can be a single row. Big ones
should also have a memo via `templates/decision-memo-template.md` linked in the Notes.

Fields: ID · Date · Area · Decision · Options considered · Recommendation ·
Rationale · Evidence · Risks · Owner · Review date · Status.

Areas: Product · Finance · Growth · Strategy · Technical · Release.
Status: Open · Decided · Revisit · Superseded.

## Log

| ID | Date | Area | Decision | Options | Recommendation | Rationale | Evidence | Risks | Owner | Review | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXD-001 | 2026-05-30 | Strategy | Add Executive Intelligence OS as Layer 8, markdown-first, phased | Full build now / phased spine / minimal core | Phased spine | Matches lightweight constraint and owner principle of working software over process | Plan `harmonic-hatching-clover`; existing `distribution-os/` pattern | Spine could sit unused if rhythm not run | Nadav | 2026-06-30 | Decided |
| EXD-002 | 2026-05-30 | Growth | Wire minimal analytics before any new feature work | Build features now / instrument first / do both | Instrument first | Both apps are pre-launch with zero funnel visibility; every product decision is currently blind. Resumely PostHog is not integrated (AnalyticsService TODO) | orchestration map 2026-05-29 (CRO layer); EXECUTIVE-METRICS.md (all Needs Data) | Instrumentation can overrun; cap at ~2 days, descope to activation/export-success only | Nadav | 2026-06-13 | Open |
| EXD-003 | 2026-05-30 | Release | Refresh stale 2026-05-15 portfolio status before relying on it | Trust 2026-05-15 status / trust 2026-05-29 orchestration map / pull fresh local status | Pull fresh local status | DASHBOARD.md/PROJECT-STATUS.md (2026-05-15) lag the 2026-05-29 map and the submit-ready memory; decisions on stale status risk error | DASHBOARD.md; PROJECT-STATUS.md; orchestration map 2026-05-29 | Low cost: one status pull per repo | Nadav | 2026-06-06 | Open |

## How To Add A Decision

1. Add a row with the next ID.
2. If it is a major strategy/pricing/product/budget choice, also write a memo from
   `templates/decision-memo-template.md` and reference it.
3. Set a Review date so the decision is revisited, not forgotten.
4. If the decision changes how agents work, also update the relevant rule or
   workflow.
