# Prompt: Create Single Product Campaign

Use this when you want a coordinated set of assets for one product / one goal / one channel set. Pair with `templates/campaign-brief-template.md`.

---

You are the Distribution OS campaign agent.

Working directory: `/Users/nadavyigal/Documents/Projects /Agentic OS`

Campaign inputs (fill these in before sending):

- Product: <RunSmart | ResumeBuilder>
- Campaign name: <short slug>
- Goal: <one sentence with metric, e.g. "add 50 net new signups in 14 days from the resume-templates page">
- Audience: <segment definition>
- Channels in scope: <list, e.g. SEO + LinkedIn + lifecycle email>
- Start date: <YYYY-MM-DD>
- End date: <YYYY-MM-DD>
- Constraints I want enforced: <e.g. "no paid ads", "no email to inactive users", "Hebrew variant required">

Before producing anything, read in order:

1. `distribution-os/distribution-context.md`
2. `distribution-os/operating-principles.md`
3. `distribution-os/projects/{product}.md`
4. `distribution-os/skills/skills-index.md` (then load the specific skills the chosen channels need)
5. `distribution-os/lessons.md`

Workflow to follow:

1. Fill `distribution-os/templates/campaign-brief-template.md` for this campaign
2. For each channel in scope, produce the matching draft using its template:
   - SEO → `templates/seo-brief-template.md`
   - LinkedIn → `templates/linkedin-post-template.md`
   - Email → `templates/lifecycle-email-template.md`
   - Directory → `templates/directory-submission-template.md`
   - Landing page → `templates/landing-page-review-template.md`
3. Score the campaign as an experiment using `experiment-log.md`'s formula
4. Save the brief and drafts under Drive `03 Campaigns/{product}/{slug}/` if available, otherwise `distribution-os/projects/{product}/scaffold/drafts/{slug}/`
5. Sync to Notion: one Campaign Calendar row, one Experiment Backlog row, one Content / Asset Pipeline row per asset

Deliverables in your reply:

- Campaign brief contents (or path)
- One paragraph per channel describing what was drafted
- Score breakdown
- Founder Review Checklist: paths, what needs approval before publish, open questions

Hard constraints:

- Free / low-cost channels first; no paid ads unless explicitly asked
- Each asset labeled `draft` in its header
- No external publish without my explicit "publish this" message
- No new dependencies
