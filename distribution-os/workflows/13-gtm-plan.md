# GTM Plan Workflow (iOS, Derived From Web)

Build or refresh a project's GTM plan by inheriting from existing web GTM work and amending for the iOS-app reality. Output is a single `gtm-plan.md` per project that becomes the durable answer to "what is the go-to-market for this app."

## When To Run

- First time installing the Distribution OS in an iOS repo
- When the iOS app crosses a stage gate (TestFlight → soft launch → App Store live → V1.x → V2)
- Quarterly during the monthly strategy review if positioning shifted

## Inputs

- The web project's existing GTM material (locate path before running)
- `distribution-os/projects/{product}.md`
- The project's scaffold `product-positioning.md`, `audience.md`, `messaging.md`, `channels.md`
- Latest market research snapshot
- App Store reality: current listing state, TestFlight or live, paid tier shape

## Steps

### 1. Locate the web GTM source

Standard locations to check (try in order):

- `<web repo>/docs/agent-os/gtm/`
- `<web repo>/docs/gtm/`
- `<web repo>/docs/product/gtm-plan.md`
- `<web repo>/marketing/gtm/`
- `<web repo>/.agent-os/distribution/gtm-plan.md` (if already migrated)

If nothing exists, treat this as a from-scratch GTM and use this workflow without the "inherit" step.

### 2. Load skills

In order:

1. `marketingskills/skills/product-marketing/SKILL.md`
2. `marketingskills/skills/customer-research/SKILL.md` (for audience verification)
3. `marketingskills/skills/launch/SKILL.md` (for the launch model)
4. `marketingskills/skills/aso/SKILL.md` (for App Store positioning specifics)
5. `marketingskills/skills/pricing/SKILL.md` (only if pricing model is changing)

### 3. Inherit from web

Produce an "Inherited from web" section. For each web GTM block, decide one of:

- **Carry as-is** — same on iOS
- **Carry with edit** — same idea, different surface (e.g., headline becomes App Store subtitle)
- **Drop** — does not apply on iOS
- **Net new** — iOS introduces something the web GTM did not have

Map web GTM blocks to iOS GTM blocks:

| Web GTM block | iOS GTM action |
|---|---|
| Positioning one-liner | Carry as-is; ASO subtitle becomes its own derived block |
| Audience segments | Carry; tag each segment iOS-likely or web-likely |
| Job-to-be-done | Carry as-is |
| Before / after | Carry as-is |
| Differentiators | Carry; add mobile-specific differentiators if any |
| Pricing | Often Net new — iOS in-app purchase vs web subscription |
| Channels | Mostly drop or change tier — see iOS channel set in `channel-backlog.md` |
| Lifecycle stages | Reframe: post-install instead of post-signup |
| Launch model | Net new — App Store version cycle, not website releases |
| Metrics & funnel | Net new for acquisition; carry retention if behavior is similar |

### 4. Build the iOS GTM document

Use `templates/gtm-plan-template.md`. Fill every section. Bias toward concrete, dated, measurable.

Required sections:

1. One-line positioning (App Store + web hero alignment)
2. Audience segments (which lean iOS, which lean web)
3. Job-to-be-done
4. Before / after
5. Differentiators
6. Anti-positioning
7. Pricing (iOS in-app + any cross-platform pricing reality)
8. Channels (iOS-first tier list — match `channel-backlog.md`)
9. Acquisition funnel (App Store and web → App Store)
10. Activation funnel (post-install)
11. Retention funnel
12. Lifecycle program summary (post-install)
13. Launch model (App Store version cycle, what triggers a marketing push)
14. Metrics & targets (90-day, 180-day)
15. Risks & mitigations
16. Open questions and owners

### 5. Pricing block deserves its own pass

iOS pricing reality is different. Decide:

- Free with in-app purchase, paid up-front, or subscription
- Trial length
- Cross-platform restore (web subscription unlocks iOS, or separate)
- Family Sharing
- Regional pricing (especially Israel for ResumeBuilder Hebrew variant)
- Apple's 15% / 30% cut and whether that changes the price the user sees vs the price the web charges

Pricing copy that does not match the App Store paywall reality will create chargebacks and 1-star reviews. Treat this section as a hard checkpoint.

### 6. Save and link

- Save to `<project repo>/.agent-os/distribution/gtm-plan.md`
- Mirror or link from the project's `weekly-plan.md` so the weekly cycle has it in scope
- Add a row in Notion Lessons Learned: "GTM inherited from web on YYYY-MM-DD; changes documented"
- Optionally copy to Drive `01 Product Docs/{product}/gtm-plan-YYYY-MM-DD.md` for sharing

### 7. Approval and use

The GTM plan is a founder document, not an agent document. Founder reviews. Once approved, every other workflow can reference it as the source for positioning, channels, and launch model decisions.

### 8. Refresh cadence

- Once: at install
- Once per quarter
- On major version ships
- On material positioning, pricing, or channel changes

## Anti-Patterns

- Generating GTM from scratch when web GTM already exists
- Treating the iOS GTM as a paste of the web GTM (defeats the point)
- Skipping pricing for v1 (it leaks into everything)
- Padding with theory; this should be specific and dated
- Treating GTM as a one-time artifact; it evolves
