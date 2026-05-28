# Global Agent Rules

These rules guide Claude Code, Codex, Cursor, and future agents across projects.

## Core Rules

1. Agents must not jump directly into code for complex tasks.
2. Agents must first understand the project context.
3. Every feature must have a clear user goal.
4. Every implementation must be broken into small stories.
5. Every claim of completion must include evidence.
6. Every UI change must include visual QA.
7. Every risky change must include rollback notes.
8. Every project should keep its own local `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, `CURSOR.md`, `tasks/` folder, `.cursor/rules/`, and `.agent-os/` folder.
9. The global OS guides behavior across projects but does not replace project-specific OS files.
10. Bridge files explain how each project connects to the global vision.
11. The global OS should be used selectively to avoid token waste.
12. The local project OS is the source of truth for implementation inside each repo.

## Context Loading Rules

- Load the minimum useful context.
- Prefer local project files for repo-specific tasks.
- Read bridge files only when cross-project context matters.
- Do not read every global file by default.
- Do not duplicate long project docs into the global OS.

## Agent Output Rules

Agents should usually provide:

- What they understood.
- What they changed or propose changing.
- Evidence.
- Risks or skipped checks.
- Next recommended action.

For implementation tasks, cite files and commands where useful.

