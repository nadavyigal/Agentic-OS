# Lifecycle Email Workflow

Both products. The cheapest, highest-leverage retention channel for a solo founder.

## Inputs

- The product's onboarding flow
- Current activation funnel definition
- User events available in PostHog / Supabase
- Any existing email templates

## Steps

### 1. Load skills

In order:

1. `marketingskills/skills/onboarding/SKILL.md` (for activation logic)
2. `marketingskills/skills/emails/SKILL.md` (for sequence design)
3. `marketingskills/skills/copywriting/SKILL.md` (for the prose)

### 2. Map the lifecycle stages

Pick the stages relevant to the product. Example:

RunSmart:

- Welcome (account created)
- Onboarding completed → first plan generated
- First workout logged
- 2-day no-show (run not logged after a planned session)
- 7-day adherence digest
- Inactive 14 days
- Reactivation
- Pre-paid offer (when monetization live)
- Cancellation save

ResumeBuilder:

- Welcome (signed up)
- Welcome 2 (didn't start a resume in 24h)
- Activation hit (first export)
- Activation missed (started but didn't export)
- 7-day digest with job-tailoring tip
- 14-day reactivation
- Job seeker monthly tip (low frequency, opt-in)
- Pre-paid offer / credit-system reminder
- Cancellation save

### 3. For each stage, write the brief

Use `templates/lifecycle-email-template.md`:

- Trigger event (specific event name)
- Delay
- Goal (single)
- Subject line (3 candidates)
- Body
- CTA
- Holdout / exclusion conditions
- Measurement

### 4. Prioritize

Pick the 3 emails with the most leverage given current funnel weak points (from `metrics-dashboard.md`). Draft those first. Park the rest.

### 5. Output

- Drafts in Drive `04 Content Assets/Email/{product}/{stage}.md`
- Sequence overview file in `.agent-os/distribution/lifecycle-program.md`
- Rows in `experiment-log.md` per email (each subject line treated as a future A/B test candidate)

### 6. Approval and implementation

Founder reviews each draft. On approval, implementation moves to the product repo (mail provider config, event triggers) via the standard planning protocol.

### 7. Measure and iterate

For each email:

- Open rate, click rate, downstream action rate
- Unsubscribe rate
- Comparison to control (no email) where possible

Iterate one element at a time (subject line, opening line, CTA). Log each test in `experiment-log.md`.

### 8. Founder constraint

No email is sent until founder approves it. No "transactional" email is silently turned into a marketing send. Job-seeker emails do not include manipulative scarcity. Running emails do not shame.
