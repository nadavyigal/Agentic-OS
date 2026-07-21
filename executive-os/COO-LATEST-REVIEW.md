# COO Operating Review - 2026-07-21

- Status: current
- Reviewed: 2026-07-21
- Selected next action: **WP-51 — repair the Resumely activation milestone (`optimized_preview_rendered`) before the 2026-08-01 EXD-015 verdict.**
- Action type: local-repo (Resumely iOS)
- Source: `DASHBOARD.md`, `PROJECT-STATUS.md`, `dashboard/status.json` (refreshed 2026-07-21 20:04), `dashboard/portfolio-hq-manual.json` (PostHog layer refreshed 2026-07-21), live PostHog reads projects 171597 + 270848 (2026-07-21, both fingerprinted before reading), Apple lookup API (2026-07-21), `executive-os/COO-OS.md`, `executive-os/workflows/coo-operating-review.md`, `executive-os/templates/work-packet-template.md`, Builder OS `2026-07-21-weekly-review`.
- Revisit when: WP-51 lands and a fresh 14-day funnel reads monotonic; or 2026-08-01, whichever comes first.
- Supersedes: COO Operating Review 2026-07-12 (WP-32 closed inconclusive, WP-31 named as next).

## 1. Operating Summary

Both apps are live and store-verified: RunSmart iOS **1.1.1 (25)** since 2026-07-20T20:38:19Z, Resumely **1.4.3 (13)** since 2026-07-19T21:47:02Z with 1.4.4 (14) merged but not submitted. Execution over the last fortnight was overwhelmingly **measurement repair rather than product** — WP-46, WP-47, WP-48, WP-50, the WP-51 instrumentation, two autopsies, and eval harnesses across both repos.

That investment paid out on 2026-07-21, and the payout was bad news twice. RunSmart's new instrumentation caught **Sign in with Apple failing 5/5 with `ASAuthorizationError` code 1000 on the live public binary** (real App Store install; `$is_testflight`/`$is_sideloaded`/`$is_emulator` all false), which closes the open outage-versus-persuasion question in favour of outage. Resumely's funnel became readable and immediately returned a **non-monotonic** result — more people export than render a preview — meaning the activation milestone itself is defective.

Net operating position: **0 active work packets, 52 total.** Three plans sit at `needs_next_packet` and all three are GTM/distribution, which is the wrong thing to packetize while both funnels are broken. The portfolio is not blocked on capacity or sequencing; it is blocked on two specific defects.

## 2. Loop Needing Attention

**No registered loop needs attention.** The only registered loop, `resumely-submission`, is closed and its close condition (Ready for Sale + launch analytics verified) still holds.

Flagged for the next CEO review rather than acted on here: there is no registered loop covering **activation measurement integrity**, which is now the third consecutive review where a measurement defect has been the binding constraint. That is a loop-shaped problem currently handled as a series of one-off packets.

Evidence: `dashboard/status.json` `osRegistry.outcomeLoops`; `executive-os/loops/resumely-submission.md`.

## 3. Plans Needing Packets

| Plan | Source | Next milestone to packetize |
|---|---|---|
| Business + GTM Plan v0 | Source: `executive-os/BUSINESS-GTM-PLAN-V0.md` | **No packet now.** Both funnels are confirmed broken as of 2026-07-21; GTM effort compounds the loss. Revisit after WP-51 and the RunSmart gate decision. |
| RunSmart Hebrew-First Distribution Playbook | Source: `docs/superpowers/plans/2026-06-22-runsmart-hebrew-first-distribution-playbook.md` | **No packet now.** Parked by EXD-016 until 2026-08-01, and independently blocked: driving Hebrew traffic into a sign-in wall that returns a hard Apple error is value-destroying. |
| GTM Plan — RunSmart iOS | Source: RunSmart iOS `.agent-os/distribution/gtm-plan.md` | **No packet now.** Blocked on the same P0. Cannot produce a measurable result until the gate opens. |

All three are correctly flagged by the dashboard and all three are correctly deferred. The `needs_next_packet` status is not drift; it is a standing invitation the COO is declining on evidence.

## 4. Current Bottleneck

**Resumely's activation milestone is defective and the EXD-015 verdict is 11 days away.**

`optimized_preview_rendered` fires for 3 people across 60 days while both `optimization_completed` and `export_success` exceed it. The 2026-08-01 review will otherwise arrive with no verdict possible — for a measurement reason, not a product reason, for the fourth time this month.

**Owner of the unblock:** Resumely iOS engineer, via WP-51.

RunSmart's confirmed sign-in outage is the more severe defect in absolute terms, but RunSmart is secondary by standing decision (EXD-015), and its next step is a product-shape choice the COO does not own — see escalation.

## 5. Next Execution Sequence

1. **WP-51 — repair `optimized_preview_rendered`** *(local-repo, Resumely iOS)*. The only work that changes whether 2026-08-01 produces an answer. Packet attached.
2. **CEO decision on RunSmart's gate** *(manual-founder)*. Repair the Apple configuration chain, or ship a guest path. Do not start either until decided — they are different products, not different tasks.
3. ~~Resumely 1.4.4 submission~~ **— done. Founder confirmed 2026-07-21 that 1.4.4 (14) is submitted and under ASC review** (Match Score language, honest locked screens, corrected share/Terms/Privacy links, fixed "Create free account" routing, full Hebrew, layout polish). This **raises** WP-51's urgency rather than lowering it: 1.4.4 carries no measurement fix, so approval resets the exact-version cohort clock and starts a fresh cohort measured by a milestone that under-fires. WP-51 must be ready to ship as 1.4.5 on approval.
4. ~~Resolve the 1.4.4 field anomaly~~ **— explained.** The 1.4.4 events in PostHog are consistent with pre-submission/TestFlight validation of the build now under review, not an unrecorded release. No packet needed; confirm the persons carry `is_internal_tester` on the next cohort read.
5. **Stranded-work sweep** *(global-OS)*. 62 items, concentrated in RunSmart iOS: `main` 8 behind origin plus 5 local-only `claude/*` branches with deleted remotes. `./agentic-os clean --apply` handles the agent branches. Low urgency, non-blocking.

## 6. CEO Escalation Needed: **Yes**

Two decisions, both genuinely CEO-owned:

**(a) RunSmart: repair Apple, or route around it?** The sign-in outage is confirmed on the live binary. Repairing the Apple Developer chain fixes one gate; shipping a guest path to plan generation removes Apple from the activation critical path permanently. Resumely already proves the second pattern works in this portfolio — and did so by accident, as a June workaround to this same Apple failure (Builder OS `2026-07-21-apple-signin-cross-product-pattern`). This changes RunSmart's product shape and its resourcing against a standing "RunSmart is secondary" decision, so it is not a COO call.

**(b) EXD-015's target is not testable as written.** "20% activation by 2026-08-01" has n=12 over 30 days. Even with a perfectly working milestone, that sample cannot distinguish 8% from 30%. The target needs restating in terms current volume can test, or the window needs extending, or the decision needs to rest on something other than this metric. Deciding to measure something unmeasurable is the failure mode worth naming before 08-01, not after.

## 7. CFO Escalation Needed: **No**

No pricing, budget, or unit-economics decision is live. Monetization remains correctly gated behind activation evidence that does not yet exist.

## 8. Analysis Needed: **No**

The diagnosis is complete for both defects. What is missing is execution and one product decision, not further research. Explicitly: do **not** commission competitor or market analysis this cycle — the constraint is internal and identified.

## 9. Risk Review Needed: **No**

Flagged but not escalated: RunSmart has a confirmed production outage blocking first-time sign-up. Severe, but it has a named owner, a named hypothesis, and a decision routed to CEO. It becomes a Risk OS item if the CEO decision stalls past one week, or if the Apple configuration turns out to affect Resumely's re-enablement path too.

## 10. Exact Decision Required

> **RunSmart's sign-in gate: repair the Apple Developer configuration chain (App ID SIWA capability → Services ID → private key → Supabase Authorized Client ID), or ship a guest path to plan generation and remove Apple from activation entirely?**
>
> Prior art favouring the second: the 2026-06-10 Resumely decision shows this portfolio has already hit this exact chain once, could not complete the Services ID / private key setup in-session, chose to route around it, and that choice is the reason Resumely's funnel is readable today.
>
> **And:** restate EXD-015's 20%-by-08-01 target in terms n=12 can actually test, or extend the window.

## 11. Work Packet

**WP-51 — Repair the Resumely activation milestone.** Full packet: `executive-os/work-packets/WP-51-resumely-fix-activation-milestone.md`

- Project: Resumely iOS
- Signal: non-monotonic funnel on the canonical WP-50 contract (12 → 7 → 1, with 3 exporters)
- Success signal: `optimized_preview_rendered` person-count ≥ `export_success` person-count; funnel monotonic on a fresh 14-day read
- Loop: Resumely activation measurement loop
- Rollback: revert the instrumentation commit; analytics-emission surface only

## 12. What Not To Touch

- **Any GTM, distribution, ASO, or acquisition work.** All three `needs_next_packet` plans stay unpacketized. Both funnels are broken; traffic effort compounds the loss.
- **The WP-50 denominator decision.** Settled, twice-reviewed, correct.
- **RunSmart FTUX copy, onboarding polish, or E1 experiment assignment.** All sit downstream of a gate that returns a hard error. They cannot produce a readable result and will consume capacity while appearing productive.
- **Adaptive Coach Phase 2.** Its gate (2 weeks live AND ≥20 real `adaptive_coach_shown` users) is arithmetically unfillable at current entry volume.
- **The 1.4.4 archive/upload.** Founder-triggered only, and should follow WP-51.
- **The `is_internal_tester` classifier defect.** Real, tracked, but not on the critical path to 08-01.
