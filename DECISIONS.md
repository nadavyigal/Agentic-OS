# Global Decisions

Record durable cross-project decisions here. Use `TEMPLATES/decision-template.md`.

## 2026-05-12: Global OS Is A Reference Layer

Decision: The Global Agentic OS is a lightweight reference library and cross-project command center, not a full project operating system.

Reason: Daily coding should happen inside product repos using their local Agent OS files to avoid token waste and stale duplicated context.

Impact:

- Bridge files connect global strategy to local repos.
- Project-specific implementation docs stay local.
- Agents load this folder selectively.

