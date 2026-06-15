# Work Packet WP-6

- Status: Open
- Created: 2026-06-10
- Source: AHA_MOMENTS.md (RunSmart web repo, implemented there in PR #90); founder decision to couple the iOS port to the 1.0.2 resubmission
- Workflow pattern: normal
- Input trust: trusted
- Outcome loop: runsmart-submission
- Success signal: All four aha moments work in the native iOS app using existing design components, simulator build + tests pass, build bumped to 15, included in the resubmission archive.
- Depends on: WP-4 (resubmission flow). The account-deletion work in build 13 is already done; this packet adds the aha moments on top and the archive then ships both.

# Work Packet

## Owner Role
iOS Engineer (Codex / Cursor / Claude Code — founder will paste the activation prompt below into the chosen tool)

## Project
RunSmart iOS
Path: `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app`
Branch: `main` (current release line is 1.0.2 build 15)

## Goal
Port the four AHA_MOMENTS to the native iOS app: rebuild the moment components, the insight/context detection services, and `user_aha_moments` persistence in Swift, composed into the existing UI/UX.

## Context
- The spec is `/Users/nadavyigal/Documents/RunSmart/AHA_MOMENTS.md` (canonical, in the web repo).
- The web implementation (reference only, do not import): `v0/lib/userInsightService.ts`, `v0/lib/achievementDetector.ts`, `v0/lib/contextDetector.ts`, `v0/components/runner-identity-moment.tsx`, `goal-timeline-moment.tsx`, `achievement-moment.tsx`, `noticed-moment.tsx`, `aha-moment-overlay.tsx` in the web repo.
- Backend is ALREADY LIVE in the shared Supabase project `dxqglotcyirxzyqaxqln`: table `user_aha_moments` (id, user_id uuid, moment_id text, context text, variant text, fired_at, cta_clicked, dismissed_at, shared; UNIQUE(user_id, moment_id, context)) with RLS `auth.uid() = user_id` for select/insert/update; `profiles` has `runner_identity`, `goal_timeline_weeks`, `projected_goal_date` columns. No backend work needed.

## Validation
- `xcodebuild build` and `xcodebuild test` pass with 0 errors.
- Manual simulator pass: fresh onboarding shows Moment #1 then Moment #3; first finished run shows Moment #2; a qualifying run shows the Moment #4 card; re-running onboarding/run does not re-fire one-shot moments.
- Rows appear in `user_aha_moments` for the signed-in test user.
- Build bumped to 14 before archive.

---

## Activation Prompt (paste everything below into the implementing tool)

```
Execution mode work packet — RunSmart iOS, Aha Moments port (WP-6).

REPO: /Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app
BRANCH: main (1.0.2 build 13). Work on main or a short-lived branch merged back to main.
SPEC: read /Users/nadavyigal/Documents/RunSmart/AHA_MOMENTS.md first — it defines all trigger
logic, sequencing rules, copy, and edge cases. Web reference implementations live in
/Users/nadavyigal/Documents/RunSmart/v0 (lib/userInsightService.ts, lib/achievementDetector.ts,
lib/contextDetector.ts, components/*-moment.tsx). Port the logic, not the code.

GOAL
Bring the four aha moments to the native SwiftUI app, composed into the existing screens and
design system. Success = all four moments fire per the spec, build + tests pass, build = 15.

BACKEND (already live — do not create)
Supabase project dxqglotcyirxzyqaxqln (the app's existing SupabaseManager.client):
- user_aha_moments(user_id uuid, moment_id text, context text, variant text, fired_at,
  cta_clicked bool, dismissed_at, shared bool), UNIQUE(user_id, moment_id, context),
  RLS auth.uid() = user_id for select/insert/update. Insert/select directly from the app.
- profiles.runner_identity (text), goal_timeline_weeks (int), projected_goal_date (date).

TASK — one story at a time, in this order
1. Shared infra:
   - Services/AhaMoments/UserInsightService.swift — pure functions ported from the spec:
     getRunningIdentity(goal:experience:paceMinPerKm:) -> RunnerIdentity enum
     (endurance_builder / speed_seeker / comeback_runner / first_timer / balanced_athlete)
     and projectGoalTimeline(goal:experience:) -> (weeks, milestoneWeek, projectedDate)
     using the lookup table from AHA_MOMENTS.md (min 4, max 24 weeks).
   - Services/AhaMoments/AhaMomentStore.swift — thin Supabase wrapper:
     hasFired(momentId:context:) async, record(momentId:context:variant:ctaClicked:) async
     (insert into user_aha_moments, ignore unique-violation errors), and an upsert of the
     three profiles columns. All calls fire-and-forget; never block UI on network.
2. Moment #1 "This knows me" — Features/AhaMoments/RunnerIdentityMomentView.swift.
   Full-screen overlay shown after onboarding completes: identity badge (SF Symbol glyph +
   label), headline/subline copy from the spec (use variant C "warm/human" as the single
   launch variant), CTA + subtle skip. Staggered fade-in (badge, then headline 400ms,
   subline 600ms, CTA 800ms). Identity accent colors per spec mapped to the existing
   palette (endurance=accentSuccess, speed=accentPrimary, comeback=accentRecovery,
   first_timer=accentHeart, balanced=accentPrimary — match closest existing Color tokens,
   do not invent new hex values).
3. Moment #3 "I can see where I'm going" — Features/AhaMoments/GoalTimelineMomentView.swift.
   Three-dot horizontal timeline (Today / milestone week / goal) with a line that draws
   left-to-right (600ms), goal dot uses the identity color from Moment #1, week count
   beneath ("in 6 weeks"). CTA continues into the app. Fires right after Moment #1 is
   dismissed (separate scene, same session).
   INTEGRATION for #1+#3: Features/Onboarding/OnboardingView.swift calls
   onComplete(completed) at the end (line ~125). Intercept there (or in the parent that
   provides onComplete, in App/RunSmartLiteAppShell.swift) to present #1 then #3 before
   handing control to the main tabs. On any failure, fall through to normal navigation —
   moments must never trap the user. Compute identity from the onboarding profile
   (goal strings like "First 5K"/"10K PR"/..., experience strings like "Getting started";
   no pace question exists in iOS onboarding — pass nil pace and rely on goal/experience
   classification). Persist runner_identity + timeline columns and the user_aha_moments rows.
4. Moment #2 "I just did something I didn't think I could" —
   Features/AhaMoments/AchievementMomentView.swift + a reusable AnimatedCounter.
   Full-screen overlay: counting-up distance number (1.2s ease-out), "New personal best" /
   first-run label, spec copy (variant C), auto-dismiss after 4.5s or any tap.
   Detection: Services/AhaMoments/AchievementDetector.swift — first run ever always fires;
   otherwise fires when distance > previous best (compare against the app's existing local
   run history source used by Features/Run; include runs <0.3km via the "you showed up"
   copy variant).
   INTEGRATION: the post-run flow is RunTabView -> PostRunSummaryView (onSave). Present the
   overlay on top of PostRunSummaryView when it first appears and a new best was detected,
   BEFORE the user reads their stats. Record to user_aha_moments (moment_id 'achievement').
5. Moment #4 "Someone noticed" — Features/AhaMoments/NoticedMomentCard.swift (inline card,
   NOT an overlay: icon + 3px accent left border + headline + subline, no animation) and
   Services/AhaMoments/ContextDetector.swift — pure function, priority order from the spec:
   streak (3/7/14/30/60/100) > category_first (5K/10K/21.1K) > comeback (7+ day gap) >
   high_effort (pace >8% above 30-day avg) > early_morning (<6:30) > late_night (>21:00) >
   third_run_week. SKIP the weather contexts entirely in this version (no weather API in
   the iOS app — fall through to the next priority). Enforce the 3-day minimum gap between
   firings using the latest 'noticed' fired_at from user_aha_moments.
   INTEGRATION: insert the card into PostRunSummaryView's content between the stats section
   and the actions (and/or the run report detail in the Report tab if that is where stats
   live — choose the screen the user actually sees after a run). Record with
   context key (e.g. 'streak_7') so the UNIQUE constraint prevents repeats.
6. Analytics: add to Services/Analytics/AnalyticsEvents.swift following its existing
   static-func style: trackAhaMomentFired(momentId:context:), trackAhaMomentCTAClicked(momentId:),
   trackAhaMomentDismissed(momentId:). Fire them from the views.
7. Bump CURRENT_PROJECT_VERSION to 15 in IOS RunSmart app.xcodeproj/project.pbxproj
   (all 4 occurrences). Leave MARKETING_VERSION at 1.0.2.

UI/UX CONSTRAINTS — compose into the existing system, do not restyle the app
- Reuse the existing design system: RunSmartPanel / GlassCard containers, SectionLabel,
  Color tokens (accentPrimary, accentSuccess, accentRecovery, accentHeart, textPrimary,
  textSecondary, surfaceCard, border), fonts (.displayMD, .bodyLG, .bodyMD, .caption,
  .labelSM), NeonButtonStyle where a primary button is needed. Look at
  Features/Profile/ProfileTabView.swift and Features/Secondary/SecondaryFlowView.swift
  for the established patterns before writing any view.
- Dark theme only (the app is dark); overlays use the brand dark background, not pure black.
- Max ONE moment per screen transition; #1 and #3 are sequential but separate scenes.
- Restrained motion: no confetti; the spec's particle effect is optional — skip if it
  doesn't match existing app motion.
- Copy: use AHA_MOMENTS.md variant C (warm/human) verbatim as the single launch copy.
  No A/B infra in this version; store variant 'C' in the variant column.

GENERAL CONSTRAINTS
- No new SPM dependencies. No backend/schema changes. No edits to account deletion,
  auth, or submission files beyond the build number.
- One story at a time; build after each story. Unit-test the pure logic
  (UserInsightService, AchievementDetector, ContextDetector) in IOS RunSmart appTests
  following the existing test style (see FlexWeekCacheTests).
- Moments are additive and fail-open: any thrown error or missing data skips the moment
  and continues the normal flow. Never block onboarding completion or post-run save.
- Do not invent validation results.

VALIDATION (run all before claiming done)
1. xcodebuild build -project "IOS RunSmart app.xcodeproj" -scheme "IOS RunSmart app"
   -destination 'generic/platform=iOS Simulator' — 0 errors.
2. xcodebuild test on iPhone 17 Pro simulator — all tests pass including the new ones.
3. Simulator walkthrough: fresh sign-in + onboarding -> #1 then #3 appear once with working
   CTA/skip; complete a run -> #2 overlay then summary; complete a qualifying run
   (e.g. 3rd consecutive day) -> #4 card in the summary; repeat onboarding/run -> one-shot
   moments do not re-fire.
4. Confirm user_aha_moments rows exist for the test user (or report the insert calls fired).
5. Report: files changed, tests run with results, what was NOT done.
```

---

## After Implementation (founder, part of WP-4 flow)
1. Device smoke including the four moments.
2. Archive 1.0.2 (15) — this build carries BOTH the account deletion fix and the aha moments.
3. Continue WP-4 steps 4-6 (recording, upload, ASC reply) using build 15.
