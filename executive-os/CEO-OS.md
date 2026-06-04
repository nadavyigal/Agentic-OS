# CEO OS

> **Not daily** — route here for weekly CEO review, portfolio tradeoffs, and OKRs. Daily path: `DAILY.md` → `./agentic-os morning`.

## Purpose

The CEO OS is responsible for strategic focus, goals, priorities, operating rhythm,
decision-making, accountability, and portfolio-level tradeoffs. It is where the
founder decides what matters most across the whole portfolio and what to ignore.

It is run by `agents/ceo-agent.md` (owns focus, OKRs, decisions, tradeoffs) and
operated by `agents/chief-of-staff-agent.md` (turns priorities into rhythm, agendas,
and follow-ups). CEO outputs must **recommend decisions, not just summarize.**

## Mission

Build AI-powered products that are useful, polished, and trustworthy, and turn them
into a sustainable solo-founder portfolio. RunSmart is primary; Resumely is
secondary.

## Product Portfolio

| Product | Role | Stage focus |
|---|---|---|
| RunSmart iOS | Primary; premium native mobile | App Store approval (submit-ready, build 6) |
| RunSmart Web | Source of product logic | Stability, UX, integrations, monetization |
| Resumely iOS | Secondary native app | Pre-submission: copy + analytics pending |
| ResumeBuilder Web | Resume optimization product | Output quality before monetization |
| Atlas | Future orchestration layer | Cross-project coordination (not yet active) |

## What The CEO OS Manages

- **Mission & focus rules** — what we are and are not doing this quarter.
- **Quarterly OKRs** — via `templates/okr-template.md`.
- **Weekly priorities** — top 3, set in the Weekly CEO Review.
- **Decision board** — `EXECUTIVE-DECISIONS.md`.
- **Stop-doing list** — what to drop to protect focus.
- **Delegate-to-agents list** — what the agents should work on next.
- **Human-judgment list** — what must not be delegated.
- **Portfolio tradeoffs** — where to spend the next unit of time across the products
  above.

## Focus Rules (default)

1. RunSmart before Resumely when they compete for time.
2. Unblock App Store approval before starting new feature work.
3. One submission sprint at a time; do not split the sprint.
4. Manual operating rhythm before any automation.
5. No new paid-acquisition spend until activation and retention are visible.

## Workflows

Phase 1 (live):

- Weekly CEO Review — `workflows/weekly-ceo-review.md` (keystone)

Phase 2 (tracked in `EXECUTIVE-BACKLOG.md`):

- Quarterly OKR Review
- Executive Decision Review
- Portfolio Prioritization

## Quarterly OKRs

_First draft set 2026-05-31. Review cadence: weekly check / monthly score / quarterly close._
_All KR metrics follow the format: value known / unknown — need: \<source\>._

---

### OKR 1 — Submission Sprint (Q2 2026: May–June)

- **Quarter:** Q2 2026
- **Objective:** Get both iOS apps approved and live on the App Store before the end of June.
- **Why it matters:** No revenue, no activation data, and no distribution until at least one app is
  live. Shipping is the single gate blocking everything else.

| # | Key Result | Metric | Baseline | Target | Source |
|---|---|---|---|---|---|
| 1 | RunSmart iOS approved and visible on App Store | Approval status | Not submitted | Approved + live | App Store Connect portal |
| 2 | Resumely iOS submitted for review | Submission status | Not submitted | Submitted (approval pending) | App Store Connect portal |
| 3 | PostHog receiving events from both apps before their first day live | Event receipt confirmed | RunSmart: token unverified; Resumely: no SDK | Both apps firing ≥ 3 events in PostHog | PostHog dashboard |

- **Owner:** Nadav
- **Projects involved:** RunSmart iOS, Resumely iOS
- **Risks:** App Store approval delay (typically 24–72 h, up to 14 days on rejection); Resumely
  PostHog integration can slip if scope expands.
- **Review cadence:** Check daily during portal close-out; score at Q2 close (2026-06-30).

---

### OKR 2 — Post-Launch Activation (Q3 2026: July–September, first draft)

- **Quarter:** Q3 2026
- **Objective:** Turn the first wave of App Store users into engaged, retained runners and resume
  builders who complete the core action at least once.
- **Why it matters:** Downloads without activation are vanity. The first cohort must validate product
  fit before paid-acquisition spend or feature expansion is justified.

| # | Key Result | Metric | Baseline | Target | Source |
|---|---|---|---|---|---|
| 1 | RunSmart iOS: % of new installs who complete a GPS run within 7 days of install (D7 activation) | D7 activation rate | unknown — need: PostHog + App Store Connect installs | ≥ 30% | PostHog funnel: install → run_completed |
| 2 | Resumely iOS: % of new installs who complete an optimization within 7 days (D7 activation) | D7 activation rate | unknown — need: PostHog + App Store Connect installs | ≥ 40% | PostHog funnel: install → optimize_completed |
| 3 | At least 1 paid subscriber across the portfolio (first revenue signal) | Paid subscription count | 0 | ≥ 1 | App Store Connect / RevenueCat |

- **Owner:** Nadav
- **Projects involved:** RunSmart iOS, Resumely iOS, RunSmart Web, ResumeBuilder Web
- **Risks:** Both apps may not be approved in time for Q3 data; activation targets are guesses
  without baseline data — treat as directional until post-launch week 1 data is available;
  monetization model not yet defined (Needs Decision per Monetization Board).
- **Review cadence:** Weekly check starting week 2 post-launch; score at Q3 close (2026-09-30).

---

## Rules

- Recommend a decision for every open question; do not stop at a summary.
- Cite evidence from the dashboard, project status, and decisions log.
- Mark unknown metrics `unknown — need: <source>`; never fabricate.
- Every important strategy/product/pricing/budget choice gets a row in
  `EXECUTIVE-DECISIONS.md`.
