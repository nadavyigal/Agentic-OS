# Project Progress

Project: Global Agentic OS
Status: Active
Current Phase: Advanced OS patterns lean pilot
Active Story: Restore dashboard trust and carry current founder work into the daily command surface: both current ASC releases live, Portfolio Activation Playbook V2 plus distribution ranking in progress with Claude Code, and WP-45 S0 implemented on the Resumely iOS branch.
Last Completed Story: Model-routing rollout + Portfolio HQ model tracking (2026-07-10, on main). Merged the two frontmatter PRs (RunSmart #117, ResumeBuilder #113 → `claude-sonnet-5`). Verified all July-2026 pricing independently (claude-api skill + web). Added a **Models** tab to Portfolio HQ: new `dashboard/model-registry.json` (10 models, 4 utilities, 13-row routing matrix), wired through `scripts/portfolio_hq/refresh_portfolio_hq.py`, rendered + verified in-browser. Fixed a real cost bug — `collect_usage.py` priced Opus at Claude-3-era $15/$75 (inflated ~3x); corrected to $5/$25 and re-ran (30d spend now ~$4.4k, was ~$8.6k). Framed routes as "recommendation, not a rule" (GLOBAL-TOOL-USAGE.md) and made the git workflow tool-agnostic for Codex/Cursor (AGENTS.md). Earlier same day: rewrote GLOBAL-TOOL-USAGE.md "Model routing" for the new lineup; added the "Model route" WP-template field; logged DECISIONS.md (two 2026-07-10 entries). Prior on main: Portfolio HQ v3 shipped — generator parses executive-os + distribution-os plus per-workflow last-ran dates; HTML shell rewritten with an orchestrator SVG map. Before that: weekly distribution review (2026-07-09) logged WP-31 + WP-32 and the monthly CFO review.
Next Recommended Story: Finish dashboard-trust reconciliation, push Agentic OS main, then use the refreshed one-move recommendation for today's work.
Estimated Completion: dashboard trust refresh and sync in this session
Blockers: —
Risks: Growth/Executive tabs parse markdown headings (## Active, Top 3 Priorities, Week of YYYY-MM-DD, - Reviewed:) — if those file formats change, the parsers return empty sections rather than failing. WP-31/WP-32 still have real gaps (no asset pack for WP-31, no engagement/ASC log for WP-32) before the 2026-07-12 measurement window closes.
Last Validation: Pending refreshed `./agentic-os morning` after the 2026-07-13 founder evidence reconciliation.
Last Updated: 2026-07-13
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
