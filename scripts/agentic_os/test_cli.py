#!/usr/bin/env python3
"""Hermetic unit tests for the Agentic OS status parser.

No external repos, git, or network. Fixtures are written to temp dirs so the parser
pipeline is regression-proof. Run with `./agentic-os test` or `python3 -m unittest`.
"""
from __future__ import annotations

import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path

import cli


def write_tasks(root: str, files: dict[str, str]) -> None:
    tasks = Path(root) / "tasks"
    tasks.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        (tasks / name).write_text(content, encoding="utf-8")


class TestPureHelpers(unittest.TestCase):
    def test_clean_value(self):
        self.assertIsNone(cli.clean_value("—"))
        self.assertIsNone(cli.clean_value("  none "))
        self.assertEqual(cli.clean_value("  Hello   world. "), "Hello world")

    def test_split_list(self):
        self.assertEqual(cli.split_list("a; b ; c"), ["a", "b", "c"])
        self.assertEqual(cli.split_list("—"), [])

    def test_validation_evidence(self):
        self.assertTrue(cli.has_validation_evidence("All tests passed on 2026-06-01"))
        self.assertFalse(cli.has_validation_evidence("validation pending"))
        self.assertFalse(cli.has_validation_evidence("not yet tested"))
        self.assertFalse(cli.has_validation_evidence(None))

    def test_freshness(self):
        today = datetime.now()
        self.assertEqual(cli.compute_freshness([today])[0], "Fresh")
        self.assertEqual(cli.compute_freshness([today - timedelta(days=5)])[0], "Needs Review")
        self.assertEqual(cli.compute_freshness([today - timedelta(days=20)])[0], "Stale")
        self.assertEqual(cli.compute_freshness([None])[0], "Unknown")
        # newest date wins
        self.assertEqual(cli.compute_freshness([today - timedelta(days=30), today])[0], "Fresh")

    def test_texts_disagree(self):
        self.assertFalse(cli.texts_disagree("App Store review", "app store review"))
        self.assertFalse(cli.texts_disagree("App Store review plus planning", "App Store review"))
        self.assertTrue(cli.texts_disagree("Pre-release", "App Store submission"))
        self.assertFalse(cli.texts_disagree("", "x"))

    def test_extract_evidence(self):
        evidence = cli.extract_evidence(
            {
                "lastValidation": "build succeeded; tests passed 53 XCTest + 5 Swift Testing; see docs/qa/run.md (2026-06-01)",
                "lastUpdated": "2026-05-01",
            }
        )
        self.assertIn("53 XCTest", evidence["tests"])
        self.assertIn("5 Swift Testing", evidence["tests"])
        self.assertEqual(evidence["buildStatus"], "succeeded")
        self.assertIn("docs/qa/run.md", evidence["qaDocs"])
        self.assertEqual(evidence["evidenceDate"], "2026-06-01")

    def test_evidence_date_fallback(self):
        evidence = cli.extract_evidence({"lastValidation": "passed", "lastUpdated": "2026-05-01"})
        self.assertEqual(evidence["evidenceDate"], "2026-05-01")

    def test_section_bullets(self):
        text = "## Open Questions\n- q1\n- q2\n\n## Other\n- x"
        self.assertEqual(cli.section_bullets(text, r"^#{2,4}\s*open questions?\b"), ["q1", "q2"])

    def test_open_questions_section_only(self):
        text = "Checked the historical open questions for X\n## Open Questions\n- real q\n- Resolved: old"
        self.assertEqual(cli.extract_open_questions({"tasks/x.md": text}), ["real q"])

    def test_open_decisions_excludes_made(self):
        text = "## Decisions Needed\n- pick path\n## Decisions Made\n- shipped X"
        self.assertEqual(cli.extract_open_decisions({"tasks/x.md": text}), ["pick path"])


class TestParseTaskFiles(unittest.TestCase):
    def test_progress_present_high(self):
        with tempfile.TemporaryDirectory() as d:
            write_tasks(
                d,
                {
                    "progress.md": (
                        "Current Phase: Beta\n"
                        "Next Recommended Story: ship it\n"
                        "Blockers: —\n"
                        "Last Validation: All tests passed on 2026-06-01\n"
                        "Last Updated: 2026-06-01\n"
                    )
                },
            )
            parsed = cli.parse_task_files(Path(d))
            self.assertEqual(parsed["preferredSource"], "tasks/progress.md")
            self.assertEqual(parsed["sourceConfidence"], "High")
            self.assertEqual(parsed["currentPhase"], "Beta")
            self.assertEqual(parsed["nextRecommendedStory"], "ship it")
            self.assertEqual(parsed["blockers"], [])

    def test_progress_present_medium_without_validation(self):
        with tempfile.TemporaryDirectory() as d:
            write_tasks(
                d,
                {"progress.md": "Current Phase: Beta\nLast Validation: not yet tested\nLast Updated: 2026-06-01\n"},
            )
            parsed = cli.parse_task_files(Path(d))
            self.assertEqual(parsed["preferredSource"], "tasks/progress.md")
            self.assertEqual(parsed["sourceConfidence"], "Medium")

    def test_derived_from_todo_and_session(self):
        with tempfile.TemporaryDirectory() as d:
            write_tasks(
                d,
                {
                    "todo.md": "# Task State\n## Current Task\nWire the API\n",
                    "session-log.md": "## 2026-06-01 - Sprint work\n### Validation\n- All tests passed\n",
                },
            )
            parsed = cli.parse_task_files(Path(d))
            self.assertEqual(parsed["preferredSource"], "derived")
            self.assertEqual(parsed["currentPhase"], "Sprint work")
            self.assertEqual(parsed["activeStory"], "Wire the API")
            self.assertEqual(parsed["lastUpdated"], "2026-06-01")
            self.assertEqual(parsed["sourceConfidence"], "High")

    def test_missing_path_unknown(self):
        parsed = cli.parse_task_files(Path("/nonexistent/path/xyz123"))
        self.assertEqual(parsed["sourceConfidence"], "Unknown")
        self.assertEqual(parsed["preferredSource"], "none")
        self.assertTrue(parsed["missing"])

    def test_no_task_files_unknown(self):
        with tempfile.TemporaryDirectory() as d:
            parsed = cli.parse_task_files(Path(d))
            self.assertEqual(parsed["sourceConfidence"], "Unknown")
            self.assertIn("No local task files", parsed["notes"])


class TestDriftAndConfidence(unittest.TestCase):
    def test_drift_high_only(self):
        status = {
            "projects": [
                {"name": "A", "sourceConfidence": "High", "currentPhase": "Old phase", "taskParse": {"currentPhase": "New phase"}},
                {"name": "B", "sourceConfidence": "Low", "currentPhase": "X", "taskParse": {"currentPhase": "Y"}},
                {"name": "C", "sourceConfidence": "High", "currentPhase": "Same", "taskParse": {"currentPhase": "Same"}},
            ]
        }
        names = {(w["project"], w["field"]) for w in cli.compute_drift_warnings(status)}
        self.assertIn(("A", "current phase"), names)
        self.assertNotIn(("B", "current phase"), names)  # Low confidence is ignored
        self.assertNotIn(("C", "current phase"), names)  # agreement is not drift

    def test_resolve_confidence_narrative_fallback(self):
        parse = cli.empty_task_parse()  # no sources -> Unknown
        project_with_narrative = {"currentPhase": "Some phase"}
        self.assertEqual(cli.resolve_confidence(parse, project_with_narrative, exists=True), "Low")
        self.assertEqual(cli.resolve_confidence(parse, {}, exists=False), "Unknown")

    def test_confidence_directive_levels(self):
        self.assertIn("may proceed", cli.confidence_directive("High", False).lower())
        self.assertIn("must re-read", cli.confidence_directive("Low", False).lower())
        self.assertIn("re-validate", cli.confidence_directive("High", True).lower())


if __name__ == "__main__":
    unittest.main()
