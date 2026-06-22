---
type: distribution-playbook
product: RunSmart
status: draft
approved: no
created: 2026-06-22
last_updated: 2026-06-22
owner: founder
channels:
  - Hebrew market
  - ASO
  - Web landing
  - Partnerships
  - Community research
related_experiments:
  - rs-he-aso-001
  - rs-he-web-001
  - rs-he-part-001
  - rs-he-comm-001
source_notes:
  - distribution-os/projects/runsmart/scaffold/drafts/2026-06-20-rs-aso-003-listing-audit/aso-review.md
  - distribution-os/projects/runsmart/scaffold/gtm-plan.md
  - /Users/nadavyigal/Documents/RunSmart/docs/strategy/MARKET_ENTRY_GROWTH_PLAN.md
---

# RunSmart - Hebrew-First Distribution Playbook

## Purpose

Use Israel as a focused, high-context acquisition loop for RunSmart, starting with Hebrew App Store optimization and founder-led local distribution.

Hebrew-first does not mean translating every English asset. It means the first public-facing campaign is authored for Hebrew-speaking Israeli runners, measured separately where possible, and repurposed into English only after the Hebrew angle is clear.

## Source Facts

- RunSmart is an iOS-first AI running coach for beginner and returning runners who need safe daily adaptation, not a rigid race plan.
- The live App Store listing already shows English and Hebrew according to `rs-aso-003`, but the Hebrew locale has not had a separate ASO pass.
- v1.0 ships free. Do not reuse older 50% discount or "pioneer badge" language unless the founder explicitly re-approves that offer.
- Android is out of scope for 2026.
- App Store Connect is currently the live source of truth for published metadata, because repo metadata was stale versus the store in the 2026-06-20 ASO audit.
- Do not claim full Hebrew in-app support, RTL support, Shabbat-aware planning, injury prevention, or outcome guarantees unless product QA confirms the exact behavior.

## Core Hypothesis

If RunSmart runs an authored Hebrew-first campaign across App Store metadata, one Hebrew landing surface, and a small number of founder-approved local distribution posts or partnerships, then Israeli storefront install rate and first-plan activation will improve within 21 days because the product will feel locally relevant before it asks for trust.

## What Hebrew-First Means

1. **Authored Hebrew, not translated English.** Use Israeli running language, local race context, and plain coach phrasing.
2. **Local proof before scale.** Start with 20 to 50 qualified Israeli runners, clubs, coaches, or founder-adjacent communities before broad SEO.
3. **App Store first.** The native iOS app is the conversion surface. Web pages exist to send traffic to the App Store.
4. **Safety-forward, not fear-forward.** Lead with "what should I run today?" and "a plan that adapts when life interrupts," not medical promises.
5. **Permissioned community only.** Personal posts, warm asks, club partnerships, and founder-owned channels are allowed. Spammy group drops are not.

## Audience

| Segment | Hebrew framing | Best first channel |
|---|---|---|
| Beginner or returning runner | "רוצה לחזור לרוץ בלי להרגיש שהתוכנית גדולה עליך" | App Store Hebrew screenshots, Facebook page, warm WhatsApp asks |
| First 5K or 10K runner | "מה לרוץ היום, ובאיזה קצב, בלי לנחש" | Hebrew landing page, local SEO, beginner communities |
| Garmin or Apple Watch runner | "הנתונים כבר קיימים, RunSmart עוזר להבין מה לעשות איתם" | App Store metadata, Garmin/Apple Health content, partnerships |
| Coach, club, or run crew organizer | "כלי עזר למתאמנים שצריכים עקביות בין מפגשים" | Personal outreach, partnership packet |

## Message House

### One-Line Hebrew Positioning

מאמן ריצה חכם שמתאים את האימון להיום, לא לתוכנית קשיחה.

### Supporting Points

- תדע מה לרוץ היום, ובאיזו עצימות.
- תוכנית שמתעדכנת לפי האימונים שבאמת ביצעת.
- סיכום ריצה בשפה פשוטה, לא עוד לוח מספרים.
- חיבור ל-Garmin ול-Apple Health רק אם זה נכון לבילד המאושר.

### English Back-Translation

An intelligent running coach that adapts today's workout, instead of forcing a rigid plan.

### Words To Avoid

- "מונע פציעות" unless backed by approved clinical or product evidence.
- "מחליף מאמן" because RunSmart is better framed as an everyday coaching layer.
- "שבת" or "תוכנית מותאמת לשבת" until schedule-aware product behavior exists.
- "50% הנחה לכל החיים" unless the paid offer is live and founder-approved.

## Repeatable Weekly Loop

Run this as a one-week campaign pattern whenever Hebrew market is the focus product/channel.

| Day | Work | Output |
|---|---|---|
| 0 | Pick one hypothesis and one metric | One experiment row selected from the Hebrew menu |
| 1 | Confirm product truth | App Store metadata, screenshots, claims, and URL verified |
| 2 | Draft the asset | Hebrew ASO copy, landing page brief, post, or partner note |
| 3 | Founder review | Draft marked reviewed or revised, no external publish yet |
| 4 | Founder publishes manually | Only after explicit approval in the current session |
| 5-7 | Measure and learn | App Store, web CTA, PostHog, and manual response notes logged |

Do not run more than one Hebrew experiment at a time until the metric source is stable.

## Experiment Menu

| ID | Channel | Hypothesis | Primary metric | Time box | Decision |
|---|---|---|---|---|---|
| rs-he-aso-001 | Hebrew ASO | Authored Hebrew subtitle, keyword field, promotional text, and screenshot captions will lift Israeli storefront install rate | `runsmart.acquisition.app_store_install_rate` filtered to Israel / Hebrew locale if available | 21 days after publish | Do first |
| rs-he-web-001 | Hebrew landing | A single Hebrew landing page with App Store CTA will convert local intent better than the English generic page | `runsmart.acquisition.web_landing_to_appstore_click_rate` | 14 days after publish | Do after ASO |
| rs-he-part-001 | Partnerships | Ten personal coach, club, or run crew notes will produce two qualified conversations and one approved share | Manual partner response log plus App Store clicks if tracked | 14 days | Do after URL and ASO are clean |
| rs-he-comm-001 | Community research | Founder-approved local posts in owned or permissioned communities will produce qualified install traffic without spam | App Store clicks by `ct=rs_he_comm_001`, if tracked, plus replies | 7 days | Use sparingly |

## Asset Recipes

### 1. Hebrew ASO Pass

Produce:

- Hebrew subtitle candidates, max 30 chars each.
- Hebrew keyword field candidates, avoiding title/subtitle repeats.
- Hebrew promotional text, 170 chars max.
- Five Hebrew screenshot caption headlines.
- One reviewer note listing claims that need App Store Connect verification.

Draft quality bar:

- Authored Hebrew, not direct English mirror.
- First three screenshot captions explain the morning decision, adaptive plan, and post-run debrief.
- No medical, guaranteed outcome, or unverified integration claims.

### 2. Hebrew Landing Page Brief

Produce a page brief, not product code, unless the founder explicitly asks for implementation.

Required sections:

- Hebrew hero: one line about today's run decision.
- Three feature blocks: readiness, adaptive plan, debrief.
- App Store CTA with campaign tracking.
- FAQ that clarifies RunSmart is not medical advice and does not replace professional care.
- Measurement plan for page views, App Store CTA clicks, installs if available, and first plan generated.

Recommended route when implemented later: `/he` or `/he/running-coach`, with `dir="rtl"` and Hebrew typography QA.

### 3. Founder-Led Local Post Pack

Produce:

- One founder Facebook/LinkedIn post in Hebrew.
- One short WhatsApp personal message for one-to-one sends, not group blasting.
- One "ask permission first" group message variant for communities where the founder has context.

Rules:

- The founder posts manually.
- No fake urgency.
- No discount unless the offer is live.
- No broad WhatsApp group drop without admin permission or real relationship context.

### 4. Israeli Partnership Packet

Produce:

- Ten target categories, not scraped personal contacts.
- One personal coach note.
- One club or run crew note.
- One podcast or newsletter note.
- A simple partner ask: test the app with 3 to 5 runners, or share the App Store link if they genuinely like it.

Measure:

- Notes sent by founder.
- Replies.
- Qualified conversations.
- Approved partner shares.
- Installs if campaign tracking is available.

### 5. Hebrew SEO Seed Set

Use only after ASO and landing are clean.

Seed topics:

- מאמן ריצה AI
- תוכנית ריצה למתחילים 5 ק"מ
- איך לחזור לרוץ אחרי הפסקה
- תוכנית ריצה שמתאימה את עצמה
- אפליקציית ריצה עם Garmin

Each article must send mobile traffic to the App Store and avoid generic fitness-blog filler.

## Measurement

| Metric | Source | Status |
|---|---|---|
| `runsmart.acquisition.app_store_impressions` | App Store Connect | Pull manually, filter Israel / Hebrew locale when possible |
| `runsmart.acquisition.app_store_install_rate` | App Store Connect | Primary ASO metric |
| `runsmart.acquisition.web_landing_to_appstore_click_rate` | PostHog | Use once a Hebrew landing exists |
| `runsmart.activation.first_open_to_onboarding_complete` | PostHog | Activation guardrail |
| `runsmart.activation.first_plan_generated` | PostHog | Product-quality guardrail |
| Partner replies | Manual log | Use for partnership experiment only |

If a metric cannot be filtered by Hebrew locale or Israel storefront, mark it `unknown` and use directional evidence only. Do not invent attribution.

## First Sprint Recommendation

Start with `rs-he-aso-001`.

Why:

- Hebrew is already live on the App Store, so the smallest useful move is optimizing the existing locale.
- It does not require product code or external publishing by the agent.
- It protects every later Hebrew channel because the App Store page is the conversion destination.

First sprint outputs:

1. Hebrew ASO audit against the live App Store Connect metadata.
2. Hebrew subtitle, keyword, promotional text, and screenshot caption draft.
3. Founder approval gate before any ASC change.
4. 21-day measurement note in `metrics-dashboard.md` or Notion after publish.

## Publish Gates

Nothing from this playbook publishes until all are true:

1. Founder explicitly approves the exact asset.
2. The public App Store URL is verified.
3. Claims are checked against the approved build.
4. Measurement source is named, even if the metric is manually pulled.
5. Rollback is obvious: revert metadata, unpublish page, or delete the post.

## Kill Criteria

Pause the Hebrew-first loop if:

- Israeli storefront install rate drops by 20% or more after a metadata change and no other cause is found.
- Founder review flags the Hebrew voice as unnatural or over-promising.
- Community feedback says the post feels spammy.
- Activation from Hebrew/Israel traffic is materially worse than the app baseline once tracking exists.

## Reuse Instructions For Agents

When asked to run a Hebrew-first RunSmart cycle:

1. Read this playbook, `product-positioning.md`, `messaging.md`, and the latest ASO audit.
2. Choose one experiment from the menu.
3. Produce one asset bundle only.
4. Label every draft `status: draft` and `approved: no`.
5. Report the publish gate and measurement plan in the final response.
