# Work Packet WP-10

- Status: Open
- Created: 2026-06-22
- Source: EXD-012; `executive-os/research/2026-06-22-resumely-ats-match-score-positioning.md`
- Workflow pattern: normal
- Input trust: trusted
- Outcome loop: resumely-submission (post-launch copy defensibility)
- Loop: Resumely D7 / Gate A credibility loop
- Signal: Analysis OS research (2026-06-22) + prior iOS implementation (2026-06-20) left known gaps
- Memory update: `tasks/todo.md`, `tasks/progress.md`, `tasks/session-log.md` in Resumely iOS repo
- Success signal: Zero user-facing score labels imply an external ATS score; explainer present on every primary score surface; optional target-band hint visible; ASC metadata audited and listed for founder update if needed

# Work Packet

## Owner Role
iOS product engineer (local)

## Project
Resumely iOS (ResumeBuilder IOS APP)

Path: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`

Branch: `main`

## Goal
Close remaining gaps from EXD-012 so Resumely's score is consistently positioned as a self-defined **Resumely Match Score** (or **Match Score** in tight UI), with disclosure copy, not an external ATS vendor score.

## Context

**Decision (EXD-012):** Keep the self-computed score. Reposition the label. Do not claim the number is what a real ATS scores.

**Already done (2026-06-20, see `tasks/todo.md`):** Most rename + explainer work shipped. Canonical strings and file checklist are in `tasks/todo.md`. Build succeeded. Do not redo completed work.

**Known gaps to verify/fix this session:**

1. `HomeView.swift` — MetricCard label still `"ATS Match"` (should be `"Match Score"` per canonical strings).
2. `OptimizedResumeView.swift` — `Text("ATS Match")` ~line 690 (score surface, not descriptive feature copy).
3. **Target band (~80):** Research recommends showing "aim ~80" so users do not chase 100. Not implemented yet. Add a subtle hint on primary score surfaces only if it fits without clutter (one line, e.g. "Most strong matches land around 75–85%").
4. **App Store Connect live metadata:** `docs/app-store/he-metadata.md` was fixed; EN metadata and **live ASC fields** were not verified this session. Audit repo docs + list any ASC fields founder must update manually (no ASC login from agent).
5. **Screenshot manifests** flagged in `tasks/todo.md`: `dist/app-store-screenshots/*/upload-manifest.md` may still say "Templates that pass ATS" — fix if manifests are still used for uploads.

## Read First

- `AGENTS.md` / `CLAUDE.md` / `CURSOR.md`
- `tasks/todo.md` (canonical strings + completed checklist)
- `tasks/progress.md`
- `tasks/session-log.md`
- `executive-os/research/2026-06-22-resumely-ats-match-score-positioning.md` (in Agentic OS repo; path above is cross-repo reference)
- `executive-os/EXECUTIVE-DECISIONS.md` — EXD-012

## Task

1. **Audit:** `rg -i 'ATS Score|ATS Match Score|"ATS Match"'` across `ResumeBuilder IOS APP/` and `docs/`. Classify each hit: user-facing score label (fix) vs allowed descriptive ATS usage (keep per `tasks/todo.md` §Deliberately kept).
2. **Fix score labels:** Apply canonical strings from `tasks/todo.md`:
   - Room: **Resumely Match Score** / he **ציון ההתאמה של Resumely**
   - Constrained: **Match Score** / he **ציון התאמה**
   - Explainer (where score is primary): **Based on formatting + keyword match vs the job you paste. Not affiliated with any ATS vendor.** (+ Hebrew)
3. **Target band (optional, include if low-effort):** Add one-line "aim ~75–85%" hint on `ScoreResultView` and OptimizedResumeView score card. Localize EN + HE in `Localizable.xcstrings`.
4. **Metadata audit:** Read `docs/app-store/` (all files). Produce a short list: field name → current text → recommended text → needs founder ASC edit (yes/no).
5. **Screenshot manifests:** If still referenced for ASO uploads, align copy with EXD-012; otherwise note "deferred" in session output.
6. **Do not change:** Scoring logic, API models, `atsScore*` property names, analytics event names, backend contracts.

## Constraints

- Copy/labels only. No scoring algorithm changes.
- No App Store submission or ASC edits without explicit founder approval.
- No unrelated files. No new dependencies.
- Keep "ATS" in allowed descriptive contexts (ATS check, ATS insights, Improve ATS, ATS-friendly templates).
- One focused session. If target band adds scope risk, ship label fixes first and defer band to a follow-up.

## Validation

- `rg` audit: no user-facing score label says "ATS Match Score", "ATS Score", or bare "ATS Match" on a score metric (descriptive "ATS match" in sentences may remain).
- Explainer visible on `ScoreResultView` and OptimizedResumeView score card (EN; HE if RTL strings exist).
- Xcode build succeeds (simulator Debug is enough).
- Manual smoke: Home tab metric card + Improve optimized resume score card show correct labels.
- Update `tasks/todo.md` (new gaps closed), `tasks/progress.md`, `tasks/session-log.md`.

## Completion Gate

Before final response, report:

- What changed (file list)
- `rg` before/after summary
- ASC metadata audit table (founder action items)
- Build command + result
- What was NOT done (if deferred)

## Final Output

- Files changed
- Validation evidence
- Remaining risks (e.g. live ASC not updated)
- Next recommended action (likely: founder updates ASC EN fields if needed; O2 anti-myth copy deferred post-D7)
