# Research Brief: Resumely "ATS Match Score" — Keep Self-Defined or Reposition

- **Date:** 2026-06-22
- **Researcher / agent:** Analysis OS (Cursor)
- **Role context:** Solo founder, pre-Gate-A (pre first traction/validation gate).
- **Question:** Should Resumely's "ATS Match Score" stay a self-defined score, or be repositioned?
- **Why it matters now:** The score is the headline value prop of the resume optimizer. Pre-Gate-A is exactly when to lock naming and positioning, before App Store copy, screenshots, paid claims, and onboarding all harden around a frame that is hard to undo later. The cost to change is near zero now and rises with every asset built on top of it.
- **Tools available:** Web search / fetch — yes. Sources cited below. Product implementation details (how Resumely currently computes and labels the score) not inspected this session — treated as an assumption, flagged in §3.

---

## 1. Facts

1. No major ATS auto-rejects a resume on a match score or keyword threshold. Final decisions require human review. The "robot scores you and deletes you" model is a myth actively debunked through 2026. [S1][S2]
2. There is no universal, candidate-facing "ATS score." What a recruiter actually sees varies by platform: Workday (post-2024 HiredScore) shows an A/B/C/D letter grade, iCIMS a tier, Greenhouse a bucket label, and Lever / Workable / BambooHR show no score at all. None show a 0–100 percentage. [S2][S3]
3. The automated filter that does exist is knockout questions (work authorization, required certifications, location), set by humans, not resume keyword scoring. [S1][S2]
4. Every consumer resume tool that shows a "score" computes its own proxy against its own algorithm, not against any employer's real ATS: Jobscan "Match Rate," Teal "Match Score," Resume Worded "Relevancy Score," plus Rezi and Enhancv. A self-defined score is the category norm, not an outlier. [S2][S3][S4]
5. The credible tools frame the number as a job-description match proxy and openly state it is not the employer's real ATS score. CVHive (a competitor's own benchmark guide) states plainly: "No employer sees that score... it does not replicate what any real ATS does." [S2][S3]
6. Published target bands cluster at 75–85% (Jobscan ~75–80, Teal ~80, Resume Worded ~85). Scores above ~90% signal keyword stuffing, which hurts with human readers. Interview-rate lift flattens above 85% and is effectively flat above 90%. The score is useful as a relative self-check, not an absolute predictor. [S3][S4]
7. FTC law: any objective claim, express or implied, in app-store copy, on a website, or inside the app, must be truthful and backed by a "reasonable basis" of competent and reliable evidence held before the claim runs. The net impression governs, and a literally-true statement can still be deceptive by implication. [S5][S6]
8. The FTC has acted against mobile apps that marketed automated-analysis accuracy without substantiation (MelApp, Mole Detective). It does not mandate a fixed accuracy level, it requires that the marketed claim match the evidence held (e.g., if testing shows 60% accuracy, you may claim 60%, not more). [S6][S7]

---

## 2. Sources

| # | Source | Type | Reliability | Date |
|---|---|---|---|---|
| S1 | Sean Tanos (recruiter, works inside Greenhouse/Workday/Lever), LinkedIn | Practitioner | Medium-High | 2026 |
| S2 | Huntr, "How Applicant Tracking Systems Actually Work in 2026" | Market/industry blog | Medium | 2026 |
| S3 | CVHive, "What is a good ATS score? Real 2026 benchmarks" | Competitor blog | Medium | 2026 |
| S4 | Jobscan vs Teal / vs Resume Worded comparisons; joblabs.ai; careery.pro | Vendor + review blogs | Medium | 2026 |
| S5 | FTC, Advertising FAQs for Small Business; Advertising Substantiation Policy Statement; Myths and Half-Truths About Deceptive Advertising | Official (regulator) | High | Current |
| S6 | FTC, "Marketing Your Mobile App: Get It Right from the Start" | Official (regulator) | High | Current |
| S7 | FTC statement, MelApp / Mole Detective enforcement (File No. 132 3211 / 132 3210) | Official (regulator) | High | 2015 |

Note: S1–S4 are industry/vendor sources, reliability Medium; they agree with each other and with the regulator-grade framing in S5–S7, which raises overall confidence. Exact private-ATS internals are proprietary and unverifiable from outside.

---

## 3. Assumptions

1. Resumely's score is currently computed by Resumely's own logic (keyword/JD overlap plus formatting), i.e. it is already a self-defined proxy. **Not verified in the repo this session.** If it is instead claimed to be sourced from a real ATS, the risk in §6 jumps from medium to high.
2. The score is surfaced to users with the literal label "ATS Match Score" in-app and likely in marketing. **Verify against current UI and App Store copy.**
3. Resumely's near-term market includes the US, so FTC standards are the relevant advertising floor. Other markets (EU, Israel) have comparable truth-in-advertising regimes.
4. Pre-Gate-A means low sunk cost in brand assets, so a rename is cheap now.

---

## 4. Insights

**I1 — The mechanic is fine; the label is the liability.** A self-computed score is the category standard and there is no reason to abandon it. The exposure comes from the word "ATS," which makes an implied claim that the number reflects what a real applicant tracking system would score. Facts §2 and §5 say that claim is not substantiable, because no such universal score exists.

**I2 — The honest framing is also the more defensible product.** Competitors that survive scrutiny (Jobscan, Teal) describe the number as a match against the specific job description, not as the employer's ATS verdict. Reframing from "what the ATS thinks of you" to "how well this resume matches this job" is simultaneously more truthful, more useful to the user, and harder to attack. You lose nothing real and shed the weakest part of the claim.

**I3 — The "ATS myth" is decaying, which is a risk and an opening.** 2026 content is actively teaching job seekers that the robot-gatekeeper is a myth (§1). A product whose headline leans on that myth ages badly and looks naive to informed users. A product that says "real ATS don't auto-score you; here is how well you match this job, and what to fix" can position against the myth instead of riding it. That is a credibility differentiator at near-zero cost.

**I4 — Pre-Gate-A is the cheapest possible moment to fix this.** The decision is not "is the score good," it is "what do we promise about the score before we build all our copy on it." Deferring locks in cleanup debt across App Store metadata, screenshots, onboarding, and any paid claims.

**I5 — A number with a target band beats a number alone.** Facts §6 show the value is relative (hit ~80, do not chase 100). A bare percentage labeled "ATS Match Score" implies an absolute pass/fail the data does not support. Pairing the score with a target band and a "what to fix" action list converts a fragile claim into a genuine tool.

---

## 5. Opportunities

### O1 — Reposition the score (keep mechanic, change frame + add disclosure) [recommended]
Keep the self-computed score. Rename to a job-match frame (candidates: "Job Match Score," "Match Rate," "Resume Match"). Add a one-line, always-visible disclosure: "An estimate of how well your resume matches this job description. Not an official score from any employer's ATS." Show a target band (aim ~80) and a "what to fix" list.
- Impact: 4/5 · Confidence: 4/5 · Effort: 1/5 (copy + one tooltip/disclosure, optional band UI) · Revenue fit: 3/5 · Strategic fit: 5/5 · Risk: 1/5

### O2 — Anti-myth positioning as a marketing wedge
Lead onboarding and store copy with "ATS bots don't auto-reject you — here's the truth, and here's how to actually match this job." Turns the corrected framing into differentiation versus competitors still selling the myth.
- Impact: 3/5 · Confidence: 3/5 · Effort: 2/5 · Revenue fit: 3/5 · Strategic fit: 4/5 · Risk: 2/5

### O3 — Status quo: keep "ATS Match Score" as-is [not recommended]
Lowest immediate effort, but carries the implied-claim and FTC exposure (§7), ages against the decaying myth, and gets more expensive to unwind after Gate-A.
- Impact: 1/5 · Confidence: 2/5 · Effort: 0/5 · Revenue fit: 2/5 · Strategic fit: 1/5 · Risk: 4/5

---

## 6. Risks

| Risk | Impact | Likelihood | Note / mitigation |
|---|---|---|---|
| Implied "ATS score" claim is unsubstantiable (FTC §7) | High | Medium | Reposition + disclosure (O1). Make no accuracy/"will pass the ATS" claim you cannot prove. |
| Informed users perceive the app as naive / riding a debunked myth | Medium | Medium-High | Anti-myth framing (O2). |
| Renaming mid-stream after Gate-A forces rework of store assets, copy, onboarding | Medium | High if deferred | Decide now, pre-Gate-A, while sunk cost is ~0. |
| Dropping "ATS" hurts App Store keyword discoverability | Medium | Medium | Keep "ATS" in keyword metadata and descriptive body copy ("optimize for ATS keyword matching") without labeling the score itself an "ATS score." Discoverability and the in-product claim are separable. |
| Score computed differently than assumed (§3) | High | Unknown | Verify in repo before finalizing copy. |
| Over-rotating into legal caution makes the product feel weak | Low | Low | Disclosure is one line; the score and action list stay front and center. |

---

## 7. Recommendations

1. **Reposition, do not remove (O1).** Keep the self-defined score. Stop labeling it "ATS Match Score." Use a job-match name plus a one-line disclosure that it is an estimate of resume-to-job-description fit, not an employer's real ATS output. This is the highest-leverage, lowest-effort move and it removes the only material legal/credibility exposure.
2. **Add a target band and a "what to fix" list** next to the number so the score reads as a relative tool (aim ~80), not an absolute verdict (§6 facts).
3. **Keep "ATS" in keyword/SEO metadata, not on the score itself.** Preserve discoverability without making the unsubstantiable in-product claim.
4. **Verify the assumption (§3) in the repo** before writing final copy: confirm the score is self-computed from JD overlap + formatting, and capture exactly where the "ATS Match Score" string appears (UI, App Store, marketing).
5. **(Optional, O2) Adopt anti-myth positioning** as a marketing wedge once the rename lands.

---

## 8. Open Questions

1. Exactly how is Resumely's score computed today, and where does the "ATS Match Score" label appear (UI strings, App Store metadata, screenshots, marketing)?
2. Is there any current claim (express or implied) that the score predicts passing a real ATS or getting an interview? Those are the highest-risk claims.
3. Which name does founder taste prefer among "Job Match Score," "Match Rate," "Resume Match"? (Naming is a taste call; the requirement is only that it not imply a real ATS produced it.)
4. Are there non-US target markets whose advertising rules should also be checked before launch copy locks?

---

## 9. Decision Needed

**Does Resumely keep "ATS Match Score" as the label, or reposition the score to an honest job-match frame with a disclosure (O1)?**

Recommendation: **Reposition (O1).** Keep the score mechanic, drop the "ATS score" label and implied claim, add a one-line disclosure and a target band, retain "ATS" only in discoverability metadata.

---

**Confidence:** High that the *self-defined score should stay* (it is the category norm and there is no real ATS score to defer to). High that the *"ATS Match Score" label should be repositioned* (FTC substantiation standard + no universal ATS score + a decaying myth all point one way). Medium on exact implementation, pending repo verification of how the score is computed and labeled (§3).

**Recommended next step:** In the ResumeBuilder iOS repo, locate every "ATS Match Score" string (UI + App Store metadata) and confirm how the score is computed, then change the in-product label to a job-match name with the one-line disclosure. One scoped work packet, low effort, do it before Gate-A copy locks.
