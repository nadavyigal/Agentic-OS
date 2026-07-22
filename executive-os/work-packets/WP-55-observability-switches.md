# Work Packet WP-55 — Turn on the observability that is already paid for

- Status: Open
- Mode: Builder
- Source: PostHog AI audits of projects 171597 + 270848 (2026-07-21)
- Workflow pattern: normal
- Input trust: trusted
- Loop: Activation measurement integrity loop
- Signal: Session replay is off in RunSmart (zero `$snapshot` events in 90 days) while 9 users rage-clicked the main screen 30 times. Error tracking is off in both projects (zero `$exception` events). RunSmart's `$screen_name` resolves to raw SwiftUI class names, which makes replay and rage-click data undiagnosable even once replay is on.
- Memory update: `tasks/lessons.md` in both iOS repos
- Success signal: `$snapshot` events present in RunSmart; `$exception` events present in both; `$screen_name` shows human-readable names like `PlanView` rather than `UIHostingController<ModifiedContent<AnyView, RootModifier>>`
- Model route: Sonnet 5
- Rollback: Every item is a config flag or an additive call. Revert the commit or flip the setting back.

## Owner Role
RunSmart iOS engineer + Resumely iOS/web engineer

## Project
Split across three repos — see per-item routing below.

## Why This Is Worth A Packet

This is the cheapest genuinely-new finding in either audit. Every item is a config flag or a one-line call, and together they convert the portfolio's biggest current weakness — *tiny n, so every user matters* — from a liability into an advantage. At 15 identified RunSmart users, a session replay is not a data point, it is a user interview.

The rage-click signal makes the case: **8 of roughly 15 identified RunSmart users rage-clicked the main app wrapper**, 30 events total. That is a majority of the known user base hitting something unresponsive, and there is currently no way to see what.

## Items, In Priority Order

| # | Item | Repo | Effort | Why |
|---|---|---|---|---|
| 1 | Enable session replay | RunSmart iOS | Config flag | 9 rage-clicking users, zero visibility. Highest leverage item in either audit |
| 2 | Add `posthog.screen("ViewName")` in each SwiftUI view's `onAppear` | RunSmart iOS | ~1h | Without this, replay and rage-click data stay undiagnosable. **Do item 1 and 2 together — item 1 alone is much less useful** |
| 3 | Enable error tracking / `$exception` | RunSmart iOS + Resumely web | Config | Zero crash or JS-exception visibility today. RunSmart also shows a ~29% plan-generation failure rate (28 started, 12 succeeded, 8 failed) with no error detail |
| 4 | Verify session replay is on for Resumely **web** | Resumely web | Check | Audit reports it on for iOS, unclear for web |

## Explicitly Deferred — monetization instrumentation

Both audits flag the total absence of `paywall_viewed`, `purchase`, `subscription_started`, and (Resumely) any Stripe connection, and both rank it top-3. **That finding is correct and it is deliberately deferred**, not an oversight: monetization is gated behind activation evidence that does not yet exist, and both funnels are currently confirmed broken.

The judgement call worth making now: adding the *instrumentation* is cheap and starts accumulating data before there is anything to sell, whereas connecting Stripe is pointless while zero purchase events exist. If any of this is done early, do the event stubs, not the warehouse integration.

Do not treat "the audit ranked it #3" as authorization to build a paywall.

## Out of Scope

- Acting on what replay reveals. This packet turns the cameras on; diagnosing what they record is separate work.
- The RunSmart `Application Opened` vs `app_launched` duplicate — WP-54 detects it, the product repo decides.
- `garmin_sync_completed` going quiet 20 days ago. **Not a defect** — Garmin is parked per EXD-021 and the app was deactivated. The audit flagged it as needing investigation because it has no access to that decision.
