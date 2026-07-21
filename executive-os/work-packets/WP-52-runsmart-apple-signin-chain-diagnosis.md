# Work Packet WP-52 — Diagnose the RunSmart Apple sign-in chain (timeboxed)

- Status: In Progress
- Started: 2026-07-21 (founder launched the session in the RunSmart iOS repo). Timebox runs from this date.
- Mode: Sweeper
- Source: COO Operating Review 2026-07-21 §10 (CEO decision (a)); live PostHog project 171597 (2026-07-21); Builder OS `2026-07-21-apple-signin-cross-product-pattern`; `05-Decisions/2026-06-10-resumely-apple-signin-hidden`
- Workflow pattern: normal
- Input trust: trusted
- Loop: RunSmart activation gate loop
- Signal: On live 1.1.1 (25), a genuine App Store install (`$is_testflight`/`$is_sideloaded`/`$is_emulator` all false) on iPhone17,1 produced **5 consecutive `ASAuthorizationError` code 1000** events at `screen=sign_in_wall`, 2026-07-20 12:22-12:25 UTC, 0 completions. Cumulative 12 events / 4 devices / 3 builds. Every `sign_in_completed` on record belongs to an Apple ID that had already authorized RunSmart.
- Memory update: `tasks/lessons.md` (RunSmart iOS) + a decision entry in Agentic OS `EXECUTIVE-DECISIONS.md`
- Success signal: A written verdict naming **which specific link** in the chain is broken, or ruling all of them out — sufficient to choose between WP-52a (repair) and WP-53 (guest path)
- Model route: Sonnet 5 (configuration inspection and evidence gathering; no architecture)
- Rollback: N/A — diagnosis only, no code or config changes. **Do not "fix while looking."**

## ⚠️ Correction to the 2026-07-21 PostHog AI audit — read before acting on it

A PostHog-generated audit run the same day claims: *"`sign_in_failed` — `error`, `provider`: both are null on all 12 occurrences. The event fires but carries no diagnostic info. You cannot tell what is failing or which auth provider. Fix immediately."* It lists this as the #2 priority for the week.

**That claim is false, and acting on it would waste this packet's timebox.**

The audit queried property names that do not exist on the event. The real properties are populated on all 12 occurrences:

| Property queried by the audit | Exists? | Actual property | Actual value |
|---|---|---|---|
| `error` | No | `error_code` | `1000` |
| `provider` | No | `error_domain` | `com.apple.AuthenticationServices.AuthorizationError` |
| — | — | `screen` | `sign_in_wall` |

The diagnostics that make this packet possible are already there. **Do not add sign-in instrumentation.** The instrumentation is fine; the Apple configuration is not.

This is itself the fifth recorded instance of the wrong-property-name failure class that WP-54 exists to prevent (`marketing_version`, `resume_uploaded`, `resume_upload_succeeded`, `optimized_preview_rendered`, and now this). Treat any "property is null" claim as unverified until the property is confirmed to exist in the project taxonomy.

## Owner Role
RunSmart iOS engineer + founder (portal access required)

## Project
RunSmart iOS — `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`

## Why This Is A Separate, Timeboxed Packet

The CEO decision is repair-versus-route-around, and it cannot be made responsibly without knowing whether this is a ten-minute portal fix or a structural problem. **The diagnosis is the same work under either branch**, so it runs first and it runs timeboxed.

**Timebox: one working session.** If the broken link is not identified by the end of it, that outcome *is* the answer — stop and proceed to WP-53. Do not extend. Six weeks have already gone into debugging this from the app side; the constraint on this packet is deliberately tight.

## The Chain To Inspect, In Order

Resumely hit this exact chain in June and could not complete the Services ID / private key step. Treat that as the leading hypothesis, not a coincidence.

| # | Link | What to confirm | Failure signature |
|---|---|---|---|
| 1 | **App ID** | Sign In with Apple capability enabled on the RunSmart App ID in the Apple Developer portal | code 1000 on-device, no network call |
| 2 | **Distribution provisioning profile** | The App Store distribution profile actually includes the SIWA entitlement, and the shipped build was signed with it | code 1000 on-device, no network call |
| 3 | **Services ID** | Exists, and is associated with the primary App ID | code 1000 or redirect failure |
| 4 | **Private key (.p8) + Key ID** | Generated, downloaded, and registered | Supabase-side failure |
| 5 | **Supabase Apple provider** | Enabled, and Authorized Client IDs contains the exact bundle ID `com.runsmart.lite` | `provider_disabled` in auth logs — the Resumely June signature |

Links 1-3 fail **on-device before any network request**, which matches RunSmart's observed signature (no `/token` request in Supabase auth logs during failures). **Start there.** Links 4-5 produce the Resumely-style failure and are less likely given the evidence, but confirm them anyway since a device that has already authorized would mask them.

## Evidence To Produce

1. Screenshot or text record of each of the five links' current state.
2. The entitlements actually present in the shipped 1.1.1 (25) binary — extract from the archive rather than trusting the project settings. `codesign -d --entitlements :- <path-to-.app>` is sufficient.
3. A statement of which link is broken, or an explicit "all five confirmed correct" verdict.
4. If all five are correct: the failure is not configuration, and WP-53 becomes the answer by elimination.

## Out of Scope — Do Not Touch

- **Do not change any portal or Supabase setting during this packet.** Diagnosis only. A silent config change mid-investigation destroys the ability to attribute a later result.
- Do not modify app code.
- Do not test on a device that has previously authorized RunSmart — it will succeed and prove nothing. This is the trap that produced the misleading 2026-07-20 clean-install result.
- Do not submit a build.

## Open Question To Resolve In-Session

Does RunSmart's Supabase project have Apple auth logs older than 24h retention that show `provider_disabled` from the 2026-07-15 failures? If retention has expired, say so explicitly rather than treating absence as evidence of correctness.
