# Global QA Rules

QA exists to protect users, product trust, and shipping confidence.

## Completion Evidence

Every completion claim must include evidence:

- Tests run and results.
- Build or lint results when relevant.
- Visual QA for UI changes.
- Manual flow checks for user-facing behavior.
- Known gaps or skipped verification.
- For any AI-facing feature: a PostHog event confirmed in the dashboard, or a test asserting it fires, before the story is closed. "The AI call works" without a captured event is not sufficient evidence.

## Visual QA

Every UI change must include visual QA.

Preferred evidence:

- Browser screenshot or screen recording for web.
- Simulator screenshot or TestFlight/manual device check for iOS.
- Responsive checks for key viewport sizes.
- Empty/loading/error/success states when affected.

## Risky Changes

Risky changes include:

- Auth, payments, subscriptions, data migrations, permissions, background services, location, HealthKit, exports, AI output generation, and deployment config.

Risky changes require:

- Rollback notes.
- Manual verification plan.
- Clear owner-visible risk summary.
- Post-release check suggestion.

## QA Checklist

- Acceptance criteria verified.
- No obvious regressions.
- Edge cases considered.
- Security/privacy checked where relevant.
- UI visually checked if touched.
- Rollback notes included for risky work.
- Evidence recorded in PR summary or QA report.

