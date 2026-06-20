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

## 2026-06-05: Escalation Patterns Stay Optional And Outcome-Led

Decision: Keep normal work-packet execution as the default. Use only three
optional workflow patterns (`parallel-research`, `independent-review`,
`evaluator-loop`), treat input trust as a separate security property, and pilot
one evidence-backed outcome loop before creating more.

Reason: The daily OS is intentionally simple. Additional orchestration is useful
only when it improves research coverage, independent review, measurable revision,
or continuity across a real multi-session business outcome.

Impact:

- `Workflow pattern` does not replace Execution mode.
- Untrusted external content is reduced to structured, source-linked facts before
  it can drive actions; session separation alone is not a security boundary.
- Context extraction remains an on-demand founder interview with an approval gate
  before durable promotion.
- Additional outcome-loop cards require two successful COO reviews of the pilot
  without status duplication.

## 2026-06-20: Resumely ATS Claims — Branded "Match Score", Process Claims Only

Decision: Resumely's score is a self-defined "Resumely Match Score", not a representation of any external ATS vendor's score. All ATS-related copy (App Store metadata, paywall, /ats-checker, public share posts) must be process-descriptive, never outcome-guaranteeing.

Reason: The product computes a numeric "ATS score" (free score -> paid export, the core monetization frame) and substitutes it into public LinkedIn posts via LinkedInShareComposer.swift. Real ATS systems (Workday/Greenhouse/Taleo) are proprietary and do not expose scoring, so "your ATS score" is unverifiable and exposes the app to Apple 2.3.1 (misleading) review risk and FTC unsubstantiated-claims risk.

Impact:

- Allowed: "ATS-friendly formatting", "checks against common ATS parsing rules", "match score vs the job you paste", a branded "Resumely Match Score".
- Forbidden: "your ATS score" as an external number, "guaranteed to pass ATS"/"beat the bots", interview/hire outcome stats, named ATS vendors.
- Pending product work (iOS + web repos): rename in-product "ATS score" label to "Resumely Match Score"; update LinkedInShareComposer.swift share copy; audit App Store metadata (en+he); add "not affiliated with any ATS vendor" microcopy.
- Human-readable record: Nadav Builder OS vault 05-Decisions/2026-06-20-resumely-ats-claim-defensibility.md.
