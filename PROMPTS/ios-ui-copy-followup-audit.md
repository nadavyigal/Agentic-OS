# Prompt: iOS UI + Copy Follow-up Audit

Use this prompt in a new Codex task opened at the root of one iOS product repo.
Run it once for Resumely, then again for RunSmart. Do not audit both apps in one
task because their product voices, source trees, evidence, and implementation
plans are different.

## Which repo to open

| Product | Repo | Product taste | Required prior evidence |
|---|---|---|---|
| Resumely | `/Users/nadavyigal/Documents/Projects /ResumeBuilder/ResumeBuilder IOS APP` | Professional career assistant, credible and controlled, never an AI resume gimmick | `docs/audits/first-time-user-journey-audit 2.md`, `docs/qa/reports/wp46-story13-release-candidate-journey-audit-2026-07-18.md`, and `/Users/nadavyigal/Documents/Projects /Agentic OS/executive-os/research/2026-07-19-resumely-copy-rewrite-v2.md` |
| RunSmart | `/Users/nadavyigal/Documents/Projects /IOS RunSmart light /IOS RunSmart app` | Calm personal coach, focused and encouraging, never an analytics dashboard or generic fitness app | `audits/product-design-2026-06-25/audit-notes.md` and the latest FTUX/onboarding QA reports found under `docs/qa/reports/` |

## Copy-ready Codex prompt

Replace `[Resumely or RunSmart]`, then paste everything inside the block into a
Codex task in the matching product repo.

```txt
You are in Plan Mode. You produce an evidence-backed UI and product-copy audit,
followed by a decision-complete improvement plan. You do not edit product code,
strings, tests, project files, task status, or memory in this task. Temporary
build output and audit screenshots must stay outside the repo.

TARGET APP: [Resumely or RunSmart]

OBJECTIVE
Audit the current shipped-intent iOS experience after the FTUX improvements.
Find the UI patterns and user-facing writing that still feel generic,
machine-generated, overbuilt, unclear, repetitive, off-brand, or inaccessible.
Produce a prioritized improvement plan that preserves what is already strong.

SUCCESS
- Every material finding is tied to a fresh screenshot, observed interaction,
  exact current string, or exact source location.
- The audit distinguishes regressions, unresolved prior findings, new findings,
  and prior findings that are now fixed.
- Recommended copy is specific, truthful, concise, and native to this product.
- The plan is split into small, independently verifiable stories and makes no
  unresolved implementation decisions.
- No implementation happens in this task.

MODE AND WORKFLOW
- Planning Mode only.
- Mode for the future implementation packet: Builder.
- Workflow pattern: tournament for copy/UI alternatives, followed by a Taste
  Review before any option is recommended.
- Audit one app only. Do not import the other app's voice or visual language.

STARTUP GATES
1. Read the repo's AGENTS.md and all session-start files it requires.
2. Read tasks/ERRORS.md if present and the global ~/.claude/ERRORS.md. Do not
   repeat a failed approach.
3. Read current progress, lessons, local design system/tokens, current
   localization catalog, and the relevant FTUX audit and QA evidence.
4. Read `/Users/nadavyigal/Documents/Projects /Agentic OS/GLOBAL-TASTE.md` and
   `/Users/nadavyigal/Documents/Projects /Agentic OS/SKILLS/taste-reviewer.md`.
5. For Resumely, also read:
   - `.agents/product-marketing.md`
   - `/Users/nadavyigal/Documents/Projects /Agentic OS/DECISIONS.md`, especially
     the Resumely Match Score and ATS-claim decisions
   - `/Users/nadavyigal/Documents/Projects /Agentic OS/executive-os/research/2026-07-19-resumely-copy-rewrite-v2.md`
6. Treat prior audits and rewrite drafts as hypotheses and historical evidence,
   not proof of the current UI. Verify current state from a fresh build and
   fresh capture.
7. Inspect git status and worktrees. This is read-only audit work. Do not clean,
   overwrite, stage, or absorb unrelated changes.

TOOLS AND SKILLS
Use these in this order:
1. `product-design:audit` for the evidence model, screenshot-linked findings,
   numbered flow, and accessibility limits.
2. `build-ios-apps:ios-debugger-agent` with XcodeBuildMCP to build, launch,
   describe the UI before interaction, navigate, and capture Simulator images.
3. Local `GLOBAL-TASTE.md` plus `SKILLS/taste-reviewer.md` for PASS, REVISE, or
   REJECT judgments.
4. Use source search with `rg` to inventory visible strings and locate their
   Swift or string-catalog owners.
5. Use `build-ios-apps:ios-simulator-browser` only if browser-visible simulator
   proof materially improves inspection and it can run without changing the
   repo or installing an unapproved dependency.

Do not use Figma, ImageGen, or a prototype tool during evidence collection.
They may explore a chosen redesign only after this audit is approved. Do not
use old screenshots as current audit evidence.

CAPTURE SCOPE
Capture the smallest complete set that represents the current experience:
- Fresh launch and first meaningful action
- The post-FTUX activation path through the app's activation event
- Each primary tab in its meaningful default state
- Loading, empty, validation, error, locked/gated, success, and recovery states
  that are part of the primary path
- The key post-success or return loop
- English and Hebrew/RTL on the highest-risk screens when both are supported
- One smaller supported iPhone size and one current standard size for layout
  and Dynamic Type risk

For every accepted screenshot:
- Save it with a numbered descriptive filename in a task-specific temporary
  folder outside the repo, such as `/private/tmp/<app>-ui-copy-audit-<date>/`.
- Inspect the saved file before citing it.
- Record app state, locale, device, data mode, and how the state was reached.
- Name blockers instead of substituting indirect evidence.

AUDIT LENSES

UI and interaction:
- Is there one obvious next action?
- Does hierarchy reflect the user's current job, or does every card compete?
- Are glass, gradients, cards, pills, badges, shadows, icons, and large hero
  treatments purposeful or repeated as decoration?
- Does the UI feel native to iOS and this product, or like a generic generated
  dashboard?
- Are spacing, type, radii, controls, selected states, navigation, and safe-area
  handling consistent with the existing design system?
- Are progress, loading, empty, error, permission, success, recovery, and return
  states calm and clear?
- Check truncation, long localization, Dynamic Type, contrast risk, target size,
  color-only meaning, VoiceOver labels/order, and RTL layout. Clearly separate
  visible risks from items that require direct accessibility testing.

Writing and anti-AI-slop:
- Flag vague benefit language, generic encouragement, inflated confidence,
  fake precision, unverified time promises, hype, filler, redundant headings,
  restated labels, unnecessary jargon, raw model tokens, and copy that explains
  the interface instead of improving it.
- Flag generic AI words and constructions when they add no meaning, including
  unlock, powerful, smarter, seamless, magic, supercharge, transform,
  next-level, tailored just for you, and empty congratulation.
- Flag repeated sentence shapes, overuse of title case, fragments that sound
  generated, decorative punctuation, and long copy where the state or control
  already communicates the meaning.
- Prefer concrete verbs, user language, one idea per sentence, and honest limits.
- Preserve exact current copy that is already strong. This is not a mandate to
  rewrite every string.

Product-specific voice:
- Resumely: professional career assistant. Keep the user in control, preserve
  factual truth, use Resumely Match Score or Match estimate, keep ATS claims
  process-descriptive, and never imply an employer ATS score or hiring outcome.
- RunSmart: calm personal coach. Convert raw metrics into useful coaching,
  respect recovery and uncertainty, avoid anxiety, macho fitness language,
  generic motivation, or a wall of analytics.

EVIDENCE LABELS
Label every finding as exactly one of:
- CONFIRMED VISUAL: visible in a fresh accepted screenshot.
- CONFIRMED BEHAVIOR: observed during the fresh flow.
- CONFIRMED SOURCE: exact current string or implementation found in source, but
  the state was not reached visually.
- PRIOR ISSUE RESOLVED: prior audit issue checked and no longer present.
- HYPOTHESIS: plausible concern that still needs a named verification step.

Do not report a hypothesis as a defect. Do not claim WCAG compliance from
screenshots. Do not use prior screenshots as fresh evidence.

REQUIRED DELIVERABLE 1: AUDIT
Return the audit in the Plan Mode response. Include:
1. Scope, user goal, devices, locales, build/commit, and evidence limits.
2. Numbered current-flow steps with inline screenshots and health per step.
3. What is distinctive and should be kept.
4. Prior FTUX finding reconciliation: fixed, regressed, still open, not tested.
5. Findings table with ID, evidence label, step/screenshot, exact current UI or
   copy, problem, user impact, severity, and source owner.
6. UI-slop pattern inventory.
7. Copy-slop pattern inventory.
8. Accessibility risks and required direct checks.
9. Overall Taste verdict and per-dimension verdicts: Product, UX, Engineering,
   AI Output, PR/QA.

Severity:
- P0: broken task, misleading claim, factual risk, inaccessible blocker, or
  severe trust failure.
- P1: material activation, comprehension, navigation, hierarchy, or credibility
  problem.
- P2: consistency and polish with a visible user cost.
- Keep: strong, distinctive work that should not be flattened by the rewrite.

REQUIRED DELIVERABLE 2: IMPROVEMENT OPTIONS
For every P0 and P1 finding, provide up to three options only when a real choice
exists. Rank them with:
- Expected user impact
- Fit with the product taste profile
- Implementation scope
- Accessibility and localization implications
- Regression risk
- Winner and explicit rejection reason for the other options

Show current and proposed copy side by side. Include context, not isolated
strings. For Resumely, reconcile each proposed string with the July 19 rewrite:
accept, revise, reject, or no longer applicable, with a short reason.

REQUIRED DELIVERABLE 3: DECISION-COMPLETE PLAN
Return a separate, copy-ready implementation plan after the audit. Do not save
it into the repo during Plan Mode. It must include:
- Objective and user outcome
- Non-goals
- Ordered stories, each small enough for one focused session
- Exact expected files and string-catalog keys where discoverable
- UI states and localization/RTL coverage per story
- Acceptance criteria
- Unit, snapshot, simulator, accessibility, and manual QA in proportion to risk
- Before/after screenshot list using the same device, locale, and state
- Banned-string or claim checks where relevant
- Rollback notes
- Dependencies and founder decision gates
- A final recommendation: proceed, proceed-with-mitigations,
  split-before-implementing, or stop-and-investigate

Do not bundle all copy and UI changes into one giant story. Separate trust and
claim fixes, activation hierarchy, state handling, accessibility, and polish
when they can be independently verified. Name all planned files so a large but
expected change does not trip the unexpected-file scope gate during execution.

FINAL RESPONSE
Lead with the verdict and the three highest-impact findings. Link the audit and
plan sections. Report:
- Confirmation that no repo files were created or changed
- Build/tests/captures run and their results
- Checks not run and why
- Open founder decisions
- What was not done, explicitly including product implementation
- Current branch, dirty-tree state, and whether anything was committed or pushed
```

## Recommended tool and plugin stack

| Stage | Use | Why |
|---|---|---|
| Current-flow capture | Product Design `audit` + iOS Debugger Agent | Produces fresh simulator evidence tied to each finding instead of a source-only opinion |
| Runtime interaction | XcodeBuildMCP through iOS Debugger Agent | Builds, launches, describes UI, navigates by labels, and captures screenshots without adding app dependencies |
| Taste and anti-slop judgment | `GLOBAL-TASTE.md` + `SKILLS/taste-reviewer.md` | Keeps the two brands distinct and forces PASS, REVISE, or REJECT decisions |
| String inventory | `rg` + `Localizable.xcstrings` and Swift source | Finds duplicates, unreachable legacy copy, source owners, and localization gaps |
| Optional mirrored review | iOS Simulator Browser | Useful when inspecting the live Simulator inside Codex; skip if it would fetch a new helper without approval |
| Optional visual exploration after approval | Product Design `ideate` or local `mobile-design` | Compare a few chosen redesign directions after the evidence and scope are approved, not during the audit |
| Optional stakeholder board | Figma plugin | Install only if a persistent screenshot-and-notes board is genuinely useful; it is not required for the audit or implementation plan |

Do not install another copywriting plugin for this work. The product's current
strings, product-marketing file, claim decisions, fresh screenshots, and Taste
profiles are better grounding than a generic copy framework.

## Recommended sequence

1. Run the prompt in the Resumely repo first because its July 19 rewrite pack is
   already a strong candidate set and Resumely is the primary product.
2. Review and approve the Resumely audit plan before implementation.
3. Run the same prompt in the RunSmart repo with RunSmart's own calm-coach voice.
4. Implement one approved story per task and finish with fresh before/after
   screenshots plus a Taste Review.
