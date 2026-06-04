#!/usr/bin/env python3
from __future__ import annotations

import argparse
import contextlib
import http.server
import json
import os
import re
import socket
import socketserver
import subprocess
import sys
import webbrowser
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
DASHBOARD = ROOT / "dashboard"
STATUS_JSON = DASHBOARD / "status.json"
INDEX_HTML = DASHBOARD / "index.html"
PROJECT_STATUS_HTML = DASHBOARD / "project-status.html"
COMMAND_CENTER_HTML = DASHBOARD / "command-center.html"
ORCHESTRATION_HTML = DASHBOARD / "orchestration.html"


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
        "task": "Run Resumely iOS live-device smoke, then prepare ASC upload.",
        "whenToUse": "Use when the next move touches App Store readiness, screenshots, smoke QA, or submission gates.",
        "evidence": "PROJECT-STATUS.md, dashboard/status.json, ResumeBuilder iOS tasks/session-log.md",
        "starter": "Act as the Release Manager for Resumely iOS. Read PROJECT-STATUS.md and the ResumeBuilder iOS tasks/session-log.md. Produce the exact smoke checklist, expected evidence, and ASC upload sequence. Do not submit or upload without explicit approval.",
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
    last_commit: str
    source_files: list[str]
    task_parse: dict[str, Any] = field(default_factory=dict)
    gtm: dict[str, Any] = field(default_factory=dict)
    plans: list[dict[str, Any]] = field(default_factory=list)


def run(cmd: list[str], cwd: Path = ROOT, timeout: int = 12) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=str(cwd),
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )


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
            rows.append((name, Path(path_match.group(1))))
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


def build_os_registry(root: Path) -> dict[str, Any]:
    """Auto-discover the Agentic OS from the repo itself, in two plain groups.

    - leadership: the Executive OS (CEO/COO/CFO/Analysis/Risk + Distribution). These review
      status and make decisions. The matching agent file is just how each is run, so it is not
      listed separately (that double-listing was confusing).
    - skillAgents: the builders that execute work packets (architect, QA, release, etc.).
    Work packets and commands are returned too, for the loop and commands sections.
    Anything created under these folders surfaces on the next run — nothing can silently vanish.
    """
    registry: dict[str, Any] = {
        "commands": [{"name": name, "purpose": purpose} for name, purpose in OS_COMMANDS],
        "leadership": [],
        "workPackets": [],
        "skillAgents": [],
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
                registry["workPackets"].append(
                    {
                        "title": title,
                        "status": clean_value(status_match.group(1)) if status_match else "Unknown",
                        "project": clean_value(project_match.group(1)) if project_match else None,
                        "goal": section_value(text, "## Goal"),
                        "path": str(packet.relative_to(root)),
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
            {"name": "Work packets", "what": f"{len(packets)} active. One focused repo task per decision that needs execution."},
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


def collect_evidence() -> list[ProjectEvidence]:
    evidence: list[ProjectEvidence] = []
    for source_name, path in parse_project_paths():
        project_id, display_name = PROJECT_ALIASES[source_name]
        sources: list[str] = []
        exists = path.exists()
        branch = "missing"
        dirty = False
        dirty_count = 0
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
                last_commit=last_commit,
                source_files=sources,
                task_parse=parse_task_files(path),
                gtm=gtm,
                plans=plans,
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
        blockers = project.get("blockers") or []
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
    return {
        "lastCommand": command,
        "lastRunAt": now_label(),
        "checksStatus": checks_status,
        "checksCompletedAt": "",
        "localhostUrl": f"http://127.0.0.1:{port}/index.html",
        "recommendedPromptProject": recommended.get("project", "No project prompt available"),
        "recommendedPromptRole": recommended.get("role", "Project Operator"),
        "recommendedPrompt": recommended.get("copyPrompt", "Run ./agentic-os refresh to generate project prompts."),
        "targetRepoState": recommended.get("repoState", "Unknown"),
        "targetBranch": recommended.get("branch", "Unknown"),
        "readyForNextSession": checks_status == "Passed",
        "summary": status.get("summary", {}).get("bestNextAction", "Run the morning loop and choose the next project prompt."),
    }


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
    status["metadata"]["sourcePolicy"] = (
        "Local folder mode. Refreshed by ./agentic-os from PROJECT-PATHS.md, local git, "
        "task memory/todo/session files, and existing dashboard status. No external dashboards queried."
    )

    status["runCenter"] = {
        "lastRefresh": now_label(),
        "command": command,
        "localhostUrl": f"http://127.0.0.1:{port}/index.html",
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
    derived = build_derived_summary(project_health, saved_plans)
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

    dirty_projects = [p["name"] for p in project_health if p["dirty"]]
    if dirty_projects:
        status.setdefault("summary", {})["mainBlockers"] = list(
            dict.fromkeys(status.get("summary", {}).get("mainBlockers", []) + [f"Dirty local repo state: {', '.join(dirty_projects)}."])
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

        # Auto-drive the displayed per-project narrative from parsed repo truth when the
        # parse is High confidence (tasks/progress.md with validation evidence). This is the
        # core trust fix: a project card can no longer show prose the repo contradicts.
        if health["sourceConfidence"] == "High" and parse:
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

        project["localEvidence"] = {
            "branch": health["branch"],
            "dirty": health["dirty"],
            "dirtyCount": health["dirtyCount"],
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
    result["localhostUrl"] = f"http://127.0.0.1:{port}/index.html"
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
    lines = [
        "# Project Status",
        "",
        f"Last updated: {status['metadata']['lastUpdated']}",
        "",
        "Source policy: local folder mode. Generated by `./agentic-os refresh` from local project paths, git state, task files, and `dashboard/status.json`. No external production dashboards were queried.",
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
    lines = [
        "# Portfolio Dashboard",
        "",
        f"Last updated: {status['metadata']['lastUpdated']}",
        "",
        status["metadata"]["sourcePolicy"],
        "",
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


def serve(port: int, open_browser: bool = True) -> int:
    port = find_port(port)
    # Serve from dashboard/ so the simple URL http://127.0.0.1:PORT/index.html works.
    # Content that lives outside dashboard/ (brainstorm, work packets) is read INTO status.json
    # by the parser and rendered inline, so there are no cross-directory links to break.
    os.chdir(DASHBOARD)
    handler = http.server.SimpleHTTPRequestHandler
    url = f"http://127.0.0.1:{port}/index.html"

    class ReusableTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    with ReusableTCPServer(("127.0.0.1", port), handler) as httpd:
        print(f"Agentic OS Command Center: {url}")
        print("Press Ctrl-C to stop.")
        if open_browser:
            webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped Agentic OS server.")
    return 0


def refresh(args: argparse.Namespace) -> int:
    status = update_status_json(port=args.port, command=f"./agentic-os {args.command}")
    print("refreshed Agentic OS")
    print(f"- last refresh: {status['runCenter']['lastRefresh']}")
    print("- brief: rebuilt from parsed repo truth (one process, always current).")
    reg = status.get("osRegistry", {})
    leaders = [o["name"] for o in reg.get("leadership", [])]
    print(f"- Executive OS (leadership): {', '.join(leaders) if leaders else 'none found'}")
    print(f"- work packets: {len(reg.get('workPackets', []))} | skill agents (builders): {len(reg.get('skillAgents', []))}")
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
    print("- no external dashboards or production services were queried")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="./agentic-os", description="Local Agentic OS command center")
    sub = parser.add_subparsers(dest="command", required=True)

    morning = sub.add_parser("morning", help="refresh, verify, serve localhost, and open Command Center")
    morning.add_argument("--port", type=int, default=8787)
    morning.add_argument("--no-open", action="store_true", help="serve without opening a browser")

    refresh_cmd = sub.add_parser("refresh", help="refresh status files without serving")
    refresh_cmd.add_argument("--port", type=int, default=8787)

    serve_cmd = sub.add_parser("serve", help="serve the current dashboard")
    serve_cmd.add_argument("--port", type=int, default=8787)
    serve_cmd.add_argument("--no-open", action="store_true", help="serve without opening a browser")

    sub.add_parser("verify", help="verify dashboard JSON, fallback sync, links, and whitespace")
    sub.add_parser("test", help="run the parser unit tests")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "refresh":
        return refresh(args)
    if args.command == "test":
        return 0 if run_tests(verbosity=2) else 1
    if args.command == "verify":
        return verify()
    if args.command == "serve":
        return serve(args.port, open_browser=not args.no_open)
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
