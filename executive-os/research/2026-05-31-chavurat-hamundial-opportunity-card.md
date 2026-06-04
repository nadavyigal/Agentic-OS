# Opportunity Card OC-001: חבורת המונדיאל — Web MVP Launch by June 7

- **Opportunity name:** Web MVP of חבורת המונדיאל — social World Cup prediction app, live before the tournament opens
- **Product:** New product (not RunSmart or ResumeBuilder)
- **User problem:** Israeli friend groups manage World Cup prediction games across WhatsApp + Google Sheets + manual tracking — fragmented, high-friction, no automation, no social host, no leaderboard
- **Evidence:** S4 (WhatsApp dominance in Israel), S1 (tournament opens June 11), product brief (24-section detailed spec from founder)
- **Target user:** Hebrew-speaking friend groups aged 18–40 running informal World Cup prediction games; also Israeli workplace groups
- **Business value:** First-mover Hebrew-native social prediction app for the largest World Cup in history (48 teams). Built-in viral loop (every group admin invites 8–15 friends). Revenue path: freemium premium group upgrade + B2B workplace sales.
- **Implementation complexity:** Medium — core prediction loop (auth + group + invite + prediction + scoring + leaderboard) is well-scoped and achievable in 4–6 days as a web app. AI host adds Medium complexity.
- **Data / API dependencies:** Supabase (Auth, Postgres, Realtime, Edge Functions, Cron), OpenAI API (Hebrew summaries), 2026 World Cup schedule seed data (needs to be located or generated), Expo push notifications (deferred to v2)
- **Revenue potential:** Medium — basis: freemium premium group (~₪20–50/group), B2B workplace leagues (₪200–500/company), potential for multi-tournament recurring subscription after July 19
- **Strategic fit:** New product vertical — not adjacent to RunSmart (fitness) or ResumeBuilder (job search). Timing-driven opportunity with a hard expiry (July 19, 2026). Must be evaluated as a standalone product decision, not as an extension of existing products.
- **Risks:** Timeline (11 days to launch), App Store approval gate for native, AI Hebrew quality unknown, scoring engine trust, post-tournament cliff, Israeli legal review pending
- **Confidence:** Medium-High on product-market fit signal; Medium on execution speed given solo founder + 11-day window

## Score (1–5 each, higher is better except Effort and Risk)

| Impact | Confidence | Effort (lower score = harder) | Revenue potential | Strategic fit | Risk (lower score = riskier) |
|---|---|---|---|---|---|
| 4 | 3 | 2 | 3 | 3 | 2 |

**Score interpretation:**
- Impact 4/5: Real, unsolved pain point with strong virality structure and tournament urgency.
- Confidence 3/5: Product concept is strong; execution feasibility and AI Hebrew quality are the unknowns.
- Effort 2/5: Very high effort given 11-day window. Achievable only with radical scope discipline.
- Revenue 3/5: Clear path exists (premium groups, B2B), but unproven willingness to pay.
- Strategic fit 3/5: Strong standalone product opportunity; not synergistic with existing products.
- Risk 2/5: Timeline, App Store, and legal risks are real. Mitigations exist but require active management.

**Recommended next step:** Decide on web-first vs. native launch vehicle today, locate World Cup schedule seed data, create product repo. Three decisions in the next 4 hours unlock everything else. See research brief for full recommendation stack.
