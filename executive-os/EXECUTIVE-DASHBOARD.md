# Executive Dashboard

Manual executive snapshot. Product status remains sourced from
`dashboard/status.json` and project `tasks/progress.md`.

Last updated: 2026-06-21 IDT

## Weekly Review

Latest review: daily Agentic OS routine (2026-06-21). Prior formal CEO review: `executive-os/WEEKLY-CEO-LATEST.md` (2026-06-18).

**Decision of the week:** Both iOS apps are live. Primary unlock is RunSmart Garmin production (migration apply + portal gates), not App Store resubmission. Resumely D7 readout ~2026-06-28.

## Top 3 (week of 2026-06-21)

1. **RunSmart Web Garmin production:** Founder approval to apply worker-RPC migration; then manual Gates 2–4 (portal + email). External Garmin approval ~2–4 weeks after submission.
2. **ResumeBuilder Web ATS fix:** Verify LinkedIn guest-scrape fix on Vercel preview IP before merge; do not treat as resolved until preview pass confirmed.
3. **Post-launch monitoring:** RunSmart Garmin readiness Story 1 (TestFlight smoke); Resumely D7 readout on/after ~2026-06-28 (PostHog dashboard 1720819).

## Portfolio Status

- **RunSmart iOS:** LIVE on App Store since 2026-06-19 (v1.0.3 build 16). Post-launch iteration; Garmin readiness active. Early PostHog ~16 users/7d. High confidence.
- **Resumely iOS:** LIVE v1.1 build 5 (founder-confirmed 2026-06-21). D7 Gate A monitoring; readout ~2026-06-28. Medium confidence.
- **RunSmart Web:** Garmin production enablement. Migration #97 merged in code; DB apply needs founder yes. High confidence.
- **ResumeBuilder Web:** ATS LinkedIn scrape fix implemented; awaiting Vercel preview verification. High confidence.
- **Agentic OS:** Status guard contradiction cleared 2026-06-21. 14 stranded-work items. High confidence.

Sources: `PROJECT-STATUS.md` (refreshed 2026-06-21 13:48), `dashboard/status.json`, `COO-LATEST-REVIEW.md` (2026-06-21).

## Decision Board

Open executive decisions: **0** in `EXECUTIVE-DECISIONS.md`.

Operational decisions (not EXD-logged):
- RunSmart Web: apply Garmin migration? → **Recommend yes** after quick rollback review (COO Risk: Yes).
- ResumeBuilder Web: merge ATS fix after preview pass? → **Recommend yes only after preview verification**.
- RunSmart iOS: flip VOICE_COACH_ENABLED? → **PARKED** (founder 2026-06-22). Keep flag false. Re-open after Garmin Story 1 + activation readout; physical voice QA required before flip. Brief: `executive-os/research/2026-06-22-voice-coach-flip-storm-deep-research.md`.

Standing:
- Monetization deferred until D7 readout (EXD-009).
- Brands separate (EXD-007).
- Paid acquisition $0.

## Plan Progress

- Business + GTM Plan: both apps live — reframe to post-launch growth (`needs_next_packet`).
- Pre-Launch Sprint: superseded by live state; extract post-launch ASO packet.
- Resumely Plan 1 (ASO): packetize after D7 readout (~2026-06-28).
- RunSmart GTM: post-launch ASO (rs-aso-001/002) — captions, ratings, conversion.
- Research plans: preserved, not this week.

## Risk Board

- **Garmin migration:** production DB change without staged rollback — mitigate with pre-apply review.
- **LinkedIn ATS on Vercel:** preview IP may differ from production; verify before merge.
- **Revenue/activation:** unknown — need App Store Connect + PostHog D7 readout.
- **Stranded work:** 14 items across repos — branches, worktrees, dirty trees at loss risk.
- **False-positive status guard:** "resubmission" token in phase text triggered prelaunch detection — fixed 2026-06-21.

## Financial Snapshot

- Revenue: `unknown — need: App Store Connect / RevenueCat`
- Activation and retention: `unknown — need: PostHog D7 readout (~2026-06-28)`
- Marketing spend: `$0`, tracked
- Other costs and runway: `unknown — need: provider billing`

## Stop Doing

- No pre-launch / "awaiting App Store approval" positioning — both apps are live.
- No RunSmart App Store resubmission work — build 16 shipped.
- No monetization until D7 readout (EXD-009).
- No Garmin production portal submission until migration applied + Gates 2–4 done.
- No RunSmart voice coach work or `VOICE_COACH_ENABLED` flip while parked (founder 2026-06-22).
- No discarding git work without explicit founder confirmation.

## Next Actions

1. Founder: approve RunSmart Web Garmin migration apply.
2. QA: ResumeBuilder Web LinkedIn scrape verification on Vercel preview.
3. RunSmart iOS: Garmin readiness Story 1 physical TestFlight smoke.
4. ~2026-06-28: Resumely D7 readout (PostHog 1720819).
5. Hygiene: stranded-work sweep (pull Resumely main first; clean empty worktrees).

## COO Reconciliation Note (2026-06-21)

COO and executive views align on bottleneck (Garmin migration approval) and sequence. No disagreement. Prior COO review (2026-06-18) referenced build 16 smoke/archive — **superseded** by live v1.0.3 build 16 on 2026-06-19.
