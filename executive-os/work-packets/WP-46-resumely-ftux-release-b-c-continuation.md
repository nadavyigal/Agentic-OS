# Work Packet WP-46 - Resumely FTUX Release B+C Continuation

- Status: Ready after the active Claude Code session finishes and pushes Stories 7 and 8
- Mode: Grower
- Source: 2026-07-16 FTUX Evidence And Release Decisions Cleared; Resumely FTUX plan; Release A 1.4.2 production measurement report
- Workflow pattern: sequential multi-story delivery
- Input trust: trusted
- Outcome loop: resumely-launch-to-export-activation
- Signal: Release A is live but has 0 clean post-release entrants; Stories 7 and 8 are being built in another Claude Code session
- Memory update: `tasks/progress.md`, `tasks/session-log.md`, and the canonical FTUX plan
- Success signal: a clean-install user can complete the evidence-backed journey through export, with canonical PII-safe measurement, and the repository can reproduce the 1.5.0 release candidate

## Owner Role

Senior iOS product engineer working in the Resumely iOS repository.

## Project

Resumely iOS: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`

## Goal

Continue from the active Stories 7-8 work, implement Stories 9-13 sequentially, and prepare one combined 1.5.0 FTUX release candidate without interfering with the live 1.4.2 app or performing any App Store action.

## Start Gate

1. Read the repository instructions and actual git/worktree state.
2. Find the active Claude Code work for Stories 7 and 8. Do not reimplement, overwrite, cherry-pick blindly, or create a competing branch.
3. Continue only after Stories 7 and 8 are committed, pushed, reviewed as required, and integrated into the branch that will carry 1.5.0. If they are not integrated, report the exact branch/PR/commit state and stop.
4. Verify the Story 9 backend contract exists and is approved. It must name the backend owner, additive response schema, endpoint delivery plan, compatibility behavior, and safe no-evidence fallback. If any field is missing, document the proposed contract and stop for founder approval before Story 9 code.
5. Read the Release A production measurement report and preserve its uncertainty: 82 exact-version rows, 5 raw people, 4 excluded, 0 clean entrants, mature D7 0/0 undefined.

## Stories

| Story | Outcome | Required gate |
|---|---|---|
| 9 | Evidence-backed Accept/Skip recommendations | Use only the approved additive backend contract. Default factual changes off when evidence is absent. Never fabricate evidence or silently edit submitted content. |
| 10 | Canonical production measurement | Emit the agreed PII-safe activation/failure events, distinguish selection from successful upload, emit preview only when visible, and prevent duplicate completion correlations. |
| 11 | Localization and accessibility | Cover every touched FTUX screen, including Dynamic Type, VoiceOver labels/order, contrast, reduced motion behavior where relevant, and localization-safe layout. |
| 12 | Optimize another job | Add the deliberate second-job retention loop without corrupting or replacing the completed first-job result. Measure entry and successful completion. |
| 13 | Release-candidate journey audit | Run the complete clean-install journey, failure/retry paths, relaunch recovery, preview/save/export, accessibility checks, analytics contract audit, and regression suite. |

## Execution Rules

- Execute one story at a time in numeric order. Start the next only after the current story's tests, build, focused manual QA, progress update, commit, push and review gate are complete.
- Begin each story from live repository evidence. Preserve existing active-session changes and unrelated user work.
- Use test-first changes where behavior is testable. No new dependency without founder approval.
- Every product change must name the activation or retention step it is intended to move and how PostHog will show whether it worked.
- Keep the backend schema additive and backwards compatible. Do not change production data, credentials, auth providers, migrations or deployed services.
- Do not alter the live 1.4.2 binary or submit/archive/upload anything.
- Target marketing version 1.5.0 only after Stories 9-13 pass. Determine the next build number from the current repository and App Store record during a separately approved release-prep step; do not hardcode it now.
- If an unexpected fix expands beyond three files outside the story's expected scope, stop and report it.

## Validation Per Story

- Run focused tests for the changed behavior.
- Run the repository's full iOS test suite and Debug build.
- For release-sensitive changes, also run the Release configuration build.
- Exercise the changed path on the smallest supported simulator and a current iPhone simulator; use a physical device where the behavior depends on Apple services or real document flows.
- Run `git diff --check` and inspect the final diff for unrelated changes and prohibited content/PII.
- Update `tasks/progress.md` and `tasks/session-log.md` with branch, commit, test/build evidence, remaining risk and next story.

## Final 1.5.0 Gate

After Story 13, produce a release-readiness handoff containing the exact commits, test/build results, device evidence, analytics event map, known limitations, marketing version and proposed next build number. Stop there. Archive, TestFlight and App Store Connect actions require a separate explicit founder approval.

## Copy Prompt

Execute WP-46 from `/Users/nadavyigal/Documents/Projects /Agentic OS/executive-os/work-packets/WP-46-resumely-ftux-release-b-c-continuation.md` in the Resumely iOS repository. Stories 7 and 8 are owned by my current Claude Code session, so first reconcile their real branch, PR and commit state and do not duplicate or overwrite them. Once they are integrated, verify the approved Story 9 additive backend-evidence contract, then implement Stories 9-13 sequentially, one fully verified and pushed story at a time. The combined target is Resumely 1.5.0, but do not archive, upload, submit, change production services, or interfere with the live 1.4.2 app. Stop only on a hard gate or after producing the complete 1.5.0 release-readiness handoff.

## Final Output

- Story-by-story changes and activation/retention signal
- Files and commits per story
- Commands and validation evidence
- Branch/PR/push state
- Remaining risks and hard gates
- Exact 1.5.0 release-readiness handoff
