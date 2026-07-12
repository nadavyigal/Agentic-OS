---
type: distribution-playbook
product: Resumely (ResumeBuilder)
status: approved
approved: yes
created: 2026-07-03
last_updated: 2026-07-04
owner: founder
adapted_from: distribution-os/projects/runsmart/scaffold/hebrew-first-playbook.md
channels:
  - Hebrew market
  - ASO
  - Web landing
  - Job-seeker communities
  - Content
related_experiments:
  - rb-he-aso-001
  - rb-he-web-001
  - rb-he-comm-001
source_notes:
  - distribution-os/projects/resumebuilder/scaffold/hebrew-program.md
  - .agents/product-marketing.md (ResumeBuilder iOS repo, last updated 2026-06-28)
  - executive-os/work-packets/WP-30-resumely-measurement-integrity-and-distribution.md (S5)
---

# Resumely — Hebrew-First Distribution Playbook

## Purpose

Use Israel as a focused, high-context acquisition loop for Resumely, the same way RunSmart's Hebrew-first playbook targets Israeli runners — here the audience is the Israeli job-seeker community. This packet exists because the 2026-07-03 PostHog read (WP-30) shows the constraint has flipped from funnel/UX to raw traffic: best week ever was 28 people, current week is 4.

Hebrew-first does not mean translating every English asset. It means the first public campaign is authored for Hebrew-speaking Israeli job seekers, measured separately where possible, and repurposed into English only after the Hebrew angle is clear.

## Source Facts

- Resumely helps job seekers check whether a role is worth applying to, tailor their resume to that job, and export a complete application package from their iPhone (source: `.agents/product-marketing.md`).
- Native iOS app with supporting web/backend services — unlike RunSmart, Resumely has a **live web funnel** too (currently broken client-side per WP-30 S1; do not launch a Hebrew web surface until S1 is verified fixed).
- Hebrew/RTL support is already a named differentiator and persona in the canonical marketing doc ("Hebrew-speaking job seeker... Authored Hebrew support and RTL-aware resume surfaces"), so this is not a net-new positioning bet — it is finishing a claim already made.
- `hebrew-program.md` (2026-05-28) has open, unresolved items that block a real launch: Hebrew App Store metadata not started, Hebrew screenshots not started, RTL PDF export end-to-end not confirmed, subdomain/path undecided, military-service resume field readiness unconfirmed.
- v1.2 build 7 is live (App Store, confirmed 2026-06-29). Free activation path — no paywall, no paid acquisition until post-1.2 funnel data is readable (approved marketing execution rule).
- Words to avoid per canonical doc: "pass ATS", "guaranteed", "beat the bots", "official ATS score", "get interviews", "auto-apply" — applies to Hebrew copy too, not just English.

## Core Hypothesis

If Resumely runs an authored Hebrew-first campaign across App Store metadata, one Hebrew landing surface (once web capture is fixed), and founder-approved local distribution in Israeli job-seeker communities, then Israeli storefront installs and Fit-First activation will improve within 21 days because the product will feel locally relevant and trustworthy before it asks for a resume upload.

## What Hebrew-First Means

1. **Authored Hebrew, not translated English.** Use Israeli job-market language: local job titles, military-service handling, education conventions — not literal translation (per `hebrew-program.md` principles).
2. **Local proof before scale.** Start with 20-50 qualified Israeli job seekers, career communities, or founder-adjacent contacts before broad SEO.
3. **App Store first, web second.** iOS is the conversion surface today. Do not build a Hebrew web landing page until WP-30 S1 (web capture fix) is verified live — otherwise the Hebrew web experiment is unmeasurable.
4. **Fit-First honesty, not score-inflation.** Lead with "check if this job is worth your effort" and "see what's missing," not "pass ATS" or "get more interviews."
5. **Permissioned community only.** Personal posts, warm asks, and job-seeker group partnerships are allowed. Spammy group drops are not.

## Audience

| Segment | Hebrew framing | Best first channel |
|---|---|---|
| Active job seeker (mass applying) | "מפסיק לשלוח קורות חיים גנריים - תדע קודם אם התפקיד מתאים לך" | App Store Hebrew screenshots, warm WhatsApp asks |
| Career switcher | "תראה מה חסר לך לפני שאתה משקיע זמן בהגשה" | Hebrew landing page (post-S1), career-switch communities |
| Recent grad / early career | "בנה חבילת הגשה שלמה מהטלפון - בלי לנחש מה חסר" | App Store metadata, campus/grad job groups |
| Hebrew-speaking job seeker wanting RTL | "עברית אמיתית, לא תרגום - כולל PDF בכיוון נכון" | App Store listing, RTL-aware screenshots |

## Message House

### One-Line Hebrew Positioning

בודקים אם התפקיד מתאים לך, לפני שאתה משקיע מאמץ בהגשה.

### Supporting Points

- תראה ציון התאמה והכוונה - Strong, Stretch או Skip - לפני שמתחילים לערוך.
- עריכות ממוקדות לקורות החיים שלך, לא שכתוב גנרי שנשמע כמו AI.
- חבילת הגשה שלמה - קורות חיים, מכתב מקדים - מוכנה מהטלפון.
- תמיכה מלאה בעברית, כולל PDF בכיוון נכון (RTL) — לא תרגום.

### English Back-Translation

Check whether the role fits you before you invest effort in applying.

### Words To Avoid

- "עוקף ATS" / "פותר את חוסמי ATS" — mirrors the English-doc rule against "pass ATS," "beat the bots."
- "ציון ATS רשמי" — the Resumely Match Score is Resumely's own estimate, not an employer ATS score.
- "מבטיח ראיונות" / "מבטיח תוצאה" — no outcome guarantees.
- Any Shabbat/holiday-specific scheduling claim — no such product behavior exists (same caution as the RunSmart draft's Shabbat note).

## Repeatable Weekly Loop

Same pattern as the RunSmart draft. Run as a one-week campaign whenever Hebrew market is the focus channel.

| Day | Work | Output |
|---|---|---|
| 0 | Pick one hypothesis and one metric | One experiment row selected from the menu below |
| 1 | Confirm product truth | App Store metadata, RTL PDF export, and claims verified against the live app — not assumed |
| 2 | Draft the asset | Hebrew ASO copy, landing brief (post-S1 only), or community post |
| 3 | Founder review | Draft marked reviewed or revised, no external publish yet |
| 4 | Founder publishes manually | Only after explicit approval in the current session |
| 5-7 | Measure and learn | App Store Connect + PostHog (excluding founder/QA per memory) + manual response notes logged |

Do not run more than one Hebrew experiment at a time until the metric source is stable — and do not start `rb-he-web-001` until WP-30 S1 is verified fixed live.

## Experiment Menu

| ID | Channel | Hypothesis | Primary metric | Time box | Decision |
|---|---|---|---|---|---|
| rb-he-aso-001 | Hebrew ASO | Authored Hebrew subtitle, keywords, promotional text, and Fit-First-led screenshots will lift Israeli storefront install rate | App Store Connect installs, Israeli storefront | 21 days after publish | Do first — no S1 dependency |
| rb-he-web-001 | Hebrew landing | A single Hebrew landing page with App Store CTA will convert local intent better than the English page | `web_landing_to_appstore_click_rate` (PostHog, `$lib='web'`) | 14 days after publish | **Blocked on WP-30 S1** |
| rb-he-comm-001 | Community | Founder-approved posts in permissioned Israeli job-seeker communities will produce qualified install traffic without spam | App Store clicks by campaign tag + manual reply log | 7 days | Do after ASO is live |

## Asset Recipes

### 1. Hebrew ASO Pass

Produce:
- Hebrew subtitle candidates, max 30 chars, Fit-First-led (not "ATS checker").
- Hebrew keyword field candidates, avoiding title/subtitle repeats.
- Hebrew promotional text, 170 chars max — adapt the approved English promotional text ("Check your fit before you apply...") rather than inventing new claims.
- Five Hebrew screenshot caption headlines: fit check, top gaps, targeted edits, application package, export.
- One reviewer note listing claims needing App Store Connect / product QA verification (especially RTL PDF export, per `hebrew-program.md` open question #2).

### 2. Hebrew Landing Page Brief (do not start until S1 verified)

Produce a brief only, not code, unless explicitly asked. Required: Hebrew hero on "check your fit first," three feature blocks (fit check, tailored edits, application package), App Store CTA with campaign tracking, FAQ clarifying Resumely does not guarantee interviews or claim an official ATS score, measurement plan (pageview, CTA click, install if trackable, Fit-First completed).

### 3. Founder-Led Local Post Pack

Produce: one founder LinkedIn/Facebook post in Hebrew, one WhatsApp personal message for one-to-one sends, one "ask permission first" variant for job-seeker groups where the founder has context.

## Open Questions to Resolve Before Publishing (from `hebrew-program.md`, still unresolved as of 2026-07-03)

1. Subdomain/path for Hebrew web (`he.` vs `/he`) — not decided, and moot until S1 lands.
2. Is RTL PDF export confirmed end-to-end in the iOS app? — not confirmed, blocks any Hebrew ASO claim about RTL export.
3. iOS Israeli-market pricing (USD/ILS) — free activation path currently, likely N/A short-term.
4. Military-service resume field readiness — confirm before Hebrew ASO promises "kesher tzva'i" handling.

## Constraints

- No paid acquisition (per approved marketing execution rules — free activation path until post-1.2 funnel data readable).
- No Hebrew web experiment until WP-30 S1 is verified fixed via live PostHog query.
- No claims (RTL export, keyword parsing, outcome guarantees) beyond what product QA confirms.
- Founder-only publish gate — no automated posting.

## Decision Needed (WP-30 S5)

Per WP-30, this draft playbook is the "(a) adapt Hebrew-first" option. Choosing it means: promote `rb-he-aso-001` (Hebrew ASO pass) to its own work packet this week, since it has no dependency on S1 and is the fastest path to the first live channel. `rb-he-web-001` stays queued behind S1.

## Progress

- 2026-07-03: Drafted from RunSmart's `hebrew-first-playbook.md` structure + `.agents/product-marketing.md` canonical copy + `hebrew-program.md` open items. Not approved, not promoted to a work packet.
- 2026-07-04: **Founder-approved.** `rb-he-aso-001` promoted to [WP-31](../../../executive-os/work-packets/WP-31-resumely-hebrew-aso-pass.md) (WP-30 S5). `rb-he-web-001` remains blocked on WP-30 S1 final production verification.
- 2026-07-12: `rb-he-comm-001` / [WP-32](../../../executive-os/work-packets/WP-32-resumely-community-distribution-experiment.md) closed **inconclusive**. Three posts produced 3 visible reactions and 1 comment total, with no visible qualitative product feedback. Israeli-storefront install lift is unknown because ASC analytics was unavailable at closeout. Do not rerun the same setup; require unique per-group campaign links, verified analytics access before publish, and a same-day engagement log.
