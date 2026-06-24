# Work Packet WP-16 - Resumely Activation Attribution + Funnel Diagnostic

- Status: Completed 2026-06-24
- Created: 2026-06-24
- Source: EXD-013; `executive-os/reviews/2026-06-24-portfolio-exec-ceo-plan.md`
- Workflow pattern: metric-diagnostic
- Input trust: trusted D7 readout from `PROMPTS/portfolio-exec-ceo-plan.md`, `CEO-OS.md`, and `EXECUTIVE-METRICS.md`
- Outcome loop: Resumely D7 activation / Gate A
- Related decision: EXD-013
- Success signal: Resumely real-organic D7 activation is either confirmed at 0/35 or corrected with person `067544b5` classified, and the main funnel drop-off is named with a next action

## Completion Summary - 2026-06-24

Result: **0 confirmed real-organic D7 activation**.

PostHog project 270848 classified person `067544b5-dbb4-589f-988b-a146f794f184` as Automation / bot-like traffic across its backend completion and later iOS sign-in events, so the unresolved raw completer is excluded from organic activation.

Current diagnostic evidence:

- Prior executive readout: 3/35 raw completers, now all excluded from real-organic activation.
- Current all-product live re-query, 2026-06-10 through 2026-06-24: 37 first-seen product users, 12 resume uploaders, 10 job-added users, 4 optimization starters, 4 raw completers, 0 confirmed organic completers.
- Saved iOS funnel `VH410GF1`, 2026-06-10 through 2026-06-24: 30 `app_launched` -> 26 `guest_mode_started` -> 5 `resume_uploaded` -> 4 `job_added` -> 1 `optimization_completed` -> 1 `export_success`.

Largest measurable drop-off: guest/app-open to resume upload. Recommended next packet: upload/import friction and preflight/error instrumentation, before monetization, paid acquisition, score-copy nudges, or more GTM volume.

Outputs:

- Resumely iOS report: `docs/qa/reports/wp-16-activation-attribution-funnel-2026-06-24.md`
- Resumely iOS updates: `tasks/progress.md`, `tasks/session-log.md`
- Agentic OS metric update: `executive-os/EXECUTIVE-METRICS.md`

## Owner Role

Analysis OS + Resumely iOS/Web product operator

## Project

Resumely iOS and ResumeBuilder Web

Paths:

- `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`
- `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`
- `/Users/nadavyigal/Documents/Projects /Agentic OS`

## Goal

Confirm whether Resumely has any real organic D7 activation, classify person `067544b5`, and diagnose the first-seen -> optimization_completed funnel before new feature, paywall, or GTM work continues.

## Context

The 2026-06-24 D7 readout says 3/35 raw completers, but all three are founder-attributed in the prompt state. One US-web case, person `067544b5` from 2026-06-10, is unconfirmed. If that person is real, real organic activation may be 1/35. If not, it is effectively 0/35.

## Read First

- Agentic OS `executive-os/reviews/2026-06-24-portfolio-exec-ceo-plan.md`
- Agentic OS `executive-os/EXECUTIVE-METRICS.md`
- Agentic OS `executive-os/EXECUTIVE-DECISIONS.md` EXD-013
- Resumely iOS `AGENTS.md` / `CLAUDE.md`
- Resumely iOS `tasks/progress.md`, `tasks/session-log.md`, `tasks/MEMORY.md`, `tasks/ERRORS.md`
- ResumeBuilder Web `tasks/progress.md`, `tasks/MEMORY.md`, `tasks/ERRORS.md`, if present

## Task

1. Classify person `067544b5` using available PostHog, device, geo, email, QA, or founder-test evidence. If you cannot access PostHog, mark this HUMAN and produce the exact query/check the founder should run.
2. Recompute the D7 activation numerator and denominator with founder, QA, and bot bursts excluded.
3. Map the funnel stages:
   - first_seen / install / app_opened
   - resume upload or import started
   - resume parsed
   - job pasted or selected
   - optimization started
   - optimization completed
   - export or copy result
4. Identify the largest drop-off that is measurable today.
5. Decide whether Fit-First, score copy, metric nudge, or upload/import friction is the highest-leverage next fix. Do not build it yet unless the fix is tiny and clearly safe.
6. Update Agentic OS `EXECUTIVE-METRICS.md` only if the attribution number changes. Update Resumely product `tasks/progress.md` / `tasks/session-log.md` with the finding.

## Constraints

- No paywall, pricing, RevenueCat, StoreKit, or paid acquisition work.
- No App Store submission or metadata change without explicit founder approval.
- Do not claim an activation number unless founder and QA traffic are excluded.
- Do not change scoring logic in this packet.

## Validation

- Attribution classification for `067544b5` is documented, or marked HUMAN with exact requested evidence.
- Funnel stage table exists with numerator, denominator, and unknowns.
- If metrics are updated, cite source and date.
- `git diff --check` passes in touched repos.

## Completion Gate

Report:

- Final real-organic D7 activation number and caveats.
- Classification of `067544b5`.
- Largest measurable drop-off.
- Recommended next packet.
- Files changed and checks run.
- What was NOT done.
