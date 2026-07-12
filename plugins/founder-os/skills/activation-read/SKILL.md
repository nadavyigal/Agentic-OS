---
name: activation-read
description: Read product activation and funnel evidence with founder, QA, bot, emulator, and sideloaded activity excluded. Use for PostHog funnel reviews and cohort gates.
---

# Activation read

1. Read the current product analytics report and exclusion contract before querying.
2. Define the product, build or marketing version, cohort window, funnel steps, and minimum sample.
3. Use connected analytics tools read-only. Never alter production data.
4. Report numerator, denominator, exclusions, uncertainty, and the exact re-read condition.
5. Update Portfolio HQ metrics only when the evidence meets the stated cohort gate. Otherwise keep the existing claim and record why the read is deferred.
6. Never infer a broken feature from a missing event alone.
