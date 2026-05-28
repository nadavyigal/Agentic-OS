# Directory Submissions Workflow

A bursty channel. Front-load a batch of 10 to 20 quality directories per product, then maintain with new directories quarterly.

Primary user: ResumeBuilder. RunSmart can use it lightly (AI app directories, productivity directories) but App Store is the primary listing surface.

## Inputs

- `distribution-os/projects/{product}.md`
- Product screenshot pack (Drive `04 Content Assets/Directory Submissions/{product}/assets/`)
- Standard founder bio + product blurb at multiple lengths

## Steps

### 1. Load skill

`marketingskills/skills/directory-submissions/SKILL.md`

### 2. Build the submission pack (once per product)

The pack is reusable across most directories. Produce:

- 25-character tagline
- 50-character tagline
- 140-character description
- 300-character description
- 1000-character description
- Founder bio (50, 140, 500 chars)
- Logo (PNG, SVG)
- Screenshots (5 to 8) — labeled and sized to common requirements
- Demo video link if available (optional)
- Pricing summary
- Privacy and terms URLs
- Categories and tags (5 candidates)

Save to Drive `04 Content Assets/Directory Submissions/{product}/pack/`.

### 3. Build the directory list

For each product, identify 10 to 20 directories worth submitting to. Use `templates/directory-submission-template.md` for each row:

- Name
- URL
- Category fit (1–5)
- Effort (1–5)
- Cost (free / paid)
- Backlink quality
- Notes

ResumeBuilder candidates (illustrative, verify before submitting):

- AI tool directories (Futurepedia, There's An AI For That, AI Tool Hunt, Toolify)
- Career tool directories
- Startup directories (Product Hunt — only when ready for a launch, not on submission day; Launching Next; BetaList)
- Resume-specific listings
- Hebrew / Israeli market directories where relevant

RunSmart candidates:

- Running app round-up sites (verify low-spam)
- AI assistant directories
- iOS app review sites
- Health and fitness review sites
- Avoid every "submit your app, get reviewed" pay-for-review service

### 4. Submit in batches of 5

- Submit 5 per week
- Track each submission status (submitted / approved / rejected / live)
- Capture any feedback or content edits the directory required

### 5. Maintain

- Quarterly: re-check live listings for accuracy
- When positioning changes: update the pack in Drive, then push updates to top-tier directories first

### 6. Output

- Updated `experiment-log.md` row per submission batch
- Per-product running list in `.agent-os/distribution/directories.md` (scaffold) with status
- Notion Content / Asset Pipeline rows per submission

### 7. Quality bar

- Never submit to a directory that requires reciprocal links
- Never submit to a directory that demands payment for inclusion unless the founder explicitly approves
- Never submit a placeholder; the listing should be as polished as a landing page
