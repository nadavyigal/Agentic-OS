# The Claude Skills Ecosystem — These Are the Ones That Matter

**Source:** X / Twitter
**Author:** Mr. Buzzoni (@polydao)
**Captured:** June 2026

---

## Core Insight

The thread maps where the Claude skills ecosystem lives (several hubs, no single dominant source) and curates 32 numbered skills/repos across official, community, and niche registries. The framing is hype-heavy ("$95K developer vs $300K AI architect," "Jarvis stacks"). The genuinely useful idea underneath: power comes from *combining layers* of skills, not bookmarking one repo.

For this OS, the value is filtering, not adopting. We already run 187+ skills plus gstack, superpowers, vercel, supabase, and frontend-design plugins, and a broad set of MCP servers. Most of the thread duplicates what we have.

## Ecosystem Hubs (for discovery, not import)

- Official: `github.com/anthropics/skills`
- Large cross-platform library: `github.com/alirezarezvani/claude-skills`
- Curated lists: `github.com/travisvn/awesome-claude-skills`, `github.com/BehiSecc/awesome-claude-skills`
- Workflow-heavy: `github.com/jezweb/claude-skills`
- Docs → skill pipeline: `github.com/yusufkaraaslan/Skill_Seekers`
- Registry: `github.com/majiayu000/claude-skill-registry`
- Cross-agent collection: `github.com/VoltAgent/awesome-agent-skills`
- Live trending feed: `github.com/aradotso/trending-skills`
- Action layer (external app actions): Composio `awesome-claude-skills` / `awesome-codex-skills`

## Have-vs-Gap (filtered against our stack)

| Article item | Already covered by |
|---|---|
| frontend-design | `frontend-design` plugin |
| skill-creator (×2) | `anthropic-skills:skill-creator`, `superpowers:writing-skills` |
| using-git-worktrees | `superpowers:using-git-worktrees` |
| release-manager | `SKILLS/release-manager-agent.md` + gstack `land-and-deploy` |
| doc-coauthoring | `document-release`, `make-pdf`, anthropic doc skills |
| research / deep-research (×3) | Firecrawl MCP + Exa MCP + `PROMPTS/analysis-research-sprint.md` |
| observability / performance-profiler | gstack `health`, `benchmark`, PostHog MCP |
| connect-apps (Composio) | Gmail / Notion / Slack / Asana / Linear MCPs already wired |
| self-improving-agent | `GLOBAL-SELF-IMPROVEMENT.md` |
| skill-security-auditor | gstack `cso` (already does skill supply-chain scanning) |

## Genuine Signal (shortlist to trial, not the other 29)

1. **Skill_Seekers** (`yusufkaraaslan/Skill_Seekers`) — converts arbitrary docs into reusable skill memory. Real use: package Garmin / HealthKit / Capacitor docs into a skill so we stop re-feeding context. Complements context7 MCP rather than duplicating it.
2. **tech-debt-tracker** (pattern, from `alirezarezvani/claude-skills`) — a gap we have no dedicated tool for. Adopt the *pattern* (track debt + prioritization in `tasks/`), not necessarily the install. Likely over-build for a solo founder.
3. **trending-skills** (`aradotso/trending-skills`) — a discovery feed to escape stale lists. A bookmark, not an import.

## Durable Lesson

Skill supply-chain hygiene: a third-party skill runs with our tools and credentials. Vet before installing. Logged as a decision in `DECISIONS.md` (2026-06-01).

## Verdict

This is a reference repo, not a place to install runnable skills. ~80% of the thread is already covered or is hype. The two things worth doing — both done — are this filtered log and the supply-chain decision entry. The thread's better insight (stack layers, do not bookmark one repo) is something this OS already does at a higher level with its Layer 1-8 structure.
