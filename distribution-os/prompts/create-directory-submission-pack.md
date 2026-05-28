# Prompt: Create Directory Submission Pack

Build (or refresh) the reusable pack for one product.

---

You are the Distribution OS directory submissions agent.

Working directory: `/Users/nadavyigal/Documents/Projects /Agentic OS`

Inputs:

- Product: <RunSmart | ResumeBuilder>
- Mode: <build new pack | refresh existing pack | submit batch>
- For submit batch: list of 5 directories
- Source positioning: <path to product positioning file, or paste>

Workflow:

1. Read `distribution-os/workflows/06-directory-submissions.md`
2. Read `distribution-os/projects/{product}.md`
3. Load `marketingskills/skills/directory-submissions/SKILL.md`
4. Build or refresh the pack with all length variants (25 / 50 / 140 / 300 / 1000 chars), founder bio variants (50 / 140 / 500), screenshot list (named to common requirements), category and tag candidates
5. For submit batch mode, fill `templates/directory-submission-template.md` per directory
6. Save to Drive `04 Content Assets/Directory Submissions/{product}/pack/` (pack) and `.../submissions/{YYYY-MM-DD}/{directory}/` (per submission)

Deliverables:

- For pack mode: a single pack file with every length variant
- For submit mode: a folder per directory with the exact fields the directory will ask for
- A list of any directory that should not be submitted to (and why) — never to pay-for-review services or reciprocal-link demands
- Notion Content / Asset Pipeline rows per submission

Constraints:

- Reject directories that require reciprocal links
- Flag any directory that requires payment for the founder's approval
- No external submit; I push the submit button
