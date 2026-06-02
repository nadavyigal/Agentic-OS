# Global Decisions

Record durable cross-project decisions here. Use `TEMPLATES/decision-template.md`.

## 2026-05-12: Global OS Is A Reference Layer

Decision: The Global Agentic OS is a lightweight reference library and cross-project command center, not a full project operating system.

Reason: Daily coding should happen inside product repos using their local Agent OS files to avoid token waste and stale duplicated context.

Impact:

- Bridge files connect global strategy to local repos.
- Project-specific implementation docs stay local.
- Agents load this folder selectively.

## 2026-06-01: Vet Third-Party Skills Before Install

Decision: Treat any third-party Claude skill as untrusted until reviewed. A skill runs with our tools and credentials, so it is a supply-chain surface.

Reason: The skills ecosystem is growing fast (see `external-resources/06-claude-skills-ecosystem-map.md`). Convenience installs are a real risk.

Impact:

- Read a skill's source before installing; never paste-install on hype.
- Prefer official (`anthropics/skills`) and already-trusted plugins (superpowers, gstack, vercel, supabase, frontend-design).
- Use gstack `cso` skill supply-chain scanning for periodic review of installed skills.

## 2026-06-02: Dashboard Trust Rule

Decision: Global status must be parsed from local project task files when available. Existing `dashboard/status.json` narratives are fallback context, not proof of current status.

Reason: The refresh previously leaned on curated narrative fields that could drift from reality. Parsing local task files (`tasks/progress.md`, then `tasks/todo.md` + latest `tasks/session-log.md` + `tasks/MEMORY.md`) ties each project's state to source evidence and exposes how trustworthy that state is.

Impact:

- The refresh parses local task files and attaches a `taskParse` block plus a `sourceConfidence` rating (High / Medium / Low / Unknown) to every project.
- `tasks/progress.md` is the preferred status source; when absent, status is derived from todo + latest session-log + MEMORY; when no task files exist, the project is marked Low (narrative only) or Unknown (no source).
- High confidence requires parsed validation evidence (passed build/tests/QA). Without it, confidence caps at Medium.
- `PROJECT-STATUS.md`, `DASHBOARD.md`, and `executive-os/EXECUTIVE-DASHBOARD.md` surface the confidence column so a reader can tell parsed truth from narrative.
- Agents must not treat a narrative-only (Low) status as confirmed; re-read the local repo before acting on it.

