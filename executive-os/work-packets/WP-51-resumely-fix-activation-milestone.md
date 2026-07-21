# Work Packet WP-51 — Repair the Resumely activation milestone before the EXD-015 verdict

- Status: In Progress
- Started: 2026-07-21 (founder launched the session in the Resumely iOS repo)
- Mode: Builder
- Source: COO Operating Review 2026-07-21; live PostHog read project 270848 (2026-07-21); `docs/qa/reports/wp46-story10-activation-funnel-2026-07-18.md` (measurement contract); **EXD-022** (activation gate = ≥20 clean activations on a working milestone; supersedes EXD-015's 20%-by-08-01 target)
- Workflow pattern: normal
- Input trust: trusted
- Loop: Resumely activation measurement loop
- Signal: The 2026-07-21 live read on the canonical WP-50 contract returned a **non-monotonic funnel** — 12 `resume_file_selected` → 7 `optimization_completed` → **1** `optimized_preview_rendered`, with **3** `export_success`. More people exported than rendered a preview, which is impossible if the milestone fired reliably. `optimized_preview_rendered` has only 3 people across 60 days.
- Memory update: `tasks/lessons.md` (Resumely iOS) + `docs/qa/reports/wp46-story10-activation-funnel-2026-07-18.md` (amend the contract with the fix)
- Success signal: `optimized_preview_rendered` person-count is **≥** `export_success` person-count over the same window, and the ordered funnel is monotonic non-increasing on a fresh 14-day read. Secondary: `save_failed`, `optimization_apply_failed` and `optimization_state_recovery_failed` all carry a populated `reason` on every new occurrence.
- Model route: Sonnet 5 (instrumentation fix + verification; no architectural change)
- Rollback: Revert the instrumentation commit. This packet touches analytics emission only — no auth, billing, data, or migration surface. If the fix over-fires instead, the event's person-count exceeding `optimization_completed` is the tell.

## Owner Role
Resumely iOS engineer

## Project
Resumely iOS — `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`

## Why This Packet Exists Now

**EXD-022 (decided 2026-07-21)** replaced EXD-015's untestable "20% by 2026-08-01" with an absolute-count gate: **≥20 clean activations observed on a working milestone**, no calendar deadline. That restatement makes this packet the gating item rather than one of several.

The reason is arithmetic. Under a percentage target, a broken milestone produced a wrong ratio. Under a count target, a broken milestone means **activations do not accumulate at all** — the counter is stuck near zero for an instrumentation reason, and no amount of elapsed time or traffic advances it. The gate cannot open until the event fires correctly.

Compounding it: 1.4.4 (14) is under App Store review and carries no measurement fix, so its approval resets the exact-version cohort clock and starts a fresh cohort on the same broken instrument. This is the same failure class the portfolio already spent two weeks on (WP-46, WP-48, WP-50). This packet exists to stop it recurring a fourth time.

This is **not** a request to change the activation definition. WP-50's contract is sound and was chosen deliberately over two rejected alternatives (`resume_uploaded`, whose call site was removed in 1.4.3; `resume_upload_succeeded`, which sits behind the sign-in guard — WP-48 Defect B). The contract is right; the emission is broken.

## Scope

1. **Locate the emission site** for `optimized_preview_rendered`. Per the WP-46 Story 10 contract it fires "once per optimization only after `WKWebView` reports a successful visible HTML navigation and the optimized résumé has visible applied changes."
2. **Determine which of the two conditions suppresses it.** The most likely candidates, in order: the `WKWebView` navigation callback not firing (or firing on a path the handler does not observe), and the "visible applied changes" check being stricter than intended or evaluating before render completes.
3. **Fix the emission** so it fires whenever a user actually sees a rendered optimized résumé. Preserve the once-per-optimization guarantee and the `optimization_id` correlation field.
4. **Add a regression test** proving the event fires on a successful preview render. Red before, green after.
5. **Verify against live data** after the fix ships: re-run the canonical funnel and confirm monotonicity.

## Scope addition from the 2026-07-21 PostHog AI audit (verified)

The audit independently found three failure events firing with **zero diagnostic properties**. Verified against live data the same day, 30d window:

| Event | Events | Persons | Rows with a populated reason/error |
|---|---|---|---|
| `save_failed` | 21 | 20 | **0 of 21** |
| `optimization_apply_failed` | 12 | 9 | **0 of 12** |
| `optimization_state_recovery_failed` | 24 | 12 | **0 of 24** |

These sit in the **same post-activation commit path** as the milestone this packet repairs: a user optimizes, then tries to apply/save/recover the result and it fails, blind. Given only 7 clean people reach `optimization_completed` in 30 days, 20 people hitting `save_failed` means the failures are concentrated among users who are not otherwise visible as activated — and every one of them is undiagnosable.

**Add to this packet:** a `reason` and `error_code` property on all three events. Same instrumentation surface, same session, and it turns three blind failure paths into debuggable ones. Do not attempt to *fix* the underlying failures here — just make them visible. The fix is a separate packet once you can see the causes.

## Rejected: the audit's proposal to redefine activation as `optimization_completed`

The audit states *"No explicit activation definition exists in this project"* and proposes `optimization_completed` as activation. **Both the premise and the proposal are wrong, and adopting them would silently revert WP-48 and WP-50.**

The definition does exist — it lives in the repo (`docs/qa/reports/wp46-story10-activation-funnel-2026-07-18.md`), not in PostHog, which is why the audit could not see it. Denominator `resume_file_selected`, milestone `optimized_preview_rendered`.

`optimization_completed` was considered and is **backend completion, not delivered value.** The whole point of `optimized_preview_rendered` is that it fires only when the user actually *sees* a rendered optimized résumé. Substituting backend completion reintroduces exactly the gap WP-46 Story 10 closed.

That said, the audit's instinct points at something real, and it is this packet's open question: **the gap between the two events is either the defect or the truth, and the monotonicity check settles it.** Clean 30d figures, `is_internal_tester` excluded:

```
optimization_completed        7
optimized_viewed              4
optimized_preview_rendered    1   <- milestone
export_success                3   <- MORE than rendered a preview
```

Three people exported a résumé that one person is recorded as having seen. That is not a behavioural funnel; it is impossible. **This is the proof that the milestone under-fires rather than users dropping off**, and it is the reason the audit's Experiment 2 (progress-framing to fix a "56% fall-off" between completion and viewing) would be optimizing a measurement artifact. Do not ship that experiment until this packet lands.

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
