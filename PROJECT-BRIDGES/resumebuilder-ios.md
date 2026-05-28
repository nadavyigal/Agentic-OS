# Project Bridge: ResumeBuilder iOS

Use this bridge only when cross-project context matters. The ResumeBuilder iOS repo's local Agent OS remains the source of truth for implementation.

## 1. Project Identity

ResumeBuilder iOS is the native iOS app for the ResumeBuilder product.

It focuses on mobile resume optimization, resume output quality, template/design quality, PDF/export behavior, and eventual TestFlight/App Store readiness.

## 2. Role In The Larger Vision

ResumeBuilder iOS is separate from RunSmart. It can reuse global agent workflows and QA standards, but it must not inherit RunSmart product logic, running UX, Garmin assumptions, or HealthKit/location patterns.

## 3. Responsible For

- Native iOS resume optimization flows.
- Resume output quality.
- Expert/apply behavior.
- Template selection and customization.
- Preview/PDF/export quality.
- TestFlight and App Store readiness for the iOS resume product.
- Hebrew/English and RTL/LTR support when approved and scoped.

## 4. Not Responsible For

- RunSmart running, coaching, route, Garmin, Apple Health, location, or background GPS logic.
- Atlas orchestration implementation.
- ResumeBuilder Web status unless a specific bridge task calls for it.
- Adding new dependencies or backend assumptions without repo evidence.

## 5. Relationship To Other Projects

- ResumeBuilder iOS stays separate from RunSmart except for reusable agent workflows.
- ResumeBuilder iOS may share lessons about AI output quality, PDF/export QA, SwiftUI, and TestFlight with the Global OS.
- Atlas may later coordinate status, specs, QA, and lessons, but must use local ResumeBuilder iOS files as the source of truth.

## 6. Source-Of-Truth Files Inside The Local Repo

Agents must inspect the local repo before implementation. Likely source-of-truth areas include:

- `tasks/progress.md`
- `tasks/todo.md`
- `tasks/session-log.md`
- `tasks/lessons.md`
- `docs/specs/`
- `docs/qa/`
- `.agent-os/workflows/`
- SwiftUI V2 feature files, view models, services, template/design models, and export/preview code as needed.

Exact paths must be discovered inside the repo. Do not assume spec paths, APIs, PDF render routes, or template systems exist without checking.

## 7. Local Agent OS Files Agents Must Read

Inside ResumeBuilder iOS, read local files first:

- `AGENTS.md`
- `CURSOR.md` (Cursor agents)
- `CLAUDE.md` (Claude Code agents)
- `tasks/MEMORY.md` and `tasks/ERRORS.md`
- `tasks/progress.md`
- `tasks/todo.md`
- `tasks/session-log.md`
- `tasks/lessons.md` when blockers or repeated issues matter
- `.cursor/rules/` (loaded automatically by Cursor)
- Relevant `.agent-os/workflows/`

If a file is missing, say so and continue with the next best local context.

## 8. Global OS Files Agents May Reference

Use selectively:

- `PROJECT-BRIDGES/resumebuilder-ios.md`
- `GLOBAL-STANDARDS.md`
- `GLOBAL-WORKFLOWS.md`
- `GLOBAL-AGENT-RULES.md`
- `GLOBAL-SELF-IMPROVEMENT.md`

Do not load RunSmart bridge files unless the task explicitly concerns shared agent workflow or portfolio planning.

## 9. Product Priorities

- Outstanding resume output quality.
- Template and design quality.
- Reliable Preview/PDF/export behavior.
- Clear expert/apply UX.
- User confidence.
- Hebrew/English direction when relevant.
- Product quality before monetization.

## 10. Engineering Priorities

- Follow Swift 6 and Swift Observation rules from local lessons.
- Keep new screens/features in `Features/V2/`.
- Avoid unapproved Swift Package dependencies.
- Verify API endpoints, render routes, and export behavior before assuming they exist.
- Keep changes small and validation-friendly.

## 11. UX Priorities

- Applying expert changes should feel immediate and trustworthy.
- Preview and PDF output should match what users expect to share.
- Template customization should be clear and reversible.
- Hebrew/RTL support should be explicit, not accidental.

## 12. QA Expectations

- Build evidence is required before completion.
- Manual simulator/device smoke evidence is required for apply, preview, PDF, template, and export flows.
- PDF/export changes need visual output checks.
- TestFlight claims require signing, bundle id, archive, upload, and smoke test evidence.

## 13. Risk Areas

- Swift 6 concurrency strictness.
- WKWebView preview/PDF rendering fragility.
- Missing or stale specs.
- Dirty worktrees and branch/status mismatch.
- No Hebrew/RTL support yet.
- Over-optimizing monetization before output quality.

## 14. What Agents Must Never Do

- Do not mix RunSmart logic or UI into ResumeBuilder iOS.
- Do not assume APIs, specs, PDF routes, or template engines exist without checking.
- Do not claim output quality improved without sample evidence.
- Do not claim TestFlight readiness without archive/upload and smoke evidence.
- Do not add dependencies without explicit approval.
- Do not replace the local ResumeBuilder iOS OS with this bridge.

## 15. Example Prompts

```txt
Read the local ResumeBuilder iOS Agent OS and current status files. Do not change code. Run the next validation task, record exact evidence, and update tasks/progress.md.
```

```txt
Plan the next ResumeBuilder iOS story from the active tracked spec. If the spec path is missing, stop and create or restore the spec before implementation.
```

```txt
Review this ResumeBuilder iOS preview/PDF change for output quality, device behavior, and user confidence. Include visual or sample-output evidence.
```

## 16. How To Update This Bridge

Update this bridge after major changes to:

- Resume optimization flow.
- Expert/apply behavior.
- Preview/PDF/export architecture.
- Template/design system.
- Hebrew/RTL support.
- TestFlight/App Store readiness process.

Keep implementation details in the local repo.

## 17. Token-Efficiency Guidance

- Load this bridge only for cross-project dashboard, portfolio, or shared workflow tasks.
- For daily ResumeBuilder iOS implementation, read local status files and the one relevant workflow/spec.
- Do not load RunSmart bridges unless comparing reusable agent practices.
- Summarize lessons globally only when they are likely to matter again.

