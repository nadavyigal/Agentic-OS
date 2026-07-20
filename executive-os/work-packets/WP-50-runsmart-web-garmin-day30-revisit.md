# Work Packet

- Status: Ready (time-gated — do not start before ~2026-08-01)
- Mode: Maintainer
- Source: tasks/progress.md 2026-07-03 entry; 2026-07-02 priority-reset decision
- Workflow pattern: normal
- Input trust: trusted
- Success signal: a written go/no-go on the Garmin track, with the stale premise corrected
- Model route: Claude Opus

## Owner Role
Founder + engineer (decision packet, not a build packet)

## Project
RunSmart Web — `/Users/nadavyigal/Documents/RunSmart`

## Goal
Run the day-30 revisit of the paused Garmin track and produce an explicit go/no-go.

## Context
Garmin relaunch is paused **by decision**, not blocked (2026-07-02 priority reset, Resumely primary). This packet exists so the pause gets revisited on purpose instead of decaying into permanent drift.

One fact must be corrected at the revisit: the maintenance-mode decision rested on "keep the 5 currently-synced users working," but a 2026-07-03 Supabase check found **all 9 `garmin_connections` rows are `reauth_required`, 0 `connected`** (newest successful sync 2026-07-01 03:40:58). There are zero users syncing, not five. The premise behind the pause is stale in a way that makes the pause *easier* to justify, not harder — but it should be stated, not quietly carried.

There is no maintenance-mode-compatible fix: restoring sync needs either commercial credentials (WP-26 Steps 3-4) or pointing real users at the Evaluation-tier Internal Test app, which is the same Terms violation that got the original app deactivated.

## Read First
- AGENTS.md, CLAUDE.md
- tasks/progress.md (Current Phase, Next Recommended Story, Risks)
- Nadav Builder OS `05-Decisions/2026-07-02-priority-reset-resumely-primary.md`
- Agentic OS DECISIONS.md, and WP-26 / WP-27 / WP-28

## Task
1. Re-verify the `garmin_connections` state (read-only) — confirm whether it is still 0 connected.
2. Decide: resume the commercial-app track, keep paused for another 30 days, or formally kill it and tell the 9 affected users.
3. Log the decision in Agentic OS `DECISIONS.md` and update `tasks/progress.md`.

## Constraints
- Read-only against production. No migrations, no deploys, no credential changes.
- Do not resume WP-26 build work as part of this packet — the output is a decision, not code.
- Separate known issue, do not fix here: ~26 applied production migrations have no matching file in `v0/supabase/migrations/`.

## Validation
Supabase aggregate query output pasted with its date. Decision written to DECISIONS.md.

## Completion Gate
Update tasks/progress.md and Agentic OS DECISIONS.md.

## Final Output
What changed, files changed, commands run, validation evidence, remaining risks, next recommended action.
