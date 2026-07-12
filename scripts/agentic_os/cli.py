#!/usr/bin/env python3
from __future__ import annotations

import argparse
import contextlib
import http.server
import json
import os
import re
import shutil
import socket
import socketserver
import subprocess
import sys
import urllib.error
import urllib.request
import webbrowser
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
LOCAL_ENV_FILE = Path.home() / ".config" / "agentic-os.env"
DASHBOARD = ROOT / "dashboard"
STATUS_JSON = DASHBOARD / "status.json"
INDEX_HTML = DASHBOARD / "index.html"
PROJECT_STATUS_HTML = DASHBOARD / "project-status.html"
COMMAND_CENTER_HTML = DASHBOARD / "command-center.html"
ORCHESTRATION_HTML = DASHBOARD / "orchestration.html"
PORTFOLIO_HQ_PAGE = "portfolio-hq.html"


PROJECT_ALIASES = {
    "RunSmart iOS": ("runsmart-ios", "RunSmart iOS"),
    "ResumeBuilder iOS": ("resumebuilder-ios", "Resumely iOS"),
    "RunSmart Web": ("runsmart-web", "RunSmart Web"),
    "ResumeBuilder Web": ("resumebuilder-ai", "ResumeBuilder AI (Web)"),
    "Global Agentic OS": ("agentic-os", "Agentic OS"),
}


DEFAULT_AGENT_QUEUE = [
    {
        "role": "Release Manager",
        "task": "Handle an App Store review outcome without reopening completed submission work.",
        "whenToUse": "Use only after Apple approves, rejects, or requests information for either submitted app.",
        "evidence": "PROJECT-STATUS.md, dashboard/status.json, ResumeBuilder iOS tasks/session-log.md",
        "starter": "Act as Release Manager. Read dashboard/status.json and the target iOS repo tasks/progress.md plus tasks/session-log.md. If there is no new Apple review outcome, stop and report that monitoring is the only action. If Apple responded, create one focused response packet from the exact review message. Do not resubmit or change release scope without explicit approval.",
    },
    {
        "role": "CEO OS",
        "task": "Resolve the next portfolio decision and keep focus tight.",
        "whenToUse": "Use when there are competing next moves across RunSmart, Resumely, distribution, and backend support.",
        "evidence": "executive-os/EXECUTIVE-DASHBOARD.md, dashboard/status.json decisionBoard",
        "starter": "Act as CEO OS. Read dashboard/status.json and executive-os/EXECUTIVE-DASHBOARD.md. Pick the one highest-leverage decision, recommend an option, state cost of delay, and list the single next action.",
    },
    {
        "role": "Director / Orchestrator",
        "task": "Turn the current Action Board into one reviewable work packet.",
        "whenToUse": "Use when you want the next agent task delegated without losing source context.",
        "evidence": "dashboard/status.json priorityBoard and projectHealth",
        "starter": "Act as Director. Read dashboard/status.json, especially priorityBoard, projectHealth, and agentQueue. Create one decision-complete task packet for the recommended agent. Include goal, files to read, acceptance criteria, checks, and what not to touch.",
    },
    {
        "role": "QA",
        "task": "Verify dashboard or product readiness with evidence.",
        "whenToUse": "Use before calling a status, UI, or release task done.",
        "evidence": "GLOBAL-QA-RULES.md, dashboard runCenter checksRun",
        "starter": "Act as QA. Read GLOBAL-QA-RULES.md and dashboard/status.json. Build a focused QA checklist for the target change, run the available checks, and report pass/fail with evidence and missing validation.",
    },
]


PROJECT_PROMPT_ROLES = {
    "runsmart-ios": "iOS Release / Product Engineer",
    "resumebuilder-ios": "iOS Release Manager",
    "runsmart-web": "Backend Support Engineer",
    "resumebuilder-ai": "Backend Rollout Engineer",
    "agentic-os": "Agentic OS Operator",
}


# Local task files the parser reads, in preference order. tasks/progress.md is the
# preferred status source when present; the rest are used to derive or enrich status.
TASK_FILES = [
    "tasks/progress.md",
    "tasks/todo.md",
    "tasks/session-log.md",
    "tasks/MEMORY.md",
    "tasks/ERRORS.md",
    "tasks/lessons.md",
]

# GTM / distribution plans the parser reads so launch context is never lost from the
# dashboard. First match wins. Without these, a real GTM plan stays invisible no matter
# how fresh the run (the failure that hid runsmart-ios/.agent-os/distribution/gtm-plan.md).
GTM_RELPATHS = [
    ".agent-os/distribution/gtm-plan.md",
    "docs/distribution/gtm-plan.md",
    "distribution/gtm-plan.md",
    ".agent-os/distribution/gtm.md",
]

# Headings whose first content line is the product's one-line positioning.
POSITIONING_HEADINGS = [
    "## 1. One-Line Positioning",
    "## One-Line Positioning",
    "## Positioning",
    "## 1. Positioning",
]

# The two shippable apps, in best-next-action priority order. Used to rank the derived
# headline so the founder sees the most actionable app move first.
APP_IDS = ["resumebuilder-ios", "runsmart-ios"]
# All real product repos (apps + their web/back-end support repos).
PRODUCT_IDS = {"runsmart-ios", "resumebuilder-ios", "runsmart-web", "resumebuilder-ai"}
LAUNCHD_LABEL = "com.nadav.agentic-os-refresh"
LAUNCHD_PLIST = Path.home() / "Library/LaunchAgents/com.nadav.agentic-os-refresh.plist"
POSTHOG_BASE_URL = "https://us.posthog.com"
POSTHOG_KEY_ENV = "AGENTIC_OS_POSTHOG_API_KEY"
POSTHOG_TIMEOUT_SEC = 10
GROUND_TRUTH_OVERRIDES_ENV = "AGENTIC_OS_GROUND_TRUTH_OVERRIDES"
APP_STORE_STATE_ENV = "AGENTIC_OS_APPSTORE_STATES"
POSTHOG_PROJECTS = {
    "runsmart-ios": {"projectId": 171597, "name": "RunSmart"},
    "resumebuilder-ios": {"projectId": 270848, "name": "Resumely"},
}

# Directories where the founder's saved plans / specs / GTM live. Every saved plan must
# surface on the dashboard (the founder's rule: "any plan I asked to save must surface").
# Scanned per project; first-level *.md only (no deep recursion, to keep it fast and honest).
PLAN_DIRS = [
    ("docs/superpowers/plans", "plan"),
    ("docs/plans", "plan"),
    ("docs/superpowers/specs", "spec"),
    ("docs/specs", "spec"),
    (".agent-os/distribution", "gtm"),
    ("docs/distribution", "gtm"),
]
# How many recent plans to surface per project on the dashboard (GTM plans are always kept).
PLANS_PER_PROJECT = 6

# Maps a lowercased `Key: Value` label from tasks/progress.md to a parsed field name.
PROGRESS_KEY_MAP = {
    "status": "status",
    "current phase": "currentPhase",
    "active story": "activeStory",
    "last completed story": "lastCompletedStory",
    "next recommended story": "nextRecommendedStory",
    "blockers": "blockers",
    "risks": "risks",
    "last validation": "lastValidation",
    "last updated": "lastUpdated",
    "latest qa report": "qaNeeded",
    "estimated completion": "estimatedCompletion",
}

# Tokens that mean "no real value" when they are the entire field value.
EMPTY_TOKENS = {"", "-", "—", "–", "none", "n/a", "na", "tbd", "pending", "todo"}

# Validation evidence: positive signals must appear and not be negated.
VALIDATION_POSITIVE = re.compile(
    r"(\bpass(ed|es|ing)?\b|\bsucceeded\b|\bsuccess\b|\bgreen\b|\bverified\b|"
    r"\bbuild succeeded\b|tests? (?:passed|green)|✓|✅)",
    re.IGNORECASE,
)
VALIDATION_NEGATIVE = re.compile(
    r"(not (?:yet )?(?:validated|run|done|tested|verified)|no validation|"
    r"\buntested\b|\bunverified\b|\bunclear\b|validation pending|pending verify)",
    re.IGNORECASE,
)


@dataclass
class ProjectEvidence:
    project_id: str
    name: str
    path: Path
    exists: bool
    branch: str
    dirty: bool
    dirty_count: int
    extra_worktrees: int
    last_commit: str
    source_files: list[str]
    task_parse: dict[str, Any] = field(default_factory=dict)
    gtm: dict[str, Any] = field(default_factory=dict)
    plans: list[dict[str, Any]] = field(default_factory=list)
    stranded: dict[str, Any] = field(default_factory=dict)


def load_local_env() -> None:
    """Load ~/.config/agentic-os.env for manual CLI runs (launchd uses daily-refresh.sh)."""
    if not LOCAL_ENV_FILE.is_file():
        return
    for raw_line in LOCAL_ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].strip()
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip()
        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]
        if key and key not in os.environ:
            os.environ[key] = value


def run(cmd: list[str], cwd: Path = ROOT, timeout: int = 12) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            cmd,
            cwd=str(cwd),
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        return subprocess.CompletedProcess(
            cmd,
            124,
            stdout=exc.stdout or "",
            stderr=f"Timed out after {timeout} seconds",
        )


def command_available(name: str) -> bool:
    return shutil.which(name) is not None


def parse_launchctl_job(text: str) -> dict[str, Any]:
    parsed: dict[str, Any] = {
        "loaded": bool(text.strip()),
        "state": None,
        "lastExitCode": None,
        "runs": None,
    }
    state = re.search(r"state = ([^\n]+)", text)
    if state:
        parsed["state"] = state.group(1).strip()
    exit_code = re.search(r"last exit code = (-?\d+)", text)
    if exit_code:
        parsed["lastExitCode"] = int(exit_code.group(1))
    runs = re.search(r"runs = (\d+)", text)
    if runs:
        parsed["runs"] = int(runs.group(1))
    return parsed


def launchd_job_status(label: str = LAUNCHD_LABEL) -> dict[str, Any]:
    domain = f"gui/{os.getuid()}/{label}"
    proc = run(["launchctl", "print", domain], timeout=10)
    if proc.returncode != 0:
        return {
            "loaded": False,
            "state": "missing",
            "lastExitCode": None,
            "runs": 0,
            "raw": proc.stderr.strip() or proc.stdout.strip(),
        }
    status = parse_launchctl_job(proc.stdout)
    status["raw"] = proc.stdout
    return status


def check_hook_health() -> list[str]:
    """Non-blocking health check for global Stop hooks and the launchd refresh job.

    Returns human-readable issue strings; empty list means healthy. Never raises -
    a missing or malformed settings.json is itself a reportable issue, not a crash.
    """
    issues: list[str] = []
    settings_path = Path.home() / ".claude" / "settings.json"
    if not settings_path.exists():
        issues.append("~/.claude/settings.json not found - Stop hooks are not configured")
    else:
        try:
            settings = json.loads(settings_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            issues.append("~/.claude/settings.json is not valid JSON - hooks cannot be verified")
        else:
            stop_groups = settings.get("hooks", {}).get("Stop", [])
            commands = [
                h.get("command", "")
                for group in stop_groups
                for h in group.get("hooks", [])
            ]
            if not any("update-progress.sh" in c for c in commands):
                issues.append("Stop hook update-progress.sh is missing from settings.json")
            if not any("intent-log-check.sh" in c for c in commands):
                issues.append("Stop hook intent-log-check.sh is missing from settings.json")

    launchd = launchd_job_status(LAUNCHD_LABEL)
    last_exit = launchd.get("lastExitCode")
    if last_exit not in (None, 0):
        issues.append(f"launchd job {LAUNCHD_LABEL} last exited with status {last_exit}")

    return issues


def parse_time_label(value: str | None) -> datetime | None:
    if not value:
        return None
    match = re.search(r"(\d{4}-\d{2}-\d{2})[ T](\d{2}:\d{2})", value)
    if not match:
        return None
    try:
        return datetime.strptime(f"{match.group(1)} {match.group(2)}", "%Y-%m-%d %H:%M")
    except ValueError:
        return None


def parse_json_env(name: str) -> dict[str, Any]:
    raw = os.environ.get(name, "").strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


def fetch_posthog_live_users(project_id: int, api_key: str) -> dict[str, Any]:
    payload = {
        "query": {
            "kind": "HogQLQuery",
            "query": (
                "SELECT uniq(person_id) AS live_users_7d "
                "FROM events WHERE timestamp >= now() - INTERVAL 7 DAY"
            ),
        }
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{POSTHOG_BASE_URL}/api/projects/{project_id}/query/",
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=POSTHOG_TIMEOUT_SEC) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        return {"available": False, "error": str(exc)}

    users = None
    results = body.get("results")
    if isinstance(results, list) and results:
        first = results[0]
        if isinstance(first, dict):
            users = first.get("live_users_7d")
        elif isinstance(first, list) and first:
            users = first[0]
    if users is None and isinstance(body.get("result"), list) and body["result"]:
        users = body["result"][0]
    try:
        users_int = int(users) if users is not None else 0
    except (TypeError, ValueError):
        users_int = 0
    return {"available": True, "liveUsers7d": users_int}


def today_idt() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def now_label() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


# Freshness thresholds (days). Aligned with metadata.freshnessRule in status.json.
FRESHNESS_FRESH_DAYS = 2
FRESHNESS_REVIEW_DAYS = 7
CONFIDENCE_DOWNGRADE = {"High": "Medium", "Medium": "Low", "Low": "Unknown", "Unknown": "Unknown"}


def parse_date(value: Any) -> datetime | None:
    if not value:
        return None
    match = re.search(r"(\d{4})-(\d{2})-(\d{2})", str(value))
    if not match:
        return None
    try:
        return datetime(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    except ValueError:
        return None


def compute_freshness(dates: list[datetime | None]) -> tuple[str, str | None]:
    """Freshness label from the newest available date. Day granularity is enough."""
    valid = [d for d in dates if d is not None]
    if not valid:
        return "Unknown", None
    freshest = max(valid)
    days = (datetime.now() - freshest).days
    if days <= FRESHNESS_FRESH_DAYS:
        label = "Fresh"
    elif days <= FRESHNESS_REVIEW_DAYS:
        label = "Needs Review"
    else:
        label = "Stale"
    return label, freshest.strftime("%Y-%m-%d")


def latest_date_in(text: str | None) -> datetime | None:
    """The most recent YYYY-MM-DD found in free text, or None."""
    dates = [parse_date(token) for token in re.findall(r"\d{4}-\d{2}-\d{2}", text or "")]
    valid = [d for d in dates if d is not None]
    return max(valid) if valid else None


# Build-result phrasing in validation text.
BUILD_OK = re.compile(r"build succeeded|xcodebuild build[^.]*succeed|build passed|compil\w+[^.]*(?:passed|succeeded)", re.IGNORECASE)
BUILD_FAIL = re.compile(r"build failed|compile error|compilation failed", re.IGNORECASE)
# Test-count phrasing, e.g. "53 XCTest", "5 Swift Testing", "12 tests".
TEST_COUNT = re.compile(r"(\d+)\s+(XCTest|Swift Testing|tests?|specs?|unit tests?)", re.IGNORECASE)


def extract_evidence(parse: dict[str, Any]) -> dict[str, Any]:
    """Pull structured proof out of the free-text validation line.

    Captures test counts, a build result, and any docs/ QA links, plus the most recent
    date the evidence references (falling back to Last Updated). Story 3.1.
    """
    text = parse.get("lastValidation") or ""
    evidence: dict[str, Any] = {"tests": [], "buildStatus": None, "qaDocs": [], "evidenceDate": None}

    for match in TEST_COUNT.finditer(text):
        evidence["tests"].append(f"{match.group(1)} {match.group(2)}")
    evidence["tests"] = list(dict.fromkeys(evidence["tests"]))

    if BUILD_OK.search(text):
        evidence["buildStatus"] = "succeeded"
    elif BUILD_FAIL.search(text):
        evidence["buildStatus"] = "failed"

    qa_docs = re.findall(r"docs/[\w./-]+", text)
    qa_field = parse.get("qaNeeded")
    if qa_field and str(qa_field).startswith("docs/"):
        qa_docs.append(qa_field)
    evidence["qaDocs"] = list(dict.fromkeys(qa_docs))

    dated = latest_date_in(text)
    evidence["evidenceDate"] = dated.strftime("%Y-%m-%d") if dated else parse.get("lastUpdated")
    return evidence


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def remap_ci_path(path: Path) -> Path:
    """Remap a local Mac path to its CI clone location.

    PROJECT-PATHS.md holds Nadav's local absolute paths. In CI (e.g. the cloud
    morning-refresh workflow) sibling repos are cloned under a different root, so
    AGENTIC_OS_PATH_ROOT_MAP="<local-prefix>=><ci-prefix>" swaps the prefix before
    the path is read. No-op when the env var is unset (local/launchd runs).
    """
    mapping = os.environ.get("AGENTIC_OS_PATH_ROOT_MAP")
    if not mapping or "=>" not in mapping:
        return path
    local_prefix, ci_prefix = mapping.split("=>", 1)
    path_str = str(path)
    if path_str.startswith(local_prefix):
        return Path(ci_prefix + path_str[len(local_prefix):])
    return path


def parse_project_paths() -> list[tuple[str, Path]]:
    text = (ROOT / "PROJECT-PATHS.md").read_text(encoding="utf-8")
    rows: list[tuple[str, Path]] = []
    for line in text.splitlines():
        if not line.startswith("| ") or "`/" not in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        name = re.sub(r"`", "", cells[0]).strip()
        path_match = re.search(r"`([^`]+)`", cells[1])
        if name in PROJECT_ALIASES and path_match:
            # This repo's own row always resolves to ROOT (this checkout), never
            # remapped -- there's no sibling clone of Agentic OS itself in CI.
            resolved = ROOT if name == "Global Agentic OS" else remap_ci_path(Path(path_match.group(1)))
            rows.append((name, resolved))
    if "Global Agentic OS" not in {name for name, _ in rows}:
        rows.append(("Global Agentic OS", ROOT))
    return rows


def record_if_exists(path: Path, root: Path, sources: list[str]) -> str:
    if not path.exists():
        return ""
    try:
        sources.append(str(path.relative_to(root)))
    except ValueError:
        sources.append(str(path))
    return path.read_text(encoding="utf-8", errors="replace")


def empty_task_parse() -> dict[str, Any]:
    return {
        "status": None,
        "currentPhase": None,
        "activeStory": None,
        "lastCompletedStory": None,
        "nextRecommendedStory": None,
        "blockers": [],
        "risks": [],
        "lastValidation": None,
        "lastUpdated": None,
        "qaNeeded": None,
        "estimatedCompletion": None,
        "decisionsNeeded": [],
        "openQuestions": [],
        "evidence": {"tests": [], "buildStatus": None, "qaDocs": [], "evidenceDate": None},
        "preferredSource": "none",
        "sourcesUsed": [],
        "missing": [],
        "sourceConfidence": "Unknown",
        "notes": "",
    }


def clean_value(value: Any) -> str | None:
    if value is None:
        return None
    text = re.sub(r"\s+", " ", str(value)).strip().rstrip(".").strip()
    if text.lower() in EMPTY_TOKENS:
        return None
    return text or None


def split_list(value: Any) -> list[str]:
    cleaned = clean_value(value)
    if not cleaned:
        return []
    parts = re.split(r"\s*;\s*", cleaned)
    return [p.strip() for p in parts if p.strip() and p.strip().lower() not in EMPTY_TOKENS]


def has_validation_evidence(text: str | None) -> bool:
    if not text:
        return False
    if VALIDATION_NEGATIVE.search(text):
        return False
    return bool(VALIDATION_POSITIVE.search(text))


def keyed_fields(text: str) -> dict[str, str]:
    """Parse leading `Key: Value` metadata lines (tasks/progress.md style)."""
    fields: dict[str, str] = {}
    for line in text.splitlines():
        if ":" not in line or line.lstrip().startswith(("#", "|", "-", ">", "*")):
            continue
        key, _, value = line.partition(":")
        normalized = key.strip().lower()
        if normalized in PROGRESS_KEY_MAP and normalized not in fields:
            fields[normalized] = value.strip()
    return fields


def section_value(text: str, heading: str) -> str | None:
    """Return the first non-empty, non-heading line after a heading line."""
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.strip() == heading:
            for follow in lines[index + 1:]:
                stripped = follow.strip()
                if not stripped:
                    continue
                if stripped.startswith("#"):
                    return None
                return clean_value(stripped)
    return None


def latest_session_entry(text: str) -> tuple[str | None, str | None]:
    """Find the most recent dated session entry (`## YYYY-MM-DD - title`)."""
    pattern = re.compile(r"^#{2,3}\s*(\d{4}-\d{2}-\d{2})(?:\s*[-—:]\s*(.*))?\s*$")
    for line in text.splitlines():
        match = pattern.match(line)
        if match:
            return match.group(1), clean_value(match.group(2) or "")
    return None, None


def latest_validation_block(text: str) -> str | None:
    """Join bullet lines under the first `### Validation` heading in a session log."""
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if re.match(r"^#{2,4}\s*validation\b", line.strip(), re.IGNORECASE):
            collected: list[str] = []
            for follow in lines[index + 1:]:
                stripped = follow.strip()
                if not stripped:
                    if collected:
                        break
                    continue
                if stripped.startswith("#"):
                    break
                collected.append(stripped.lstrip("-* ").strip())
            joined = "; ".join(collected).strip()
            return clean_value(joined)
    return None


def todo_validation_line(text: str) -> str | None:
    for line in text.splitlines():
        if re.search(r"\bPASS\b", line) and re.search(r"\d{4}-\d{2}-\d{2}", line):
            return clean_value(re.sub(r"[*\[\]]|- \[.\]", " ", line))
    return None


def scan_blockers(contents: dict[str, str]) -> list[str]:
    found: list[str] = []
    for text in contents.values():
        for line in text.splitlines():
            match = re.match(r"^\s*Blockers?:\s*(.+)$", line, re.IGNORECASE)
            if match:
                found.extend(split_list(match.group(1)))
    # de-dupe, keep order
    return list(dict.fromkeys(found))[:5]


def section_bullets(text: str, heading_regex: str) -> list[str]:
    """Bullet items listed under a matching `## Heading`, until the next heading/blank gap."""
    out: list[str] = []
    capturing = False
    for line in text.splitlines():
        stripped = line.strip()
        if re.match(heading_regex, stripped, re.IGNORECASE):
            capturing = True
            continue
        if capturing:
            if stripped.startswith("#"):
                break
            if stripped.startswith(("-", "*")):
                item = stripped.lstrip("-* ").strip()
                if item:
                    out.append(item)
    return out


def extract_open_questions(contents: dict[str, str]) -> list[str]:
    # Section-only: a loose "any line mentioning open questions" scan produced false positives
    # (e.g. "Checked the historical open questions ..."). The `## Open Questions` section is the
    # reliable convention; see STATUS-SCHEMA.md.
    found: list[str] = []
    for text in contents.values():
        for item in section_bullets(text, r"^#{2,4}\s*open questions?\b"):
            if not re.search(r"resolved|answered|closed", item, re.IGNORECASE):
                cleaned = clean_value(item)
                if cleaned:
                    found.append(cleaned)
    return list(dict.fromkeys(found))[:5]


def extract_open_decisions(contents: dict[str, str]) -> list[str]:
    found: list[str] = []
    for text in contents.values():
        for line in text.splitlines():
            if line.lstrip().startswith("#"):
                continue
            if re.search(r"needs? decision|decision needed|open decision|undecided", line, re.IGNORECASE):
                cleaned = clean_value(line.lstrip("-*# ").strip())
                if cleaned:
                    found.append(cleaned)
        for item in section_bullets(text, r"^#{2,4}\s*(?:open decisions?|decisions? (?:needed|to make|pending|open))\b"):
            cleaned = clean_value(item)
            if cleaned:
                found.append(cleaned)
    return list(dict.fromkeys(found))[:5]


def derive_status(result: dict[str, Any], contents: dict[str, str]) -> None:
    """Derive status when tasks/progress.md is absent (todo + session-log + MEMORY)."""
    todo = contents.get("tasks/todo.md", "")
    session = contents.get("tasks/session-log.md", "")

    # The most recent dated session entry is the freshest signal for the current phase.
    date, title = latest_session_entry(session)
    if date:
        result["lastUpdated"] = date
    if title:
        result["currentPhase"] = title

    # The todo "Current Task" is the active or last-completed story.
    current_task = section_value(todo, "## Current Task")
    if current_task:
        if re.search(r"\b(complete|completed|done|shipped)\b", current_task, re.IGNORECASE):
            result["lastCompletedStory"] = current_task
        else:
            result["activeStory"] = current_task
        result["currentPhase"] = result["currentPhase"] or current_task

    if not result["activeStory"] and title:
        result["activeStory"] = title

    validation = latest_validation_block(session) or todo_validation_line(todo)
    if validation:
        result["lastValidation"] = validation

    next_action = section_value(session, "### Next Recommended Action") or section_value(
        todo, "## Next Recommended Story"
    )
    if next_action:
        result["nextRecommendedStory"] = next_action

    result["blockers"] = scan_blockers(contents)


def compute_confidence(result: dict[str, Any]) -> str:
    if not result["sourcesUsed"]:
        return "Unknown"
    if has_validation_evidence(result.get("lastValidation")):
        return "High"
    return "Medium"


def parse_task_files(path: Path) -> dict[str, Any]:
    """Read local task files and extract structured, source-backed status.

    Preference order: tasks/progress.md (structured `Key: Value`) when present,
    otherwise derive from tasks/todo.md + latest tasks/session-log.md + tasks/MEMORY.md.
    When no task files exist, confidence stays Unknown and `missing` explains the gap.
    """
    result = empty_task_parse()

    if not path.exists():
        result["missing"] = list(TASK_FILES)
        result["notes"] = "Project path not found on disk; no local task files could be read."
        return result

    contents: dict[str, str] = {}
    for rel in TASK_FILES:
        file_path = path / rel
        if file_path.exists():
            contents[rel] = file_path.read_text(encoding="utf-8", errors="replace")
            result["sourcesUsed"].append(rel)
        else:
            result["missing"].append(rel)

    if not contents:
        result["notes"] = (
            "No local task files found (progress/todo/session-log/MEMORY/ERRORS/lessons). "
            "Status falls back to existing dashboard narrative."
        )
        return result

    progress = contents.get("tasks/progress.md")
    if progress:
        result["preferredSource"] = "tasks/progress.md"
        for key, field_name in keyed_fields(progress).items():
            target = PROGRESS_KEY_MAP[key]
            if target in ("blockers", "risks"):
                result[target] = split_list(field_name)
            else:
                result[target] = clean_value(field_name)
    else:
        result["preferredSource"] = "derived"
        result["notes"] = (
            "Derived from tasks/todo.md, latest tasks/session-log.md, and tasks/MEMORY.md "
            "because tasks/progress.md is absent."
        )
        derive_status(result, contents)

    result["decisionsNeeded"] = extract_open_decisions(contents)
    result["openQuestions"] = extract_open_questions(contents)
    result["evidence"] = extract_evidence(result)
    result["sourceConfidence"] = compute_confidence(result)
    return result


def parse_gtm(path: Path) -> dict[str, Any]:
    """Read a project's GTM / distribution plan so launch context surfaces on the dashboard.

    Returns positioning, declared status, the relative path, and the freshest date found.
    A missing plan yields exists=False rather than an error, so projects without GTM are fine.
    """
    info: dict[str, Any] = {
        "exists": False,
        "path": None,
        "positioning": None,
        "status": None,
        "lastUpdated": None,
    }
    if not path.exists():
        return info
    for rel in GTM_RELPATHS:
        gtm_file = path / rel
        if not gtm_file.exists():
            continue
        text = gtm_file.read_text(encoding="utf-8", errors="replace")
        info["exists"] = True
        info["path"] = rel
        for heading in POSITIONING_HEADINGS:
            value = section_value(text, heading)
            if value:
                info["positioning"] = value
                break
        status_match = re.search(r"^status:\s*(.+)$", text, re.IGNORECASE | re.MULTILINE)
        if status_match:
            info["status"] = clean_value(status_match.group(1))
        dated = latest_date_in(text)
        info["lastUpdated"] = dated.strftime("%Y-%m-%d") if dated else None
        break
    return info


def _plan_title(text: str, fallback: str) -> str:
    """First markdown heading is the plan title; else a humanized filename."""
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return clean_value(stripped[2:]) or fallback
        if stripped.startswith("## "):
            return clean_value(stripped[3:]) or fallback
    return fallback


def collect_plans(path: Path) -> list[dict[str, Any]]:
    """Every saved plan/spec/GTM in a repo, newest first.

    The founder's rule: any plan they asked to save must surface on the dashboard. This scans
    the known plan directories so a saved plan can never silently disappear. README index files
    are skipped as noise; GTM/distribution plans are flagged so they are always kept on display.
    """
    plans: list[dict[str, Any]] = []
    if not path.exists():
        return plans
    seen: set[str] = set()
    for rel_dir, kind in PLAN_DIRS:
        directory = path / rel_dir
        if not directory.is_dir():
            continue
        for plan_file in sorted(directory.glob("*.md")):
            name_lower = plan_file.name.lower()
            if name_lower == "readme.md":
                continue
            # Distribution folders hold many reference docs (audience, channels, competitors...);
            # only the actual plans there ("*plan*", e.g. gtm-plan.md, weekly-plan.md) are saved plans.
            if kind == "gtm" and "plan" not in name_lower:
                continue
            rel = str(plan_file.relative_to(path))
            if rel in seen:
                continue
            seen.add(rel)
            # Within a distribution folder, only a *gtm* file is the GTM plan; other *plan* files
            # (e.g. weekly-plan.md) are ordinary plans.
            effective_kind = kind
            if kind == "gtm" and "gtm" not in name_lower:
                effective_kind = "plan"
            text = plan_file.read_text(encoding="utf-8", errors="replace")
            dated = latest_date_in(plan_file.name) or latest_date_in(text)
            status_match = re.search(r"^status:\s*(.+)$", text, re.IGNORECASE | re.MULTILINE)
            plans.append(
                {
                    "title": _plan_title(text, plan_file.stem.replace("-", " ").replace("_", " ")),
                    "path": rel,
                    "date": dated.strftime("%Y-%m-%d") if dated else None,
                    "status": clean_value(status_match.group(1)) if status_match else None,
                    "kind": effective_kind,
                }
            )
    plans.sort(key=lambda p: (p["date"] or "0000-00-00", p["path"]), reverse=True)
    return plans


# Every `./agentic-os` command and a plain-language description of what it does.
OS_COMMANDS = [
    ("./agentic-os morning", "The one command. Refreshes from every repo, surfaces all OS layers and plans, rebuilds the brief, updates the dashboard, verifies, and opens it on localhost."),
    ("./agentic-os eod", "Evening bookend. Drafts today's End-of-Day close in the Builder OS daily note from today's git commits + Claude Code sessions (Cursor stays a manual line)."),
    ("./agentic-os refresh", "Rebuilds the dashboard data from local repos. No server."),
    ("./agentic-os serve", "Opens the current dashboard on localhost. No refresh."),
    ("./agentic-os verify", "Checks the dashboard data, links, and tests all line up."),
    ("./agentic-os test", "Runs the parser unit tests."),
]


def _doc_summary(path: Path) -> tuple[str, str]:
    """Title (first H1) and a one-line plain-language purpose (first real sentence) of a doc."""
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    title = path.stem.replace("-", " ").replace("_", " ")
    purpose = ""
    for index, line in enumerate(lines):
        if line.strip().startswith("# "):
            title = clean_value(line.strip()[2:]) or title
            for follow in lines[index + 1:]:
                stripped = follow.strip()
                if not stripped or stripped.startswith(("#", "-", "*", "|", ">", "```", "---")):
                    continue
                purpose = stripped
                break
            break
    if not purpose:
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.startswith(("#", "-", "*", "|", ">", "```", "---")):
                purpose = stripped
                break
    purpose = re.sub(r"\s+", " ", purpose).strip()
    if len(purpose) > 160:
        purpose = purpose[:157].rstrip() + "..."
    return title, purpose


def _metadata_value(text: str, label: str) -> str | None:
    """Read a top-level Markdown metadata line such as `- Status: active`."""
    match = re.search(
        rf"^\s*[-*]?\s*{re.escape(label)}:\s*(.+?)\s*$",
        text,
        re.IGNORECASE | re.MULTILINE,
    )
    return clean_value(match.group(1)) if match else None


def _frontmatter_value(text: str, label: str) -> str | None:
    """Read a simple YAML frontmatter scalar, preserving body metadata as fallback."""
    if not text.startswith("---"):
        return None
    match = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.DOTALL)
    if not match:
        return None
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep and key.strip().lower() == label.lower():
            return clean_value(value.strip().strip("\"'"))
    return None


def build_os_registry(root: Path) -> dict[str, Any]:
    """Auto-discover the Agentic OS from the repo itself, in two plain groups.

    - leadership: the Executive OS (CEO/COO/CFO/Analysis/Risk + Distribution). These review
      status and make decisions. The matching agent file is just how each is run, so it is not
      listed separately (that double-listing was confusing).
    - skillAgents: the builders that execute work packets (architect, QA, release, etc.).
    - plugins: private workflow bundles that package reusable skills for ChatGPT and Codex.
    Work packets, outcome loops, context checkpoints, and commands are returned too.
    Anything created under these folders surfaces on the next run — nothing can silently vanish.
    """
    registry: dict[str, Any] = {
        "commands": [{"name": name, "purpose": purpose} for name, purpose in OS_COMMANDS],
        "leadership": [],
        "workPackets": [],
        "outcomeLoops": [],
        "contextCheckpoints": [],
        "skillAgents": [],
        "plugins": [],
        "sideProjects": [],
        "researchTopics": [],
    }
    exec_dir = root / "executive-os"
    if exec_dir.is_dir():
        for sub_os in sorted(exec_dir.glob("*-OS.md")):
            title, purpose = _doc_summary(sub_os)
            registry["leadership"].append({"name": title, "purpose": purpose, "path": str(sub_os.relative_to(root))})
        packets_dir = exec_dir / "work-packets"
        if packets_dir.is_dir():
            for packet in sorted(packets_dir.glob("*.md")):
                text = packet.read_text(encoding="utf-8", errors="replace")
                title, _ = _doc_summary(packet)
                status_match = re.search(r"Status:\s*([A-Za-z ]+)", text)
                project_match = re.search(r"##\s*Project\s*\n+\s*(.+)", text)
                path_match = re.search(r"Path:\s*`?([^`\n]+)`?", text)
                project_raw = clean_value(project_match.group(1)) if project_match else None
                repo_path = clean_value(path_match.group(1)) if path_match else None
                # Map the project line to a short repo id so the dashboard can label it clearly.
                repo_id = "research"
                if repo_path:
                    lower = repo_path.lower()
                    if "runsmart" in lower and ("ios" in lower or "app" in lower):
                        repo_id = "runsmart-ios"
                    elif "runsmart" in lower:
                        repo_id = "runsmart-web"
                    elif "new-resumebuilder-ai" in lower or "resumebuilder-ai" in lower:
                        repo_id = "resumebuilder-ai"
                    elif "resumebuilder" in lower or "resumely" in lower:
                        repo_id = "resumebuilder-ios"
                    elif "agentic" in lower:
                        repo_id = "agentic-os"
                goal = section_value(text, "## Goal")
                packet_source = _metadata_value(text, "Source")
                workflow_pattern = _metadata_value(text, "Workflow pattern") or "normal"
                input_trust = _metadata_value(text, "Input trust") or "trusted"
                outcome_loop = _metadata_value(text, "Outcome loop")
                loop = _metadata_value(text, "Loop")
                signal = _metadata_value(text, "Signal")
                memory_update = _metadata_value(text, "Memory update")
                success_signal = _metadata_value(text, "Success signal")
                # Build a copy-ready prompt: repo instruction + full packet body.
                # This IS the prompt the founder pastes into Claude Code for that repo.
                if repo_path:
                    prompt_header = (
                        f"Repo: {repo_path}\n"
                        f"\n"
                        f"How to start:\n"
                        f"  Claude Code → cd \"{repo_path}\" && claude\n"
                        f"  Cursor      → open \"{repo_path}\" in Cursor, paste this in the AI panel\n"
                        f"  Codex       → create a task, paste this as the full task context\n"
                        f"\n"
                        f"--- WORK PACKET ---\n"
                    )
                else:
                    prompt_header = (
                        "No specific repo — run this in the Agentic OS directory.\n"
                        "  Claude Code → cd \"Agentic OS\" && claude\n"
                        "  Cursor      → open Agentic OS folder, paste in AI panel\n"
                        "  Codex       → paste as task context\n\n"
                        "--- WORK PACKET ---\n"
                    )
                packet_status = (
                    _frontmatter_value(text, "status")
                    or (clean_value(status_match.group(1)) if status_match else None)
                    or "Unknown"
                )
                registry["workPackets"].append(
                    {
                        "title": title,
                        "status": packet_status,
                        "project": project_raw,
                        "repoId": repo_id,
                        "repoPath": repo_path,
                        "goal": goal,
                        "source": packet_source,
                        "workflowPattern": workflow_pattern,
                        "inputTrust": input_trust,
                        "outcomeLoop": outcome_loop,
                        "loop": loop,
                        "signal": signal,
                        "memoryUpdate": memory_update,
                        "successSignal": success_signal,
                        "path": str(packet.relative_to(root)),
                        "copyPrompt": prompt_header + text if packet_status.lower().startswith("active") else None,
                    }
                )
        loops_dir = exec_dir / "loops"
        if loops_dir.is_dir():
            for loop_file in sorted(loops_dir.glob("*.md")):
                if loop_file.name.lower() == "readme.md":
                    continue
                text = loop_file.read_text(encoding="utf-8", errors="replace")
                title, _ = _doc_summary(loop_file)
                registry["outcomeLoops"].append(
                    {
                        "title": title,
                        "status": _metadata_value(text, "Status") or "unknown",
                        "owner": _metadata_value(text, "Owner"),
                        "outcome": _metadata_value(text, "Outcome"),
                        "source": _metadata_value(text, "Source"),
                        "linkedPacket": _metadata_value(text, "Linked packet"),
                        "leadingSignal": _metadata_value(text, "Leading signal"),
                        "resultMetric": _metadata_value(text, "Result metric"),
                        "currentMilestone": _metadata_value(text, "Current milestone"),
                        "constraint": _metadata_value(text, "Constraint"),
                        "lastReviewed": _metadata_value(text, "Last reviewed"),
                        "evidenceSource": _metadata_value(text, "Evidence source"),
                        "memoryDestination": _metadata_value(text, "Memory destination"),
                        "closeCondition": _metadata_value(text, "Close condition"),
                        "path": str(loop_file.relative_to(root)),
                    }
                )
        research_dir = exec_dir / "research"
        if research_dir.is_dir():
            for research_file in sorted(research_dir.glob("*.md"), reverse=True):
                if research_file.name.lower() == "readme.md":
                    continue
                title, purpose = _doc_summary(research_file)
                registry["researchTopics"].append(
                    {
                        "name": title,
                        "purpose": purpose,
                        "path": str(research_file.relative_to(root)),
                    }
                )
    checkpoint_dirs = [root / "brainstorms", exec_dir / "context"]
    for context_dir in checkpoint_dirs:
        if not context_dir.is_dir():
            continue
        for checkpoint_file in sorted(context_dir.glob("*.md"), reverse=True):
            if checkpoint_file.name.lower() == "readme.md":
                continue
            text = checkpoint_file.read_text(encoding="utf-8", errors="replace")
            title, _ = _doc_summary(checkpoint_file)
            registry["contextCheckpoints"].append(
                {
                    "title": title,
                    "status": _metadata_value(text, "Status") or "unknown",
                    "topic": _metadata_value(text, "Topic"),
                    "purpose": _metadata_value(text, "Purpose"),
                    "created": _metadata_value(text, "Created"),
                    "lastUpdated": _metadata_value(text, "Last updated"),
                    "path": str(checkpoint_file.relative_to(root)),
                }
            )
    # Distribution OS is part of the executive layer (growth/launch), surfaced as leadership.
    dist_readme = root / "distribution-os" / "README.md"
    if dist_readme.exists():
        _, purpose = _doc_summary(dist_readme)
        registry["leadership"].append({"name": "Distribution OS", "purpose": purpose or "Cross-product launch and growth.", "path": "distribution-os/README.md"})
    skills_dir = root / "SKILLS"
    if skills_dir.is_dir():
        for skill in sorted(skills_dir.glob("*.md")):
            title, purpose = _doc_summary(skill)
            registry["skillAgents"].append({"name": title, "purpose": purpose, "path": str(skill.relative_to(root))})
    plugins_dir = root / "plugins"
    if plugins_dir.is_dir():
        for manifest in sorted(plugins_dir.glob("*/.codex-plugin/plugin.json")):
            try:
                plugin = json.loads(manifest.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            plugin_root = manifest.parents[1]
            registry["plugins"].append(
                {
                    "name": plugin.get("name") or plugin_root.name,
                    "purpose": plugin.get("description") or "Private workflow plugin.",
                    "version": plugin.get("version"),
                    "skillCount": len(list((plugin_root / "skills").glob("*/SKILL.md"))),
                    "path": str(manifest.relative_to(root)),
                }
            )
    for candidate in sorted(root.iterdir()) if root.is_dir() else []:
        if not candidate.is_dir() or candidate.name.startswith("."):
            continue
        readme = candidate / "README.md"
        skill = candidate / "SKILL.md"
        if readme.exists() and skill.exists():
            title, purpose = _doc_summary(readme)
            registry["sideProjects"].append(
                {
                    "name": title,
                    "purpose": purpose,
                    "path": str(readme.relative_to(root)),
                }
            )
    return registry


def parse_decisions(root: Path) -> list[dict[str, Any]]:
    """Read the executive decisions log into structured rows (newest decisions first).

    Source: executive-os/EXECUTIVE-DECISIONS.md markdown table. Open decisions are what the
    founder still has to call; Decided ones should flow into work packets. This makes the
    decisions real (parsed) instead of a hand-kept dashboard list.
    """
    decisions: list[dict[str, Any]] = []
    path = root / "executive-os" / "EXECUTIVE-DECISIONS.md"
    if not path.exists():
        return decisions
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip().startswith("| EXD-"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 12:
            continue
        status_raw = cells[11]
        state = status_raw.split("-")[0].split("—")[0].strip() or "Unknown"
        decisions.append(
            {
                "id": cells[0],
                "date": cells[1],
                "area": cells[2],
                "decision": cells[3],
                "recommendation": cells[5],
                "owner": cells[9],
                "review": cells[10],
                "status": state,
            }
        )
    decisions.sort(key=lambda d: d["id"], reverse=True)
    return decisions


def build_executive_loop(decisions: list[dict[str, Any]], registry: dict[str, Any], root: Path) -> dict[str, Any]:
    """Assemble the operating loop the founder asked to see, end to end.

    morning -> project status -> executive review -> decisions -> work packets -> brainstorm.
    Links each work packet to the decision it came from (via 'Related decision: EXD-xxx').
    """
    packets = registry.get("workPackets", [])
    active_packets = [packet for packet in packets if _packet_is_active(packet)]
    # Link packets to decisions by scanning each packet file for "Related decision: EXD-xxx".
    for packet in packets:
        related = None
        packet_path = root / packet.get("path", "")
        if packet_path.exists():
            match = re.search(r"Related decision:\s*(EXD-\d+)", packet_path.read_text(encoding="utf-8", errors="replace"))
            related = match.group(1) if match else None
        packet["decision"] = related
    open_decisions = [d for d in decisions if d["status"].lower().startswith("open")]
    # Flag decisions whose review date has passed, so a stale "open" decision (like an EXD that
    # reality already resolved) gets caught and revisited instead of lingering.
    today = datetime.now()
    for d in open_decisions:
        review = parse_date(d.get("review"))
        d["reviewOverdue"] = bool(review and review < today)
    brainstorm = root / "executive-os" / "NEXT-MOVES.md"
    brainstorm_text = ""
    if brainstorm.exists():
        # Strip the heading clutter; keep the body so it can render inline on the dashboard.
        raw = brainstorm.read_text(encoding="utf-8", errors="replace")
        body_lines = [ln for ln in raw.splitlines() if ln.strip() and not ln.strip().startswith("#")]
        brainstorm_text = "\n".join(body_lines).strip()
    return {
        "stages": [
            {"name": "Morning", "what": "./agentic-os morning reads every repo and refreshes status."},
            {"name": "Project status", "what": "Per-project state, blockers, and next action."},
            {"name": "Executive review", "what": "CEO / COO / CFO / Analysis read status and add remarks."},
            {"name": "Decisions", "what": f"{len(open_decisions)} open of {len(decisions)} logged in EXECUTIVE-DECISIONS.md."},
            {"name": "Work packets", "what": f"{len(active_packets)} active, {len(packets)} total. Copy only Active packets; closed packets are history."},
            {"name": "Brainstorm / next moves", "what": ("Open ideas in NEXT-MOVES.md." if brainstorm.exists() else "Add executive-os/NEXT-MOVES.md to capture ideas.")},
        ],
        "openDecisions": open_decisions[:8],
        "workPackets": packets,
        "brainstormExists": brainstorm.exists(),
        "brainstorm": brainstorm_text,
    }


def check_repo_integrity(root: Path) -> dict[str, Any]:
    """Cross-tool sync signal: is everything committed and on main, with no stray worktrees?

    The founder works across Codex, Claude Code, and Cursor; the only shared truth is git.
    This surfaces uncommitted changes, the current branch vs main, and extra worktrees so
    drift between tools is visible instead of silently losing work.
    """
    branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=root)
    current = branch.stdout.strip() if branch.returncode == 0 else "unknown"
    dirty = run(["git", "status", "--short"], cwd=root)
    # Generated dashboard artifacts churn on every refresh; their change is not "unsynced work".
    # The sync signal should only flag REAL source drift, so exclude generated paths from the count.
    generated_prefixes = (
        "dashboard/", "DASHBOARD.md", "PROJECT-STATUS.md", "executive-os/EXECUTIVE-DASHBOARD.md",
    )
    real_changes = []
    if dirty.returncode == 0:
        for line in dirty.stdout.splitlines():
            path = line[3:].strip().strip('"') if len(line) > 3 else ""
            if path and not path.startswith(generated_prefixes):
                real_changes.append(path)
    uncommitted = len(real_changes)
    wt = run(["git", "worktree", "list"], cwd=root)
    worktrees = [ln for ln in wt.stdout.splitlines() if ln.strip()] if wt.returncode == 0 else []
    extra_worktrees = max(0, len(worktrees) - 1)
    synced = current == "main" and uncommitted == 0 and extra_worktrees == 0
    notes: list[str] = []
    if current != "main":
        notes.append(f"On branch '{current}', not main. Merge to main so all tools see it.")
    if uncommitted:
        notes.append(f"{uncommitted} uncommitted change(s). Commit so nothing is lost between sessions/tools.")
    if extra_worktrees:
        notes.append(f"{extra_worktrees} extra worktree(s) open. Consolidate to main; do not work in worktrees.")
    return {
        "branch": current,
        "uncommitted": uncommitted,
        "extraWorktrees": extra_worktrees,
        "synced": synced,
        "notes": notes or ["Clean: on main, fully committed, no stray worktrees."],
    }


def _is_strategic_plan(plan: dict[str, Any]) -> bool:
    path = (plan.get("path") or "").lower()
    kind = (plan.get("kind") or "").lower()
    if kind == "gtm":
        return True
    markers = ("gtm", "launch", "monetization", "distribution", "business-gtm")
    return any(m in path for m in markers)


def _packet_links_plan(packet: dict[str, Any], plan_path: str) -> bool:
    source = (packet.get("source") or "").lower()
    path_key = plan_path.replace("\\", "/").lower()
    name = Path(plan_path).name.lower()
    stem = Path(plan_path).stem.lower()
    hay = f"{source} {packet.get('path', '')}".lower()
    return name in hay or stem in hay or path_key in hay


def _packet_is_active(packet: dict[str, Any]) -> bool:
    status = (packet.get("status") or "").lower()
    return status.startswith("active")


def _build_numbers(text: str) -> list[int]:
    return [int(match) for match in re.findall(r"\bbuild\s+(\d+)\b", text, flags=re.IGNORECASE)]


def build_packet_hygiene(status: dict[str, Any], root: Path) -> list[dict[str, str]]:
    """Find packet registry states that contradict the current dashboard."""
    issues: list[dict[str, str]] = []
    packets = status.get("executiveLoop", {}).get("workPackets", [])
    runsmart = next((p for p in status.get("projectHealth", []) if p.get("name") == "RunSmart iOS"), {})
    runsmart_current = " ".join(
        str(runsmart.get(key) or "")
        for key in ("state", "nextAction", "parsedActiveStory", "parsedLastValidation")
    )
    current_runsmart_builds = _build_numbers(runsmart_current)
    current_runsmart_build = max(current_runsmart_builds) if current_runsmart_builds else None
    active_by_repo: dict[str, list[str]] = {}

    for packet in packets:
        packet_path = root / (packet.get("path") or "")
        packet_text = packet_path.read_text(encoding="utf-8", errors="replace") if packet_path.exists() else ""
        packet_label = f"{packet.get('title', 'Untitled')} ({packet.get('path', 'unknown path')})"
        status_text = packet.get("status") or ""

        if _packet_is_active(packet):
            active_by_repo.setdefault(packet.get("repoId") or "unknown", []).append(packet_label)
            if "superseded" in packet_text.lower() or "historical packet" in packet_text.lower():
                issues.append(
                    {
                        "severity": "error",
                        "path": packet.get("path") or "",
                        "message": f"{packet_label} is marked Active but its text says it is superseded/historical.",
                    }
                )
            packet_builds = _build_numbers(
                " ".join(
                    str(packet.get(key) or "")
                    for key in ("title", "goal", "source", "successSignal", "path")
                )
            )
            if (
                packet.get("repoId") == "runsmart-ios"
                and current_runsmart_build
                and packet_builds
                and max(packet_builds) < current_runsmart_build
            ):
                issues.append(
                    {
                        "severity": "error",
                        "path": packet.get("path") or "",
                        "message": (
                            f"{packet_label} is Active for build {max(packet_builds)}, "
                            f"but current RunSmart status is build {current_runsmart_build}."
                        ),
                    }
                )

        packet_builds = _build_numbers(packet_text)
        if (
            packet.get("repoId") == "runsmart-ios"
            and current_runsmart_build
            and status_text.lower().startswith(("open", "active"))
            and packet_builds
            and max(packet_builds) < current_runsmart_build
        ):
            issues.append(
                {
                    "severity": "warning",
                    "path": packet.get("path") or "",
                    "message": (
                        f"{packet_label} is {status_text} but references older build "
                        f"{max(packet_builds)} while current RunSmart status is build {current_runsmart_build}."
                    ),
                }
            )

    for repo_id, labels in active_by_repo.items():
        if len(labels) > 1:
            issues.append(
                {
                    "severity": "error",
                    "path": "executive-os/work-packets",
                    "message": f"{repo_id} has multiple Active packets: {', '.join(labels)}",
                }
            )

    coo_latest = root / "executive-os" / "COO-LATEST-REVIEW.md"
    if coo_latest.exists() and current_runsmart_build:
        coo_builds = _build_numbers(coo_latest.read_text(encoding="utf-8", errors="replace"))
        if coo_builds and max(coo_builds) < current_runsmart_build:
            issues.append(
                {
                    "severity": "error",
                    "path": str(coo_latest.relative_to(root)),
                    "message": (
                        f"COO latest review references build {max(coo_builds)}, "
                        f"but current RunSmart status is build {current_runsmart_build}."
                    ),
                }
            )

    return issues


def build_plan_execution_status(
    saved_plans: list[dict[str, Any]],
    work_packets: list[dict[str, Any]],
    root: Path,
) -> dict[str, Any]:
    """Index strategic plans vs active work packets — never label a plan Stale.

    Plans (GTM, launch, monetization, distribution) stay in savedPlans for full text.
    This surface is titles + executionStatus only: active, needs_next_packet, research_only.
    """
    seen_paths: set[str] = set()
    rows: list[dict[str, Any]] = []

    def add_row(
        *,
        title: str,
        path: str,
        project: str,
        project_id: str,
        execution_status: str,
        active_packet: str | None = None,
        note: str | None = None,
    ) -> None:
        norm = path.replace("\\", "/")
        if norm in seen_paths:
            return
        seen_paths.add(norm)
        rows.append(
            {
                "title": title,
                "path": norm,
                "project": project,
                "projectId": project_id,
                "executionStatus": execution_status,
                "activePacket": active_packet,
                "note": note,
            }
        )

    for entry in saved_plans:
        for plan in entry.get("plans") or []:
            if not _is_strategic_plan(plan):
                continue
            path = plan.get("path") or ""
            active = next(
                (p for p in work_packets if _packet_is_active(p) and _packet_links_plan(p, path)),
                None,
            )
            if active:
                add_row(
                    title=plan.get("title") or Path(path).stem,
                    path=path,
                    project=entry["project"],
                    project_id=entry["projectId"],
                    execution_status="active",
                    active_packet=active.get("title"),
                )
            else:
                add_row(
                    title=plan.get("title") or Path(path).stem,
                    path=path,
                    project=entry["project"],
                    project_id=entry["projectId"],
                    execution_status="needs_next_packet",
                    note="COO: extract next milestone into one work packet.",
                )

    gtm_v0 = root / "executive-os" / "BUSINESS-GTM-PLAN-V0.md"
    if gtm_v0.exists():
        rel = "executive-os/BUSINESS-GTM-PLAN-V0.md"
        if rel not in seen_paths:
            active = next(
                (p for p in work_packets if _packet_is_active(p) and _packet_links_plan(p, rel)),
                None,
            )
            add_row(
                title="Business + GTM Plan v0",
                path=rel,
                project="Agentic OS",
                project_id="agentic-os",
                execution_status="active" if active else "needs_next_packet",
                active_packet=active.get("title") if active else None,
                note=None if active else "Portfolio GTM source — next packet from COO review.",
            )

    research_dir = root / "executive-os" / "research"
    if research_dir.is_dir():
        for doc in sorted(research_dir.glob("*.md")):
            rel = str(doc.relative_to(root)).replace("\\", "/")
            add_row(
                title=doc.stem.replace("-", " ").title(),
                path=rel,
                project="Agentic OS",
                project_id="agentic-os",
                execution_status="research_only",
                note="Research input — not daily execution.",
            )

    order = {"active": 0, "needs_next_packet": 1, "research_only": 2}
    rows.sort(key=lambda r: (order.get(r["executionStatus"], 9), r["project"], r["title"]))
    needs = sum(1 for r in rows if r["executionStatus"] == "needs_next_packet")
    active_count = sum(1 for r in rows if r["executionStatus"] == "active")
    return {
        "plans": rows,
        "activeCount": active_count,
        "needsNextPacket": needs,
        "researchOnlyCount": sum(1 for r in rows if r["executionStatus"] == "research_only"),
        "vocabulary": "Plan execution uses active | needs_next_packet | research_only. Repo freshness Stale is separate.",
    }


def build_portfolio_trust(
    project_health: list[dict[str, Any]],
    repo_integrity: dict[str, Any],
    run_center: dict[str, Any],
    plan_execution: dict[str, Any] | None = None,
    contradictions: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Whether the founder can trust today's dashboard for App Store / ship claims."""
    today = datetime.now().date()
    refresh_today = False
    last_refresh = run_center.get("lastRefresh") or ""
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", last_refresh)
    if date_match:
        parsed = parse_date(date_match.group(1))
        if parsed:
            refresh_today = parsed.date() == today

    apps = [p for p in project_health if p.get("id") in APP_IDS]
    stale_apps = [p["name"] for p in apps if p.get("freshness") == "Stale"]
    dirty_apps = [p["name"] for p in apps if p.get("dirty")]
    app_worktrees = [
        f"{p['name']} ({p.get('extraWorktrees', 0)})"
        for p in apps
        if p.get("extraWorktrees", 0)
    ]
    low_conf = [
        p["name"]
        for p in apps
        if (p.get("sourceConfidence") or "").lower() in ("low", "unknown")
    ]
    evidence_gaps = [p["name"] for p in apps if p.get("evidenceGap")]

    level = "actionable"
    reasons: list[str] = []
    hard_contradictions = [c for c in (contradictions or []) if c.get("severity") == "hard"]
    if hard_contradictions:
        level = "refresh_required"
        reasons.append("Status contradicts reality. Confirm and reconcile status before acting.")
        reasons.extend(c.get("message", "Unspecified contradiction.") for c in hard_contradictions[:3])
    elif not repo_integrity.get("synced"):
        level = "refresh_required"
        reasons.append(
            "Run ./agentic-os morning or fix sync before trusting App Store / ship / readiness claims."
        )
        reasons.extend(repo_integrity.get("notes") or [])
    elif not refresh_today:
        level = "refresh_required"
        reasons.append(
            "Run ./agentic-os morning or fix sync before trusting App Store / ship / readiness claims."
        )
        reasons.append("Morning refresh was not run today.")
    elif stale_apps:
        level = "refresh_required"
        reasons.append(
            "Run ./agentic-os morning or fix sync before trusting App Store / ship / readiness claims."
        )
        reasons.append(f"Stale shippable app evidence: {', '.join(stale_apps)}.")
    elif dirty_apps or low_conf or evidence_gaps:
        level = "caution"
        reasons.append(
            "Status can guide planning, but validate before acting on release, billing, auth, production, or App Store steps."
        )
        if dirty_apps:
            reasons.append(f"Dirty shippable app repo: {', '.join(dirty_apps)}.")
        if low_conf:
            level = "caution"
            reasons.append(f"Low source confidence: {', '.join(low_conf)}.")
        if evidence_gaps:
            reasons.append(f"Evidence gap after latest commit: {', '.join(evidence_gaps)}.")

    labels = {
        "actionable": "Actionable",
        "caution": "Use caution",
        "refresh_required": "Refresh required",
    }
    needs = (plan_execution or {}).get("needsNextPacket", 0)
    if needs and level == "actionable":
        reasons.append(
            f"{needs} strategic plan(s) need the next work packet (COO review) — plans are not abandoned."
        )
    if not reasons:
        reasons.append("Sync clean, refreshed today, app evidence current.")

    hygiene_warnings: list[str] = []
    if dirty_apps:
        hygiene_warnings.append(f"Uncommitted files in product repos: {', '.join(dirty_apps)}.")
    if app_worktrees:
        hygiene_warnings.append(f"Extra product worktrees retained for review: {', '.join(app_worktrees)}.")

    return {
        "level": level,
        "label": labels[level],
        "reasons": reasons,
        "refreshToday": refresh_today,
        "needsNextPacketCount": needs,
        "hygieneWarnings": hygiene_warnings,
    }


def build_saved_plans(project_health: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Flatten per-project plans into one portfolio board, recent first, GTM always kept.

    Each project keeps the most recent PLANS_PER_PROJECT plans plus all GTM plans, with a total
    count so nothing looks hidden. This is the surface that guarantees a saved plan is visible.
    """
    board: list[dict[str, Any]] = []
    for project in project_health:
        plans = project.get("plans") or []
        if not plans:
            continue
        gtm = [p for p in plans if p.get("kind") == "gtm"]
        recent = plans[:PLANS_PER_PROJECT]
        # union (recent + all gtm), de-duped by path, preserving recent-first order
        chosen: list[dict[str, Any]] = []
        for plan in recent + gtm:
            if plan not in chosen:
                chosen.append(plan)
        board.append(
            {
                "project": project["name"],
                "projectId": project["id"],
                "total": len(plans),
                "shown": len(chosen),
                "plans": chosen,
            }
        )
    return board


def build_derived_summary(
    project_health: list[dict[str, Any]],
    saved_plans: list[dict[str, Any]] | None = None,
    plan_execution: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Assemble the portfolio headline + priority board purely from parsed repo truth.

    This is the single source for the headline. It used to be hand-written prose that nothing
    regenerated, so it went stale (showing 'build 6 in review' after build 8 shipped). Everything
    here is derived from each repo's parsed status, so it can never contradict the repos and is
    rebuilt on every `./agentic-os morning`. The two shippable apps get their next step inline;
    support repos show their phase only.
    """
    by_id = {p.get("id"): p for p in project_health}
    products = [p for p in project_health if p.get("id") in PRODUCT_IDS]

    def headline_part(project: dict[str, Any]) -> str:
        phase = clean_cell(project.get("state") or "Unknown")
        if project.get("id") in APP_IDS and project.get("nextAction"):
            return f"{project['name']} — {phase}: {clean_cell(project['nextAction'])}"
        return f"{project['name']} — {phase}"

    overall = " · ".join(headline_part(p) for p in products) or "No product status parsed from local repos."

    def actionable(project: dict[str, Any]) -> bool:
        action = (project.get("nextAction") or "").lower()
        return bool(action) and not action.startswith(("monitor", "refresh local", "none"))

    ranked = [by_id[i] for i in APP_IDS if i in by_id]
    best_src = next(
        (p for p in ranked if actionable(p)),
        ranked[0] if ranked else (products[0] if products else None),
    )
    best = (
        f"{best_src['name']}: {best_src.get('nextAction') or 'Refresh local status.'}"
        if best_src
        else "Run ./agentic-os morning to refresh local status."
    )

    now: list[str] = []
    nxt: list[str] = []
    later: list[str] = []
    blocked: list[str] = []
    blockers_all: list[str] = []

    for project in products:
        line = f"{project['name']}: {project.get('nextAction') or 'Refresh local status.'}"
        if project.get("id") in APP_IDS:
            now.append(line)
        else:
            nxt.append(line)
        for blocker in project.get("blockers") or []:
            blockers_all.append(f"{project['name']}: {blocker}")
            if re.search(
                r"external|apple|founder|backend|credential|locked|review outcome|not live",
                blocker,
                re.IGNORECASE,
            ):
                blocked.append(f"{project['name']}: {blocker}")
        gtm = project.get("gtm") or {}
        if gtm.get("exists") and gtm.get("positioning"):
            later.append(
                f"{project['name']} GTM ready ({gtm.get('status') or 'draft'}): "
                f"{gtm['positioning']} — see {gtm.get('path')}"
            )

    # Surface saved-plan presence in the board so the founder sees that plans they asked to
    # save exist and where (the full list is the Saved Plans board).
    for entry in saved_plans or []:
        latest = entry["plans"][0] if entry.get("plans") else None
        if latest:
            later.append(
                f"{entry['project']}: {entry['total']} saved plan(s) — latest \"{latest['title']}\" "
                f"({latest.get('date') or 'undated'}). See Saved Plans."
            )

    needs_packets = (plan_execution or {}).get("needsNextPacket", 0)
    if needs_packets:
        later.append(
            f"Portfolio: {needs_packets} strategic plan(s) need the next work packet — "
            "run COO operating review (see Command Center plan index)."
        )

    return {
        "overallStatus": overall,
        "bestNextAction": best,
        "mainBlockers": list(dict.fromkeys(blockers_all)),
        "priorityBoard": {
            "now": now or ["Run ./agentic-os morning to refresh local status."],
            "next": nxt or ["None parsed."],
            "later": later or ["None parsed."],
            "blocked": list(dict.fromkeys(blocked)) or ["None parsed."],
        },
    }


def collect_stranded_work(path: Path) -> dict[str, Any]:
    """Scan a repo for work that can silently get lost across tools and sessions.

    Claude Code, Codex, and Cursor sessions leave behind: commits on branches that were
    never pushed, local-only branches with no upstream, branches whose remote was deleted
    ([gone]) while unmerged commits remain, extra worktrees (sometimes dirty), and a
    default branch that is itself ahead or behind origin. Each one is a place finished
    work goes to die. This collects all of them so the dashboard and morning brief can
    show one consolidated board.
    """
    result: dict[str, Any] = {
        "unpushedBranches": [],
        "unmergedLocalBranches": [],
        "staleMergedBranchCount": 0,
        "extraWorktrees": [],
        "defaultBranchIssues": [],
    }
    refs = run(
        [
            "git",
            "for-each-ref",
            "refs/heads",
            "--format=%(refname:short)|%(upstream:short)|%(upstream:track)|%(committerdate:short)",
        ],
        cwd=path,
    )
    if refs.returncode != 0:
        return result

    default_branch = "main"
    heads = {line.split("|", 1)[0] for line in refs.stdout.splitlines() if line.strip()}
    if "main" not in heads and "master" in heads:
        default_branch = "master"

    # Merged-ness is judged against origin's default branch when available, so branches
    # merged from another machine or the web UI are not misreported as lost work.
    merge_base = f"origin/{default_branch}"
    merged = run(["git", "branch", "--format=%(refname:short)", "--merged", merge_base], cwd=path)
    if merged.returncode != 0:
        merged = run(
            ["git", "branch", "--format=%(refname:short)", "--merged", default_branch], cwd=path
        )
    merged_branches = (
        {b.strip() for b in merged.stdout.splitlines() if b.strip()}
        if merged.returncode == 0
        else set()
    )

    for line in refs.stdout.splitlines():
        parts = (line.split("|") + ["", "", "", ""])[:4]
        branch, upstream, track, commit_date = parts
        if not branch:
            continue
        ahead_match = re.search(r"ahead (\d+)", track)
        behind_match = re.search(r"behind (\d+)", track)
        ahead = int(ahead_match.group(1)) if ahead_match else 0
        behind = int(behind_match.group(1)) if behind_match else 0
        gone = "[gone]" in track
        if branch == default_branch:
            if ahead:
                result["defaultBranchIssues"].append(
                    f"{branch} has {ahead} unpushed commit(s)"
                )
            if behind:
                result["defaultBranchIssues"].append(
                    f"{branch} is {behind} commit(s) behind origin (pull needed)"
                )
            continue
        if ahead:
            result["unpushedBranches"].append(
                {"branch": branch, "ahead": ahead, "lastCommitDate": commit_date}
            )
        elif (not upstream or gone) and branch not in merged_branches:
            reason = "remote branch deleted" if gone else "never pushed"
            result["unmergedLocalBranches"].append(
                {"branch": branch, "reason": reason, "lastCommitDate": commit_date}
            )
        elif (not upstream or gone) and branch in merged_branches:
            result["staleMergedBranchCount"] += 1

    wt = run(["git", "worktree", "list", "--porcelain"], cwd=path)
    if wt.returncode == 0:
        entries: list[dict[str, str]] = []
        current: dict[str, str] = {}
        for line in wt.stdout.splitlines():
            if line.startswith("worktree "):
                if current:
                    entries.append(current)
                current = {"path": line[len("worktree ") :].strip()}
            elif line.startswith("branch "):
                current["branch"] = line[len("branch ") :].replace("refs/heads/", "").strip()
        if current:
            entries.append(current)
        for entry in entries[1:]:  # the first entry is the primary checkout
            wt_path = Path(entry.get("path", ""))
            dirty_count = 0
            if wt_path.exists():
                st = run(["git", "status", "--short"], cwd=wt_path)
                if st.returncode == 0:
                    dirty_count = len([ln for ln in st.stdout.splitlines() if ln.strip()])
            result["extraWorktrees"].append(
                {
                    "path": str(wt_path),
                    "branch": entry.get("branch", "detached"),
                    "dirtyCount": dirty_count,
                }
            )
    return result


def summarize_stranded_work(
    name: str, stranded: dict[str, Any], dirty_count: int
) -> list[dict[str, str]]:
    """Turn one repo's stranded-work scan into actionable board items (pure, testable)."""
    items: list[dict[str, str]] = []
    for issue in stranded.get("defaultBranchIssues", []):
        items.append(
            {
                "project": name,
                "type": "default-branch",
                "detail": issue,
                "action": "Sync the default branch first: pull, then push.",
            }
        )
    for b in stranded.get("unpushedBranches", []):
        items.append(
            {
                "project": name,
                "type": "unpushed",
                "detail": f"{b['branch']}: {b['ahead']} unpushed commit(s), last commit {b['lastCommitDate']}",
                "action": f"Push {b['branch']} and open a PR, or explicitly hand it off.",
            }
        )
    for b in stranded.get("unmergedLocalBranches", []):
        items.append(
            {
                "project": name,
                "type": "local-only",
                "detail": (
                    f"{b['branch']}: unmerged commits, {b['reason']}, "
                    f"last commit {b['lastCommitDate']}"
                ),
                "action": f"Push {b['branch']} and open a PR, or consciously discard it.",
            }
        )
    for w in stranded.get("extraWorktrees", []):
        dirty = f", {w['dirtyCount']} uncommitted file(s)" if w.get("dirtyCount") else ""
        items.append(
            {
                "project": name,
                "type": "worktree",
                "detail": f"worktree on {w.get('branch', 'detached')}{dirty} at {w['path']}",
                "action": "Land or discard this worktree, then `git worktree remove` it.",
            }
        )
    if dirty_count:
        items.append(
            {
                "project": name,
                "type": "dirty",
                "detail": f"{dirty_count} uncommitted file(s) in the primary working tree",
                "action": "Commit or discard before the next session ends.",
            }
        )
    stale = stranded.get("staleMergedBranchCount", 0)
    if stale:
        items.append(
            {
                "project": name,
                "type": "cleanup",
                "detail": f"{stale} merged branch(es) safe to delete",
                "action": "Delete merged local branches to cut noise.",
            }
        )
    return items


AGENT_BRANCH_PREFIXES = ("claude/", "codex/", "cursor/")


def decide_cleanup_action(branch: str, dirty: bool, merged: bool) -> str:
    """Cleanup policy for one branch/worktree (pure, testable).

    Only agent-created branches (claude/*, codex/*) are ever cleaned; the founder's
    intentional branches (main, monetization, feature work) are reported, never touched.

    Returns:
      'skip'   - not an agent branch: report only
      'delete' - agent branch merged into origin's default branch: remove outright
      'backup' - agent branch with unmerged commits or dirty files: push to origin
                 first (work preserved, recoverable), then remove locally
    """
    if not branch.startswith(AGENT_BRANCH_PREFIXES):
        return "skip"
    if dirty:
        return "backup"
    return "delete" if merged else "backup"


def clean_repos(apply: bool) -> int:
    """Remove agent-created worktrees and branches across all project repos.

    Dry run by default; --apply executes. Backup-first: anything unmerged or dirty is
    committed on its own branch and pushed to origin with an explicit refspec (never to
    the default branch) before local removal. Nothing unrecoverable is ever deleted.
    """
    mode = "APPLY" if apply else "DRY RUN (use --apply to execute)"
    print(f"Agent worktree/branch cleanup - {mode}")
    failures = 0
    for source_name, path in parse_project_paths():
        _, display_name = PROJECT_ALIASES[source_name]
        if not path.exists():
            continue
        refs = run(
            ["git", "for-each-ref", "refs/heads", "--format=%(refname:short)|%(upstream:track)"],
            cwd=path,
        )
        if refs.returncode != 0:
            continue
        print(f"\n== {display_name} ({path})")
        run(["git", "fetch", "origin", "--prune"], cwd=path, timeout=60)

        heads = {ln.split("|", 1)[0] for ln in refs.stdout.splitlines() if ln.strip()}
        default_branch = "main" if "main" in heads or "master" not in heads else "master"
        merged_out = run(
            ["git", "branch", "--format=%(refname:short)", "--merged", f"origin/{default_branch}"],
            cwd=path,
        )
        merged = (
            {b.strip() for b in merged_out.stdout.splitlines() if b.strip()}
            if merged_out.returncode == 0
            else set()
        )
        primary_branch = run(["git", "branch", "--show-current"], cwd=path).stdout.strip()

        # Worktrees first (a branch checked out in a worktree cannot be deleted until
        # the worktree is removed).
        wt = run(["git", "worktree", "list", "--porcelain"], cwd=path)
        worktree_branches: set[str] = set()
        entries: list[dict[str, str]] = []
        current: dict[str, str] = {}
        for line in wt.stdout.splitlines():
            if line.startswith("worktree "):
                if current:
                    entries.append(current)
                current = {"path": line[len("worktree ") :].strip()}
            elif line.startswith("branch "):
                current["branch"] = line[len("branch ") :].replace("refs/heads/", "").strip()
            elif line.strip() == "detached":
                current["branch"] = ""
        if current:
            entries.append(current)
        for entry in entries[1:]:
            wt_path = Path(entry.get("path", ""))
            branch = entry.get("branch", "")
            if not branch:
                print(f"  REPORT detached worktree at {wt_path} - resolve manually")
                continue
            worktree_branches.add(branch)
            dirty_count = 0
            if wt_path.exists():
                st = run(["git", "status", "--short"], cwd=wt_path)
                dirty_count = len([ln for ln in st.stdout.splitlines() if ln.strip()])
            action = decide_cleanup_action(branch, dirty_count > 0, branch in merged)
            if action == "skip":
                print(f"  REPORT non-agent worktree on {branch} at {wt_path} - left untouched")
                continue
            label = f"worktree {wt_path} (branch {branch}, {dirty_count} dirty)"
            if not apply:
                print(f"  PLAN {action}: {label}")
                continue
            ok = True
            if action == "backup":
                if dirty_count and wt_path.exists():
                    run(["git", "add", "-A"], cwd=wt_path)
                    run(
                        ["git", "commit", "-m", "wip: preserve agent worktree state before cleanup"],
                        cwd=wt_path,
                    )
                push = run(
                    ["git", "push", "origin", f"{branch}:refs/heads/{branch}"], cwd=path, timeout=120
                )
                ok = push.returncode == 0
                if not ok:
                    print(f"  FAIL push {branch}; worktree kept: {push.stderr.strip()[:200]}")
                    failures += 1
            if ok:
                try:
                    # Web worktrees can hold node_modules; deletion can take minutes.
                    removed = run(
                        ["git", "worktree", "remove", "--force", str(wt_path)],
                        cwd=path,
                        timeout=600,
                    )
                except subprocess.TimeoutExpired:
                    print(f"  FAIL remove {wt_path}: timed out")
                    failures += 1
                    continue
                if removed.returncode == 0:
                    run(["git", "branch", "-D", branch], cwd=path)
                    print(f"  DONE {action}: {label}")
                else:
                    print(f"  FAIL remove {wt_path}: {removed.stderr.strip()[:200]}")
                    failures += 1

        run(["git", "worktree", "prune"], cwd=path)

        # Then agent branches without worktrees.
        refs = run(
            ["git", "for-each-ref", "refs/heads", "--format=%(refname:short)"], cwd=path
        )
        for branch in [b.strip() for b in refs.stdout.splitlines() if b.strip()]:
            if branch in (default_branch, primary_branch) or branch in worktree_branches:
                continue
            action = decide_cleanup_action(branch, False, branch in merged)
            if action == "skip":
                continue
            if not apply:
                print(f"  PLAN {action}: branch {branch}")
                continue
            ok = True
            if action == "backup":
                push = run(
                    ["git", "push", "origin", f"{branch}:refs/heads/{branch}"], cwd=path, timeout=120
                )
                ok = push.returncode == 0
                if not ok:
                    print(f"  FAIL push {branch}; branch kept: {push.stderr.strip()[:200]}")
                    failures += 1
            if ok:
                run(["git", "branch", "-D", branch], cwd=path)
                print(f"  DONE {action}: branch {branch}")
    print(f"\nCleanup {'complete' if apply else 'planned'}; failures: {failures}")
    return 1 if failures else 0


def collect_evidence() -> list[ProjectEvidence]:
    evidence: list[ProjectEvidence] = []
    for source_name, path in parse_project_paths():
        project_id, display_name = PROJECT_ALIASES[source_name]
        sources: list[str] = []
        exists = path.exists()
        branch = "missing"
        dirty = False
        dirty_count = 0
        extra_worktrees = 0
        last_commit = "No git data"

        if exists:
            for rel in [
                "tasks/MEMORY.md",
                "tasks/todo.md",
                "tasks/progress.md",
                "tasks/session-log.md",
                "docs/agent-os/project-context.md",
                "docs/specs/README.md",
                "docs/product/product-vision.md",
                "docs/product/current-product-state.md",
            ]:
                record_if_exists(path / rel, path, sources)

            status = run(["git", "status", "--short", "--branch"], cwd=path)
            if status.returncode == 0:
                lines = status.stdout.splitlines()
                branch = lines[0].replace("## ", "") if lines else "unknown"
                dirty_count = max(0, len(lines) - 1)
                dirty = dirty_count > 0

            commit = run(["git", "log", "-1", "--pretty=%cd %h %s", "--date=short"], cwd=path)
            if commit.returncode == 0 and commit.stdout.strip():
                last_commit = commit.stdout.strip()

            worktrees = run(["git", "worktree", "list", "--porcelain"], cwd=path)
            if worktrees.returncode == 0:
                worktree_count = sum(
                    1 for line in worktrees.stdout.splitlines() if line.startswith("worktree ")
                )
                extra_worktrees = max(0, worktree_count - 1)

        gtm = parse_gtm(path) if exists else {"exists": False, "path": None, "positioning": None, "status": None, "lastUpdated": None}
        if gtm.get("exists") and gtm.get("path"):
            sources.append(gtm["path"])

        plans = collect_plans(path) if exists else []
        for plan in plans:
            if plan["path"] not in sources:
                sources.append(plan["path"])

        evidence.append(
            ProjectEvidence(
                project_id=project_id,
                name=display_name,
                path=path,
                exists=exists,
                branch=branch,
                dirty=dirty,
                dirty_count=dirty_count,
                extra_worktrees=extra_worktrees,
                last_commit=last_commit,
                source_files=sources,
                task_parse=parse_task_files(path),
                gtm=gtm,
                plans=plans,
                stranded=collect_stranded_work(path) if exists else {},
            )
        )
    return evidence


def resolve_confidence(parse: dict[str, Any], project: dict[str, Any], exists: bool) -> str:
    """Project-level confidence: prefer parsed local truth, fall back to narrative.

    High/Medium come straight from the parser (local task files were read). When no
    task files exist but the path is present and dashboard narrative is available, the
    status is narrative-only -> Low. Missing path or no source at all -> Unknown.
    """
    parsed = parse.get("sourceConfidence", "Unknown")
    if parsed in ("High", "Medium"):
        return parsed
    has_narrative = bool(project.get("currentPhase") or project.get("status"))
    if exists and has_narrative:
        return "Low"
    return "Unknown"


def project_health_from(evidence: list[ProjectEvidence], status: dict[str, Any]) -> list[dict[str, Any]]:
    by_id = {p.get("id"): p for p in status.get("projects", [])}
    health: list[dict[str, Any]] = []
    for item in evidence:
        project = by_id.get(item.project_id, {})
        parse = item.task_parse or empty_task_parse()
        blockers = parse.get("blockers") or project.get("blockers") or []
        next_actions = project.get("nextActions") or []
        next_action = (
            parse.get("nextRecommendedStory")
            or (next_actions[0] if next_actions else None)
            or project.get("nextRecommendedStory")
            or "Refresh local status."
        )
        state = (
            parse.get("currentPhase")
            or project.get("currentPhase")
            or parse.get("status")
            or project.get("status")
            or "Unknown"
        )
        confidence = resolve_confidence(parse, project, item.exists)
        freshness, freshest_date = compute_freshness(
            [parse_date(parse.get("lastUpdated")), parse_date(item.last_commit)]
        )
        # Stale evidence cannot support a confident status: downgrade one level.
        if freshness == "Stale":
            confidence = CONFIDENCE_DOWNGRADE[confidence]
        # Evidence gap: code committed after the last validation = proof predates the code.
        evidence = parse.get("evidence") or {}
        evidence_date = parse_date(evidence.get("evidenceDate"))
        commit_date = parse_date(item.last_commit)
        evidence_gap = bool(evidence_date and commit_date and commit_date > evidence_date)
        health.append(
            {
                "id": item.project_id,
                "name": item.name,
                "state": state,
                "nextAction": next_action,
                "blockerCount": len(blockers),
                "blockers": blockers,
                "gtm": item.gtm or {"exists": False},
                "plans": item.plans or [],
                "dirty": item.dirty,
                "dirtyCount": item.dirty_count,
                "extraWorktrees": item.extra_worktrees,
                "branch": item.branch,
                "lastCommit": item.last_commit,
                "stale": freshness == "Stale" or not item.exists,
                "freshness": freshness,
                "freshestDate": freshest_date,
                "evidenceGap": evidence_gap,
                "evidenceDate": evidence.get("evidenceDate"),
                "evidenceTests": evidence.get("tests") or [],
                "buildStatus": evidence.get("buildStatus"),
                "qaDocs": evidence.get("qaDocs") or [],
                "sourceFiles": item.source_files,
                "sourceConfidence": confidence,
                "preferredSource": parse.get("preferredSource", "none"),
                "parsedLastValidation": parse.get("lastValidation"),
                "parsedLastUpdated": parse.get("lastUpdated"),
                "parsedActiveStory": parse.get("activeStory"),
            }
        )
    return health


def declared_prelaunch(state: str) -> bool:
    low = (state or "").lower()
    return any(
        token in low
        for token in (
            "in review",
            "app store review",
            "review pending",
            "not launched",
            "not submitted",
            "pre-release",
            "resubmission",
            "processing",
        )
    )


def latest_tag_info(repo_path: Path) -> dict[str, Any]:
    tag = run(["git", "describe", "--tags", "--abbrev=0"], cwd=repo_path, timeout=8)
    if tag.returncode != 0 or not tag.stdout.strip():
        return {"available": False}
    tag_name = tag.stdout.strip()
    date = run(["git", "log", "-1", "--format=%cs", tag_name], cwd=repo_path, timeout=8)
    return {
        "available": True,
        "tag": tag_name,
        "date": date.stdout.strip() if date.returncode == 0 else None,
    }


def normalize_app_store_state(value: str | None) -> str:
    low = (value or "").strip().lower()
    if low in {"live", "ready for sale", "ready_for_sale"}:
        return "live"
    if low in {"in review", "in_review", "waiting for review"}:
        return "in_review"
    if low in {"not submitted", "not_submitted", "draft"}:
        return "not_submitted"
    return "unknown"


def normalize_app_store_entry(value: Any) -> dict[str, Any]:
    if isinstance(value, dict):
        return value
    if isinstance(value, str):
        return {"state": value, "source": "env"}
    return {}


def build_ground_truth(evidence: list[ProjectEvidence], project_health: list[dict[str, Any]]) -> dict[str, Any]:
    overrides = parse_json_env(GROUND_TRUTH_OVERRIDES_ENV)
    app_store_raw = parse_json_env(APP_STORE_STATE_ENV)
    posthog_key = os.environ.get(POSTHOG_KEY_ENV, "").strip()
    by_id = {item.project_id: item for item in evidence}
    health_by_id = {item["id"]: item for item in project_health}

    contradictions: list[dict[str, Any]] = []
    app_rows: list[dict[str, Any]] = []
    posthog_rows: list[dict[str, Any]] = []
    app_store_rows: list[dict[str, Any]] = []
    unavailable: list[str] = []

    for app_id, cfg in POSTHOG_PROJECTS.items():
        row: dict[str, Any] = {"projectId": cfg["projectId"], "appId": app_id, "app": cfg["name"]}
        item = by_id.get(app_id)
        health = health_by_id.get(app_id, {})
        declared_state = health.get("state", "Unknown")
        row["declaredState"] = declared_state

        if item and item.exists:
            tag_info = latest_tag_info(item.path)
        else:
            tag_info = {"available": False}
        row["git"] = tag_info
        app_rows.append(row)

        # Git contradiction: declared "in review"/"resubmission" but repo has a newer release tag date.
        if tag_info.get("available") and declared_prelaunch(declared_state):
            tag_date = parse_date(tag_info.get("date"))
            declared_date = parse_date(health.get("parsedLastUpdated") or health.get("freshestDate"))
            if tag_date and declared_date and tag_date.date() > declared_date.date():
                contradictions.append(
                    {
                        "severity": "warning",
                        "appId": app_id,
                        "source": "git",
                        "kind": "tag-newer-than-declared-review",
                        "message": (
                            f"{cfg['name']} latest tag {tag_info.get('tag')} ({tag_info.get('date')}) "
                            f"is newer than declared review state updated {health.get('parsedLastUpdated') or health.get('freshestDate')}."
                        ),
                    }
                )

        posthog_override = (overrides.get("posthog") or {}).get(app_id)
        if isinstance(posthog_override, dict):
            posthog_info = {
                "available": True,
                "liveUsers7d": int(posthog_override.get("liveUsers7d", 0)),
                "source": "override",
            }
        elif posthog_key:
            posthog_info = fetch_posthog_live_users(cfg["projectId"], posthog_key)
            posthog_info["source"] = "api" if posthog_info.get("available") else "api_error"
        else:
            posthog_info = {"available": False, "error": f"Missing {POSTHOG_KEY_ENV}", "source": "missing_key"}
            unavailable.append(f"PostHog key not configured for {cfg['name']}")
        posthog_rows.append({"appId": app_id, **posthog_info})

        live_users = int(posthog_info.get("liveUsers7d", 0) or 0) if posthog_info.get("available") else 0
        if live_users > 0 and declared_prelaunch(declared_state):
            proposed = (
                f"Confirm update for {cfg['name']}: set Current Phase to LIVE in tasks/progress.md "
                f"(PostHog shows {live_users} users/7d). No auto-write."
            )
            contradictions.append(
                {
                    "severity": "hard",
                    "appId": app_id,
                    "source": "posthog",
                    "kind": "live-users-vs-prelaunch",
                    "message": (
                        f"{cfg['name']} is declared '{declared_state}' but PostHog shows {live_users} live users in 7d."
                    ),
                    "proposedFix": proposed,
                    "confirmPrompt": proposed,
                }
            )

        app_state_override = normalize_app_store_entry(
            (overrides.get("appStore") or {}).get(app_id) or app_store_raw.get(app_id)
        )
        app_store_state = normalize_app_store_state(app_state_override.get("state"))
        app_store_entry = {
            "appId": app_id,
            "state": app_store_state,
            "date": app_state_override.get("date"),
            "source": app_state_override.get("source", "missing"),
            "available": bool(app_state_override),
        }
        app_store_rows.append(app_store_entry)
        if not app_store_entry["available"]:
            unavailable.append(f"App Store state missing for {cfg['name']} (set {APP_STORE_STATE_ENV})")
        if app_store_state == "live" and declared_prelaunch(declared_state):
            proposed = (
                f"Confirm update for {cfg['name']}: set Current Phase to LIVE in tasks/progress.md "
                f"(App Store state live as of {app_store_entry.get('date') or 'undated'}). No auto-write."
            )
            contradictions.append(
                {
                    "severity": "hard",
                    "appId": app_id,
                    "source": "appstore",
                    "kind": "live-vs-prelaunch",
                    "message": (
                        f"{cfg['name']} App Store state is LIVE ({app_store_entry.get('date') or 'undated'}) "
                        f"but declared state is '{declared_state}'."
                    ),
                    "proposedFix": proposed,
                    "confirmPrompt": proposed,
                }
            )

    return {
        "generatedAt": now_label(),
        "apps": app_rows,
        "posthog": posthog_rows,
        "appStore": app_store_rows,
        "contradictions": contradictions,
        "unavailable": unavailable,
        "needsConfirmation": bool(contradictions),
        "proposedFix": (
            "Ground truth contradicts declared status. Proposed next step: confirm and update the relevant "
            "tasks/progress.md status lines. No files were auto-edited."
            if contradictions
            else None
        ),
    }


CONFIDENCE_DIRECTIVE = {
    "High": "Source confidence is High: the status below is parsed from current local task files with validation evidence. You may proceed from it, but still open the repo to confirm specifics.",
    "Medium": "Source confidence is Medium: the status is parsed from local task files but validation is unclear. Verify the current state in the repo before acting.",
    "Low": "Source confidence is Low: the status is narrative-only, with no local task files parsed. You MUST re-read the local repo to establish the real current state before doing anything.",
    "Unknown": "Source confidence is Unknown: there is no reliable status source. Confirm the repo path exists and re-read the repo before acting.",
}


def confidence_directive(confidence: str, evidence_gap: bool) -> str:
    directive = CONFIDENCE_DIRECTIVE.get(confidence, CONFIDENCE_DIRECTIVE["Unknown"])
    if evidence_gap:
        directive += (
            " Note: the repo has commits newer than the last recorded validation, so re-validate "
            "before trusting the recorded evidence."
        )
    return directive


def build_project_prompts(status: dict[str, Any], project_health: list[dict[str, Any]]) -> list[dict[str, Any]]:
    projects = {project.get("id"): project for project in status.get("projects", [])}
    prompts: list[dict[str, Any]] = []
    for health in project_health:
        project = projects.get(health["id"], {})
        role = PROJECT_PROMPT_ROLES.get(health["id"], "Project Operator")
        blockers = health.get("blockers") or project.get("blockers") or []
        source_files = health.get("sourceFiles") or []
        source_list = ", ".join(source_files[:4]) if source_files else "tasks/MEMORY.md if present"
        next_action = health.get("nextAction") or project.get("nextRecommendedStory") or "Choose the smallest useful next action."
        confidence = health.get("sourceConfidence", "Unknown")
        directive = confidence_directive(confidence, bool(health.get("evidenceGap")))
        prompt = (
            f"Act as {role} for {health['name']}. "
            f"{directive} "
            "First read the repo AGENTS.md if it exists, then read the listed source files: "
            f"{source_list}. Current state: {health.get('state', 'Unknown')}. "
            f"Next action: {next_action}. "
            f"Known blockers: {'; '.join(blockers[:3]) if blockers else 'none listed'}. "
            "Deliver one progress-making work packet only: objective, files to inspect, exact implementation or QA steps, "
            "acceptance criteria, checks to run, and what must not be touched. "
            "Do not deploy, submit, email, bill, migrate, or change production services without explicit approval."
        )
        prompts.append(
            {
                "projectId": health["id"],
                "project": health["name"],
                "role": role,
                "repoState": "Dirty" if health.get("dirty") else "Clean",
                "branch": health.get("branch", "Unknown"),
                "nextAction": next_action,
                "sourceConfidence": confidence,
                "trustDirective": directive,
                "evidence": source_files,
                "copyPrompt": prompt,
            }
        )
    return prompts


def build_executive_overview(status: dict[str, Any], project_health: list[dict[str, Any]]) -> dict[str, Any]:
    dirty = [project["name"] for project in project_health if project.get("dirty")]
    blocked = [project["name"] for project in project_health if project.get("blockerCount", 0) > 0]
    stale = [project["name"] for project in project_health if project.get("freshness") == "Stale"]
    evidence_gaps = [project["name"] for project in project_health if project.get("evidenceGap")]
    low_trust = [
        project["name"]
        for project in project_health
        if project.get("sourceConfidence") in ("Low", "Unknown")
    ]
    decisions = status.get("decisionBoard", [])
    metrics = status.get("executiveBoard", {})
    return {
        "headline": status.get("summary", {}).get("bestNextAction", "Choose the next progress move."),
        "portfolioState": status.get("summary", {}).get("overallStatus", "No executive summary available."),
        "focus": metrics.get("top3", []),
        "risks": status.get("summary", {}).get("mainBlockers", []),
        "openDecisionCount": len(decisions),
        "blockedProjectCount": len(blocked),
        "dirtyProjectCount": len(dirty),
        "dirtyProjects": dirty,
        "blockedProjects": blocked,
        "staleProjectCount": len(stale),
        "staleProjects": stale,
        "evidenceGapCount": len(evidence_gaps),
        "evidenceGapProjects": evidence_gaps,
        "lowTrustProjects": low_trust,
        "financialSnapshot": metrics.get("financialSnapshot", "Needs Data"),
        "metricStatus": "Most revenue, retention, and cost metrics are still Needs Data until live sources are wired.",
    }


def normalize_text(value: Any) -> str:
    text = re.sub(r"[^a-z0-9 ]+", " ", str(value or "").lower())
    return re.sub(r"\s+", " ", text).strip()


def texts_disagree(narrative: Any, parsed: Any) -> bool:
    """True when two free-text values genuinely diverge (not just punctuation/casing).

    One string containing the other is treated as agreement, so a longer curated phrasing
    that includes the parsed phrase is not flagged.
    """
    a, b = normalize_text(narrative), normalize_text(parsed)
    if not a or not b or a == b:
        return False
    if a in b or b in a:
        return False
    return True


# Curated project field -> parsed taskParse field -> human label, compared for High projects.
DRIFT_FIELDS = [
    ("currentPhase", "currentPhase", "current phase"),
    ("nextRecommendedStory", "nextRecommendedStory", "next story"),
    ("lastValidation", "lastValidation", "last validation"),
]


def compose_status_narrative(parse: dict[str, Any], health: dict[str, Any]) -> str:
    """Rebuild the long-form project status from parsed repo truth.

    The status field previously carried over from the prior status.json run, so old
    narrative accreted forever. Every sentence here traces to a parsed field, ends with
    provenance, and warns when commits postdate the parsed status (git is then fresher).
    """

    def sentence(text: str) -> str:
        text = text.strip()
        return text if text.endswith(".") else text + "."

    parts: list[str] = []
    if parse.get("currentPhase"):
        parts.append(sentence(f"Phase: {parse['currentPhase']}"))
    if parse.get("activeStory"):
        parts.append(sentence(f"Active: {parse['activeStory']}"))
    if parse.get("lastCompletedStory"):
        parts.append(sentence(f"Last completed: {parse['lastCompletedStory']}"))
    source = parse.get("preferredSource") or "local task files"
    updated = parse.get("lastUpdated") or "unknown date"
    parts.append(f"Source: {source}, updated {updated}.")
    parsed_date = parse_date(parse.get("lastUpdated"))
    commit_date = parse_date(health.get("lastCommit"))
    if parsed_date and commit_date and commit_date > parsed_date:
        parts.append(
            sentence(
                f"Newer commits exist after this status (last commit: "
                f"{clean_cell(health['lastCommit'])}); trust git for the latest state"
            )
        )
    return " ".join(parts)


def compute_drift_warnings(status: dict[str, Any]) -> list[dict[str, Any]]:
    """Flag High-confidence projects whose curated narrative diverges from the parsed source.

    Parsed local task files are the trustworthy truth for a High project, so a curated field
    that disagrees is drift the operator should reconcile (or consciously keep). Story 4.1.
    """
    warnings: list[dict[str, Any]] = []
    for project in status.get("projects", []):
        if project.get("sourceConfidence") != "High":
            continue
        parse = project.get("taskParse") or {}
        for curated_key, parsed_key, label in DRIFT_FIELDS:
            narrative = project.get(curated_key)
            parsed = parse.get(parsed_key)
            if narrative and parsed and texts_disagree(narrative, parsed):
                warnings.append(
                    {
                        "project": project.get("name"),
                        "field": label,
                        "narrative": clean_cell(narrative),
                        "parsed": clean_cell(parsed),
                    }
                )
    return warnings


def build_data_flow(status: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "step": "1. Project paths",
            "source": "PROJECT-PATHS.md",
            "output": "Canonical local folders for RunSmart, Resumely, web support repos, and Agentic OS.",
        },
        {
            "step": "2. Local evidence",
            "source": "git status/log plus tasks/MEMORY.md, tasks/todo.md, tasks/session-log.md, docs/specs/README.md",
            "output": "Dirty flags, branch state, last commit, source files read, blockers, and next actions.",
        },
        {
            "step": "3. Shared contract",
            "source": "dashboard/status.json",
            "output": "projects, projectHealth, executiveOverview, projectPrompts, dailyRunResult, agentQueue, decisions, QA, metrics, and runCenter.",
        },
        {
            "step": "4. Localhost dashboards",
            "source": "dashboard/*.html",
            "output": "Command Center, Project Status, Orchestration, Executive, Decisions, Metrics, and Data Flow pages.",
        },
        {
            "step": "5. Delegation",
            "source": "dailyRunResult plus copy-ready prompts",
            "output": "Paste the recommended prompt inside the right project repo to make one concrete progress step.",
        },
    ]


def build_daily_run_result(
    status: dict[str, Any],
    project_prompts: list[dict[str, Any]],
    command: str,
    port: int,
    checks_status: str,
) -> dict[str, Any]:
    recommended = select_recommended_prompt(status, project_prompts)
    next_actions = build_founder_next_actions(status)
    contradictions = status.get("contradictions") or []
    top_banner = None
    confirm_prompt = None
    if contradictions:
        top_banner = "⚠️ Status contradicts reality"
        confirm_prompt = (
            "Ground truth disagrees with declared status. Confirm to update the affected "
            "tasks/progress.md entries. No auto-write was performed."
        )
    return {
        "lastCommand": command,
        "lastRunAt": now_label(),
        "checksStatus": checks_status,
        "checksCompletedAt": "",
        "localhostUrl": portfolio_hq_url(port),
        "recommendedPromptProject": recommended.get("project", "No project prompt available"),
        "recommendedPromptRole": recommended.get("role", "Project Operator"),
        "recommendedPrompt": recommended.get("copyPrompt", "Run ./agentic-os refresh to generate project prompts."),
        "targetRepoState": recommended.get("repoState", "Unknown"),
        "targetBranch": recommended.get("branch", "Unknown"),
        "readyForNextSession": checks_status == "Passed",
        "summary": status.get("summary", {}).get("bestNextAction", "Run the morning loop and choose the next project prompt."),
        "nextActions": next_actions,
        "topBanner": top_banner,
        "contradictionCount": len(contradictions),
        "confirmProposedFix": confirm_prompt,
    }


def parse_latest_coo_review(root: Path) -> dict[str, Any] | None:
    path = root / "executive-os" / "COO-LATEST-REVIEW.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8", errors="replace")
    return {
        "reviewed": _metadata_value(text, "Reviewed"),
        "selectedNextAction": _metadata_value(text, "Selected next action"),
        "actionType": _metadata_value(text, "Action type"),
        "source": _metadata_value(text, "Source"),
        "revisitWhen": _metadata_value(text, "Revisit when"),
        "path": str(path.relative_to(root)),
    }


def build_founder_next_actions(status: dict[str, Any]) -> list[dict[str, str]]:
    contradictions = status.get("contradictions") or []
    if contradictions:
        first = contradictions[0].get("message", "Ground truth contradiction detected.")
        return [{
            "title": "Resolve contradiction before execution",
            "detail": first,
            "type": "system",
            "where": "Agentic OS repo",
            "copyPrompt": "Confirm the contradiction fix to update status docs manually (one-tap confirm, no auto-write).",
        }]

    trust = status.get("portfolioTrust", {})
    if trust.get("level") == "refresh_required":
        return [{
            "title": "Restore dashboard trust",
            "detail": "Fix the sync or freshness warning, then run ./agentic-os morning again.",
            "type": "system",
        }]

    actions: list[dict[str, str]] = []
    apps_in_review = [
        project["name"]
        for project in status.get("projectHealth", [])
        if project.get("id") in APP_IDS and "review" in (project.get("state") or "").lower()
    ]
    if apps_in_review:
        actions.append({
            "title": "Check App Store Connect",
            "detail": f"Check {', '.join(apps_in_review)}. If Apple has not responded, do not change the submitted builds.",
            "type": "manual-founder",
            "where": "App Store Connect",
            "copyPrompt": None,
        })

    active_packets = [
        packet for packet in status.get("executiveLoop", {}).get("workPackets", [])
        if _packet_is_active(packet)
    ]
    if active_packets:
        packet = active_packets[0]
        actions.append({
            "title": f"Run active packet: {packet.get('title', 'work packet')}",
            "detail": f"Copy it into {packet.get('repoId') or 'the target repo'} and execute one focused session.",
            "type": "local-repo",
            "where": packet.get("repoPath") or packet.get("repoId") or "Target product repo",
            "copyPrompt": packet.get("copyPrompt"),
        })
    else:
        review = status.get("latestCooReview") or {}
        reviewed = parse_date(review.get("reviewed"))
        fresh_review = bool(reviewed and reviewed.date() == datetime.now().date())
        selected_action = review.get("selectedNextAction") or ""
        if fresh_review and selected_action and not selected_action.lower().startswith("completed"):
            actions.append({
                "title": "Continue the COO-selected action",
                "detail": selected_action,
                "type": review.get("actionType") or "global-OS",
                "where": "Agentic OS repo, in this Codex thread",
                "copyPrompt": (
                    "Continue the latest COO-selected action. Read "
                    "executive-os/COO-LATEST-REVIEW.md and the Source file named there. "
                    "Execute only the selected next action. Do not publish, email, deploy, "
                    "submit, or touch product code without explicit approval."
                ),
            })
        elif status.get("planExecution", {}).get("needsNextPacket", 0):
            actions.append({
                "title": "Run a COO operating review",
                "detail": "Choose the next milestone from plans marked Needs next packet. Create at most one packet.",
                "type": "global-OS",
                "where": "Agentic OS repo, in this Codex thread",
                "copyPrompt": "Run the COO operating review using PROMPTS/coo-operating-review.md.",
            })

    if len(actions) < 3:
        actions.append({
            "title": "Use the Weekly CEO Review only for a priority choice",
            "detail": "Run it when launch preparation, product work, and a side project genuinely compete for focus.",
            "type": "executive",
            "where": "Agentic OS repo, in this Codex thread",
            "copyPrompt": "Run the Weekly Executive Review using PROMPTS/executive-weekly-review.md.",
        })
    if trust.get("level") == "caution" and len(actions) < 3:
        reason = (trust.get("reasons") or ["Validate risky claims before acting."])[0]
        actions.append({
            "title": "Validate caution items before risky moves",
            "detail": reason,
            "type": "system",
            "where": "Affected product repo(s)",
            "copyPrompt": None,
        })
    return actions[:3]


def select_recommended_prompt(status: dict[str, Any], project_prompts: list[dict[str, Any]]) -> dict[str, Any]:
    if not project_prompts:
        return {}
    next_action = status.get("summary", {}).get("bestNextAction", "").lower()
    aliases = {
        "resumebuilder-ios": ["resumely", "resumebuilder ios", "resume builder ios"],
        "runsmart-ios": ["runsmart ios", "run smart ios"],
        "runsmart-web": ["runsmart web", "run smart web"],
        "resumebuilder-ai": ["resumebuilder web", "resumebuilder ai", "resume builder web"],
        "agentic-os": ["agentic os", "command center"],
    }
    ranked: list[tuple[int, dict[str, Any]]] = []
    for prompt in project_prompts:
        terms = [prompt.get("project", "").lower(), prompt.get("projectId", "").lower()]
        terms.extend(aliases.get(prompt.get("projectId", ""), []))
        positions = [next_action.find(term) for term in terms if term and term in next_action]
        if positions:
            ranked.append((min(positions), prompt))
    if ranked:
        return sorted(ranked, key=lambda item: item[0])[0][1]
    return project_prompts[0]


def update_status_json(port: int = 8787, command: str = "./agentic-os refresh") -> dict[str, Any]:
    status = read_json(STATUS_JSON)
    evidence = collect_evidence()
    project_health = project_health_from(evidence, status)
    parse_by_id = {item.project_id: item.task_parse for item in evidence}
    sources = sorted({f"{item.name}: {src}" for item in evidence for src in item.source_files})
    generated = today_idt()

    status.setdefault("metadata", {})
    status["metadata"]["lastUpdated"] = f"{generated} IDT"
    status["metadata"]["lastSuccessfulRefresh"] = now_label()
    status["metadata"]["sourcePolicy"] = (
        "Local folder mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, "
        "task memory/todo/session files, and existing dashboard status. No external dashboards queried."
    )

    status["runCenter"] = {
        "lastRefresh": now_label(),
        "command": command,
        "localhostUrl": portfolio_hq_url(port),
        "sourcesRead": sources,
        "checksRun": [
            "parser unit tests",
            "dashboard/status.json parsed",
            "embedded dashboard JSON parsed",
            "project-status.html fallback sync checked",
            "source confidence and freshness validated",
            "drift warnings checked",
            "git diff --check",
        ],
        "safeMode": "No App Store, billing, production, email, or external service action is triggered.",
        "synthesisNote": "One process: `./agentic-os morning` refreshes evidence, surfaces every saved plan, rebuilds the brief from repo truth, updates the HTML, verifies, and serves localhost. No separate synthesis step.",
    }
    status["projectHealth"] = project_health

    # ONE process, ONE source of truth. The headline, priority board, and blockers are ALWAYS
    # rebuilt from parsed repo truth (each repo's tasks/progress.md + every saved plan) on every
    # run. There is no hand-written overlay to go stale and no separate "write the brief" step.
    # Trust = the dashboard is literally the repos, re-derived each time `./agentic-os morning` runs.
    saved_plans = build_saved_plans(project_health)
    status["savedPlans"] = saved_plans
    registry = build_os_registry(ROOT)
    status["osRegistry"] = registry
    status["decisions"] = parse_decisions(ROOT)
    status["executiveLoop"] = build_executive_loop(status["decisions"], registry, ROOT)
    status["repoIntegrity"] = check_repo_integrity(ROOT)
    status["planExecution"] = build_plan_execution_status(
        saved_plans, registry.get("workPackets", []), ROOT
    )
    status["packetHygiene"] = build_packet_hygiene(status, ROOT)
    stranded_items: list[dict[str, str]] = []
    for item in evidence:
        stranded_items.extend(summarize_stranded_work(item.name, item.stranded, item.dirty_count))
    actionable = [i for i in stranded_items if i["type"] != "cleanup"]
    status["strandedWork"] = {
        "generatedOn": generated,
        "items": stranded_items,
        "actionableCount": len(actionable),
        "note": (
            "Work that exists only on this machine or only on a side branch/worktree. "
            "Anything listed here is at risk of being forgotten. Rebuilt every refresh "
            "from git; never hand-edit."
        ),
    }
    status["groundTruth"] = build_ground_truth(evidence, project_health)
    status["contradictions"] = status["groundTruth"].get("contradictions", [])
    status["latestCooReview"] = parse_latest_coo_review(ROOT)
    status["portfolioTrust"] = build_portfolio_trust(
        project_health,
        status["repoIntegrity"],
        status["runCenter"],
        status["planExecution"],
        status.get("contradictions"),
    )
    derived = build_derived_summary(project_health, saved_plans, status["planExecution"])
    freshest_dates = [parse_date(p.get("freshestDate")) for p in project_health]
    freshest = max([d for d in freshest_dates if d], default=None)
    summary = status.setdefault("summary", {})
    summary["overallStatus"] = derived["overallStatus"]
    summary["bestNextAction"] = derived["bestNextAction"]
    summary["mainBlockers"] = derived["mainBlockers"]
    summary["evidenceFreshDate"] = freshest.strftime("%Y-%m-%d") if freshest else None
    summary["generatedFrom"] = "Parsed local repo truth (tasks/progress.md) + every saved plan/spec/GTM. One process, re-derived each run."
    # Retire the old two-mode fields so nothing downstream can resurrect the dual process.
    for stale_key in ("synthesisMode", "derived", "synthesizedOn"):
        summary.pop(stale_key, None)
    # The priority board is always rebuilt from parsed truth (a board of facts, not prose).
    status["priorityBoard"] = derived["priorityBoard"]

    status["agentQueue"] = DEFAULT_AGENT_QUEUE
    status["projectPrompts"] = build_project_prompts(status, project_health)
    status["executiveOverview"] = build_executive_overview(status, project_health)
    status["dataFlow"] = build_data_flow(status)
    status["dailyRunResult"] = build_daily_run_result(
        status=status,
        project_prompts=status["projectPrompts"],
        command=command,
        port=port,
        checks_status="Pending verify",
    )

    for project in status.get("projects", []):
        parse = parse_by_id.get(project.get("id"))
        if parse is not None:
            project["taskParse"] = parse
        health = next((p for p in project_health if p["id"] == project.get("id")), None)
        if not health:
            # Conceptual or path-less project (e.g. Atlas): no local source to parse.
            project["sourceConfidence"] = resolve_confidence(
                parse or empty_task_parse(), project, exists=False
            )
            continue
        project["sourceConfidence"] = health["sourceConfidence"]
        project["freshness"] = health["freshness"]
        project["lastUpdated"] = generated
        project["gtm"] = health.get("gtm") or {"exists": False}

        # Auto-drive the displayed per-project narrative from parsed repo truth whenever a
        # parse exists (High: tasks/progress.md with validation evidence; Medium: derived
        # from todo/session-log). This is the core trust fix: a project card can no longer
        # show prose the repo contradicts, and the long-form status field is rebuilt every
        # run so stale narrative cannot accrete across refreshes.
        if (
            health["sourceConfidence"] in ("High", "Medium")
            and parse
            and any(parse.get(k) for k in ("currentPhase", "activeStory", "lastCompletedStory"))
        ):
            for display_key, parsed_key in [
                ("currentPhase", "currentPhase"),
                ("activeStory", "activeStory"),
                ("nextRecommendedStory", "nextRecommendedStory"),
                ("lastCompletedStory", "lastCompletedStory"),
                ("lastValidation", "lastValidation"),
            ]:
                value = parse.get(parsed_key)
                if value:
                    project[display_key] = value
            project["blockers"] = health.get("blockers") or []
            project["status"] = compose_status_narrative(parse, health)

        project["localEvidence"] = {
            "branch": health["branch"],
            "dirty": health["dirty"],
            "dirtyCount": health["dirtyCount"],
            "extraWorktrees": health["extraWorktrees"],
            "lastCommit": health["lastCommit"],
            "sourceFiles": health["sourceFiles"],
            "sourceConfidence": health["sourceConfidence"],
            "preferredSource": health["preferredSource"],
            "freshness": health["freshness"],
            "freshestDate": health["freshestDate"],
            "evidenceGap": health["evidenceGap"],
            "evidenceDate": health["evidenceDate"],
        }

    drift_warnings = compute_drift_warnings(status)
    status["driftWarnings"] = drift_warnings
    status["executiveOverview"]["driftWarningCount"] = len(drift_warnings)
    status["executiveOverview"]["driftProjects"] = sorted({w["project"] for w in drift_warnings})

    # Decisions and open questions sourced from the repos themselves (not hand-curated).
    open_questions: list[dict[str, Any]] = []
    repo_decisions: list[dict[str, Any]] = []
    for project in status.get("projects", []):
        parse = project.get("taskParse") or {}
        for question in parse.get("openQuestions", []):
            open_questions.append({"project": project.get("name"), "question": question})
        for decision in parse.get("decisionsNeeded", []):
            repo_decisions.append({"project": project.get("name"), "decision": decision})
    status["openQuestionsBoard"] = open_questions
    status["repoDecisions"] = repo_decisions
    status["executiveOverview"]["openQuestionCount"] = len(open_questions)
    status["executiveOverview"]["repoDecisionCount"] = len(repo_decisions)

    write_json(STATUS_JSON, status)
    sync_project_status_fallback(status)
    write_project_status(status)
    write_dashboard(status)
    write_executive_dashboard(status)
    update_command_center_generated(generated, status)
    update_orchestration_generated(status)
    return status


def mark_daily_run_verified(port: int, passed: bool) -> None:
    status = read_json(STATUS_JSON)
    result = status.setdefault("dailyRunResult", {})
    result["checksStatus"] = "Passed" if passed else "Failed"
    result["checksCompletedAt"] = now_label()
    result["readyForNextSession"] = passed
    result["localhostUrl"] = portfolio_hq_url(port)
    write_json(STATUS_JSON, status)
    sync_project_status_fallback(status)
    update_command_center_generated(today_idt(), status)


def sync_project_status_fallback(status: dict[str, Any] | None = None) -> None:
    if status is None:
        status = read_json(STATUS_JSON)
    source = json.dumps(status, indent=2)
    html = PROJECT_STATUS_HTML.read_text(encoding="utf-8")
    html = re.sub(
        r'(<script id="status-data" type="application/json">\n).*?(\n    </script>)',
        lambda m: m.group(1) + source + m.group(2),
        html,
        count=1,
        flags=re.S,
    )
    PROJECT_STATUS_HTML.write_text(html, encoding="utf-8")


def update_command_center_generated(generated: str, status: dict[str, Any]) -> None:
    for path in [INDEX_HTML, COMMAND_CENTER_HTML]:
        html = path.read_text(encoding="utf-8")
        match = re.search(r'(<script id="cc-data" type="application/json">\n)(.*?)(\n    </script>)', html, flags=re.S)
        if not match:
            continue
        data = json.loads(match.group(2))
        data["generated"] = generated
        data["fallbackStatus"] = {
            "summary": status.get("summary", {}),
            "priorityBoard": status.get("priorityBoard", {}),
            "runCenter": status.get("runCenter", {}),
            "projectHealth": status.get("projectHealth", []),
            "agentQueue": status.get("agentQueue", []),
            "projectPrompts": status.get("projectPrompts", []),
            "executiveOverview": status.get("executiveOverview", {}),
            "dataFlow": status.get("dataFlow", []),
            "driftWarnings": status.get("driftWarnings", []),
            "savedPlans": status.get("savedPlans", []),
            "osRegistry": status.get("osRegistry", {}),
            "decisions": status.get("decisions", []),
            "executiveLoop": status.get("executiveLoop", {}),
            "repoIntegrity": status.get("repoIntegrity", {}),
            "portfolioTrust": status.get("portfolioTrust", {}),
            "groundTruth": status.get("groundTruth", {}),
            "contradictions": status.get("contradictions", []),
            "dailyRunResult": status.get("dailyRunResult", {}),
            "planExecution": status.get("planExecution", {}),
            "packetHygiene": status.get("packetHygiene", []),
            "openQuestionsBoard": status.get("openQuestionsBoard", []),
            "repoDecisions": status.get("repoDecisions", []),
        }
        html = html[: match.start()] + match.group(1) + json.dumps(data, indent=2) + match.group(3) + html[match.end() :]
        path.write_text(html, encoding="utf-8")


def update_orchestration_generated(status: dict[str, Any]) -> None:
    html = ORCHESTRATION_HTML.read_text(encoding="utf-8")
    match = re.search(r'(<script id="os-data" type="application/json">\n)(.*?)(\n    </script>)', html, flags=re.S)
    if not match:
        return
    data = json.loads(match.group(2))
    data["generated"] = status.get("runCenter", {}).get("lastRefresh") or status.get("metadata", {}).get("lastUpdated", today_idt())
    html = html[: match.start()] + match.group(1) + json.dumps(data, indent=2) + match.group(3) + html[match.end() :]
    ORCHESTRATION_HTML.write_text(html, encoding="utf-8")


def write_project_status(status: dict[str, Any]) -> None:
    contradictions = status.get("contradictions") or []
    lines = [
        "# Project Status",
        "",
        f"Last updated: {status['metadata']['lastUpdated']}",
        "",
        "Source policy: local folder mode. Generated by `./agentic-os refresh` from local project paths, git state, task files, and `dashboard/status.json`. No external production dashboards were queried.",
        "",
        "## Contradictions vs Ground Truth",
        "",
    ]
    if contradictions:
        lines.append("⚠️ Status contradicts reality. Treat freshness as secondary until these are reconciled:")
        lines.append("")
        for item in contradictions:
            lines.append(f"- [{item.get('severity', 'warning').upper()}] {clean_cell(item.get('message', ''))}")
        proposal = status.get("groundTruth", {}).get("proposedFix")
        if proposal:
            lines += ["", f"- Proposed fix (confirm first): {proposal}"]
    else:
        lines.append("None. No contradictions were detected between declared state and ground truth checks.")

    lines += [
        "",
        "## Status Table",
        "",
        "Confidence is parsed from local task files: High = task file parsed with validation "
        "evidence; Medium = task file parsed, validation unclear; Low = no task files, dashboard "
        "narrative only; Unknown = no reliable source. Stale evidence (newest signal older than "
        "7 days) downgrades confidence one level.",
        "",
        "| Project | State | Next Action | Blockers | Dirty | Freshness | Confidence | Source | Last Commit |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for p in status.get("projectHealth", []):
        lines.append(
            f"| {p['name']} | {clean_cell(p['state'])} | {clean_cell(p['nextAction'])} | {p['blockerCount']} | "
            f"{'Yes (' + str(p['dirtyCount']) + ')' if p['dirty'] else 'No'} | "
            f"{clean_cell(p.get('freshness', 'Unknown'))} | "
            f"{clean_cell(p.get('sourceConfidence', 'Unknown'))} | {clean_cell(p.get('preferredSource', 'none'))} | "
            f"{clean_cell(p['lastCommit'])} |"
        )

    gaps = [p for p in status.get("projectHealth", []) if p.get("evidenceGap")]
    lines += ["", "## Evidence Gaps", ""]
    if gaps:
        lines.append("Latest commit post-dates the last validation (code moved since the last proof):")
        lines.append("")
        for p in gaps:
            lines.append(
                f"- {p['name']}: validated {p.get('evidenceDate') or 'unknown'}, "
                f"last commit {clean_cell(p['lastCommit'])}"
            )
    else:
        lines.append("None. Every project's validation is at least as recent as its last commit.")

    drift = status.get("driftWarnings", [])
    lines += ["", "## Drift Warnings", ""]
    if drift:
        lines.append(
            "High-confidence projects whose curated narrative differs from the parsed local "
            "source. Reconcile the dashboard field or confirm the narrative is intentional:"
        )
        lines.append("")
        for warning in drift:
            lines.append(
                f"- {warning['project']} ({warning['field']}): narrative = "
                f"\"{warning['narrative']}\" / parsed = \"{warning['parsed']}\""
            )
    else:
        lines.append("None. Curated narrative matches the parsed source for all High-confidence projects.")

    stranded = status.get("strandedWork", {}).get("items", [])
    lines += ["", "## Stranded Work", ""]
    if stranded:
        lines.append(
            "Commits, branches, and worktrees that exist only locally or only on a side "
            "branch. Every item here is at risk of being lost. Push + PR, hand off "
            "explicitly, or consciously discard:"
        )
        lines.append("")
        for item in stranded:
            lines.append(
                f"- [{item['project']}] {clean_cell(item['detail'])} -> {clean_cell(item['action'])}"
            )
    else:
        lines.append("None. Every branch is pushed, every worktree is clean and accounted for.")

    packet_hygiene = status.get("packetHygiene", [])
    lines += ["", "## Work Packet Hygiene", ""]
    if packet_hygiene:
        lines.append("Packet states that may make the dashboard misleading:")
        lines.append("")
        for item in packet_hygiene:
            lines.append(
                f"- {item.get('severity', 'warning').upper()} [{clean_cell(item.get('path', ''))}]: "
                f"{clean_cell(item.get('message', ''))}"
            )
    else:
        lines.append("None. Active/open packet states match the current project status.")

    questions = status.get("openQuestionsBoard", [])
    repo_decisions = status.get("repoDecisions", [])
    lines += ["", "## Open Questions & Decisions (from repos)", ""]
    if questions or repo_decisions:
        for item in repo_decisions:
            lines.append(f"- Decision needed [{item['project']}]: {clean_cell(item['decision'])}")
        for item in questions:
            lines.append(f"- Open question [{item['project']}]: {clean_cell(item['question'])}")
    else:
        lines.append(
            "None surfaced from repos yet. Add a `## Open Questions` or `## Decisions Needed` "
            "section (bullet items) to a project's task files to surface them here."
        )

    lines += [
        "",
        "## Morning Brief",
        "",
        status.get("summary", {}).get("overallStatus", "No summary available."),
        "",
        "## What To Do Next",
        "",
        status.get("summary", {}).get("bestNextAction", "Refresh status and choose the next action."),
        "",
        "## Action Board",
        "",
    ]
    for key, title in [("now", "Now"), ("next", "Next"), ("later", "Later"), ("blocked", "Blocked")]:
        lines += [f"### {title}", ""]
        items = status.get("priorityBoard", {}).get(key, [])
        lines += [f"- {item}" for item in items] or ["- None listed."]
        lines.append("")

    lines += ["## Agent Queue", ""]
    for item in status.get("agentQueue", []):
        lines.append(f"- **{item['role']}** - {item['task']}")
    lines += ["", "## Sources Read", ""]
    sources = status.get("runCenter", {}).get("sourcesRead", [])
    lines += [f"- {src}" for src in sources] or ["- No source files recorded."]
    lines.append("")
    (ROOT / "PROJECT-STATUS.md").write_text("\n".join(lines), encoding="utf-8")


def write_dashboard(status: dict[str, Any]) -> None:
    contradictions = status.get("contradictions") or []
    lines = [
        "# Portfolio Dashboard",
        "",
        f"Last updated: {status['metadata']['lastUpdated']}",
        "",
        status["metadata"]["sourcePolicy"],
        "",
    ]
    if contradictions:
        lines += [
            "## ⚠️ Status Contradicts Reality",
            "",
        ]
        for item in contradictions:
            lines.append(f"- [{item.get('severity', 'warning').upper()}] {clean_cell(item.get('message', ''))}")
        proposal = status.get("groundTruth", {}).get("proposedFix")
        if proposal:
            lines += ["", f"- Proposed fix (confirm before write): {proposal}"]
        lines.append("")

    lines += [
        "## Executive Summary",
        "",
        status.get("summary", {}).get("overallStatus", "No summary available."),
        "",
        f"Best next action: {status.get('summary', {}).get('bestNextAction', 'Refresh status.')}",
        "",
        "## Run Center",
        "",
        f"- Last refresh: {status.get('runCenter', {}).get('lastRefresh', 'Unknown')}",
        f"- Localhost: `{status.get('runCenter', {}).get('localhostUrl', 'Unknown')}`",
        f"- Safe mode: {status.get('runCenter', {}).get('safeMode', 'Unknown')}",
        "",
        "## Project Health",
        "",
        "| Project | State | Next Action | Dirty | Freshness | Confidence |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for p in status.get("projectHealth", []):
        lines.append(
            f"| {p['name']} | {clean_cell(p['state'])} | {clean_cell(p['nextAction'])} | "
            f"{'Yes' if p['dirty'] else 'No'} | {clean_cell(p.get('freshness', 'Unknown'))} | "
            f"{clean_cell(p.get('sourceConfidence', 'Unknown'))} |"
        )

    stranded = status.get("strandedWork", {}).get("items", [])
    actionable = [i for i in stranded if i.get("type") != "cleanup"]
    lines += ["", "## Stranded Work", ""]
    if actionable:
        lines.append(
            f"{len(actionable)} item(s) at risk of being lost (full list with actions "
            "in PROJECT-STATUS.md):"
        )
        lines.append("")
        for item in actionable:
            lines.append(f"- [{item['project']}] {clean_cell(item['detail'])}")
    else:
        lines.append("None. Every branch is pushed and every worktree is accounted for.")

    packet_hygiene = status.get("packetHygiene", [])
    lines += ["", "## Work Packet Hygiene", ""]
    if packet_hygiene:
        for item in packet_hygiene:
            lines.append(
                f"- {item.get('severity', 'warning').upper()} [{clean_cell(item.get('path', ''))}]: "
                f"{clean_cell(item.get('message', ''))}"
            )
    else:
        lines.append("- None. Active/open packet states match the current project status.")

    lines += [
        "",
        "## Decision Board",
        "",
        "| Decision | Project | Recommendation | Urgency |",
        "| --- | --- | --- | --- |",
    ]
    for decision in status.get("decisionBoard", []):
        lines.append(
            f"| {clean_cell(decision.get('decision', ''))} | {clean_cell(decision.get('project', ''))} | "
            f"{clean_cell(decision.get('recommendedOption', ''))} | {clean_cell(decision.get('urgency', ''))} |"
        )

    lines += ["", "## Agent Delegation", ""]
    for item in status.get("agentQueue", []):
        lines.append(f"- **{item['role']}**: {item['task']} Evidence: {item['evidence']}")
    gaps = [p for p in status.get("projectHealth", []) if p.get("evidenceGap")]
    lines += ["", "## Evidence Gaps", ""]
    if gaps:
        for p in gaps:
            lines.append(f"- {p['name']}: validated {p.get('evidenceDate') or 'unknown'}, latest commit is newer.")
    else:
        lines.append("- None. Every project's validation is at least as recent as its last commit.")

    drift = status.get("driftWarnings", [])
    lines += ["", "## Drift Warnings", ""]
    if drift:
        for warning in drift:
            lines.append(f"- {warning['project']} ({warning['field']}): curated narrative differs from parsed source.")
    else:
        lines.append("- None. Curated narrative matches the parsed source for all High-confidence projects.")

    lines += ["", "## Validation", ""]
    lines += [f"- {check}" for check in status.get("runCenter", {}).get("checksRun", [])]
    lines.append("")
    (ROOT / "DASHBOARD.md").write_text("\n".join(lines), encoding="utf-8")


def write_executive_dashboard(status: dict[str, Any]) -> None:
    weekly_review = ROOT / "executive-os" / "WEEKLY-CEO-LATEST.md"
    if weekly_review.exists():
        reviewed = parse_date(_metadata_value(weekly_review.read_text(encoding="utf-8"), "Reviewed"))
        if reviewed is not None:
            review_age = (datetime.now() - reviewed).days
            if 0 <= review_age <= FRESHNESS_REVIEW_DAYS:
                return

    executive = status.get("executiveBoard", {})
    lines = [
        "# Executive Dashboard",
        "",
        "Manual source-of-truth dashboard for the Executive Intelligence OS. Financial cells stay `Needs Data` until a real source exists.",
        "",
        f"Last updated: {status['metadata']['lastUpdated']}",
        "",
        "## Executive Summary",
        "",
        status.get("summary", {}).get("overallStatus", "No summary available."),
        "",
        "## CEO Focus",
        "",
    ]
    lines += [f"- {item}" for item in executive.get("top3", [])] or ["- Refresh status and choose the next focus."]
    lines += [
        "",
        "## Financial Snapshot",
        "",
        f"{executive.get('financialSnapshot', 'Needs Data - no revenue/cost instrumentation wired.')}",
        "",
        "## Open Decisions",
        "",
    ]
    lines += [f"- {item}" for item in executive.get("openDecisions", [])] or ["- None listed."]
    lines += [
        "",
        "## Status Confidence",
        "",
        "How much each project's state is backed by parsed local task files versus narrative only.",
        "",
        "| Project | Confidence | Source | Last Validation |",
        "| --- | --- | --- | --- |",
    ]
    for p in status.get("projectHealth", []):
        lines.append(
            f"| {p['name']} | {clean_cell(p.get('sourceConfidence', 'Unknown'))} | "
            f"{clean_cell(p.get('preferredSource', 'none'))} | "
            f"{clean_cell(p.get('parsedLastValidation') or 'Not parsed')} |"
        )
    lines += ["", "## Risk Board", ""]
    for blocker in status.get("summary", {}).get("mainBlockers", []):
        lines.append(f"- {blocker}")
    lines += ["", "## Next Recommended Actions", ""]
    for item in status.get("priorityBoard", {}).get("now", []):
        lines.append(f"1. {item}")
    lines.append("")
    (ROOT / "executive-os" / "EXECUTIVE-DASHBOARD.md").write_text("\n".join(lines), encoding="utf-8")


def clean_cell(value: Any) -> str:
    return str(value).replace("|", "/").replace("\n", " ").strip()


def extract_json_script(path: Path, script_id: str) -> Any | None:
    text = path.read_text(encoding="utf-8")
    match = re.search(
        rf'<script id="{re.escape(script_id)}" type="application/json">\n(.*?)\n\s*</script>',
        text,
        flags=re.S,
    )
    if not match:
        return None
    return json.loads(match.group(1))


def verify_links() -> list[str]:
    errors: list[str] = []
    html_files = [
        INDEX_HTML,
        PROJECT_STATUS_HTML,
        COMMAND_CENTER_HTML,
        ORCHESTRATION_HTML,
        DASHBOARD / "executive.html",
        DASHBOARD / "data-flow.html",
    ]
    literal_href = re.compile(r'href="([^"]+)"')
    for html_file in html_files:
        html = html_file.read_text(encoding="utf-8")
        hrefs = literal_href.findall(html)
        if html_file in [INDEX_HTML, COMMAND_CENTER_HTML]:
            cc = extract_json_script(html_file, "cc-data") or {}
            for group in cc.get("groups", []):
                for item in group.get("items", []):
                    for link in item.get("links", []):
                        hrefs.append(link.get("href", ""))
        for href in hrefs:
            if not href or href.startswith(("#", "http:", "https:", "file:", "mailto:")):
                continue
            target = (html_file.parent / href).resolve()
            if not target.exists():
                errors.append(f"{html_file.relative_to(ROOT)} -> missing link {href}")
    return errors


def run_tests(verbosity: int = 2) -> bool:
    """Run the parser unit suite (scripts/agentic_os/test_cli.py) in-process."""
    import io
    import unittest

    if str(SCRIPT_DIR) not in sys.path:
        sys.path.insert(0, str(SCRIPT_DIR))
    loader = unittest.TestLoader()
    try:
        suite = loader.loadTestsFromName("test_cli")
    except Exception as exc:  # noqa: BLE001 - surface any import/collection failure
        print(f"could not load parser tests: {exc}")
        return False
    stream = sys.stderr if verbosity >= 2 else io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=verbosity).run(suite)
    return result.wasSuccessful()


def verify() -> int:
    errors: list[str] = []
    status = read_json(STATUS_JSON)
    if not run_tests(verbosity=0):
        errors.append("parser unit tests failed (run ./agentic-os test for detail)")
    if extract_json_script(INDEX_HTML, "cc-data") is None:
        errors.append("dashboard/index.html missing parseable cc-data JSON")
    project_status = extract_json_script(PROJECT_STATUS_HTML, "status-data")
    if project_status != status:
        errors.append("dashboard/project-status.html embedded status-data is not synced with dashboard/status.json")
    if extract_json_script(COMMAND_CENTER_HTML, "cc-data") is None:
        errors.append("dashboard/command-center.html missing parseable cc-data JSON")
    if extract_json_script(ORCHESTRATION_HTML, "os-data") is None:
        errors.append("dashboard/orchestration.html missing parseable os-data JSON")

    allowed_confidence = {"High", "Medium", "Low", "Unknown"}
    allowed_freshness = {"Fresh", "Needs Review", "Stale", "Unknown"}
    for health in status.get("projectHealth", []):
        confidence = health.get("sourceConfidence")
        if confidence not in allowed_confidence:
            errors.append(
                f"projectHealth '{health.get('name', '?')}' has invalid sourceConfidence: {confidence!r}"
            )
        freshness = health.get("freshness")
        if freshness not in allowed_freshness:
            errors.append(
                f"projectHealth '{health.get('name', '?')}' has invalid freshness: {freshness!r}"
            )
        if not isinstance(health.get("evidenceGap"), bool):
            errors.append(
                f"projectHealth '{health.get('name', '?')}' has non-boolean evidenceGap: "
                f"{health.get('evidenceGap')!r}"
            )

    drift = status.get("driftWarnings")
    if not isinstance(drift, list):
        errors.append("driftWarnings missing or not a list")
    else:
        for warning in drift:
            if not all(key in warning for key in ("project", "field", "narrative", "parsed")):
                errors.append(f"driftWarnings entry missing required keys: {warning!r}")

    if not isinstance(status.get("openQuestionsBoard"), list):
        errors.append("openQuestionsBoard missing or not a list")
    if not isinstance(status.get("repoDecisions"), list):
        errors.append("repoDecisions missing or not a list")
    contradictions = status.get("contradictions")
    if not isinstance(contradictions, list):
        errors.append("contradictions missing or not a list")
    elif contradictions and status.get("portfolioTrust", {}).get("level") != "refresh_required":
        errors.append("portfolioTrust must be refresh_required when contradictions exist")
    if not isinstance(status.get("groundTruth"), dict):
        errors.append("groundTruth missing or not an object")
    packet_hygiene = status.get("packetHygiene")
    if not isinstance(packet_hygiene, list):
        errors.append("packetHygiene missing or not a list")
    else:
        for item in packet_hygiene:
            if not all(key in item for key in ("severity", "path", "message")):
                errors.append(f"packetHygiene entry missing required keys: {item!r}")
            if item.get("severity") == "error":
                errors.append(f"work packet hygiene error: {item.get('message')} ({item.get('path')})")
    for prompt in status.get("projectPrompts", []):
        if prompt.get("sourceConfidence") not in allowed_confidence:
            errors.append(
                f"projectPrompt '{prompt.get('project', '?')}' has invalid sourceConfidence: "
                f"{prompt.get('sourceConfidence')!r}"
            )
    for project in status.get("projects", []):
        if "taskParse" in project and project.get("sourceConfidence") not in allowed_confidence:
            errors.append(
                f"project '{project.get('name', '?')}' has invalid sourceConfidence: "
                f"{project.get('sourceConfidence')!r}"
            )

    errors.extend(verify_links())

    diff = run(["git", "diff", "--check"], cwd=ROOT)
    if diff.returncode != 0:
        errors.append(diff.stdout.strip() or diff.stderr.strip() or "git diff --check failed")

    if errors:
        print("verify failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("verify passed")
    print("- parser unit tests passed")
    print("- dashboard/status.json parsed")
    print("- embedded dashboard JSON parsed")
    print("- project-status.html fallback is synced")
    print("- source confidence and freshness values valid")
    print("- drift warnings well-formed")
    print("- work packet hygiene checked")
    print("- dashboard links resolve")
    print("- git diff --check passed")
    return 0


def find_port(start: int) -> int:
    port = start
    while port < start + 100:
        with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            if sock.connect_ex(("127.0.0.1", port)) != 0:
                return port
        port += 1
    raise RuntimeError("No free localhost port found")


def portfolio_hq_url(port: int) -> str:
    return f"http://127.0.0.1:{port}/{PORTFOLIO_HQ_PAGE}"


def serve(port: int, open_browser: bool = True) -> int:
    port = find_port(port)
    # Serve from dashboard/ so Portfolio HQ and its generated data stay together.
    # Content that lives outside dashboard/ (brainstorm, work packets) is read INTO status.json
    # by the parser and rendered inline, so there are no cross-directory links to break.
    os.chdir(DASHBOARD)
    handler = http.server.SimpleHTTPRequestHandler
    url = portfolio_hq_url(port)

    class ReusableTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    with ReusableTCPServer(("127.0.0.1", port), handler) as httpd:
        print(f"Portfolio HQ: {url}")
        print("Press Ctrl-C to stop.")
        if open_browser:
            webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped Agentic OS server.")
    return 0


def refresh(args: argparse.Namespace) -> int:
    hook_issues = check_hook_health()
    if hook_issues:
        print("⚠️ Hook health check")
        for issue in hook_issues:
            print(f"  - {issue}")
    status = update_status_json(port=args.port, command=f"./agentic-os {args.command}")
    contradictions = status.get("contradictions") or []
    if contradictions:
        print("⚠️ Status contradicts reality")
        for item in contradictions[:3]:
            print(f"  - {item.get('message')}")
        if status.get("groundTruth", {}).get("proposedFix"):
            print(f"  - proposed fix: {status['groundTruth']['proposedFix']}")
    print("refreshed Agentic OS")
    print(f"- last refresh: {status['runCenter']['lastRefresh']}")
    print("- brief: rebuilt from parsed repo truth (one process, always current).")
    reg = status.get("osRegistry", {})
    leaders = [o["name"] for o in reg.get("leadership", [])]
    print(f"- Executive OS (leadership): {', '.join(leaders) if leaders else 'none found'}")
    print(
        f"- work packets: {len(reg.get('workPackets', []))}"
        f" | outcome loops: {len(reg.get('outcomeLoops', []))}"
        f" | context checkpoints: {len(reg.get('contextCheckpoints', []))}"
        f" | skill agents (builders): {len(reg.get('skillAgents', []))}"
        f" | plugins: {len(reg.get('plugins', []))}"
    )
    decisions = status.get("decisions", [])
    open_d = [d for d in decisions if d.get("status", "").lower().startswith("open")]
    print(f"- decisions: {len(open_d)} open of {len(decisions)} logged (decisions -> work packets)")
    integ = status.get("repoIntegrity", {})
    if integ.get("synced"):
        print("- sync: CLEAN (on main, committed, no stray worktrees). All tools see the same truth.")
    else:
        print(f"- sync: ATTENTION — {' '.join(integ.get('notes', []))}")
    total_plans = sum(entry.get("total", 0) for entry in status.get("savedPlans", []))
    plan_projects = [f"{e['project']} ({e['total']})" for e in status.get("savedPlans", [])]
    print(f"- saved plans surfaced: {total_plans} across {len(status.get('savedPlans', []))} projects"
          + (f" — {', '.join(plan_projects)}" if plan_projects else ""))
    gtm_projects = [p["name"] for p in status.get("projectHealth", []) if (p.get("gtm") or {}).get("exists")]
    print(f"- GTM plans: {', '.join(gtm_projects) if gtm_projects else 'none found'}")
    print("- suggested next actions:")
    for index, action in enumerate(status.get("dailyRunResult", {}).get("nextActions", []), start=1):
        print(f"  {index}. {action.get('title')}: {action.get('detail')}")
    print("- sources read:")
    for source in status["runCenter"]["sourcesRead"]:
        print(f"  - {source}")
    drift = status.get("driftWarnings", [])
    if drift:
        print(f"- drift warnings ({len(drift)}): curated narrative differs from parsed source")
        for warning in drift:
            print(f"  - {warning['project']} ({warning['field']})")
    else:
        print("- drift warnings: none")
    stale_apps = [p["name"] for p in status.get("projectHealth", []) if p.get("freshness") == "Stale"]
    if stale_apps:
        print(f"- stale evidence: {', '.join(stale_apps)}")
    else:
        print("- stale evidence: none")
    ground = status.get("groundTruth") or {}
    queried = [row.get("appId") for row in ground.get("posthog", []) if row.get("source") == "api"]
    if queried:
        print(f"- ground truth: PostHog queried for {', '.join(queried)}")
    elif ground.get("unavailable"):
        print(f"- ground truth: unavailable ({'; '.join(ground.get('unavailable', [])[:2])})")
    else:
        print("- ground truth: local git + optional overrides only (no PostHog key)")
    refresh_portfolio_hq()
    refresh_daily_note()
    refresh_brain_map()
    return 0


def refresh_portfolio_hq() -> None:
    script = ROOT / "scripts" / "portfolio_hq" / "refresh_portfolio_hq.py"
    try:
        result = subprocess.run(
            [sys.executable, str(script)], capture_output=True, text=True, timeout=60
        )
    except subprocess.TimeoutExpired:
        print("⚠️ portfolio HQ refresh timed out (dashboard/portfolio-hq.html left as-is)")
        return
    if result.returncode == 0:
        print(result.stdout.strip())
    else:
        print("⚠️ portfolio HQ refresh failed (dashboard/portfolio-hq.html left as-is)")
        print(f"  - {result.stderr.strip() or result.stdout.strip()}")


def _run_vault_helper(script: Path, label: str) -> None:
    """Run a founder-approved vault helper; never fail the refresh over it."""
    try:
        result = subprocess.run(
            [sys.executable, str(script)], capture_output=True, text=True, timeout=60
        )
    except subprocess.TimeoutExpired:
        print(f"⚠️ {label} timed out (vault left as-is)")
        return
    if result.returncode == 0 and result.stdout.strip():
        print(result.stdout.strip())
    elif result.returncode != 0:
        print(f"⚠️ {label} failed (vault left as-is)")
        print(f"  - {result.stderr.strip() or result.stdout.strip()}")


def refresh_daily_note() -> None:
    """Pre-fill today's Builder OS journal note (founder-approved 2026-07-12)."""
    _run_vault_helper(ROOT / "scripts" / "agentic_os" / "daily_note.py", "daily note")


def refresh_brain_map() -> None:
    """Regenerate the vault Brain Map from real wikilinks (deterministic)."""
    _run_vault_helper(ROOT / "scripts" / "brain_map" / "generate_brain_map.py", "brain map")


def run_eod_close(force: bool = False) -> None:
    """Draft today's end-of-day close in the Builder OS daily note (evening rail)."""
    script = ROOT / "scripts" / "agentic_os" / "eod_close.py"
    argv = [str(script), "--force"] if force else [str(script)]
    _run_vault_helper_argv(argv, "eod close")


def _run_vault_helper_argv(argv: list[str], label: str) -> None:
    """Like _run_vault_helper but for a helper that takes CLI arguments."""
    try:
        result = subprocess.run(
            [sys.executable, *argv], capture_output=True, text=True, timeout=60
        )
    except subprocess.TimeoutExpired:
        print(f"⚠️ {label} timed out (vault left as-is)")
        return
    if result.returncode == 0 and result.stdout.strip():
        print(result.stdout.strip())
    elif result.returncode != 0:
        print(f"⚠️ {label} failed (vault left as-is)")
        print(f"  - {result.stderr.strip() or result.stdout.strip()}")


def doctor() -> int:
    issues: list[str] = []
    status = read_json(STATUS_JSON)
    metadata = status.get("metadata", {})
    last_success = parse_time_label(metadata.get("lastSuccessfulRefresh"))
    now = datetime.now()

    print("agentic-os doctor")
    print(f"- launchd label: {LAUNCHD_LABEL}")
    launchd = launchd_job_status(LAUNCHD_LABEL)
    if not launchd.get("loaded"):
        issues.append("launchd job is not loaded")
        print("- launchd: MISSING")
    else:
        print(
            f"- launchd: loaded, state={launchd.get('state')}, runs={launchd.get('runs')}, "
            f"lastExit={launchd.get('lastExitCode')}"
        )
        if launchd.get("lastExitCode") not in (0, None):
            issues.append(f"launchd last exit is {launchd.get('lastExitCode')} (expected 0)")
            if launchd.get("lastExitCode") == 126:
                print(
                    "- hint: exit 126 often means launchd cannot execute the repo script "
                    "(TCC/Full Disk Access). Use scripts/launchd-wrapper.sh via ~/.local/bin."
                )

    if not LAUNCHD_PLIST.exists():
        issues.append(f"missing plist at {LAUNCHD_PLIST}")
        print(f"- plist: missing {LAUNCHD_PLIST}")
    else:
        plist_text = LAUNCHD_PLIST.read_text(encoding="utf-8", errors="replace")
        run_at_load = "<key>RunAtLoad</key>" in plist_text and "<true/>" in plist_text.split("<key>RunAtLoad</key>", 1)[1][:80]
        print(f"- plist: found ({LAUNCHD_PLIST}) | RunAtLoad={'true' if run_at_load else 'false'}")
        if not run_at_load:
            issues.append("RunAtLoad is false (missed schedules will not catch up)")

    for tool in ("python3", "git"):
        ok = command_available(tool)
        print(f"- tool {tool}: {'OK' if ok else 'MISSING'}")
        if not ok:
            issues.append(f"{tool} not found in PATH")

    if last_success is None:
        issues.append("metadata.lastSuccessfulRefresh missing or invalid")
        print("- lastSuccessfulRefresh: missing")
    else:
        age_hours = (now - last_success).total_seconds() / 3600.0
        print(f"- lastSuccessfulRefresh: {metadata.get('lastSuccessfulRefresh')} ({age_hours:.1f}h ago)")
        if age_hours > 24:
            issues.append("lastSuccessfulRefresh is older than 24h")

    contradictions = status.get("contradictions") or []
    if contradictions:
        print(f"- contradictions: {len(contradictions)} (semantic — reconcile via morning brief; not an automation failure)")
        for item in contradictions[:2]:
            print(f"  - {item.get('message')}")
    else:
        print("- contradictions: none")

    if issues:
        print("doctor: FAIL")
        for issue in issues:
            print(f"  - {issue}")
        return 1
    print("doctor: PASS")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="./agentic-os", description="Local Agentic OS command center")
    sub = parser.add_subparsers(dest="command", required=True)

    morning = sub.add_parser("morning", help="refresh, verify, serve localhost, and open Portfolio HQ")
    morning.add_argument("--port", type=int, default=8787)
    morning.add_argument("--no-open", action="store_true", help="serve without opening a browser")

    refresh_cmd = sub.add_parser("refresh", help="refresh status files without serving")
    refresh_cmd.add_argument("--port", type=int, default=8787)

    serve_cmd = sub.add_parser("serve", help="serve the current dashboard")
    serve_cmd.add_argument("--port", type=int, default=8787)
    serve_cmd.add_argument("--no-open", action="store_true", help="serve without opening a browser")

    sub.add_parser("verify", help="verify dashboard JSON, fallback sync, links, and whitespace")
    sub.add_parser("test", help="run the parser unit tests")
    sub.add_parser("doctor", help="verify launchd health, refresh recency, and local toolchain")
    sub.add_parser("brainmap", help="regenerate the vault Brain Map (clickable Excalidraw of real wikilinks)")

    eod_cmd = sub.add_parser("eod", help="draft today's end-of-day close in the Builder OS daily note")
    eod_cmd.add_argument("--force", action="store_true", help="redraft even if the End-of-Day block is already filled")

    clean_cmd = sub.add_parser(
        "clean",
        help="remove agent worktrees/branches (claude/*, codex/*); backup-first, dry run by default",
    )
    clean_cmd.add_argument("--apply", action="store_true", help="execute (default is dry run)")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command in {"refresh", "verify", "doctor", "morning"}:
        load_local_env()
    if args.command == "refresh":
        return refresh(args)
    if args.command == "test":
        return 0 if run_tests(verbosity=2) else 1
    if args.command == "verify":
        return verify()
    if args.command == "doctor":
        return doctor()
    if args.command == "brainmap":
        refresh_brain_map()
        return 0
    if args.command == "eod":
        run_eod_close(force=args.force)
        return 0
    if args.command == "serve":
        return serve(args.port, open_browser=not args.no_open)
    if args.command == "clean":
        return clean_repos(apply=args.apply)
    if args.command == "morning":
        rc = refresh(args)
        if rc != 0:
            return rc
        rc = verify()
        if rc != 0:
            mark_daily_run_verified(args.port, passed=False)
            return rc
        mark_daily_run_verified(args.port, passed=True)
        return serve(args.port, open_browser=not args.no_open)
    parser.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
