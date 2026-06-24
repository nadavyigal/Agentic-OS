# Executive Dashboard

Manual executive snapshot. Product status remains sourced from
`dashboard/status.json` and project `tasks/progress.md`.

Last updated: 2026-06-24 IDT

## Weekly Review

Latest review: `executive-os/reviews/2026-06-24-portfolio-exec-ceo-plan.md`.

**Decision of the week:** The portfolio is no longer blocked by shipping, it is blocked by credible activation. RunSmart remains primary, but first reconcile the RunSmart live-vs-blocked status contradiction before any Garmin reply. Then investigate RunSmart plan->run drop-off and Resumely real-organic activation before monetization, GTM expansion, or new feature scope.

Sources: `DASHBOARD.md`, `PROJECT-STATUS.md`, `dashboard/status.json`, `executive-os/CEO-OS.md`, `executive-os/EXECUTIVE-METRICS.md`, `PROMPTS/portfolio-exec-ceo-plan.md`.

## Top 3 (week of 2026-06-24)

1. **RunSmart status + Garmin gate:** Confirm exact live App Store build, reconcile RunSmart iOS `tasks/progress.md`, rerun `./agentic-os morning`, and only then prepare the Garmin reply if live evidence matches the submitted screenshots.
2. **Activation diagnosis:** RunSmart plan_generated is 30% (3/10) but run_completed is 0% (0/10); Resumely has approximately 0% real organic activation. Investigate the drop-offs before shipping more scope.
3. **Metrics discipline:** Keep monetization, paid acquisition, and GTM volume paused. Schedule the first true organic RunSmart D7 reread around 2026-06-26 and resolve Resumely person `067544b5` attribution.

## Portfolio Status

- **RunSmart iOS:** Dashboard status is not trustworthy until reconciled. `DASHBOARD.md` and `PROJECT-STATUS.md` say the declared state is blocked on Apple review, but ground truth checks show live App Store state and PostHog live users. D7 activation readout is 0% (0/10 real users), beta cohort caveated.
- **Resumely iOS:** Post-launch D7 Gate A monitoring. `PROJECT-STATUS.md` says app is live with no approval pending. D7 readout is approximately 0% real organic activation, with 3/35 raw completers founder-attributed.
- **RunSmart Web:** Garmin web/backend side complete in the current status narrative, but Garmin reply remains sequenced behind iOS live evidence.
- **ResumeBuilder Web:** ATS scoring accuracy fixes merged; metric-free resume nudge is a future feature decision, not a defect fix.
- **Agentic OS:** Morning refresh works, but portfolio trust is `refresh_required` because the RunSmart contradiction must be reconciled at source.

## Decision Board

Open executive decisions before this run: **0** in `EXECUTIVE-DECISIONS.md`.

New decisions logged:

| ID | Decision | Recommendation | Review |
|---|---|---|---|
| EXD-013 | Response to 2026-06-24 D7 activation readout | Investigate activation now; do not unlock monetization or GTM expansion. | 2026-07-01 |
| EXD-014 | RunSmart live-vs-blocked contradiction before Garmin reply | Reconcile product status and live build evidence before any external Garmin reply. | 2026-06-26 |

Operational decisions:

| Item | Recommendation | Source |
|---|---|---|
| RunSmart plan->run gap | Plan and run a product/instrumentation diagnostic this week. | `EXECUTIVE-METRICS.md`, `PROMPTS/portfolio-exec-ceo-plan.md` |
| Resumely person `067544b5` | Confirm or exclude before claiming any real organic activation. | `PROMPTS/portfolio-exec-ceo-plan.md` |
| ResumeBuilder Web metric nudge | Plan later, after activation diagnosis. | `PROJECT-STATUS.md` |
| Agentic OS auto-heal / strict verify | Defer until current source contradiction is fixed. | `PROJECT-STATUS.md` |

## Plan Progress

- Business + GTM Plan: still `needs_next_packet`, but next packet should be activation learning before acquisition scale.
- RunSmart GTM: do not scale until live build status is reconciled and plan->run is understood.
- Resumely ASO / launch assets: defer until D7 activation diagnosis clarifies whether more traffic would help or just amplify drop-off.
- Monetization plan: model shape remains decided, but implementation remains gated by EXD-009 and EXD-013.

## Risk Board

1. **Activation risk:** RunSmart D7 activation is 0% (0/10 real users, beta cohort); Resumely is approximately 0% real organic. Source: `EXECUTIVE-METRICS.md`.
2. **Status-trust risk:** RunSmart status contradicts ground truth, causing `portfolioTrust.level = refresh_required`. Source: `dashboard/status.json`, `DASHBOARD.md`, `PROJECT-STATUS.md`.
3. **External-communication risk:** Garmin reply could be sent before live build evidence is reconciled. Source: `PROJECT-STATUS.md`.
4. **Revenue/retention blindness:** WAU, retention, paying users, revenue, cost, and runway remain unknown or source-needed. Source: `EXECUTIVE-METRICS.md`.
5. **Stranded-work risk:** Multiple repos still have uncommitted or unmerged work at loss risk. Source: `PROJECT-STATUS.md`.

## Financial Snapshot

- Revenue: `unknown - need: App Store Connect / RevenueCat`
- Paying users: `unknown - need: RevenueCat / App Store`
- Retention: `unknown - need: PostHog retention source`
- Marketing spend: `$0`, tracked
- Paid acquisition: paused by CEO focus rule and EXD-013

## Stop Doing

- Do not treat App Store live status as success without activation.
- Do not start monetization, paywall, RevenueCat, StoreKit, or pricing execution.
- Do not scale ASO / GTM volume into a funnel with approximately 0% real organic activation.
- Do not send Garmin external replies from contradictory status.
- Do not add OS automation while product activation and status reconciliation are waiting.

## Next Actions

1. HUMAN / Release Manager: confirm RunSmart live build state, reconcile RunSmart iOS `tasks/progress.md`, rerun `./agentic-os morning`.
2. RunSmart iOS agent: plan-feature for plan_generated -> run_completed diagnostic and one intervention.
3. Analysis OS: schedule first true organic RunSmart D7 reread around 2026-06-26 with founder and QA/bot exclusions.
4. Analysis OS: classify Resumely person `067544b5`; update D7 readout note.
5. COO OS: rewrite the next GTM packet as activation-learning work, not traffic scaling.

## Research / Opportunity Board

Source: `executive-os/research/2026-06-22-resumely-ats-match-score-positioning.md` and EXD-012.

| ID | Opportunity | Status | Next step |
|---|---|---|---|
| O1 | Reposition score as Resumely Match Score / Match Score | In progress | Keep, but do not let copy polish outrank activation diagnosis. |
| O2 | Anti-myth positioning as marketing wedge | Backlog | Defer until O1 and D7 activation diagnosis are closed. |

## COO Reconciliation Note (2026-06-24)

The prior COO review on 2026-06-21 put Garmin production as the primary unlock. The 2026-06-24 data changes the emphasis: Garmin still matters, but the RunSmart status contradiction must be fixed before external execution, and measured activation is now the portfolio learning gate.
