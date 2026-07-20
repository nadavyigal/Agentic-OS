# Work Packet

- Status: Ready
- Mode: Grower
- Source: docs/plans/2026-07-19-activation-cliff-fix-plan.md (S1); 2026-07-20 morning brief
- Workflow pattern: normal
- Input trust: trusted
- Success signal: sign_in_wall_viewed fires for organic users, and the viewed→tapped→completed drop is finally attributable
- Model route: Claude Opus (device + analytics reasoning)

## Owner Role
iOS engineer

## Project
RunSmart iOS — `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

## Goal
Make the sign-in wall measurable, then determine whether the ASAuthorizationError 1000 failures are a configuration outage or a persuasion problem.

## Context
1.1.0 (24) went live 2026-07-19T21:48:08Z and shipped **none** of the wall fixes. The 1.0.9 read found 22/23 organic users producing zero events after app open, 5 non-cancel ASAuthorizationError 1000 failures, and 0 sign_in_completed. Adaptive Coach shipped flag-ON *behind* that wall, so its Phase 2 gate (>=20 real `adaptive_coach_shown`) cannot fill while the wall stands. Every new download today hits this.

Per `~/.claude/ERRORS.md` 2026-07-19: exclusion rules protect against inflated numbers, not deleted signal. Any excluded person carrying an ERROR event must be individually re-examined, not swept.

## Read First
- AGENTS.md, CLAUDE.md
- docs/plans/2026-07-19-activation-cliff-fix-plan.md
- tasks/progress.md (top entry: 1.1.0 LIVE)
- tasks/lessons.md
- `RunSmartLiteAppShell.swift:184`

## Task
1. Instrument the wall: `sign_in_wall_viewed`, `sign_in_wall_tapped`, `sign_in_wall_abandoned`, with screen names. Fix the known double-fire.
2. Reproduce ASAuthorizationError 1000 on a **physical device against the live App Store build** (not a simulator, not a local build) to separate config failure from user drop-off.
3. Ship as 1.1.1.

## Constraints
- Do not touch unrelated files. Do not bundle Adaptive Coach Phase 2 work.
- No new SPM dependencies without asking.
- Do not deploy edge functions or submit to ASC without explicit approval in the current message.

## Validation
Full iOS suite via `xcodebuild test` on iPhone 17 / iOS 26.5 with `-derivedDataPath` under `/private/tmp` (see tasks/lessons.md — iCloud xattrs break CodeSign otherwise). Report the real pass count from the xcresult bundle, not pipe output.

## Completion Gate
Update tasks/todo.md, tasks/progress.md, tasks/session-log.md.

## Final Output
What changed, files changed, commands run, validation evidence, remaining risks, next recommended action.
