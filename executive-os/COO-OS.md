# COO OS

> **Not daily** — route here when sequencing is unclear or the Command Center shows **Needs next packet** for a strategic plan. Daily path: active work packets on the Command Center.

The minimal operations layer. It turns a plan into an ordered, executable sequence and decides what becomes a work packet. It is intentionally thin: enough to move from plan to execution without standing up the full Executive OS.

## Purpose

The COO OS owns operations, execution sequence, bottlenecks, work packets, handoffs, release readiness, status hygiene, and QA sequencing. It is the layer that answers "what happens next, where, and in what order," so the founder is not re-deciding sequencing every session.

It is run by `agents/coo-agent.md` and operated via `workflows/coo-operating-review.md`. Its job is to **sequence and packetize**, not to strategize.

## What It Owns

- Execution sequencing (first, second, third).
- Bottleneck identification (what is blocked, by what, and who owns the unblock).
- Work packet creation (one focused, repo-bound task at a time).
- **Long-running plans** (GTM, launch, monetization, distribution): the plan stays the strategy source; the COO extracts the **next milestone** into one packet with `Source:` pointing at the plan. If the dashboard shows `needs_next_packet`, draft that packet — the plan is not abandoned.
- Repo routing (which local project receives the next packet).
- Handoffs between sessions and roles.
- Release readiness sequencing (what must pass before a submit/deploy action, which the founder still triggers).
- QA sequencing (what needs verification, in what order).
- Status hygiene (keep the dashboard/action board clean; flag drift; never invent status).
- Escalation routing (decide whether CEO / CFO / Analysis / Risk input is actually required).

## What It Does Not Own

- Strategy, focus, priorities, portfolio tradeoffs (CEO OS).
- Pricing, budgets, revenue, unit economics, monetization decisions (CFO OS).
- Research, opportunities, competitor/market scans (Analysis OS).
- Implementation inside a repo (the local project OS owns that; the COO routes a packet to it).
- Submitting, deploying, billing, emailing, migrating, or changing production services. The COO sequences readiness; the founder triggers the action.

## The Questions COO OS Answers

- What is blocked?
- What should happen first, second, third?
- Which repo should receive the next work packet?
- What needs QA?
- What should not be touched?
- Is CEO / CFO / Analysis / Risk escalation needed?

## Required Output (every COO run)

1. **Operating summary** - one short paragraph: where execution stands right now.
2. **Current bottleneck** - the single thing most blocking forward motion, and who owns the unblock.
3. **Execution sequence** - ordered first / second / third, each tagged manual-founder, local-repo, global-OS, research, or QA.
4. **Escalation needed** - explicit Yes/No for CEO, CFO, Analysis, Risk. Default No.
5. **One work packet** - only if execution inside a local repo is the next step (see Work Packet Rule).
6. **What not to touch** - the explicit do-not-touch list for the current step.

## Focus Rules (inherited, do not override)

1. RunSmart before Resumely when they compete for time (`CEO-OS.md`). The COO may still place Resumely first in the *queue* when RunSmart is externally blocked, and must say so.
2. One submission sprint at a time; do not split the sprint.
3. Manual operating rhythm before automation.
4. No paid-acquisition spend until activation and retention are visible.
5. Never invent status. Parse local task files; narrative-only status is not confirmed (`DECISIONS.md` 2026-06-02 Dashboard Trust Rule).

## Escalation Triggers (so escalation stays rare)

Escalate only when the blocker is genuinely owned by another layer. Default to No.

- **CEO** - a strategy, focus, priority, scope, or portfolio-tradeoff decision is required, or two A-priorities truly compete for the same time. Not for routine sequencing.
- **CFO** - a spend, price, or monetization decision blocks the next step. Not for tracking costs that do not block execution.
- **Analysis** - the next decision needs external research or evidence not present in the repos.
- **Risk** - the next step is risky or hard to reverse (release, production, billing, auth, data, migration), or a new high-severity risk appeared.

If none apply, the COO does not escalate. It sequences and, if work is needed in a repo, emits one work packet.

## Work Packet Rule

Create a work packet **only when all four hold**:

- The task must be executed inside a local project repo.
- The target project is clear.
- The owner role is clear.
- The expected validation is clear.
- (And) the task fits one focused work session.

Global-OS work (drafts, sequencing, status hygiene, channel scoring) is **not** packetized. It runs in this OS. Use `templates/work-packet-template.md` for the packet format. Active packets are saved one-file-per-packet under `work-packets/` with a status header (e.g. `work-packets/WP-1-resumely-device-smoke.md`).

## Workflows

Phase 1 (live):

- COO Operating Review - `workflows/coo-operating-review.md` (run via `PROMPTS/coo-operating-review.md`).

## Inputs (reuse, do not re-collect)

- `../DASHBOARD.md`, `../PROJECT-STATUS.md`, `../dashboard/status.json` - portfolio status and action board.
- `BUSINESS-GTM-PLAN-V0.md` - the current plan and its work-packet outlines (WP-1..WP-5).
- `EXECUTIVE-DECISIONS.md` - to see which decisions are open (escalation signal).
- The relevant `PROJECT-BRIDGES/*.md` only when repo routing needs it.

## Rules

- Reuse existing status; synthesize, do not re-derive.
- Separate facts from assumptions; never invent status or numbers (`unknown - need: <source>`).
- Keep escalation rare; the COO exists to prevent unnecessary CEO/CFO/Analysis/Risk churn.
- One work packet per run when execution is needed; do not batch.
- The founder triggers any submit/deploy/bill/email/migrate action; the COO only sequences readiness.
- Keep this layer thin. Do not expand into the full Executive OS; that work stays in `EXECUTIVE-BACKLOG.md`.
