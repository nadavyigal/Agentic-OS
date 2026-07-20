# Resumely: GTM brief vs marketing vs this app screen

- **Date:** 2026-07-19
- **Inputs:** `2026-07-19-x-twitter-activation-gtm-hooks.md` + `.agents/product-marketing.md` + ASO listing draft + founder screenshot (Preview / Resume diagnosis after PDF export)
- **Status:** audit · draft recommendations only

## Scoreboard (research → reality)

| Brief hook | Marketing (ASO / product-marketing) | App output (this screen) |
|---|---|---|
| A1 Invisible / searchable for *this* job | Partial — Fit-First exists in marketing; ASO still leads “ATS Check / pass ATS filters” | Weak — diagnosis is job-specific (good) but never says “invisible / searchable” |
| A2 Sound like you, not resume soup | Strong in product-marketing objections; weak in ASO promo | Partial — “using your own wording” is right; gap text still a bit AI-mechanical |
| A3 Keywords you already earned | Strong — missing keywords / gaps language | Strong — concrete gaps + metric ask |
| A4 Export parser-clean PDF | Strong in JTBD; ASO has export | Strong — “PDF exported successfully” + re-export CTA |
| A5 One role > spray volume | Strong in product-marketing (“fewer, better-fit”) | Strong — “Optimize for another job” *after* export |
| Anti-claim: no hiring guarantee | Strong in glossary | Strong — footer on card |
| Anti-claim: no “pass ATS” / official score | **Broken in older ASO promo/description** | Mostly OK — “% match” + “Estimated match guidance”; “Improve ATS” chip is a residual risk |

---

## Marketing overlay

### What already matches the brief

Canonical `.agents/product-marketing.md` (2026-06-28) is already on-brief:

- Fit before spray; Match Score as estimate, not employer ATS
- “I do not want my resume to sound like AI wrote it”
- Words to avoid: pass ATS, guaranteed, official ATS score
- JTBD: tailor without losing voice → export package

### What’s off (high leverage)

Older ASO draft `listing-copy-v1.md` still carries pre–Fit-First claims:

| Field | Current (draft) | Problem vs brief |
|---|---|---|
| Subtitle | “AI Resume Tailor & ATS Check” | “ATS Check” invites official-score expectation |
| Promo | “…AI suggestions that **pass ATS filters**…” | Explicitly on the do-not-claim list |
| Description open | “…scores your resume against **ATS filters**…” | Same; fights the honest Match Score story |

**Recommended marketing lines** (pick one set to file when next ASC edit is allowed):

| Field | Candidate |
|---|---|
| Subtitle (≤30) | `Fit check & resume tailor` (25) |
| Promo (≤170) | `Upload a resume, paste one job, see what’s missing, and export a tailored PDF that still sounds like you — from your iPhone.` |
| Description open (~255) | `Silence after applying isn’t always a verdict — sometimes your resume is invisible for that job. Resumely shows keyword gaps, keeps your wording, and exports a clean PDF for this posting.` |

Do **not** use the brief’s “75% ATS reject” meme anywhere.

---

## App output overlay (this screenshot)

### What’s on-screen (facts)

- Title: Preview · chip: “Improve ATS”
- Card: “Resume diagnosis” · **41% match**
- Impression: recruiter may see relevant experience; needs sharper proof for **Business Development Manager at Getac**
- Gaps: weave ‘job title business’ in *your own wording*; add a metric to most recent role
- Footer: “Estimated match guidance based on the target job, not a hiring guarantee.”
- Success: “PDF exported successfully”
- Actions: Share again · Optimize for another job · Preview & Export PDF · Submit Package

### Hook fit

| Element | Verdict | Why |
|---|---|---|
| Job-named diagnosis | ✅ A1/A3 | Tied to a real role, not generic polish |
| “your own wording” | ✅ A2 | Direct anti–resume-soup instruction |
| Metric gap | ✅ A3 | Specific, interview-defensible |
| Hiring-guarantee footer | ✅ anti-claim | Keep forever |
| PDF exported + Optimize for another job | ✅ A4/A5 | Correct activation sequence |
| Big “41% match” | ⚠️ | Fine if framed as guidance; risky if user reads it as hireability |
| Gap: “job title business” | ❌ | Sounds like model sludge — undermines A2 trust |
| Chip: “Improve ATS” | ❌ | Conflicts with Match Score / no-official-ATS positioning |
| Post-export primary still “Preview & Export PDF” | ⚠️ | After success, primary should push share / next job / Submit Package, not re-export as hero |

### Concrete app copy rewrites (same screen)

| Spot | Current | Proposed |
|---|---|---|
| Chip | Improve ATS | Improve match / Improve fit |
| Score caption | % match | Match estimate (or keep “% match” if space-tight) |
| Gap 1 title/body | Work the concept ‘job title business’… | Use the employer’s job title (or a close title you actually held) in one achievement — in your words |
| Optional one-liner under score | *(none)* | Make this posting find you — keywords you already earned, said their way |
| After export primary | Preview & Export PDF (still hero) | Keep export secondary; hero = Share / Submit Package / Optimize for another job |

---

## One recommended “line” for each surface

1. **Marketing (ASO/web):** “AI that keeps your voice — not another bowl of resume soup.” → expressed as the promo candidate above (no “pass ATS”).
2. **App (this screen):** Keep the footer; fix the chip + the ‘job title business’ gap; after export, demote re-export.

---

## Decision needed

- [ ] Approve marketing candidate set for next ASC metadata edit (when 1.4.3 clears / next update)
- [ ] Approve app string changes (chip + gap wording + post-export CTA priority) for a code session

No publish and no code in this audit.
