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
import subprocess
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


def git_date(rel_path):
    """Date (YYYY-MM-DD) of the last commit touching rel_path, or None."""
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", rel_path],
            cwd=ROOT, capture_output=True, text=True, timeout=15,
        )
        return out.stdout.strip() or None
    except Exception:
        return None


def read_text(path):
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def latest_vault_weekly_review():
    """Newest 'Weekly Review - YYYY-MM-DD' note date in the Obsidian vault, or None."""
    vault = Path("/Users/nadavyigal/Documents/Projects /Nadav Builder OS/07-Weekly-Reviews")
    dates = []
    try:
        for f in vault.glob("*.md"):
            m = re.search(r"(\d{4}-\d{2}-\d{2})", f.name)
            if m:
                dates.append(m.group(1))
    except OSError:
        return None
    return max(dates) if dates else None


def build_workflows(status, usage, manual):
    """Named OS workflows with a real last-ran date each, so the dashboard can say
    'fresh / due / overdue — run it' instead of leaving cadence to memory."""
    ceo_text = read_text(ROOT / "executive-os" / "WEEKLY-CEO-LATEST.md")
    m = re.search(r"^- Reviewed:\s*(\d{4}-\d{2}-\d{2})", ceo_text, re.M)
    ceo_date = m.group(1) if m else git_date("executive-os/WEEKLY-CEO-LATEST.md")

    growth_text = read_text(ROOT / "distribution-os" / "weekly-growth-review.md")
    growth_dates = re.findall(r"Week of (\d{4}-\d{2}-\d{2})", growth_text)
    growth_date = max(growth_dates) if growth_dates else git_date("distribution-os/weekly-growth-review.md")

    coo = status.get("latestCooReview", {}) or {}
    coo_date = coo.get("reviewed") or git_date("executive-os/COO-LATEST-REVIEW.md")

    return [
        {
            "id": "refresh", "name": "Repo refresh (rebuilds this page)",
            "cadence": "daily", "warn": 1.5, "crit": 3,
            "lastRan": status.get("metadata", {}).get("lastSuccessfulRefresh"),
            "how": "Re-reads every repo and rebuilds all auto sections of this page.",
            "run": {"type": "command", "text": "./agentic-os refresh"},
        },
        {
            "id": "metrics", "name": "Live numbers refresh (PostHog layer)",
            "cadence": "weekly", "warn": 5, "crit": 9,
            "lastRan": manual.get("asOf"),
            "how": "Claude pulls founder-excluded PostHog numbers and updates the funnels, traffic and founder queue on this page.",
            "run": {"type": "prompt", "text": (
                "Refresh my Portfolio HQ. 1) Pull live PostHog numbers with founder/QA/bot accounts excluded: "
                "weekly people (Resumely) and weekly installs (RunSmart), plus both activation funnels. "
                "2) In the Agentic OS repo, update dashboard/portfolio-hq-manual.json — bump asOf and update traffic, "
                "funnels, activationHeadline, clocks, founderCommand, knownUnknown and weekPriorities where reality changed. "
                "3) Run ./agentic-os refresh. 4) Tell me in plain language what changed and whether any clock or decision became urgent."
            )},
        },
        {
            "id": "ceo", "name": "Weekly CEO review",
            "cadence": "weekly", "warn": 8, "crit": 12,
            "lastRan": ceo_date,
            "how": "Reads the whole portfolio and picks the week's top 3. Output lands on the Executive tab.",
            "run": {"type": "prompt", "text": (
                "Run the weekly CEO review. In the Agentic OS repo, read PROMPTS/executive-weekly-review.md and follow it "
                "end to end: refresh status first, update executive-os/WEEKLY-CEO-LATEST.md, and log any new decisions in "
                "executive-os/EXECUTIVE-DECISIONS.md."
            )},
        },
        {
            "id": "coo", "name": "COO operating review",
            "cadence": "as needed", "warn": 10, "crit": 21,
            "lastRan": coo_date,
            "how": "Answers 'what do I do next?' from current evidence when you feel lost between sessions.",
            "run": {"type": "prompt", "text": (
                "Run a COO operating review. In the Agentic OS repo, read PROMPTS/coo-operating-review.md and follow it: "
                "pick the single best next action from current repo evidence and record it in executive-os/COO-LATEST-REVIEW.md."
            )},
        },
        {
            "id": "growth", "name": "Distribution growth review",
            "cadence": "weekly", "warn": 8, "crit": 12,
            "lastRan": growth_date,
            "how": "Logs the weekly growth cycle: what ran, what the numbers did, what to try next. Feeds the Growth tab.",
            "run": {"type": "prompt", "text": (
                "Run the weekly distribution review. In the Agentic OS repo, read PROMPTS/distribution-weekly.md and follow it: "
                "log this week's cycle in distribution-os/weekly-growth-review.md and move experiment rows in "
                "distribution-os/experiment-log.md to their true status (WP-31 Hebrew ASO and WP-32 FB-groups are live but unlogged)."
            )},
        },
        {
            "id": "vault", "name": "Weekly review note (Obsidian)",
            "cadence": "weekly", "warn": 8, "crit": 12,
            "lastRan": latest_vault_weekly_review(),
            "how": "The human-readable week summary in the vault (07-Weekly-Reviews).",
            "run": {"type": "prompt", "text": (
                "Write this week's weekly review note in the Nadav Builder OS vault. Follow "
                "01-Agentic-OS/Workflows/weekly-obsidian-review.md, using the refreshed Agentic OS dashboard as input."
            )},
        },
        {
            "id": "cfo", "name": "Finance review (CFO)",
            "cadence": "monthly", "warn": 32, "crit": 45,
            "lastRan": None,
            "how": "Monthly money check. No logged run found yet — it has never produced a dated artifact.",
            "run": {"type": "prompt", "text": (
                "Run the monthly CFO review. In the Agentic OS repo, read PROMPTS/cfo-monthly-review.md and follow it; "
                "save the dated output under executive-os/reviews/ so the dashboard can track when it last ran."
            )},
        },
        {
            "id": "usage", "name": "Cost tracker (token spend)",
            "cadence": "weekly", "warn": 5, "crit": 10,
            "lastRan": usage.get("generatedAt"),
            "how": "Collects Claude Code token cost per project (Numbers tab).",
            "run": {"type": "command", "text": "python3 scripts/usage/collect_usage.py"},
        },
    ]


def build_executive(status):
    """Executive OS layer: latest weekly CEO read + COO review, parsed from their files."""
    text = read_text(ROOT / "executive-os" / "WEEKLY-CEO-LATEST.md")
    reviewed = None
    m = re.search(r"^- Reviewed:\s*(\d{4}-\d{2}-\d{2})", text, re.M)
    if m:
        reviewed = m.group(1)
    else:
        m = re.search(r"^# .*?(\d{4}-\d{2}-\d{2})", text, re.M)
        reviewed = m.group(1) if m else git_date("executive-os/WEEKLY-CEO-LATEST.md")

    operating_read = ""
    m = re.search(r"^## Operating Read\s*\n+(.+?)(?:\n\n|\nEvidence:)", text, re.S | re.M)
    if m:
        operating_read = " ".join(m.group(1).split())

    top3 = []
    m = re.search(r"^## Top 3 Priorities\s*\n(.*?)(?:\n## |\Z)", text, re.S | re.M)
    if m:
        for line in m.group(1).splitlines():
            pm = re.match(r"^\d+\.\s+\*\*(.+?)\*\*\s*(.*)$", line.strip())
            if pm:
                body = re.sub(r"\s*Source:.*$", "", pm.group(2)).strip()
                top3.append({"title": pm.group(1).rstrip("."), "body": body})

    return {
        "ceoReviewed": reviewed,
        "operatingRead": operating_read,
        "top3": top3,
        "coo": status.get("latestCooReview", {}) or {},
    }


def build_distribution():
    """Distribution OS layer: active experiments + last logged growth cycle."""
    text = read_text(ROOT / "distribution-os" / "experiment-log.md")
    experiments = []
    m = re.search(r"^## Active\s*\n(.*?)(?:\n## |\Z)", text, re.S | re.M)
    if m:
        for line in m.group(1).splitlines():
            if not line.startswith("|") or re.match(r"^\|\s*(ID|---|-)", line.strip()):
                continue
            cols = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cols) >= 7 and cols[0]:
                experiments.append({
                    "id": cols[0], "product": cols[1], "channel": cols[2],
                    "hypothesis": cols[3], "score": cols[5], "status": cols[6],
                })

    growth_text = read_text(ROOT / "distribution-os" / "weekly-growth-review.md")
    growth_dates = re.findall(r"Week of (\d{4}-\d{2}-\d{2})", growth_text)
    return {
        "experiments": experiments,
        "lastGrowthReview": max(growth_dates) if growth_dates else None,
        "logTouched": git_date("distribution-os/experiment-log.md"),
    }


def build_auto(status, usage, manual):
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
        "workflows": build_workflows(status, usage, manual),
        "executive": build_executive(status),
        "distribution": build_distribution(),
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
        "auto": redact_paths(build_auto(status, usage, manual)),
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
