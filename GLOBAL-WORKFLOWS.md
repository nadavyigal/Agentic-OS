# Global Workflows

Use these workflows selectively. Daily project implementation should follow the local project OS.

## Universal Product-To-Shipping Workflow

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

## 1. Idea

Capture the raw idea, target user, expected outcome, and why it matters now.

Output: short note or backlog item.

## 2. Product Brief

Turn the idea into a clear product direction.

Output: product brief covering user goal, problem, proposed solution, constraints, success signals, and non-goals.

## 3. Feature Spec

Define behavior, flows, data needs, UI expectations, dependencies, edge cases, and rollout risk.

Output: feature spec.

## 4. Development Stories

Break the feature into small independently testable stories.

Output: story list with acceptance criteria and test plan.

## 5. Implementation Plan

Map stories to files, commands, dependencies, migration needs, and verification steps.

Output: practical implementation plan.

## 6. Validation / QA

Verify acceptance criteria, tests, UI, regressions, edge cases, security, and performance where relevant.

Output: QA report with evidence.

## 7. PR Summary

Summarize what changed, why it changed, how it was tested, and known risks.

Output: PR summary.

## 8. Deployment Review

Review env vars, migrations, rollback notes, monitoring, release timing, and post-release checks.

Output: deployment review.

## 9. Learning / Update Lessons

Capture reusable lessons only when they are likely to matter again.

Output: update to `LESSONS.md`, relevant prompt/workflow, and project-local lessons when applicable.

## Cross-Project Planning Workflow

1. Read `PROJECTS.md`.
2. Read only the relevant bridge files.
3. Define the shared product or technical goal.
4. Identify project-specific source-of-truth files that must be checked later.
5. Produce decisions, stories, or bridges without copying full local docs.

## Project Repo Workflow

1. Read the relevant bridge only if cross-project context is needed.
2. Read local `AGENTS.md`.
3. Read local `CODEX.md` or `CLAUDE.md`.
4. Read local `tasks/lessons.md`.
5. Read only the local workflow file needed for the task.
6. Follow the local project OS as the source of truth.

## Executive Workflows (Layer 8)

Founder-level reviews run on a cadence. They synthesize existing status; they do not
re-collect it. See `executive-os/EXECUTIVE-RHYTHM.md` for the full cadence.

- **Weekly CEO Review** — `executive-os/workflows/weekly-ceo-review.md` (run via
  `PROMPTS/executive-weekly-review.md`). Top 3 priorities, decisions, stop-doing,
  delegation. Consumes `morning-brief`, `exec-review`, `DASHBOARD.md`,
  `PROJECT-STATUS.md`, and `distribution-os/weekly-growth-review.md`.
- **Monthly Finance Review** — `executive-os/workflows/monthly-finance-review.md`
  (run via `PROMPTS/cfo-monthly-review.md`). Financial snapshot from available data
  only; no invented numbers.
- **Analysis Research Sprint** — `executive-os/workflows/research-brief.md` (run via
  `PROMPTS/analysis-research-sprint.md`). Evidence table → scored opportunities →
  recommended next step.

