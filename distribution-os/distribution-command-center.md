# Distribution Command Center

The single page that answers: what is this week about, what is shipping, what is blocked. Update at the start and end of every distribution cycle. The Notion Command Center database mirrors this — Notion is the dashboard, this file is the source the agent reads.

## This Week

- **Week of**: 2026-06-29
- **Focused product**: ResumeBuilder iOS (Resumely) — post-launch outreach restart
- **Other product status**: RunSmart — v1.0.3 (16) live on the App Store since 2026-06-19; maintenance only this week, no active distribution push
- **Theme**: Reconcile drifted marketing copy against the locked Fit/Match positioning, then run zero-budget 0-10 user outreach (personal DM, vibecoding FB group, LinkedIn job-seeker groups) now that v1.2 (7) is live
- **Top experiments this cycle**:
  1. Reconciled all reusable Resumely outreach templates (email, LinkedIn personal post, Reddit, Slack/Discord, ASO metadata, screenshot briefs, launch-day posts, content calendar) to Fit/Match language and the real App Store link — **done 2026-06-29**
  2. Hebrew DM + FB (vibecoding israel) + LinkedIn (job-seeker groups) outreach copy drafted for founder to send personally — **ready, no paid spend**
  3. Distribution-os restart: command center and project bridge were frozen at pre-launch state (last touched 2026-05-28); refreshed to reflect both apps live — **done 2026-06-29**
  4. rb-dir-001 directory pack rewritten from stale "ATS score" framing to Fit/Match copy; real App Store URL (id6776752349) substituted for the placeholder; score rescored 15 -> 17 to match `channel-backlog.md` — **done 2026-06-29, awaiting founder review**
- **Assets in flight**:
  - `new-ResumeBuilder-ai-/launch-assets/*` — rewritten, Fit/Match positioning, real App Store link substituted for placeholders and the old web-tool link
  - `ResumeBuilder IOS APP/launch-assets/aso/screenshot-briefs.md` — synced to drop "ATS score" framing, matches `.agents/product-marketing.md`
  - Hebrew outreach messages (DM/FB/LinkedIn) — drafted in chat this session, not yet filed as a Drive asset
  - `projects/resumebuilder/scaffold/drafts/2026-05-28-rb-dir-001/directory-pack-v1.md` — rewritten to Fit/Match copy, real App Store URL inserted, ready for founder review before submission
- **Awaiting founder action**:
  - Send the personal DM, FB post (vibecoding israel group), and LinkedIn posts (job-seeker groups) manually — founder publishes, not the OS
  - Confirm exact FB/LinkedIn group names (could not verify current real group names/membership by search; founder has access)
  - Review and approve the rewritten rb-dir-001 directory pack, then submit to the 5 directories one at a time
  - Decide whether to reconcile the web repo's free ATS-checker tool (`/api/ats/score`, `/api/public/ats-check`, `resumelybuilderai.com` framing) to Fit/Match language, or keep it as an intentionally distinct "ATS score" free-tool funnel feeding the iOS app — still open, not decided by this OS
- **Awaiting external response**: first 0-10 organic Resumely users from this outreach wave
- **PostHog read (2026-06-29, project 270848)**: app_launched 55 -> 117, resume_uploaded 12 -> 76, optimization_completed 29 -> 48 (current 14-day window vs prior 14-day window) — directional only, low sample size (single digits to low teens per day). The zero-budget outreach wave itself only started today; only 1 partial day of post-outreach data exists (1 app_launched, 0 of everything else on 6/29) — too early for any signal.
- **Blocked**:
  - `docs/gtm/week-1-*` and `canonical-90-day-plan.md` in the web repo are dated, pre-launch (2026-02-14/16) historical execution logs — intentionally NOT rewritten; they document what was actually sent at the time. Per `operating-principles.md` Principle 6, `.agents/product-marketing.md` wins for product facts going forward; these are left as historical record, not a competing source of truth.
  - RunSmart distribution work — paused this week per Principle 4 (one product in focus)

## Current Channel Status

### RunSmart

| Channel | Status | Owner Of Next Step | Notes |
|---|---|---|---|
| ASO | live, v1.0.3 (16) | Founder — monitor reviews/ratings | Live since 2026-06-19; no active iteration this week |
| All other channels | maintenance | — | Paused this week; RunSmart gets focus a different week per Principle 4 |

### ResumeBuilder (Resumely)

| Channel | Status | Owner Of Next Step | Notes |
|---|---|---|---|
| ASO | live, v1.2 (7) | Founder — monitor reviews/ratings | Live since 2026-06-29; Fit-First + Resumely Match Score rebrand now visible in-app, matching ASO copy for the first time |
| Personal outreach (DM) | ready | Founder — send | Hebrew template ready, real link included |
| FB community (vibecoding israel) | ready | Founder — post + confirm group name | Hebrew post ready |
| LinkedIn job-seeker groups | ready | Founder — post + confirm 1-2 group names | Hebrew post ready |
| Web launch-assets (email/LinkedIn/Reddit/Slack templates) | reconciled | Founder — reuse as needed | All rewritten to Fit/Match, 2026-06-29 |
| Directories | unknown status | Agent — re-check rb-dir-001 next cycle | Was blocked pre-launch on App Store URL; URL now exists, re-score next cycle |
| Hebrew market | live in-app | — | RTL + Hebrew support shipped in v1.1 (5), Hebrew ASO metadata locked 2026-06-28 |
| Web → App Store funnel reconciliation | not started | Agent — next focus week | Web repo's free ATS-checker tool (resumelybuilderai.com) still frames itself around "ATS score," separate from the iOS Fit/Match rebrand; not reconciled this cycle, flagged as next open item |

Status values: `not started` · `planned` · `in progress` · `awaiting review` · `approved` · `published` · `measuring` · `learned` · `paused` · `killed`

## Last Cycle's Decisions

- 2026-06-29 (mid-cycle): rb-dir-001 rescored 15 -> 17 and rewritten to Fit/Match copy now that the App Store URL exists; PostHog checked for early outreach signal (none yet, outreach started same day).
- 2026-06-29: Resumely v1.2 (7) confirmed live by founder — Fit-First visible, Resumely Match Score rebrand, Hebrew/RTL, WP-18 upload-funnel instrumentation now in production.
- 2026-06-29: Canonical Resumely positioning (`.agents/product-marketing.md`) is the single source of truth when web-repo and iOS-repo marketing copy disagree.
- 2026-06-29: Zero-budget, founder-time-limited (2-3 hrs/week) outreach approach chosen over paid acquisition, consistent with the no-paid-acquisition gate until post-1.2 funnel data is readable.
- 2026-06-21: RunSmart v1.0.3 (16) and Resumely v1.1 (5) both confirmed live (superseded for Resumely by the 2026-06-29 v1.2(7) update above).

## This Cycle's Done Definition

A cycle is done when:

1. Drifted marketing assets are reconciled against the current canonical product-marketing doc
2. The command center reflects actual live/launch status, not stale pre-launch framing
3. `weekly-growth-review.md` has this cycle's report appended
4. The Notion Command Center is synced with this file
5. Outreach assets are handed to the founder for manual send — the OS does not publish
