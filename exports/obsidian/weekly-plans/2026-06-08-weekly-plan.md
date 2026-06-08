# Weekly Plan — Week of 2026-06-08

> [!info] Source
> Pulled from `executive-os/EXECUTIVE-DASHBOARD.md`, `executive-os/COO-LATEST-REVIEW.md`, `executive-os/WEEKLY-CEO-LATEST.md`, `PROJECT-STATUS.md`.
> No section written from memory.

---

# Part 1 — Last Week Review

## Completed Work

- RunSmart iOS: HealthKit disclosure screens fixed, resubmitted as Build 10 after Apple rejection; build 10 archived, resubmission with UI-change response prepared (source: PROJECT-STATUS.md, tasks/progress.md).
- Resumely iOS: Submitted to App Store Review on 2026-06-05 (founder-confirmed).
- COO Operating Review run on 2026-06-07; selected next action documented.
- RunSmart A1 LinkedIn launch draft created and staged in `distribution-os/` (status: draft, not yet approved).
- Obsidian integration docs added; weekly plan + weekly review system designed and committed.

## Missed Tasks

- RunSmart A1 LinkedIn draft not yet founder-reviewed or approved.
- PostHog live event receipt not yet verified for either app.
- RunSmart Web dirty-tree triage not started.

## Active Projects Status

Source: `PROJECT-STATUS.md` 2026-06-07

| Project | Status | Next gate |
|---|---|---|
| RunSmart iOS | App Store Review Response (Apple) | Archive build 10, verify HealthKit + PostHog, resubmit with response |
| Resumely iOS | App Store Review (Apple) | Monitor App Store Connect; respond only to Apple feedback |
| RunSmart Web | Sprint 11 backend / reference | Triage dirty files before any new web work |
| ResumeBuilder Web | Parked | Keep parked unless Resumely exposes backend issues |
| Agentic OS | Advanced OS patterns pilot | Use Resumely loop in COO reviews; no new loop cards |

## Recurring Problems

- Apple review timing is external and creates week-long pauses on both products.
- PostHog activation data is still unknown; blocks monetization decisions.

## Ideas Worth Saving

- Weekly plan + weekly review split into two separate workflows (Monday operational / Friday reflective) — now implemented in Obsidian templates.

---

# Part 2 — This Week Plan

## Headline

This week protects both App Store submissions while the founder reviews A1 and advances one launch-window asset.

## Time Budget

- Available days: 5 (Mon–Fri)
- Focus blocks: 2 deep blocks per day
- External gates: Apple review for both RunSmart and Resumely (external, unknown timing)

---

## Priority 1 — App Store Monitor `[blocker]`

**Why this week:** Both apps are in Apple review. Failure to respond promptly when Apple replies extends delay.

**Tasks:**
- [ ] Check App Store Connect for RunSmart and Resumely each morning.
- [ ] If Apple responds to RunSmart, create a single-scope response packet and handle only that outcome.
- [ ] If Apple responds to Resumely, handle only the review outcome before any post-launch scope.

**Success criteria:** Any Apple response is handled within 24 hours of receipt.

---

## Priority 2 — RunSmart A1 LinkedIn Draft Review `[milestone]`

**Why this week:** A1 is the next unblocked launch-window action. Until the founder reviews and approves (or revises) it, no further launch assets can be staged.

**Tasks:**
- [ ] Read `distribution-os/projects/runsmart/scaffold/drafts/2026-06-05-rs-linkedin-launch/launch-post-v1.md`.
- [ ] Approve for post-approval queue, or request specific revisions.
- [ ] If approved, stage the next smallest RunSmart launch asset (nothing publishes).

**Success criteria:** A1 has a clear status — approved for queue or revised — and the next launch asset decision is made.

---

## Priority 3 — PostHog Event Verification Prep `[milestone]`

**Why this week:** Monetization and activation decisions depend on PostHog data. Blocking on Apple is not a reason to skip preparation; on approval, verification should happen same-day.

**Tasks:**
- [ ] Document the exact PostHog events to verify at launch (install, first run, key funnel steps) for RunSmart.
- [ ] Document the same for Resumely.
- [ ] Confirm PostHog SDK is present and keys are correct in both apps (read-only check, no code changes while in review).

**Success criteria:** A one-page launch-event checklist exists for each app, ready to run on approval day.

---

## Decision Backlog

> Decisions that must be made this week.

- [ ] Approve or revise RunSmart A1 LinkedIn draft.
- [ ] Decide: should RunSmart Web dirty-tree triage begin this week or stay on hold?

---

## What Is NOT on This Plan

- New iOS feature scope for RunSmart or Resumely while in review.
- Monetization implementation.
- ResumeBuilder Web rollout.
- Any publishing or posting to external channels.
- Paid acquisition.

---

## Success Criteria for the Week

1. Any Apple response to RunSmart or Resumely is handled within 24 hours.
2. RunSmart A1 LinkedIn draft has a clear status (approved or revised).
3. PostHog launch-event checklist drafted for both apps.

---

## Links

- [[Current Priorities]]
- [[Executive Dashboard]]
