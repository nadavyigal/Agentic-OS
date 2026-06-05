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


class TestOSRegistry(unittest.TestCase):
    def test_side_projects_and_research_topics_are_discovered(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            side_project = root / "clarity-funnel"
            research = root / "executive-os" / "research"
            side_project.mkdir(parents=True)
            research.mkdir(parents=True)
            (side_project / "README.md").write_text(
                "# Clarity Funnel\n\nA structured brainstorm for testing a new project idea.\n",
                encoding="utf-8",
            )
            (side_project / "SKILL.md").write_text("# Skill\n", encoding="utf-8")
            (research / "README.md").write_text("# Research\n", encoding="utf-8")
            (research / "2026-06-05-new-project.md").write_text(
                "# New Project Research\n\nEvidence and questions for a possible product.\n",
                encoding="utf-8",
            )

            registry = cli.build_os_registry(root)

            self.assertEqual(registry["sideProjects"][0]["name"], "Clarity Funnel")
            self.assertEqual(registry["sideProjects"][0]["path"], "clarity-funnel/README.md")
            self.assertEqual(registry["researchTopics"][0]["name"], "New Project Research")
            self.assertEqual(
                registry["researchTopics"][0]["path"],
                "executive-os/research/2026-06-05-new-project.md",
            )

    def test_packet_metadata_defaults_remain_backward_compatible(self):
        with tempfile.TemporaryDirectory() as d:
            packets = Path(d) / "executive-os" / "work-packets"
            packets.mkdir(parents=True)
            (packets / "WP-1.md").write_text(
                "# Work Packet WP-1 (Active)\n"
                "- Status: Active\n"
                "- Source: launch-plan.md\n\n"
                "## Project\nExample\n\n"
                "## Goal\nShip the change.\n",
                encoding="utf-8",
            )

            packet = cli.build_os_registry(Path(d))["workPackets"][0]

            self.assertEqual(packet["workflowPattern"], "normal")
            self.assertEqual(packet["inputTrust"], "trusted")
            self.assertIsNone(packet["outcomeLoop"])
            self.assertIsNone(packet["successSignal"])

    def test_packet_metadata_and_operating_artifacts_are_discovered(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            packets = root / "executive-os" / "work-packets"
            loops = root / "executive-os" / "loops"
            context = root / "executive-os" / "context"
            packets.mkdir(parents=True)
            loops.mkdir(parents=True)
            context.mkdir(parents=True)

            (packets / "WP-1.md").write_text(
                "# Work Packet WP-1 (Active)\n"
                "- Status: Active\n"
                "- Workflow pattern: independent-review\n"
                "- Input trust: untrusted\n"
                "- Outcome loop: resumely-submission\n"
                "- Success signal: signed smoke evidence exists\n\n"
                "## Project\nResumely iOS\n\n"
                "## Goal\nProduce evidence.\n",
                encoding="utf-8",
            )
            (loops / "README.md").write_text("# Outcome Loops\n", encoding="utf-8")
            (loops / "resumely-submission.md").write_text(
                "# Outcome Loop: Resumely Submission\n"
                "- Status: active\n"
                "- Owner: COO OS\n"
                "- Outcome: approved and live with analytics verified\n"
                "- Source: BUSINESS-GTM-PLAN-V0.md\n"
                "- Linked packet: WP-1-resumely-device-smoke.md\n"
                "- Leading signal: submit-ready evidence exists\n"
                "- Result metric: App Store status is Ready for Sale\n"
                "- Current milestone: authenticated device smoke\n"
                "- Constraint: founder-controlled upload\n"
                "- Last reviewed: 2026-06-05\n"
                "- Evidence source: product tasks/progress.md\n"
                "- Memory destination: product tasks/session-log.md\n"
                "- Close condition: approved and analytics verified\n",
                encoding="utf-8",
            )
            (context / "README.md").write_text("# Context Checkpoints\n", encoding="utf-8")
            (context / "2026-06-05-offer.md").write_text(
                "# Context Checkpoint: Offer\n"
                "- Status: ready-for-promotion\n"
                "- Topic: AI Audit offer\n"
                "- Purpose: define the first sellable version\n"
                "- Created: 2026-06-05\n"
                "- Last updated: 2026-06-05\n",
                encoding="utf-8",
            )

            registry = cli.build_os_registry(root)
            packet = registry["workPackets"][0]
            loop = registry["outcomeLoops"][0]
            checkpoint = registry["contextCheckpoints"][0]

            self.assertEqual(packet["workflowPattern"], "independent-review")
            self.assertEqual(packet["inputTrust"], "untrusted")
            self.assertEqual(packet["outcomeLoop"], "resumely-submission")
            self.assertEqual(packet["successSignal"], "signed smoke evidence exists")
            self.assertEqual(loop["status"], "active")
            self.assertEqual(loop["owner"], "COO OS")
            self.assertEqual(loop["resultMetric"], "App Store status is Ready for Sale")
            self.assertEqual(checkpoint["status"], "ready-for-promotion")
            self.assertEqual(checkpoint["topic"], "AI Audit offer")
            self.assertEqual(len(registry["outcomeLoops"]), 1)
            self.assertEqual(len(registry["contextCheckpoints"]), 1)


class TestGtm(unittest.TestCase):
    def test_parse_gtm_present(self):
        with tempfile.TemporaryDirectory() as d:
            dist = Path(d) / ".agent-os" / "distribution"
            dist.mkdir(parents=True)
            (dist / "gtm-plan.md").write_text(
                "---\nstatus: draft\n---\n"
                "## 1. One-Line Positioning\n\n"
                "The AI running coach for beginners.\n\n"
                "last_updated: 2026-05-28\n",
                encoding="utf-8",
            )
            gtm = cli.parse_gtm(Path(d))
            self.assertTrue(gtm["exists"])
            self.assertEqual(gtm["status"], "draft")
            self.assertIn("running coach", gtm["positioning"])
            self.assertEqual(gtm["path"], ".agent-os/distribution/gtm-plan.md")
            self.assertEqual(gtm["lastUpdated"], "2026-05-28")

    def test_parse_gtm_absent(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertFalse(cli.parse_gtm(Path(d))["exists"])

    def test_parse_gtm_missing_path(self):
        self.assertFalse(cli.parse_gtm(Path("/nonexistent/xyz123"))["exists"])


class TestPlans(unittest.TestCase):
    def test_collect_plans_finds_and_sorts(self):
        with tempfile.TemporaryDirectory() as d:
            plans_dir = Path(d) / "docs" / "superpowers" / "plans"
            plans_dir.mkdir(parents=True)
            (plans_dir / "2026-06-03-build-8.md").write_text("# Build 8 resubmission\nbody", encoding="utf-8")
            (plans_dir / "2026-05-01-old-plan.md").write_text("# Old plan\nbody", encoding="utf-8")
            (plans_dir / "README.md").write_text("# Index\n", encoding="utf-8")  # skipped as noise
            dist = Path(d) / ".agent-os" / "distribution"
            dist.mkdir(parents=True)
            (dist / "gtm-plan.md").write_text("---\nstatus: draft\n---\n# GTM Plan\nlast_updated: 2026-05-28\n", encoding="utf-8")
            plans = cli.collect_plans(Path(d))
            titles = [p["title"] for p in plans]
            self.assertIn("Build 8 resubmission", titles)
            self.assertIn("GTM Plan", titles)
            self.assertNotIn("Index", titles)  # README skipped
            # newest first
            self.assertEqual(plans[0]["date"], "2026-06-03")
            gtm = next(p for p in plans if p["kind"] == "gtm")
            self.assertEqual(gtm["status"], "draft")

    def test_collect_plans_missing_path(self):
        self.assertEqual(cli.collect_plans(Path("/nonexistent/xyz123")), [])

    def test_build_saved_plans_keeps_gtm_and_counts(self):
        plans = [{"title": f"P{i}", "path": f"docs/plans/p{i}.md", "date": f"2026-06-0{i%9}", "kind": "plan", "status": None} for i in range(1, 9)]
        plans.append({"title": "GTM", "path": ".agent-os/distribution/gtm-plan.md", "date": "2026-01-01", "kind": "gtm", "status": "draft"})
        health = [{"id": "runsmart-ios", "name": "RunSmart iOS", "plans": plans}]
        board = cli.build_saved_plans(health)
        self.assertEqual(board[0]["total"], 9)
        # GTM (old, kind=gtm) is always kept even though it is past the recent cap
        self.assertTrue(any(p["kind"] == "gtm" for p in board[0]["plans"]))


class TestDerivedSummary(unittest.TestCase):
    def _health(self):
        return [
            {
                "id": "runsmart-ios",
                "name": "RunSmart iOS",
                "state": "App Store Review",
                "nextAction": "Monitor build 8 review",
                "blockers": ["Apple review outcome is external"],
                "dirty": False,
                "freshestDate": "2026-06-03",
                "gtm": {"exists": True, "positioning": "AI running coach", "status": "draft", "path": ".agent-os/distribution/gtm-plan.md"},
            },
            {
                "id": "resumebuilder-ios",
                "name": "Resumely iOS",
                "state": "Pre-release",
                "nextAction": "Founder runs device smoke on iPhone 13",
                "blockers": ["Device locked during session"],
                "dirty": True,
                "freshestDate": "2026-06-03",
                "gtm": {"exists": False},
            },
            {
                "id": "agentic-os",
                "name": "Agentic OS",
                "state": "Reference",
                "nextAction": "Run checks",
                "blockers": [],
                "dirty": False,
                "freshestDate": "2026-06-04",
                "gtm": {"exists": False},
            },
        ]

    def test_overall_includes_products_excludes_os(self):
        d = cli.build_derived_summary(self._health())
        self.assertIn("RunSmart iOS", d["overallStatus"])
        self.assertIn("Resumely iOS", d["overallStatus"])
        self.assertNotIn("Agentic OS", d["overallStatus"])

    def test_best_action_prefers_actionable_app(self):
        # Resumely has a real next action; RunSmart only "monitors" -> Resumely wins.
        d = cli.build_derived_summary(self._health())
        self.assertIn("Resumely iOS", d["bestNextAction"])
        self.assertIn("device smoke", d["bestNextAction"])

    def test_board_now_has_apps_and_gtm_in_later(self):
        d = cli.build_derived_summary(self._health())
        self.assertTrue(any("Founder runs device smoke" in x for x in d["priorityBoard"]["now"]))
        self.assertTrue(any("GTM ready" in x for x in d["priorityBoard"]["later"]))
        self.assertTrue(any("external" in x.lower() for x in d["priorityBoard"]["blocked"]))

    def test_empty_health_is_safe(self):
        d = cli.build_derived_summary([])
        self.assertIn("No product status", d["overallStatus"])
        self.assertEqual(d["priorityBoard"]["now"], ["Run ./agentic-os morning to refresh local status."])

    def test_derived_later_mentions_needs_next_packet(self):
        pe = {"needsNextPacket": 2}
        d = cli.build_derived_summary(self._health(), plan_execution=pe)
        self.assertTrue(any("need the next work packet" in x for x in d["priorityBoard"]["later"]))


class TestPortfolioTrust(unittest.TestCase):
    def _health(self):
        return [
            {
                "id": "runsmart-ios",
                "name": "RunSmart iOS",
                "freshness": "Fresh",
                "dirty": False,
                "sourceConfidence": "High",
            },
            {
                "id": "resumebuilder-ios",
                "name": "Resumely iOS",
                "freshness": "Stale",
                "dirty": True,
                "sourceConfidence": "Medium",
            },
        ]

    def test_synced_and_fresh_is_actionable(self):
        today_refresh = datetime.now().strftime("%Y-%m-%d 09:00 IDT")
        trust = cli.build_portfolio_trust(
            self._health(),
            {"synced": True, "notes": []},
            {"lastRefresh": today_refresh},
            {"needsNextPacket": 1},
        )
        self.assertEqual(trust["level"], "caution")
        self.assertIn("Stale", " ".join(trust["reasons"]))

    def test_unsynced_is_refresh_required(self):
        today_refresh = datetime.now().strftime("%Y-%m-%d 09:00 IDT")
        trust = cli.build_portfolio_trust(
            self._health(),
            {"synced": False, "notes": ["On branch 'feat', not main."]},
            {"lastRefresh": today_refresh},
        )
        self.assertEqual(trust["level"], "refresh_required")

    def test_dirty_apps_are_hygiene_warnings_not_evidence_failures(self):
        today_refresh = datetime.now().strftime("%Y-%m-%d 09:00 IDT")
        health = [
            {
                "id": "runsmart-ios",
                "name": "RunSmart iOS",
                "freshness": "Fresh",
                "dirty": True,
                "dirtyCount": 2,
                "extraWorktrees": 1,
                "sourceConfidence": "High",
            },
            {
                "id": "resumebuilder-ios",
                "name": "Resumely iOS",
                "freshness": "Fresh",
                "dirty": True,
                "dirtyCount": 3,
                "extraWorktrees": 7,
                "sourceConfidence": "High",
            },
        ]

        trust = cli.build_portfolio_trust(
            health,
            {"synced": True, "notes": []},
            {"lastRefresh": today_refresh},
        )

        self.assertEqual(trust["level"], "actionable")
        self.assertTrue(any("Uncommitted files" in item for item in trust["hygieneWarnings"]))
        self.assertTrue(any("Extra product worktrees" in item for item in trust["hygieneWarnings"]))


class TestPlanExecutionStatus(unittest.TestCase):
    def test_active_packet_links_gtm_plan(self):
        saved = [
            {
                "project": "Resumely iOS",
                "projectId": "resumebuilder-ios",
                "plans": [
                    {
                        "title": "GTM",
                        "path": ".agent-os/distribution/gtm-plan.md",
                        "kind": "gtm",
                    }
                ],
            }
        ]
        packets = [
            {
                "title": "WP-1 smoke",
                "status": "Active",
                "source": "BUSINESS-GTM-PLAN-V0.md Section 10",
            }
        ]
        pe = cli.build_plan_execution_status(saved, packets, cli.ROOT)
        statuses = {p["executionStatus"] for p in pe["plans"]}
        self.assertIn("active", statuses)
        self.assertTrue(all(p["executionStatus"] != "Stale" for p in pe["plans"]))

    def test_plan_without_packet_is_needs_next_packet(self):
        saved = [
            {
                "project": "RunSmart iOS",
                "projectId": "runsmart-ios",
                "plans": [
                    {"title": "Launch", "path": "docs/plans/launch-plan.md", "kind": "plan"}
                ],
            }
        ]
        pe = cli.build_plan_execution_status(saved, [], cli.ROOT)
        row = next(p for p in pe["plans"] if "launch-plan" in p["path"])
        self.assertEqual(row["executionStatus"], "needs_next_packet")
        self.assertGreaterEqual(pe["needsNextPacket"], 1)


if __name__ == "__main__":
    unittest.main()
