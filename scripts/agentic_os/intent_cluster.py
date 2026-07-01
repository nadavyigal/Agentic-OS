#!/usr/bin/env python3
"""Count INTENT-LOG.md theme tags for a month and append a ranked cluster section.

Standalone, stdlib-only. Run with `python3 intent_cluster.py [YYYY-MM]`
(defaults to the current month) from anywhere - it locates INTENT-LOG.md
relative to this file.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parents[2] / "INTENT-LOG.md"
ENTRY_RE = re.compile(r"^## (\d{4}-\d{2}-\d{2}) -", re.MULTILINE)
THEME_RE = re.compile(r"^\*\*Themes:\*\*\s*(.+)$", re.MULTILINE)


def entries_for_month(text: str, month: str) -> list[str]:
    """Return the raw Themes: value for every entry dated within `month` (YYYY-MM)."""
    dates = [(m.start(), m.group(1)) for m in ENTRY_RE.finditer(text)]
    themes = [(m.start(), m.group(1)) for m in THEME_RE.finditer(text)]
    result = []
    for pos, theme_line in themes:
        entry_date = None
        for d_pos, d_val in dates:
            if d_pos <= pos:
                entry_date = d_val
            else:
                break
        if entry_date and entry_date.startswith(month):
            result.append(theme_line)
    return result


def cluster(month: str, log_path: Path = LOG_PATH) -> str:
    """Append a ranked theme-frequency section for `month` to log_path. Idempotent."""
    text = log_path.read_text(encoding="utf-8")
    heading = f"## Theme Clusters - {month}"
    if heading in text:
        return f"Cluster for {month} already exists, skipping."

    theme_lines = entries_for_month(text, month)
    if not theme_lines:
        return f"No entries found for {month}, nothing to cluster."

    counts: Counter[str] = Counter()
    for line in theme_lines:
        for theme in line.split(","):
            theme = theme.strip().lower()
            if theme:
                counts[theme] += 1

    ranked = counts.most_common()
    body = "\n".join(f"- {theme} ({count})" for theme, count in ranked)
    section = f"\n{heading}\n\n{body}\n"
    log_path.write_text(text.rstrip("\n") + "\n" + section, encoding="utf-8")
    return f"Appended cluster for {month}: {len(ranked)} themes across {len(theme_lines)} entries."


def main() -> int:
    month = sys.argv[1] if len(sys.argv) > 1 else date.today().strftime("%Y-%m")
    print(cluster(month))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
