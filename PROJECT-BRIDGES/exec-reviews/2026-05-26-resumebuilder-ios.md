# Exec Review: ResumeBuilder iOS
**Date:** 2026-05-26
**Lens:** CEO + distribution

---

## 1. North-Star Check

**North-star metric:** No explicit metric defined or logged. Based on the bridge file and product priorities, the implied leading indicator is **completion rate of the core loop on a real device**: upload PDF → optimize → preview optimized resume.

**Is it moving?** Unknown — no tracking exists yet. The core loop is not verified on a real device as of today. Simulator tests pass (33/33), but physical-device smoke with a live account and known-good PDF has not been confirmed complete in any session entry.

**Why:** All engineering effort in the last 14 days has gone into making the loop runnable, not measuring whether users can complete it.

**Data source that would answer it:** One recorded end-to-end real-device smoke with a live account. No analytics infrastructure needed yet — a screen recording or manual test log is sufficient.

---

## 2. Shipped vs Matters

**Shipped in the last 14 days (PRs #19–30 + hotfix):**

| PR | What |
|----|------|
| #19 | Tailor errors, Me tab, Application resume, Expert reports wiring |
| #20 | 4 device regressions from PR #19 smoke |
| #21 | 4 root-cause bugs: mock PDF path, design switch, apply design, expert preview |
| #22 | 3 post-optimize regressions (expert 500, preview header, design per-category) |
| #23 | Build time reduction 78% (compilation caching) |
| #24 | Removed runtime mocks — live-only services |
| #25–26 | Live endpoint stabilization, style history removed, scanned-PDF rejection |
| #27 | Upload PDF normalization (text-layer re-emit before sending to backend) |
| #28 | End-to-end live stabilization (Resume Library gate, preview cancel handling) |
| #29 | Optimize/design/expert data flow repair (contact decode, template UUID, ATS) |
| #30 | Preview category switching fix, preview loading decoupled from section fetch |
| hotfix | Optimized preview no longer blocks on section-detail load |

**Which serve north-star:**
- PR #24 (live-only services), #27 (PDF normalization), #29 (contact/design/expert data flow), #30 + hotfix (preview loads correctly) — these directly enable the core loop to work on a real device.
- PR #23 (build time) is a DX win, not user-facing. Reduces future iteration friction but doesn't move the north-star.

**Gap:** 12 PRs in 14 days, yet the core loop is still unverified on device. Every PR was a fix to a fix. Pattern: simulator passes → device smoke → new regression found → fix → simulator passes again. Zero new features shipped in this window.

**One sentence:** Busy, not productive — high commit velocity, but the north-star has not moved because the real-device smoke test that would confirm the loop still hasn't happened.

---

## 3. Distribution Reality

**Who is seeing the product:** No one outside of the developer. No TestFlight users. No App Store submission. Distribution is zero.

**What's working:** The backend and iOS are connected end-to-end in code. Simulator passes consistently. Backend endpoints for optimize, design apply, Expert, and preview are implemented (with known gaps: `/api/v1/resumes` returns 404, `/api/v1/styles/history` returns 500).

**What isn't working:** Resume Library is feature-flagged off. Style history is silent-disabled. No real-device smoke has been completed with a known-good text PDF. No TestFlight or beta users exist.

**Distribution hypothesis being tested:** None. The project has not reached the stage where one is being tested.

**Biggest unverified assumption:** That a non-developer user can complete the core loop — upload a PDF, optimize, view the preview, apply a design — without a support handoff. This assumption is entirely untested.

---

## 4. Next Bet

**Hypothesis:** If we complete and record one successful end-to-end smoke on a real device (real account, real PDF, real optimize, real preview render), we will have the evidence needed to submit a TestFlight build and begin external validation.

**What to ship:**
1. Confirm latest `main` builds and runs on a physical iPhone with a live account.
2. Upload a text-based PDF (exported from Pages or Word — not scanned).
3. Complete: optimize → Optimized tab preview renders → apply one design category → run Expert → apply Expert changes → confirm ATS score refresh.
4. Document the smoke (video or screenshot + log) and close any remaining critical blockers found.
5. Archive the build and submit to TestFlight internal track.

This is a QA + distribution story, not a code-shipping story. Code is ready enough for one real user to try it.

**How we'll know it worked:** TestFlight internal build uploaded and at least one external tester (non-developer) completes the optimize → preview loop without a support handoff.

**Kill criteria:** If three consecutive real-device smokes with different PDFs all fail on the same step and the fix requires backend work (e.g., `/api/v1/resumes`), stop and prioritize the backend gap before TestFlight instead of shipping a broken library tab.
