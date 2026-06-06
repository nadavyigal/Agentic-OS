---
type: gtm-execution-packet
asset_id: A2
status: draft
approved: no
product: RunSmart
channel: Facebook page
created: 2026-06-06
last_updated: 2026-06-06
target_publish: after App Store approval
publish_owner: founder
campaign: RunSmart Launch Window Sprint
source: docs/superpowers/specs/2026-06-04-pre-launch-sprint-design.md
related_asset: distribution-os/projects/runsmart/scaffold/drafts/2026-06-05-rs-linkedin-launch/launch-post-v1.md
---

# GTM Packet A2: RunSmart Facebook Page Launch Post

## Goal

Stage the next smallest RunSmart launch-window asset so the founder can publish
from the RunSmart Facebook page within 30 minutes of App Store approval.

## Why This Exists

Both iOS apps are submitted and product work is externally blocked by Apple. The
useful GTM move is launch readiness, not new product scope. A1 already exists as
the founder LinkedIn launch post. A2 turns the same launch message into a shorter
Facebook page post with a direct App Store CTA.

## Hypothesis

A concise Facebook page launch post that leads with the runner outcome will earn
more qualified App Store clicks than a feature-list announcement because it is
easy to understand, easy to share, and tied to the approval moment.

## Channel And Audience

- Channel: Facebook page
- Audience: beginner and returning runners who need a plan that adapts when real
  life interrupts training
- Funnel stage: acquisition
- Campaign: RunSmart Launch Window Sprint

## Task

Create `page-launch-post-v1.md` in this folder with:

1. A 100-120 word Facebook page post.
2. One screenshot placement note.
3. One App Store CTA with `[APP STORE LINK]` placeholder.
4. A publish gate that blocks publishing until App Store approval, founder
   approval, and verified public listing URL.
5. A measurement section for the first seven days after publishing.

## Constraints

- Do not publish.
- Do not edit App Store metadata.
- Do not touch any product repo.
- Do not make performance, injury-prevention, medical, customer-result, or
  adoption claims.
- Do not imply Garmin, Apple Health, GPS, or background tracking behavior beyond
  what the approved build supports.
- Keep the post shorter and more direct than the A1 LinkedIn draft.
- Use a product-led tone, not hype or motivational filler.

## Validation

- `page-launch-post-v1.md` exists with front matter.
- Front matter includes `status: draft` and `approved: no`.
- Post includes `[APP STORE LINK]` placeholder.
- Publish gate says founder approval and App Store approval are required.
- Measurement section lists Facebook reach/engagement and App Store link clicks,
  if tracked.
- No external action was taken.

## Founder Review

Founder reviews the draft after A1 is approved or revised. If approved, update
the draft header to `approved: yes - YYYY-MM-DD`. Founder publishes manually only
after App Store approval and a verified public App Store URL.

## Next Step After This Packet

If Apple still has not responded and A2 is approved, continue to A3: Facebook
group post variants. If Apple approves first, pause asset creation and execute
the approved launch checklist in order: verify public URL, re-read claims against
the approved build, then publish only founder-approved assets.
