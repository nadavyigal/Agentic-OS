# Prompt: STORM Multi-Perspective Research

Fast, offline, ungrounded multi-perspective scan of any topic or decision:
5 expert lenses -> contradiction map -> synthesis briefing -> self peer-review.
The lightweight cousin of `fan-out-research` / `deep-research`. Adapted from the
Stanford OVAL STORM method (NAACL 2024) — but this version drops STORM's Retrieval
stage, so it produces structured hypotheses, NOT verified, cited facts.

Trigger phrases:
- "storm <topic>"
- "multi-perspective scan on <topic>"
- "five perspectives on <topic>"

```txt
You are running a STORM Multi-Perspective Scan on: <TOPIC>.
Caller role (for the action step): <ROLE>.

This is an UNGROUNDED pass. You have no required source access. Reason from
general knowledge, but: never invent statistics, studies, or citations, and
flag every claim that rests on general reasoning rather than a known source.

Run four steps in order, labelling each:

STEP 1 — FIVE PERSPECTIVES. Simulate: Practitioner (daily user — what academics
miss), Academic (what peer-reviewed evidence says vs popular belief), Skeptic
(strongest counterargument; ignored evidence), Economist (who profits; incentives),
Historian (parallels; how they played out). For each: core position (2 sentences),
strongest supporting evidence, and the one thing only this lens would tell me.

STEP 2 — CONTRADICTION MAP. Where do lenses clash (name the specific claims)?
Strongest vs weakest evidence and why? The one question that resolves the biggest
conflict? What ALL lenses agree on (likely true)? What NONE addressed (the blind spot)?

STEP 3 — SYNTHESIS BRIEFING. (a) One-paragraph CEO summary with nuance.
(b) 5 key findings ranked by reliability, each noting supporting/challenging lenses.
(c) One hidden connection visible only across all 5 lenses. (d) Specific action for
a <ROLE>. (e) The frontier question that would change everything.

STEP 4 — PEER REVIEW. Confidence-score each finding 1-10 with reasons; name the
weakest link and what would verify it; flag overrepresented lens / dominant voice;
propose a missing 6th angle; give an overall grade and what to fix. END by listing
every claim that scored below 7/10.

Then STOP and recommend: if any sub-7 claim or any decision of real consequence is
in play, escalate — run a `fan-out-research` packet (or the deep-research skill) to
ground those claims in real, dated sources before acting. Do not present this scan's
output as verified fact.

Rules:
- No invented data, studies, or citations; mark gaps "unknown — need: <source>".
- Unsourced claims are assumptions, not facts.
- The "25% more organized" STORM benchmark is the FULL grounded system's, not this
  prompt's — never cite it as this scan's accuracy.
```
