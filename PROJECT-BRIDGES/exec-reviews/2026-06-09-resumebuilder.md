# Exec Review: ResumeBuilder (Resumely)
Date: 2026-06-09
Sources: resumebuilder-ai.md bridge, tasks/MEMORY.md, tasks/lessons.md, docs/agent-os/project-context.md, .agent-os/distribution/metrics.md, .agent-os/distribution/channels.md, git log --since="14 days ago"

---

## 1. North-Star Check

**North-star:** First resume exported (primary activation metric, per metrics.md)

**Is it moving?** Unknown. Not tracked. PostHog is not instrumented on ResumeBuilder iOS or web. The `resume_exported` event does not exist yet.

**Why it is not moving:** The app is not yet on the App Store. Submission is pending Apple's response as of 2026-06-08. No live distribution channel is active. `/ats-checker` is live on Vercel but the App Store CTA contains a placeholder URL (`id000000000`), making the primary conversion path broken.

**Data source that would answer it:** PostHog `resume_exported` event (needs 1-line instrumentation), App Store Connect installs panel (needs Apple approval first).

---

## 2. Shipped vs Matters

**What shipped in the last 14 days (from git log):**

| Item | Commit range | Type |
|---|---|---|
| PDF/DOCX pipeline fixes (xref errors, timeout, two-pass) | fix/pdf-parse-xref-error, 1f058e5, 4261890 | Bug fix |
| MarkItDown microservice removed, replaced with local pdf-parse + mammoth | 5fcfdb2, 4c083cb | Refactor |
| DOCX upload support | f57373e | Feature |
| Standalone /ats-checker + /he/ats-checker SEO page (live) | f216e7b, aeb5ebf | Feature |
| EN + HE App Store metadata (5 files committed) | 0afe4fd, cabb06e | Content |
| Screenshot briefs | 8ce4359 | Content |
| 4-week LinkedIn content calendar | 4e0a86e | Content |
| Launch-day community posts | 05e9fb5 | Content |
| StoreKit paywall schema + edge function skeleton | 542d2d3 | Skeleton |
| Ambassador flow schema + edge function skeleton | 885c7a9 | Skeleton |

**Which items serve the north-star:**

The pipeline fixes and DOCX support directly serve it. A user cannot export a resume if the upload and parse pipeline is broken. These were the right work. The ATS checker page is a legitimate distribution feeder but is currently broken (placeholder URL).

**What does not yet serve the north-star:**

The StoreKit and ambassador skeletons are correctly gated (waiting on Gate A: CFO price validation + D7 activation data per EXD-009). Shipping monetization infrastructure before measuring activation is the right call. The LinkedIn calendar and launch posts are real assets but have no destination until the App Store URL is live.

**Gap:** 14 days of output was high in volume but the activation funnel is still closed. The pipeline work was critical-path; everything else is pre-activation staging. One blocker keeps all distribution work from mattering: PDF/DOCX upload smoke test was planned but NOT completed (logged explicitly in tasks/MEMORY.md).

**Verdict:** Productive on pipeline infrastructure. Staging work ahead of distribution validation is a minor over-rotation, but not harmful if the smoke test closes quickly.

---

## 3. Distribution Reality

**Who is actually seeing the product:** Essentially no one. The app is not on the App Store. The web `/ats-checker` page is live but the App Store CTA is broken (placeholder `id000000000`). All channels in `.agent-os/distribution/channels.md` show status: `not started`.

**What is working:** Nothing measurable yet. No Search Console data, no PostHog data, no App Store Connect data is populated in metrics.md. All fields are `not tracked` or `unknown`.

**Distribution hypothesis being tested right now:** None actively live. The implicit hypothesis is: submit to App Store with bilingual (EN + HE) ASO metadata and organic search will drive first installs from the Hebrew job-seeker segment. This is an untested assumption — the app has not been approved yet.

**Biggest unverified assumption:** That Hebrew-locale job seekers convert at a meaningfully higher rate than English-locale, justifying the bilingual distribution prioritization. The Hebrew ASO content, RTL support, and Hebrew ATS checker page were all shipped but no install or activation data can validate this until the app goes live.

---

## 4. Next Bet

**Hypothesis:** If we complete the PDF/DOCX smoke test, fix the `/ats-checker` App Store URL on approval, and wire the single `resume_exported` PostHog event, we can drive the first 20-50 real users through the activation funnel and get a north-star reading within 7 days of App Store approval.

**What to ship (concrete, plan-feature can pick this up):**

1. **PDF + DOCX upload smoke test** - end-to-end upload, parse, optimize, export on both iOS and web. This is the top-listed blocker from the last session. Do not post launch content until this passes.
2. **Fix `/ats-checker` App Store URL** - change `id000000000` to the real App Store ID once Apple approves. One-line change in `src/app/[locale]/ats-checker/page.tsx`.
3. **Wire `resume_exported` PostHog event** - one tracking call at the export confirmation step. This is the north-star event and takes ~30 minutes. Without it, the first real cohort is invisible.
4. **Post the 5 staged launch assets** (LinkedIn calendar + launch-day posts) - only after the App Store URL is live. Already written; just needs publishing.

**How we will know it worked:** 10+ `resume_exported` PostHog events within 7 days of the app going live on the App Store.

**Kill criteria:** Apple rejects the app again (pause distribution spend, fix rejection reason first), or fewer than 3 exports after driving 50+ installs (activation funnel is broken — investigate before any distribution spend).
