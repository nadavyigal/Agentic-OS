# Executive Dashboard

Manual source-of-truth dashboard for the Executive Intelligence OS. Financial cells stay `Needs Data` until a real source exists.

Last updated: 2026-06-02 IDT

## Executive Summary

RunSmart iOS v1.0 build 6 is in App Store review context and should stay frozen. Resumely iOS cleared analytics and UX/export gates on June 1, so the next constraint is an authenticated real-device smoke plus App Store Connect upload. RunSmart Web and ResumeBuilder Web are support repos and need dirty-tree triage before more implementation.

## CEO Focus

- Resumely iOS: authenticated real-device smoke and event/export verification.
- Resumely iOS: ASC upload and submit after smoke passes.
- RunSmart iOS: monitor App Store review, then scope 1.0.1 after review outcome.

## Financial Snapshot

Needs Data - no revenue/cost instrumentation wired.

## Open Decisions

- RunSmart 1.0.1 smallest safe scope after v1.0 review outcome
- Resumely ASC upload path: Fastlane API key versus manual portal upload
- ResumeBuilder Web rollout timing if Resumely smoke exposes backend issues

## Status Confidence

How much each project's state is backed by parsed local task files versus narrative only.

| Project | Confidence | Source | Last Validation |
| --- | --- | --- | --- |
| RunSmart iOS | High | derived | Swift parse validation passed for SupabaseRunSmartServices.swift after edit.; trackPlanGenerated call confirmed at line 271 via grep |
| Resumely iOS | High | tasks/progress.md | Phase 2 submit package: focused `OptimizedResumeViewModelTests` passed 11/11; `xcodebuild build` succeeded on iPhone 17 simulator using `/tmp/resumebuilder-derived`; full `xcodebuild test` passed 66 XCTest + 5 Swift Testing tests; `simctl` install/launch smoke succeeded on booted iPhone 17 with Home screenshot checked at `/tmp/resumebuilder-smoke/phase2-submit-package-launch-late.png` (2026-06-02). Default project-local `.derivedData` codesign is blocked by FileProvider/Finder extended attributes, but signed build/test passes from `/tmp` DerivedData |
| RunSmart Web | Medium | derived | Not parsed |
| ResumeBuilder AI (Web) | Medium | derived | Not parsed |
| Agentic OS | Medium | derived | Not parsed |

## Risk Board

- RunSmart iOS: Apple review outcome is external; v1.0 artifacts should remain frozen.
- Resumely iOS: no local Fastlane config / ASC API key, or manual portal upload is needed.
- Resumely iOS: real-device authenticated smoke has not been run after the June 1 fixes.
- RunSmart Web: dirty local tree with many modified/untracked files before more voice work.
- ResumeBuilder Web: rollout plan remains unchecked on a dirty PDF parse branch.
- Dirty local repo state: RunSmart iOS, Resumely iOS, RunSmart Web, Agentic OS, ResumeBuilder AI (Web).
- Dirty local repo state: RunSmart iOS, Resumely iOS, RunSmart Web, ResumeBuilder AI (Web).

## Next Recommended Actions

1. Resumely iOS: run authenticated real-device smoke through optimize, design, expert, preview/export.
1. Resumely iOS: verify PostHog Live Events/export coverage from a keyed build.
1. Resumely iOS: upload screenshots/listing and submit after smoke passes.
1. RunSmart iOS: monitor App Store review and keep v1.0 frozen.
