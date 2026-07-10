#!/usr/bin/env python3
"""Cross-tool token/cost observability collector.

Makes AI development OpEx visible across tools and models so spend can be
managed (and routed — see benchmark item #4). Writes a summary the Agentic OS
dashboard reads.

Coverage (by what each tool actually persists on disk):
  - Claude Code  : FULL token usage + model + project (per-message). Priced.
  - Codex CLI    : activity only (sessions per project + rate-limit %). Codex
                   does not persist per-request token counts, so no cost.
  - Cursor       : not captured (state lives in opaque SQLite). Add manual
                   records to usage-manual.jsonl to include it (see README).

Usage:
  python3 collect_usage.py [--since DAYS] [--quiet]

Outputs (next to the dashboard):
  dashboard/usage.json        structured summary (consumed by the dashboard)
  dashboard/usage-log.jsonl   append-only normalized per-session records
"""
import argparse
import collections
import datetime as dt
import glob
import json
import os
import sys

HOME = os.path.expanduser("~")
CLAUDE_PROJECTS = os.path.join(HOME, ".claude", "projects")
CODEX_DIRS = [os.path.join(HOME, ".codex", "archived_sessions"), os.path.join(HOME, ".codex", "sessions")]
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DASHBOARD = os.path.join(ROOT, "dashboard")
MANUAL = os.path.join(DASHBOARD, "usage-manual.jsonl")

# Price table, USD per million tokens. Verified 2026-07-10 against the claude-api
# skill / dashboard/model-registry.json. Opus 4.x is $5/$25 — NOT the Claude-3-era
# $15/$75 (that stale row inflated the Opus cost line ~3x). cache_write = 1.25x in,
# cache_read = 0.1x in. Sonnet 5 lists $3/$15 ($2/$10 intro through 2026-08-31 —
# using the standard rate here so cost isn't understated after the intro ends).
PRICES = {
    "opus":   {"in": 5.0,  "out": 25.0, "cache_write": 6.25,  "cache_read": 0.50},
    "sonnet": {"in": 3.0,  "out": 15.0, "cache_write": 3.75,  "cache_read": 0.30},
    "haiku":  {"in": 1.0,  "out": 5.0,  "cache_write": 1.25,  "cache_read": 0.10},
}
DEFAULT_FAMILY = "sonnet"  # unknown models priced as sonnet (clearly flagged)


def family_for(model: str) -> str:
    m = (model or "").lower()
    for fam in ("opus", "sonnet", "haiku"):
        if fam in m:
            return fam
    return DEFAULT_FAMILY


def project_for(cwd: str) -> str:
    c = (cwd or "")
    for needle, label in (
        ("RunSmart", "RunSmart"),
        ("ResumeBuilder", "ResumeBuilder"),
        ("Agentic OS", "Agentic OS"),
        ("Nadav Builder OS", "Builder OS Vault"),
        ("IOS RunSmart", "RunSmart iOS"),
    ):
        if needle in c:
            return label
    return os.path.basename(c.rstrip("/")) or "unknown"


def cost_for(family: str, u: dict) -> float:
    p = PRICES.get(family, PRICES[DEFAULT_FAMILY])
    return (
        u.get("input_tokens", 0) * p["in"]
        + u.get("output_tokens", 0) * p["out"]
        + u.get("cache_creation_input_tokens", 0) * p["cache_write"]
        + u.get("cache_read_input_tokens", 0) * p["cache_read"]
    ) / 1_000_000


def parse_ts(s: str):
    try:
        return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def collect_claude(since: dt.datetime):
    """Yield per-session aggregated records from Claude Code transcripts."""
    sessions = {}  # session_id -> aggregate
    for path in glob.glob(os.path.join(CLAUDE_PROJECTS, "*", "*.jsonl")):
        try:
            if dt.datetime.fromtimestamp(os.path.getmtime(path), dt.timezone.utc) < since:
                continue
        except OSError:
            continue
        with open(path, "r", errors="ignore") as fh:
            for line in fh:
                if '"usage"' not in line:
                    continue
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                msg = d.get("message", {})
                usage = msg.get("usage")
                if not isinstance(usage, dict):
                    continue
                sid = d.get("sessionId") or os.path.basename(path)
                fam = family_for(msg.get("model", ""))
                rec = sessions.setdefault(sid, {
                    "tool": "claude-code", "session": sid,
                    "project": project_for(d.get("cwd", "")),
                    "model_family": fam, "models": set(),
                    "input_tokens": 0, "output_tokens": 0,
                    "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0,
                    "cost_usd": 0.0, "first_ts": None, "last_ts": None,
                })
                rec["models"].add(msg.get("model", "?"))
                for k in ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"):
                    rec[k] += usage.get(k, 0) or 0
                rec["cost_usd"] += cost_for(fam, usage)
                ts = parse_ts(d.get("timestamp", ""))
                if ts:
                    iso = ts.isoformat()
                    if rec["first_ts"] is None or iso < rec["first_ts"]:
                        rec["first_ts"] = iso
                    if rec["last_ts"] is None or iso > rec["last_ts"]:
                        rec["last_ts"] = iso
    for rec in sessions.values():
        rec["models"] = sorted(m for m in rec["models"] if m and m != "?")
        rec["day"] = (rec["last_ts"] or "")[:10]
        yield rec


def collect_codex(since: dt.datetime):
    """Codex persists no token counts; yield activity records (project + rate-limit %)."""
    for d in CODEX_DIRS:
        for path in glob.glob(os.path.join(d, "*.jsonl")):
            try:
                if dt.datetime.fromtimestamp(os.path.getmtime(path), dt.timezone.utc) < since:
                    continue
            except OSError:
                continue
            cwd, ts0, rl = "", "", None
            with open(path, "r", errors="ignore") as fh:
                for line in fh:
                    if '"session_meta"' not in line and '"token_count"' not in line:
                        continue
                    try:
                        rec = json.loads(line)
                    except Exception:
                        continue
                    p = rec.get("payload", {})
                    if rec.get("type") == "session_meta":
                        cwd = p.get("cwd", cwd)
                        ts0 = p.get("timestamp", ts0) or rec.get("timestamp", ts0)
                    elif p.get("type") == "token_count":
                        prim = (p.get("rate_limits") or {}).get("primary") or {}
                        rl = prim.get("used_percent", rl)
            yield {
                "tool": "codex", "session": os.path.basename(path),
                "project": project_for(cwd), "day": (ts0 or "")[:10],
                "rate_limit_used_percent": rl,
                "input_tokens": 0, "output_tokens": 0, "cost_usd": 0.0,
                "note": "codex does not persist token counts",
            }


def collect_manual():
    if not os.path.exists(MANUAL):
        return
    with open(MANUAL, "r", errors="ignore") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                yield json.loads(line)
            except Exception:
                continue


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", type=int, default=30, help="look back this many days")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()
    since = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=args.since)

    records = list(collect_claude(since)) + list(collect_codex(since)) + list(collect_manual())

    def agg(key):
        out = collections.defaultdict(lambda: {"cost_usd": 0.0, "input_tokens": 0, "output_tokens": 0, "cache_read_tokens": 0, "sessions": 0})
        for r in records:
            k = r.get(key) or "unknown"
            out[k]["cost_usd"] += r.get("cost_usd", 0.0)
            out[k]["input_tokens"] += r.get("input_tokens", 0)
            out[k]["output_tokens"] += r.get("output_tokens", 0)
            out[k]["cache_read_tokens"] += r.get("cache_read_input_tokens", 0)
            out[k]["sessions"] += 1
        return {k: {**v, "cost_usd": round(v["cost_usd"], 2)} for k, v in sorted(out.items(), key=lambda x: -x[1]["cost_usd"])}

    total_cost = round(sum(r.get("cost_usd", 0.0) for r in records), 2)
    total_cache_read = sum(r.get("cache_read_input_tokens", 0) for r in records)
    summary = {
        "generatedAt": dt.datetime.now(dt.timezone.utc).isoformat(),
        "windowDays": args.since,
        "totalCostUsd": total_cost,
        "totalCacheReadTokens": total_cache_read,
        "sessionCount": len(records),
        "note": "Claude Code: priced from on-disk usage (PRICES verified 2026-07-10 vs model-registry.json; Opus now $5/$25, was mis-priced at Claude-3-era $15/$75). Codex: activity only (no token counts persisted). Cursor: not captured (see README). Cache-read tokens (from long sessions) are typically the dominant cost driver.",
        "byTool": agg("tool"),
        "byProject": agg("project"),
        "byModelFamily": agg("model_family"),
        "byDay": agg("day"),
    }

    os.makedirs(DASHBOARD, exist_ok=True)
    with open(os.path.join(DASHBOARD, "usage.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
    with open(os.path.join(DASHBOARD, "usage-log.jsonl"), "w") as fh:
        for r in records:
            fh.write(json.dumps(r) + "\n")

    if not args.quiet:
        print(f"Token/cost — last {args.since}d — total ${total_cost} across {len(records)} sessions\n")
        print(f"{'by model':<18}{'cost':>10}{'sessions':>10}")
        for k, v in summary["byModelFamily"].items():
            print(f"{k:<18}{('$'+str(v['cost_usd'])):>10}{v['sessions']:>10}")
        print(f"\n{'by project':<18}{'cost':>10}{'sessions':>10}")
        for k, v in list(summary["byProject"].items())[:8]:
            print(f"{k[:17]:<18}{('$'+str(v['cost_usd'])):>10}{v['sessions']:>10}")
        print(f"\nWrote {os.path.join(DASHBOARD, 'usage.json')}")


if __name__ == "__main__":
    main()
