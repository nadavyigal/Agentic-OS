# WP-40 — RunSmart: HealthKit Activation & Discoverability

- **Status:** NOT STARTED
- **Created:** 2026-07-09
- **Source:** EXD-021 (Garmin tri-track split + HealthKit redirect) — RunSmart's wearable-data engineering focus moves to HealthKit, since every iOS user already grants it and it's already built but essentially unused.
- **Mode:** Builder
- **Workflow pattern:** one story at a time, smallest shippable diff, device QA per story
- **Related:** EXD-021, EXD-015 (non-wearable / Phone-Only-Runner focus), WP-39 S7 (RunSmart activation funnel — 0 `healthkit_sync_completed` in 14d), WP-26/27 (Garmin, now background-only)
- **Success signal:** a real user can go from first launch to a connected, syncing HealthKit source without ever opening the Profile tab on their own initiative, and the existing `healthkit_disclosure_viewed → connect_tapped → sync_completed` funnel actually populates in PostHog with a real cohort.

## Project

RunSmart iOS: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

## Read First

- `IOS RunSmart app/Services/HealthKit/HealthKitSyncService.swift` — the existing integration (already reads workouts, routes, heart rate, resting HR, HRV, steps, sleep, active energy; already writes imported runs + a daily wellness snapshot to local store)
- `IOS RunSmart app/Features/Profile/ProfileTabView.swift` (~L240-330, `ConnectedServiceTile` grid) — where the real "Connect" action currently lives
- `IOS RunSmart app/Features/Secondary/SecondaryFlowView.swift` (~L2200-2260) — the connect/sync flow logic and analytics hooks
- `IOS RunSmart app/Features/Onboarding/OnboardingView.swift` (~L99-107) — the current onboarding treatment
- `IOS RunSmart app/Services/Analytics/AnalyticsEvents.swift` (~L206-220) — existing `healthkit_disclosure_viewed`, `healthkit_connect_tapped`, `healthkit_sync_completed` events (already instrumented, just never firing at volume)

## Context — what's actually true today (verified 2026-07-09, don't re-derive this)

The integration is **built, functional, and already reads real data** — this is not a from-scratch feature. `HealthKitSyncService` requests workouts, routes, heart rate, resting HR, HRV, steps, sleep, and active energy; `importHealthData()` de-duplicates against existing runs and saves a daily wellness snapshot; analytics events already exist for the disclosure/connect/sync funnel.

**The gap is discoverability, not capability.** The actual "Connect HealthKit" action lives inside `ConnectedServiceTile` on the **Profile tab** — a secondary/settings surface, not the primary onboarding or activation flow. Onboarding (`OnboardingView.swift` L99-107) only shows a `DevicePreviewRow` — informational text ("Uses HealthKit to read approved workouts... You can connect devices later") with no actual connect button. Garmin has the identical placement problem (also buried in the same Profile tab grid), which is part of why WP-39's Phase 1 read found 0 `healthkit_sync_completed` events in the last 14 days despite the feature working end-to-end for anyone who happens to find it.

This matches WP-39's other finding: `ai_insights` and `aha_moment_fired` are both at 0 — even if HealthKit data gets imported, there's currently no visible product moment that makes the import valuable to the user, which compounds the discoverability problem (even a user who connects has little reason to check back).

## Stories

| Story | Problem | Proposed change (smallest diff) | Acceptance | Model route |
|---|---|---|---|---|
| **S1 — Move HealthKit connect into the primary flow** | The only real "Connect" action is buried in Profile → Connected Services; onboarding only previews it. | Add a real, tappable HealthKit connect step either at the end of onboarding or as the first screen immediately after onboarding completes (founder/dev to pick the exact placement — acceptance criteria below is outcome-based, not layout-prescriptive). Reuse `HealthKitSyncService.requestAccess()` — no new permission logic. Skippable (don't force it), but it must be reachable without the user having to discover the Profile tab on their own. | A fresh install → onboarding completion → the HealthKit connect prompt appears without the user navigating to Profile. Tapping "Connect" triggers the real `requestAccess()` flow (same permission sheet as today's Profile-tab path). Skipping is possible and doesn't block onboarding completion. | Sonnet |
| **S2 — Auto-import after connect, not manual-tap-only** | Check whether `importHealthData()` only runs when the user manually taps Sync in Profile, or runs automatically after a successful connect. | If it's currently manual-only: trigger one `importHealthData()` call automatically right after `requestAccess()` succeeds (from S1's new flow), so the very first sync doesn't require a second discovery step. Also check whether there's any periodic/background re-sync (e.g. on app foreground) — if not, decide with the founder whether that's in scope here or a follow-up (don't build background refresh speculatively without confirming it's wanted). | After connecting in S1's flow, at least one sync happens automatically — verify via a fresh HealthKit-seeded simulator/device with existing workout data, confirm runs land in the local store without a manual Sync tap. | Sonnet |
| **S3 — Confirm HealthKit data actually surfaces value once imported** | `RecoveryDashboardView`/`TodayTabView`/Wellness Trends already read HealthKit-derived fields (steps, sleep, HRV, resting HR per `SupabaseRunSmartServices.swift` ~L1580-1660) — confirm these actually render meaningfully once a real HealthKit snapshot exists, not just silently populate a data model nobody sees. | No new UI unless a gap is found — this story is a verification pass with device QA screenshots. If a real gap is found (e.g. a HealthKit-derived field that's computed but never rendered anywhere), scope the smallest fix to surface it; if the fix would be larger than a 1-2 file change, stop and report instead of expanding. | Device QA: connect HealthKit with seeded data (steps, sleep, resting HR present), confirm Today tab and/or Recovery dashboard visibly reflect at least one of those fields. Screenshot evidence. | Sonnet |
| **S4 — Verify the funnel populates in PostHog** | `healthkit_disclosure_viewed` → `healthkit_connect_tapped` → `healthkit_sync_completed` already exist as events but fire near-zero because the flow was unreachable (per WP-39). | No new instrumentation — S1-S2 should make these fire naturally once the flow is reachable. This story is verification only: after S1-S3 ship and get real usage (founder/QA testing or early cohort), pull the funnel from PostHog project 171597 ("Running coach", RunSmart's project — not Resumely's) and confirm events are firing at a rate consistent with actual connects, not still near-zero. | PostHog funnel query, `filterTestAccounts=true`. Report actual counts, don't assume. | Sonnet |

### Explicitly out of scope for this packet
- Making HealthKit the *only* device option or removing Garmin's tile — Garmin stays available (background thread per EXD-021), this packet just fixes HealthKit's own discoverability.
- Any new AI-insight/coaching feature built on top of HealthKit data (aha-moment/ai_insights work) — that's a separate, larger product decision; note the gap in S3 but don't build a coaching feature here.
- Background/periodic re-sync, unless S2 finds it's trivial and the founder confirms it's wanted — don't build speculative infra.

## Constraints

- Reuse `HealthKitSyncService` as-is — this packet is about reachability and activation flow, not re-architecting the HealthKit integration itself.
- No changes to Garmin's placement or behavior in this packet (that's EXD-021's separate background track).
- Smallest shippable diff per story; device QA screenshots per story into `docs/qa/reports/`.
- Do not build a new onboarding step that blocks progression if HealthKit permission is denied or skipped — this must stay optional.

## Validation

- Device QA screenshots per story (fresh install for S1/S2, seeded HealthKit data for S3).
- `git status --short --branch` + push + PR per session-end rule.
- Unit test coverage where the existing test suite already covers `HealthKitSyncService`/`HealthKitRecordedRunMapper` — extend, don't duplicate.

## Completion Gate

Report per story: what was found (was S2's auto-import already there or not; was S3's rendering gap real or not), diff summary, device evidence, what was explicitly NOT done. Packet is complete when S1-S4 land or are explicitly re-scoped with reason.

## Progress

- 2026-07-09 — Packet created from EXD-021. Grounded in a real code read (not speculative): confirmed `HealthKitSyncService` is fully built and functional, confirmed the actual connect action lives only in `ProfileTabView`'s Connected Services grid (same placement problem as Garmin), confirmed onboarding only shows an informational preview row with no action. Not started.
