# Global Agentic OS

This folder is the global operating layer for how I build AI-powered products across projects.

It is a reference library and cross-project command center for Claude Code, Codex, Cursor, and future agents. It is not meant to be loaded fully for every task.

Use this OS when work spans multiple products, shared standards, project bridges, reusable prompts, global lessons, or Atlas-style orchestration.

For daily implementation inside a product repo, use that repo's local OS files as the source of truth.

## Active Products

- RunSmart Web: main AI running coach web product and source of current product logic.
- RunSmart iOS: native SwiftUI mobile version of RunSmart.
- ResumeBuilder AI: AI resume optimization product.
- Atlas: future orchestration layer across products, agents, specs, QA, and workflows.

## Universal Workflow

```txt
Idea
-> Product Brief
-> Feature Spec
-> Development Stories
-> Implementation Plan
-> Validation / QA
-> PR Summary
-> Deployment Review
-> Learning / Update Lessons
```

## How To Use Inside A Project Repo

1. Read the global bridge file only if cross-project context is needed.
2. Read the local `AGENTS.md`.
3. Read local `CODEX.md` or `CLAUDE.md`.
4. Read local `tasks/lessons.md`.
5. Read only the local workflow file needed for the task.
6. Follow the local project OS as the source of truth.

## How To Use Inside This Global OS

Use this folder for:

- Cross-project planning
- Bridge creation
- Shared standards
- Reviewing product strategy
- Creating reusable prompts
- Updating global lessons
- Defining Atlas-like orchestration

Do not use this folder for:

- Normal daily code changes inside a specific project
- Reading every project file every time
- Replacing local project OS files

## Folder Map

- `PROMPTS/`: reusable prompts for planning, implementation, QA, PRs, onboarding, bridges, and lessons.
- `PROJECT-BRIDGES/`: short bridge files explaining how each product connects to the global vision.
- `TEMPLATES/`: lightweight templates for briefs, specs, stories, QA, PRs, decisions, lessons, and bridge files.
- `SKILLS/`: reusable agent role definitions for multi-agent work.

