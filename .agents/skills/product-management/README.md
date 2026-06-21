# Product Management Skills

Structured planning/requirements layer that sits **before** code: PRD → user stories → prioritization → pre-mortem → discovery. Fills the gap between the marketing skills (`.agents/skills/marketing/`) and the engineering libraries (superpowers, gstack).

## Source & Provenance

- **Upstream:** [phuryn/pm-skills](https://github.com/phuryn/pm-skills) — MIT, © 2026 Pawel Huryn
- **Adopted:** 2026-06-20, per `docs/research/external-skills-and-tools-adoption-plan.md` (Section 4.5)
- **Slice:** 8 of 100+ skills — `pm-execution` + `pm-product-discovery` cores only. `SKILL.md` files only (no scripts/assets/evals).
- **Excluded by design:** team-ceremony skills (sprint-plan, stakeholder-map); GTM / market-research / marketing-growth categories (owned by `.agents/skills/marketing/`).

## Security Gate

Scanned with SkillSpector before install (the local Docker tool, gitignored under `tools/`):

- **Full upstream repo:** 100/100 CRITICAL — but every finding was in binary images (`.docs/images/*.png/.webp`, false positives) or the un-adopted `pm-ai-shipping/` category.
- **These 8 skills, scanned in isolation:** **0/100 — SAFE, no issues, no executables.**

Re-run the gate on any future pull: `docker run --rm -v "$PWD:/scan" skillspector scan ./.agents/skills/product-management/ --no-llm`

## Installed Skills

| Skill | Category | Use for |
|---|---|---|
| `create-prd` | execution | Write a PRD before Codex/Claude writes code (the core gap) |
| `user-stories` | execution | Break a PRD into user stories |
| `prioritization-frameworks` | execution | Decide what to build next (RICE, etc.) |
| `pre-mortem` | execution | High-stakes release readiness (e.g. RunSmart Garmin production) |
| `outcome-roadmap` | execution | Roadmap by outcomes, not feature lists |
| `analyze-feature-requests` | discovery | Triage incoming requests from live users |
| `prioritize-assumptions` | discovery | Rank riskiest assumptions before building |
| `interview-script` | discovery | Structure user-research interviews |

## Invocation

Skills self-trigger on their `description` phrases, or invoke by intent: "write a PRD", "run a pre-mortem", "prioritize these feature requests". Pair with the existing planning-protocol and one-story-at-a-time rule.

## Operating Rules

- These skills run before code, ahead of the planning protocol. A PRD or user-stories artifact is the input to implementation, not a substitute for it.
- Honor the global rules: one story at a time, plan before code, no scope creep.
- Every PM artifact is a dated draft file under the relevant repo, for example `tasks/prd-<feature>-YYYY-MM-DD.md`.
- Every PM artifact starts with a header block that includes product, status (`draft`, `reviewed`, or `approved`), and `founder-review-needed`.
- A pre-mortem is mandatory before any high-stakes, hard-to-reverse release, for example RunSmart Garmin production.
- For incoming user feedback now that both apps are live, start with `analyze-feature-requests`, then `prioritize-assumptions`, before committing to build.
