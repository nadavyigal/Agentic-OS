# Executive Rhythm

The operating cadence for the Executive Intelligence OS. Manual rhythm first; this is
the heartbeat that makes the rest of the layer useful. Each entry says what to run
and which existing artifact it reuses.

| Cadence | Ritual | Run / reuse | Output |
|---|---|---|---|
| Daily | Check-in | `DAILY.md` Tier 0: `./agentic-os morning` + Command Center (trust, packets, plan index) | One execution move; executive docs only if needed |
| On-demand | COO Operating Review | `PROMPTS/coo-operating-review.md` → `workflows/coo-operating-review.md` | Next execution sequence + one work packet |
| Weekly | CEO Review | `PROMPTS/executive-weekly-review.md` → `workflows/weekly-ceo-review.md` | Top 3, decisions, stop-doing, delegation, dashboard update |
| Weekly | Product review | `./agentic-os morning` + `PROMPTS/morning-brief.md` (optional depth) | Cross-project execution status + **plan progress** (`planExecution` index, `needs_next_packet`) |
| Weekly | Distribution review | `../distribution-os/weekly-growth-review.md` (existing) | Channel status feeding the CEO Review |
| Monthly | CFO Review | `PROMPTS/cfo-monthly-review.md` → `workflows/monthly-finance-review.md` | Financial snapshot, runway, risks, recommended financial actions |
| Monthly | Strategy review | `workflows/weekly-ceo-review.md` run at portfolio depth | Portfolio tradeoffs, focus rules check |
| Quarterly | OKR review | `templates/okr-template.md` (Phase 2 workflow) | Set / score quarterly OKRs |

## Recommended Order Within The Weekly CEO Review

1. Pull product status (`morning-brief` + `DASHBOARD.md` + `PROJECT-STATUS.md`).
2. Pull distribution status (`distribution-os/weekly-growth-review.md`).
3. Pull CFO snapshot if a Monthly Finance Review is current.
4. Pull open decisions (`EXECUTIVE-DECISIONS.md`) and metrics (`EXECUTIVE-METRICS.md`).
5. Produce the review, update `EXECUTIVE-DASHBOARD.md`, log any new decisions.

## Principles

- Do not skip the manual rhythm to build automation.
- Reuse existing reviews; the Executive layer synthesizes, it does not re-collect.
- Every ritual ends with a recommended action and, where relevant, a logged decision.
