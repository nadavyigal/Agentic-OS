# Work Packet WP-51 — Repair the Resumely activation milestone before the EXD-015 verdict

- Status: Open
- Mode: Builder
- Source: COO Operating Review 2026-07-21; live PostHog read project 270848 (2026-07-21); `docs/qa/reports/wp46-story10-activation-funnel-2026-07-18.md` (measurement contract); EXD-015 (20% activation by 2026-08-01)
- Workflow pattern: normal
- Input trust: trusted
- Loop: Resumely activation measurement loop
- Signal: The 2026-07-21 live read on the canonical WP-50 contract returned a **non-monotonic funnel** — 12 `resume_file_selected` → 7 `optimization_completed` → **1** `optimized_preview_rendered`, with **3** `export_success`. More people exported than rendered a preview, which is impossible if the milestone fired reliably. `optimized_preview_rendered` has only 3 people across 60 days.
- Memory update: `tasks/lessons.md` (Resumely iOS) + `docs/qa/reports/wp46-story10-activation-funnel-2026-07-18.md` (amend the contract with the fix)
- Success signal: `optimized_preview_rendered` person-count is **≥** `export_success` person-count over the same window, and the ordered funnel is monotonic non-increasing on a fresh 14-day read
- Model route: Sonnet 5 (instrumentation fix + verification; no architectural change)
- Rollback: Revert the instrumentation commit. This packet touches analytics emission only — no auth, billing, data, or migration surface. If the fix over-fires instead, the event's person-count exceeding `optimization_completed` is the tell.

## Owner Role
Resumely iOS engineer

## Project
Resumely iOS — `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`

## Why This Packet Exists Now

EXD-015 sets a 20% activation target reviewed on **2026-08-01 — 11 days out**. The milestone chosen to measure it does not fire reliably, so on current trajectory that review arrives with no verdict possible for a measurement reason rather than a product reason. That is the same failure the portfolio already spent two weeks on (WP-46, WP-48, WP-50). This packet exists to stop it recurring a fourth time.

This is **not** a request to change the activation definition. WP-50's contract is sound and was chosen deliberately over two rejected alternatives (`resume_uploaded`, whose call site was removed in 1.4.3; `resume_upload_succeeded`, which sits behind the sign-in guard — WP-48 Defect B). The contract is right; the emission is broken.

## Scope

1. **Locate the emission site** for `optimized_preview_rendered`. Per the WP-46 Story 10 contract it fires "once per optimization only after `WKWebView` reports a successful visible HTML navigation and the optimized résumé has visible applied changes."
2. **Determine which of the two conditions suppresses it.** The most likely candidates, in order: the `WKWebView` navigation callback not firing (or firing on a path the handler does not observe), and the "visible applied changes" check being stricter than intended or evaluating before render completes.
3. **Fix the emission** so it fires whenever a user actually sees a rendered optimized résumé. Preserve the once-per-optimization guarantee and the `optimization_id` correlation field.
4. **Add a regression test** proving the event fires on a successful preview render. Red before, green after.
5. **Verify against live data** after the fix ships: re-run the canonical funnel and confirm monotonicity.

## Out of Scope — Do Not Touch

- The WP-50 denominator decision (`resume_file_selected`). Settled.
- Any other activation event's semantics.
- The 1.4.4 archive/upload action — founder-gated, unchanged by this packet.
- The `is_internal_tester` classifier defect. Real, tracked separately, and not what blocks the 08-01 verdict.

## Validation

- Targeted regression test red → green
- Full suite passes (baseline: 205 passed / 1 intentional skip)
- Debug + unsigned Release builds green
- Post-ship live read: `optimized_preview_rendered` ≥ `export_success` over 14d, funnel monotonic

## Open Question To Resolve In-Session

Was the under-firing introduced by the Story 10 commits (`31b73b6` / `8277cba`) that shipped in 1.4.3, or has this event never worked? Check whether any pre-1.4.3 window shows healthy volume. This determines whether the 12.5% historical baseline was ever measured on a working event, and therefore whether any prior activation figure is trustworthy.
