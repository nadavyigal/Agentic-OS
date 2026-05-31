# PLANS.md

Use this template for complex Agentic OS work that spans multiple files, tools, or phases. Keep active execution plans in `docs/superpowers/plans/` when a persistent artifact is needed.

## Template

Goal: <one sentence, one verifiable outcome>

Constraints:
- Do not touch unrelated files.
- Do not run deploys, migrations, publishing, or paid actions without explicit approval.
- Do not store secrets in repo files.

Phases:
1. Discovery: read source files, memory, errors, and decisions.
2. Plan: define scope, files, risks, and verification.
3. Implement: make the smallest change that satisfies the goal.
4. Review: simplify, remove unnecessary changes, and check for drift.
5. Verify: run documented checks, record skipped checks and risks.

Stop for Nadav on:
- irreversible external writes
- production or billing impact
- new dependencies or tools
- scope expanding beyond 3 unexpected files
- uncertainty about source of truth
