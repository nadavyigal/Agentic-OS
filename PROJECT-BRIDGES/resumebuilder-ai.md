# Project Bridge: ResumeBuilder AI

Use this bridge only when cross-project context matters. The ResumeBuilder AI repo's local Agent OS remains the source of truth for implementation.

## 1. Project Identity

ResumeBuilder AI is the AI resume optimization product.

It helps users create stronger, more tailored, more confidence-building resumes.

## 2. Role In The Larger Vision

ResumeBuilder AI is a separate AI product in the portfolio. It should benefit from reusable agent workflows, QA standards, and product thinking, but it must stay separate from RunSmart product logic and design patterns.

## 3. Responsible For

- Outstanding resume output quality.
- Job-tailored resume results.
- Resume templates.
- Export quality.
- PDF generation.
- User confidence and editing clarity.
- Hebrew/English direction where relevant.
- Product quality before monetization.

## 4. Not Responsible For

- RunSmart training, coaching, Garmin, Apple, running, or health logic.
- RunSmart visual patterns unless independently justified.
- Atlas orchestration implementation.
- Cross-project shared business logic.
- Monetization before resume quality is strong.

## 5. Relationship To Other Projects

- ResumeBuilder stays separate from RunSmart except for reusable agent workflows.
- Lessons about AI output quality, QA, prompts, or exports may become global lessons if broadly useful.
- Atlas may later coordinate ResumeBuilder specs, QA, and workflows, but must use the local ResumeBuilder OS as source of truth.
- RunSmart UI, coaching, and fitness logic should not leak into ResumeBuilder.

## 6. Source-Of-Truth Files Inside The Local Repo

Agents must inspect the local repo before implementation. Likely source-of-truth areas include:

- Resume generation prompts and logic.
- Template files.
- Export/PDF generation code.
- Job-tailoring logic.
- User flows and editor screens.
- Localization, Hebrew/English, and direction handling.
- Local tasks, specs, and lessons.

Exact paths must be discovered inside the repo. Do not assume template engines, export tools, APIs, or AI providers exist without checking.

## 7. Local Agent OS Files Agents Must Read

Inside ResumeBuilder AI, read local files first:

- `AGENTS.md`
- `CURSOR.md` (Cursor agents)
- `CLAUDE.md` (Claude Code agents)
- `tasks/MEMORY.md`, `tasks/ERRORS.md`, `tasks/lessons.md`
- `.cursor/rules/` (loaded automatically by Cursor)
- Relevant `.specify/` files (Speckit planning)

If a file is missing, say so and continue with the next best local context.

## 8. Global OS Files Agents May Reference

Use selectively:

- `PROJECT-BRIDGES/resumebuilder-ai.md`
- `GLOBAL-STANDARDS.md` for shared product/engineering standards.
- `GLOBAL-WORKFLOWS.md` for cross-project planning.
- `GLOBAL-AGENT-RULES.md` for agent behavior.
- `GLOBAL-SELF-IMPROVEMENT.md` when saving reusable lessons.

Do not load RunSmart bridge files unless the task explicitly concerns shared agent workflow or portfolio planning.

## 9. Product Priorities

- Outstanding resume output quality.
- High-quality templates.
- Reliable export and PDF generation.
- Job-tailored results.
- User confidence.
- Hebrew/English direction where relevant.
- Product quality before monetization.

## 10. Engineering Priorities

- Deterministic, testable export behavior where possible.
- Strong AI prompt/version discipline.
- Template quality that supports real-world resume use.
- Avoid one-off formatting hacks.
- Check existing AI, PDF, and template architecture before changes.
- Keep changes scoped and verifiable.

## 11. UX Priorities

- Users should understand what changed and why.
- Resume output should feel professional, editable, and trustworthy.
- Export flow should be clear and reliable.
- Hebrew/English direction should not feel bolted on.
- Confidence-building matters more than flashy UI.

## 12. QA Expectations

- Include evidence for completion: tests, build/lint results, sample output, PDF/export checks, or manual QA notes.
- Resume quality changes should include before/after examples or evaluation notes.
- Template and export changes need visual/PDF QA.
- Hebrew/English direction changes need language-direction verification.
- Risky monetization changes require rollback notes.

## 13. Risk Areas

- Low-quality AI output.
- Broken PDF/export formatting.
- Resume templates that look good but parse poorly.
- Hebrew/English direction bugs.
- User overconfidence in weak resume suggestions.
- Mixing RunSmart assumptions into ResumeBuilder.
- Monetization pressure before product quality.

## 14. What Agents Must Never Do

- Do not mix RunSmart logic or design patterns into ResumeBuilder.
- Do not assume PDF/export libraries or AI providers without checking the repo.
- Do not optimize monetization at the expense of resume quality.
- Do not claim resume output quality improved without evidence.
- Do not ignore Hebrew/English direction when relevant.
- Do not replace the local ResumeBuilder OS with this bridge.

## 15. Example Prompts

```txt
Read the local ResumeBuilder Agent OS, then improve this resume feature with output quality as the primary goal. Include before/after evidence and export QA.
```

```txt
Review this template or PDF change for professional quality, parsing risk, Hebrew/English direction, and user confidence.
```

```txt
Plan this ResumeBuilder feature without importing RunSmart assumptions. Use global standards only for agent workflow, QA, and lessons.
```

## 16. How To Update This Bridge

Update this bridge after major changes to:

- Resume generation strategy.
- Template system.
- PDF/export pipeline.
- Job-tailoring workflow.
- Hebrew/English direction support.
- Monetization strategy once product quality is strong.
- Reusable AI-output lessons that may matter globally.

Keep implementation details in the local repo.

## 17. Token-Efficiency Guidance

- Load this bridge only for ResumeBuilder strategy, shared standards, or cross-project planning.
- For daily ResumeBuilder implementation, read local OS files and the specific local task/spec.
- Do not load RunSmart bridges unless there is an explicit reusable workflow question.
- Summarize output-quality lessons globally only when they are likely to matter again.

