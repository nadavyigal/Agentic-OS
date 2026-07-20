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
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DASHBOARD = ROOT / "dashboard"
HTML = DASHBOARD / "portfolio-hq.html"
MANUAL = DASHBOARD / "portfolio-hq-manual.json"
STATUS = DASHBOARD / "status.json"
USAGE = DASHBOARD / "usage.json"
REGISTRY = DASHBOARD / "model-registry.json"
SITE_DATA = DASHBOARD / "site-data"
SITE_PROJECT_DATA = ROOT / "sites" / "portfolio-hq" / "data"
SITE_AUDIENCES = ("founder", "team", "public")

PACKET_DONE = {"closed", "completed", "superseded", "shipped", "posted"}
DECISION_DONE = {"closed", "done", "superseded", "reconciled"}

# How long a hand-maintained manual block may go unverified before the page
# says so out loud. A week matches the founder's weekly review cadence.
MANUAL_BLOCK_MAX_AGE_DAYS = 7

# status.json text fields (work packet "project"/"goal"/etc.) sometimes carry absolute local
# filesystem paths (e.g. a client repo path). This dashboard ends up in a public repo, so strip
# them from the auto layer before embedding rather than repeating them verbatim.
ABSOLUTE_PATH = re.compile(r"/Users/[^`\"\n)]+")
ENV_KEY = re.compile(
    r"\b[A-Z][A-Z0-9_]{3,}_(?:KEY|SECRET|TOKEN|CLIENT_ID|CLIENT_SECRET|URL)\b"
)
EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)


def redact_paths(value):
    if isinstance(value, str):
        return ABSOLUTE_PATH.sub("<local path redacted>", value)
    if isinstance(value, list):
        return [redact_paths(v) for v in value]
    if isinstance(value, dict):
        return {k: redact_paths(v) for k, v in value.items()}
    return value


def sanitize_site_value(value):
    """Remove local and credential-shaped details from hostable payloads."""
    if isinstance(value, str):
        value = ABSOLUTE_PATH.sub("<local path redacted>", value)
        value = ENV_KEY.sub("<configuration value>", value)
        return EMAIL.sub("<email redacted>", value)
    if isinstance(value, list):
        return [sanitize_site_value(item) for item in value]
    if isinstance(value, dict):
        return {key: sanitize_site_value(item) for key, item in value.items()}
    return value


def site_display_text(value):
    text = str(value or "").strip()
    text = re.sub(
        r";\s*see deferred-read entry above for query definition\.?$",
        ".",
        text,
        flags=re.I,
    )
    return text


def build_site_payload(payload, audience):
    """Build an explicit, progressively narrower hosting contract."""
    if audience not in SITE_AUDIENCES:
        raise ValueError(f"unknown Site audience: {audience}")

    auto = payload.get("auto", {})
    manual = payload.get("manual", {})
    products = []
    for product in auto.get("health", []):
        state = str(product.get("state", ""))
        if audience == "public":
            products.append(
                {
                    "name": product.get("name"),
                    "availability": (
                        "Live"
                        if re.search(r"\blive\b|post-launch", state, re.I)
                        else "In progress"
                    ),
                }
            )
            continue
        products.append(
            {
                key: product.get(key)
                for key in (
                    "name",
                    "state",
                    "nextAction",
                    "freshness",
                    "evidenceDate",
                    "dirty",
                    "dirtyCount",
                )
            }
        )

    if audience == "public":
        return sanitize_site_value(
            {
                "schemaVersion": 1,
                "audience": audience,
                "generatedAt": payload.get("generatedAt"),
                "products": products,
            }
        )

    site_payload = {
        "schemaVersion": 1,
        "audience": audience,
        "generatedAt": payload.get("generatedAt"),
        "sources": payload.get("sources", {}),
        "trust": auto.get("trust", {}),
        "consistencyIssues": auto.get("consistencyIssues", []),
        "command": {
            "bestNextAction": site_display_text(
                auto.get("summary", {}).get("bestNextAction")
            )
        },
        "products": products,
        "numbers": {
            "activation": manual.get("activationHeadline", {}),
            "funnels": [
                {
                    key: funnel.get(key)
                    for key in ("id", "name", "tag", "steps")
                }
                for funnel in manual.get("funnels", [])
            ],
        },
        "clocks": [
            {key: clock.get(key) for key in ("date", "when", "what", "state")}
            for clock in manual.get("clocks", [])
        ],
        "workflows": [
            {
                key: workflow.get(key)
                for key in ("id", "name", "cadence", "lastRan", "how")
            }
            for workflow in auto.get("workflows", [])
        ],
    }
    if audience == "founder":
        executive = auto.get("executive", {})
        # The artifact registry (manual["artifacts"]) is deliberately NOT hosted:
        # every entry names a branch and a local path, which this payload's
        # contract excludes. It renders only in the local dashboard HTML, which
        # embeds the manual layer verbatim.
        site_payload["numbers"]["posthogDashboards"] = [
            {
                key: dashboard.get(key)
                for key in (
                    "id", "product", "url", "decisionSnapshot", "exclusions",
                    "cohortCutoff", "refreshedAt", "warning",
                )
            }
            for dashboard in manual.get("posthogDashboards", [])
        ]
        site_payload.update(
            {
                "executive": {
                    "ceoReviewed": executive.get("ceoReviewed"),
                    "top3": executive.get("top3", []),
                },
                "growth": auto.get("distribution", {}),
                "models": auto.get("models", {}),
                "usage": auto.get("usage", {}),
            }
        )
    return sanitize_site_value(site_payload)


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        sys.exit(f"ERROR: missing {path}")
    except json.JSONDecodeError as e:
        sys.exit(f"ERROR: bad JSON in {path}: {e}")


def load_optional(path):
    """Like load(), but a missing/broken file returns {} instead of aborting the
    whole refresh — the Models tab is nice-to-have, not load-bearing."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


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


def string_values(value):
    """Yield text leaves from a bounded JSON-like value."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from string_values(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from string_values(item)


def parse_iso_date(value):
    """Parse a YYYY-MM-DD stamp, or return None if it is missing or malformed."""
    match = re.search(r"(\d{4}-\d{2}-\d{2})", str(value or ""))
    if not match:
        return None
    try:
        return datetime.strptime(match.group(1), "%Y-%m-%d").date()
    except ValueError:
        return None


def find_stale_manual_blocks(manual, today=None, max_age_days=MANUAL_BLOCK_MAX_AGE_DAYS):
    """Flag manual blocks whose claims have not been re-verified recently.

    portfolio-hq-manual.json is hand-maintained input that this refresh never
    writes, so it decays silently while the page keeps rendering a fresh
    `asOf` — a current-looking date stamp over stale content, which is worse
    than an obviously old page (2026-07-20).

    Each block carries its own `verified` date, checked here against the clock.
    The issues returned flow into the same surface as cross-layer
    contradictions, so an unverified block downgrades trust and becomes
    visible instead of rotting quietly behind a today-stamped header.
    """
    issues = []
    today = today or datetime.now().date()
    verified = manual.get("verified") or {}
    blocks = [
        key
        for key in manual
        if key not in ("asOf", "note", "verifiedNote", "verified")
    ]

    for key in sorted(blocks):
        raw = verified.get(key)
        stamped = parse_iso_date(raw)
        if not stamped:
            issues.append(
                {
                    "id": f"manual-unverified-{key}",
                    "source": "Manual layer freshness",
                    "message": (
                        f"Manual block '{key}' has no verified date, so nothing "
                        "vouches for its claims. Check it against a real source "
                        "and add it to \"verified\" in portfolio-hq-manual.json."
                    ),
                }
            )
            continue
        age = (today - stamped).days
        if age > max_age_days:
            issues.append(
                {
                    "id": f"manual-stale-{key}",
                    "source": "Manual layer freshness",
                    "message": (
                        f"Manual block '{key}' was last verified {raw} "
                        f"({age} days ago). Re-check it against git, the App Store, "
                        "or PostHog before acting on it — a refresh cannot make a "
                        "hand-maintained claim true."
                    ),
                }
            )
    return issues


def find_consistency_issues(auto, manual):
    """Find contradictions between independently refreshed dashboard layers.

    The checks intentionally target decision-driving claims, not historical notes.
    Historical artifacts remain intact; the current dashboard is responsible for
    warning when newer repository or metrics evidence supersedes them.
    """
    issues = []

    resumely = next(
        (f for f in manual.get("funnels", []) if f.get("id") == "resumely"),
        {},
    )
    export_count = 0
    for step in resumely.get("steps", []):
        if len(step) >= 2 and "export" in str(step[0]).lower():
            try:
                export_count = max(export_count, int(step[1]))
            except (TypeError, ValueError):
                pass
    decision_copy = " ".join(
        string_values(
            {
                "suggestedSessions": manual.get("suggestedSessions", []),
                "readouts": manual.get("readouts", []),
            }
        )
    )
    zero_export_claim = re.search(
        r"(?:0|zero)\s+real\s+(?:people\s+have\s+ever\s+)?export",
        decision_copy,
        re.I,
    )
    if export_count > 0 and zero_export_claim:
        issues.append(
            {
                "id": "resumely-export",
                "source": "Command vs Numbers",
                "message": (
                    f"The Numbers layer records {export_count} real export, but a "
                    "decision card still claims zero. Treat the card as superseded."
                ),
            }
        )

    live_versions = []
    for project in auto.get("health", []):
        if "resumely" not in str(project.get("name", "")).lower():
            continue
        match = re.search(
            r"(\d+\.\d+(?:\.\d+)?)\s*(?:\([^)]*\))?\s*live",
            str(project.get("state", "")),
            re.I,
        )
        if match:
            live_versions.append(match.group(1))
    executive_copy = " ".join(string_values(auto.get("executive", {})))
    stale_live_versions = [
        version
        for version in live_versions
        if re.search(rf"submit\s+{re.escape(version)}\b", executive_copy, re.I)
    ]
    if stale_live_versions:
        version = stale_live_versions[0]
        issues.append(
            {
                "id": "resumely-live-version",
                "source": "Products vs Executive",
                "message": (
                    f"Products says Resumely {version} is live, while the latest "
                    "executive review still says to submit it. The review is historical."
                ),
            }
        )

    logged_review = auto.get("distribution", {}).get("lastGrowthReview")
    growth_note = str(manual.get("growth", {}).get("note", ""))
    note_match = re.search(r"last logged growth cycle.*?(\d{4}-\d{2}-\d{2})", growth_note, re.I)
    if logged_review and note_match and note_match.group(1) < str(logged_review)[:10]:
        issues.append(
            {
                "id": "growth-review-date",
                "source": "Growth log vs Manual note",
                "message": (
                    f"The Growth log records {str(logged_review)[:10]}, while the "
                    f"manual note still cites {note_match.group(1)}."
                ),
            }
        )

    return issues


def build_consistency_trust(base_trust, issues):
    trust = deepcopy(base_trust or {})
    if not issues:
        return trust
    trust["level"] = "mixed"
    trust["label"] = "Mixed freshness"
    reasons = list(trust.get("reasons", []))
    count = len(issues)
    reasons.insert(
        0,
        f"{count} cross-layer contradiction{'s' if count != 1 else ''} "
        f"{'needs' if count == 1 else 'need'} review before acting.",
    )
    trust["reasons"] = reasons
    return trust


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


def build_models(usage, registry):
    """Model routing registry + real spend, for the Models tab. Registry is the
    recommendation layer (models, pricing, roles, harnesses/utilities); usage is
    where the money actually went (by model family and by tool)."""
    fam = {
        k: {"cost_usd": round(v.get("cost_usd", 0), 2), "sessions": v.get("sessions", 0)}
        for k, v in usage.get("byModelFamily", {}).items()
    }
    tool = {
        k: {"cost_usd": round(v.get("cost_usd", 0), 2), "sessions": v.get("sessions", 0)}
        for k, v in usage.get("byTool", {}).items()
    }
    return {
        "asOf": registry.get("asOf"),
        "source": registry.get("source"),
        "note": registry.get("note"),
        "harnesses": registry.get("harnesses", []),
        "models": registry.get("models", []),
        "matrix": registry.get("matrix", []),
        "crossVendorReview": registry.get("crossVendorReview"),
        "spendByFamily": fam,
        "spendByTool": tool,
        "spendWindowDays": usage.get("windowDays"),
        "spendGeneratedAt": usage.get("generatedAt"),
    }


def build_auto(status, usage, manual, registry):
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
                "taskSource",
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
        "eodHandoff": status.get("eodHandoff", {}),
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
        "models": build_models(usage, registry),
    }


def main():
    status = load(STATUS)
    usage = load(USAGE)
    manual = load(MANUAL)
    registry = load_optional(REGISTRY)

    auto = redact_paths(build_auto(status, usage, manual, registry))
    consistency_issues = find_consistency_issues(auto, manual) + find_stale_manual_blocks(manual)
    auto["consistencyIssues"] = consistency_issues
    auto["trust"] = build_consistency_trust(auto.get("trust"), consistency_issues)

    payload = {
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "sources": {
            "status": status.get("metadata", {}).get("lastSuccessfulRefresh"),
            "usage": usage.get("generatedAt"),
            "manual": manual.get("asOf"),
            # asOf is only when the file was last written. The oldest per-block
            # verification is the honest floor on how current the claims are.
            "manualOldestVerified": min(
                (str(v) for v in (manual.get("verified") or {}).values() if parse_iso_date(v)),
                default=None,
            ),
        },
        "auto": auto,
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
    SITE_DATA.mkdir(parents=True, exist_ok=True)
    for audience in SITE_AUDIENCES:
        site_payload = build_site_payload(payload, audience)
        destination = SITE_DATA / f"portfolio-hq-{audience}.json"
        destination.write_text(
            json.dumps(site_payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        if audience == "founder" and SITE_PROJECT_DATA.parent.is_dir():
            SITE_PROJECT_DATA.mkdir(parents=True, exist_ok=True)
            (SITE_PROJECT_DATA / "portfolio-hq-founder.json").write_text(
                json.dumps(site_payload, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
    print(f"- portfolio HQ: refreshed (dashboard/portfolio-hq.html, {len(payload['auto']['packets'])} open packets, "
          f"{payload['auto']['stranded']['actionableCount']} stranded, {len(payload['auto']['decisions'])} open decisions, "
          f"{len(SITE_AUDIENCES)} Site audiences)")


if __name__ == "__main__":
    main()
