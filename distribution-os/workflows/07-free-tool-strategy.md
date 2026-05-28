# Free Tool Strategy Workflow

Primary user: ResumeBuilder (free ATS / resume scoring tool). RunSmart's free wedge is the product itself + free benchmark routes; a separate free tool is not necessarily needed.

## When To Run

- Considering a new free tool
- Re-evaluating an existing free tool's contribution
- Founder is bored or distracted and free tools sound fun (decision is usually "not now")

## Inputs

- Product positioning
- Recent customer research
- Current acquisition funnel

## Steps

### 1. Load skill

`marketingskills/skills/free-tools/SKILL.md`

### 2. Confirm there is a real job

A free tool should:

- Solve a discrete user job that exists today (resumes scored against an ATS pattern)
- Not require signup to be useful (signup at the end, after value)
- Produce a result the user wants to share or save

If any of these is uncertain, stop. Free tools without clear jobs become abandoned subdomains.

### 3. Decide build vs cobble

- Can the result be delivered with prompt + simple UI? (low effort)
- Does it need a real evaluator (parser, embeddings, scoring rubric)?
- Is there an existing open-source piece that does 70% of the work?

A tool that needs > 1 week of focused build time should be rejected unless the channel score is already proven on a smaller version.

### 4. Design the funnel

A free tool is useless if the funnel doesn't catch users:

- Where does the tool live (subdomain, route on main site)
- What's the upgrade prompt after the result
- What lead capture exists (optional email at result step, never gated)
- How does the result page reference the paid product without nagging

### 5. Decide the lead-magnet pair

Pair the tool with a lead magnet from `marketingskills/skills/lead-magnets/SKILL.md`. Example pairs:

- Free ATS score + "How to fix the top 10 ATS rejections" PDF guide
- Free resume word counter + "Job-title-specific resume length cheat sheet"

### 6. Define success

Before building, the agent must produce:

- Target weekly tool runs (90 days out)
- Target signup rate from tool result page
- Target activation rate (tool user → completed first resume)

If any target requires more than the current site's traffic to be plausible, reject or simplify.

### 7. Output

- A free tool brief in Drive `03 Campaigns/{product}/free-tools/{slug}.md`
- Updated `.agent-os/distribution/seo-program.md` linking the tool to SEO pages
- A row in `experiment-log.md` with the tool's success thresholds

### 8. Build

The build happens in the product repo via the standard planning protocol. This OS hands off a brief, not a PR.

### 9. Measure and decide

90 days after launch:

- Did it hit targets?
- If yes, expand (more inputs, more outputs, a v2)
- If no, write a "did not work" entry in `lessons.md` and either sunset or hand off to maintenance only
