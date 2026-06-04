# Work Packet WP-2 (Active)

- Status: Research + spec complete, waiting for activation data to implement
- Created: 2026-06-04
- Source: EXD-005 (model shape) + EXD-009 (timing)
- Routed by: COO OS
- Escalation: CFO (pricing), Analysis (research) — both for input, not blocking
- Related decision: EXD-005, EXD-009

---

# Work Packet

## Owner Role
CFO OS + Analysis OS (research & design now). Implementation is later, after activation data.

## Goal
Define the freemium model for both apps now — the free activation moment, the paywall line, and the upgrade trigger — and prepare a ready-to-build spec, so when first-cohort activation data arrives we implement immediately instead of starting from scratch.

## Decided (EXD-005, EXD-009)
- Model shape: **freemium with a free activation moment**, both apps.
- Timing: monetize **after** first-cohort activation is readable (do not paywall at launch).
- Price: **set later**, from activation data. Not now.

## Initial recommendation (advice — refine with research + data)
**RunSmart (running coach):**
- Free activation moment: onboarding → first AI plan generated → first run logged → week-1 adherence. All free. This is the "this coach knows me" moment; gating it kills retention.
- Paywall line (candidate): adaptive/Flex Week, advanced Garmin/wearable depth, voice coach, long-horizon race plans.
- Upgrade trigger: after the user feels the plan adapt to them (week 2-3), not before.

**Resumely (resume builder):**
- Free activation moment: one full optimize → preview → first export, so the user sees a better resume once.
- Paywall line (candidate): additional optimizations/exports, Expert modes (cover letter, ATS deep-dive), design templates beyond a starter set.
- Upgrade trigger: at the second resume / second job application.

**Shape:** subscription as primary (recurring value: ongoing coaching / ongoing job search), with the free tier permanently usable so activation is never blocked. Revisit one-time-unlock only if subscription activation is weak.

## Research needed (Analysis OS) — to confirm before locking price
- Competitor pricing & free-tier lines: Runna, Nike Run Club, Strava (RunSmart); Teal, Rezi, Kickresume, Jobscan (Resumely).
- Willingness-to-pay signals for each audience (rookie runner vs. job seeker urgency).
- Which gated feature each segment values most (drives the paywall line).

## Build-readiness checklist (so implementation is instant when data arrives)
- [x] Free vs paid feature matrix per app: `executive-os/work-packets/WP-2-monetization-spec.md` Section 1.
- [x] Paywall placement spec (which screen, which trigger event): `executive-os/work-packets/WP-2-monetization-spec.md` Section 2.
- [x] PostHog events needed to read activation to paywall conversion: `executive-os/work-packets/WP-2-monetization-spec.md` Section 3.
- [x] StoreKit / IAP product IDs drafted (no prices committed): `executive-os/work-packets/WP-2-monetization-spec.md` Section 4.
- [x] Price experiment plan (A/B once there is traffic): `executive-os/work-packets/WP-2-monetization-spec.md` Section 5.

## Research outputs
- Competitor pricing research: `executive-os/research/WP-2-competitor-pricing-research.md`
- Full CFO spec: `executive-os/work-packets/WP-2-monetization-spec.md`

## Constraints
- Do not implement a paywall or set a price until activation data exists (EXD-009).
- No new dependencies; no production/billing changes without explicit founder approval.
- Research only uses public sources; never invent numbers (mark unknowns "need: <source>").

## Validation / Done
- Feature matrix + paywall spec + events list exist and are reviewed.
- EXD-005 / EXD-009 reference this packet; CFO-OS.md updated with the model shape (price still Needs Data).

## Next recommended action
Analysis OS runs the competitor + willingness-to-pay research brief; CFO OS drafts the free/paid matrix and paywall spec from the recommendation above. Keep price blank until activation data.
