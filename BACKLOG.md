# Global Backlog

Use this for cross-project or global OS work only. Product-specific tasks belong in the local repo.

## Ready

- Execute the Agentic OS Top-Tier Plan (`OS-UPGRADE-PLAN.md`); Phases 0-1 done, Phase 2 next: standardize the status schema so Medium projects can reach High. — Mode: Sweeper
- Create/update local Agent OS files inside RunSmart Web. — Mode: Builder
- Create/update local Agent OS files inside RunSmart iOS. — Mode: Builder
- Create bridge files for new products as they become active. — Mode: Builder

## Later

- **Gated until after 2026-08-01.** Build a contradiction-sweep workflow in `.claude/workflows/`: one agent per executive-layer doc (`EXECUTIVE-DASHBOARD.md`, `WEEKLY-CEO-LATEST.md`, `COO-LATEST-REVIEW.md`, `PROJECT-STATUS.md`), each checking its claims against live git + the fresh dashboard; barrier; report contradictions. Motivated by the 2026-07-21 weekly-plan run, where 3 of 4 executive inputs were stale and the 07-17 CEO review's "no App Store action authorized" was contradicted by two builds shipping 07-20 with nothing noticing. Success criterion: catches a real staleness contradiction the weekly cadence missed; otherwise delete it. Do NOT adopt worktree-isolated fan-out until stranded work is sustained under 20 (61 as of 2026-07-21). Research: Builder OS vault `03-Research/2026-07-21-graph-orchestration-claude-workflows.md`. — Mode: Prototyper
- Audit `INTENT-LOG.md` on or after 2026-06-16: decide keep / promote into the memory system / delete. — Mode: Sweeper
- Define Atlas v0 orchestration scope. — Mode: Prototyper
- Create shared release checklist across web and iOS. — Mode: Maintainer
- Create shared AI output quality rubric for product-facing AI features. — Mode: Maintainer

## Icebox

- Cross-project dashboard for product status, QA, release readiness, and lessons. — Mode: Builder

## Mode Legend

Prototyper | Builder | Sweeper | Grower | Maintainer — see `AGENTS.md` Mode Contracts for what each permits. Untagged items default to Builder.

