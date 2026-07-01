#!/usr/bin/env python3
"""Unit tests for intent_cluster.py. Run with `python3 -m unittest test_intent_cluster`."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import intent_cluster

SAMPLE_LOG = """# Intent Log

## 2026-06-08 - Vault bootstrap
**Request:** Bootstrap the vault.
**Intent / why:** Needed an index.
**Themes:** infrastructure, wiki-quality, navigation

---

## 2026-06-02 - Make Agentic OS top-tier
**Request:** Move the OS to top tier.
**Intent / why:** Distrust of curated narrative status.
**Themes:** trust, verifiability, anti-bloat

## 2026-05-30 - Out of range entry
**Request:** Something in a different month.
**Intent / why:** Should not be counted for 2026-06.
**Themes:** trust, out-of-range
"""


class TestEntriesForMonth(unittest.TestCase):
    def test_extracts_only_matching_month(self):
        themes = intent_cluster.entries_for_month(SAMPLE_LOG, "2026-06")
        self.assertEqual(
            themes,
            [
                "infrastructure, wiki-quality, navigation",
                "trust, verifiability, anti-bloat",
            ],
        )

    def test_empty_for_month_with_no_entries(self):
        themes = intent_cluster.entries_for_month(SAMPLE_LOG, "2026-01")
        self.assertEqual(themes, [])


class TestCluster(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.log_path = Path(self.tmpdir.name) / "INTENT-LOG.md"
        self.log_path.write_text(SAMPLE_LOG, encoding="utf-8")

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_appends_ranked_cluster_section(self):
        result = intent_cluster.cluster("2026-06", self.log_path)
        text = self.log_path.read_text(encoding="utf-8")
        self.assertIn("## Theme Clusters - 2026-06", text)
        self.assertIn("- trust (1)", text)
        self.assertIn("- infrastructure (1)", text)
        self.assertIn("6 themes across 2 entries", result)

    def test_idempotent_second_call_is_noop(self):
        intent_cluster.cluster("2026-06", self.log_path)
        before = self.log_path.read_text(encoding="utf-8")
        result = intent_cluster.cluster("2026-06", self.log_path)
        after = self.log_path.read_text(encoding="utf-8")
        self.assertEqual(before, after)
        self.assertIn("already exists", result)

    def test_no_entries_for_month_does_not_write(self):
        result = intent_cluster.cluster("2026-01", self.log_path)
        text = self.log_path.read_text(encoding="utf-8")
        self.assertNotIn("Theme Clusters - 2026-01", text)
        self.assertIn("No entries found", result)


if __name__ == "__main__":
    unittest.main()
