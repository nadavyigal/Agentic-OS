# Project Progress

Project: Global Agentic OS
Status: Active
Current Phase: Daily portfolio operations and evidence reconciliation
Active Story: Land the completed Resumely seven-story UI/copy pass and prepare 1.4.4; RunSmart 1.1.1 is live and waits on the true first-time Apple sign-in S0.
Last Completed Story: OS instrumentation refinement (2026-07-21). Wired GitHub Actions conclusions into `./agentic-os refresh` via `check_ci_health()`, which immediately surfaced both product eval harnesses as long-running red (RunSmart plan-generator >=11 gated runs since 2026-07-11; ResumeBuilder resume-optimizer >=7 since 2026-07-15). Added `refresh_usage()` so `usage.json` regenerates each refresh instead of going stale, printing the product-vs-meta spend split against the >=60% target (now 27.0%). Added `Rollback` and `Secrets` fields to the work-packet template, with the Maintainer mode contract requiring `Rollback`. 94 parser tests pass (was 75).
Next Recommended Story: Fix the two red eval harnesses — they are the only deterministic quality gates the products have and both have been down for over a week. Start with the RunSmart plan-generator eval (`gh run view --log` on the newest failure; the step fails before writing `report.json`, so check the OPENAI_API_KEY repo secret first). Then, in the Resumely iOS repo, review and merge `claude/session-ec92e2` and prepare 1.4.4.
Estimated Completion: one focused eval-repair session, then Resumely release prep
Blockers: Both product eval harnesses are red (RunSmart >=11 gated runs, ResumeBuilder >=7). Releases that depend on eval evidence have no working gate until these are fixed.
Risks: Growth/Executive tabs parse markdown headings (## Active, Top 3 Priorities, Week of YYYY-MM-DD, - Reviewed:) — if those file formats change, the parsers return empty sections rather than failing. WP-31/WP-32 still have real gaps (no asset pack for WP-31, no engagement/ASC log for WP-32) before the 2026-07-12 measurement window closes.
Last Validation: 2026-07-21 — `./agentic-os test` 94 passed (19 new: CI streak counting, out-of-order runs, PR-noise filtering, truncated streaks, three fail-open paths, spend-split math). `./agentic-os refresh` run end-to-end; CI health and spend split both printed from live data.
Last Updated: 2026-07-21
Latest QA Report: —

<!--
The Agentic OS is markdown-first; "validation" here means ./agentic-os verify passing plus
parser checks, not app build/test. See STATUS-SCHEMA.md for the keys this block exposes and
OS-UPGRADE-PLAN.md for the phased roadmap this progress tracks.
-->

## Decisions Needed

- Should drift detection stay detect-only, or gain a `refresh --reconcile` that auto-heals curated narrative for High projects?
- Should web-repo (RunSmart Web, ResumeBuilder Web) `tasks/progress.md` seeding proceed now or stay on hold?

## Open Questions

- Is the demand-side `INTENT-LOG.md` worth keeping past the 2026-06-16 audit?
- Should `verify` gain a `--strict` mode that fails on drift warnings and evidence gaps?
