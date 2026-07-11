#!/usr/bin/env python3
"""Hermetic unit tests for the Agentic OS status parser.

No external repos, git, or network. Fixtures are written to temp dirs so the parser
pipeline is regression-proof. Run with `./agentic-os test` or `python3 -m unittest`.
"""
from __future__ import annotations

import tempfile
import unittest
import os
import json
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

    def test_current_weekly_review_preserves_executive_dashboard(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            executive = root / "executive-os"
            executive.mkdir()
            dashboard = executive / "EXECUTIVE-DASHBOARD.md"
            dashboard.write_text("manual weekly judgment\n", encoding="utf-8")
            (executive / "WEEKLY-CEO-LATEST.md").write_text(
                f"# Review\n\n- Reviewed: {datetime.now().strftime('%Y-%m-%d')}\n",
                encoding="utf-8",
            )
            original_root = cli.ROOT
            cli.ROOT = root
            try:
                cli.write_executive_dashboard(
                    {
                        "metadata": {"lastUpdated": "2026-06-05"},
                        "summary": {},
                        "executiveBoard": {},
                        "projectHealth": [],
                        "priorityBoard": {},
                    }
                )
            finally:
                cli.ROOT = original_root
            self.assertEqual(dashboard.read_text(encoding="utf-8"), "manual weekly judgment\n")

    def test_stale_weekly_review_allows_executive_dashboard_refresh(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            executive = root / "executive-os"
            executive.mkdir()
            dashboard = executive / "EXECUTIVE-DASHBOARD.md"
            dashboard.write_text("stale judgment\n", encoding="utf-8")
            stale_date = (datetime.now() - timedelta(days=8)).strftime("%Y-%m-%d")
            (executive / "WEEKLY-CEO-LATEST.md").write_text(
                f"# Review\n\n- Reviewed: {stale_date}\n",
                encoding="utf-8",
            )
            original_root = cli.ROOT
            cli.ROOT = root
            try:
                cli.write_executive_dashboard(
                    {
                        "metadata": {"lastUpdated": "2026-06-05"},
                        "summary": {"overallStatus": "Current status"},
                        "executiveBoard": {},
                        "projectHealth": [],
                        "priorityBoard": {},
                    }
                )
            finally:
                cli.ROOT = original_root
            self.assertIn("# Executive Dashboard", dashboard.read_text(encoding="utf-8"))


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
    def test_private_plugins_are_discovered(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            plugin = root / "plugins" / "founder-os"
            skills = plugin / "skills"
            manifest = plugin / ".codex-plugin"
            skills.mkdir(parents=True)
            manifest.mkdir(parents=True)
            (manifest / "plugin.json").write_text(
                json.dumps(
                    {
                        "name": "founder-os",
                        "version": "0.1.0",
                        "description": "Founder operating workflows.",
                    }
                ),
                encoding="utf-8",
            )
            (skills / "morning-brief" ).mkdir()
            (skills / "morning-brief" / "SKILL.md").write_text(
                "# Morning Brief\n\nChoose the next evidence-backed action.\n",
                encoding="utf-8",
            )

            registry = cli.build_os_registry(root)

            self.assertEqual(registry["plugins"][0]["name"], "founder-os")
            self.assertEqual(registry["plugins"][0]["skillCount"], 1)
            self.assertEqual(
                registry["plugins"][0]["path"],
                "plugins/founder-os/.codex-plugin/plugin.json",
            )

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

    def test_packet_frontmatter_status_overrides_stale_body_status(self):
        with tempfile.TemporaryDirectory() as d:
            packets = Path(d) / "executive-os" / "work-packets"
            packets.mkdir(parents=True)
            (packets / "WP-7.md").write_text(
                "---\n"
                "title: Work Packet: Closed But Old Body\n"
                "status: closed\n"
                "---\n\n"
                "# Work Packet — Closed But Old Body\n\n"
                "- Status: Active\n"
                "- Source: old dashboard\n\n"
                "## Goal\nDo not resurface this as active.\n",
                encoding="utf-8",
            )

            packet = cli.build_os_registry(Path(d))["workPackets"][0]

            self.assertEqual(packet["status"], "closed")
            self.assertFalse(cli._packet_is_active(packet))
            self.assertIsNone(packet["copyPrompt"])

    def test_resumebuilder_web_packet_routes_to_web_repo_id(self):
        with tempfile.TemporaryDirectory() as d:
            packets = Path(d) / "executive-os" / "work-packets"
            packets.mkdir(parents=True)
            (packets / "WP-19.md").write_text(
                "# Work Packet WP-19\n"
                "- Status: Active\n\n"
                "## Project\nResumeBuilder AI (Web)\n"
                "Path: `/Users/example/ResumeBuilder/new-ResumeBuilder-ai-`\n",
                encoding="utf-8",
            )

            packet = cli.build_os_registry(Path(d))["workPackets"][0]

            self.assertEqual(packet["repoId"], "resumebuilder-ai")

    def test_packet_hygiene_flags_active_older_runsmart_build(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            packets = root / "executive-os" / "work-packets"
            packets.mkdir(parents=True)
            (packets / "WP-3.md").write_text(
                "# Work Packet WP-3 - RunSmart Build 12 Resubmission\n"
                "- Status: Active\n\n"
                "## Project\nRunSmart iOS\n"
                "Path: `/Users/example/IOS RunSmart app`\n\n"
                "## Goal\nPrepare build 12.\n",
                encoding="utf-8",
            )
            status = {
                "projectHealth": [
                    {
                        "name": "RunSmart iOS",
                        "state": "1.0.2 build 14 resubmission prep",
                        "nextAction": "Archive build 14",
                    }
                ],
                "executiveLoop": {"workPackets": cli.build_os_registry(root)["workPackets"]},
            }

            issues = cli.build_packet_hygiene(status, root)

            self.assertEqual(issues[0]["severity"], "error")
            self.assertIn("current RunSmart status is build 14", issues[0]["message"])

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
                "- Workflow pattern: adversarial-review\n"
                "- Input trust: untrusted\n"
                "- Outcome loop: resumely-submission\n"
                "- Loop: Resumely submission readiness loop\n"
                "- Signal: signed smoke evidence requested\n"
                "- Memory update: tasks/progress.md\n"
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

            self.assertEqual(packet["workflowPattern"], "adversarial-review")
            self.assertEqual(packet["inputTrust"], "untrusted")
            self.assertEqual(packet["outcomeLoop"], "resumely-submission")
            self.assertEqual(packet["loop"], "Resumely submission readiness loop")
            self.assertEqual(packet["signal"], "signed smoke evidence requested")
            self.assertEqual(packet["memoryUpdate"], "tasks/progress.md")
            self.assertEqual(packet["successSignal"], "signed smoke evidence exists")
            self.assertEqual(loop["status"], "active")
            self.assertEqual(loop["owner"], "COO OS")
            self.assertEqual(loop["resultMetric"], "App Store status is Ready for Sale")
            self.assertEqual(checkpoint["status"], "ready-for-promotion")
            self.assertEqual(checkpoint["topic"], "AI Audit offer")
            self.assertEqual(len(registry["outcomeLoops"]), 1)
            self.assertEqual(len(registry["contextCheckpoints"]), 1)

    def test_brainstorm_checkpoints_are_discovered(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            brainstorms = root / "brainstorms"
            brainstorms.mkdir()
            (brainstorms / "README.md").write_text("# Brainstorms\n", encoding="utf-8")
            (brainstorms / "2026-06-06-ai-audit.md").write_text(
                "# Context Checkpoint: AI Audit\n"
                "- Status: open\n"
                "- Topic: AI Audit Toolkit\n"
                "- Purpose: capture offer context\n"
                "- Created: 2026-06-06\n"
                "- Last updated: 2026-06-06\n",
                encoding="utf-8",
            )

            checkpoint = cli.build_os_registry(root)["contextCheckpoints"][0]

            self.assertEqual(checkpoint["topic"], "AI Audit Toolkit")
            self.assertEqual(checkpoint["path"], "brainstorms/2026-06-06-ai-audit.md")


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
    def _health(self, *, freshness="Fresh", dirty=False, confidence="High", evidence_gap=False):
        return [
            {
                "id": "runsmart-ios",
                "name": "RunSmart iOS",
                "freshness": "Fresh",
                "dirty": False,
                "sourceConfidence": "High",
                "evidenceGap": False,
            },
            {
                "id": "resumebuilder-ios",
                "name": "Resumely iOS",
                "freshness": freshness,
                "dirty": dirty,
                "sourceConfidence": confidence,
                "evidenceGap": evidence_gap,
            },
        ]

    def test_clean_synced_fresh_apps_are_actionable(self):
        today_refresh = datetime.now().strftime("%Y-%m-%d 09:00 IDT")
        trust = cli.build_portfolio_trust(
            self._health(),
            {"synced": True, "notes": []},
            {"lastRefresh": today_refresh},
        )
        self.assertEqual(trust["level"], "actionable")
        self.assertIn("Sync clean, refreshed today, app evidence current.", trust["reasons"])

    def test_unsynced_is_refresh_required(self):
        today_refresh = datetime.now().strftime("%Y-%m-%d 09:00 IDT")
        trust = cli.build_portfolio_trust(
            self._health(),
            {"synced": False, "notes": ["On branch 'feat', not main."]},
            {"lastRefresh": today_refresh},
        )
        self.assertEqual(trust["level"], "refresh_required")

    def test_not_refreshed_today_is_refresh_required(self):
        yesterday_refresh = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d 09:00 IDT")
        trust = cli.build_portfolio_trust(
            self._health(),
            {"synced": True, "notes": []},
            {"lastRefresh": yesterday_refresh},
        )
        self.assertEqual(trust["level"], "refresh_required")
        self.assertIn("Morning refresh was not run today.", trust["reasons"])

    def test_stale_shippable_app_is_refresh_required(self):
        today_refresh = datetime.now().strftime("%Y-%m-%d 09:00 IDT")
        trust = cli.build_portfolio_trust(
            self._health(freshness="Stale"),
            {"synced": True, "notes": []},
            {"lastRefresh": today_refresh},
        )
        self.assertEqual(trust["level"], "refresh_required")
        self.assertTrue(any("Stale shippable app evidence" in reason for reason in trust["reasons"]))

    def test_dirty_shippable_app_is_caution(self):
        today_refresh = datetime.now().strftime("%Y-%m-%d 09:00 IDT")
        trust = cli.build_portfolio_trust(
            self._health(dirty=True),
            {"synced": True, "notes": []},
            {"lastRefresh": today_refresh},
        )

        self.assertEqual(trust["level"], "caution")
        self.assertTrue(any("Dirty shippable app repo" in reason for reason in trust["reasons"]))
        self.assertTrue(any("Uncommitted files" in item for item in trust["hygieneWarnings"]))

    def test_needs_next_packet_alone_does_not_downgrade(self):
        today_refresh = datetime.now().strftime("%Y-%m-%d 09:00 IDT")
        trust = cli.build_portfolio_trust(
            self._health(),
            {"synced": True, "notes": []},
            {"lastRefresh": today_refresh},
            {"needsNextPacket": 3},
        )
        self.assertEqual(trust["level"], "actionable")
        self.assertTrue(any("need the next work packet" in reason for reason in trust["reasons"]))

    def test_low_confidence_shippable_app_is_caution(self):
        today_refresh = datetime.now().strftime("%Y-%m-%d 09:00 IDT")
        trust = cli.build_portfolio_trust(
            self._health(confidence="Unknown"),
            {"synced": True, "notes": []},
            {"lastRefresh": today_refresh},
        )
        self.assertEqual(trust["level"], "caution")

    def test_evidence_gap_shippable_app_is_caution(self):
        today_refresh = datetime.now().strftime("%Y-%m-%d 09:00 IDT")
        trust = cli.build_portfolio_trust(
            self._health(evidence_gap=True),
            {"synced": True, "notes": []},
            {"lastRefresh": today_refresh},
        )
        self.assertEqual(trust["level"], "caution")

    def test_contradiction_forces_refresh_required(self):
        today_refresh = datetime.now().strftime("%Y-%m-%d 09:00 IDT")
        trust = cli.build_portfolio_trust(
            self._health(),
            {"synced": True, "notes": []},
            {"lastRefresh": today_refresh},
            {},
            [{"severity": "hard", "message": "Reality mismatch"}],
        )
        self.assertEqual(trust["level"], "refresh_required")
        self.assertTrue(any("contradicts reality" in reason.lower() for reason in trust["reasons"]))


class TestGroundTruthContradictions(unittest.TestCase):
    def test_posthog_live_users_contradict_in_review_for_both_apps_and_force_refresh_required(self):
        old = os.environ.get(cli.GROUND_TRUTH_OVERRIDES_ENV)
        old_state = os.environ.get(cli.APP_STORE_STATE_ENV)
        os.environ.pop(cli.APP_STORE_STATE_ENV, None)
        os.environ[cli.GROUND_TRUTH_OVERRIDES_ENV] = (
            '{"posthog":{"runsmart-ios":{"liveUsers7d":6},'
            '"resumebuilder-ios":{"liveUsers7d":12}},"appStore":{}}'
        )
        try:
            with tempfile.TemporaryDirectory() as d:
                root = Path(d)
                runsmart_dir = root / "runsmart"
                resumely_dir = root / "resumely"
                runsmart_dir.mkdir()
                resumely_dir.mkdir()
                evidence = [
                    cli.ProjectEvidence(
                        project_id="runsmart-ios",
                        name="RunSmart iOS",
                        path=runsmart_dir,
                        exists=True,
                        branch="main",
                        dirty=False,
                        dirty_count=0,
                        extra_worktrees=0,
                        last_commit="2026-06-15 deadbeef test",
                        source_files=[],
                        task_parse=cli.empty_task_parse(),
                    ),
                    cli.ProjectEvidence(
                        project_id="resumebuilder-ios",
                        name="Resumely iOS",
                        path=resumely_dir,
                        exists=True,
                        branch="main",
                        dirty=False,
                        dirty_count=0,
                        extra_worktrees=0,
                        last_commit="2026-06-15 feedface test",
                        source_files=[],
                        task_parse=cli.empty_task_parse(),
                    ),
                ]
                health = [
                    {
                        "id": "runsmart-ios",
                        "name": "RunSmart iOS",
                        "state": "1.0.2 build 15 in review",
                        "parsedLastUpdated": "2026-06-15",
                        "freshestDate": "2026-06-15",
                        "freshness": "Fresh",
                        "dirty": False,
                        "sourceConfidence": "High",
                        "evidenceGap": False,
                    },
                    {
                        "id": "resumebuilder-ios",
                        "name": "Resumely iOS",
                        "state": "In App Store review (build 4)",
                        "parsedLastUpdated": "2026-06-16",
                        "freshestDate": "2026-06-16",
                        "freshness": "Fresh",
                        "dirty": False,
                        "sourceConfidence": "High",
                        "evidenceGap": False,
                    },
                ]
                truth = cli.build_ground_truth(evidence, health)
                hard = [item for item in truth["contradictions"] if item["severity"] == "hard"]
                self.assertEqual(2, len(hard))
                self.assertTrue(any("RunSmart" in item["message"] for item in hard))
                self.assertTrue(any("Resumely" in item["message"] for item in hard))
                self.assertTrue(any("PostHog shows 6 live users" in item["message"] for item in hard))
                self.assertTrue(any("PostHog shows 12 live users" in item["message"] for item in hard))
                trust = cli.build_portfolio_trust(
                    health,
                    {"synced": True, "notes": []},
                    {"lastRefresh": datetime.now().strftime("%Y-%m-%d 09:00 IDT")},
                    {},
                    truth["contradictions"],
                )
                self.assertEqual(trust["level"], "refresh_required")
        finally:
            if old is None:
                os.environ.pop(cli.GROUND_TRUTH_OVERRIDES_ENV, None)
            else:
                os.environ[cli.GROUND_TRUTH_OVERRIDES_ENV] = old
            if old_state is None:
                os.environ.pop(cli.APP_STORE_STATE_ENV, None)
            else:
                os.environ[cli.APP_STORE_STATE_ENV] = old_state

    def test_app_store_states_accept_raw_env_strings(self):
        old_key = os.environ.get(cli.POSTHOG_KEY_ENV)
        old_state = os.environ.get(cli.APP_STORE_STATE_ENV)
        old_override = os.environ.get(cli.GROUND_TRUTH_OVERRIDES_ENV)
        os.environ.pop(cli.POSTHOG_KEY_ENV, None)
        os.environ.pop(cli.GROUND_TRUTH_OVERRIDES_ENV, None)
        os.environ[cli.APP_STORE_STATE_ENV] = '{"runsmart-ios":"live","resumebuilder-ios":"live"}'
        try:
            with tempfile.TemporaryDirectory() as d:
                root = Path(d)
                runsmart_dir = root / "runsmart"
                resumely_dir = root / "resumely"
                runsmart_dir.mkdir()
                resumely_dir.mkdir()
                evidence = [
                    cli.ProjectEvidence(
                        project_id="runsmart-ios",
                        name="RunSmart iOS",
                        path=runsmart_dir,
                        exists=True,
                        branch="main",
                        dirty=False,
                        dirty_count=0,
                        extra_worktrees=0,
                        last_commit="2026-06-15 deadbeef test",
                        source_files=[],
                        task_parse=cli.empty_task_parse(),
                    ),
                    cli.ProjectEvidence(
                        project_id="resumebuilder-ios",
                        name="Resumely iOS",
                        path=resumely_dir,
                        exists=True,
                        branch="main",
                        dirty=False,
                        dirty_count=0,
                        extra_worktrees=0,
                        last_commit="2026-06-15 feedface test",
                        source_files=[],
                        task_parse=cli.empty_task_parse(),
                    ),
                ]
                health = [
                    {"id": "runsmart-ios", "name": "RunSmart iOS", "state": "Live on the App Store"},
                    {"id": "resumebuilder-ios", "name": "Resumely iOS", "state": "Live on the App Store"},
                ]

                truth = cli.build_ground_truth(evidence, health)

                self.assertEqual([], truth["contradictions"])
                self.assertEqual(["live", "live"], [item["state"] for item in truth["appStore"]])
                self.assertNotIn(
                    "App Store state missing for RunSmart (set AGENTIC_OS_APPSTORE_STATES)",
                    truth["unavailable"],
                )
                self.assertNotIn(
                    "App Store state missing for Resumely (set AGENTIC_OS_APPSTORE_STATES)",
                    truth["unavailable"],
                )
        finally:
            if old_key is None:
                os.environ.pop(cli.POSTHOG_KEY_ENV, None)
            else:
                os.environ[cli.POSTHOG_KEY_ENV] = old_key
            if old_state is None:
                os.environ.pop(cli.APP_STORE_STATE_ENV, None)
            else:
                os.environ[cli.APP_STORE_STATE_ENV] = old_state
            if old_override is None:
                os.environ.pop(cli.GROUND_TRUTH_OVERRIDES_ENV, None)
            else:
                os.environ[cli.GROUND_TRUTH_OVERRIDES_ENV] = old_override


class TestFounderNextActions(unittest.TestCase):
    def test_refresh_required_blocks_next_actions(self):
        status = {
            "portfolioTrust": {"level": "refresh_required"},
            "projectHealth": [],
            "executiveLoop": {
                "workPackets": [
                    {"title": "Real packet", "status": "Active", "repoId": "agentic-os"}
                ]
            },
        }

        actions = cli.build_founder_next_actions(status)

        self.assertEqual(actions, [{
            "title": "Restore dashboard trust",
            "detail": "Fix the sync or freshness warning, then run ./agentic-os morning again.",
            "type": "system",
        }])

    def test_caution_allows_real_next_actions(self):
        status = {
            "portfolioTrust": {
                "level": "caution",
                "reasons": ["Dirty shippable app repo: RunSmart iOS."],
            },
            "projectHealth": [],
            "executiveLoop": {
                "workPackets": [
                    {
                        "title": "Work Packet — Reconcile Fit/Match",
                        "status": "Active",
                        "repoId": "resumebuilder-ai",
                        "repoPath": "/tmp/resumebuilder-ai",
                        "copyPrompt": "Do the work.",
                    }
                ]
            },
            "planExecution": {},
        }

        actions = cli.build_founder_next_actions(status)

        self.assertEqual(actions[0]["title"], "Run active packet: Work Packet — Reconcile Fit/Match")
        self.assertEqual(actions[-1]["title"], "Validate caution items before risky moves")

    def test_fresh_coo_review_replaces_repeat_review_suggestion(self):
        status = {
            "portfolioTrust": {"level": "actionable"},
            "projectHealth": [
                {"id": "runsmart-ios", "name": "RunSmart iOS", "state": "App Store Review"},
                {"id": "resumebuilder-ios", "name": "Resumely iOS", "state": "App Store Review"},
            ],
            "executiveLoop": {"workPackets": []},
            "planExecution": {"needsNextPacket": 2},
            "latestCooReview": {
                "reviewed": datetime.now().strftime("%Y-%m-%d"),
                "selectedNextAction": "Draft the launch post.",
                "actionType": "global-OS",
            },
        }

        actions = cli.build_founder_next_actions(status)

        self.assertEqual(actions[0]["title"], "Check App Store Connect")
        self.assertEqual(actions[1]["title"], "Continue the COO-selected action")
        self.assertIn("Agentic OS repo", actions[1]["where"])
        self.assertTrue(actions[1]["copyPrompt"])
        self.assertFalse(any(action["title"] == "Run a COO operating review" for action in actions))

    def test_completed_coo_review_does_not_become_next_action(self):
        status = {
            "portfolioTrust": {"level": "actionable"},
            "projectHealth": [],
            "executiveLoop": {"workPackets": []},
            "planExecution": {"needsNextPacket": 1},
            "latestCooReview": {
                "reviewed": datetime.now().strftime("%Y-%m-%d"),
                "selectedNextAction": "Completed - PR #97 merged to main.",
                "actionType": "global-OS",
            },
        }

        actions = cli.build_founder_next_actions(status)

        self.assertEqual(actions[0]["title"], "Run a COO operating review")
        self.assertFalse(any(action["title"] == "Continue the COO-selected action" for action in actions))

    def test_missing_coo_review_suggests_review_when_plans_need_packets(self):
        status = {
            "portfolioTrust": {"level": "actionable"},
            "projectHealth": [],
            "executiveLoop": {"workPackets": []},
            "planExecution": {"needsNextPacket": 1},
            "latestCooReview": None,
        }

        actions = cli.build_founder_next_actions(status)

        self.assertEqual(actions[0]["title"], "Run a COO operating review")


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


class TestStrandedWork(unittest.TestCase):
    def test_unpushed_branch_becomes_actionable_item(self):
        stranded = {
            "unpushedBranches": [
                {"branch": "fix/login", "ahead": 2, "lastCommitDate": "2026-06-10"}
            ],
            "unmergedLocalBranches": [],
            "staleMergedBranchCount": 0,
            "extraWorktrees": [],
            "defaultBranchIssues": [],
        }
        items = cli.summarize_stranded_work("RunSmart Web", stranded, dirty_count=0)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["type"], "unpushed")
        self.assertIn("fix/login", items[0]["detail"])
        self.assertIn("2 unpushed commit(s)", items[0]["detail"])
        self.assertIn("open a PR", items[0]["action"])

    def test_default_branch_issue_listed_first(self):
        stranded = {
            "unpushedBranches": [
                {"branch": "feat/x", "ahead": 1, "lastCommitDate": "2026-06-09"}
            ],
            "unmergedLocalBranches": [],
            "staleMergedBranchCount": 0,
            "extraWorktrees": [],
            "defaultBranchIssues": ["main has 1 unpushed commit(s)"],
        }
        items = cli.summarize_stranded_work("ResumeBuilder AI (Web)", stranded, dirty_count=0)
        self.assertEqual(items[0]["type"], "default-branch")
        self.assertIn("main has 1 unpushed commit(s)", items[0]["detail"])

    def test_local_only_worktree_dirty_and_cleanup_items(self):
        stranded = {
            "unpushedBranches": [],
            "unmergedLocalBranches": [
                {"branch": "claude/lost-work", "reason": "never pushed", "lastCommitDate": "2026-06-05"}
            ],
            "staleMergedBranchCount": 3,
            "extraWorktrees": [
                {"path": "/tmp/wt", "branch": "claude/wt-branch", "dirtyCount": 2}
            ],
            "defaultBranchIssues": [],
        }
        items = cli.summarize_stranded_work("ResumeBuilder iOS", stranded, dirty_count=1)
        types = [i["type"] for i in items]
        self.assertEqual(types, ["local-only", "worktree", "dirty", "cleanup"])
        worktree_item = items[1]
        self.assertIn("2 uncommitted file(s)", worktree_item["detail"])
        cleanup_item = items[3]
        self.assertIn("3 merged branch(es)", cleanup_item["detail"])

    def test_clean_repo_yields_no_items(self):
        stranded = {
            "unpushedBranches": [],
            "unmergedLocalBranches": [],
            "staleMergedBranchCount": 0,
            "extraWorktrees": [],
            "defaultBranchIssues": [],
        }
        self.assertEqual(cli.summarize_stranded_work("RunSmart iOS", stranded, 0), [])

    def test_missing_keys_are_tolerated(self):
        self.assertEqual(cli.summarize_stranded_work("Atlas", {}, 0), [])


class TestCleanupPolicy(unittest.TestCase):
    def test_founder_branches_are_never_touched(self):
        self.assertEqual(cli.decide_cleanup_action("main", False, True), "skip")
        self.assertEqual(cli.decide_cleanup_action("monetization", False, False), "skip")
        self.assertEqual(cli.decide_cleanup_action("feature/paywall", True, False), "skip")
        self.assertEqual(cli.decide_cleanup_action("docs/launch", False, True), "skip")

    def test_merged_clean_agent_branch_is_deleted(self):
        self.assertEqual(cli.decide_cleanup_action("claude/old-session", False, True), "delete")
        self.assertEqual(cli.decide_cleanup_action("codex/done-task", False, True), "delete")

    def test_unmerged_agent_branch_is_backed_up_not_deleted(self):
        self.assertEqual(cli.decide_cleanup_action("claude/wip-session", False, False), "backup")

    def test_dirty_agent_worktree_is_backed_up_even_if_merged(self):
        self.assertEqual(cli.decide_cleanup_action("claude/messy", True, True), "backup")


if __name__ == "__main__":
    unittest.main()
