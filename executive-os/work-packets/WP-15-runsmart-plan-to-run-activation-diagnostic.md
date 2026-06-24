# Work Packet WP-15 - RunSmart Plan-to-Run Activation Diagnostic

- Status: Open
- Created: 2026-06-24
- Source: EXD-013; `executive-os/reviews/2026-06-24-portfolio-exec-ceo-plan.md`
- Workflow pattern: feature-diagnostic
- Input trust: trusted D7 readout from `PROMPTS/portfolio-exec-ceo-plan.md`, `CEO-OS.md`, and `EXECUTIVE-METRICS.md`
- Outcome loop: RunSmart D7 activation
- Related decision: EXD-013
- Success signal: the plan_generated -> run_completed drop-off has a named root cause, an instrumented fix plan, and either one shipped intervention or a clear plan-feature ready to execute

## Owner Role

RunSmart iOS product engineer + product analyst

## Project

RunSmart iOS

Path: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

## Goal

Explain why 0/10 real users completed a run within 7 days even though 30% reached `plan_generated`, then prepare the smallest activation intervention that can move plan-to-run conversion above zero.

## Context

The 2026-06-24 D7 readout is caveated because the RunSmart cohort predates the first live App Store build, but it still exposes a specific product problem: onboarding and plan generation happen, then no one records a run. Do not assume this is just sample noise until the path is inspected.

## Read First

- RunSmart iOS `AGENTS.md` / `CLAUDE.md`
- RunSmart iOS `tasks/progress.md`, `tasks/session-log.md`, `tasks/MEMORY.md`, `tasks/ERRORS.md`
- Agentic OS `executive-os/reviews/2026-06-24-portfolio-exec-ceo-plan.md`
- Agentic OS `executive-os/EXECUTIVE-METRICS.md`
- Agentic OS `executive-os/EXECUTIVE-DECISIONS.md` EXD-013
- Relevant RunSmart iOS analytics definitions for onboarding, plan generation, run start, and run completion

## Task

1. Audit the actual funnel instrumentation: install/first launch, onboarding start/completion, `plan_generated`, first-run CTA, run start, run completion, permission failures, and reminder events.
2. Confirm whether `run_started` / `run_completed` can fire reliably on the current live code path. If event names differ, map them explicitly.
3. Inspect the UI path immediately after plan generation. Identify whether the user is given a concrete next run, a primary CTA, and a reminder path.
4. Check for blockers that can explain zero completion: Health/GPS permissions, empty Today state, plan not assigned, Garmin-only path confusion, simulator-only assumptions, or analytics event mismatch.
5. Produce one of:
   - A tiny implementation fix in the RunSmart iOS repo, if the cause is obvious and low risk.
   - A ready `plan-feature` prompt in RunSmart iOS `docs/superpowers/plans/` if the fix needs design or broader review.
6. Update RunSmart iOS `tasks/progress.md`, `tasks/session-log.md`, and `tasks/MEMORY.md` with the diagnostic result.

## Constraints

- Do not start broad UX redesign.
- Do not add dependencies.
- Do not change training science or Garmin integration scope.
- Keep the intervention focused on first-run activation after plan generation.
- If a fix touches more than 3 unexpected files, stop and report scope expansion.

## Validation

- Build/checks required by RunSmart iOS local instructions.
- Analytics event map documented.
- If code changes: simulator or device smoke of plan-generated -> first-run CTA path.
- If no code changes: plan-feature file is concrete enough for a coding agent to execute.

## Completion Gate

Report:

- Root cause hypothesis, with file/event evidence.
- Files changed.
- Build/check results.
- The exact next metric to watch: plan_generated -> run_started and run_completed, threshold >=20% plan-to-run conversion in the next usable cohort.
- What was NOT done.

