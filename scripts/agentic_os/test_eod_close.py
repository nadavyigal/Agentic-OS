#!/usr/bin/env python3
"""Hermetic unit tests for the end-of-day close rail (eod_close.py).

No repos, git, or network — the pure rendering/splicing/heuristic functions are
tested directly, plus the loop-closing invariant that the Carry lines eod_close
writes are exactly what daily_note.carried_lines() reads the next morning.
Run with `python3 -m unittest test_eod_close`.
"""
from __future__ import annotations

import unittest

import daily_note
import eod_close


BLANK_NOTE = """---
title: "Daily Note - 2026-07-12"
---

# Daily Note - 2026-07-12

## Today's Focus

> Seeded from the priority board.

1. Reconcile Agentic OS main so the daily-note habit activates
2. Build the eod_close script

## Captures

-

## End-of-Day Check

- Moved:
- Didn't:
- Carry →:

## Links

- [[Builder OS Brain Map]]
"""


class BlankDetectionTests(unittest.TestCase):
    def test_pristine_block_is_blank(self):
        self.assertTrue(eod_close.block_is_blank(BLANK_NOTE))

    def test_filled_block_is_not_blank(self):
        commits = [("Agentic OS", ["feat: eod_close script"])]
        block = eod_close.build_eod_block(commits, ["Agentic OS"], ["something"], ["something"])
        filled = eod_close.splice_eod(BLANK_NOTE, block)
        self.assertFalse(eod_close.block_is_blank(filled))

    def test_missing_block_is_not_blank(self):
        self.assertFalse(eod_close.block_is_blank("# Note\n\n## Today's Focus\n\n1. x\n"))


class FocusAndSplitTests(unittest.TestCase):
    def test_focus_items_read_numbered_lines(self):
        items = eod_close.focus_items(BLANK_NOTE)
        self.assertEqual(len(items), 2)
        self.assertIn("Build the eod_close script", items)

    def test_focus_items_stop_at_next_heading(self):
        # "Moved"/"Didn't" template lines live under a *different* heading and must not leak in.
        self.assertNotIn("Moved:", " ".join(eod_close.focus_items(BLANK_NOTE)))

    def test_split_moved_when_commit_shares_token(self):
        focus = ["Build the eod_close script", "Ship the marketing page"]
        commits = ["feat: add eod_close script and tests"]
        moved, didnt = eod_close.split_moved_didnt(focus, commits)
        self.assertIn("Build the eod_close script", moved)
        self.assertIn("Ship the marketing page", didnt)

    def test_split_all_didnt_when_no_commits(self):
        focus = ["Reconcile main", "Build the script"]
        moved, didnt = eod_close.split_moved_didnt(focus, [])
        self.assertEqual(moved, [])
        self.assertEqual(len(didnt), 2)


class BlockRenderTests(unittest.TestCase):
    def test_always_includes_one_manual_cursor_line(self):
        block = eod_close.build_eod_block([], [], [], [])
        cursor_bullets = [ln for ln in block.splitlines() if ln.lstrip().startswith("- Cursor")]
        self.assertEqual(len(cursor_bullets), 1)
        self.assertIn("manually", cursor_bullets[0].lower())

    def test_commits_and_sessions_render(self):
        commits = [("RunSmart", ["fix: plan eval", "chore: bump"]), ("Agentic OS", ["feat: eod"])]
        block = eod_close.build_eod_block(commits, ["RunSmart", "Builder OS Vault"], [], [])
        self.assertIn("RunSmart — fix: plan eval; chore: bump", block)
        self.assertIn("Claude Code sessions today: RunSmart, Builder OS Vault", block)

    def test_commit_overflow_is_summarised(self):
        subs = [f"commit {i}" for i in range(7)]
        block = eod_close.build_eod_block([("RunSmart", subs)], [], [], [])
        self.assertIn("(+3 more)", block)

    def test_empty_carry_uses_bare_marker(self):
        block = eod_close.build_eod_block([], [], [], carry=[])
        self.assertIn("- Carry →:", block)

    def test_no_evidence_is_stated_not_hidden(self):
        block = eod_close.build_eod_block([], [], [], [])
        self.assertIn("no git commits or Claude sessions", block)


class SpliceTests(unittest.TestCase):
    def test_splice_replaces_only_eod_block(self):
        block = eod_close.build_eod_block([("Agentic OS", ["feat: x"])], [], ["y"], ["y"])
        out = eod_close.splice_eod(BLANK_NOTE, block)
        self.assertEqual(out.count("## End-of-Day Check"), 1)
        self.assertIn("## Today's Focus", out)   # untouched
        self.assertIn("## Links", out)           # untouched
        self.assertIn("feat: x", out)

    def test_splice_is_idempotent_on_rerun(self):
        block1 = eod_close.build_eod_block([("Agentic OS", ["feat: x"])], [], ["y"], ["y"])
        once = eod_close.splice_eod(BLANK_NOTE, block1)
        block2 = eod_close.build_eod_block([("Agentic OS", ["feat: z"])], [], ["w"], ["w"])
        twice = eod_close.splice_eod(once, block2)
        self.assertEqual(twice.count("## End-of-Day Check"), 1)
        self.assertIn("feat: z", twice)
        self.assertNotIn("feat: x", twice)


class CarryForwardLoopTests(unittest.TestCase):
    """The morning rail must be able to read the Carry lines the evening rail writes."""

    def test_carry_lines_are_readable_by_daily_note(self, tmpname="2026-07-12.md"):
        import tempfile
        from pathlib import Path

        carry = ["Finish eod_close tests", "Push and open PR"]
        block = eod_close.build_eod_block([("Agentic OS", ["feat: x"])], [], carry, carry)
        note = eod_close.splice_eod(BLANK_NOTE, block)
        with tempfile.TemporaryDirectory() as d:
            prev = Path(d) / tmpname
            prev.write_text(note)
            recovered = daily_note.carried_lines(prev)
        self.assertEqual(recovered, carry)


if __name__ == "__main__":
    unittest.main()
