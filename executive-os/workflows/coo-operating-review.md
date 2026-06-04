# Workflow: COO Operating Review

The thin operations workflow. It converts current status into an ordered execution sequence and, when work belongs in a repo, one work packet. It reuses existing status; it does not re-collect it. It is not the Weekly CEO Review and does not replace it.

## Purpose

Answer six questions every run: what is blocked, what happens first/second/third, which repo gets the next packet, what needs QA, what not to touch, and whether CEO/CFO/Analysis/Risk escalation is actually needed.

## When To Use

- Any time you need the next concrete execution step from the current plan.
- Run via `PROMPTS/coo-operating-review.md`.
- Use instead of a full executive review when the question is operational, not strategic.

## Inputs (reuse, do not duplicate)

1. `../DASHBOARD.md`, `../PROJECT-STATUS.md`, `../dashboard/status.json` - status and action board.
2. `../executive-os/COO-OS.md` - ownership, escalation triggers, work packet rule.
3. `templates/work-packet-template.md` - packet format.
4. `BUSINESS-GTM-PLAN-V0.md` - plan and WP outlines, if present.
5. `EXECUTIVE-DECISIONS.md` - open decisions (escalation signal).

## Steps

1. Read the inputs. Do not re-derive status that already exists; do not invent status.
2. Identify the **current bottleneck**: the single thing most blocking forward motion, and who owns the unblock (founder, a repo, or another OS layer).
3. Build the **execution sequence** (first/second/third). Tag each step: manual-founder / local-repo / global-OS / research / QA. Respect the focus rules in `COO-OS.md`.
4. Run the **escalation test** for each layer using the triggers in `COO-OS.md`. Default each to No. Set Yes only when the blocker is genuinely owned by that layer; when Yes, write the exact decision/question.
5. If the next step runs inside a local repo and all four work packet conditions hold, emit **one** work packet from the template. Otherwise emit no packet and say why (global-OS work, blocked externally, or escalation required).
6. State **what not to touch** for the current step.
7. Note any status drift you saw, but do not edit status files unless that is the explicit task.

## Output Format

```
## COO Operating Review - <date>
1. Operating summary
2. Current bottleneck (owner of the unblock)
3. Execution sequence (first / second / third, each tagged)
4. Escalation needed:
   - CEO: Yes/No
   - CFO: Yes/No
   - Analysis: Yes/No
   - Risk: Yes/No
   (If any Yes: the exact decision/question and owning layer)
5. Work packet (one, only if execution in a repo is the next step) or "No packet - <reason>"
6. What not to touch
```

## Escalation Rules

- Escalate only when the blocker is owned by another layer (see `COO-OS.md` triggers). Routine sequencing is never an escalation.
- Multiple Yes answers are allowed but should be rare. If everything escalates, the bottleneck is a decision, not execution; say so plainly.

## Work Packet Rule

One packet per run, only when: the task runs in a local repo, the project is clear, the owner role is clear, the validation is clear, and it fits one focused session. Global-OS work is not packetized.

## Evidence Requirements

- Cite the source file or parsed task file for each blocker and status claim.
- Mark unknown values `unknown - need: <source>`. No fabrication.

## Completion Checklist

- [ ] Operating summary + single bottleneck with unblock owner.
- [ ] Sequence ordered; each step tagged by work type.
- [ ] Escalation Yes/No for all four layers; exact question where Yes.
- [ ] One packet (if repo execution is next) or a stated reason for none.
- [ ] "What not to touch" listed.
- [ ] No invented status; sources cited.

## Updates

- This workflow does not write status. If a packet is executed, the executing session updates the repo's `tasks/` files per the packet's Completion Gate.
- Add to `EXECUTIVE-LESSONS.md` only if a reusable operating lesson emerged.
