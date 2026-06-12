# Executive Dashboard

Manual executive snapshot. Product status remains sourced from
`dashboard/status.json` and project `tasks/progress.md`.

Last updated: 2026-06-12 IDT

## Weekly Review

Latest review: `executive-os/WEEKLY-CEO-LATEST.md`

**Decision of the week:** The submission sprint is not over. Close both repos before anything else. OKR-1 deadline is 18 days out.

## Top 3 (week of 2026-06-14)

1. **RunSmart iOS build 14:** resolve stranded items (pull main, `fix/code-review-p0-identity` decision, 5 dirty migrations), archive, upload to App Store Connect, submit with reviewer response.
2. **Resumely iOS:** real-device smoke + PostHog Live Events screenshot + archive via Xcode Organizer + upload to App Store Connect.
3. **Decision board cleanup:** build-8-era items → Superseded; log EXD-010 (build 14 scope = WP-4 + WP-6 only).

## Portfolio Status

- **RunSmart iOS:** 1.0.2 build 14 ready for archive. Stranded items (main 2 behind, `fix/code-review-p0-identity` unpushed, 5 dirty migration files) blocking archive. Medium dashboard confidence.
- **Resumely iOS:** Build 3 fixes applied (Submit Package/PDF flow). Device smoke not yet done. High dashboard confidence.
- **RunSmart Web:** High confidence. Story 1 (Today content inventory) queued. Parked until iOS submissions clear.
- **ResumeBuilder Web:** High confidence. PDF smoke + APP_STORE_URL placeholder remain. Parked.
- **Agentic OS:** High confidence. Daily refresh automation live. Vault on GitHub.

Sources: `dashboard/status.json` (refreshed 2026-06-12), `PROJECT-STATUS.md`.

## Decision Board

Open executive decisions: **1** (EXD-010).

- **EXD-010 (open):** Build 14 scope = WP-4 + WP-6 only. VOICE_COACH_ENABLED flip only post-approval + device QA. Needs founder decision.
- Submitted builds frozen until Apple responds.
- Monetization deferred until first-cohort activation readable (EXD-009).
- Brands separate (EXD-007).
- Paid acquisition $0.

Source: `executive-os/EXECUTIVE-DECISIONS.md`.

## Plan Progress

- Business + GTM Plan: build 14 resubmission is the current launch gate.
- Pre-Launch Sprint: A1 LinkedIn draft awaits founder review — after submissions.
- RunSmart GTM: ASO/listing after resubmission only.
- ResumeBuilder Web weekly plan: parked.
- Research plans: preserved, not this week.

## Risk Board

- **June deadline (HIGH):** 18 days left; neither app submitted as of 2026-06-12.
- Resumely device smoke not done; Submit Package/PDF flow risk unresolved.
- RunSmart stranded items block archive; `fix/code-review-p0-identity` has unreviewed schema changes.
- Live PostHog event receipt not verified in production; post-approval decisions will be blind.

## Financial Snapshot

- Revenue: `unknown - need: App Store Connect / RevenueCat`
- Activation and retention: `unknown - need: PostHog`
- Marketing spend: `$0`, tracked
- Other costs and runway: `unknown - need: provider billing`

## Stop Doing

- No new iOS features while submissions pending.
- No VOICE_COACH_ENABLED flip before approval + device QA.
- No GTM/ASO content before at least one approval.
- No monetization implementation.
- No ResumeBuilder Web rollout.
- No new executive-os ceremony during submission sprint.

## Next Actions

1. RunSmart iOS: pull main → `fix/code-review-p0-identity` → archive build 14 → upload ASC.
2. Resumely iOS: device smoke → PostHog screenshot → archive → upload ASC.
3. COO review after first submission clears.
4. Log EXD-010 as Decided.
