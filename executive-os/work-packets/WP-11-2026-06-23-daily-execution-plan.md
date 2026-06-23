# Work Packet WP-11 — Daily Execution Plan 2026-06-23

- Status: Open
- Created: 2026-06-22
- Source: 2026-06-22 session close-out (Garmin Gate-4 + ATS + STORM day)
- Workflow pattern: normal
- Input trust: trusted (derived from live git state on 2026-06-22)
- Outcome loop: mixed (Garmin approval, voice-coach activation, Resumely credibility, hygiene)
- Mirror: vault `00-Inbox/2026-06-23-plan-tomorrow.md`
- Success signal: Garmin remediation email sent + evidence resubmitted; voice-coach flag decided (flip or defer, logged in DECISIONS.md); ATS next priority chosen; wiki-index links fixed and PR #92 dispositioned

> Suggested order: Prompt 1 (Garmin) → Prompt 2 (voice coach) → Prompt 3 (ATS) → Prompt 4 (hygiene).
> Each block below is a paste-ready execution prompt. Open the named repo, then paste the prompt.

---

## Prompt 1 — Garmin Gate-4 resubmission (PRIMARY)

**Repo:** RunSmart Web `/Users/nadavyigal/Documents/RunSmart` (+ RunSmart iOS `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app` for on-device verify)

```
Goal: Finish the Garmin Gate-4 remediation and resubmit the evidence package to Marc Lussi.

Task:
1. Read docs/garmin-application/12-MARC-2026-06-22-REJECTION-REMEDIATION-PLAN.md and 10-MARC-LUSSI-GATE-1-4-EMAIL-DRAFT.md.
2. Verify HRV dual-source collection works end-to-end on device — confirm HealthKit-read HRV now surfaces as "Apple Health", not Garmin (iOS commit 2d44154). Capture a corrected screenshot if the prior one was a rejection reason.
3. Reconcile the email draft against the remediation plan; finalize the message to Marc.
4. Refresh and verify the evidence zip contains the corrected, brand-compliant screenshots.
5. Delete the 3 untracked Finder-duplicate artifacts (docs/garmin-application/*" 2.md") — confirm each is a dup of a real file before deleting.
6. Commit the WIP and update tasks/progress.md (RunSmart iOS uses todo+session-log+MEMORY; RunSmart Web is derived-status, update tasks/MEMORY.md).

Constraints: Brand-compliance is the rejection cause — every Garmin-sourced data point must be attributed correctly; do not re-introduce un-attributed Garmin labels. No new dependencies. Do not resubmit until the evidence zip is verified.

Validation: Email finalized and ready to send; evidence zip opened and screenshots confirmed brand-compliant; on-device HRV attribution verified; WIP committed + pushed; progress/MEMORY updated.
```

---

## Prompt 2 — Voice coach flip decision (standing reminder)

**Repo:** Agentic OS `/Users/nadavyigal/Documents/Projects /Agentic OS` (review) + RunSmart Web `/Users/nadavyigal/Documents/RunSmart` (flag, if flipping)

```
Goal: Decide whether to flip VOICE_COACH_ENABLED in RunSmart, or defer — and log the decision.

Task:
1. Review Agentic OS draft PR #17 (cursor/voice-coach-flip-research-c95e): the VOICE_COACH_ENABLED STORM + deep research brief.
2. Confirm the cost ring-fencing, throttle, and instrumentation already shipped (RunSmart commit 91089e6) cover the risks the research flags.
3. Decide: flip the flag (with a rollout %/guardrail) or defer with a named trigger condition.
4. Record the decision in Agentic OS DECISIONS.md and mirror to the vault Decision Log.
5. If flipping: make the flag change in RunSmart on a branch, open a PR. If deferring: update the standing reminder so it stops re-surfacing every session.

Constraints: Do not flip a production flag without the cost guardrails verified as active. No flip without a logged decision. Branch first; do not commit the flag change directly to main.

Validation: Decision written to DECISIONS.md with date + rationale; either a RunSmart flag PR is open OR the defer trigger is documented; standing reminder updated.
```

---

## Prompt 3 — ResumeBuilder ATS next priority — **DONE 2026-06-23**

**Repo:** Resumely iOS `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP` + ResumeBuilder Web `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`

**COMPLETED → WP-12 Stories 0–4 all merged to main. E2E gate closed. iOS PR #75 merged (`17d2122`, 11:25Z), rebased clean (union preserved #72), 27 tests pass, HE xliff verified, ships dark (`isFitCheckEnabled=false`). See WP-12.**

```
Goal: Land the Fit-First Triage wedge (PR #73) as the next ATS priority. Full plan: WP-12.

Task:
1. Resolve the two decisions in WP-12's DECISION GATE (verdict thresholds; resume-input contract). Log them in DECISIONS.md.
2. Pre-flight: merge PR #73 (iOS docs/plan), disposition PR #72 (iOS per-keyword preview approval UI — merge or close), merge web PR #84 if green.
3. Execute WP-12 build sequence: Story 0 (web /api/public/ats-check fit block) first, then iOS Stories 1–4 behind isFitCheckEnabled.

Constraints: One story at a time. Additive API change only — do not rename score/preview/quickWins/checksRemaining. No copy implies an external/vendor ATS score (EXD-012). Ship iOS dark behind the flag.

Validation: two decisions logged; #73/#72/#84 dispositioned; fit block returns from the endpoint with existing fields unchanged; iOS verdict flow builds + smokes behind the flag; progress.md updated.
```

---

## Prompt 4 — Quick hygiene (low effort, high signal)

**Repo:** Vault `/Users/nadavyigal/Documents/Projects /Nadav Builder OS` + RunSmart Web `/Users/nadavyigal/Documents/RunSmart`

```
Goal: Fix the flagged vault index links and disposition the stale RunSmart PR.

Task:
1. In the vault, fix the 3 broken wiki-index.md links flagged by the 2026-06-22 nightly sweep: [[00-Inbox/2026-06-17-packet-agentic-os-status-truth]], [[00-Inbox/2026-06-17-packet-arm-status-guard]], [[00-Inbox/2026-06-17-packet-hygiene-stranded-sweep]] (lines 31, 34, 35) — these packets were archived to 10-Archive on 2026-06-20. Re-point to the archived note titles or drop the entries.
2. Append a wiki-log.md entry recording the fix.
3. Review RunSmart PR #92 (feature/aha-moments-phase1, open since 2026-06-15). Decide: merge if still valid, rebase/revise, or close. Act on the decision.

Constraints: Vault edits stay in the vault folder map; do not touch product status claims. Do not merge PR #92 without confirming it still builds/tests against current main.

Validation: wiki-index.md has zero broken links; wiki-log.md entry appended; both committed + pushed; PR #92 merged, updated, or closed with a one-line reason.
```
