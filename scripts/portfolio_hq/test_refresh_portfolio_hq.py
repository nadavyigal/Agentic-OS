import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("refresh_portfolio_hq.py")
SPEC = importlib.util.spec_from_file_location("refresh_portfolio_hq", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PortfolioConsistencyTests(unittest.TestCase):
    def base_auto(self):
        return {
            "trust": {
                "level": "actionable",
                "label": "Actionable",
                "reasons": ["Repo evidence is current."],
                "hygieneWarnings": [],
            },
            "health": [
                {
                    "name": "Resumely iOS",
                    "state": "Post-launch — 1.4.1 (11) live",
                }
            ],
            "executive": {
                "operatingRead": "The founder should submit 1.4.1 next.",
                "top3": [
                    {
                        "title": "Resumely — submit 1.4.1",
                        "body": "Founder submits 1.4.1 (11) to ASC.",
                    }
                ],
            },
            "distribution": {"lastGrowthReview": "2026-07-07"},
        }

    def base_manual(self):
        return {
            "funnels": [
                {
                    "id": "resumely",
                    "steps": [
                        ["Optimization completed", 2],
                        ["Export success", 1],
                    ],
                }
            ],
            "suggestedSessions": [
                {
                    "title": "Find why 0 real people have ever exported",
                    "why": "The funnel says 0 real exports ever.",
                }
            ],
            "readouts": [
                {"app": "Resumely", "wall": "export: 0 real people ever exported"}
            ],
            "growth": {
                "note": "The last logged growth cycle is the week of 2026-06-21."
            },
        }

    def test_detects_cross_layer_contradictions(self):
        issues = MODULE.find_consistency_issues(self.base_auto(), self.base_manual())

        issue_ids = {issue["id"] for issue in issues}
        self.assertEqual(
            issue_ids,
            {"resumely-export", "resumely-live-version", "growth-review-date"},
        )

    def test_contradictions_downgrade_global_trust(self):
        auto = self.base_auto()
        issues = MODULE.find_consistency_issues(auto, self.base_manual())

        trust = MODULE.build_consistency_trust(auto["trust"], issues)

        self.assertEqual(trust["level"], "mixed")
        self.assertEqual(trust["label"], "Mixed freshness")
        self.assertIn("3 cross-layer contradiction", trust["reasons"][0])

        single_issue_trust = MODULE.build_consistency_trust(auto["trust"], issues[:1])
        self.assertIn("1 cross-layer contradiction needs review", single_issue_trust["reasons"][0])

    def test_clean_layers_preserve_actionable_trust(self):
        auto = self.base_auto()
        auto["executive"] = {"operatingRead": "", "top3": []}
        auto["distribution"] = {"lastGrowthReview": "2026-07-07"}
        manual = self.base_manual()
        manual["suggestedSessions"] = []
        manual["readouts"][0]["wall"] = "export: 1 confirmed iOS export"
        manual["growth"]["note"] = "Growth review logged 2026-07-07."

        issues = MODULE.find_consistency_issues(auto, manual)
        trust = MODULE.build_consistency_trust(auto["trust"], issues)

        self.assertEqual(issues, [])
        self.assertEqual(trust["level"], "actionable")
        self.assertEqual(trust["label"], "Actionable")


class SitePayloadTests(unittest.TestCase):
    def source_payload(self):
        return {
            "generatedAt": "2026-07-11 18:00 UTC",
            "sources": {"status": "2026-07-11", "manual": "2026-07-10"},
            "auto": {
                "trust": {"level": "mixed", "label": "Mixed freshness", "reasons": []},
                "consistencyIssues": [
                    {"id": "review", "source": "Products vs Executive", "message": "Review is historical."}
                ],
                "summary": {
                    "bestNextAction": "Re-read the Resumely funnel; see deferred-read entry above for query definition",
                    "overallStatus": "Private operating detail",
                    "mainBlockers": ["GARMIN_TEST_CLIENT_SECRET is missing"],
                },
                "health": [
                    {
                        "name": "Resumely iOS",
                        "state": "Post-launch — 1.4.1 live",
                        "nextAction": "Re-read the funnel",
                        "freshness": "Fresh",
                        "evidenceDate": "2026-07-11",
                        "dirty": False,
                        "dirtyCount": 0,
                        "branch": "main...origin/main",
                        "lastCommit": "secret detail",
                    }
                ],
                "workflows": [
                    {
                        "id": "ceo",
                        "name": "Weekly CEO review",
                        "cadence": "weekly",
                        "lastRan": "2026-07-09",
                        "how": "Picks the top three.",
                        "run": {"type": "prompt", "text": "Open /Users/founder/private.md"},
                    }
                ],
                "executive": {"ceoReviewed": "2026-07-09", "operatingRead": "Private read", "top3": []},
                "distribution": {"lastGrowthReview": "2026-07-07", "experiments": []},
                "models": {"asOf": "2026-07-10", "models": [], "matrix": [], "spendByTool": {}},
                "usage": {"generatedAt": "2026-07-10", "windowDays": 30, "totalCostUsd": 12.34},
                "prompts": [{"copyPrompt": "private"}],
            },
            "manual": {
                "activationHeadline": {"rows": [], "note": "Founder-excluded."},
                "funnels": [{"id": "resumely", "name": "Resumely", "tag": "real users", "steps": []}],
                "posthogDashboards": [{
                    "id": "resumely", "product": "Resumely",
                    "url": "https://us.posthog.com/project/1/dashboard/2",
                    "decisionSnapshot": "0/73", "exclusions": "Founder",
                    "cohortCutoff": "2026-07-12", "refreshedAt": "2026-07-12",
                    "warning": "Different window",
                }],
                "clocks": [{"date": "2026-07-25", "what": "Activation read", "state": "running"}],
            },
        }

    def test_founder_site_payload_omits_execution_and_local_details(self):
        payload = MODULE.build_site_payload(self.source_payload(), "founder")
        encoded = MODULE.json.dumps(payload)

        self.assertEqual(payload["audience"], "founder")
        self.assertEqual(payload["products"][0]["name"], "Resumely iOS")
        self.assertEqual(payload["command"]["bestNextAction"], "Re-read the Resumely funnel.")
        self.assertNotIn("/Users/", encoded)
        self.assertNotIn("copyPrompt", encoded)
        self.assertNotIn("branch", encoded)
        self.assertNotIn("GARMIN_TEST_CLIENT_SECRET", encoded)
        self.assertEqual(
            payload["numbers"]["posthogDashboards"][0]["url"],
            "https://us.posthog.com/project/1/dashboard/2",
        )

    def test_team_and_public_payloads_are_progressively_narrower(self):
        source = self.source_payload()
        team = MODULE.build_site_payload(source, "team")
        public = MODULE.build_site_payload(source, "public")

        self.assertNotIn("executive", team)
        self.assertNotIn("usage", team)
        self.assertNotIn("posthogDashboards", team["numbers"])
        self.assertEqual(public["products"], [{"name": "Resumely iOS", "availability": "Live"}])
        self.assertNotIn("nextAction", MODULE.json.dumps(public))

    def test_artifact_registry_is_never_hosted(self):
        """The artifact registry names branches and local paths, which no hosted
        audience is allowed to carry. It is local-dashboard-only by design."""
        source = self.source_payload()
        source["manual"]["artifacts"] = {
            "note": "Storage truth, not quality.",
            "groups": [{
                "name": "Resumely FTUX",
                "items": [{
                    "title": "First-time-user journey audit",
                    "what": "The audit behind the 13-story plan.",
                    "url": "https://github.com/x/y/blob/docs/ftux-audit-rescue/docs/audits/a.md",
                    "local": "/Users/founder/repo/docs/audits/a.md",
                    "state": "branch-only",
                }],
            }],
        }
        for audience in MODULE.SITE_AUDIENCES:
            payload = MODULE.build_site_payload(source, audience)
            encoded = MODULE.json.dumps(payload)
            self.assertNotIn("artifacts", payload, f"{audience} must not host the registry")
            self.assertNotIn("ftux-audit-rescue", encoded)
            self.assertNotIn("/Users/", encoded)

    def test_rejects_unknown_site_audience(self):
        with self.assertRaises(ValueError):
            MODULE.build_site_payload(self.source_payload(), "customers")


if __name__ == "__main__":
    unittest.main()
