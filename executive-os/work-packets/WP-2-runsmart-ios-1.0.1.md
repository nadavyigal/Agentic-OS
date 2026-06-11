# Work Packet WP-2 (Recovered)

- Status: Superseded - recovered historical packet; current RunSmart 1.0.2 build 14 path is WP-4/WP-6.
- Created: 2026-06-03
- Source: Founder directive (work RunSmart iOS next version now), runs in parallel with WP-1
- Routed by: COO OS (COO Operating Review, 2026-06-03)
- Escalation: none current. Historical note: this originally overrode CEO-OS focus rule 2 and EXD-008 timing, but that path has been superseded by the build 14 resubmission line.
- Related decision: EXD-008 (RunSmart 1.0.1 scope)
- Cross-project dependency: RunSmart Web `/api/coach/voice-cue` TTS endpoint behind `VOICE_COACH_ENABLED` (PROJECT-STATUS.md, commit f677ad7, 2026-06-01)

---

# Work Packet

## Owner Role
iOS Engineer (local), with simulator visual QA

## Project
RunSmart iOS
Path: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

## Goal
Make small, reviewable progress on the 1.0.1 next version (voice cues + UX/UI redesign) on an isolated branch, without touching the v1.0 build that is in Apple review and without resubmitting.

## Context
RunSmart v1.0 build 6 is frozen in App Store review (PROJECT-STATUS.md). A "UX redesign spec for 1.0.1 fast follow" already exists in the iOS repo (commit 234d2d5, 2026-05-31), and RunSmart Web shipped a `/api/coach/voice-cue` TTS endpoint behind the `VOICE_COACH_ENABLED` flag (commit f677ad7). EXD-008 recommended scoping 1.0.1 only after the review outcome; the founder has chosen to start 1.0.1 implementation in parallel. This packet exists so that work proceeds safely and cannot affect the in-review v1.0.

## Read First
- AGENTS.md
- CLAUDE.md
- tasks/todo.md
- tasks/session-log.md (latest)
- tasks/MEMORY.md
- tasks/lessons.md
- The 1.0.1 UX redesign spec in `docs/specs/` (the artifact added in commit 234d2d5)
- `PROJECT-BRIDGES/runsmart-web.md` and the `/api/coach/voice-cue` endpoint contract (for the voice-cue integration)
- `PROJECT-BRIDGES/runsmart-ios.md` taste rule (calm coach, one clear next action, not a dashboard)

## Task
1. Create or check out an isolated 1.0.1 feature branch off the correct base. Do NOT branch from or commit to the frozen v1.0 release branch.
2. From the 1.0.1 UX redesign spec, break the work into small independently testable stories (voice-cue consumption of the existing web endpoint behind a client flag; UX/UI changes per the spec). List the stories.
3. Pick ONE story to implement first (recommend the smallest UX/UI story that needs no backend, so voice cues can wait on endpoint verification).
4. Implement that one story with native SwiftUI patterns, small and reviewable, with simulator visual QA.

## Constraints
- Do not touch unrelated files.
- Do NOT modify the v1.0 build under review: no changes to its release branch, version/build numbers, signing config, or any submitted App Store artifact.
- Do NOT archive-for-release, submit, or upload anything while v1.0 is in review.
- Voice cues must consume the existing `/api/coach/voice-cue` contract; do not invent a new backend, and do not assume background-audio or TTS entitlements without checking the repo.
- No new SPM dependencies without explicit approval.
- One story at a time; visual QA for every UI change.
- Do not invent validation results.

## Validation
- `xcodebuild build` succeeds on a simulator.
- Targeted tests pass for the touched code.
- Simulator screenshots for each UI change (before/after where relevant).
- Evidence that the work is on an isolated branch (git branch) and that no version/build/signing artifacts changed.

## Completion Gate
Before final response, update or report:
- tasks/todo.md
- tasks/session-log.md
- tasks/lessons.md only if a reusable lesson was learned
Record which story is done and which is next.

## Final Output
- What changed
- Files changed
- Commands run
- Validation evidence (build, tests, screenshots)
- Confirmation that v1.0 artifacts were untouched and nothing was submitted
- Remaining risks
- Next recommended story
