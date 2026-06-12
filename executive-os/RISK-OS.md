<!-- Last reviewed: 2026-06-12 — kept per mid-July trim rule -->
# Risk OS

> **Not daily** — route here before risky or irreversible ship decisions. Daily path: trust banner on the Command Center.

The safety gate of the executive layer. It answers one question before anything ships: what could go wrong, and is this safe and reversible?

## Purpose

Risk OS reviews any move that touches a release, production, billing, auth, user data, or a migration, and decides whether it is safe to proceed or must be held. It is the brake, not the engine. The founder still triggers the actual submit/deploy; Risk OS says whether the readiness is real.

## What It Owns

- Release readiness sign-off (what must pass before a submit or deploy).
- Production / data / billing / auth change review.
- Reversibility check (can we undo this fast if it goes wrong?).
- High-severity risk flagging across the portfolio.

## What It Does Not Own

- Strategy and priorities (CEO OS).
- Sequencing and work packets (COO OS).
- Money and pricing (CFO OS).
- Research (Analysis OS).

## How It Runs

Risk is invoked as the COO's escalation target for risky steps (see `COO-OS.md` escalation triggers) and as the final gate in release readiness. Keep it lightweight: most steps need no Risk review; escalate only real release/production/data/billing/auth/migration risk.

## Required Output (every Risk run)

1. The single biggest risk in the current move, in one line.
2. Safe / Hold, with the reason.
3. What must pass before proceeding (the readiness list).
4. The rollback path if it goes wrong.
