# Weekly Growth Review Log

Append-only. One entry per week per product focus. Use the template at `templates/weekly-report-template.md`.

## How To Add An Entry

1. Run the weekly distribution cycle workflow
2. Fill the template at `templates/weekly-report-template.md`
3. Paste the filled report at the top of the entries section below (newest first)
4. Sync the same report to `Google Drive > Distribution OS > 06 Weekly Reports`

## Entries

<!-- newest first -->

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
