# Workflow: Context Extraction

A durable founder interview for vague ideas, major plans, offers, and proposed OS
changes. It turns implicit context into a reviewable checkpoint before a decision
or work packet is created.

## When To Use

- The idea is important but Goal, audience, constraints, success criteria, or
  non-goals are still unclear.
- Founder taste, examples, or tradeoffs materially change the plan.
- The work may span sessions and the reasoning must survive a context reset.

Do not use this workflow for an already scoped work packet, routine COO
sequencing, or Tier 0-1 daily execution. Clarity Funnel compresses a messy ask
inside one chat; Context Extraction preserves a multi-turn founder interview.

## Output

Save one checkpoint at:

`executive-os/context/YYYY-MM-DD-<topic-slug>.md`

Start from `executive-os/templates/context-checkpoint-template.md`.

## Lifecycle

`open -> ready-for-promotion -> promoted | closed`

- `open`: interview is active or material gaps remain.
- `ready-for-promotion`: the checkpoint is decision-complete and awaiting founder
  approval.
- `promoted`: approved content was moved into a decision, plan, or work packet.
- `closed`: no promotion is needed.

## Interview Rules

1. State the topic, purpose, and current understanding before the first question.
2. Ask exactly one question per turn.
3. After each founder answer, append the question and answer to the checkpoint,
   update the extraction sections, and set `Last updated`.
4. Default to no more than ten questions. Continue only when the founder
   explicitly asks for deeper extraction.
5. Label extracted statements as `Confirmed`, `Assumption`, or `Open`.
6. Capture Goal, audience, constraints, success criteria, non-goals,
   taste/preferences, examples, and unresolved decisions.
7. Do not store secrets, credentials, customer data, or production data.
8. Do not update `DECISIONS.md`, `EXECUTIVE-DECISIONS.md`, skills, plans, or active
   work packets without founder approval.

## Completion

When the required fields are clear:

1. Set status to `ready-for-promotion`.
2. Summarize unresolved gaps without filling them silently.
3. List suggested document updates as links only.
4. Draft the next work packet only if repo, owner, task, constraints, and
   validation are all clear.
5. Ask for the specific promotion decision, not broad permission to continue.

After approval, apply only the approved updates, record their links in the
checkpoint, and set status to `promoted`.

## Validation

- The Q&A log contains one question per turn.
- Every extracted claim has a label.
- No durable decision or active packet was changed without approval.
- The checkpoint has a current status and `Last updated` date.
- The proposed next step is bounded and source-linked.
