# D7 Activation Readout #3 — 2026-07-12

Live, read-only PostHog read completed during Founder Morning. Project timezone is UTC for both apps. No PostHog configuration, cohort, dashboard, or production data was changed.

## Headline

| App | Mature D7 denominator | Activated | Rate | Confirmed wall |
|---|---:|---:|---:|---|
| RunSmart iOS | 13 organic physical-device installs through 2026-07-05 | 0 `run_completed` | 0% | 13 installed → 1 onboarded → 1 planned → 0 started/completed |
| Resumely | 73 founder/test-excluded first-seen people through 2026-07-05 | 0 `optimization_completed` | 0% | 73 first seen → 9 uploaded → 0 optimized/exported within D7 |

Both activation gates remain closed. Do not unlock monetization, paid acquisition, or high-volume GTM from this read.

## Cohorts and exclusions

### RunSmart

- PostHog project `171597`, canonical metric `Application Installed → run_completed` within seven days.
- Install window: 2026-06-19 00:00 UTC through 2026-07-05 23:59 UTC; conversion observation through 2026-07-12.
- Excluded install rows with `$is_emulator=true`, `$is_testflight=true`, or `$is_sideloaded=true`, plus the two established founder person prefixes.
- The project's bot property was unavailable in the query taxonomy and was not used. The canonical mobile install event and physical-device filters keep this limitation low-risk, but it remains a caveat.

### Resumely

- PostHog project `270848`, canonical metric first `app_launched` or `$pageview` → `optimization_completed` within seven days.
- First-seen window: 2026-06-10 00:00 UTC through 2026-07-05 23:59 UTC; conversion observation through 2026-07-12.
- Excluded `is_internal_tester=true` and the four established founder/QA/bot person prefixes from the prior activation contract.
- The virtual-bot property was unavailable in the project taxonomy, so the web-inclusive denominator may contain unattributed automated pageviews. The 0% result is sufficient to keep the gate closed, but denominator comparisons should retain this caveat.

## Decision and re-read conditions

- Resumely remains primary. Close WP-32's seven-day community experiment and finish the founder-approved WP-31 Hebrew ASO asset pack. The post-live 1.4.1 picker cohort is separate and remains deferred until 2026-07-18 minimum / 2026-07-25 preferred.
- RunSmart stays maintenance-plus. WP-40 S1+S2 is merged, but WP-42 has no clean production disclosure cohort. Re-run after one clean disclosure viewer exists; require at least 10 before recommending a product change.
- Voice coach remains deferred. Garmin remains maintenance-only.

Source timestamp: 2026-07-12, queried during the 08:46 IDT Founder Morning run.
