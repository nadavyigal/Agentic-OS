# Prompt: Context Extraction

Runs the durable founder-interview workflow for an important but unscoped topic.

Trigger:

`context extraction on <topic>`

```txt
Use the Executive OS Context Extraction workflow.

Read:
- executive-os/workflows/context-extraction.md
- executive-os/templates/context-checkpoint-template.md
- executive-os/context/README.md
- existing files directly relevant to <topic>

Create or resume:
executive-os/context/YYYY-MM-DD-<topic-slug>.md

State the topic, purpose, and current understanding, then ask exactly one
question. After every answer, update the checkpoint before asking the next
question.

Default to ten questions maximum. Label extracted statements Confirmed,
Assumption, or Open. Capture Goal, audience, constraints, success criteria,
non-goals, taste/preferences, examples, and unresolved decisions.

Do not store secrets or customer data. Do not update decisions, plans, skills, or
active work packets without explicit founder approval. When the checkpoint is
decision-complete, mark it ready-for-promotion and present the specific suggested
updates and draft next packet.
```
