#!/usr/bin/env python3
"""Refresh dashboard/portfolio-hq.html from status.json + usage.json + the manual metrics layer.

Reads (read-only):
  - dashboard/status.json              (rebuilt by ./agentic-os refresh, just before this runs)
  - dashboard/usage.json               (rebuilt by scripts/usage/collect_usage.py)
  - dashboard/portfolio-hq-manual.json (PostHog metrics + founder queue; hand/Claude-maintained)

Writes:
  - dashboard/portfolio-hq.html — replaces the <script id="hq-data"> JSON block.

Runs automatically as the last step of `./agentic-os refresh` / `./agentic-os morning`.
Also runnable standalone: `python3 scripts/portfolio_hq/refresh_portfolio_hq.py`.
No dependencies beyond the standard library. Exits non-zero on any problem.
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DASHBOARD = ROOT / "dashboard"
HTML = DASHBOARD / "portfolio-hq.html"
MANUAL = DASHBOARD / "portfolio-hq-manual.json"
STATUS = DASHBOARD / "status.json"
USAGE = DASHBOARD / "usage.json"

PACKET_DONE = {"closed", "completed", "superseded", "shipped", "posted"}
DECISION_DONE = {"closed", "done", "superseded", "reconciled"}

# status.json text fields (work packet "project"/"goal"/etc.) sometimes carry absolute local
# filesystem paths (e.g. a client repo path). This dashboard ends up in a public repo, so strip
# them from the auto layer before embedding rather than repeating them verbatim.
ABSOLUTE_PATH = re.compile(r"/Users/[^`\"\n)]+")


def redact_paths(value):
    if isinstance(value, str):
        return ABSOLUTE_PATH.sub("<local path redacted>", value)
    if isinstance(value, list):
        return [redact_paths(v) for v in value]
    if isinstance(value, dict):
        return {k: redact_paths(v) for k, v in value.items()}
    return value


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        sys.exit(f"ERROR: missing {path}")
    except json.JSONDecodeError as e:
        sys.exit(f"ERROR: bad JSON in {path}: {e}")


def build_auto(status, usage):
    packets = [
        {
            "title": w.get("title"),
            "status": w.get("status"),
            "project": w.get("project"),
            "goal": w.get("goal"),
            "path": w.get("path"),
            "copyPrompt": w.get("copyPrompt"),
        }
        for w in status.get("osRegistry", {}).get("workPackets", [])
        if str(w.get("status", "")).lower() not in PACKET_DONE
    ]
    decisions = [
        d
        for d in status.get("decisions", [])
        if str(d.get("status", "")).lower() not in DECISION_DONE
    ]
    health = [
        {
            k: p.get(k)
            for k in (
                "id", "name", "state", "nextAction", "blockers", "dirty",
                "dirtyCount", "extraWorktrees", "branch", "lastCommit",
                "freshness", "stale", "evidenceGap", "evidenceDate",
                "buildStatus", "gtm",
            )
        }
        for p in status.get("projectHealth", [])
    ]
    stranded = status.get("strandedWork", {})
    usage_by_project = {
        k: round(v.get("cost_usd", 0), 2)
        for k, v in usage.get("byProject", {}).items()
    }
    return {
        "summary": {
            "overallStatus": status.get("summary", {}).get("overallStatus"),
            "bestNextAction": status.get("summary", {}).get("bestNextAction"),
            "mainBlockers": status.get("summary", {}).get("mainBlockers", []),
            "needsDecision": status.get("summary", {}).get("needsDecision", []),
        },
        "trust": status.get("portfolioTrust", {}),
        "priority": {
            "now": status.get("priorityBoard", {}).get("now", []),
            "next": status.get("priorityBoard", {}).get("next", []),
            "blocked": status.get("priorityBoard", {}).get("blocked", []),
            "laterCount": len(status.get("priorityBoard", {}).get("later", [])),
        },
        "health": health,
        "stranded": {
            "generatedOn": stranded.get("generatedOn"),
            "actionableCount": stranded.get("actionableCount", 0),
            "items": stranded.get("items", []),
        },
        "packets": packets,
        "prompts": status.get("projectPrompts", []),
        "decisions": decisions,
        "groundTruth": {
            "apps": status.get("groundTruth", {}).get("apps", []),
            "posthog": status.get("groundTruth", {}).get("posthog", []),
            "appStore": status.get("groundTruth", {}).get("appStore", []),
            "contradictions": status.get("groundTruth", {}).get("contradictions", []),
        },
        "usage": {
            "generatedAt": usage.get("generatedAt"),
            "windowDays": usage.get("windowDays"),
            "totalCostUsd": usage.get("totalCostUsd"),
            "byProject": usage_by_project,
            "note": usage.get("note"),
        },
    }


def main():
    status = load(STATUS)
    usage = load(USAGE)
    manual = load(MANUAL)

    payload = {
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "sources": {
            "status": status.get("metadata", {}).get("lastSuccessfulRefresh"),
            "usage": usage.get("generatedAt"),
            "manual": manual.get("asOf"),
        },
        "auto": redact_paths(build_auto(status, usage)),
        "manual": manual,
    }

    html = HTML.read_text(encoding="utf-8")
    blob = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    # </script> inside JSON strings would terminate the block early
    blob = blob.replace("</", "<\\/")
    new_html, n = re.subn(
        r'(<script id="hq-data" type="application/json">).*?(</script>)',
        lambda m: m.group(1) + "\n" + blob + "\n" + m.group(2),
        html,
        count=1,
        flags=re.S,
    )
    if n != 1:
        sys.exit("ERROR: hq-data block not found in dashboard/portfolio-hq.html")
    HTML.write_text(new_html, encoding="utf-8")
    print(f"- portfolio HQ: refreshed (dashboard/portfolio-hq.html, {len(payload['auto']['packets'])} open packets, "
          f"{payload['auto']['stranded']['actionableCount']} stranded, {len(payload['auto']['decisions'])} open decisions)")


if __name__ == "__main__":
    main()
