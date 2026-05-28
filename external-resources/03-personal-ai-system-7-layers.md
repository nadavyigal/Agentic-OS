# How to Build a Personal AI System With Claude That Knows Everything About You

**Source:** X / Twitter  
**Author:** Nav Toor (@heynavtoor)  
**Published:** May 15, 2026  
**Views:** 128.5K  

---

## The Problem

Most people open Claude, explain who they are, what they do, and what they need. Every single time. Claude forgets them overnight. They start from zero every morning.

The solution: build a personal AI system that knows you. Build it once. Every conversation after starts at mile 10, not mile zero.

---

## Layer 1: Tell Claude Who You Are (5 minutes)

Go to Claude → Settings → Personal Preferences.

```
WHO I AM
Name: [Your name]
Role: [Your job title and what you actually do day to day]
Company: [Your company name and what it does in one sentence]
Industry: [Your industry]
Experience: [Years of experience and your core skill]

HOW I WORK
I prefer [short/detailed] responses unless I ask otherwise.
I communicate in a [casual/professional/direct] tone.
When I ask for help with writing, match my voice. Do not sound like AI.
I use [list your main tools: Notion, Slack, Google Docs, etc].

WHAT I DO NOT WANT
Never start responses with 'Great question!' or 'Absolutely!'
Never use em dashes.
Never use the phrases 'dive deep into' or 'in today's world' or 'it's worth noting.'
Do not ask 'would you like me to continue?' Just continue.
Do not give generic advice. Be specific to my situation.

MY CURRENT GOALS
[Goal 1: what you are working toward right now]
[Goal 2: your second priority]
[Goal 3: your third priority]
```

Keep under 500 words. The "What I Do Not Want" section is the most powerful part.

---

## Layer 2: Build Separate Brains for Separate Work (15 minutes)

Use **Projects** — separate workspaces with their own instructions, files, memory, and conversations.

Example project setup:
- **Content Creation** — knows your writing voice, audience, content calendar
- **Client Work** — knows your clients, businesses, preferences, project history
- **Business Operations** — knows your SOPs, pricing, tools, workflows
- **Research and Learning** — knows what you're studying, skill gaps, learning goals
- **Personal** — knows personal goals, schedule preferences, health targets

Each Project has custom instructions distinct from global preferences. Global = who you are. Project = what this workspace is for.

**Example project instruction (Content Creation):**
```
This Project is for content creation.
My audience is AI professionals and Claude users on X.
My tone is direct, practical, no jargon.
My best-performing content is practical how-to guides with specific numbers.
When writing for me, use short sentences. No filler. Lead with value.
Reference my previous posts when relevant.
```

---

## Layer 3: Turn On Memory So Claude Learns From You (2 minutes)

Go to Settings → Memory → Turn it on.

From this point Claude builds a profile automatically:
- You always ask for bullets → Claude remembers and starts using bullets
- You corrected a formatting preference 3 times → Claude never makes that mistake again
- You mentioned your company name in 5 conversations → Claude uses it naturally

You can manually trigger: *"Remember that my client Sarah prefers formal emails with no exclamation marks."*

View and edit what Claude remembers: Settings → Memory.

The power is compounding: 1 week = basics, 1 month = patterns, 3 months = anticipates your needs.

---

## Layer 4: Teach Claude Your Exact Voice (10 minutes)

1. Collect 5–10 pieces of your best writing (blog posts, emails, social posts, reports)
2. Upload to your Content Creation Project as Project Knowledge
3. Add a voice instruction:

```
VOICE PROFILE
When writing for me, match the tone, rhythm, and vocabulary of the uploaded writing samples.
My sentences are short. Rarely over 15 words.
I use simple words. Never say 'utilize' when 'use' works.
I start paragraphs with action, not throat-clearing.
I never use filler phrases like 'in order to' or 'it is important to note.'
I end articles with a clear action step, not a summary.
```

4. Create a custom Style in Claude (Settings → Styles → Create) and select it in any conversation.

---

## Layer 5: Upload Your World Into Claude (15 minutes)

Each Project can hold files that become part of Claude's knowledge.

| Project | Files to Upload |
|---------|----------------|
| Content | Content calendar, best posts, audience research, brand guidelines |
| Client | Client list with key details, pricing tiers, proposal template, SOW template |
| Operations | SOPs for recurring tasks, tool stack docs, meeting templates, onboarding checklist |
| Learning | Reading list, skill gap analysis, learning goals, course notes |
| Personal | Year goals, daily routine, health targets, reading backlog |

Start with 3 most important files per Project. Add more as you notice what context Claude is missing.

---

## Layer 6: Connect Claude to Your Tools (10 minutes)

Go to Settings → Connectors → Add each tool:

- **Gmail** — reads your emails, drafts replies, surfaces urgent messages
- **Google Calendar** — sees your schedule, preps for meetings, suggests time blocks
- **Google Drive** — reads documents, references files, saves outputs directly
- **Slack** — scans channels, surfaces threads needing attention, posts updates

Once connected, ask Claude: *"What does my day look like and what should I focus on?"* — it answers with YOUR real schedule, YOUR real emails, YOUR real deadlines.

---

## Layer 7: Make It Work While You Sleep (5 minutes)

Claude Cowork (scheduled tasks) / Claude Code (Routines):

| Time | Task |
|------|------|
| 6:30 AM daily | Morning Briefing — reads Gmail, Calendar, Slack; generates one-page briefing to personal Slack |
| 4:00 PM Friday | Weekly Report — compiles week's accomplishments, metrics, next week's priorities; saves to Drive |
| 8:00 PM Sunday | Content Plan — reads analytics, identifies top performers, generates next week's content plan |

---

## The Compound Effect

| Timeline | What Changes |
|----------|-------------|
| Week 1 | Knows your name, role, preferences — stops sounding generic |
| Week 2 | Voice matched from samples — content sounds like you |
| Week 3 | Memory built up — stops requiring re-explanation |
| Month 1 | Scheduled tasks running — mornings faster, reports write themselves |
| Month 2 | Anticipates what you need, catches mistakes, references past conversations |
| Month 3 | You cannot imagine going back |

---

## The Implementation Order

1. **Today (5 min):** Layer 1 — Personal Preferences
2. **Today (15 min):** Layer 2 — Create 3 Projects
3. **Today (2 min):** Layer 3 — Turn on Memory
4. **Tomorrow (10 min):** Layer 4 — Upload writing samples + voice profile
5. **This week (15 min):** Layer 5 — Upload key files to each Project
6. **This week (10 min):** Layer 6 — Connect Gmail and Google Calendar
7. **Next week (5 min):** Layer 7 — Set up first scheduled task

**Total: ~60 minutes. Return: 5–10 hours saved per week, permanently.**
