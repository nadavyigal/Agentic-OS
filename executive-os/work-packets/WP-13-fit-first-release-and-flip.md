# Work Packet WP-13 — Ship the Fit-First Triage Release, Then Flip the Flag

- Status: Open
- Created: 2026-06-23
- Source: WP-12 (Fit-First Triage wedge) — code is merged to `main` (`17d2122`) but ships dark behind `isFitCheckEnabled=false`. This packet is the release vehicle that gets the dark code onto devices, then the staged flip that turns it on.
- Workflow pattern: feature (release-gated)
- Input trust: trusted (derived from live git/PR state 2026-06-23; current TestFlight/App Store version confirmed via `project.pbxproj`: v1.1 build 5, the version already live per [[Resumely iOS Live Version]] memory)
- Outcome loop: Resumely activation / D7 — the wedge does nothing for users until it ships and is turned on
- Related: WP-12 (built it), WP-11 Prompt 2 (sibling decision — RunSmart `VOICE_COACH_ENABLED` flip, same ship-dark-then-flip pattern, decide both together if convenient)
- Success signal: a build containing the Fit-First code is approved and live on the App Store; `isFitCheckEnabled` flip decision is made and logged in DECISIONS.md; if flipped, rollout is staged (not 100% on day one) and analytics confirm the 4 fit-check events are firing in production

---

## Why this packet exists

WP-12 closed the *build* gate, not the *ship* gate. `isFitCheckEnabled=false` means the Fit-First code is inert on every device until two more things happen: (1) a new build reaches users, (2) someone flips the flag. Without this packet the feature sits finished-but-invisible indefinitely — the same trap a dark-launched feature always risks.

## Pre-flight (confirm before starting)

- [ ] Confirm `origin/main` HEAD still contains `isFitCheckEnabled = false` and no other uncommitted iOS changes are pending (check the agent's leftover `tasks/MEMORY.md`/`tasks/progress.md` diffs and the Finder-duplicate junk under `dist/app-store-screenshots/` flagged in this session — clean those before cutting a release branch).
- [ ] Independently confirm the two manual verification steps Cursor reported (simulator smoke with flag temporarily ON; HE xliff export) — they were reported via the background agent, not independently re-verified by me in this session. Re-run `xcodebuild -exportLocalizations` once before trusting it for App Store copy review.

## Step 1 — Cut the release build (S)

Repo: `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP`

- Bump `CURRENT_PROJECT_VERSION` (currently `5`) to `6`; keep `MARKETING_VERSION 1.1` unless there's other user-facing change queued for this build (if so, decide 1.1→1.2 explicitly, don't drift).
- Build archive (`xcodebuild archive` or Xcode Organizer — note from WP-12: local `xcodebuild` CLI repeatedly hung in this sandboxed environment; do this step in Xcode directly or via Cursor/Codex where the build was already confirmed green).
- Upload to App Store Connect / TestFlight.
- Update `tasks/progress.md` + `tasks/MEMORY.md` with the build number and what it contains (Fit-First Triage, dark).

## Step 2 — Internal validation with the flag ON (S)

- On a TestFlight internal-tester build (not the public release), flip `isFitCheckEnabled = true` on a branch, build, distribute to internal testers only. Do NOT ship this flagged-on build publicly.
- Confirm: paste-JD → Check Fit → verdict screen → Optimize handoff works end-to-end against the live `/api/public/ats-check` endpoint (not mock); all 4 analytics events appear in PostHog; HE locale renders correctly RTL.
- This is the one true end-to-end-on-device check that hasn't happened yet — Cursor's reported "BUILD SUCCEEDED" was a compile check, not a live device run with the flag on.

## Step 3 — Submit the dark build (flag OFF) for App Store review (S)

- The public release keeps `isFitCheckEnabled = false`. Submit build 6 (flag off) for review — this is a safe, low-risk submission since the new code path is unreachable.
- Track approval the same way as the last two releases (see [[RunSmart iOS Live Version]] / [[Resumely iOS Live Version]] memory pattern — verify via App Store Connect + founder confirmation, not `progress.md` alone).

## Step 4 — Decide the flip (the actual decision gate)

Once build 6 (or whichever version carries the dark code) is live:

- **Flip now to 100%** — only if Step 2's internal validation was clean and you're comfortable with day-one full exposure on a brand-new front door.
- **Staged rollout** — flip via a percentage/cohort gate if one exists in `BackendConfig`/`RuntimeFeatures` (check whether `RuntimeFeatures` supports a rollout percentage the way RunSmart's flag system might; if not, the practical staged option is "flip in the next build after a few days of internal-only soak").
- **Defer** — name a trigger condition (e.g., "flip after D7 Gate A readout on 2026-06-24" since that's already a scheduled checkpoint for Resumely).

Log whichever choice in Agentic OS `DECISIONS.md` and mirror to the vault Decision Log, same as the 2026-06-23 verdict-thresholds decision.

## Step 5 — If flipped: verify in production

- Confirm via PostHog (or whatever analytics surface is wired) that `fit_check_started`/`fit_check_completed`/`fit_check_optimize_tapped`/`fit_check_skipped` are firing from real users, not just the contract test.
- Confirm the EXD-012 guardrail holds in the wild: spot-check that the verdict copy in the live build still reads as process-descriptive, not an ATS-vendor claim.

## Guardrails (carried from WP-12, still apply)

- A Fit verdict must never consume an optimization credit — re-confirm this didn't regress in the release build.
- EXD-012: no copy implies an external/vendor ATS score.
- Don't flip a production-facing flag without the Step 2 internal validation actually having happened with a real device + live endpoint, not just a green compile.

## Memory update on completion

- iOS `tasks/progress.md` (canonical), `tasks/session-log.md`, `tasks/MEMORY.md` — build number, flip status.
- Agentic OS `DECISIONS.md` — the flip decision.
- Vault `05-Decisions/Decision Log` — mirror.
