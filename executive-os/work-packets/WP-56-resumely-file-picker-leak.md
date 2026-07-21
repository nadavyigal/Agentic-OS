# Work Packet WP-56 — Resumely file-picker abandonment

- Status: Open (queued behind WP-51)
- Mode: Builder
- Source: PostHog AI audit of project 270848 (2026-07-21), Section B8
- Workflow pattern: normal
- Input trust: trusted
- Loop: Resumely activation loop
- Signal: 27 people opened the file picker in 30 days; 13 selected a file. **A 48% abandonment at the single step where the user has already declared intent.** This is the largest upstream leak in the Resumely funnel.
- Memory update: `tasks/lessons.md` (Resumely iOS)
- Success signal: picker-open → file-selected conversion above 65% on a 4-week post-change read, measured against the 48% pre-change baseline
- Model route: Sonnet 5
- Rollback: Ship the text-paste fallback behind a flag; flipping it off restores the picker-only flow.

## Owner Role
Resumely iOS engineer

## Project
Resumely iOS — `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`

## Why This Is Queued Behind WP-51, Not Ahead Of It

Under EXD-022 the gate is ≥20 clean activations **on a working milestone**. This packet plausibly increases real activations; WP-51 makes them countable. Shipping this first would improve the product and leave the counter still stuck near zero, and the improvement would be unmeasurable — the exact trap the last month has repeatedly fallen into.

Land WP-51, then this.

## The Leak

Thirty-day funnel, from the audit and consistent with the canonical read:

```
Saw upload CTA        56
Tapped upload CTA     28   (50%)
Opened file picker    27   (96%)  <- intent is unambiguous here
Selected a file       13   (48%)  <- half walk away
Resume uploaded       13   (100%)
```

The 96% tap→picker and 100% select→upload rates matter: **the surrounding steps are healthy.** Nothing is broken in the CTA or the upload pipeline. The loss is entirely inside the picker interaction, among users who have already decided to upload a résumé.

## Hypotheses, Most Likely First

1. **No file to pick.** The user is on a phone, their résumé is in email, Google Drive, or a desktop machine. They open the picker, find nothing usable, and quit. This is the audit's leading hypothesis and it fits mobile behaviour.
2. **iCloud/Files navigation friction.** The iOS document picker opens somewhere unhelpful and the file is several taps away.
3. **Format expectation mismatch.** The picker filters to PDF/DOCX and their résumé is Pages, Google Docs, or a photo.
4. **They expected to paste text.** Reasonable for an AI product.

Hypotheses 1 and 4 have the same fix, which is why it is the recommended first move.

## Scope

1. **Add a "paste your résumé text instead" path** alongside the file picker, visible at the same moment rather than behind a secondary screen.
2. **Instrument the abandonment.** Add `resume_file_picker_cancelled` properties capturing time-in-picker and whether any directory navigation occurred, so hypothesis 2 becomes distinguishable from hypothesis 1. (The event already exists — 22 events, 9 persons — but carries nothing useful.)
3. **Consider an email-a-résumé-to-yourself hint** if hypothesis 1 dominates.

## Measurement Approach — Do Not A/B Test This

The audit correctly computes that a proper experiment on this step needs ~150 persons per variant, which at 51 picker-opens per 90 days would take roughly 18 weeks. **Do not run it as an A/B test.**

Ship the change directly and measure a 4-week pre/post comparison against the 48% baseline. The change has no plausible downside — adding an input method cannot make the picker worse — so the usual reason for a control group does not apply.

This is the same reasoning that applies to the audit's Experiments 1-3 generally: at current volume none of them can reach significance in a useful timeframe. Ship the no-downside ones directly, and use session replay (WP-55) plus a survey for the ones that need judgement.

## Out of Scope

- The export funnel (3 of 25 optimizers export). Real, worse in percentage terms, but downstream — fixing it while the upstream leak persists means optimizing for a smaller cohort.
- Any paywall or monetization change.
