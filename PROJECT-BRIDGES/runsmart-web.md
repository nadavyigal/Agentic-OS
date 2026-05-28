# Project Bridge: RunSmart Web

Use this bridge only when cross-project context matters. The RunSmart Web repo's local Agent OS remains the source of truth for implementation.

## 1. Project Identity

RunSmart Web is the current main RunSmart product logic and web experience.

It contains the existing user flows, product functionality, training concepts, AI coaching behavior, web pages, experiments, and monetization work.

## 2. Role In The Larger Vision

RunSmart Web is the main reference for RunSmart product capabilities across the portfolio.

It should remain stable while being improved. It should help define what RunSmart does, but it should not force other platforms to copy how the web UI looks or behaves.

## 3. Responsible For

- Current web user experience.
- Existing RunSmart product functionality.
- AI running coach behavior and quality.
- Training plan and coaching product logic.
- Web monetization experiments and readiness.
- Garmin/Apple readiness from the web product perspective.
- Documentation of product logic that RunSmart iOS may adapt.

## 4. Not Responsible For

- Native iOS interface decisions.
- App Store or TestFlight release requirements.
- ResumeBuilder AI product logic, design, or resume workflows.
- Atlas orchestration implementation.
- Duplicating every mobile feature or platform behavior.

## 5. Relationship To Other Projects

- RunSmart iOS may use Web as a product reference, not a UI copy source.
- If a feature exists in Web but not iOS, decide whether it belongs in iOS based on mobile user value.
- If iOS introduces a better UX pattern, agents may recommend bringing it back to Web.
- Product logic can be shared conceptually, but UI should be platform-native.
- Agents should not create duplicated business logic without documenting why.
- ResumeBuilder AI stays separate except for reusable agent workflows.
- Atlas may coordinate RunSmart Web tasks, specs, QA, and lessons, but must not replace the local Web OS.

## 6. Source-Of-Truth Files Inside The Local Repo

Agents must inspect the local repo before implementation. Likely source-of-truth areas include:

- Product routes/pages and user flows.
- AI coaching logic.
- Training plan logic.
- Integrations and API routes.
- Auth, subscription, and monetization files.
- Local tasks, specs, and lessons.

Exact paths must be discovered inside the repo. Do not assume APIs, integrations, or file names exist without checking.

## 7. Local Agent OS Files Agents Must Read

Inside RunSmart Web, read local files first:

- `AGENTS.md`
- `CURSOR.md` (Cursor agents)
- `CLAUDE.md` (Claude Code agents)
- `tasks/MEMORY.md`, `tasks/ERRORS.md`, `tasks/lessons.md`
- `.cursor/rules/` (loaded automatically by Cursor)
- `.cursor/skills/` (running coach AI skills, Cursor only)
- Relevant `docs/agent-os/` files

If a file is missing, say so and continue with the next best local context.

## 8. Global OS Files Agents May Reference

Use selectively:

- `PROJECT-BRIDGES/runsmart-web.md`
- `PROJECT-BRIDGES/runsmart-ios.md` when work affects iOS adaptation.
- `GLOBAL-STANDARDS.md` for shared product/engineering standards.
- `GLOBAL-WORKFLOWS.md` for cross-project planning.
- `GLOBAL-AGENT-RULES.md` for agent behavior.
- `GLOBAL-SELF-IMPROVEMENT.md` when saving reusable lessons.

Do not load the full Global OS for normal Web tasks.

## 9. Product Priorities

- Reliable UX.
- AI coaching quality.
- Training plan usefulness and trust.
- Garmin/Apple readiness.
- Monetization readiness.
- Clear product logic that can later be adapted to iOS.
- Stability while improving active user flows.

## 10. Engineering Priorities

- Preserve existing behavior unless the task explicitly changes it.
- Check existing project patterns before adding abstractions.
- Verify integration assumptions before planning sync behavior.
- Avoid duplicated business logic unless the reason is documented.
- Keep risky changes small and reversible.

## 11. UX Priorities

- Web flows should be clear, stable, and confidence-building.
- UI changes need responsive visual QA.
- Do not make Web imitate iOS just because iOS improves a pattern.
- Consider whether iOS learnings can improve Web without breaking web expectations.

## 12. QA Expectations

- Include evidence for completion: tests, build/lint results, manual checks, or screenshots.
- Every UI change needs visual QA.
- Garmin, Apple, AI coaching, auth, subscriptions, and data changes need extra verification.
- Risky changes require rollback notes.

## 13. Risk Areas

- AI coaching correctness and user trust.
- Training plan logic regressions.
- Garmin/Apple readiness and sync assumptions.
- Auth, payments, subscriptions, and monetization.
- Data privacy and user health/running data.
- Web-to-iOS logic drift.

## 14. What Agents Must Never Do

- Do not assume APIs exist without checking the repo.
- Do not invent sync behavior for Garmin, Apple Health, or background GPS.
- Do not force iOS to copy Web UI.
- Do not mark work complete without evidence.
- Do not edit local project OS files unless the task calls for it.
- Do not move ResumeBuilder logic or design patterns into RunSmart.
- Do not replace the local RunSmart Web OS with this bridge.

## 15. Example Prompts

```txt
Read the local RunSmart Web Agent OS, then compare this feature to the RunSmart iOS bridge. Decide whether the product logic should be documented for iOS adaptation without copying the web UI.
```

```txt
Plan this RunSmart Web feature using local repo context first. Include user goal, small stories, QA evidence, integration assumptions checked, and rollback notes if risky.
```

```txt
Review this RunSmart Web UI change for reliable UX, responsive behavior, AI coaching trust, and whether any iOS bridge note should be updated.
```

## 16. How To Update This Bridge

Update this bridge after major changes to:

- Core product capabilities.
- Training or AI coaching logic that iOS may adapt.
- Garmin/Apple readiness assumptions.
- Monetization strategy.
- Cross-project decisions involving Web and iOS.

Keep updates short. Put implementation details in the local repo.

## 17. Token-Efficiency Guidance

- Load this bridge only for cross-project work.
- For daily Web implementation, read local OS files and only the specific local spec/task needed.
- Do not load RunSmart iOS, ResumeBuilder, or Atlas bridges unless the task touches them.
- Summarize cross-project decisions instead of copying local docs.

