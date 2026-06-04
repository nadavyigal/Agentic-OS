# Prompt: COO Operating Review

Runs the thin COO Operating Review. Operational, not strategic: it produces the next execution sequence and at most one work packet, and only escalates to CEO/CFO/Analysis/Risk when the blocker is genuinely owned by that layer. Different from `executive-weekly-review` (strategic, portfolio-wide).

Trigger phrases:
- "coo operating review"
- "next execution sequence"
- "what should I do next"

```txt
Use the Executive OS.

Act as COO OS.

Based on the latest dashboard and project status, give me the next execution sequence.

Do not run a full executive review unless needed.

Read:
- DASHBOARD.md
- PROJECT-STATUS.md
- dashboard/status.json
- executive-os/COO-OS.md
- executive-os/workflows/coo-operating-review.md
- executive-os/templates/work-packet-template.md

Output:
1. Operating summary
2. Current bottleneck
3. Next execution sequence
4. CEO escalation needed: Yes/No
5. CFO escalation needed: Yes/No
6. Analysis needed: Yes/No
7. Risk review needed: Yes/No
8. If escalation is needed, state the exact decision/question
9. If no escalation is needed, create one copy-ready work packet for the relevant local project
10. What not to touch
```
