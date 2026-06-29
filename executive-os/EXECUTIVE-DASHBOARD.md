# Executive Dashboard

Manual source-of-truth dashboard for the Executive Intelligence OS. Financial cells stay `Needs Data` until a real source exists.

Last updated: 2026-06-29 IDT

## Executive Summary

RunSmart iOS — LIVE on App Store as marketing version `1.0.4`; build 18 upload/submission/live confirmation remains founder-only. Garmin external reply remains gated until build 18 is genuinely live and all 6 Gate-4 screenshots are recaptured against that live build: Founder uploads/submits build 18 to App Store Connect, waits for approval, confirms build 18 live from App Store/ASC, then recaptures all 6 Gate-4 screenshots and sends the Garmin reply with the new zip. The `plan_run_cta_tapped` cohort cannot be measured until build 18 ships · Resumely iOS — Post-launch — v1.2 (7) live; verifying production funnel events and planning next ASO/outreach iteration: (1) Verify production PostHog project 270848 receives upload-funnel and `fit_check_*` events now that 1.2 (7) is live. (2) Read results of the founder's zero-budget outreach wave. (3) Use the clean post-1.2 funnel read to decide whether ASO volume, lifecycle messaging, monetization, or backend/state follow-ups are next · RunSmart Web — Web/backend Gate-4 work complete; iOS build 18 locally archive/export validated but not confirmed live. Garmin reply remains blocked until founder uploads/submits build 18, Apple approves it, build 18 is genuinely live, and all 6 screenshots are recaptured against that live build · ResumeBuilder AI (Web) — ATS scoring accuracy — both compounding causes from the 2026-06-21 diagnosis are resolved. PR #80 and PR #81 both merged to main. Story 2's metric-nudge follow-up is parked for a future build (founder decision 2026-06-21/22: leave metrics_presence as-is for now, plan the nudge feature via PM skill before building)

## CEO Focus

- Resumely iOS: founder device smoke on iPhone 13, then Xcode Organizer archive + ASC upload.
- RunSmart iOS: monitor build 8 review — approved triggers GTM; rejected triggers minimal fix as build 9.
- RunSmart iOS: GTM plan at .agent-os/distribution/gtm-plan.md is ready to activate on approval.

## Financial Snapshot

Needs Data - no revenue/cost instrumentation wired.

## Open Decisions

- RunSmart iOS: if build 8 rejected again, decide minimal fix scope vs. expanding v2 feature set before resubmit.
- RunSmart iOS: when to flip VOICE_COACH_ENABLED=true in Vercel (voice coach is in build 8 but feature flag is off).
- ResumeBuilder Web: defer rollout unless Resumely smoke exposes backend blockers.

## Status Confidence

How much each project's state is backed by parsed local task files versus narrative only.

| Project | Confidence | Source | Last Validation |
| --- | --- | --- | --- |
| RunSmart iOS | High | tasks/progress.md | 2026-06-26 - Release archive passed for `build/RunSmart-build18-AppStore-20260626-codex.xcarchive`; non-upload App Store export passed to `build/RunSmart-build18-AppStoreExport-20260626-codex/RunSmart.ipa`; exported IPA is `RunSmart`, `com.runsmart.lite`, `1.0.4 (18)`, encryption false, HealthKit/SIWA/associated-domains present, `get-task-allow=false`, with dSYM present. Known HealthKit deprecation warning remains |
| Resumely iOS | High | tasks/progress.md | 2026-06-26 — full test suite passed on iPhone 17 simulator (105 XCTest + 5 Swift Testing, 0 failures); iPhone SE 3rd gen simulator visual smoke passed for Home EN/HE, locked Optimized/Design/Expert teasers, and Me language/RTL after fixing visible Hebrew fallback strings |
| RunSmart Web | High | tasks/progress.md | 2026-06-26 — iOS build 18 Release archive and non-upload App Store export passed locally. Apple public lookup confirms live marketing version `1.0.4` dated 2026-06-24 but does not expose build number, so it cannot prove build 18 is live |
| ResumeBuilder AI (Web) | High | tasks/progress.md | fix/ats-jd-requirements-and-metrics (commit 3c0a4ee) — new regression test (`tests/unit/linkedin-job-extractor.test.ts` + fixture `guest-fragment-varied-headings.html`), 32/32 unit tests pass, lint clean, tsc 21 pre-existing errors only (none in touched files). Real-data repro against live Fresha LinkedIn guest fragment confirmed responsibilities/requirements/nice_to_have all populate where they were previously null |
| Agentic OS | High | tasks/progress.md | ./agentic-os verify passed with JSON, fallback sync, confidence, freshness, drift, packet hygiene, links, and git diff checks on 2026-06-12 |

## Risk Board

- RunSmart iOS: Codex cannot upload/submit to App Store Connect or prove build 18 live. Do not recapture or send Garmin evidence until build 18 is confirmed live. The 01-03 logo remains a documented Garmin corporate wordmark fallback, not the Connect-specific tile
- Resumely iOS: Backend/state capabilities remain absent for paste-text diagnosis, sample/demo diagnosis, parser-stage progress callbacks, point-delta apply-all fixes, resumable offline analysis, globally accurate pre-optimization `hasResume`/`hasJob` flags, and a true NWPathMonitor-driven auto-resume for connection-lost recovery (current Retry is manual only)
- RunSmart Web: Build 18 is not confirmed live from this session, so screenshot recapture and Garmin send remain blocked. The 01-03 asset remains a documented Garmin corporate wordmark fallback, not a guaranteed pass for Marc's Connect-specific tile request
- ResumeBuilder AI (Web): Founder decision on Story 2's framing above. Also still open from before: keyword_phrase (12% weight) re-weighting — requires verbatim 3-6 word n-gram overlap, near-0 for any paraphrased resume by design, not a bug

## Next Recommended Actions

1. RunSmart iOS: Founder uploads/submits build 18 to App Store Connect, waits for approval, confirms build 18 live from App Store/ASC, then recaptures all 6 Gate-4 screenshots and sends the Garmin reply with the new zip. The `plan_run_cta_tapped` cohort cannot be measured until build 18 ships
1. Resumely iOS: (1) Verify production PostHog project 270848 receives upload-funnel and `fit_check_*` events now that 1.2 (7) is live. (2) Read results of the founder's zero-budget outreach wave. (3) Use the clean post-1.2 funnel read to decide whether ASO volume, lifecycle messaging, monetization, or backend/state follow-ups are next
