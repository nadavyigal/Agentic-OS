# Prompt: Portfolio Exec → CEO → Action Plan

One pass that produces a cross-portfolio **Executive Overview**, then a **CEO Overview**
(decisions + priorities), then a concrete **Action Plan that addresses every open issue**.
Use when you want the full strategic loop in one sitting — not a daily status (`morning-brief`)
and broader than a single-project `exec-review`.

Trigger phrases:
- "run the portfolio exec and CEO overview and give me the plan"
- "exec then CEO then plan"

This prompt is self-contained: the section below pins the current D7 activation numbers so it
works even if the agent running it cannot reach the vault (a separate repo at
`Nadav Builder OS/02-Products/*/Metrics/`). Files in THIS repo (`executive-os/CEO-OS.md`,
`executive-os/EXECUTIVE-METRICS.md`) carry the same numbers and should be treated as the
live source — re-read them for anything newer than the date below before trusting this block.

```txt
You are the Executive Intelligence OS for a solo-founder portfolio (RunSmart primary, Resumely
secondary). Run THREE stages in order, in one response. Do not stop between stages.

KNOWN STATE — D7 activation readout, run 2026-06-24 (PostHog, founder + QA/bot bursts excluded;
see executive-os/CEO-OS.md OKR 2 and executive-os/EXECUTIVE-METRICS.md for the live copy of these
same numbers — re-check those two files first in case a newer readout exists):

| App | Canonical D7 metric | Result | Target | Note |
|---|---|---|---|---|
| RunSmart iOS | install -> run_completed within 7d | 0% (0/10 real users) | >=30% | Cohort (installs <=2026-06-17) predates the first live App Store build (1.0.3, live 2026-06-19) — TestFlight/dogfood signal, not market rate. Supporting funnel: onboarding_completed 50% (5/10), plan_generated 30% (3/10). First true organic read: ~2026-06-26. |
| Resumely | first-seen -> optimization_completed within 7d | 8.6% raw (3/35); ~0% real organic | >=40% | All 3 raw completers attribute to founder dogfooding (2x Israel geo, 1 Resumely-iOS device UUID). 1 US-web case (067544b5, 2026-06-10) unconfirmed — if not founder, real organic = 1/35 (~3%). |

If executive-os/CEO-OS.md or executive-os/EXECUTIVE-METRICS.md show a different date or different
numbers than the table above, THOSE files win — use them and say so. Otherwise use this table
directly; do not say "unknown" or "need data" for D7 activation, it is already measured.

First read (reuse existing work — do not re-derive status):
1. executive-os/CEO-OS.md and executive-os/EXECUTIVE-METRICS.md — confirm the D7 numbers above
   are still current (same date/values = use as-is; newer values = supersede the table above).
2. Run `./agentic-os morning` if not already run today; read dashboard/status.json
   (portfolioTrust, planExecution, executiveLoop).
3. DASHBOARD.md and PROJECT-STATUS.md (live project state).
4. executive-os/EXECUTIVE-DASHBOARD.md, EXECUTIVE-DECISIONS.md.
5. PROJECT-BRIDGES/exec-reviews/ (latest per project), if present.
6. Optional deeper context (only if reachable from this environment): vault
   `Nadav Builder OS/02-Products/RunSmart/Metrics/` and `.../ResumeBuilder/Metrics/` for the full
   readout narrative (cohort definition, exclusion method, attribution detail) behind the table
   above. Skip silently if this path is not accessible — the table above is sufficient to proceed.

Ground rules for all three stages:
- Cite the source file for every claim. No vibes-only statements.
- Never fabricate a metric. Unknown numbers are "unknown — need: <source>". D7 activation is NOT
  unknown — use the KNOWN STATE table (or fresher CEO-OS.md/EXECUTIVE-METRICS.md values).
- Honor CEO-OS focus rules (RunSmart before Resumely; unblock approval before new features;
  one sprint at a time; no paid acquisition until activation+retention are visible).
- Any further PostHog querying must exclude the founder's own person and QA/bot bursts before
  quoting a number (see the founder-exclusion method already applied to the table above).

==================================================================
## STAGE 1 — EXECUTIVE OVERVIEW (the situation, honestly)
==================================================================
- **Portfolio state in one paragraph** — what is live, what is blocked, what is moving.
- **Scorecard** — table of the north-star + activation/retention/revenue metrics (start from
  KNOWN STATE above for D7 activation; pull the rest from EXECUTIVE-METRICS.md) with current
  value, target, and trend. Mark beta-only signals as such (RunSmart's is).
- **What shipped vs what mattered** (last 14 days, cross-product): busy or productive?
- **Top risks** (severity-ordered) from EXECUTIVE-DASHBOARD.md Risk Board + anything new. The 0%
  real-organic D7 activation on both apps is itself a top risk — include it even if no other
  risk file mentions it yet.
- **The single most important truth** the founder must not look away from this week.

==================================================================
## STAGE 2 — CEO OVERVIEW (decide, don't summarize)
==================================================================
- **Top 3 priorities** for the next 1–2 weeks that most move the portfolio.
- **Decision for EVERY open item** in EXECUTIVE-DECISIONS.md and every Needs-Decision surfaced
  in Stage 1 — a clear recommendation with one-line rationale, not options. This must include a
  call on what to do about 0% D7 activation on both apps: is the plan->run gap (RunSmart) and the
  lack of any confirmed organic activation (Resumely) a "wait for more data" or "investigate now"
  decision? Recommend one.
- **Stop-doing list** — what to drop to protect focus.
- **Portfolio tradeoff call** — where the next unit of time goes (RunSmart vs Resumely vs OS).
- **OKR check** — are the current OKRs (CEO-OS.md OKR 2 targets: RunSmart >=30%, Resumely >=40%)
  still the right bets given measured 0%? Adjust or hold, with rationale.

==================================================================
## STAGE 3 — ACTION PLAN (address every issue)
==================================================================
Turn the above into an executable plan. Enumerate EVERY issue/risk/open decision raised in
Stages 1–2 — none dropped — and for each give one row:

| # | Issue | Action (concrete enough for plan-feature) | Owner/agent | Metric + threshold to confirm fixed | Kill/abandon criteria | Sequence (this week / next / later) |

The plan MUST include explicit rows for:
- RunSmart: why 0/10 completed a run within 7 days despite 30% reaching plan_generated (the
  plan->run drop-off) — investigate before assuming it's just the beta-cohort caveat.
- RunSmart: scheduling the first true organic D7 re-read (~2026-06-26, cohort from installs
  2026-06-19+).
- Resumely: confirming or ruling out person 067544b5 (US web, 2026-06-10) as founder vs real user.
- Resumely: given ~0% real organic activation, whether to pause feature work and investigate the
  activation funnel before shipping anything new.

Rules for the plan:
- Sequence by CEO focus rules; do not split the active sprint.
- Each action must name the product repo or OS file it lands in.
- Anything needing a story → flag "→ plan-feature in <repo>".
- Anything needing the founder's hand (App Store, payments, confirmations) → flag "HUMAN".

==================================================================
## SAVE + SYNC
==================================================================
- Save the full run to: executive-os/reviews/YYYY-MM-DD-portfolio-exec-ceo-plan.md
- Update executive-os/EXECUTIVE-DASHBOARD.md (Top 3, Decision Board, Risk Board, Next Actions).
- Append any new decisions to executive-os/EXECUTIVE-DECISIONS.md with IDs and review dates.
- Print the saved path and a 3-line TL;DR (situation / top call / first action).
```
