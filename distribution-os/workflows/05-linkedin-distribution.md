# LinkedIn Distribution Workflow

One repeatable cadence. Founder posts as the founder, not the company. Goal is credibility and audience compounding, not virality.

## Cadence Defaults

- 1 post per week (per active product focus week)
- 1 longer "build-in-public" update per month
- Comments and replies: ad hoc, no scheduled engagement work

## Inputs

- `distribution-os/projects/{focused-product}.md`
- This week's experiments and any user wins
- `templates/linkedin-post-template.md`

## Steps

### 1. Load skill

`marketingskills/skills/social/SKILL.md`. Apply only the LinkedIn sections; ignore advice that assumes multi-channel operation.

### 2. Pick the angle

Choose one of the angles below. Rotate roughly weekly. Do not stack two of the same in a row.

| Angle | Description |
|---|---|
| Specific user outcome | A real (anonymized if needed) user story. Detail over hype. |
| Founder thinking | A decision being made now, with the tradeoff. |
| Behind the scenes | A choice in the product (data, AI model, UX) and why. |
| Industry observation | A pattern in running / job search the founder noticed, tied loosely to the product. |
| Lesson learned | A failed experiment from `lessons.md`, repackaged honestly. |

### 3. Draft using the template

Open `templates/linkedin-post-template.md`. Fill it. Keep under 1200 characters where possible. One CTA at the end, or none.

### 4. Self-critique pass

Apply these checks:

- Would this be true even if the product did not exist?
- Is there a specific concrete detail in the first two lines?
- Is there a CTA (or none) — never a soft pitch?
- Does it dodge generic LinkedIn motivational tone?
- Is anything cited that needs verification?

If two checks fail, rewrite.

### 5. Approval and queue

Save the draft to Drive `04 Content Assets/LinkedIn/{product}/{YYYY-MM-DD}-{slug}.md` with header `status: draft`. Notify founder for review.

On approval the founder either posts manually or schedules via LinkedIn's native scheduler. This OS does not publish.

### 6. Capture results

A week after publish, log:

- Impressions
- Reactions
- Comments and any notable replies
- Profile views
- Any DMs that became conversations

Update the post header to `status: published` and append the result block.

### 7. Decide reuse

If a post earns a strong response, mark it in `lessons.md` and consider:

- Expanding into a landing page
- Repurposing as a section in onboarding email
- Using the language verbatim on a product page

If a post lands flat, log it as flat. After 3 flats on the same angle, retire the angle for a month.
