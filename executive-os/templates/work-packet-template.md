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
- Mode: [Prototyper | Builder | Sweeper | Grower | Maintainer] — see `AGENTS.md` Mode Contracts for what each permits
- Source: [Plan, decision, or status source]
- Workflow pattern: normal
- Input trust: trusted
- Outcome loop: [Optional loop slug]
- Loop: [Optional business or operating loop]
- Signal: [Optional trigger or evidence]
- Memory update: [Optional destination file or lesson]
- Success signal: [Observable evidence or metric]
- Model route: [Default model/tier to run this packet — see GLOBAL-TOOL-USAGE.md "Model routing". Multi-story packets add a per-story "Model route" column in the Stories table instead, e.g. WP-40]
- Rollback: [How to undo this if it lands badly — required when Mode is Maintainer, or when the packet touches auth, billing, data, migrations, or deployment config. Name the concrete step: revert PR #N, flip flag X off, restore from migration Y. "Revert the commit" only counts when nothing else changed state]

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
- Secrets: [none | the named credentials this packet may read, e.g. `OPENAI_API_KEY` from the local env]. Never write, print, commit, or move a production secret. If the task cannot proceed without a credential not named here, stop and ask.
- Do not touch unrelated files.
- Do not deploy, submit, bill, email, or change production services without explicit approval.
- Do not invent validation results.
- Keep the task to one focused work session.

## Validation
[Name a runnable command or eval when one exists — e.g. `npm test`, `pytest`, or a
named eval harness (RunSmart plan-generator eval, ResumeBuilder resume-optimizer
eval). Fall back to manual QA steps only when no runnable check exists for this
task.]

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
