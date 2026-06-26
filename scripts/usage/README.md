# Token / cost observability

Makes AI-development OpEx visible across tools and models, so spend can be
managed and routed. This is benchmark item #3 (observability) and the data that
feeds item #4 (model routing) and #5 (context diet).

## Run

```bash
python3 scripts/usage/collect_usage.py --since 7     # last 7 days
python3 scripts/usage/collect_usage.py --since 30 --quiet
```

Writes:
- `dashboard/usage.json` — structured summary (total cost, by tool / model / project / day)
- `dashboard/usage-log.jsonl` — normalized per-session records

## Coverage (by what each tool persists on disk)

| Tool | Captured | Notes |
|---|---|---|
| **Claude Code** (Opus/Sonnet/Haiku) | Full token usage + model + project, priced | Read from `~/.claude/projects/**/*.jsonl`. The accurate, complete source. |
| **Codex CLI** | Activity only (sessions per project, rate-limit %) | Codex does **not** persist per-request token counts (`token_count` events carry only rate-limit %), so no cost is computed. |
| **Cursor / Composer** | Not captured | Cursor keeps usage in opaque SQLite state, not a parseable log. To include it, append records to `dashboard/usage-manual.jsonl` (one JSON object per line: `{"tool":"cursor","project":"RunSmart","model_family":"sonnet","input_tokens":...,"output_tokens":...,"cost_usd":...,"day":"2026-06-26"}`). |

## Pricing

`PRICES` in `collect_usage.py` is USD per million tokens and is **directional** —
verify against current pricing (the `claude-api` skill or anthropic.com/pricing)
and edit the one dict. Cache-read tokens are priced at the cache-read rate and,
for long sessions, are usually the largest single cost component.

## Wire into the daily refresh (optional)

Add this line to the Agentic OS refresh flow so the dashboard always has fresh
spend data:

```bash
python3 scripts/usage/collect_usage.py --since 30 --quiet
```

Then a dashboard view can read `dashboard/usage.json`.

## What the first run revealed (2026-06-26)

- Opus dominated spend (~83%) over Sonnet, on fewer sessions.
- Cache-read tokens from long sessions were the dominant cost driver (a single
  377-turn session carried ~90M cache-read tokens).
- The orchestration layers (Agentic OS, Builder OS vault) cost more than the
  product repos — a signal to route that work to cheaper models (#4) and trim
  static context (#5).
