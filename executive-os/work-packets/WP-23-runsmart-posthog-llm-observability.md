# WP-23 — RunSmart PostHog LLM Observability

**Created:** 2026-06-30
**Status:** Done — merged `775a9ed` "[codex] Add RunSmart PostHog LLM observability (#108)", including a follow-up fix for streaming-capture reliability (awaited inside `ReadableStream.start()` / `streamText`'s `onFinish` instead of a racing fire-and-forget call). Verified 2026-07-01.
**Repo:** `/Users/nadavyigal/Documents/RunSmart`
**Execute with:** Codex (new session)
**Free tier:** Yes — first 100K `$ai_*` events/month free, no card required
**PostHog project:** Running coach (id: 171597)

---

## Key difference from WP-21 (ResumeBuilder)

ResumeBuilder uses the raw `openai` npm package.
RunSmart uses the **Vercel AI SDK** (`@ai-sdk/openai`, `streamText`, `generateText`) as the primary interface in `chatDriver.ts` and likely in the route handlers. PostHog has a different integration path for Vercel AI SDK.

Before writing any code, check the PostHog docs for the Vercel AI SDK wrapper:
- https://posthog.com/docs/ai-observability/vercel-ai-sdk
- If a dedicated Vercel AI SDK integration exists, use that — it will be simpler and cover streaming automatically.
- If not, fall back to the manual `$ai_generation` event pattern.

---

## Context

RunSmart makes LLM calls on every core product interaction — plan generation, coaching chat, Garmin insights, run reports. None are logged to PostHog. Project 171597 shows zero `$ai_*` events across 90 days.

RunSmart is the primary product with 48 active users/30d. The AI coaching is the core value prop. Knowing what the plan generator and coach are producing for real users — and what it costs — is more critical here than in ResumeBuilder.

---

## What we want to see after this is done

In PostHog LLM Traces (us.posthog.com/project/171597):
- Every LLM call logged with: input prompt, output, model, tokens, cost, latency
- Calls attributed to the user (`distinctId` = Supabase user ID)
- `traceName` set to the feature: `generate-plan`, `chat`, `garmin-insights`, `run-report`, `ai-activity`
- The plan generator traces are especially important — they should show the full system prompt + user context so quality can be assessed without running the eval harness

---

## AI call surface to instrument

### Primary chokepoints (instrument these first)

| File | SDK used | Priority |
|---|---|---|
| `v0/lib/chatDriver.ts` | `@ai-sdk/openai` (`streamText`) | P0 |
| `v0/lib/planGenerator.ts` | Check — may be direct API or Vercel AI SDK | P0 |
| `v0/lib/adaptiveCoachingEngine.ts` | Check — OpenAI direct or via chatDriver | P1 |

### Route files (for `traceName` context — check which chokepoint they call)

| Route | traceName |
|---|---|
| `v0/app/api/generate-plan/route.ts` | `generate-plan` |
| `v0/app/api/chat/route.ts` | `chat` |
| `v0/app/api/ai/garmin-insights/route.ts` | `garmin-insights` |
| `v0/app/api/run-report/route.ts` | `run-report` |
| `v0/app/api/ai-activity/route.ts` | `ai-activity` |

### Worker (check separately)

`services/worker/src/jobs/ai-activity.ts` — runs as a background job. Check if it makes direct OpenAI calls or goes through a shared lib. If direct, instrument it separately. Worker calls need `distinctId` from the job context (user ID from the queued job payload).

---

## Implementation steps

### Step 0 — Read PostHog docs for Vercel AI SDK
- https://posthog.com/docs/ai-observability/vercel-ai-sdk
- https://posthog.com/docs/ai-observability/start-here
- Determine whether the Vercel AI SDK wrapper auto-instruments `streamText`/`generateText` or requires manual wrapping per call.

### Step 1 — Check posthog-node in package.json
RunSmart likely already has PostHog tracking set up. Check `v0/package.json` for `posthog-node`. If not present, flag before installing.

Also check if there is already a PostHog server singleton in `v0/lib/` — do not create a duplicate.

### Step 2 — Create or extend the PostHog server singleton
If a server-side PostHog instance doesn't exist, create `v0/lib/posthog.server.ts`:
```ts
// Server-only — never import in client components
import { PostHog } from 'posthog-node'

let instance: PostHog | null = null

export function getPostHogServer(): PostHog {
  if (!instance) {
    const key = process.env.POSTHOG_API_KEY
    if (!key) throw new Error('POSTHOG_API_KEY is not set')
    instance = new PostHog(key, { host: 'https://us.i.posthog.com' })
  }
  return instance
}
```

Environment variable needed: `POSTHOG_API_KEY` — value is the project API key from
us.posthog.com/project/171597/settings/project.

### Step 3 — Wrap chatDriver.ts (Vercel AI SDK path)

If PostHog has a Vercel AI SDK integration (Step 0), use it in `chatDriver.ts`. Pattern will look something like:

```ts
import { streamText } from 'ai'
import { openai } from '@ai-sdk/openai'
import { withPostHog } from '@posthog/ai' // check exact package name from docs

const result = streamText({
  model: withPostHog(openai(config.defaultModel), {
    posthog: getPostHogServer(),
    distinctId: userId,
    traceId: crypto.randomUUID(),
    traceName: 'chat'
  }),
  messages,
  ...
})
```

If no Vercel AI SDK integration exists, emit manual `$ai_generation` events by timing the call and capturing input/output. See PostHog docs for the manual event schema.

### Step 4 — Wrap planGenerator.ts

Read `v0/lib/planGenerator.ts` to determine which SDK it uses. If it calls an API route, the route file is the right place to instrument. If it uses OpenAI directly:

```ts
// If raw OpenAI SDK:
const trackedClient = posthog.wrapOpenAI(new OpenAI(...), { distinctId, traceName: 'generate-plan' })

// If Vercel AI SDK:
// Same pattern as chatDriver.ts
```

The plan generator is the highest-value trace to capture — it determines the user's entire training experience.

### Step 5 — Worker instrumentation

For `services/worker/src/jobs/ai-activity.ts`:
- Read the file to understand how it gets the user context
- The worker needs a `distinctId` from the job payload (user ID of the person whose activity is being processed)
- Worker is not a Next.js route, so `posthog.shutdown()` is especially important — call it at the end of each job, not at process exit

### Step 6 — Verify in PostHog

After running locally or deploying:
1. Generate a training plan → check us.posthog.com/project/171597 → LLM Observability
2. Send a chat message → check trace appears
3. Confirm: distinctId set, traceName set, model visible, token counts present

---

## Scope gates

Do NOT do any of these in this work packet:
- Add intent classification / tagging — that is a follow-up
- Change prompt content, system prompts, or model selection
- Add new AI features
- Instrument the iOS app (PostHog iOS SDK does not have AI observability yet)
- Modify the eval harness — it is a separate quality layer, not observability

---

## Acceptance criteria

- [ ] `$ai_generation` events appear in PostHog project 171597 for generate-plan and chat calls
- [ ] Each trace has `distinctId` set (not `anonymous` for signed-in users)
- [ ] Each trace has `traceName` identifying the feature
- [ ] Token counts and cost appear (auto-calculated by PostHog from model name)
- [ ] Streaming responses in chat are captured (not just non-streaming calls)
- [ ] Worker AI calls instrumented with user `distinctId` from job context
- [ ] No regression in existing AI features (plan generation, chat still work)
- [ ] `POSTHOG_API_KEY` added to `.env.local` and `.env.example`
- [ ] Lint and type-check pass

---

## Do WP-21 (ResumeBuilder) first

The Vercel AI SDK integration pattern in RunSmart is slightly more complex than ResumeBuilder's raw OpenAI wrapper. Do WP-21 first to establish the PostHog AI observability workflow, then apply learnings here. The `POSTHOG_API_KEY` environment variable name is the same in both repos.

---

## Return format (for Codex to fill in)

- Files changed:
- Vercel AI SDK integration used (yes/no) and package name:
- PostHog traces confirmed visible: yes/no
- Worker instrumented: yes/no
- Any calls not yet instrumented and why:
- Risks or skipped checks:
