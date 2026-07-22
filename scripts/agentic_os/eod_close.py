#!/usr/bin/env python3
"""Draft today's end-of-day close in the Builder OS daily note (the evening rail).

Counterpart to daily_note.py (the morning rail). Where daily_note.py seeds the
morning, eod_close.py fills the `## End-of-Day Check` block at day's end with an
evidence-based DRAFT so the founder edits instead of composing from a blank line:

  - Moved:  today's git commits across every product/OS repo, plus which projects
            saw Claude Code sessions today. Concrete "what actually moved."
  - Didn't: today's focus items (read back from this note) with no matching commit
            today — planned, not shipped. A prompt to confirm or cross off, not truth.
  - Carry →: the Didn't items, emitted as `- Carry → ...` lines so unfinished work
            flows into tomorrow's note (daily_note.py reads exactly these lines the
            next morning — keep that inline format or the carry-forward loop breaks).

Cursor can't be introspected (its state lives in opaque SQLite), so the draft
always leaves exactly one explicit manual Cursor line for the founder to fill.

Honest scope: git commits and Claude sessions are real evidence; the Moved↔Didn't
split is a keyword heuristic and is labelled a draft. Idempotent — only fills a
still-blank End-of-Day block; never clobbers founder edits (use --force to redraft).
Read-only against every repo (git log only). Stdlib only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import os
import re
import subprocess
import sys
from pathlib import Path

# Reuse the morning rail's constants + note scaffolding so the two stay in lockstep.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import daily_note  # noqa: E402  (same directory; added to path above)

VAULT = daily_note.VAULT
JOURNAL = daily_note.JOURNAL
DATE_RE = daily_note.DATE_RE

HOME = Path.home()
CLAUDE_PROJECTS = HOME / ".claude" / "projects"

# Canonical repo set (mirrors ~/.claude/CLAUDE.md Active Projects + this OS + the vault).
REPOS: list[tuple[str, str]] = [
    ("/Users/nadavyigal/Documents/RunSmart", "RunSmart"),
    ("/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-", "ResumeBuilder Web"),
    ("/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app", "RunSmart iOS"),
    ("/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP", "Resumely iOS"),
    ("/Users/nadavyigal/Documents/Projects /Agentic OS", "Agentic OS"),
    (str(VAULT), "Builder OS Vault"),
]

_STOPWORDS = {
    "with", "from", "that", "this", "into", "your", "will", "have", "when", "then",
    "them", "they", "make", "made", "need", "next", "just", "over", "only", "once",
    "note", "notes", "item", "items", "line", "lines", "work", "task", "tasks",
    "run", "runs", "edit", "open", "read", "done", "todo", "plan", "plans",
}


def _significant_tokens(text: str) -> set[str]:
    """Lowercased alphanumeric tokens of length >= 4, minus generic stopwords."""
    tokens = re.findall(r"[A-Za-z0-9]{4,}", text.lower())
    return {t for t in tokens if t not in _STOPWORDS}


# --- evidence collection (side-effectful; git log + session files) -----------------

def git_commits_today(day: str) -> list[tuple[str, list[str]]]:
    """Return [(repo_label, [commit_subject, ...]), ...] for repos with commits on `day`."""
    since = f"{day} 00:00:00"
    until = f"{day} 23:59:59"
    out: list[tuple[str, list[str]]] = []
    for path, label in REPOS:
        if not os.path.isdir(os.path.join(path, ".git")):
            continue
        try:
            res = subprocess.run(
                ["git", "-C", path, "log", "--all", "--no-merges",
                 f"--since={since}", f"--until={until}", "--pretty=%s"],
                capture_output=True, text=True, timeout=20,
            )
        except (subprocess.TimeoutExpired, OSError):
            continue
        if res.returncode != 0:
            continue
        subjects = [s.strip() for s in res.stdout.splitlines() if s.strip()]
        if subjects:
            out.append((label, subjects))
    return out


def _project_for(cwd: str) -> str:
    for needle, label in (
        ("RunSmart", "RunSmart"),
        ("ResumeBuilder", "ResumeBuilder"),
        ("Agentic OS", "Agentic OS"),
        ("Nadav Builder OS", "Builder OS Vault"),
        ("IOS RunSmart", "RunSmart iOS"),
    ):
        if needle in (cwd or ""):
            return label
    return ""


def claude_projects_today(day: str) -> list[str]:
    """Distinct project labels with a Claude Code session touched on `day`."""
    projects: set[str] = set()
    day_start = dt.datetime.fromisoformat(day).replace(tzinfo=dt.timezone.utc)
    for path in glob.glob(str(CLAUDE_PROJECTS / "*" / "*.jsonl")):
        try:
            mtime = dt.datetime.fromtimestamp(os.path.getmtime(path), dt.timezone.utc)
        except OSError:
            continue
        if mtime < day_start:  # cheap pre-filter: file untouched today
            continue
        cwd = ""
        touched_today = False
        try:
            with open(path, "r", errors="ignore") as fh:
                for line in fh:
                    if not cwd and '"cwd"' in line:
                        m = re.search(r'"cwd"\s*:\s*"([^"]+)"', line)
                        if m:
                            cwd = m.group(1)
                    if not touched_today and f'"{day}' in line and '"timestamp"' in line:
                        touched_today = True
                    if cwd and touched_today:
                        break
        except OSError:
            continue
        if touched_today:
            label = _project_for(cwd)
            if label:
                projects.add(label)
    return sorted(projects)


# --- pure rendering (unit-tested) --------------------------------------------------

def focus_items(note_text: str) -> list[str]:
    """Read the numbered/bulleted lines under this note's '## Today's Focus'."""
    items: list[str] = []
    in_focus = False
    for line in note_text.splitlines():
        if line.lstrip().startswith("#"):
            in_focus = "today's focus" in line.lower() or "todays focus" in line.lower()
            continue
        if in_focus:
            m = re.match(r"^\s*(?:\d+\.|[-*])\s+(.*\S.*)$", line)
            if m:
                items.append(m.group(1).strip())
    return items


def split_moved_didnt(focus: list[str], commit_subjects: list[str]) -> tuple[list[str], list[str]]:
    """Heuristic: a focus item counts as 'moved' if it shares a significant token
    with any commit subject today; otherwise it lands in 'didn't'. Draft only."""
    commit_tokens: set[str] = set()
    for subj in commit_subjects:
        commit_tokens |= _significant_tokens(subj)
    didnt: list[str] = []
    for item in focus:
        if _significant_tokens(item) & commit_tokens:
            continue
        didnt.append(item)
    moved = [f for f in focus if f not in didnt]
    return moved, didnt


def build_eod_block(
    commits: list[tuple[str, list[str]]],
    sessions: list[str],
    didnt: list[str],
    carry: list[str],
) -> str:
    """Render the filled '## End-of-Day Check' block. Carry lines stay in the
    `- Carry → ...` inline form that daily_note.carried_lines() reads next morning."""
    moved_lines: list[str] = []
    for label, subjects in commits:
        shown = "; ".join(subjects[:4])
        if len(subjects) > 4:
            shown += f"; (+{len(subjects) - 4} more)"
        moved_lines.append(f"    - {label} — {shown}")
    if sessions:
        moved_lines.append(f"    - Claude Code sessions today: {', '.join(sessions)}")
    if not commits and not sessions:
        moved_lines.append("    - (no git commits or Claude sessions detected today)")
    # Exactly one explicit manual line — Cursor can't be introspected.
    moved_lines.append("    - Cursor — _fill manually (Cursor sessions aren't introspectable)_")

    didnt_lines = (
        [f"    - {d}" for d in didnt]
        if didnt
        else ["    - (nothing flagged — confirm before closing)"]
    )
    # Bare `- Carry →:` when empty so carried_lines() skips it (no phantom carry).
    carry_lines = [f"- Carry → {c}" for c in carry] if carry else ["- Carry →:"]

    body = "\n".join(
        [
            "## End-of-Day Check",
            "",
            "> Draft from `./agentic-os eod` — today's git commits + Claude Code sessions."
            " Edit freely; Cursor is manual.",
            "",
            "- Moved:",
            *moved_lines,
            "- Didn't:",
            *didnt_lines,
            *carry_lines,
        ]
    )
    return body


_EOD_HEADER_RE = re.compile(r"^##\s+End-of-Day Check\s*$", re.M)


def block_is_blank(note_text: str) -> bool:
    """True when the End-of-Day block is still the pristine template (no draft, no
    founder content) — i.e. safe to fill without clobbering anything."""
    seg = _extract_eod_segment(note_text)
    if seg is None:
        return False
    for line in seg.splitlines()[1:]:  # skip the header line itself
        s = line.strip()
        if not s:
            continue
        if s in ("- Moved:", "- Didn't:", "- Carry →:", "- Carry ->:"):
            continue
        return False
    return True


def _extract_eod_segment(note_text: str) -> str | None:
    """The text from the '## End-of-Day Check' header up to (not including) the next
    '## ' header or end of file. None if there is no such block."""
    m = _EOD_HEADER_RE.search(note_text)
    if not m:
        return None
    start = m.start()
    nxt = re.search(r"^##\s+", note_text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(note_text)
    return note_text[start:end].rstrip() + "\n"


def splice_eod(note_text: str, new_block: str) -> str:
    """Replace the existing End-of-Day block with new_block, preserving surrounding
    sections. If no block exists, append one before the '## Links' section (or EOF)."""
    seg = _extract_eod_segment(note_text)
    if seg is not None:
        return note_text.replace(seg.rstrip("\n"), new_block, 1)
    insert = f"\n{new_block}\n"
    links = re.search(r"^##\s+Links\s*$", note_text, re.M)
    if links:
        return note_text[: links.start()] + new_block + "\n\n" + note_text[links.start():]
    return note_text.rstrip("\n") + "\n" + insert


# --- entry point -------------------------------------------------------------------

def close_day(day: str, force: bool) -> tuple[bool, str]:
    """Fill today's note. Returns (changed, message)."""
    if not VAULT.is_dir():
        return False, "⚠️ eod close: vault not found, skipped"
    # Never draft into a checkout that is behind its remote (2026-07-22).
    if not daily_note.vault_git.require_fresh_vault(VAULT, "eod close"):
        return False, ""
    JOURNAL.mkdir(exist_ok=True)
    target = JOURNAL / f"{day}.md"
    if not target.exists():
        # No morning note yet — scaffold one so the close has somewhere to land.
        target.write_text(daily_note.build_note(day, daily_note.previous_note(day)))
    note_text = target.read_text(errors="ignore")

    if not force and not block_is_blank(note_text):
        return False, f"eod close: {target.name} End-of-Day block already filled, left as-is (use --force to redraft)"

    commits = git_commits_today(day)
    sessions = claude_projects_today(day)
    all_subjects = [s for _, subs in commits for s in subs]
    _moved, didnt = split_moved_didnt(focus_items(note_text), all_subjects)
    block = build_eod_block(commits, sessions, didnt, carry=didnt)
    target.write_text(splice_eod(note_text, block))

    repo_n = sum(len(subs) for _, subs in commits)
    return True, (
        f"eod close: drafted End-of-Day in 11-Journal/{target.name} "
        f"({repo_n} commits across {len(commits)} repos, {len(sessions)} Claude projects; "
        f"edit + add Cursor by hand)"
    )


def main() -> int:
    parser = argparse.ArgumentParser(prog="eod_close.py", description="Draft today's end-of-day close.")
    parser.add_argument("date", nargs="?", help="YYYY-MM-DD (defaults to today)")
    parser.add_argument("--force", action="store_true", help="redraft even if the block is already filled")
    args = parser.parse_args()

    day = dt.date.today().isoformat()
    if args.date and DATE_RE.match(args.date):
        day = args.date

    _changed, message = close_day(day, args.force)
    if not message:
        # The staleness guard already printed its own refusal; don't add a blank
        # line, and exit non-zero so the caller reports it as blocked.
        return 1
    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
