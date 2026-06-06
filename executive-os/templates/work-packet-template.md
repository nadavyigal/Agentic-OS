# Work Packet

A work packet is created only when a task must run inside a local project repo, the project is clear, the owner role is clear, the expected validation is clear, and the task fits one focused work session. Global-OS work is not packetized. Copy the block below and fill it in.

Optional routing metadata defaults to `Workflow pattern: normal` and
`Input trust: trusted`. Add an outcome loop only when the packet advances a
multi-session business outcome.

Future important packets should include these optional but preferred fields when
they help explain why the packet exists:

- `Loop`: the business or operating loop this packet advances.
- `Signal`: what changed or what evidence triggered this packet.
- `Memory update`: what file or lesson should be updated after completion.

Daily packets should not be isolated tasks. They should advance a loop when
possible:

`Signal -> Diagnosis -> Recommendation -> Action -> Result -> Memory`

Example loops: RunSmart App Store launch loop, RunSmart GTM loop, ASO conversion
loop, first 100 users learning loop, monetization readiness loop, Resumely
submission readiness loop, AI Audit Toolkit client discovery loop, AI Audit
Toolkit delivery loop.

Keep this lean. Do not make work packets heavy just to fill optional fields.

---

# Work Packet

- Status: Draft
- Source: [Plan, decision, or status source]
- Workflow pattern: normal
- Input trust: trusted
- Outcome loop: [Optional loop slug]
- Loop: [Optional business or operating loop]
- Signal: [Optional trigger or evidence]
- Memory update: [Optional destination file or lesson]
- Success signal: [Observable evidence or metric]

## Owner Role
[Local role]

## Project
[Project name]

## Goal
[One clear outcome]

## Context
[Why this matters now]

## Read First
- AGENTS.md
- CODEX.md or CLAUDE.md
- tasks/progress.md, if present
- tasks/todo.md
- tasks/session-log.md
- tasks/lessons.md, if relevant
- Relevant workflow/spec

## Task
[Exact task]

## Constraints
- Do not touch unrelated files.
- Do not deploy, submit, bill, email, or change production services without explicit approval.
- Do not invent validation results.
- Keep the task to one focused work session.

## Validation
[Build/test/manual QA required]

## Completion Gate
Before final response, update or report:
- tasks/todo.md
- tasks/progress.md, if present
- tasks/session-log.md
- tasks/lessons.md only if a reusable lesson was learned

## Final Output
- What changed
- Files changed
- Commands run
- Validation evidence
- Remaining risks
- Next recommended action
