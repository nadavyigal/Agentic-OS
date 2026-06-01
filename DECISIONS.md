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

