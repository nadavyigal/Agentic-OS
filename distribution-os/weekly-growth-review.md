# Weekly Growth Review Log

Append-only. One entry per week per product focus. Use the template at `templates/weekly-report-template.md`.

## How To Add An Entry

1. Run the weekly distribution cycle workflow
2. Fill the template at `templates/weekly-report-template.md`
3. Paste the filled report at the top of the entries section below (newest first)
4. Sync the same report to `Google Drive > Distribution OS > 06 Weekly Reports`

## Entries

<!-- newest first -->

### Week of 2026-07-14 — ResumeBuilder iOS — Live Experiment Reconciliation (WP-31, WP-32)

**Status:** Reconciliation cycle complete. Founder confirmed on 2026-07-15 that WP-31 Hebrew ASO is live. WP-32 Facebook-groups distribution went live on 2026-07-05 and closed inconclusive on 2026-07-12. Both live states are now reflected in `experiment-log.md`; no external publishing occurred in this review.

#### Metrics This Week

| Metric | This Week | Prior Week | Notes |
|---|---|---|---|
| WP-31 Hebrew ASO publish state | live (founder-confirmed 2026-07-15) | queued / unlogged | Actual App Store Connect publish timestamp is not yet logged |
| WP-31 Israeli storefront conversion | unknown | unknown | Baseline export is missing; 21-day close date cannot be set honestly until the publish timestamp is captured |
| WP-32 Facebook-group posts live | 3 posts (published 2026-07-05) | 0 logged | `israel.hitech.jobs`, `Vibe Coding - Israel`, and `israel.hightech` |
| WP-32 visible engagement at close | 3 reactions, 1 comment, 0 visible qualitative product-feedback replies | not captured | Authenticated read-only closeout on 2026-07-12 |
| WP-32 Israeli storefront install lift | unknown | unknown | App Store Connect analytics was unavailable at closeout |

#### What Happened

- `rb-he-aso-001` (WP-31) moved from queued to **published — measuring** after the founder confirmed the Hebrew ASO changes are live. The publish date and pre-publish Israeli-storefront baseline remain unlogged, so this review does not invent a start date or result.
- `rb-he-comm-001` (WP-32) is recorded as an experiment that **went live** on 2026-07-05 and then closed inconclusive on 2026-07-12. Its current home remains `Done — Did Not Work` because the setup failed to produce a measurable install-lift answer; this is not evidence that Facebook groups themselves cannot work.
- No new experiment or asset was created. This cycle corrected the operating record so future reviews no longer treat live distribution work as queued or absent.

#### Experiments Reviewed

1. **rb-he-aso-001** (unscored) — live and measuring; collect the actual publish timestamp and App Store Connect Israeli-storefront baseline, then set the 21-day readout date.
2. **rb-he-comm-001** (unscored) — live 2026-07-05, closed inconclusive 2026-07-12; do not repeat without unique per-group campaign links, confirmed analytics access, and a same-day manual engagement log.

No third experiment was selected. This was a status-reconciliation cycle, and no additional scored candidate had current evidence or an approved asset ready to run.

#### Blockers

- WP-31: actual App Store Connect publish timestamp and Israeli-storefront baseline/export are missing.
- WP-32: primary install-lift result remains unknowable for the completed window because attribution and App Store Connect access were not in place before publish.

#### Next Week Focus

- Record WP-31's actual publish timestamp, calculate its 21-day close date, and pull the Israeli-storefront baseline/current comparison.
- Keep WP-32 closed. Carry its measurement-design requirements into any future community experiment before another post publishes.

---

### Week of 2026-07-07 — ResumeBuilder iOS — Hebrew-First Distribution Catch-Up (WP-31, WP-32)

**Status:** Catch-up cycle. Two experiments (WP-31 Hebrew ASO, WP-32 Facebook-groups community) were founder-approved/requested on 2026-07-04/05 and executed in the field, but had not been logged into `experiment-log.md` or this review — this entry closes that gap per the 2026-07-09 CEO review finding ("Distribution blind spot").

#### Metrics This Week

| Metric | This Week | Prior Week | Notes |
|---|---|---|---|
| RunSmart real activation (D7) | 0% (readout #2, 2026-07-05) | 0% | Inside EXD-015 30-day window, closes 2026-08-01 |
| Resumely real activation (D7) | 0% (readout #2, 2026-07-05) | 0% | Same window; traffic is the confirmed constraint, not the funnel (WP-30 evidence) |
| Resumely weekly launches | 5 (latest) | 28 (prior) | Trend: 6→16→28→5, per WEEKLY-CEO-LATEST 2026-07-09 |
| WP-32 Israeli storefront installs, before/after | not yet pulled | — | Window closes 2026-07-12; App Store Connect export still needed |
| WP-32 manual engagement log | not yet captured | — | Comments/reactions/replies on the 3 posted groups not yet logged |

#### What Happened

- rb-he-aso-001 (Hebrew ASO) promoted to WP-31 on 2026-07-04 after founder approved `hebrew-first-playbook.md`. Status: ready, not started — no asset pack drafted yet.
- rb-he-comm-001 (Facebook-groups community) promoted to WP-32 on 2026-07-05 at founder's explicit request, posted ahead of WP-31 (sequencing override, noted in the packet). Founder manually posted in 3 Israeli job-seeker/tech groups: `israel.hitech.jobs`, `israel.hightech`, and group `1684554685829832`.
- 2026-07-08 evidence audit found two open gaps against WP-32's acceptance criteria: (1) no draft post pack filed under `distribution-os/projects/resumebuilder/scaffold/drafts/` — posts went live without an in-repo asset pack; (2) no manual engagement log or App Store Connect before/after read captured yet.
- Both experiments added to `experiment-log.md` Active table this cycle (previously untracked there); `distribution-command-center.md` This Week and ResumeBuilder channel status updated to reflect the real state (Hebrew market: planned → measuring).
- No channel-level or experiment-level score exists yet for rb-he-aso-001 / rb-he-comm-001 in the playbook's experiment menu — logged as unscored rather than inventing a number.

#### Top 3 Experiments (this cycle)

1. **rb-he-comm-001** (unscored) — Facebook-groups posting; measuring, 7-day window closes 2026-07-12.
2. **rb-he-aso-001** (unscored) — Hebrew ASO pass; founder-approved, asset pack not started.
3. **rs-onboarding-001** (score 21) — Held behind WP-40 HealthKit activation per EXD-021; RunSmart's active lever this week is WP-40, not this queued item.

#### Blockers

- WP-31: RTL PDF export status needs product-QA confirmation before any Hebrew ASO copy references it.
- WP-32: target-group shortlist for future posts and the manual engagement log for the 3 already-posted groups are founder-only inputs, not yet supplied.
- Both: App Store Connect Israeli-storefront install export needed to compute before/after lift; not available in this environment.

#### Next Week Focus

- Founder: log WP-32 engagement (comments/reactions/replies) and pull the Israeli-storefront install comparison once the 2026-07-12 window closes.
- Agent: draft the WP-31 Hebrew ASO asset pack (subtitle, keywords, promo text, 5 captions, reviewer note) so it is ready for founder review the moment RTL PDF export is confirmed.
- Feed WP-32's 2026-07-12 readout back into `hebrew-first-playbook.md` Progress log and this review.

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
