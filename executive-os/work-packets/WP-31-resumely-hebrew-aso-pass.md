# Work Packet WP-31 - Resumely: Hebrew ASO Pass (rb-he-aso-001)

- Status: **READY** (created 2026-07-04, not started)
- Created: 2026-07-04
- Source: WP-30 S5 decision (2026-07-03/04) — Hebrew-first distribution chosen as the first channel to ship; `rb-he-aso-001` promoted here because it has no dependency on web capture (WP-30 S1, done) and is the fastest path to a live channel.
- Mode: Builder + founder publish gate
- Workflow pattern: one story at a time (draft → founder review → founder publishes manually → measure)
- Outcome loop: Resumely 20% real activation / 30 days (founder decision 2026-07-02); current constraint is traffic, not funnel (WP-30 evidence)
- Related: WP-30 (measurement integrity + distribution decision), `distribution-os/projects/resumebuilder/scaffold/hebrew-first-playbook.md` (draft, not yet approved), `distribution-os/projects/resumebuilder/scaffold/hebrew-program.md` (prior open items)

## Project(s)

- ResumeBuilder iOS (App Store Connect metadata): `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`
- Canonical marketing copy source: `.agents/product-marketing.md` in the ResumeBuilder iOS repo (last updated 2026-06-28)

## Task

Produce the Hebrew ASO asset pack per the playbook's Asset Recipe #1:

1. Hebrew subtitle candidates (max 30 chars each), Fit-First-led — not "ATS checker" framing.
2. Hebrew keyword field candidates, avoiding repeats of title/subtitle words.
3. Hebrew promotional text (170 chars max) — adapt the approved English promo text ("Check your fit before you apply. Resumely shows what is missing, helps tailor your resume, and exports a complete application package from your iPhone."), do not invent new claims.
4. Five Hebrew screenshot caption headlines, following the fit check → top gaps → targeted edits → application package → export sequence.
5. One reviewer note flagging every claim that needs App Store Connect or product QA verification before publish — RTL PDF export end-to-end status is unconfirmed (open item #2 in `hebrew-program.md`) and must be checked before any Hebrew ASO copy references it.

## Constraints

- Founder-only publish gate — draft only, no automated App Store Connect submission.
- Words to avoid (per canonical marketing doc + Hebrew playbook): "עוקף ATS", "ציון ATS רשמי", "מבטיח ראיונות" / any outcome guarantee, Shabbat/holiday-specific scheduling claims (no such product behavior exists).
- No paid acquisition — this is ASO/organic only, per approved marketing execution rules.
- No new dependencies. No secrets in code.

## Acceptance

- Draft asset pack complete (subtitle, keywords, promo text, 5 captions, reviewer note).
- Reviewer note explicitly lists any claim needing verification, with RTL PDF export flagged.
- Founder reviews and either approves for manual publish or requests revisions.
- Once published: track via App Store Connect analytics (Israeli storefront impressions/installs) — no PostHog dependency for this story, since ASO conversion happens pre-install.

## Validation

- Before publish: founder confirms RTL PDF export status with product QA.
- After publish: 21-day window per the playbook's experiment menu (`rb-he-aso-001`), then compare Israeli storefront install rate before/after in App Store Connect.

## Progress

- 2026-07-04: Packet created from WP-30 S5 decision. Not started.
- 2026-07-04: Founder approved `distribution-os/projects/resumebuilder/scaffold/hebrew-first-playbook.md` (frontmatter `approved: yes`). Cleared to start.
