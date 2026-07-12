# Project Progress

Project: Global Agentic OS
Status: Active
Current Phase: Advanced OS patterns lean pilot
Active Story: Reconcile main + end-of-day close rail (branch claude/agentic-os-reconcile-and-eod, PR #27). (1) Local main had diverged: 12 Codex commits (sites/portfolio-hq, plugins/founder-os, cli.py refactor, tests) vs origin's daily-note habit rail (daily_note.py, generate_brain_map.py, refresh wiring from PR #26/#31). Merged origin into main — clean, both bodies survive (big divergences were added-on-one-side-only); removed 8 untracked iCloud " 2" dedup files. Daily-note habit now live on local main, so tomorrow's ./agentic-os morning fires it. (2) Built eod_close.py + ./agentic-os eod — evening bookend to daily_note.py: drafts today's note's End-of-Day block from today's git commits across all 6 repos + Claude Code sessions, with Moved/Didn't/Carry and one manual Cursor line; Carry lines stay in the inline format daily_note.carried_lines() reads next morning (loop closed + tested).
Last Completed Story: Model-routing rollout + Portfolio HQ model tracking (2026-07-10, on main). Merged the two frontmatter PRs (RunSmart #117, ResumeBuilder #113 → `claude-sonnet-5`). Verified all July-2026 pricing independently (claude-api skill + web). Added a **Models** tab to Portfolio HQ: new `dashboard/model-registry.json` (10 models, 4 utilities, 13-row routing matrix), wired through `scripts/portfolio_hq/refresh_portfolio_hq.py`, rendered + verified in-browser. Fixed a real cost bug — `collect_usage.py` priced Opus at Claude-3-era $15/$75 (inflated ~3x); corrected to $5/$25 and re-ran (30d spend now ~$4.4k, was ~$8.6k). Framed routes as "recommendation, not a rule" (GLOBAL-TOOL-USAGE.md) and made the git workflow tool-agnostic for Codex/Cursor (AGENTS.md). Earlier same day: rewrote GLOBAL-TOOL-USAGE.md "Model routing" for the new lineup; added the "Model route" WP-template field; logged DECISIONS.md (two 2026-07-10 entries). Prior on main: Portfolio HQ v3 shipped — generator parses executive-os + distribution-os plus per-workflow last-ran dates; HTML shell rewritten with an orchestrator SVG map. Before that: weekly distribution review (2026-07-09) logged WP-31 + WP-32 and the monthly CFO review.
Next Recommended Story: Merge PR #27, then run ./agentic-os morning once to confirm the reconciled pipeline regenerates dashboards AND fires the daily-note habit end to end. (Older: PR #25 Portfolio HQ v3 still open.)
Estimated Completion: reconcile + eod complete and verified; awaiting PR #27 merge
Blockers: —
Risks: Growth/Executive tabs parse markdown headings (## Active, Top 3 Priorities, Week of YYYY-MM-DD, - Reviewed:) — if those file formats change, the parsers return empty sections rather than failing. WP-31/WP-32 still have real gaps (no asset pack for WP-31, no engagement/ASC log for WP-32) before the 2026-07-12 measurement window closes.
Last Validation: Reconcile + eod (2026-07-12) — `python3 -m unittest test_cli test_eod_close` = 83 pass (68+15); cli.py parses; merge kept both bodies (daily_note.py + generate_brain_map.py + sites/portfolio-hq + plugins/founder-os all present, cli.py carries both wirings). Live: `./agentic-os eod` drafted today's real note (15 commits / 3 repos / 1 Claude project), idempotent re-run confirmed, `--force` redraft works, carry-forward loop verified (daily_note.carried_lines reads the Carry line). daily_note.py + generate_brain_map.py both exit 0.
Last Updated: 2026-07-12
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
