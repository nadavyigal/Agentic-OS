# Work Packet WP-54 — Measurement integrity guardrails

- Status: Open
- Mode: Builder
- Source: COO Operating Review 2026-07-21; Builder OS `2026-07-21-weekly-review`; PostHog AI audits of projects 171597 + 270848 (2026-07-21)
- Workflow pattern: normal
- Input trust: trusted
- Loop: Activation measurement integrity loop (**register this loop as part of this packet — it does not exist yet**)
- Signal: Seven recorded instances of the same failure class, plus two non-monotonic funnels, across two projects and three consecutive reviews.
- Memory update: `~/.claude/LEARNINGS.md` + Agentic OS `LESSONS.md`
- Success signal: A dashboard series or plan doc referencing a non-existent event/property fails loudly at refresh time instead of rendering as zero; a non-monotonic funnel raises a drift warning
- Model route: Sonnet 5
- Rollback: Guardrails are additive checks in the refresh path. Revert the commit; nothing downstream depends on them.

## Owner Role
Agentic OS maintainer

## Project
Agentic OS — `/Users/nadavyigal/Documents/Projects /Agentic OS`

## The Failure Class, With Every Recorded Instance

Each of these produced a number that looked like data and was actually a naming or emission defect. Three were found on 2026-07-21 alone, and **instance 5 was committed by the PostHog audit itself while auditing for exactly this kind of problem** — which is the strongest possible argument that humans and models both need a mechanical check rather than discipline.

| # | Property / event | Project | What it produced |
|---|---|---|---|
| 1 | `marketing_version` | RunSmart 171597 | Not in taxonomy; referenced by plan docs. Every row null, read as "no data" |
| 2 | `resume_uploaded` | Resumely 270848 | Call site removed by WP-46 Story 10 in 1.4.3; every dashboard series built on it silently zeroed |
| 3 | `resume_upload_succeeded` | Resumely 270848 | Sits behind the sign-in guard, structurally cannot exceed `sign_in_completed`; used as a denominator anyway (WP-48 Defect B) |
| 4 | `optimized_preview_rendered` | Resumely 270848 | Under-fires; produces a non-monotonic funnel (WP-51) |
| 5 | `sign_in_failed.error` / `.provider` | RunSmart 171597 | **Queried by the 2026-07-21 PostHog audit. Neither property exists.** Real properties are `error_code` (=1000), `error_domain`, `screen`, all populated. The audit concluded "you cannot diagnose this" and made it a top-5 weekly priority — a non-bug that would have consumed WP-52's timebox |
| 6 | `save_failed` / `optimization_apply_failed` / `optimization_state_recovery_failed` | Resumely 270848 | Fire with zero diagnostic properties: 0/21, 0/12, 0/24 rows populated (verified 2026-07-21) |
| 7 | Duplicate event pairs | Both | `Application Opened`/`app_launched`; `plan_generated`/`plan_generation_succeeded`; `expert_run_started`/`expert_mode_run_started`; `job_added`/`job_description_added`. Any aggregate over either name is wrong by an unknown amount |

**Non-monotonic funnels found so far** — a later step exceeding an earlier one, which is logically impossible and always indicates a defect:
- Resumely: 3 `export_success` persons vs 1 `optimized_preview_rendered` person (you cannot export what you never saw)
- RunSmart: 4 `first_run_completed` persons vs 3 `run_started` persons

## Build

**a. Event/property existence pre-flight.** Any event or property named in a dashboard series, a manual-layer block, or a plan doc must be verified to exist in the target project's taxonomy. Fail loudly at refresh time. A missing name must never render as zero.

**b. Funnel monotonicity assertion.** Any ordered funnel the dashboard renders gets checked: if step N+1 exceeds step N, raise a drift warning naming both steps. This is cheap and would have caught instances 4 and the RunSmart run/complete inversion automatically.

**c. Event-retirement rule.** Retiring or renaming an event requires updating every series built on it. Add a check that flags dashboard series whose source event has had no volume in 30 days, so a silently-zeroed series announces itself.

**d. Duplicate-name detector.** Flag event pairs that differ only by a known synonym pattern (`X` vs `X_mode`, `X` vs `X_succeeded`, Title Case vs snake_case of the same words) and both carry volume.

**e. Register the outcome loop.** Create `executive-os/loops/activation-measurement-integrity.md`. This has been the binding constraint in three consecutive COO reviews and is still being handled as one-off packets, which is the signature of a missing loop.

## Also Worth Doing, Cheaply — PostHog event definitions

Both projects have **zero** event definitions (descriptions, verified status) across 57 custom events in RunSmart and ~35 in Resumely. That absence is the root enabler of this whole failure class: with no definitions, the only way to learn an event's real property names is to query it and guess.

Define at minimum the events that appear in any funnel or dashboard series. This is PostHog UI work, no code, and it is the highest-leverage low-effort item the audits surfaced.

## Out of Scope

- Fixing the underlying emission defects — those belong to WP-51 (Resumely) and their own packets.
- Consolidating the duplicate event pairs. Detect them here; deciding which name is canonical is a product-repo decision.
