---
status: draft
experiment: rb-aso-002
product: Resumely (ResumeBuilder iOS)
type: App Store screenshot brief — English (US), iPhone
created: 2026-05-28
author: distribution-os agent
awaiting: founder review
notes: |
  90% of App Store visitors never scroll past screenshot 3 — first 3 slots are the conversion unit.
  Screenshot captions are indexed by Apple since June 2025 — use keyword-rich captions.
  All captions must accurately reflect real UI (no mockups, no features not in the app).
  Device sizes required: iPhone 6.7" (iPhone 15 Pro Max) and iPhone 6.5" (iPhone 11 Pro Max) minimum.
---

# Resumely — Screenshot Brief v1 (English, iPhone)

## Strategy

Resumely is a Challenger app — every screenshot must carry a message. No bare UI dumps. Each slot has a headline (large, readable), a sub-line (optional), and the underlying UI must match the claim.

Primary conversion question each screenshot answers:
1. "What does this do?" (hook)
2. "How does it work?" (mechanism)
3. "What do I get out of it?" (output)
4–5: Reinforce trust, show breadth, handle an objection

---

## Screenshot Sequence (5 slots — primary set)

### Slot 1 — Hero / Hook

**Goal**: Answer "what is this?" in under 2 seconds.

- **Headline**: `Your resume, tailored for any job`
- **Sub-line**: `Paste a posting. See what's blocking you.`
- **UI to show**: Tailor tab — job description pasted in, ATS score starting to render (score ring visible)
- **Caption** (indexed since 2025): `AI resume tailor and ATS checker for job seekers`
- **Design notes**: Dark background (app is dark-mode only). Score ring is the visual anchor — make it prominent.

---

### Slot 2 — The ATS Score / Pain Point

**Goal**: Make the user feel the cost of NOT using Resumely.

- **Headline**: `See exactly what's blocking you`
- **Sub-line**: `ATS scores every section of your resume`
- **UI to show**: Optimized / ATS score view — scored sections visible (Summary: 62, Experience: 78, Skills: 45 style display)
- **Caption**: `ATS resume score by section — find the blockers before applying`
- **Design notes**: Color-code the scores — red/amber/green visible on screen. The pain is the low scores.

---

### Slot 3 — The Fix / AI Action

**Goal**: Show the value moment — this is where the magic happens.

- **Headline**: `AI edits that actually fit the role`
- **Sub-line**: `Applied section by section, in one tap`
- **UI to show**: Optimized tab showing a before/after bullet improvement, or the AI suggestion cards with an "Apply" button visible
- **Caption**: `AI resume optimization by job description — improve bullets and summary`
- **Design notes**: Show the suggestion text and the Apply button clearly. The specificity of the edit is the proof point.

---

### Slot 4 — Design / Output Quality

**Goal**: Show that the output looks professional — addresses the "will it look cheap?" objection.

- **Headline**: `Templates that pass ATS and impress recruiters`
- **Sub-line**: `Export a polished PDF from your phone`
- **UI to show**: Design tab — template grid visible, or PDF preview showing a clean rendered resume
- **Caption**: `Resume design templates — ATS safe and professionally formatted`
- **Design notes**: Show a template that looks clean and has visible structure (headers, bullet list, contact section).

---

### Slot 5 — Expert / Depth

**Goal**: Show there's more than the basics — reduces the "is this too simple?" objection.

- **Headline**: `Expert analysis for every section`
- **Sub-line**: `Targeted rewrites at hiring-manager level`
- **UI to show**: Expert tab — an expert report card visible with one expanded recommendation
- **Caption**: `Expert resume review with AI rewrite suggestions`
- **Design notes**: Text-rich screenshot is OK here — it signals depth. Show one specific, credible recommendation visible.

---

## Optional Slot 6 (add if testing)

### Slot 6 — Free / Objection Handle

**Goal**: Handle the "what does it cost?" objection before it becomes a reason not to install.

- **Headline**: `Free to use. No subscription.`
- **Sub-line**: `All core features included`
- **UI to show**: Profile / Me tab or the home screen — any UI that looks complete and unpaywalled
- **Caption**: `Free resume builder and ATS checker — no subscription`
- **Design notes**: Keep it clean — the message is the screenshot, not the UI complexity.

---

## Device Sizes Required

| Device | Size | Required? |
|---|---|---|
| iPhone 15 Pro Max | 6.7" (1290 × 2796) | Yes — required by Apple |
| iPhone 11 Pro Max / XS Max | 6.5" (1242 × 2688) | Yes — required by Apple |
| iPad (if app supports iPad) | 12.9" (2048 × 2732) | Check app target — if iPad not supported, skip |

All screenshots must be actual device screenshots (or accurate simulator screenshots). No Photoshop mockups of non-existent UI.

---

## Caption Keyword Strategy

Screenshot captions are indexed since June 2025. All 5 captions above are written to capture keyword combinations not already covered by the title/subtitle/keyword field:

| Slot | Caption covers |
|---|---|
| 1 | "AI resume tailor", "ATS checker", "job seekers" |
| 2 | "ATS resume score", "blockers before applying" |
| 3 | "AI resume optimization by job description" |
| 4 | "ATS safe templates", "professionally formatted" |
| 5 | "Expert resume review", "AI rewrite suggestions" |

---

## Production Checklist

- [ ] Capture real simulator screenshots (not mockups) for each slot
- [ ] Confirm UI matches the copy claim for each slot
- [ ] Add text overlays (headline + sub-line) using design tool (Figma / Canva)
- [ ] Export at correct resolution for each device size
- [ ] Upload to App Store Connect in order (Slot 1 first)
- [ ] Review on mobile before filing — screenshots compress in the search results

---

## Open Questions for Founder

1. Does the current app UI show an ATS score ring / section scores? (Slot 2 depends on this)
2. Does the Optimized tab show before/after diffs or suggestion cards with Apply buttons? (Slot 3 depends on this)
3. Is Expert mode visible to all users in the current build, or behind a flag?
4. Who will render the overlays? (Figma file needed — agent can provide copy, founder or designer renders)
5. Hebrew screenshots: same design, Hebrew text overlay, or fully separate screenshots? (Deferred to Hebrew launch)
