# Bootstrap Cursor OS

Generate the Cursor Agent OS files for a product repo.

## Input

- Repo path (local filesystem)
- Existing `AGENTS.md` content (read from repo)
- Which `tasks/` tier applies (minimal: MEMORY + ERRORS + lessons; full: + todo + session-log; full+dashboard: + progress)

## Steps

1. Read the repo's `AGENTS.md` to understand stack, commands, and project-specific rules.
2. Read `tasks/` to confirm which files exist.
3. Generate `.cursor/rules/agent-os-core.mdc` from `TEMPLATES/cursor-rules-core.mdc`, adding the project's done-gate command under "Work Rules".
4. If the project has iOS/Swift code, generate `.cursor/rules/swift-ios.mdc` with signing, bundle ID, nested git root, and SwiftUI rules from the local `AGENTS.md`.
5. If the project has Next.js/TypeScript code, generate `.cursor/rules/nextjs-ts.mdc` with lint/type-check/build gate and relevant web-specific rules.
6. Generate `CURSOR.md` from `TEMPLATES/cursor-router-template.md`, filling in project name, stack, done gate, and cross-project path.
7. Create `tasks/ERRORS.md` if missing (empty with format header).

## Output

List all files created with their paths. Do not duplicate content already in `AGENTS.md`. Keep rules concise: enforce ritual, not architecture.

## Constraints

- Do not import `.cursor/skills/` from other repos.
- Do not create `tasks/` files that the project does not use (respect tier).
- Do not modify existing `AGENTS.md` or `CLAUDE.md`.
- The `.cursor/rules/agent-os-core.mdc` should be nearly identical across repos; only the done-gate line differs.
