# Project Progress

Project: Global Agentic OS
Status: Active
Current Phase: Advanced OS patterns lean pilot
Active Story: Portfolio HQ v3 (branch claude/portfolio-hq-v3, PR #25) — 6-tab redesign: Command (founder-as-orchestrator), Products, Numbers, Growth (reads distribution-os), Executive (reads executive-os), Map with a "Should I run it?" workflow board showing real last-ran dates. Rebased onto main (2026-07-09) so it carries the weekly distribution review's WP-31/WP-32 logging; founder decision session (voice-coach defer, Michal pivot, librarian rejected) recorded on this branch.
Last Completed Story: Portfolio HQ v3 shipped — generator now parses executive-os (WEEKLY-CEO-LATEST, COO review) and distribution-os (experiment log, growth review) plus per-workflow last-ran dates; HTML shell rewritten in plain language with an orchestrator SVG map and run/edit prompts per layer. Prior on main: weekly distribution review (2026-07-09) logged WP-31 (Resumely Hebrew ASO) + WP-32 (Facebook-groups) and the 2026-07-09 monthly CFO review.
Next Recommended Story: Merge PR #25, then run ./agentic-os refresh once to confirm the full pipeline regenerates the new page end to end; run the second COO operating review to close the pilot's validation gate.
Estimated Completion: v3 implementation complete; awaiting merge
Blockers: —
Risks: Growth/Executive tabs parse markdown headings (## Active, Top 3 Priorities, Week of YYYY-MM-DD, - Reviewed:) — if those file formats change, the parsers return empty sections rather than failing. WP-31/WP-32 still have real gaps (no asset pack for WP-31, no engagement/ASC log for WP-32) before the 2026-07-12 measurement window closes.
Last Validation: python3 scripts/portfolio_hq/refresh_portfolio_hq.py exit 0 on 2026-07-09; all 6 tabs rendered in Playwright with zero JS console errors; workflow last-ran dates verified against git/file truth.
Last Updated: 2026-07-09
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
