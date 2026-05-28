# Launch Campaign Workflow

For product launches, major feature ships, App Store / iOS releases, paid tier launches, Product Hunt launches, or partnership announcements.

A launch is not a tweet. It is a coordinated set of assets across the channels that matter for that audience, on a sequence that gives the launch oxygen.

## Inputs

- The thing being launched (clear definition)
- Target date
- Audience for the launch (which segment of which product)
- Available assets (screenshots, video, copy)

## Steps

### 1. Load skill

`marketingskills/skills/launch/SKILL.md`

### 2. Define the launch one-liner and three angles

- One-liner: what shipped, for whom, why now (1 sentence)
- Three angles (rotate across surfaces): the product angle, the founder-story angle, the user-outcome angle

### 3. Build the asset list per channel

For RunSmart launches the default list is:

- App Store listing update (screenshots, what's new, keywords)
- Landing page or homepage hero update
- LinkedIn post (founder)
- Email to existing users
- One in-product banner (sparingly)
- Partnership outreach to 3 to 5 specific people (only if you have actual relationships)

For ResumeBuilder launches:

- Landing or feature page
- Homepage hero update
- LinkedIn post
- Email to existing users
- Directory updates where the listing should reflect the new state
- Product Hunt prep (only if the launch is big enough)
- Schema updates if relevant (`marketingskills/skills/schema/SKILL.md`)

### 4. Build a sequence

Default timing:

- T minus 7 days: founder LinkedIn teaser (one)
- T minus 3 days: email teaser to existing users
- T minus 1 day: final review of all assets
- T 0: ship product, update landing, update App Store, send email, post LinkedIn
- T plus 1: reply to all comments / questions
- T plus 7: results check
- T plus 14: lessons captured

### 5. Output

- A launch brief in Drive `03 Campaigns/{product}/launches/{slug}/`
- Drafts of every asset
- A checklist in the project's `.agent-os/distribution/launches.md` (scaffold)
- Rows in `experiment-log.md` for each asset's hypothesis

### 6. Anti-patterns

- Launching without a pre-launch sequence
- Launching with broken funnels (signup, payment) untested that morning
- Launching to many channels at once for the first time
- Launching without an honest "what is shipped vs what is coming" statement

### 7. Post-launch

Two weeks after launch:

- Funnel comparison vs prior baseline
- Acquisition source breakdown
- Asset performance ranking
- Lessons (good and bad)
- Decision: was the launch worth the energy, or would smaller releases compound better
