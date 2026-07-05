# Work Packet WP-33 - Michal AI Operations Pilot: Track C Kickoff (first AI Audit Toolkit client)

- Status: In progress (partial live setup completed 2026-07-05)
- Created: 2026-07-05
- Source: Founder request 2026-07-05 ("I want to make progress with this project... this is the pilot for me using the OS and provide the AI advisory services")
- Mode: HUMAN-heavy (needs Michal's live Gemini account) + Builder assists on drafting/config
- Workflow pattern: one story at a time, per the existing meeting runbook
- Outcome loop: first real client validation of the AI Audit Toolkit (parked toolkit, `AI Audit Toolkit Home.md`); doubles as Michal's own AI operating system
- Related: Michal repo `README.md`, `docs/engagement-plan.md`, `docs/track-c-ai-os-spec.md`, `docs/track-c-meeting-runbook.md`

## Why this packet exists

Track C (the Gemini OS foundation: privacy preamble, Voice doc, 3 demo posts, 4 Gems) is fully drafted and paste-ready per the Michal repo's own status note. Nothing has shipped because the remaining steps all require Michal's live Gemini account, which has no packet tracking it in Agentic OS — this promotes that "last mile" into a trackable unit of work, and gives the AI Audit Toolkit its first real pilot data point.

## Project

Michal repo: `/Users/nadavyigal/Documents/Projects /Michal`

## Read First

- `README.md` (status, layout, privacy red line)
- `docs/engagement-plan.md` (3-track plan: A billing, B content, C OS foundation)
- `docs/track-c-ai-os-spec.md` (deep spec — decisions log, architecture, the 4 Gems)
- `docs/track-c-meeting-runbook.md` (scripted steps for the live account session)
- `gems/privacy-preamble.md` (the no-PII rule every Gem must restate)

## Task

Run the live-account session per `docs/track-c-meeting-runbook.md`:

1. **Account audit** — confirm Michal's Gemini tier (Google AI Plus per the spec's decisions log), confirm Gems feature access.
2. **Stand up the 4 Gems** — Billing, Content/Voice, Newsletter, Repurpose — paste the pre-authored instruction text from `gems/` into her account, attach the "Michal's Voice" knowledge doc to each per the architecture diagram in the spec.
3. **PII red-team** — walk through each Gem's expected inputs/outputs and confirm no client PII (full names, emails, identifying details) can enter Gemini; aliases in, real names re-attached offline by Michal only. This is the hard constraint per the repo's own red line — do not skip or soften it.
4. **Confirm framing** — the spec flags an unresolved item: whether Michal's practice is framed as pure life/couples coaching or a dual practice (also organizational/management coaching, ~20-employee insurance agency background). Get her explicit confirmation before the audit report locks this in (per `track-c-ai-os-spec.md` decisions log, 2026-06-28 entry).
5. **File the pilot's first audit-toolkit artifact** — once the above is done, write the intake/audit notes back into `templates/` per the toolkit's 6-step model (Intake → Pre-audit → Call → Report → Roadmap → Implementation), since this pilot is meant to backfill the toolkit's missing templates.

## Constraints

- **Privacy is the hard constraint.** No client PII ever enters Gemini or this repo, in any commit, draft, or test input. Aliases in; Michal keeps the private offline alias→identity map.
- No platform change — Gemini only (Antigravity explicitly rejected in the spec's decisions log; not an option here either).
- No engagement-repo content merges into Michal's own product repos (`Michal-full-course-`, etc.) — those are read sources only.
- This is a live-account session — cannot be simulated or drafted around; if Michal's account isn't available this cycle, the packet stays Ready, not Blocked (it's a scheduling gap, not a technical one).

## Acceptance

- All 4 Gems live in Michal's Gemini account, each with the Voice doc attached as a knowledge file.
- PII red-team walkthrough documented (what was checked, what if anything needed a fix).
- Framing question (life-coach-only vs dual-practice) explicitly confirmed by Michal, not assumed.
- First audit-toolkit template artifact filed, closing the loop back to `AI Audit Toolkit Home.md`.

## Validation

- Spot-check one real (aliased) session note through the Content/Voice Gem to confirm tone matches the Voice doc before calling the pilot "live."
- No PII round-trip check: confirm no real name/email exists anywhere in this repo's git history after the session (grep before committing).

## Progress

- 2026-07-05: Packet created from founder request during weekly review. Not started — needs a scheduled session with Michal's live Gemini account.
- 2026-07-05: Founder completed a partial live setup with Michal: the content OS is set up across Gemini and NotebookLM, and a live Gemini Gem for "Michal's Voice" is in place. Verified local supporting artifacts in the Michal repo: `/Users/nadavyigal/Documents/Projects /Michal/Michal-share-workspace/NOTEBOOKLM-SETUP-GUIDE.md`, `/Users/nadavyigal/Documents/Projects /Michal/Michal-share-workspace/GEMINI-LIVE-SETUP-CHECKLIST.md`, `/Users/nadavyigal/Documents/Projects /Michal/docs/michal-voice-tone-design.md`, and the paste-ready `gems/` instruction files. Not complete against original acceptance yet: the Billing, Newsletter, and Repurpose workflows are still being reconsidered, possibly as separate NotebookLM notebooks instead of Gems; the full four-Gem setup, PII red-team documentation, framing confirmation, and first audit-toolkit artifact remain open.
