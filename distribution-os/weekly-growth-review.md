# Weekly Growth Review Log

Append-only. One entry per week per product focus. Use the template at `templates/weekly-report-template.md`.

## How To Add An Entry

1. Run the weekly distribution cycle workflow
2. Fill the template at `templates/weekly-report-template.md`
3. Paste the filled report at the top of the entries section below (newest first)
4. Sync the same report to `Google Drive > Distribution OS > 06 Weekly Reports`

## Entries

<!-- newest first -->

### Week of 2026-06-29 — Resumely — Distribution OS Restart + Zero-Budget Outreach

**Status:** Distribution OS had gone stale since 2026-05-28 (a month before either app actually launched). Restarted with current live state and reconciled drifted copy.

#### Metrics This Week

| Metric | This Week | Prior Week | Notes |
|---|---|---|---|
| Resumely App Store live | v1.2 (7) since 2026-06-29 | v1.1 (5) since 2026-06-21 | Approved in <24h; Fit-First + Match Score rebrand now live in-app |
| RunSmart App Store live | v1.0.3 (16), unchanged | same | Maintenance only this week |
| Marketing files reconciled | 9 (web repo launch-assets x8 + iOS repo screenshot-briefs) | n/a | ATS-score framing replaced with Fit/Match per `.agents/product-marketing.md` |
| Outreach assets drafted | 3 (Hebrew DM, FB vibecoding israel post, LinkedIn job-seeker post) | 0 | Zero-budget, founder sends manually, 2-3 hrs/week budget |
| Distribution OS staleness | 0 days (just refreshed) | 32 days | Command center + resumebuilder.md open questions were answered |

#### What Happened

- Founder confirmed Resumely v1.2 (7) approved and live (submitted 2026-06-28, live 2026-06-29 — under 24h Apple review turnaround).
- Found the canonical positioning doc (`.agents/product-marketing.md` in the iOS repo, locked 2026-06-28) was never propagated to the web repo's reusable outreach templates, which still used pre-rebrand "ATS score/ATS checker" language and, in two ASO files, an exact stale duplicate of pre-fix iOS copy.
- Rewrote 8 reusable templates in the web repo (`launch-assets/`) and 1 duplicate file in the iOS repo to match Fit/Match positioning; left dated pre-launch execution logs (`docs/gtm/week-1-*`, `canonical-90-day-plan.md`, 2026-02-14/16) untouched as historical record per Principle 6 (project repo's current canonical doc wins for product facts, but historical logs are not retroactively rewritten).
- Drafted zero-budget Hebrew outreach copy (personal DM, FB vibecoding israel group post, 1-2 LinkedIn job-seeker group posts) for the founder's 0-10 user goal — no paid acquisition, consistent with the locked no-paid-acquisition-until-funnel-readable rule.
- Answered the open question in `distribution-os/projects/resumebuilder.md` ("is the iOS app live?") at the source.

#### Top 3 Experiments

1. Personal/community outreach wave (zero budget) — founder sends this week, measure installs via App Store Connect + PostHog.
2. Directory submissions (rb-dir-001) — was blocked on App Store URL pre-launch; URL now exists, re-score next cycle.
3. Web → iOS funnel reconciliation — the web free ATS-checker tool still uses old "ATS score" framing; not touched this cycle, flagged as next open item.

#### Blockers

- FB/LinkedIn group names could not be verified by web search (groups change too often to trust a snapshot); founder to confirm directly since they already have access.
- Web repo's free ATS tool positioning vs. iOS Fit/Match rebrand still unreconciled — separate, larger scope than this cycle.

#### Next Week Focus

- Founder sends the outreach wave; read results in PostHog (project 270848) before deciding next ASO iteration.
- Re-score rb-dir-001 directory submissions now that the App Store URL exists.
- Decide whether to reconcile the web ATS-checker tool's positioning or leave it as a distinct, intentionally separate free-tool funnel.

---

### Week of 2026-06-21 — Portfolio — Post-Launch Growth (Both Apps Live)

**Status:** First distribution cycle with both iOS apps live on the App Store. Pre-launch positioning retired.

#### Metrics This Week

| Metric | This Week | Prior Week | Notes |
|---|---|---|---|
| RunSmart App Store live | v1.0.3 build 16 since 2026-06-19 | In review / pre-live | Founder-confirmed go-live |
| Resumely App Store live | v1.1 build 5 since 2026-06-21 | Submitted 2026-06-18 | Founder-confirmed go-live |
| RunSmart PostHog users (7d) | ~16 | unknown | Early post-launch, low volume — expected |
| Resumely PostHog D7 readout | scheduled ~2026-06-28 | n/a | 7 days after 2026-06-21 go-live |
| App Store impressions / conversion | unknown | unknown | need: App Store Connect |
| Directory referrals | 0 | 0 | rb-dir-001 still blocked on founder submit |

#### What Happened

- RunSmart iOS v1.0.3 build 16 confirmed live 2026-06-19; status guard false positive cleared (phase text contained "resubmission").
- Resumely iOS v1.1 build 5 confirmed live 2026-06-21.
- RunSmart Web: Garmin worker-RPC lockdown merged (#97); migration await founder apply.
- ResumeBuilder Web: LinkedIn ATS scrape fix on branch; awaiting Vercel preview verification.
- Experiment log still shows pre-launch statuses (rs-aso-001/002 "awaiting review") — needs refresh to post-launch framing.

#### Top 3 Experiments (post-launch reframed)

1. **rs-aso-002** (score 18) — Screenshot caption overlays for RunSmart live listing; measure conversion pre/post in ASC.
2. **rb-aso-001** (score 21) — Resumely listing already filed; iterate subtitle/keywords after D7 readout.
3. **rb-dir-001** (score 15) — Directory submissions now unblocked (App Store URL exists); founder submit to 5 directories.

#### Blockers

- RunSmart Garmin production: migration apply + manual portal gates (founder).
- ResumeBuilder ATS: preview verification before merge.
- All conversion metrics: need ASC + PostHog D7.

#### Next Week Focus

- Post-launch ASO for RunSmart (first ratings, screenshot captions).
- Resumely D7 readout ~2026-06-28.
- Directory pack submit (rb-dir-001) once founder reviews.

---

### Week of 2026-05-27 — RunSmart — ASO Finalization (Pre-Launch)

**Status:** Cycle complete. Assets ready for founder action. App not yet submitted for review.

#### Metrics This Week (all pre-launch — no live data)

| Metric | This Week | Prior Week | Notes |
|---|---|---|---|
| App Store impressions | unknown | — | Not live yet |
| Product page → install rate | unknown | — | Not live yet |
| Weekly active runners | 0 | — | Not live yet |
| New user activation | 0 | — | Not live yet |
| LinkedIn impressions | unknown | — | No posts yet |

#### What Happened

First distribution cycle. App is uploaded to App Store Connect (build 2026-05-19) but not yet submitted for review. All energy this week went to finalizing ASO assets before submission.

Pre-work from prior sessions (screenshot copy, Garmin audit, analytics spec) was recovered and filed in the main tree after a worktree sync issue. All three assets are now ready for action.

#### Experiments Queued This Week

| ID | Score | Status | Asset Location |
|---|---|---|---|
| rs-aso-001 | 24 | awaiting founder action | `distribution-os/projects/runsmart/scaffold/drafts/2026-05-27-rs-aso-001/description.txt` |
| rs-analytics-001 | 22 | awaiting product session | `.agent-os/distribution/analytics-instrumentation-spec.md` |
| rs-aso-002 | 18 | awaiting overlay render | `.agent-os/distribution/screenshot-overlay-copy.md` |

#### Bottleneck

App Store submission. Once the three experiment actions above are done, the app can be submitted. Until submission, zero acquisition metrics are possible.

#### Decisions

- Screenshot A variants locked for all 5 slots
- Garmin description sentence approved
- Top channel priority confirmed: ASO > lifecycle email > PLG landing pages

#### Next Week Focus

Confirm App Store submission is in review. Begin LinkedIn founder launch post. Plan PLG landing page experiment. Wire lifecycle email if rs-analytics-001 is done.

---

---

## Week of 2026-05-28 — ResumeBuilder iOS, Cycle 1

**Focused product**: ResumeBuilder iOS
**Theme**: ASO listing v1 (English) — write Resumely App Store copy before first submission
**Cycle type**: First distribution cycle; pre-launch; all metrics baseline at zero

#### Decisions Locked This Cycle

| Decision | Confirmed |
|---|---|
| App name | Resumely |
| iOS launch pricing | Free (no IAP at launch; pricing deferred) |
| App Store status | Pre-submission |
| Hebrew approach | Single listing + Hebrew locale (in-app RTL deferred) |
| ATS tool iOS CTA | Missing (confirmed blocker — web repo task) |
| Apple Search Ads | Out of scope |

#### Metrics

All unknown — app is pre-submission. No App Store Connect data, no PostHog on iOS, no installs.

#### Bottleneck

The App Store listing does not exist. Zero acquisition can happen without it. Everything this cycle points at filling that gap.

#### Experiments Queued This Week

| ID | Score | Status | Asset Location |
|---|---|---|---|
| rb-aso-001 | 21 | awaiting founder review | `drafts/2026-05-28-rb-aso-001/listing-copy-v1.md` |
| rb-aso-002 | 20 | awaiting founder review | `drafts/2026-05-28-rb-aso-002/screenshot-brief-v1.md` |
| rb-dir-001 | 15 | awaiting review + App Store URL | `drafts/2026-05-28-rb-dir-001/directory-pack-v1.md` |

#### Open Items Requiring Founder

1. Review listing copy (rb-aso-001): confirm subtitle, description claims, privacy policy URL
2. Review screenshot brief (rb-aso-002): confirm UI matches each slot claim; assign rendering
3. Fix ATS tool result page: add App Store CTA with `ct=ats-tool-result` (web repo — highest Tier A blocker after listing)
4. Confirm privacy policy URL is live (App Store submission blocker)
5. Confirm support URL is live (App Store submission blocker)

#### Next Week Focus

Confirm listing copy is approved → screenshots rendered → submit Resumely to App Store review.
Secondary: fix ATS tool result page iOS CTA in web repo.
