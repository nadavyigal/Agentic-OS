# Project Bridge: Atlas

Use this bridge for future orchestration planning. Atlas must coordinate projects, not replace local project Agent OS files.

## 1. Project Identity

Atlas is the future orchestration layer for the product portfolio.

It is not the first place to implement product code.

## 2. Role In The Larger Vision

Atlas should become the control layer for product, engineering, QA, growth, and monetization agents across RunSmart Web, RunSmart iOS, ResumeBuilder AI, and future products.

It should coordinate tasks, context, specs, QA, and workflows while keeping each project repo as the source of truth.

## 3. Responsible For

- Cross-project task coordination.
- Context routing.
- Spec and story coordination.
- QA and release readiness visibility.
- Shared workflow orchestration.
- Agent role coordination.
- Lesson and decision routing.
- Portfolio-level product, engineering, QA, growth, and monetization visibility.

## 4. Not Responsible For

- Direct product code implementation at first.
- Replacing local Agent OS files.
- Storing secrets or credentials.
- Centralizing full project documentation.
- Inventing project APIs or sync behavior.
- Forcing every project into one rigid workflow.

## 5. Relationship To Other Projects

- Atlas reads from local project OS files as source of truth.
- Atlas may summarize, route, and coordinate work across projects.
- Atlas should know that RunSmart Web is the current product capability reference for RunSmart.
- Atlas should know that RunSmart iOS is a native mobile translation, not a web copy.
- Atlas should know ResumeBuilder is separate from RunSmart except for reusable agent workflows.
- Atlas must not create duplicated business logic without documenting why.

## 6. Source-Of-Truth Files Inside The Local Repos

Atlas should route agents toward each repo's local source of truth:

- `AGENTS.md`
- `CODEX.md`
- `CLAUDE.md`
- `tasks/lessons.md`
- Relevant `tasks/` files
- Relevant `.agent-os/` files
- Repo-specific source files only after a scoped task requires them

Atlas should not cache or duplicate full local project docs unless a future design explicitly proves that is necessary.

## 7. Local Agent OS Files Agents Must Read

For Atlas work itself, read local Atlas files first once an Atlas repo exists:

- `AGENTS.md`
- `CODEX.md`
- `CLAUDE.md`
- `tasks/lessons.md`
- Relevant `tasks/` files
- Relevant `.agent-os/` files

For coordinated work in another project, read that project's local OS before making implementation recommendations.

## 8. Global OS Files Agents May Reference

Use selectively:

- `PROJECT-BRIDGES/atlas.md`
- Relevant project bridge files only for projects being coordinated.
- `PROJECTS.md` for portfolio overview.
- `GLOBAL-STANDARDS.md` for shared standards.
- `GLOBAL-WORKFLOWS.md` for cross-project workflow.
- `GLOBAL-AGENT-RULES.md` for agent behavior.
- `GLOBAL-SELF-IMPROVEMENT.md` for lessons routing.

Do not load every bridge by default.

## 9. Product Priorities

- Prove the orchestration workflow manually before building automation.
- Make cross-project work easier to plan, route, QA, and learn from.
- Keep the system lightweight and useful.
- Help agents know what context to load and what to ignore.

## 10. Engineering Priorities

- Start with documentation and workflow coordination.
- Avoid direct product code changes at first.
- Use local project OS files as source of truth.
- Keep context routing explicit and token-efficient.
- Design for auditability: what context was used, what decision was made, and what evidence supports it.

## 11. UX Priorities

- Atlas should feel like a control layer, not another noisy dashboard.
- Prioritize clarity, status, next actions, blockers, and evidence.
- Make it easy to see which project owns a task.
- Avoid hiding local repo truth behind global summaries.

## 12. QA Expectations

- Atlas outputs should cite which local OS files or bridges were used.
- Cross-project recommendations must identify assumptions and required repo checks.
- Workflow changes should include small examples.
- Any future Atlas automation needs rollback/disable notes.

## 13. Risk Areas

- Replacing local project truth with stale global summaries.
- Loading too much context.
- Inventing project capabilities.
- Over-centralizing secrets, docs, or decisions.
- Creating fake certainty across repos.
- Turning orchestration into heavyweight process.

## 14. What Agents Must Never Do

- Do not implement product code directly from Atlas at first.
- Do not replace local project OS files.
- Do not assume APIs exist without checking the relevant repo.
- Do not invent sync behavior for Garmin, Apple Health, or background GPS.
- Do not mix ResumeBuilder with RunSmart product logic.
- Do not load every project file for routine tasks.
- Do not store secrets or private credentials.

## 15. Example Prompts

```txt
Using Atlas as a coordination layer, route this cross-project idea into the correct project bridge, local repo files to inspect, likely stories, QA expectations, and open assumptions.
```

```txt
Create a portfolio status summary from the relevant project bridges and local OS summaries only. Do not infer implementation status without repo evidence.
```

```txt
Design a small manual Atlas workflow for coordinating Web-to-iOS product logic adaptation without copying UI or duplicating business logic.
```

## 16. How To Update This Bridge

Update this bridge after major changes to:

- Atlas scope.
- Cross-project routing rules.
- Agent role responsibilities.
- Manual workflows that are proven enough to automate.
- Lessons routing.
- Portfolio-level QA or release process.

Keep Atlas lightweight until repeated manual workflows justify automation.

## 17. Token-Efficiency Guidance

- Load only the bridges for projects involved in the task.
- Prefer summaries of local OS files over full project context.
- Route agents to local repos for implementation details.
- Avoid centralizing full project docs in Atlas.
- Treat Atlas as a coordinator, not a giant context warehouse.

