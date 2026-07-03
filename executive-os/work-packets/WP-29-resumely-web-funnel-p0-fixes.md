# Work Packet WP-29 - Resumely Web: Fix the 4 P0 Funnel Breaks (Demo 1 findings)

- Status: **IN PROGRESS** (S1-S2 complete 2026-07-03; S3 next)
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
