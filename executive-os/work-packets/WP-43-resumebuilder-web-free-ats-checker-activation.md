# WP-43 — ResumeBuilder Web Free ATS Checker Entry-Funnel Activation (Tier A)

- **Status:** Ready for execution — PR open, not yet merged
- **Mode:** Builder
- **Workflow pattern:** normal, one story at a time
- **Input trust:** trusted local context, live product walkthrough evidence
- **Project:** ResumeBuilder AI (Web), `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`
- **PR:** [nadavyigal/new-ResumeBuilder-ai- #115](https://github.com/nadavyigal/new-ResumeBuilder-ai-/pull/115) on branch `docs/wp-43-free-ats-checker-activation`
- **Full packet:** `tasks/work-pack-wp-43-free-ats-checker-entry-activation.md` in the product repo (on the PR branch)
- **Companion packet:** WP-44 (iOS upload activation) — same activation loop, web + iOS twin findings
- **Success signal:** higher share of landers who reach `ats_checker_submitted`; fewer sessions that select a resume but never submit

## Source

Live cold first-time-user walkthrough of resumelybuilderai.com (Claude session, 2026-07-11). Not a code-read audit — an actual browser walkthrough via the entry funnel, including a real 32-word paste test against the "Minimum 100 words" gate.

## Finding

The first-value gate is heavier than the hero's promise. To see any score, a cold user must clear a native unstyled PDF file input AND paste 100+ words of a job description — two non-trivial inputs before any payoff. Supporting friction: no above-the-fold CTA, account/login copy surfacing before the tool, disabled-button state unexplained, and a LinkedIn-URL path that silently returns a garbage low score (datacenter-IP thin-scrape, already documented in this repo's own history).

Cross-surface signal: the iOS app's Home screen already solves this (above-fold CTA, styled dropzone, "PDF or DOCX up to 5MB", Step-1-of-3 disclosure). This packet ports that proven pattern to web.

## Six Tier A stories (copy/design + client-only, no backend changes)

1. Above-the-fold "Check my resume" CTA that scrolls to the upload card.
2. Rebrand the raw native file input as a styled dropzone with PDF-only + size copy stated up front.
3. Show both requirements (resume + job description) as a live checklist instead of one hint at a time.
4. Nudge users under the 100-word count toward the backend-supported URL path.
5. Warn inline when a pasted URL is a LinkedIn link (documented scrape failure).
6. Move "Already have an account? Log in" below the tool on mobile.

Backend-dependent items (DOCX support on the free path, resume-only first score before the JD ask) are explicitly parked as Tier B in the full packet — not silently dropped.

## Next step

Execute via Codex or Cursor from the PR branch. Ties to the existing Resumely funnel re-read scheduled 2026-07-18 / 07-25 — new event `ats_checker_hero_cta_clicked` plus existing `ats_checker_submitted` volume are the measurement.
