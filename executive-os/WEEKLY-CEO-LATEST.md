# Weekly Executive Summary - 2026-06-12

- Status: current
- Reviewed: 2026-06-12
- Portfolio trust: Actionable
- Open executive decisions: 1 (EXD-010 below)
- Source: dashboard/status.json, PROJECT-STATUS.md, DASHBOARD.md (refreshed 2026-06-12), executive-os/COO-LATEST-REVIEW.md (2026-06-11), executive-os/EXECUTIVE-METRICS.md

## Plan Progress

| Plan | Current milestone | Executive direction |
|---|---|---|
| `executive-os/BUSINESS-GTM-PLAN-V0.md` | Build 14 resubmission is the launch gate. | RunSmart first. Archive, upload, submit. |
| `docs/superpowers/specs/2026-06-04-pre-launch-sprint-design.md` | A1 LinkedIn draft still awaits founder review. | Not this week. Unblock submissions first. |
| RunSmart `.agent-os/distribution/gtm-plan.md` | App Store listing/ASO hardening after resubmission. | Post-submission packet only. |
| ResumeBuilder Web weekly plan | Parked unless Resumely smoke exposes backend issues. | Stay parked. |
| Research plans | Preserved. | No execution this week. |

## Top 3 Priorities (week of 2026-06-14)

1. **RunSmart iOS build 14: close the stranded items and submit.** Pull main, resolve `fix/code-review-p0-identity` (review and merge to main or discard), commit the 5 dirty migration files in a proper PR, archive build 14, upload to App Store Connect, submit with the prepared reviewer response. Every piece is ready — this is execution only. OKR-1 deadline is 18 days out.
2. **Resumely iOS: real-device smoke and archive.** Sign in on device, smoke optimize → Improve ATS → Preview & Export PDF → Submit Package → Save Package to Me → share PDF / copy cover letter → tap Submit at Job Link. Screenshot PostHog Live Events (`app_launched`, `optimization_completed`, `export_success`). Archive via Xcode Organizer, upload to App Store Connect.
3. **Close the stale decision board.** The decision board still shows "build 8 rejection" framing. We are on build 14. Flag old items as Superseded; log EXD-010.

## Key Decisions

### EXD-010 (new) — RunSmart iOS 1.0.2 build 14 resubmission scope
- **Recommendation:** Minimal: WP-4 (account deletion) + WP-6 (aha moments). Nothing else in build 14.
- **Voice coach flag:** Flip VOICE_COACH_ENABLED only after approval + physical-device voice QA. Not for build 14.
- **Status:** Open — needs founder approval to log as Decided.

### Standing calls (unchanged)
- Submitted builds frozen until Apple responds.
- Monetization deferred until first-cohort activation is readable (EXD-009).
- Brands remain separate (EXD-007).
- Paid acquisition at $0.

## Stop-Doing List

- Do not open new iOS feature work while submissions are pending.
- Do not flip VOICE_COACH_ENABLED before approval + device QA.
- Do not start GTM/ASO content work before at least one app is approved.
- Do not implement the monetization spec yet.
- Do not advance ResumeBuilder Web rollout without a real mobile/backend blocker.
- Do not expand executive-os with new OS ceremony while the submission sprint is the OKR.

## OKR-1 Check (Q2: both apps approved before end of June)

| App | Status | Remaining founder tasks |
|---|---|---|
| RunSmart iOS | Build 14 ready; stranded items blocking archive | Resolve git, archive, upload, submit |
| Resumely iOS | Fixes applied; device smoke not done | Device smoke + PostHog evidence + archive + upload |

Both executable this week. No external blockers before submission.

## Top Risks

1. **June deadline:** 18 days left. Neither app is submitted as of 2026-06-12. Apple review alone takes 1-3 days. Every day of delay narrows the window.
2. **Resumely device smoke still undone:** Submit Package / PDF flow was broken as recently as 2026-06-11. Fixes applied, but no successful end-to-end device smoke captured. This is the last gate before archive.
3. **RunSmart stranded items:** `fix/code-review-p0-identity` has unreviewed migration changes. Resolve explicitly — do not archive over unreviewed schema changes.
4. **Metrics Needs Data:** No live PostHog receipt from any production user. Post-approval decisions will be blind until verified.

## Recommended Next Actions

1. RunSmart iOS session Monday → pull main → `fix/code-review-p0-identity` decision → archive build 14 → upload ASC.
2. Resumely iOS session → device smoke → PostHog screenshot → archive + upload.
3. After one submission is in, COO review for first GTM/ASO milestone.
4. Log EXD-010 as Decided.

## Decision Of The Week

**The submission sprint is not over. Close the repos before anything else.** OKR-1 deadline is 18 days out. The OS is in good shape. Submit first.
