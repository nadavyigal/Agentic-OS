# Work Packet WP-32 - Resumely: Community / FB-Groups Distribution Experiment (rb-he-comm-001)

- Status: Closed — inconclusive (measurement design failed; 2026-07-12)
- Created: 2026-07-05
- Source: Founder request 2026-07-05 ("start posting in facebook groups to try using the app"), promoting `rb-he-comm-001` from `distribution-os/projects/resumebuilder/scaffold/hebrew-first-playbook.md`
- Mode: Builder drafts + founder publish gate
- Workflow pattern: one story at a time (draft asset pack → founder review → founder publishes manually → measure)
- Outcome loop: Resumely 20% real activation / 30 days (EXD-015); current constraint is traffic, not funnel (WP-30 evidence, confirmed again by readout #2 — Resumely weekly launches 6→16→28→5)
- Related: WP-30 (measurement integrity + distribution decision), WP-31 (Hebrew ASO pass, running in parallel), `hebrew-first-playbook.md` Asset Recipe #3 ("Founder-Led Local Post Pack") and Experiment Menu row `rb-he-comm-001`

## Sequencing note

The playbook lists `rb-he-comm-001` as "do after ASO is live" (WP-31). Founder has explicitly asked to start community posting now, in parallel rather than sequentially — noted here as an intentional override, not a process violation. If WP-31's ASO copy publishes first, reuse its approved claims/wording in the community posts for consistency.

## Project(s)

- Distribution asset drafting: this repo (`distribution-os/projects/resumebuilder/`)
- Canonical marketing copy source: ResumeBuilder iOS repo `.agents/product-marketing.md` (last updated 2026-06-28)
- Publish target: Facebook groups (Israeli job-seeker / tech communities), founder's own account only

## Task

Produce the Founder-Led Local Post Pack (playbook Asset Recipe #3), adapted for Facebook groups specifically:

1. **One Hebrew Facebook post**, Fit-First-led framing (matches the approved English promo: "Check your fit before you apply..."). No outcome guarantees, no "beats ATS" framing (per Resumely-Battlecard / EXD-012).
2. **A "permission-first" variant** for groups where posting requires admin approval or isn't the founder's own group — shorter, clearly discloses it's the founder's own product, asks permission where the group requires it.
3. **A target group shortlist** (3-5 real Israeli job-seeker / tech Facebook groups the founder has actual context in) — do not invent groups; founder supplies or confirms this list.
4. **A reviewer note** flagging any claim needing verification before posting (same RTL PDF export caveat as WP-31 — do not promise RTL export in the post unless confirmed).
5. **A measurement plan**: since Facebook groups don't carry UTM-trackable links reliably, use App Store Connect Israeli-storefront install lift (same signal as WP-31) plus a manual log of post engagement (comments/reactions) and any direct replies mentioning trying the app.

## Constraints

- Founder-only publish gate — no automated posting, no scheduling tools, no paid boosting.
- One post per group per week max — no spam pattern across groups.
- Words to avoid (per canonical marketing doc + Hebrew playbook): "עוקף ATS", "ציון ATS רשמי", "מבטיח ראיונות" / any outcome guarantee.
- No paid acquisition (per EXD-009 / distribution rules — organic only until activation is proven).
- No new dependencies. No secrets in code.

## Acceptance

- Draft post pack complete (main post, permission-first variant, group shortlist, reviewer note, measurement plan).
- Founder reviews and either approves for manual posting or requests revisions.
- Once posted: track via App Store Connect (Israeli storefront installs) + manual engagement log for 7 days per the playbook's `rb-he-comm-001` time box.

## Validation

- Before posting: founder confirms the target groups are ones they have real standing/context in (not cold blasts).
- After posting: 7-day window, compare Israeli storefront installs before/after; log qualitative replies.
- Feed results back into `hebrew-first-playbook.md` Progress log and this packet.

## Progress

- 2026-07-05: Packet created from founder request during weekly review. Not started.
- 2026-07-05: Founder posted the community experiment manually in three Facebook groups:
  - `https://www.facebook.com/groups/israel.hitech.jobs/posts/10162695610290807/?notif_id=1783240698437026&notif_t=group_post_approved&ref=notif`
  - `https://www.facebook.com/groups/1684554685829832/posts/2072696087015688/?notif_id=1783240478117588&notif_t=group_post_approved&ref=notif`
  - `https://www.facebook.com/groups/israel.hightech/posts/10163521132537677/?notif_id=1783240597243645&notif_t=group_post_approved&ref=notif`
  Verification note: URLs are founder-supplied approved-post links; Facebook content fetch was blocked from this environment, so post body/engagement could not be independently read. Next evidence to collect: 7-day Israeli storefront install lift, comments/reactions, direct replies, and any qualitative fit/activation signal.
- 2026-07-08: Evidence audit (no founder input required). Publish step verified: three founder-supplied post URLs remain the only live evidence; target groups identified as `israel.hitech.jobs`, `israel.hightech`, and numeric group `1684554685829832`. Facebook group endpoints resolve (HTTP 200) but post bodies and engagement counts are not machine-readable from this environment. Gaps still open vs acceptance: (1) no draft post pack filed under `distribution-os/projects/resumebuilder/scaffold/drafts/` — posts went live without a committed asset pack in-repo; (2) no manual engagement log or App Store Connect Israeli-storefront before/after read captured yet. Measurement window closes **2026-07-12**; feed results back to `hebrew-first-playbook.md` Progress log when complete.
- 2026-07-12: **Closed — inconclusive.** An authenticated, read-only Facebook check of all three canonical post URLs found:
  - `israel.hitech.jobs`: 1 visible reaction, 0 comments.
  - `1684554685829832` (`Vibe Coding - Israel`): 2 visible reactions, 1 comment; no visible qualitative product feedback was available in the loaded post view.
  - `israel.hightech`: 0 visible reactions, 0 comments.
  - Total: **3 visible reactions, 1 comment, 0 visible qualitative product-feedback replies**.
  App Store Connect redirected to login and no local ASC API/reporting path exists, so Israeli-storefront installs before/after remain `unknown`. The experiment therefore did not produce a measurable answer to its stated hypothesis. This is a failure of the experiment's attribution and evidence design, not evidence that Facebook groups cannot work.

## Closeout Verdict

- **Decision:** Do not repeat this exact experiment setup.
- **Why:** Engagement was too weak to supply qualitative learning, and the primary install-lift metric was unavailable at closeout.
- **Next-time requirement:** Before any new community post, use one unique trackable App Store campaign link per group (or another verified attribution path), confirm App Store Connect analytics access before publishing, and keep a same-day manual engagement log.
- **Acceptance deviations:** The posts were published before the planned in-repo draft/review sequence, no draft post pack was committed, and the ASC comparison could not be completed. These deviations are preserved rather than backfilled after the fact.
