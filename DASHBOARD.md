# Portfolio Dashboard

Last updated: 2026-05-15 17:12 IDT

Source policy: local folder mode only. No GitHub status was used. The dashboard does not infer progress beyond local Agent OS files and targeted git metadata checks.

## 1. Executive Summary

Overall portfolio status: both active iOS projects are fresh and have moved forward.

Main progress since last dashboard update:

- RunSmart iOS now has a connected iPhone discovered and a successful physical-device Debug build for bundle id `com.runsmart.lite`.
- RunSmart iOS also consolidated its Agent OS status source of truth: app repo task files are canonical, outer task files are pointer stubs.
- ResumeBuilder iOS completed the five-story spec "Merge Track->Me, Redesign Optimized Resume, Real Resume Library."
- ResumeBuilder iOS moved from 10% to 25% estimated completion in local progress.

Biggest blockers:

- RunSmart iOS still needs manual outdoor/background recording and battery-delta QA before external TestFlight.
- ResumeBuilder iOS still needs a simulator smoke test across all 5 tabs.
- ResumeBuilder iOS Resume Library backend endpoints are not live, so the app is still using mocks for that service.

Projects needing QA:

- RunSmart iOS: physical-device outdoor recording, lock/background behavior, battery delta, and follow-up release-readiness checks.
- ResumeBuilder iOS: smoke test Tailor, Optimized, Design, Expert, and Me.

Projects needing my decision:

- RunSmart iOS: whether one focused physical-device pass is enough before archive/upload readiness.
- ResumeBuilder iOS: whether to create the PR immediately after smoke QA or wait for backend `/api/v1/resumes`.

Best next action: run the RunSmart iOS manual outdoor/background/battery test, then run ResumeBuilder's five-tab simulator smoke test.

## 2. Project Status Table

| Project | Status | Current phase | Active story | Last completed story | Next recommended story | Estimated completion | Last validation | Last updated | Blockers | Risks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RunSmart iOS | Fresh; device build passed; needs manual device QA | Route feature TestFlight polish / external beta prep | Manual outdoor/background recording and battery-delta check | Story 10 plus Agent OS status-source consolidation | Device outdoor/background/battery QA, then archive/upload readiness | Not estimated in local files | 2026-05-15 physical-device Debug build passed on connected iPhone 13; simulator build passed; latest full XCTest attempt stalled | 2026-05-15 | Manual outdoor/background/battery validation | Location/background behavior, battery, Garmin missing map data, warning noise |
| ResumeBuilder iOS | Fresh; five-story spec complete; needs smoke QA | Pre-release / TestFlight prep | Simulator smoke test all 5 tabs | Spec "Merge Track->Me, Redesign Optimized Resume, Real Resume Library" all 5 stories | Smoke test all tabs, create PR, flip mock library flag after backend ships | 25% per local progress | Xcode build succeeded after each story commit; manual smoke TODO | 2026-05-15 | Resume Library backend endpoints not live; mock service active | Swift 6 concurrency, WKWebView PDF fragility, no Hebrew/RTL support, backend dependency |

Freshness rule:

- Fresh: updated in the last 48 hours.
- Needs Review: updated in the last 3-7 days.
- Stale: older than 7 days.
- Unknown: no reliable updated date found.

## 3. RunSmart iOS Detailed Status

### Completed

- Route Stories 5-10 are recorded as complete.
- Story 10 added route/location privacy copy, weak GPS copy, Garmin missing-map copy, saved-route deletion copy, and TestFlight release notes.
- Historical `RunSmartTab` ambiguity and `GlassCard` redeclaration compile blockers no longer reproduce in the active simulator build.
- Agent OS status source-of-truth was consolidated: app repo task files are canonical, outer wrapper task files are pointer stubs.
- Duplicate loose task files were removed.
- Connected iPhone was discovered and physical-device Debug build passed.

### Currently Active

- Manual outdoor/background recording and battery-delta check before external TestFlight.

### Blocked

- External beta readiness remains blocked by manual physical-device run QA.
- Latest full iPhone 17 XCTest attempt stalled and cannot be counted as passed.

### Validation Done

- Simulator build passed on 2026-05-15.
- Device discovery passed for `Nadav.Yigal's iPhone`, iPhone 13, iOS 26.4.2.
- Physical-device Debug build passed on connected iPhone with bundle id `com.runsmart.lite`.
- Story 10 full iPhone 17 test pass succeeded on 2026-05-14.

### Risks Remaining

- Background location and battery behavior are not validated in a real outdoor run.
- Garmin imports can lack map data.
- Weak GPS can reduce route-match confidence.
- Pre-existing AppIcon warnings and older actor-isolation warning noise remain.

### Recommended Next 3 Actions

1. Run manual outdoor recording on the connected iPhone, including lock/background behavior and battery delta.
2. Record exact evidence in RunSmart iOS `tasks/todo.md` and `tasks/session-log.md`.
3. After device QA passes, do archive/upload readiness: signing, bundle id, privacy strings, App Store Connect, and release notes.

## 4. ResumeBuilder iOS Detailed Status

### Completed

- Full spec "Merge Track->Me, Redesign Optimized Resume, Real Resume Library" is marked complete.
- Tab structure is now Tailor / Optimized / Design / Expert / Me.
- `AppState.latestOptimizationId` is persisted and drives Optimized and Expert tabs.
- Optimized Resume is preview-first with inline `ResumePreviewWebView`.
- Applications were merged into Me/Profile.
- Resume Library model, endpoints, real/mock service, view model, save prompt, and picker were added.
- Legacy Score/ProfileV2/Applications list files were deleted.

### Currently Active

- Simulator smoke test all 5 tabs.

### Blocked

- Resume Library backend endpoints are not live.
- `BackendConfig.useMockLibraryService = true` remains active until `/api/v1/resumes` ships on the web/backend side.

### Validation Done

- Local progress says Xcode build succeeded after each story commit.
- Manual simulator smoke test all 5 tabs remains TODO.
- No latest QA report is listed.

### Risks Remaining

- Swift 6 concurrency strictness.
- WKWebView PDF render fragility on real device.
- No Hebrew/RTL support.
- Mock Resume Library may hide backend integration issues until `/api/v1/resumes` exists.

### Recommended Next 3 Actions

1. Smoke test all 5 tabs: Tailor, Optimized, Design, Expert, and Me.
2. Create PR `claude/hungry-chatelet-a86030` -> `main` after smoke QA.
3. Flip `BackendConfig.useMockLibraryService = false` only after `/api/v1/resumes` ships.

## 5. Cross-Project Priority Board

### Now

- RunSmart iOS: manual outdoor/background/battery validation.
- ResumeBuilder iOS: five-tab simulator smoke test.

### Next

- RunSmart iOS: archive/upload readiness after physical-device QA.
- ResumeBuilder iOS: PR from `claude/hungry-chatelet-a86030` to `main`.

### Later

- RunSmart iOS: clean up warning noise and confirm external beta notes.
- ResumeBuilder iOS: backend resume library integration, PDF/export device QA, Hebrew/RTL planning.

### Blocked

- RunSmart iOS external TestFlight until manual outdoor/background/battery validation is done.
- ResumeBuilder iOS real Resume Library integration until `/api/v1/resumes` ships.

### Needs QA

- RunSmart iOS: physical-device outdoor run, lock/background behavior, battery delta, Garmin map/no-map scenarios.
- ResumeBuilder iOS: five-tab smoke test, preview-first Optimized tab, save prompt, library picker, Me/Profile applications.

### Needs My Decision

- RunSmart iOS: acceptable threshold for TestFlight after physical-device run validation.
- ResumeBuilder iOS: whether PR can proceed with mock library service while backend endpoints are pending.

## 6. Validation Board

| Project | Build status | Test status | Manual QA status | TestFlight readiness | Latest validation date | Missing validation |
| --- | --- | --- | --- | --- | --- | --- |
| RunSmart iOS | Simulator build passed; physical-device Debug build passed | Full Story 10 test passed 2026-05-14; 2026-05-15 full test attempt stalled | Manual outdoor/background/battery QA not done | Not external-beta ready until manual device run QA and archive/upload checks pass | 2026-05-15 | Outdoor/background/battery run, archive/upload readiness |
| ResumeBuilder iOS | Xcode build succeeded after each story commit | No full test pass recorded in progress | Five-tab smoke test TODO | Not ready | 2026-05-15 build notes | Five-tab smoke test, PR review, real backend resume library integration, PDF/export device QA |

## 7. Decision Board

| Decision | Project | Why it matters | Options | Recommended option | Urgency |
| --- | --- | --- | --- | --- | --- |
| Is one focused physical-device run enough before archive prep? | RunSmart iOS | External beta depends on real background/battery confidence | One focused device check; broader device matrix; pause for more automation | One focused outdoor/background/battery check, then archive readiness review | High |
| Can ResumeBuilder PR proceed while Resume Library uses mocks? | ResumeBuilder iOS | The five-story spec is complete, but backend endpoints are pending | PR now with mock flag; wait for backend; split PR | PR after smoke QA, clearly documenting mock flag and backend dependency | High |
| When to flip `useMockLibraryService` | ResumeBuilder iOS | Real library behavior depends on web/backend `/api/v1/resumes` | Flip now; flip after backend ships; keep mocks for TestFlight | Flip only after backend endpoint is live and tested | Medium |

## 8. Risks And Blockers

### Technical Blockers

- RunSmart iOS: latest full XCTest attempt stalled with `NSMachErrorDomain Code=-308`.
- ResumeBuilder iOS: Resume Library backend endpoints are not live.

### Product Blockers

- ResumeBuilder iOS: real Resume Library behavior is not fully product-valid until backend integration exists.

### QA Blockers

- RunSmart iOS: manual outdoor/background/battery validation is not complete.
- ResumeBuilder iOS: five-tab simulator smoke test is not complete.

### Design/UX Blockers

- ResumeBuilder iOS: no Hebrew/RTL support is listed as a risk.
- RunSmart iOS: weak GPS and Garmin missing-map UX must be manually checked.

### Apple/TestFlight Blockers

- RunSmart iOS: archive/upload readiness, signing, bundle id, privacy strings, and App Store Connect checks remain after device QA.
- ResumeBuilder iOS: TestFlight readiness not established; PDF/export device QA still ahead.

### Unknowns Caused By Missing Data

- RunSmart iOS still has no `tasks/progress.md`; local lessons say canonical status is `tasks/todo.md`, `tasks/session-log.md`, and `tasks/lessons.md`.
- ResumeBuilder iOS local progress names `claude/hungry-chatelet-a86030` as the branch for PR, while local git currently reports `main`.
- No latest QA report is listed for ResumeBuilder iOS.

## 9. Lessons / Repeated Patterns

- RunSmart iOS: app repo task memory is canonical; outer wrapper task files should only point to it.
- RunSmart iOS: do not claim TestFlight readiness without signing, bundle id, archive status, permissions, privacy strings, and smoke tests.
- RunSmart iOS: simulator build and XCTest pass are separate evidence; a stalled XCTest run is not a pass.
- ResumeBuilder iOS: use Swift Observation with `@Observable` and `@MainActor`; Swift 6 concurrency issues are build errors.
- ResumeBuilder iOS: new screens/features belong in `Features/V2/`.
- ResumeBuilder iOS: do not add SPM dependencies without approval.

## 10. Recommended Next Steps

Best next action for RunSmart iOS:

1. Run the outdoor/background/battery validation on the connected iPhone and record evidence.

Best next action for ResumeBuilder iOS:

1. Smoke test all five tabs and record exact pass/fail evidence.

Best cross-project action:

1. Keep both projects paused on new feature implementation until the current QA checks are recorded.

What to ask Codex/Claude to do next:

```txt
Inside the project repo, read AGENTS.md, CODEX.md or CLAUDE.md, tasks/todo.md, tasks/progress.md if present, and tasks/session-log.md. Do not start new feature work. Run the current validation task only, record exact evidence, and update the local status files.
```

Recommendation:

- RunSmart iOS: pause new story implementation until physical-device outdoor/background/battery QA is complete.
- ResumeBuilder iOS: pause new story implementation until five-tab smoke QA is complete and PR readiness is clear.

## 11. Executive Intelligence OS

Layer 8 summary. Source of truth: `executive-os/EXECUTIVE-DASHBOARD.md`. Financial
figures are `Needs Data` until a real source is wired; no numbers are invented here.

| Sub-OS | Status | Note |
| --- | --- | --- |
| CEO OS | Active | Focus: clear the two-app App Store submission sprint before new scope |
| CFO / Monetization OS | Needs Data | No revenue/cost instrumentation yet; schema defined in `executive-os/EXECUTIVE-METRICS.md` |
| Analysis OS | Ready | No active research sprint; run `PROMPTS/analysis-research-sprint.md` to start |

- **Current CEO priority:** RunSmart iOS App Store approval; Resumely iOS copy +
  analytics, then submit.
- **Current financial focus:** define real data sources for revenue, cost, and
  activation (values still `Needs Data`).
- **Current research sprint:** none.
- **Open executive decisions:** see `executive-os/EXECUTIVE-DECISIONS.md` (EXD-001
  logged: adopt Layer 8, markdown-first, phased).
- **Top executive risks:** App Store approval delay blocks both apps; no
  financial/activation visibility; Resumely analytics not wired before submit.

Run cadence: `executive-os/EXECUTIVE-RHYTHM.md`.

