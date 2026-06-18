# Work Pack: Agentic OS Sync + Weekly Review Prep — 2026-06-18

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to execute task-by-task.

**Repo:** `/Users/nadavyigal/Documents/Projects /Agentic OS`

**Goal:** Commit and push all pending Agentic OS changes, add the 2 untracked work packet files, and prepare the Friday CEO Review + Weekly Obsidian Review ritual (due 2026-06-19).

**Context:**
- 1 unpushed commit: `f607058 Arm status guard with live-state env`.
- 9 modified tracked files (dashboard HTML + JSON + scripts — these are the `./agentic-os refresh` output).
- 2 untracked files: `executive-os/work-packets/WP-7-arm-status-guard-reconcile.md` and `executive-os/work-packets/WP-8-hygiene-stranded-work-sweep.md`.
- Friday CEO Review + Weekly Obsidian Review are due tomorrow 2026-06-19. Last weekly review was 2026-06-12.

---

## Task 1: Commit the 9 modified dashboard + script files (10 min)

These are the output of `./agentic-os refresh` — they represent the current ground truth.

- [ ] Review what's modified:
  ```bash
  cd "/Users/nadavyigal/Documents/Projects /Agentic OS"
  git diff --stat HEAD
  ```
  Expected: DASHBOARD.md, PROJECT-STATUS.md, dashboard/*.html, dashboard/status.json, scripts/agentic_os/cli.py, scripts/agentic_os/test_cli.py (9 files).

- [ ] Stage and commit:
  ```bash
  git add DASHBOARD.md PROJECT-STATUS.md \
    dashboard/command-center.html \
    dashboard/index.html \
    dashboard/orchestration.html \
    dashboard/project-status.html \
    dashboard/status.json \
    scripts/agentic_os/cli.py \
    scripts/agentic_os/test_cli.py
  git commit -m "chore: refresh dashboard + status after 2026-06-18 morning brief"
  ```

---

## Task 2: Commit the 2 untracked work packet files (5 min)

WP-7 and WP-8 are new work packets sitting untracked.

- [ ] Stage and commit:
  ```bash
  git add executive-os/work-packets/WP-7-arm-status-guard-reconcile.md \
    executive-os/work-packets/WP-8-hygiene-stranded-work-sweep.md
  git commit -m "docs: add WP-7 (arm status guard reconcile) and WP-8 (hygiene stranded work sweep)"
  ```

---

## Task 3: Push all commits to origin (5 min)

- [ ] Push (this sends the previously unpushed commit + the 2 new commits):
  ```bash
  git push origin main
  ```

- [ ] Confirm:
  ```bash
  git status --short --branch
  git log --oneline @{u}.. 2>/dev/null
  ```
  Expected: clean, no unpushed commits.

---

## Task 4: Run a post-push refresh to verify dashboard reflects pushed state (5 min)

- [ ] Re-run refresh:
  ```bash
  ./agentic-os refresh
  ```
  Expected: "sync: OK" (no more uncommitted warning). Confirm the Agentic OS row in PROJECT-STATUS.md shows no dirty/unpushed items.

---

## Task 5: Prep the Friday CEO Review + Weekly Obsidian Review (15 min)

Due tomorrow 2026-06-19. Last review was 2026-06-12 (current week June 15 has no review).

- [ ] Open the weekly review template in the Obsidian vault:
  ```bash
  cat "/Users/nadavyigal/Documents/Projects /Nadav Builder OS/09-Templates/weekly-review-template.md"
  ```

- [ ] Create this week's review file (pre-fill headers from the morning brief):
  ```bash
  cat > "/Users/nadavyigal/Documents/Projects /Nadav Builder OS/07-Weekly-Reviews/2026-06-19-weekly-review.md" <<'EOF'
  ---
  date: 2026-06-19
  week: 2026-W25
  type: weekly-review
  ---

  # Weekly Review — 2026-06-19

  ## What shipped this week
  - RunSmart iOS: Build 15 uploaded (delete account + PrivacyInfo.xcprivacy), resubmitted for App Store review
  - Resumely iOS: Resume Library backend live, PostHog events wired, build 4 submitted
  - ResumeBuilder Web: PDF parsing fixed (unpdf — resolves Vercel 500 on ATS check), /api/v1/resumes live
  - RunSmart Web: Garmin Gate 1-4 evidence package, iOS OAuth gateway, webhook hardening

  ## What didn't ship / got stuck
  - [ ] Fill in after reviewing project status

  ## Decisions made this week
  - [ ] Fill in from docs/agent-os decisions log or Agentic OS DECISIONS.md

  ## Key metrics / data points
  - Resumely D7 Gate A deadline: 2026-06-21 (3 days from review date)
  - RunSmart iOS build 15 in App Store review

  ## What I want to focus on next week
  - [ ] Fill in

  ## CEO review questions
  - Is the Resumely D7 Gate A data showing activation before the deadline?
  - When does RunSmart build 15 get a decision from Apple?
  - Should RunSmart Web Today page redesign start this week or wait for Garmin production gate?

  ## Lessons / learnings this week
  - [ ] Add at least one and update ~/.claude/LEARNINGS.md if it applies globally
  EOF
  ```

- [ ] Also update LEARNINGS.md and ERRORS.md if either file is stale (both last updated 2026-06-12 — 6 days ago):
  ```bash
  # Check if there's anything worth logging from this week
  # At minimum, append the date to keep the file fresh
  echo "" >> ~/.claude/LEARNINGS.md
  echo "## 2026-06-18" >> ~/.claude/LEARNINGS.md
  echo "- Resumely iOS stranded work pattern: Finder ` 2.` duplicate files appear when screenshots are re-generated in a session without cleaning up. Always `rm` these before committing." >> ~/.claude/LEARNINGS.md
  ```

---

## Done criteria
- [ ] 9 dashboard files committed
- [ ] 2 untracked WP files committed
- [ ] All commits pushed, main is clean
- [ ] Post-push refresh shows clean Agentic OS state
- [ ] 2026-06-19-weekly-review.md created in Obsidian vault with headers pre-filled
- [ ] LEARNINGS.md updated with at least one entry
