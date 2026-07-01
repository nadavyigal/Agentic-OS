# OS Improvement Plan Completion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Finish the 3 remaining problems from `OS-IMPROVEMENT-PLAN-2026-06-30.md` (Problem 3: evidence-before-done, Problem 5: compound-don't-accrete workflow checklist, WP-22: INTENT-LOG auto-capture) so the plan is fully closed instead of sitting at partial completion.

**Architecture:** Two doc-only edits (Problem 3, Problem 5) followed by a three-part automation build for WP-22: a standalone theme-clustering script, a Stop hook that nudges Claude to keep INTENT-LOG.md and its clusters current, and a non-blocking hook-health check surfaced at the top of `./agentic-os morning`. WP-22's design deliberately mirrors the existing `update-progress.sh` Stop hook: the hook never writes the log entry itself (a bash script cannot paraphrase intent), it only detects the gap and emits a `systemMessage` so Claude fills it in during the same session — this is what makes it survive the "manual practices die in 30 days" failure mode (`LESSONS.md`) instead of repeating it.

**Tech Stack:** Markdown (docs), Bash (Stop hook, matches `~/.claude/hooks/update-progress.sh` conventions), Python 3 stdlib only (`scripts/agentic_os/cli.py` conventions — `unittest`, no third-party deps), JSON (`~/.claude/settings.json`).

## Global Constraints

- This repo is markdown-first with a Python CLI; there is no pytest suite. Verification is `git diff --check`, targeted file reads, and `python3 -m unittest` for the two Python modules touched here, per `AGENTS.md` "Definition of Done" in this repo.
- No new dependencies. `intent_cluster.py` must be stdlib-only, matching the existing note in `INTENT-LOG.md`: "Write `intent_cluster.py` (standalone, no dependencies)."
- Follow the repo's em-dash-free style: use `-` not `—` in all new content (deviates from the em dash shown in `INTENT-LOG.md`'s own draft spec text, intentionally).
- Every work packet / backlog-style artifact created here gets a `Mode:` field per the Mode Contracts added to `AGENTS.md` on 2026-07-01. Doc-only tasks are `Mode: Maintainer` (tightening existing rules, no new functionality). The script + hook build is `Mode: Builder`.
- Do not touch `scripts/agentic_os/cli.py`'s `run_tests()` loader or `test_cli.py` — `check_hook_health()` gets its own manual verification command, not a new entry in the existing test file, to keep this plan's blast radius to the files it lists.
- Stop hook scripts in this repo are fail-open and silent on success (see `~/.claude/hooks/update-progress.sh`). The new hook follows the same convention: no output, exit 0, when nothing needs attention.

---

## Task 1: Evidence-before-done lesson (Problem 3)

**Files:**
- Modify: `LESSONS.md:15-21` (append one lesson line to the index, before the blank line that precedes `## Lesson Template`)
- Modify: `GLOBAL-QA-RULES.md:5-13` (extend the "Completion Evidence" section with an AI-facing-feature requirement)

**Interfaces:** None — doc-only, no other task depends on this one.

- [ ] **Step 1: Add the lesson line to LESSONS.md**

Open `LESSONS.md`. Find this exact block (lines 17-21):

```markdown
- **Compound, don't accrete** — before creating a new file, check if a living page for the subject exists. If yes, update it; use the new content as the dated evidence note. Hub pages stale by more than 7 days degrade trust in the whole OS. (Recurring wiki drift 2026-06-30.)

## Lesson Template
```

Replace it with:

```markdown
- **Compound, don't accrete** — before creating a new file, check if a living page for the subject exists. If yes, update it; use the new content as the dated evidence note. Hub pages stale by more than 7 days degrade trust in the whole OS. (Recurring wiki drift 2026-06-30.)
- **Done requires evidence, not completion** — "the feature works" is not evidence. Lint pass, test output, or a PostHog event confirmed in the dashboard is evidence. Log the evidence in the INTENT-LOG entry or the session summary. (Evidence-before-commit theme, 6 of 28 backfilled sessions, 2026-06-30.)

## Lesson Template
```

- [ ] **Step 2: Verify the edit**

Run: `grep -n "Done requires evidence" LESSONS.md`
Expected: one match, on its own line, directly above `## Lesson Template`.

- [ ] **Step 3: Extend GLOBAL-QA-RULES.md**

Open `GLOBAL-QA-RULES.md`. Find this exact block (lines 5-13):

```markdown
## Completion Evidence

Every completion claim must include evidence:

- Tests run and results.
- Build or lint results when relevant.
- Visual QA for UI changes.
- Manual flow checks for user-facing behavior.
- Known gaps or skipped verification.
```

Replace it with:

```markdown
## Completion Evidence

Every completion claim must include evidence:

- Tests run and results.
- Build or lint results when relevant.
- Visual QA for UI changes.
- Manual flow checks for user-facing behavior.
- Known gaps or skipped verification.
- For any AI-facing feature: a PostHog event confirmed in the dashboard, or a test asserting it fires, before the story is closed. "The AI call works" without a captured event is not sufficient evidence.
```

- [ ] **Step 4: Verify the edit**

Run: `grep -n "PostHog event confirmed" GLOBAL-QA-RULES.md`
Expected: one match, inside the Completion Evidence bullet list.

- [ ] **Step 5: Commit**

```bash
git add LESSONS.md GLOBAL-QA-RULES.md
git commit -m "docs: close Problem 3 (evidence-before-done) from OS-IMPROVEMENT-PLAN-2026-06-30

Mode: Maintainer"
```

---

## Task 2: Post-Session checklist (Problem 5 remainder)

**Files:**
- Modify: `GLOBAL-WORKFLOWS.md` (new section — no `## Post-Session` heading exists yet; confirmed via `grep -n "^## " GLOBAL-WORKFLOWS.md`)

**Interfaces:** None.

- [ ] **Step 1: Read the file end to confirm insertion point**

Run: `tail -20 GLOBAL-WORKFLOWS.md`

You are looking for the last `## ` heading in the file (currently `## Input Trust`, per the grep above). The new section goes after the file's last line.

- [ ] **Step 2: Append the new section**

Append this exact block to the end of `GLOBAL-WORKFLOWS.md`:

```markdown

## Post-Session Checklist

Run through this before ending any session that touched more than one file (skip for single-file typo fixes):

- Did any living page's `Current State` block become stale because of this session's work? If yes, update it now — do not leave the update for a future session.
- Did any decision get written to a dated note but not to `DECISIONS.md`? If yes, mirror it now.
- Is there an uncommitted `INTENT-LOG.md` entry for today? If the Stop hook flagged one, write it before the session closes.

This checklist exists because "compound, don't accrete" (`LESSONS.md`) and "manual practices die in 30 days" (`GLOBAL-SELF-IMPROVEMENT.md` Automation Gate) both showed the same failure mode: work that should update a durable source instead sat in a dated note nobody revisited.
```

- [ ] **Step 3: Verify the edit**

Run: `grep -n "## Post-Session Checklist" GLOBAL-WORKFLOWS.md`
Expected: one match near the end of the file.

Run: `git diff --check GLOBAL-WORKFLOWS.md`
Expected: no output (no trailing-whitespace errors).

- [ ] **Step 4: Commit**

```bash
git add GLOBAL-WORKFLOWS.md
git commit -m "docs: close Problem 5 remainder — Post-Session Checklist in GLOBAL-WORKFLOWS.md

Mode: Maintainer"
```

---

## Task 3: intent_cluster.py (WP-22 part 1)

**Files:**
- Create: `scripts/agentic_os/intent_cluster.py`
- Create: `scripts/agentic_os/test_intent_cluster.py`

**Interfaces:**
- Produces: `entries_for_month(text: str, month: str) -> list[str]` — returns the raw `**Themes:** ...` value strings (not yet split/counted) for every INTENT-LOG entry whose date starts with `month` (format `"YYYY-MM"`).
- Produces: `cluster(month: str, log_path: Path) -> str` — reads `log_path`, appends a `## Theme Clusters - {month}` section if one doesn't already exist for that month, returns a one-line human-readable result string. Idempotent: calling it twice for the same month is a no-op the second time.
- Produces: `main() -> int` — CLI entry point, `python3 intent_cluster.py [YYYY-MM]`, defaults to the current month.
- Consumes: nothing from other tasks in this plan.
- Consumed by: Task 4's Stop hook shells out to this script by path; it does not import it.

- [ ] **Step 1: Write the failing test**

Create `scripts/agentic_os/test_intent_cluster.py`:

```python
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
        self.assertIn("2 themes across 2 entries", result)

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
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `cd scripts/agentic_os && python3 -m unittest test_intent_cluster -v`
Expected: `ModuleNotFoundError: No module named 'intent_cluster'` (the module doesn't exist yet).

- [ ] **Step 3: Write intent_cluster.py**

Create `scripts/agentic_os/intent_cluster.py`:

```python
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
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `cd scripts/agentic_os && python3 -m unittest test_intent_cluster -v`
Expected:
```
test_appends_ranked_cluster_section (test_intent_cluster.TestCluster) ... ok
test_idempotent_second_call_is_noop (test_intent_cluster.TestCluster) ... ok
test_no_entries_for_month_does_not_write (test_intent_cluster.TestCluster) ... ok
test_empty_for_month_with_no_entries (test_intent_cluster.TestEntriesForMonth) ... ok
test_extracts_only_matching_month (test_intent_cluster.TestEntriesForMonth) ... ok

Ran 5 tests in 0.0XXs

OK
```

- [ ] **Step 5: Dry-run against the real INTENT-LOG.md on a throwaway copy**

Run:
```bash
cd "/Users/nadavyigal/Documents/Projects /Agentic OS"
cp INTENT-LOG.md /tmp/INTENT-LOG-test.md
python3 -c "
from pathlib import Path
import sys
sys.path.insert(0, 'scripts/agentic_os')
import intent_cluster
print(intent_cluster.cluster('2026-06', Path('/tmp/INTENT-LOG-test.md')))
"
tail -15 /tmp/INTENT-LOG-test.md
rm /tmp/INTENT-LOG-test.md
```
Expected: a line like `Appended cluster for 2026-06: N themes across M entries.` followed by a real ranked list. This proves the regex works against the actual file, not just the fixture, without touching the real file.

- [ ] **Step 6: Commit**

```bash
git add scripts/agentic_os/intent_cluster.py scripts/agentic_os/test_intent_cluster.py
git commit -m "feat: add intent_cluster.py, closes WP-22 part 1 (theme clustering)

Mode: Builder"
```

---

## Task 4: Stop hook for INTENT-LOG freshness (WP-22 part 2)

**Files:**
- Create: `~/.claude/hooks/intent-log-check.sh`
- Modify: `~/.claude/settings.json` (add one entry to the existing `hooks.Stop[0].hooks` array)

**Interfaces:**
- Consumes: `scripts/agentic_os/intent_cluster.py` from Task 3 (referenced by path in the reminder text, not executed by the hook itself).
- Produces: nothing other tasks depend on.

- [ ] **Step 1: Write the hook script**

Create `~/.claude/hooks/intent-log-check.sh`:

```bash
#!/bin/bash
# Fires on every Claude Stop event, in whatever directory the session ran in.
# Mirrors update-progress.sh: silent on success, only speaks when action is
# needed, never writes the log itself (a bash script cannot paraphrase intent
# - that's Claude's job, prompted here instead of relying on human memory).

LOG="INTENT-LOG.md"
[ -f "$LOG" ] || exit 0

TODAY=$(date +%Y-%m-%d)
MONTH=$(date +%Y-%m)
MESSAGES=()

if ! grep -q "^## $TODAY" "$LOG"; then
  MESSAGES+=("No INTENT-LOG entry for $TODAY yet - prepend one before ending this session: paraphrased request, intent/why, 2-3 theme tags, matching the existing entry format in INTENT-LOG.md.")
fi

if ! grep -q "^## Theme Clusters - $MONTH" "$LOG"; then
  MESSAGES+=("No theme cluster for $MONTH yet - run: python3 scripts/agentic_os/intent_cluster.py")
fi

[ ${#MESSAGES[@]} -eq 0 ] && exit 0

JOINED=$(printf '%s ' "${MESSAGES[@]}")
echo "{\"systemMessage\": \"[auto] $JOINED\"}"
```

- [ ] **Step 2: Make it executable**

Run: `chmod +x ~/.claude/hooks/intent-log-check.sh`

- [ ] **Step 3: Verify it fires correctly outside the repo (should be silent)**

Run: `cd /tmp && bash ~/.claude/hooks/intent-log-check.sh; echo "exit: $?"`
Expected: no output, `exit: 0` (no `INTENT-LOG.md` in `/tmp`).

- [ ] **Step 4: Verify it fires correctly inside the repo (should report both gaps on a fresh day)**

Run:
```bash
cd "/Users/nadavyigal/Documents/Projects /Agentic OS"
bash ~/.claude/hooks/intent-log-check.sh
```
Expected: a single line of JSON containing `systemMessage`, mentioning both "No INTENT-LOG entry for <today>" and "No theme cluster for <this month>" — unless today's entry or this month's cluster already exist, in which case only the missing half (or nothing) prints. This is expected, not a bug: re-read the script's two independent `if` checks.

- [ ] **Step 5: Add the hook to settings.json**

Open `~/.claude/settings.json`. Find this exact block inside `"hooks"`:

```json
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$HOME/.claude/hooks/update-progress.sh",
            "statusMessage": "Stamping progress.md...",
            "async": true
          }
        ]
      }
    ]
```

Replace it with:

```json
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$HOME/.claude/hooks/update-progress.sh",
            "statusMessage": "Stamping progress.md...",
            "async": true
          },
          {
            "type": "command",
            "command": "$HOME/.claude/hooks/intent-log-check.sh",
            "statusMessage": "Checking INTENT-LOG freshness...",
            "async": true
          }
        ]
      }
    ]
```

- [ ] **Step 6: Verify settings.json is still valid JSON**

Run: `python3 -c "import json; json.load(open('$HOME/.claude/settings.json')); print('valid')"`
Expected: `valid`

- [ ] **Step 7: End-to-end test — trigger a real Stop event**

This step cannot be scripted; it requires an actual session. In the Cursor/Claude Code session executing this plan, after committing this task, do or say something trivial (e.g. "say ok") to trigger a Stop event, then check:

Run: `cat ~/.claude/hooks/intent-log-check.sh > /dev/null && echo "hook file present"` (sanity check the file wasn't accidentally deleted)

Then confirm the reminder appeared in the transcript as a system message. If it did not appear, check that the session's cwd was the Agentic OS repo root (the hook is silent everywhere else by design).

- [ ] **Step 8: Commit**

`~/.claude/` is not part of this git repo, so there is nothing to `git add` here. Note in the session's final report that `~/.claude/hooks/intent-log-check.sh` (new file) and `~/.claude/settings.json` (modified) changed outside the repo.

---

## Task 5: Hook health check surfaced in `./agentic-os morning` (WP-22 part 3)

**Files:**
- Modify: `scripts/agentic_os/cli.py:275` (add `check_hook_health()` directly after the existing `launchd_job_status()` function, which ends at line 275)
- Modify: `scripts/agentic_os/cli.py:3486` (call it at the top of `refresh()`)
- Modify: `PROMPTS/morning-brief.md` (document the new line in the reading protocol output, per WP-22's original spec: "morning brief pulls top themes from latest cluster")

**Interfaces:**
- Consumes: `LAUNCHD_LABEL` (module-level constant, line 119) and `launchd_job_status()` (defined immediately above the insertion point), both already in `cli.py`.
- Produces: `check_hook_health() -> list[str]` — returns human-readable issue strings, empty list means healthy. Called by `refresh()`; return value only printed, never affects `refresh()`'s return code (non-blocking, per the original spec: "surface it," not "fail on it").

- [ ] **Step 1: Confirm the exact insertion anchors before editing**

Run: `grep -n "^def launchd_job_status\|^def parse_time_label\|^def refresh(" scripts/agentic_os/cli.py`
Expected:
```
259:def launchd_job_status(label: str = LAUNCHD_LABEL) -> dict[str, Any]:
275:def parse_time_label(value: str | None) -> datetime | None:
3486:def refresh(args: argparse.Namespace) -> int:
```
If the line numbers differ from this plan (the file may have changed since this plan was written), use the grep output as ground truth, not the numbers above.

- [ ] **Step 2: Add check_hook_health() after launchd_job_status()**

Find this exact block (the end of `launchd_job_status` and the start of `parse_time_label`):

```python
    status = parse_launchctl_job(proc.stdout)
    status["raw"] = proc.stdout
    return status


def parse_time_label(value: str | None) -> datetime | None:
```

Replace it with:

```python
    status = parse_launchctl_job(proc.stdout)
    status["raw"] = proc.stdout
    return status


def check_hook_health() -> list[str]:
    """Non-blocking health check for global Stop hooks and the launchd refresh job.

    Returns human-readable issue strings; empty list means healthy. Never raises -
    a missing or malformed settings.json is itself a reportable issue, not a crash.
    """
    issues: list[str] = []
    settings_path = Path.home() / ".claude" / "settings.json"
    if not settings_path.exists():
        issues.append("~/.claude/settings.json not found - Stop hooks are not configured")
    else:
        try:
            settings = json.loads(settings_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            issues.append("~/.claude/settings.json is not valid JSON - hooks cannot be verified")
        else:
            stop_groups = settings.get("hooks", {}).get("Stop", [])
            commands = [
                h.get("command", "")
                for group in stop_groups
                for h in group.get("hooks", [])
            ]
            if not any("update-progress.sh" in c for c in commands):
                issues.append("Stop hook update-progress.sh is missing from settings.json")
            if not any("intent-log-check.sh" in c for c in commands):
                issues.append("Stop hook intent-log-check.sh is missing from settings.json")

    launchd = launchd_job_status(LAUNCHD_LABEL)
    last_exit = launchd.get("lastExitCode")
    if last_exit not in (None, 0):
        issues.append(f"launchd job {LAUNCHD_LABEL} last exited with status {last_exit}")

    return issues


def parse_time_label(value: str | None) -> datetime | None:
```

- [ ] **Step 3: Call it at the top of refresh()**

Find this exact block (the start of `refresh()`):

```python
def refresh(args: argparse.Namespace) -> int:
    status = update_status_json(port=args.port, command=f"./agentic-os {args.command}")
    contradictions = status.get("contradictions") or []
```

Replace it with:

```python
def refresh(args: argparse.Namespace) -> int:
    hook_issues = check_hook_health()
    if hook_issues:
        print("⚠️ Hook health check")
        for issue in hook_issues:
            print(f"  - {issue}")
    status = update_status_json(port=args.port, command=f"./agentic-os {args.command}")
    contradictions = status.get("contradictions") or []
```

- [ ] **Step 4: Verify the module still imports cleanly**

Run: `cd scripts/agentic_os && python3 -c "import cli; print('import ok')"`
Expected: `import ok`

- [ ] **Step 5: Run the existing test suite to confirm no regression**

Run: `./agentic-os test` (from the repo root)
Expected: all existing tests still pass (this task adds a new function and one call site; it does not change any function this suite already tests).

- [ ] **Step 6: Manually verify the health check prints when a hook is missing**

Run:
```bash
cd scripts/agentic_os && python3 -c "
import cli, json
from pathlib import Path
# Simulate a settings.json missing the new hook, without touching the real file
fake = {'hooks': {'Stop': [{'hooks': [{'command': '\$HOME/.claude/hooks/update-progress.sh'}]}]}}
import tempfile
with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as f:
    json.dump(fake, f)
    path = f.name
orig = cli.Path.home
cli.Path.home = staticmethod(lambda: Path(path).parent)
# Can't easily fake Path.home() to point at a single file; instead call the JSON-parsing logic directly:
settings = json.load(open(path))
commands = [h.get('command','') for g in settings.get('hooks',{}).get('Stop',[]) for h in g.get('hooks',[])]
print('intent-log-check.sh' in ' '.join(commands))
"
```
Expected: `False` — confirms the substring-matching logic correctly detects when the new hook is absent. (This step tests the detection logic in isolation since faking `Path.home()` cleanly requires more scaffolding than this plan's scope justifies; the full path is exercised for real in Task 4 Step 7's end-to-end test.)

- [ ] **Step 7: Document the health check and theme pull in PROMPTS/morning-brief.md**

Find this exact block near the top of `PROMPTS/morning-brief.md`:

```markdown
## How to Invoke

1. **Daily:** `./agentic-os morning` from the Agentic OS repo (see `DAILY.md`).
2. **Deep brief:** Use the reading protocol below only when one of the fallback conditions above is true.
```

Replace it with:

```markdown
## How to Invoke

1. **Daily:** `./agentic-os morning` from the Agentic OS repo (see `DAILY.md`). This now prints a "⚠️ Hook health check" block before anything else if a Stop hook is missing from `~/.claude/settings.json` or the launchd refresh job's last run failed — read it first if present.
2. **Deep brief:** Use the reading protocol below only when one of the fallback conditions above is true.
```

Find this exact block in the Agentic OS section of the reading protocol:

```markdown
### Agentic OS (cross-project context)
Path: `/Users/nadavyigal/Documents/Projects /Agentic OS`
- `DASHBOARD.md`
- `dashboard/status.json`
- `BACKLOG.md` (Now + Next sections only)
```

Replace it with:

```markdown
### Agentic OS (cross-project context)
Path: `/Users/nadavyigal/Documents/Projects /Agentic OS`
- `DASHBOARD.md`
- `dashboard/status.json`
- `BACKLOG.md` (Now + Next sections only)
- `INTENT-LOG.md` — most recent `## Theme Clusters - YYYY-MM` section only, if present. One line: "Top themes this month: X, Y, Z."
```

- [ ] **Step 8: Verify the doc edits**

Run: `grep -n "Hook health check\|Top themes this month" PROMPTS/morning-brief.md`
Expected: two matches.

- [ ] **Step 9: Commit**

```bash
git add scripts/agentic_os/cli.py PROMPTS/morning-brief.md
git commit -m "feat: surface hook health at top of ./agentic-os morning, closes WP-22 part 3

Mode: Builder"
```

---

## Task 6: Close out the plan record

**Files:**
- Modify: `OS-IMPROVEMENT-PLAN-2026-06-30.md` (mark the remaining action-queue rows done)
- Modify: `INTENT-LOG.md` (mark its own embedded "Implementation Plan — Auto-capture" section as executed, so a future reader doesn't re-propose it)

**Interfaces:** None — this is bookkeeping, no code depends on it.

- [ ] **Step 1: Update the action queue table in OS-IMPROVEMENT-PLAN-2026-06-30.md**

Find this exact block:

```markdown
| # | Action | File | Session |
|---|---|---|---|
| 1 | Add "never state status from memory" to LESSONS.md | `LESSONS.md` | Now |
| 2 | Add "instruction vs question" rule to global CLAUDE.md | `~/.claude/CLAUDE.md` | Now |
| 3 | Add "asking instead of acting" to ERRORS.md | `~/.claude/ERRORS.md` | Now |
| 4 | Add automation gate to GLOBAL-SELF-IMPROVEMENT.md | `GLOBAL-SELF-IMPROVEMENT.md` | Now |
| 5 | Build Stop hook INTENT-LOG auto-capture | `~/.claude/settings.json` + script | WP-22 (next session) |
| 6 | Add hook health check to morning brief | `PROMPTS/morning-brief.md` | WP-22 |
| 7 | Implement PostHog LLM observability in ResumeBuilder | ResumeBuilder repo | WP-21 (Codex session) |
```

Replace it with:

```markdown
| # | Action | File | Session | Status |
|---|---|---|---|---|
| 1 | Add "never state status from memory" to LESSONS.md | `LESSONS.md` | Now | Done 2026-06-30 |
| 2 | Add "instruction vs question" rule to global CLAUDE.md | `~/.claude/CLAUDE.md` | Now | Done 2026-06-30 |
| 3 | Add "asking instead of acting" to ERRORS.md | `~/.claude/ERRORS.md` | Now | Done 2026-06-30 |
| 4 | Add automation gate to GLOBAL-SELF-IMPROVEMENT.md | `GLOBAL-SELF-IMPROVEMENT.md` | Now | Done 2026-06-30 |
| 5 | Build Stop hook INTENT-LOG auto-capture | `~/.claude/settings.json` + script | WP-22 (next session) | Done 2026-07-01 |
| 6 | Add hook health check to morning brief | `PROMPTS/morning-brief.md` | WP-22 | Done 2026-07-01 |
| 7 | Implement PostHog LLM observability in ResumeBuilder | ResumeBuilder repo | WP-21 (Codex session) | Done 2026-07-01 (PR #98) |
```

Also add, immediately below that table, a note that Problems 3 and 5 (evidence-before-done, post-session checklist) were closed in the same pass — this plan tracked the action queue but not those two problems explicitly:

```markdown

Problem 3 (evidence-before-done) and Problem 5's `GLOBAL-WORKFLOWS.md` addition were closed 2026-07-01: see `LESSONS.md`, `GLOBAL-QA-RULES.md`, and `GLOBAL-WORKFLOWS.md`'s new Post-Session Checklist section.
```

- [ ] **Step 2: Mark INTENT-LOG.md's embedded spec as executed**

Find this exact line in `INTENT-LOG.md`:

```markdown
## Implementation Plan — Auto-capture (2026-06-30)
```

Replace it with:

```markdown
## Implementation Plan — Auto-capture (2026-06-30, executed 2026-07-01)
```

- [ ] **Step 3: Verify both edits**

Run: `grep -n "Done 2026-07-01\|executed 2026-07-01" OS-IMPROVEMENT-PLAN-2026-06-30.md INTENT-LOG.md`
Expected: 4 matches total (3 rows in the plan table + 1 in the INTENT-LOG heading).

- [ ] **Step 4: Commit**

```bash
git add OS-IMPROVEMENT-PLAN-2026-06-30.md INTENT-LOG.md
git commit -m "docs: close out OS-IMPROVEMENT-PLAN-2026-06-30, all 5 problems resolved

Mode: Maintainer"
```

- [ ] **Step 5: Push**

```bash
git push
```

---

## Self-Review Notes

- **Spec coverage:** Problem 3 (Task 1), Problem 5 remainder (Task 2), WP-22 all three parts — Stop hook (Task 4), theme clustering (Task 3), morning-brief health check (Task 5) — all covered. Task 6 closes the bookkeeping loop so `OS-IMPROVEMENT-PLAN-2026-06-30.md` stops reading as partially done.
- **Naming consistency checked:** `entries_for_month` and `cluster` (Task 3) are called identically in the test file, the implementation, and Task 4's hook comment. `check_hook_health` (Task 5) matches between its definition and its call site in `refresh()`. `intent-log-check.sh` matches between Task 4's script filename, the settings.json entry, and the substring check in `check_hook_health()`.
- **Known scope boundary:** Task 5 Step 6 cannot fully exercise `check_hook_health()` end-to-end without monkeypatching `Path.home()`, which this plan intentionally does not do (adds mocking complexity out of proportion to a 15-line function in a markdown-first repo with no existing mocking convention). The real end-to-end proof is Task 4 Step 7 plus reading `./agentic-os morning` output after Task 5 lands.
