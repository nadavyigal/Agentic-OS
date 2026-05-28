# Global Standards

These standards apply across products unless a local project OS says otherwise.

## Product Standards

- Every feature must have a clear user goal.
- Every feature should answer: who is this for, what problem does it solve, and how will we know it worked?
- Prefer simple, usable workflows over clever complexity.
- User trust matters: outputs should be explainable, editable, and recoverable.
- Monetization should not weaken core product quality.
- Accessibility, localization, and mobile behavior should be considered early when relevant.

## Engineering Standards

- Agents must first understand project context.
- Agents must not jump directly into code for complex tasks.
- Every implementation must be broken into small stories.
- Keep changes scoped to the requested outcome.
- Use existing project patterns before adding new abstractions.
- Avoid duplicating project docs in this global OS.
- No secrets, API keys, private credentials, or local-only sensitive data.
- Risky changes need rollback notes.

## UI Standards

- Every UI change must include visual QA.
- UI should support the product's real workflow, not just look complete.
- Prefer clear hierarchy, usable states, and responsive behavior.
- Check empty, loading, error, success, and permission states where relevant.
- Native mobile apps should respect platform conventions instead of copying web UI.

## QA Standards

- Every claim of completion must include evidence.
- Evidence can include tests, lint/build results, screenshots, logs, manual checks, or a clear explanation of what could not be verified.
- QA should check acceptance criteria, regressions, edge cases, security, and UX.
- Do not mark work done if key verification was skipped.

## Local Source Of Truth

Every project should keep its own:

- `AGENTS.md`
- `CLAUDE.md`
- `CODEX.md`
- `tasks/` folder
- `.agent-os/` folder

The global OS guides behavior across projects but does not replace project-specific OS files.

