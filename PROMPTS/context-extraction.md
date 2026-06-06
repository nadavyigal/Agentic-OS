# Prompt: Context Extraction

Runs the durable founder-interview workflow for an important but unscoped topic.

Trigger:

`context extraction on <topic>`

```txt
Use the Executive OS Context Extraction workflow.

Read:
- executive-os/workflows/context-extraction.md
- executive-os/templates/context-checkpoint-template.md
- brainstorms/README.md
- existing files directly relevant to <topic>

Create or resume:
brainstorms/YYYY-MM-DD-<topic-slug>.md

State the topic, purpose, and current understanding, then ask exactly one
question. After every answer, update the checkpoint before asking the next
question.

Label extracted statements confirmed, assumption, or open. Capture topic,
purpose, current understanding, Q&A log, extracted decisions, assumptions,
constraints, taste/preferences, examples, unknowns/gaps, suggested doc updates,
and a recommended next work packet when the packet is clear.

Do not store secrets or customer data. Do not update decisions, plans, skills, or
active work packets without explicit founder approval. When the checkpoint is
decision-complete, present the specific suggested updates and draft next packet.
```
