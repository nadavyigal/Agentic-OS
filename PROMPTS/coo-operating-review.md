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
- dashboard/status.json (`planExecution`, active work packets in `executiveLoop`)
- executive-os/COO-OS.md
- executive-os/workflows/coo-operating-review.md
- executive-os/templates/work-packet-template.md

Output:
1. Operating summary
2. Plans needing packets: list every `planExecution` row with `needs_next_packet` and the next milestone to packetize (with `Source:` line for the plan file)
3. Current bottleneck
4. Next execution sequence
5. CEO escalation needed: Yes/No
6. CFO escalation needed: Yes/No
7. Analysis needed: Yes/No
8. Risk review needed: Yes/No
9. If escalation is needed, state the exact decision/question
10. If no escalation is needed, create one copy-ready work packet for the relevant local project
11. What not to touch
```
