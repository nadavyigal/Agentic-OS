# Project Status

Last updated: 2026-05-15 17:12 IDT

Source policy: local folder mode only. No GitHub status was used. Status is based on local Agent OS files and targeted git metadata checks.

## Status Table

| Project | Freshness | Status | Current Phase | Active Story | Last Completed Story | Next Recommended Story | Estimated Completion | Last Validation | Last Updated | Blockers | Risks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RunSmart iOS | Fresh | Device build passed; manual outdoor/background QA still required before external TestFlight | Route feature TestFlight polish / external beta prep | Manual outdoor/background recording and battery-delta check | Story 10: TestFlight Polish And Privacy Review, plus Agent OS status source-of-truth consolidation | Physical-device outdoor/background recording check, then archive/upload readiness | Not estimated in local files | 2026-05-15 physical-device Debug build passed on connected iPhone 13, bundle id `com.runsmart.lite`; simulator build passed; latest full iPhone 17 XCTest attempt still stalled with `NSMachErrorDomain Code=-308`. | 2026-05-15 | Manual outdoor/background recording and battery-delta check remains open | Location/background behavior, battery, Garmin missing map data, pre-existing AppIcon warnings, older actor-isolation warning noise |
| ResumeBuilder iOS | Fresh | In progress; five-story tab/library spec completed, smoke QA and PR remain | Pre-release / TestFlight prep | Simulator smoke test all 5 tabs | Spec "Merge Track->Me, Redesign Optimized Resume, Real Resume Library" all 5 stories | Simulator smoke test all 5 tabs, create PR `claude/hungry-chatelet-a86030` -> `main`, then flip `BackendConfig.useMockLibraryService` once web API ships | 25% per local `tasks/progress.md` | Xcode build succeeded after each story commit. Manual smoke test all 5 tabs is still TODO. | 2026-05-15 | Resume Library backend endpoints are not live; mock service remains active | Swift 6 concurrency strictness, WKWebView PDF render fragility on real device, no Hebrew/RTL support, Resume Library backend endpoints not yet live |

## RunSmart iOS Detail

Source path: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

Source files read:

- `tasks/todo.md`
- `tasks/session-log.md`
- `tasks/lessons.md`

### Completed

- Route Stories 5-10 are recorded as complete through Story 10.
- Story 10 completed TestFlight polish and privacy review.
- Route/location privacy copy, weak GPS copy, Garmin missing-map copy, saved-route deletion copy, and TestFlight notes were updated.
- Historical compile-blocker notes for `RunSmartTab` ambiguity and `GlassCard` redeclaration were triaged as resolved in the active simulator build.
- Agent OS status source-of-truth was consolidated: the app repo task files are canonical and outer wrapper task files are pointer stubs.
- Duplicate loose task files `tasks/todo 2.md` and `tasks/todo 3.md` were removed.
- Connected physical device was discovered and a physical-device Debug build passed.

### Active

- Manual outdoor/background recording and battery-delta check before external TestFlight.

### Blocked

- External beta readiness remains blocked on manual outdoor/background/battery validation.
- Full iPhone 17 XCTest validation on 2026-05-15 stalled during simulator launch and is not a test pass.

### Validation

- Simulator build passed:
  `xcodebuild -project "IOS RunSmart app.xcodeproj" -scheme "IOS RunSmart app" -destination "generic/platform=iOS Simulator" build`
- Device discovery passed via `xcrun xctrace list devices` and `xcrun devicectl list devices`.
- Connected device evidence: `Nadav.Yigal's iPhone`, iPhone 13, iOS 26.4.2.
- Physical-device Debug build passed:
  `xcodebuild -project "IOS RunSmart app.xcodeproj" -scheme "IOS RunSmart app" -destination "platform=iOS,id=00008110-00192DDA2143801E" build`
- Device build evidence: `** BUILD SUCCEEDED **`, signing identity `Apple Development: nadav.yigal@gmail.com (V2D7D57MXR)`, provisioning profile `iOS Team Provisioning Profile: com.runsmart.lite`, bundle id `com.runsmart.lite`.
- Story 10 full iPhone 17 XCTest passed on 2026-05-14.
- Full iPhone 17 XCTest attempt on 2026-05-15 stalled with `NSMachErrorDomain Code=-308`.

### Next 3 Actions

1. Run the manual outdoor/background recording and battery-delta check on the connected iPhone.
2. Record exact device, route/run duration, lock/background behavior, battery delta, and any GPS/permission issues in local task files.
3. After device QA passes, run archive/upload readiness: signing, bundle id, privacy strings, App Store Connect, and TestFlight release notes.

## ResumeBuilder iOS Detail

Source path: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`

Source files read:

- `tasks/progress.md`
- `tasks/todo.md`
- `tasks/session-log.md`
- `tasks/lessons.md`

### Completed

- Spec "Merge Track->Me, Redesign Optimized Resume, Real Resume Library" is marked complete across all 5 stories.
- Story 1: tab restructure to Tailor / Optimized / Design / Expert / Me.
- Story 3: Score + Tailor merged; `AppState.latestOptimizationId` set on optimize.
- Story 2: Optimized Resume page redesigned preview-first with inline `ResumePreviewWebView`.
- Story 5: Me/Profile page now contains applications inline; old ProfileV2 and standalone applications list deleted.
- Story 4: Resume Library added with `SavedResume`, endpoints, real/mock service, view model, save prompt, and picker.
- Deleted files recorded: `Features/Score/ScoreView.swift`, `Features/Score/ScoreViewModel.swift`, `Features/V2/Profile/ProfileViewV2.swift`, `Features/Track/ApplicationsListView.swift`.

### Active

- Simulator smoke test all 5 tabs.

### Blocked

- Resume Library backend endpoints are not live; `BackendConfig.useMockLibraryService = true` remains active.

### Validation

- `tasks/progress.md` says Xcode build succeeded after each story commit.
- Manual simulator smoke test all 5 tabs remains TODO.
- No latest QA report is listed.

### Next 3 Actions

1. Run simulator smoke test across Tailor, Optimized, Design, Expert, and Me.
2. Create PR `claude/hungry-chatelet-a86030` -> `main` after smoke QA.
3. Flip `BackendConfig.useMockLibraryService = false` only after the web backend ships `/api/v1/resumes`.

## Data Quality Notes

- RunSmart iOS has no `tasks/progress.md`; local lessons now explicitly say app repo `tasks/todo.md`, `tasks/session-log.md`, and `tasks/lessons.md` are canonical.
- RunSmart iOS git branch is `routes`; latest local commit is `6cebead feat(routes): story 10 testflight polish`; status files are modified after that commit.
- ResumeBuilder iOS git branch reports `main`; local latest commit is `5ee5e47 Merge pull request #10 from nadavyigal/claude/vigilant-cannon-c799a3`.
- ResumeBuilder iOS local status says current branch is `claude/hungry-chatelet-a86030`; that appears to be the recommended PR/source branch rather than the currently checked-out branch.
- ResumeBuilder iOS has untracked local files in `.claire/`, `.claude/`, `.derivedData-validation/`, and duplicated asset variants.

