# Weekly Plan Creation Workflow

## Purpose

Run one weekly session that does both: review last week and plan this week. A single document replaces the separate review + plan split. Part 1 looks back, Part 2 looks forward.

## When To Run It

- Sunday evening or Monday morning.
- After the latest `executive-os/EXECUTIVE-DASHBOARD.md` and `Current Priorities` are current.
- Takes 20–30 minutes end to end.

## Inputs

1. Last week's plan note `07-Weekly-Reviews/YYYY-MM-DD-weekly-plan.md` — completed vs missed tasks.
2. `executive-os/EXECUTIVE-DASHBOARD.md` — top 3, open decisions, plan progress.
3. `executive-os/WEEKLY-CEO-LATEST.md` — stop-doing list, recommended actions.
4. `executive-os/COO-LATEST-REVIEW.md` — execution sequence, current bottleneck.
5. `PROJECT-STATUS.md` or `dashboard/status.json` — active project status.
6. `Current Priorities` — this week's live index.

## Steps

**Part 1 — Review last week (10 min)**

1. Open last week's plan note. Mark which tasks were completed and which were missed.
2. Fill Completed Work: what shipped, closed, or moved to done.
3. Fill Missed Tasks: what did not get done and why.
4. Fill Active Projects Status from `PROJECT-STATUS.md`. Do not write from memory.
5. Fill Recurring Problems. If a problem appeared two weeks in a row, it belongs in Decision Backlog this week.
6. Fill Ideas Worth Saving.

**Part 2 — Plan this week (10–15 min)**

7. Write the headline: one sentence that says what this week resolves or advances.
8. Set the time budget: real available days, focus blocks, external gates.
9. Choose 2–3 priorities. Each needs a specific reason it belongs this week. Tag each as blocker, milestone, or maintenance.
10. List decisions that must be made this week in Decision Backlog.
11. Write the explicit parking lot.
12. Write 2–3 verifiable success criteria.
13. Save as `07-Weekly-Reviews/YYYY-MM-DD-weekly-plan.md` in the Obsidian vault.
14. Update `Current Priorities` to reflect this week's top items.

## Output File Location

`exports/obsidian/weekly-plans/YYYY-MM-DD-weekly-plan.md` → copy to vault `07-Weekly-Reviews/`

## Quality Checklist

- [ ] Completed and missed tasks pulled from last week's plan, not memory.
- [ ] Active project status sourced from `PROJECT-STATUS.md`, not memory.
- [ ] Every priority has a specific reason it belongs this week.
- [ ] Recurring problems that reappeared are in Decision Backlog.
- [ ] Parking lot is explicit.
- [ ] Success criteria are verifiable by end of week.
