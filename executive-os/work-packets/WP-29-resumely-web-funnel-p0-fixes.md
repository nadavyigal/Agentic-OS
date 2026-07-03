# Work Packet WP-29 - Resumely Web: Fix the 4 P0 Funnel Breaks (Demo 1 findings)

- Status: **BLOCKED — S1 fixed the wrong route, original P0-1 crash confirmed live on production 2026-07-03 13:04 UTC.** All 7 stories merged to main and deployed; needs an S8.
- Created: 2026-07-03
- Source: Builder OS vault `02-Products/ResumeBuilder/2026-07-03-resumely-ux-walkthrough-friction-report.md` (PR #17, merged branch `claude/peaceful-mendeleev-04b751`) — full production browser walkthrough by Claude (Fable 5), every P0 verified twice
- Mode: Builder
- Workflow pattern: one story at a time (implement → lint+tests → evidence → next)
- Input trust: trusted internal (findings reproduced live against production 2026-07-03)
- Outcome loop: Resumely 20% real activation / 30 days (founder decision 2026-07-02)
- Related: WP-13 (fit-first flip), WP-21 (ResumeBuilder observability), vault [[2026-07-02-priority-reset-resumely-primary]]
- Success signal: a first-time web user can complete landing check → signup → carried-over results → full optimization → export with zero crashes, zero raw i18n keys, no lost input; verified by a repeat browser walkthrough against production

## Model Routing (per GLOBAL-TOOL-USAGE.md tiers)

Cheapest capable model per story; Opus only where correctness/judgment is the risk.

| Story | Work type | Route |
|---|---|---|
| S1 crash fix | Hard debugging, correctness-critical React context/provider | **Opus** (Claude Code) |
| S2 EN i18n keys | User-facing conversion copy against an existing he.json structure | **Sonnet** |
| S3 word-count + error surfacing | Feature fix against established pattern (shared constant, error mapping) | **Sonnet** (Codex also fits) |
| S4 upgrade CTA decision + fix | Founder decision first; then small scoped change | **HUMAN gate → Sonnet** |
| S5 carry anonymous session through signup | Cross-boundary data flow (anon session → authed user), needs design judgment | **Opus** design + **Sonnet** implementation |
| S6 cleanup batch (overflow, CSP, empty states, stop-phrases) | Mostly mechanical, well-specified edits | **Haiku** or Codex background; CSP change reviewed by **Sonnet** code-reviewer |
| S8 fix (wrong route wrapped in S1) | Correctness-critical: same class of bug as S1, on the actual production route | **Cursor** (assigned 2026-07-03, founder-executed — second attempt at the original crash) |
| Final validation walkthrough | Browser QA re-run + report | **Sonnet** (/qa-only) |

Repo subagents are already model-pinned (ResumeBuilder scaffolding PR #94); use them rather than ad-hoc prompts. Run S6 in a short, scoped session per the cost note (don't carry a huge context for boilerplate).

## Project

ResumeBuilder Web (Resumely)

Path: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`

## Goal

Remove the four production defects that structurally cap web activation, in impact order, without opening the monetization gate by accident and without bundling unrelated changes.

## Context

The 2026-07-03 walkthrough found the web funnel broken at four independent points. Each was reproduced twice on production. Grounding already done (2026-07-03, main branch of the web repo):

1. **Crash:** `/dashboard/optimizations/[id]` — `useSectionSelection must be used within SectionSelectionProvider`. Grep hits: `src/app/[locale]/dashboard/optimizations/[id]/page.tsx`, `src/components/design/DesignRenderer.tsx`, `src/components/chat/ChatSidebar.tsx`. A component using the hook renders outside its provider. Deterministic; "Try again" and reload reproduce.
2. **Missing EN i18n:** `landing.score.mainIssues.*` and `landing.popup.*` exist **only** in `src/messages-overrides/funnel/he.json`. There is no EN sibling (`grep -c mainIssues src/messages/en.json` → 0). English users see 30+ raw keys at the results/signup moment. Console: `MISSING_MESSAGE: landing.score.mainIssues (en)`.
3. **Word-count mismatch:** landing widget enforces/labels "Minimum 80 words" client-side; `src/app/api/public/ats-check/route.ts:99` rejects `wordCount < 100` with a clear message the client discards, then the client resets the form (uploaded file + JD lost) and shows the wrong error ("Add a job description (text or URL) to continue.").
4. **Upgrade dead end:** signed-in `/pricing` → "Upgrade to Premium" → silent redirect to `/dashboard`. NOTE: monetization is deliberately gated (`Monetization Branch Tracker`, Gate A not open). The bug may be an intentionally-gated flow presented as a live CTA. Do not wire Stripe without the founder's explicit call (see S4).

## Read First

- Builder OS vault `02-Products/ResumeBuilder/2026-07-03-resumely-ux-walkthrough-friction-report.md` (all 12 findings + evidence notes)
- Web repo `tasks/lessons.md` and `tasks/ERRORS.md`
- `src/messages-overrides/funnel/he.json` (structure the EN file must mirror)
- `Monetization Branch Tracker` (vault) before touching S4

## Task

### S1 — Fix the optimization review crash (P0-1) — **Opus**
Wrap the offending tree in `SectionSelectionProvider` (or move the hook consumer inside it). Add a regression test that renders the review page route with a real fixture. Acceptance: `/dashboard/optimizations/[id]` renders for a fresh review; error boundary no longer triggers; test passes.

### S2 — Add the missing EN funnel messages (P0-2) — **Sonnet**
Create the EN sibling of `src/messages-overrides/funnel/he.json` with conversion-quality copy for every `landing.score.mainIssues.*` and `landing.popup.*` key (match canonical Fit/Match positioning per iOS repo `.agents/product-marketing.md`; do not reintroduce "ATS score" phrasing). Add a CI guard or test that fails when locale key sets diverge between en and he. Acceptance: results screen + popup fully rendered in EN; `MISSING_MESSAGE` gone from console; key-parity check in CI.

### S3 — Align word-count validation and stop destroying input (P0-3) — **Sonnet**
Single shared minimum (100) used by both the widget label/enable-state and `api/public/ats-check`; surface server `error` strings verbatim in the widget; on any ats-check failure, preserve the uploaded file and JD text (no form reset). Acceptance: a 90-word JD is blocked client-side with the real requirement shown; a forced server 400 shows the server message and loses nothing.

### S4 — Resolve the upgrade CTA dead end (P0-4) — **HUMAN gate, then Sonnet**
Founder decision required first: (a) hide/disable "Upgrade to Premium" until Gate A opens (recommended; consistent with the monetization gate), (b) replace with a waitlist/notify-me, or (c) wire real checkout (opens Gate A early; contradicts the 2026-07-02 gate schedule; do NOT choose without updating the gate decision in DECISIONS.md). Implement the chosen option. Acceptance: no signed-in user ever clicks a paying CTA that silently no-ops.

### S5 — Carry the anonymous check into the new account (P1-6) — **Opus design, Sonnet implementation**
The anonymous check already returns a `sessionId`; persist it through signup (query param, cookie, or localStorage handoff) and attach the session's check to the new user so the dashboard and first optimization show their 43-style result instead of an empty state. Acceptance: landing check → "Create Free Account" → dashboard shows the pre-signup check; signup page's "Save your ATS checks" promise is true.

### S6 — Cleanup batch (P1-5, P1-7, P1-8, P2s) — **Haiku/Codex, Sonnet review on CSP**
- Mobile: eliminate 574px horizontal overflow at 375px viewport (both locales).
- CSP: allow self-origin template preview frames (`frame-src 'self'` scoped as tightly as possible) so `/api/v1/design/templates/{id}/preview` renders; verify no other frame use opens up.
- Keyword extraction: filter stop-phrases (e.g. "are hiring a") from public ats-check suggestions — the PR #80/#81 filter apparently doesn't cover this path.
- Copy: dashboard greeting for first-session users (not "Welcome back"), applications empty state ("Add your first job" not "No applications match your search"), don't render the red "0 words" error before input, decide "Work Email" → "Email".
Acceptance: each item verified in a browser; no unrelated files touched.

### S8 — Fix the real crash: wrong route was wrapped in S1 — **Cursor** (assigned 2026-07-03, founder-executed)
S1 wrapped `SectionSelectionProvider` around `src/app/[locale]/dashboard/optimizations/[id]/page.tsx` and added a regression test for that route. That route is not the one real users hit. The actual flow — landing check or dashboard "Start Full Optimization" → "Check My Match"/"Start optimization" — lands on the sibling route `src/app/[locale]/dashboard/optimization-reviews/[id]/page.tsx`, which imports and renders `DesignRenderer` (a `useSectionSelection` consumer, around line 307) with **no provider anywhere in the file**. Confirmed live on production 2026-07-03 13:04 UTC, reproduced twice (initial load + reload): full-page crash, "We Hit a Snag — useSectionSelection must be used within SectionSelectionProvider".

Task:
1. Wrap the render tree in `src/app/[locale]/dashboard/optimization-reviews/[id]/page.tsx` in `SectionSelectionProvider`, mirroring exactly how S1 did it in `optimizations/[id]/page.tsx` (see that file for the pattern — import path `@/hooks/useSectionSelection`).
2. Add a regression test that targets the **actual** `optimization-reviews` route — do not copy S1's existing test as-is, since that test passes today while the real route is still broken and would give false confidence again.
3. Evaluate whether `src/app/[locale]/dashboard/optimizations/[id]/page.tsx` is dead code (unreferenced by any live nav/redirect). If so, flag it for removal in a follow-up — its existence as an unused, already-correct decoy is exactly what let this slip through S1's own review, Codex's S6/S7 QA passes, and one earlier browser walkthrough before finally getting caught on this pass.

Acceptance: sign in, upload a resume, paste a 100+ word job description, click through to `/dashboard/optimization-reviews/{id}` — page renders the review with no error boundary, on first load and on reload. New regression test passes and fails on `main` without the fix (verify by temporarily reverting the wrap locally, confirming the new test catches it, then restoring the fix).

### Final validation — **Sonnet**
Re-run the /qa-only walkthrough against production (or preview deploy) covering the exact Demo 1 paths. Target: zero P0s, health score ≥ 80. File the delta report to the Builder OS vault and update the [[ResumeBuilder]] living page.

## Constraints

- One story at a time; lint + tests green before "done"; evidence in the story report.
- No deploy or migration without explicit founder "yes" in the current message.
- S4 must not open the monetization gate implicitly; the gate decision lives in DECISIONS.md.
- Exclude QA traffic from metrics: `nadav.yigal+fable-qa-jul03@gmail.com` and any `+fable-qa*` alias (memory: resumely-qa-test-account), per posthog-founder-account-exclusion.
- No new npm dependencies without asking. No secrets in code.
- Scope gate: if any story expands past 3 unexpected files, stop and surface.

## Validation

- Per-story acceptance criteria above, plus repo lint/test suite.
- Existing resume-optimizer eval harness must stay green (ResumeBuilder eval baseline, PR #91/#92).
- Final browser walkthrough report filed to the vault with score delta vs 55/100 baseline.

## Progress

- 2026-07-03: Packet created from Demo 1 findings (Builder OS PR #17). Not started.
- 2026-07-03: S1 completed in ResumeBuilder Web on branch `codex/wp29-s1-optimization-review-crash`. Current `origin/main` already wrapped the review tree in `SectionSelectionProvider`; added regression coverage that guards the route wrapper and proves the real `DesignRenderer`/`ChatSidebar` consumers fail without the provider and render with it. Validation: focused regression passed (2/2), targeted eslint passed, `git diff --check` passed, full `npm run lint` passed with existing warnings only, `npm run build` passed. `npx tsc --noEmit` still fails on pre-existing contract/security test typing and stale export errors, none in touched S1 files. S2 is next.
- 2026-07-03: S2 completed in ResumeBuilder Web on branch `codex/wp29-s2-en-funnel-messages`. Added EN `landing.score.mainIssues.*` and `landing.popup.*` funnel copy with Fit/Match positioning and no "ATS score" phrasing; added a focused runtime-message parity test for those critical EN/HE namespaces. Validation: JSON parse passed, focused parity test passed (2/2), `npm run check:i18n` passed, targeted eslint passed, `git diff --check` passed, full `npm run lint` passed with existing warnings only, `npm run build` passed. `npx tsc --noEmit` still fails on pre-existing contract/security test typing and stale export errors, none in touched S2 files. S3 is next.
- 2026-07-03: S3 completed in ResumeBuilder Web on branch `codex/wp29-s3-word-count-errors`. Added shared `PUBLIC_ATS_MIN_JOB_DESCRIPTION_WORDS = 100`, reused it in the landing widget and public ATS route, updated EN/HE base and funnel copy away from 80-word fallbacks, surfaced server `error` strings verbatim, and kept the upload form mounted so forced server failures preserve selected PDF and JD text. Added focused API/UI regression coverage for 90-word rejection and forced server 400 preservation. Validation: focused tests passed (6/6), `npm run check:i18n` passed, targeted eslint passed, `git diff --check` passed, full `npm run lint` passed with existing warnings only, `npm run build` passed. `npx tsc --noEmit` still fails on pre-existing contract/security test typing and stale export errors, none in touched S3 files. S4 founder decision gate is next.
- 2026-07-03: S4 completed in ResumeBuilder Web on branch `codex/wp29-s4-disable-premium-cta`. Founder chose option A; Agentic OS `DECISIONS.md` now records that Premium CTAs stay hidden/disabled until Gate A opens. Added central `MONETIZATION_GATE_OPEN = false`, disabled pricing/paywall/Expert Modes upgrade actions, preserved Expert Mode preview behavior, and guarded `/api/upgrade` with `403 MONETIZATION_GATE_CLOSED` so checkout sessions cannot be created while the gate is closed. Validation: focused pricing/upgrade tests passed (2/2), `npm run check:i18n` passed, targeted eslint passed, `npm run lint` passed with existing warnings only, `npm run build` passed. `npx tsc --noEmit` still fails on pre-existing contract/security test typing and stale export errors, none in touched S4 files. S5 is next.
- 2026-07-03: S5 completed in ResumeBuilder Web on PR #105 (`codex/wp29-s5-anon-session-handoff`). Added anonymous ATS score conversion through signup callback and dashboard surfacing. Validation reported in PR.
- 2026-07-03: S6 completed in ResumeBuilder Web on PR #106 (`codex/wp29-s6-cleanup-batch`). Fixed 375px mobile overflow, same-origin template preview CSP, stop-phrase filtering, initial 0-word styling, dashboard/application/auth copy, with focused tests and browser checks. Validation reported in PR.
- 2026-07-03: Final `/qa-only` validation rerun against PR #106 preview did **not** meet target. Health score **65/100** vs baseline 55/100; zero-P0 target failed because anonymous EN result still emits missing `landing.score.mainIssues.*` runtime keys, and Supabase signup returned `429`, blocking dashboard carryover plus signed-in review/export/applications validation. Delta report filed to Builder OS vault: `02-Products/ResumeBuilder/2026-07-03-wp29-final-validation-delta-report.md`. Next: add missing EN runtime keys, rerun locale parity against actual `MainIssuesSummary`, then rerun `/qa-only` with an account that can complete auth.
- 2026-07-03: **Root cause found for both remaining blockers (S7 needed before target can be met):**
  - **EN key gap, precise scope:** `MainIssuesSummary.tsx` (`src/components/ats/MainIssuesSummary.tsx:197`) reads a `baseKey` prop (`"landing.score.mainIssues"`, set in `src/components/landing/ATSScoreDisplay.tsx:114`) and calls `t('issueBadge')`, `t('pointsBadge')`, `t('whyLabel')`, `t('copy')`/`t('copied')`, `t('continueCta')`, plus the full `categories.{category}.{title,description,why,fallbackTerm,examples.example1,examples.example2}` subtree. S2 added only `title, subtitle, exampleLabel, continueTitle, continueDescription` — 5 of the ~15+ keys actually consumed. **This is not EN-specific: `src/messages-overrides/funnel/he.json` has the identical 5-key gap** — Demo 1 never caught it on Hebrew because that walkthrough tested the HE *dashboard*, not the HE anonymous-check result screen, so HE has been silently broken the same way since before WP-29 started. S7 must add the missing keys to **both** `en.json` and `he.json` under `landing.score.mainIssues`, matching every key `MainIssuesSummary` actually calls (grep `t(` calls in that file, not just what S2's parity test checked — the parity test apparently only compared the 5 keys S2 added, not the full runtime key set the component uses).
  - **Supabase 429:** confirmed this is Supabase Auth's own signup rate limit on the production project (`brtdyamysfmctrhuankn`), tripped by repeated QA signups across two sessions today (the 2026-07-03 Demo 1 walkthrough + this validation pass), not an application bug. Recommended unblock for QA (do not change production rate-limit config without the founder's call): create the next QA account via the Supabase Admin API (`supabase.auth.admin.createUser()` with the service-role key, already in `.env.local`) instead of the public `/auth/v1/signup` endpoint — the admin path bypasses the client-facing rate limiter. Wait ~1 hour if using the public signup form again.
- 2026-07-03: Global CLAUDE.md and MEMORY.md housekeeping from the Demo 2 OS review (unrelated to WP-29 code, noted here only because it changed session defaults): default session model for meta-work is now Sonnet-first per the routing policy; gstack skill routing narrowed to a 5-skill default set. Does not change WP-29 execution, which stays on Codex/Opus per the table above.
- 2026-07-03: **S7 completed** in ResumeBuilder Web on branch `codex/wp29-s7-mainissues-keys`. Added the full `landing.score.mainIssues` runtime key set to **both** `src/messages-overrides/funnel/en.json` and `he.json` (issueBadge, pointsBadge, whyLabel, copy/copied, continueCta, and all five `categories.*` subtrees). Tightened the parity test to assert every key `MainIssuesSummary` actually calls, not just the five keys S2 originally added. Validation: JSON parse passed, parity tests passed (4/4), `npm run check:i18n` passed, targeted eslint passed, `git diff --check` passed, `npm run build` passed. Next: merge S7, then rerun final `/qa-only` validation (use Supabase Admin API for QA signup to avoid 429 rate limit).
- 2026-07-03: **S7 (PR #107) independently verified by Claude — clean, recommend merge.** Read `MainIssuesSummary.tsx` directly and confirmed the 41-leaf-key set added matches exactly what the component consumes; ran `funnel-i18n-parity.test.ts` locally (4/4 pass); ran a live browser check against the PR's Vercel preview with a real anonymous ATS submission — zero console errors, zero `MISSING_MESSAGE`, full readable EN result screen. `ATS score` phrasing not reintroduced.
  - **Branch topology finding (not a regression, but blocks calling WP-29 done):** while QA'ing #107's preview, the "are hiring a" stop-phrase and "Work Email" label were still visible — both previously reported fixed by S6. Checked `git log origin/main`: main has only S1-S4 merged. **S5 (PR #105) and S6 (PR #106) are both still open/unmerged**, and PR #107 branched from `main` directly, not from #106 — so #107's preview never had S6's fixes to lose. The earlier 65/100 delta-report run tested #106's separately-branched preview, which does include them. **Three fix branches (S5, S6, S7) exist independently and have never been tested together**; no number reported so far (55→65, S7's clean pass) reflects what a real user sees once everything actually merges.
  - Recommended order: (1) merge #107 now, no reason to hold it; (2) reconcile/merge #105 and #106 into main (likely overlapping edits on the signup/dashboard surface — expect conflicts); (3) run the *one* final `/qa-only` pass against fully-merged main — that's the first real measurement against the ≥80 target; (4) use the Supabase Admin API for the QA account on that final pass to avoid the rate limit. Full writeup: vault `02-Products/ResumeBuilder/2026-07-03-wp29-final-validation-delta-report.md`.
- 2026-07-03: **Founder landed both remaining branches.** Tested a local scratch merge of S5+S6 onto post-S7 main first (both merged clean via git 3-way merge despite overlapping files — `FreeATSChecker.tsx`, `en.json`, `he.json`; verified merged state: valid JSON, parity test 4/4, `npm run check:i18n` 0 missing, `npm run lint` 0 errors, `npm run build` passed). Merged PR #105 (S5) then PR #106 (S6) via `gh pr merge --merge`. All 7 WP-29 stories now on `main` (`ede217b`) and deployed to production.
- 2026-07-03: **Real final validation against production (resumelybuilderai.com) — S1's crash fix does not cover the live route. WP-29 not done.**
  - **CONFIRMED FIXED in production:** signup label "Email" not "Work Email"; first-session dashboard says "Welcome, {name}" not "Welcome back"; Premium CTA on `/pricing` reads "Premium is not open yet" (no dead-end); applications empty state "Add your first job to start tracking applications"; mobile `/` at 375px has zero horizontal overflow (`scrollWidth === 375`); anonymous EN result screen previously verified clean on #107's own preview (production itself is now rate-limited for further anonymous checks from this test IP — 7-day cooldown, a working anti-abuse feature, not a bug).
  - **P0 STILL LIVE — original crash, root cause found:** signed in as a fresh QA account, ran "Start Full Optimization" → landed on `/dashboard/optimization-reviews/{id}` (note: **not** `/dashboard/optimizations/{id}`, the route S1 actually fixed) → full-page crash, "We Hit a Snag: useSectionSelection must be used within SectionSelectionProvider". Reproduced twice (initial load + reload). Root cause confirmed by reading source on current `main`: there are **two separate, similarly-named routes** — `src/app/[locale]/dashboard/optimizations/[id]/page.tsx` (S1 wrapped this one in `SectionSelectionProvider`, has the regression test) and `src/app/[locale]/dashboard/optimization-reviews/[id]/page.tsx` (imports and renders `DesignRenderer` at line ~307, **no provider import anywhere in the file**). The real user flow — landing check or dashboard "Start Full Optimization" → "Check My Match"/"Start optimization" — lands on `optimization-reviews`, not `optimizations`. S1's fix and its regression test both targeted the wrong route; the crash Demo 1 found has been live through the entire WP-29 execution.
  - **S8 needed:** wrap `src/app/[locale]/dashboard/optimization-reviews/[id]/page.tsx`'s render tree in `SectionSelectionProvider` the same way S1 did for `optimizations/[id]/page.tsx`; add a regression test targeting the actual `optimization-reviews` route (not a copy of S1's test, which would still pass while the real route is broken); consider whether `optimizations/[id]` is dead code that should be removed to prevent this exact mistake recurring.
  - Full writeup with screenshots and console traces: vault `02-Products/ResumeBuilder/2026-07-03-wp29-final-validation-delta-report.md`.
