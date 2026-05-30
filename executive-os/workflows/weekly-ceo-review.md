# Workflow: Weekly CEO Review

The keystone executive workflow. Synthesizes existing status into a focused weekly
plan. It reuses other reviews; it does not re-collect status.

## Purpose

Set the top 3 priorities, make pending decisions, decide what to stop, decide what to
delegate, and update the executive dashboard.

## When To Use

Weekly. Run via `PROMPTS/executive-weekly-review.md`.

## Inputs (reuse — do not duplicate)

1. `../DASHBOARD.md` and `../PROJECT-STATUS.md` — portfolio status.
2. `PROMPTS/morning-brief.md` output — cross-project execution status.
3. `PROMPTS/exec-review.md` outputs in `PROJECT-BRIDGES/exec-reviews/` — strategic per-project view.
4. `../distribution-os/weekly-growth-review.md` — distribution status.
5. `EXECUTIVE-DASHBOARD.md`, `EXECUTIVE-DECISIONS.md`, `EXECUTIVE-METRICS.md`.
6. CFO snapshot from the latest Monthly Finance Review, if current.

## Steps

1. Read the inputs above. Do not re-derive status that already exists.
2. Identify the 3 priorities that most move the portfolio this week.
3. For every open decision in `EXECUTIVE-DECISIONS.md`, make or restate a
   recommendation.
4. Produce the stop-doing list and the delegation list (priority → agent/workflow).
5. List top risks (from the Risk Board + any new ones).
6. Write the weekly executive summary.
7. Update `EXECUTIVE-DASHBOARD.md` (Top 3, Decision Board, Risk Board, Weekly Review,
   Next Actions). Append any new decisions to `EXECUTIVE-DECISIONS.md` with IDs and
   review dates.

## Output Format

```
## Weekly Executive Summary — YYYY-MM-DD
- Top 3 priorities
- Key decisions (with recommendation each)
- Stop-doing list
- Delegation list
- Top risks
- Recommended next actions
- Dashboard updates applied
```

## Evidence Requirements

- Cite the source review/file for each claim.
- Mark unknown metrics `unknown — need: <source>`. No fabrication.

## Completion Checklist

- [ ] Top 3 set; each open decision has a recommendation.
- [ ] Stop-doing + delegation lists produced.
- [ ] Dashboard updated; new decisions logged with review dates.

## Updates

- Dashboard: `EXECUTIVE-DASHBOARD.md`.
- Decisions: `EXECUTIVE-DECISIONS.md`.
- Lessons: add to `EXECUTIVE-LESSONS.md` only if a reusable executive lesson emerged.
