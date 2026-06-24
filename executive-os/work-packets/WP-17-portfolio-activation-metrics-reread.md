# Work Packet WP-17 - Portfolio Activation Metrics Reread

- Status: Open
- Created: 2026-06-24
- Source: EXD-013; `executive-os/reviews/2026-06-24-portfolio-exec-ceo-plan.md`
- Workflow pattern: metric-diagnostic
- Input trust: trusted prior readout; new readout must exclude founder and QA/bot bursts
- Outcome loop: Portfolio activation and OKR 2
- Related decision: EXD-013
- Success signal: `EXECUTIVE-METRICS.md`, `CEO-OS.md`, and the saved readout reflect the first true organic RunSmart D7 reread and the cleaned Resumely D7 number

## Owner Role

Analysis OS + CEO OS

## Project

Agentic OS, with PostHog/App Store evidence from RunSmart and Resumely

Path: `/Users/nadavyigal/Documents/Projects /Agentic OS`

## Goal

Run the next portfolio activation reread after the first true RunSmart organic cohort becomes available, update the executive metrics, and decide whether OKR 2 targets still hold.

## Timing

Run on or after 2026-06-26 for RunSmart installs from 2026-06-19+.

## Read First

- `PROMPTS/portfolio-exec-ceo-plan.md`
- `executive-os/reviews/2026-06-24-portfolio-exec-ceo-plan.md`
- `executive-os/EXECUTIVE-METRICS.md`
- `executive-os/CEO-OS.md`
- `executive-os/EXECUTIVE-DECISIONS.md` EXD-013
- Latest product status in `PROJECT-STATUS.md`
- Any completed outputs from WP-15 and WP-16

## Task

1. Pull RunSmart D7 activation for the first live App Store cohort: installs or first_seen on/after 2026-06-19, through run_completed within 7 days.
2. Exclude the founder's person, QA traffic, bot bursts, simulator/test users, and known internal devices before quoting the number.
3. Pull supporting RunSmart funnel stages: onboarding_completed, plan_generated, run_started, run_completed.
4. Pull the cleaned Resumely D7 activation number from WP-16 or rerun the query if WP-16 is not complete.
5. Update:
   - `executive-os/EXECUTIVE-METRICS.md`
   - `executive-os/CEO-OS.md` OKR 2 baselines, only if numbers changed
   - a new saved readout at `executive-os/reviews/YYYY-MM-DD-activation-reread.md`
6. Decide whether OKR 2 targets stay directional or need revision. If this is a major target change, add an EXD row.

## Constraints

- Do not invent metrics. Unknown numbers must be `unknown - need: <source>`.
- Do not compare beta/test cohorts directly to true organic cohorts without caveats.
- Do not unlock monetization or paid acquisition from a tiny sample unless the executive decision is explicit.
- No product repo code changes.

## Validation

- Every metric includes source, date, cohort definition, exclusion method, numerator, and denominator.
- `git diff --check` passes.
- `./agentic-os verify` passes.
- If `./agentic-os morning` is run, report any contradictions rather than hiding them.

## Completion Gate

Report:

- RunSmart D7 activation reread.
- Resumely cleaned D7 activation number.
- OKR 2 hold/revise recommendation.
- Files changed.
- Checks run.
- What was NOT done.

