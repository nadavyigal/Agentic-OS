# Work Packet WP-12 — Resumely ATS Next Priority: Land the Fit-First Triage Wedge

- Status: **Stories 0–4 complete + E2E gate closed — PR #75 blocked on a merge conflict (rebase needed)**

## Progress (2026-06-23)
- **E2E Gate — CLOSED.** Live call to `https://www.resumelybuilderai.com/api/public/ats-check` returned `fit` block; `FitVerdict` decoded as: band=`.stretch`, score=62, topGaps=["redis","terraform","kubernetes"], missingKeywords=["AWS","CI/CD","Docker"]. Band matches server verdict. `FitVerdict.swift` now has `decodeGapsOrStrings`/`decodeKeywordsOrStrings` helpers handling both object-array and string-array API responses.
- **Story 1 (iOS) — DONE, merged (#74, squash `08:59Z`).**
- **Story 0 (web) — DONE, merged (#87, `cf7bdf5` `09:05Z`).** `/api/public/ats-check` serves `fit` in prod.
- **Stories 2-4 (iOS) — built on `feat/wp-12-fit-first-stories-2-4`, PR #75 open.** BUILD SUCCEEDED. 20 analytics events (contract test updated). `isFitCheckEnabled=false`. Flag gating reviewed correct (flag-off = original path unchanged).
- **HE localization — VERIFIED (structural).** All 21 new `.xcstrings` keys carry real Hebrew values (e.g. "Strong Fit" → "התאמה חזקה"); EXD-012 disclaimer localized. Run the xliff export as final confirmation, but coverage is real.
- **⚠ MERGE BLOCKER — PR #75 is CONFLICTING (rebase required).** The branch was cut from `2cb55a9`, *before* #72/#73/#74 merged, so it re-implements Story 1 and is missing #72's `DomainModels` additions (`KeywordSuggestionPreviewDTO`, `JSONValue.displayString`). A naive "take branch" merge would DELETE #72's feature. Resolution = rebase onto `origin/main`, UNION `DomainModels.swift` (keep #72's additions AND the branch's `ATSScoreResult.fit`), keep the branch's evolved `FitVerdict.swift` (+213, E2E decoder fix supersedes #74's +176), then rebuild + smoke + merge.
- **Remaining to land #75:** rebase/resolve (above) → rebuild + full tests → simulator smoke (iPhone 17 + SE, flag temporarily on) → merge. Then mark WP-11 Prompt 3 DONE.
- Created: 2026-06-23
- Source: ResumeBuilder iOS PR #73 (strategy + Fit-First Triage feature plan); web ATS pipeline complete through PR #85 (`5879b6b`)
- Workflow pattern: feature (multi-repo, build-ordered)
- Input trust: trusted (derived from live PR contents + git state 2026-06-23)
- Outcome loop: Resumely activation / D7 — first-touch fit verdict before optimize
- Supersedes: WP-11 Prompt 3 (ATS next priority) — this is the chosen next priority
- Related: WP-10 (match-score positioning gaps — claim-defensibility guardrail still applies); EXD-012 (no external/vendor ATS score claim)
- Success signal: `/api/public/ats-check` returns an additive `fit` block (verdict + gaps + missing keywords); iOS ships a paste-JD → Strong/Stretch/Skip verdict front door behind `isFitCheckEnabled`; zero regression to existing optimize flow; no copy implies an external ATS-vendor score

---

## Why this packet exists

The web ATS matching pipeline is now solid — keyword atomization (#82), in-context suggestions (#83), and junk-phrase filtering (#85, merged `5879b6b`) are all on `main`. The matching quality work is done. The next leverage is **not** more matching accuracy; it is a new front door that uses the data we already compute: a fit verdict *before* the user spends effort optimizing.

PR #73 resolved the strategy and the build plan. This packet consolidates it into an executable sequence and names the gates.

## What is already done (do not redo)

- Web `POST /api/public/ats-check` already: free, anonymous (`x-session-id`), rate-limited (5/7 days/IP), caches in `anonymous_ats_scores`, runs `scoreResume` + `extractJob`, returns `score.overall`, ranked `suggestions`/`preview`, `quickWins`, and `must_have` requirements. The verdict + gaps are a **derivation** on top of these — not new ML.
- Web ATS keyword quality: #82, #83, #85 merged.
- iOS per-keyword preview approval UI: PR #72 (open) — see Pre-flight.

## DECISION GATE — RESOLVED 2026-06-23 (founder, see DECISIONS.md)

1. **Verdict thresholds — LOCKED:** `≥75 = Strong`, `50–74 = Stretch`, `<50 = Skip`. Server-owned, tunable post-ship.
2. **Resume-input contract — LOCKED:** keep the existing **PDF re-upload** contract to `/api/public/ats-check`. A stored `resume_id` is a flagged follow-up, not in scope for WP-12.

> Gate cleared. Story 0 and the iOS sequence are fully unblocked.

## Pre-flight (housekeeping) — DONE 2026-06-23

- [x] **PR #73 merged** (iOS) — strategy memo + Fit-First spec/stories now on iOS `main` as source of record.
- [x] **PR #72 merged** (iOS per-keyword preview approval UI) — kept; it lives in the existing Improve flow that Fit-First routes *into*, not superseded.
- [x] **Web ATS plan docs merged** — #84 closed (diverged branch / phantom conflict), re-cut clean as #86 and merged to web `main`.

## Build sequence (each story ends on a green build, independently testable)

> Story 0 (web) lands first so the `fit` fields exist; iOS Stories 1–3 build against a mocked `FitCheckService` in parallel, then point at the live endpoint.

### Story 0 — Web: add the Fit layer to the free ATS check — **M**
Repo: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`
- `src/app/api/public/ats-check/route.ts`: in `formatResponse`, add an **additive** `fit` block — `verdict` (band from `score.overall`), `scoreNote`, `topGaps`, `missingKeywords` (from `extractJob` `must_have` not matched in `resumeText`). Do NOT change/rename `score`/`preview`/`quickWins`/`checksRemaining` — live web + iOS public ATS path depend on them.
- Free-ATS-check web page: render the verdict band above the existing score + quick wins.
- Tests: assert the `fit` shape + that existing fields are unchanged.
- Validation: `npm run lint && npx tsc --noEmit && npm run build` pass; rate-limiting unchanged; no Supabase schema/RLS change (reuse `anonymous_ats_scores`; any column add goes through a reviewed migration, not silent RLS edits).

### Story 1 — iOS: Fit verdict model + service + decoder — **S/M**
Repo: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`
- Create `Models/FitVerdict.swift` (`FitVerdict` + `FitBand` enum; flexible Codable snake/camel, score clamp, reuse `ResumeGap`/`ResumeKeyword`).
- Create `Core/API/FitCheckService.swift` (protocol + live impl calling `POST /api/public/ats-check` anonymous via `x-session-id`, decodes `fit`; injectable mock).
- Create `ResumeBuilder IOS APPTests/FitCheckViewModelTests.swift`; add the file to the test target in `project.pbxproj` (per 2026-06-12 lesson).
- Validation: decode across payload shapes; band derived from `score.overall` only as fallback; safe-decode pattern (decode candidates into locals before `??`) per the 2026-06-12 Codable lesson; build + non-zero executed test count.

### Story 2 — iOS: Fit-check + verdict screens (flagged) — **M**
- Create `Features/V2/Fit/FitCheckViewModel.swift` (`@Observable @MainActor`; JD validation before network; loading/verdict/error; no-active-resume routing).
- Create `Features/V2/Fit/FitCheckView.swift` (paste JD + **Check Fit**; reuse existing scanning/loading animation).
- Create `Features/V2/Fit/FitVerdictView.swift` (band header, score ring, 3 decisive gaps, missing keywords, **Optimize for this job** + **Skip** CTAs; process-descriptive copy + explainer).
- Modify `RuntimeFeatures`/`BackendConfig`: add `isFitCheckEnabled` (default OFF).
- Validation: flag off = zero change to current flow; empty/short JD rejected inline before any call; `@Observable`+`@MainActor` (not ObservableObject); build + simulator smoke on iPhone 17 and iPhone SE against the mock.

### Story 3 — iOS: wire entry + optimize handoff — **M**
- Modify Tailor/`HomeView` optimize entry: when `isFitCheckEnabled`, route paste-JD → `FitCheckView` first; verdict's **Optimize for this job** enters the existing diagnosis → Improve flow with the same JD (no re-paste).
- Validation: optimize reached only via verdict when flag on; JD carries through without re-entry; existing optimize/diagnosis unchanged; flag off = original direct path intact; build + smoke.

### Story 4 — iOS: analytics + localization — **S/M**
- Modify `AnalyticsEvent` + analytics service: add `fit_check_started`, `fit_check_completed` (verdict, match_score), `fit_check_optimize_tapped`, `fit_check_skipped`; extend contract test (16 → 20 events).
- Modify `Localizable.xcstrings`: EN + HE for all new strings; verify via `xcodebuild -exportLocalizations` (per 2026-06-17 lesson), RTL-safe.
- Validation: all 4 events fire at the right points; contract tests pass; HE coverage verified through the xliff export, not grep.

## Guardrails (claim defensibility — non-negotiable)

- Verdict copy is **process-descriptive** ("estimated fit vs this job"), never an outcome guarantee, never an ATS-vendor claim (EXD-012, WP-10).
- A Fit verdict does **not** consume an optimization credit.
- Ship the iOS step **dark** behind `isFitCheckEnabled`; the web verdict band can render immediately since it only adds to an existing surface.

## Read first (in each product repo)

- iOS: `AGENTS.md`/`CLAUDE.md`/`CURSOR.md`, `tasks/progress.md`, `tasks/MEMORY.md`, `tasks/lessons.md`, and the three `docs/specs/drafts/fit-first-triage-*` files (after #73 merges).
- Web: `tasks/MEMORY.md`, `tasks/ERRORS.md`, `tasks/lessons.md`, `src/app/api/public/ats-check/route.ts`.

## Memory update on completion

- iOS `tasks/progress.md` (canonical), `tasks/session-log.md`, `tasks/MEMORY.md`.
- Web `tasks/MEMORY.md`.
- Log the two decisions (thresholds, resume-input contract) in Agentic OS `DECISIONS.md`.
