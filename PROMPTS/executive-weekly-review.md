# Prompt: Executive Weekly Review

Runs the keystone Weekly CEO Review. Cross-portfolio, strategic, synthesizes existing
reviews. Different from `morning-brief` (daily execution status) and `exec-review`
(single-project strategic deep dive) — this consumes both.

Trigger phrases:
- "executive weekly review"
- "run the weekly CEO review"

```txt
You are running the Weekly CEO Review for the Executive Intelligence OS.
Follow executive-os/workflows/weekly-ceo-review.md.

First read (reuse — do not re-collect status):
1. DASHBOARD.md and PROJECT-STATUS.md
2. The latest morning-brief output (or run PROMPTS/morning-brief.md if none is current)
3. PROJECT-BRIDGES/exec-reviews/ (latest per project)
4. distribution-os/weekly-growth-review.md
5. executive-os/EXECUTIVE-DASHBOARD.md, EXECUTIVE-DECISIONS.md, EXECUTIVE-METRICS.md
6. The latest Monthly Finance Review, if current

Then produce, in order:
## Weekly Executive Summary — <date>
- Top 3 priorities (what most moves the portfolio this week)
- Key decisions — a recommendation for EVERY open decision in EXECUTIVE-DECISIONS.md
- Stop-doing list
- Delegation list (priority -> agent/workflow)
- Top risks
- Recommended next actions

Then update executive-os/EXECUTIVE-DASHBOARD.md (Top 3, Decision Board, Risk Board,
Weekly Review, Next Actions) and append any new decisions to EXECUTIVE-DECISIONS.md
with IDs and review dates.

Rules:
- Reuse existing reviews; synthesize, do not re-derive status.
- Recommend decisions, do not just summarize.
- Cite the source file for each claim. No vibes-only claims.
- Do not invent metrics. Unknown numbers are "unknown — need: <source>".
- Respect the focus rules in executive-os/CEO-OS.md (no scope expansion mid-sprint).
```
