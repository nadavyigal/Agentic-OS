# Project Bridge: RunSmart iOS

Use this bridge only when cross-project context matters. The RunSmart iOS repo's local Agent OS remains the source of truth for implementation.

## 1. Project Identity

RunSmart iOS is the native SwiftUI mobile product for RunSmart.

It should use RunSmart Web as a product reference, not as a UI copy source.

## 2. Role In The Larger Vision

RunSmart iOS translates RunSmart into a simpler, cleaner, premium mobile experience for daily use.

It should become TestFlight-ready and eventually App Store-ready while respecting native iOS constraints and user expectations.

## 3. Responsible For

- Native SwiftUI mobile experience.
- Daily use workflow.
- Today screen.
- Run start and run logging.
- Plan clarity.
- AI Coach mobile experience.
- Profile and user settings.
- iOS permissions, location behavior, HealthKit readiness, and App Store-quality UX.

## 4. Not Responsible For

- Copying RunSmart Web UI.
- Recreating every web feature.
- Owning canonical web product logic.
- Inventing Garmin, Apple Health, background GPS, or sync behavior without repo evidence.
- ResumeBuilder AI workflows or design.
- Replacing the RunSmart Web source of current product capabilities.

## 5. Relationship To Other Projects

- RunSmart Web is the current product reference for capabilities and existing logic.
- iOS should decide whether each Web capability belongs on mobile based on mobile user value.
- Product logic can be shared conceptually, but UI should be native to each platform.
- If iOS introduces a better UX pattern, agents may recommend adapting the idea back to Web.
- Agents should not create duplicated business logic without documenting why.
- Atlas may later coordinate iOS tasks, specs, QA, and lessons, but must use the local iOS OS as source of truth.
- ResumeBuilder AI stays separate except for reusable agent workflows.

## 6. Source-Of-Truth Files Inside The Local Repo

Agents must inspect the local repo before implementation. Likely source-of-truth areas include:

- `tasks/progress.md` when present; if missing, use `tasks/todo.md` and latest `tasks/session-log.md` as the minimum status source.
- `tasks/todo.md`
- `tasks/session-log.md`
- `tasks/lessons.md` when blockers or repeated issues matter.
- SwiftUI screens and navigation.
- App state and models.
- Run start/logging flows.
- Plan and coach flows.
- Permission handling.
- HealthKit, location, notification, and background capability code if present.
- Local tasks, specs, and lessons.

Exact paths must be discovered inside the repo. Do not assume frameworks, APIs, entitlements, or capabilities exist without checking.

## 7. Local Agent OS Files Agents Must Read

Inside RunSmart iOS, read local files first:

- `AGENTS.md`
- `CURSOR.md` (Cursor agents)
- `CLAUDE.md` (Claude Code agents)
- `tasks/lessons.md`
- Relevant `tasks/` files
- Relevant `.agent-os/` files (note: `.agent-os/` lives at the outer wrapper, not the app repo root)
- `.cursor/rules/` (loaded automatically by Cursor)
- Xcode project and Swift package configuration when implementation requires it

If a file is missing, say so and continue with the next best local context.

## 8. Global OS Files Agents May Reference

Use selectively:

- `PROJECT-BRIDGES/runsmart-ios.md`
- `PROJECT-BRIDGES/runsmart-web.md` when adapting RunSmart product capabilities.
- `GLOBAL-STANDARDS.md` for shared product/engineering standards.
- `GLOBAL-WORKFLOWS.md` for cross-project planning.
- `GLOBAL-AGENT-RULES.md` for agent behavior.
- `GLOBAL-SELF-IMPROVEMENT.md` when saving reusable lessons.

Do not load the full Global OS for normal iOS tasks.

## 9. Product Priorities

- Daily use.
- Today screen.
- Run start and logging.
- Plan clarity.
- AI Coach.
- Profile.
- TestFlight readiness.
- App Store readiness over time.

## 10. Engineering Priorities

- Native SwiftUI patterns.
- Small stories with clear verification.
- Stable navigation and state management.
- Respect location, background activity, permissions, HealthKit, notifications, and battery constraints.
- Verify entitlements and platform APIs before implementation.
- Keep Web adaptation conceptual unless shared APIs are confirmed.

## 11. UX Priorities

- Simplify and elevate the mobile experience.
- Prioritize fast daily actions and clear next steps.
- Use platform-native navigation, controls, permissions, and feedback.
- Do not copy web layouts directly.
- Every UI change needs simulator or device visual QA.

## 12. QA Expectations

- Include evidence for completion: tests, build results, simulator checks, screenshots, or manual device notes.
- UI changes need visual QA.
- Permission, location, HealthKit, background, and run logging changes need explicit manual checks.
- TestFlight/App Store-facing changes need release notes and rollback or mitigation notes.

## 13. Risk Areas

- Location and background behavior.
- HealthKit and permissions.
- Battery usage.
- Run tracking accuracy.
- App Store review expectations.
- Over-copying web UI.
- Divergence from RunSmart product logic without documentation.

## 14. What Agents Must Never Do

- Do not copy Web UI directly.
- Do not assume a Web feature belongs in iOS without mobile user value.
- Do not assume APIs, entitlements, HealthKit, background modes, or location behavior exist without checking.
- Do not invent Garmin, Apple Health, or background GPS sync behavior.
- Do not mark TestFlight readiness without build and manual evidence.
- Do not mix ResumeBuilder patterns into RunSmart iOS.
- Do not replace the local RunSmart iOS OS with this bridge.

## 15. Example Prompts

```txt
Read the local RunSmart iOS Agent OS, then inspect the RunSmart Web bridge only for product capability context. Plan a native SwiftUI version of this flow without copying the web UI.
```

```txt
Review this iOS feature for Today, Run, Plan, Coach, and Profile fit. Include simulator/device QA evidence and note any permissions or HealthKit risks.
```

```txt
Compare this iOS UX pattern to RunSmart Web. If it improves the product, recommend whether Web should adapt the concept without copying iOS UI directly.
```

## 16. How To Update This Bridge

Update this bridge after major changes to:

- App navigation or core tabs.
- Run tracking/logging behavior.
- Today, Plan, Coach, or Profile scope.
- HealthKit, location, permissions, or background capabilities.
- TestFlight/App Store readiness expectations.
- Cross-project decisions involving RunSmart Web.

Keep implementation details in the local repo.

## 17. Token-Efficiency Guidance

- Load this bridge only for cross-project or platform-translation work.
- For daily iOS implementation, read local OS files and the specific local task/spec.
- Load the Web bridge only when adapting product capabilities.
- Do not load ResumeBuilder or Atlas bridges unless the task explicitly touches them.
