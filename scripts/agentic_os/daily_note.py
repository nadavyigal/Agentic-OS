#!/usr/bin/env python3
"""Pre-fill today's daily note in the Builder OS vault (the 5-minute habit rail).

Founder-approved vault automation (2026-07-12, same approval pattern as the
Portfolio HQ refresh): every `./agentic-os refresh` / `morning` run creates
today's `11-Journal/YYYY-MM-DD.md` if it doesn't exist yet, pre-filled with:

  - Today's focus, seeded from dashboard/status.json priorityBoard "now" items
    (truncated — they are prompts to edit, not truth to accept).
  - The "Carry ->" lines from the most recent previous journal note, so open
    loops follow the founder instead of dying in yesterday's note.
  - Links into the graph (Brain Map, Current Priorities, yesterday's note) so
    each daily note is born connected, never an orphan.

The founder's 5 minutes = edit the focus line, write 3 end-of-day lines.
Never overwrites an existing note. Read-only against status.json. Stdlib only.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vault_git  # noqa: E402  (same directory; added to path above)

AOS_ROOT = Path(__file__).resolve().parents[2]
VAULT = Path("/Users/nadavyigal/Documents/Projects /Nadav Builder OS")
JOURNAL = VAULT / "11-Journal"
STATUS_JSON = AOS_ROOT / "dashboard" / "status.json"

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def first_sentence(text: str, limit: int = 140) -> str:
    text = re.sub(r"\*\*|`", "", text).strip()
    for stop in (". ", "; "):
        idx = text.find(stop)
        if 0 < idx < limit:
            return text[: idx + 1].strip()
    return (text[: limit - 1] + "…") if len(text) > limit else text


def focus_seeds() -> list[str]:
    try:
        data = json.loads(STATUS_JSON.read_text())
        now_items = (data.get("priorityBoard") or {}).get("now") or []
        return [first_sentence(str(item)) for item in now_items[:3]]
    except Exception:
        return []


def previous_note(today: str) -> Path | None:
    if not JOURNAL.is_dir():
        return None
    candidates = sorted(
        p for p in JOURNAL.glob("*.md")
        if DATE_RE.match(p.stem) and p.stem < today
    )
    return candidates[-1] if candidates else None


def carried_lines(prev: Path | None) -> list[str]:
    """Pull 'Carry ->' bullet lines from the previous note's end-of-day block."""
    if prev is None:
        return []
    carried: list[str] = []
    in_eod = False
    for line in prev.read_text(errors="ignore").splitlines():
        if line.lstrip().startswith("#"):
            in_eod = "end-of-day" in line.lower() or "end of day" in line.lower()
            continue
        if in_eod:
            m = re.match(r"^\s*[-*]\s*Carry\s*(?:→|->)?\s*:?\s*(.+)$", line, re.I)
            if m and m.group(1).strip():
                carried.append(m.group(1).strip())
    return carried


def build_note(today: str, prev: Path | None) -> str:
    focus = focus_seeds()
    focus_block = (
        "\n".join(f"{i}. {item}" for i, item in enumerate(focus, 1))
        if focus
        else "1. "
    )
    carried = carried_lines(prev)
    carried_block = (
        "\n".join(f"- {c}" for c in carried) if carried else "- (nothing carried)"
    )
    prev_link = f" · yesterday: [[{prev.stem}]]" if prev else ""
    return f"""---
title: "Daily Note - {today}"
tags:
  - daily-note
type: daily-note
status: active
date: "{today}"
created: "{today}"
---

# Daily Note - {today}

## Today's Focus

> Seeded from the Agentic OS priority board — edit, don't accept blindly. One or two things only.

{focus_block}

## Carried from previous note

{carried_block}

## Captures

> Link anything you touched or thought today. One wikilink minimum — links are how the second brain compounds.

-

## End-of-Day Check

- Moved:
- Didn't:
- Carry →:

## Links

- [[Builder OS Brain Map]] · [[Current Priorities]]{prev_link}
"""


def main() -> int:
    today = dt.date.today().isoformat()
    if len(sys.argv) > 1 and DATE_RE.match(sys.argv[1]):
        today = sys.argv[1]
    if not VAULT.is_dir():
        print("⚠️ daily note: vault not found, skipped")
        return 0
    # Never seed a note into a checkout that is behind its remote (2026-07-22).
    if not vault_git.require_fresh_vault(VAULT, "daily note"):
        return 1
    JOURNAL.mkdir(exist_ok=True)
    target = JOURNAL / f"{today}.md"
    if target.exists():
        print(f"daily note: {target.name} already exists, left as-is")
        return 0
    prev = previous_note(today)
    target.write_text(build_note(today, prev))
    print(f"daily note: created 11-Journal/{target.name} (pre-filled, ~5 min to finish)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
