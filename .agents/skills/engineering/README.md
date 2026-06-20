# Engineering Skills

A thin slice of production-grade engineering skills that the existing libraries (superpowers, gstack) don't cover well: frontend quality, web performance, and observability. Deliberately small to avoid colliding with the TDD/review/debug skills you already run.

## Source & Provenance

- **Upstream:** [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — MIT
- **Adopted:** 2026-06-20, per `docs/research/external-skills-and-tools-adoption-plan.md` (Section 4.4)
- **Slice:** 3 skills + 1 agent of 24 skills / 4 agents. `SKILL.md` / agent `.md` only.
- **Excluded by design:** planning, code-review, debugging, tdd, ship/spec/test, git-workflow, etc. — all duplicate superpowers + gstack (`/review`, `/qa`, `/ship`, `/spec`, `/careful`) and the existing `code-reviewer` / `investigator` agents. Installing them would triple-stack conflicting instructions.

## Security Gate

Scanned with SkillSpector before install (local Docker tool, gitignored under `tools/`):

- **Full upstream repo:** 100/100 CRITICAL — driven by binary-image false positives and the un-adopted skills/agents.
- **This slice, scanned in isolation:** **0/100 — SAFE, no issues, no executables.**

Re-run on any future pull: `docker run --rm -v "$PWD:/scan" skillspector scan ./.agents/skills/engineering/ --no-llm`

## Installed

| Asset | Type | Use for |
|---|---|---|
| `frontend-ui-engineering` | skill | UI component quality on RunSmart / ResumeBuilder web |
| `performance-optimization` | skill | Core Web Vitals, bundle/runtime perf |
| `observability-and-instrumentation` | skill | Logging/metrics/tracing design |
| `web-performance-auditor.agent.md` | subagent | Web performance audit; feeds ResumeBuilder's SEO growth thesis |

## Using the agent

`web-performance-auditor.agent.md` is a Claude Code subagent definition. To use it in a product repo, copy it into that repo's `.claude/agents/` (it is kept here as the global reference copy, not auto-wired).
