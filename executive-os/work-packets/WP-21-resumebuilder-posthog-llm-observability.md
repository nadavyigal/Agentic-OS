# WP-21 — ResumeBuilder PostHog LLM Observability

**Created:** 2026-06-30
**Status:** Done — merged `e0ad2b7` "Add PostHog LLM observability (#98)". `src/lib/posthog-server.ts` and `src/lib/posthog-ai.ts` confirmed present in repo; `posthog-node` in package.json. Verified 2026-07-01.
**Repo:** `/Users/nadavyigal/Documents/Projects /ResumeBuilder/new-ResumeBuilder-ai-`
**Execute with:** Codex (new session)
**Free tier:** Yes — first 100K `$ai_*` events/month free, no card required

---

## Context

ResumeBuilder makes LLM calls on every core user action but none of them are logged to PostHog.
The `$ai_generation`, `$ai_trace`, and `$ai_tag` event types already exist in the PostHog project
(id: 270848) but show zero events across 90 days.

PostHog has a native Node.js AI observability wrapper that captures prompt, output, tokens, cost,
and latency automatically. The goal is to wrap the existing OpenAI calls — not rewrite them.

---

## What we want to see after this is done

In PostHog LLM Traces (us.posthog.com/project/270848):
- Every call to OpenAI logged with: input prompt, output, model, tokens, cost, latency
- Calls grouped by user (`distinctId`) and by session (trace)
- The `traceName` field set to the feature that triggered the call (e.g. `optimize`, `chat`, `refine-section`, `expert-mode`, `ats-check`)
- No PII in the system prompt field (resume content is OK; email/name should be excluded from the trace if possible)

---

## AI call surface to instrument

All calls go through two chokepoints. Instrument these — do not touch the route files.

| File | What it does | Priority |
|---|---|---|
| `src/lib/openai.ts` | Singleton OpenAI client used by optimize, upload-resume, ats routes | P0 |
| `src/lib/chat-manager/ai-client.ts` | Streaming + non-streaming chat completions | P0 |
| `src/lib/expert-workflows/orchestrator.ts` | Expert mode multi-step calls | P1 |

Route files that call the above (for `traceName` context only — do not instrument these directly):
- `/api/optimize/route.ts` → traceName: `optimize`
- `/api/v1/chat/route.ts` → traceName: `chat`
- `/api/v1/refine-section/route.ts` → traceName: `refine-section`
- `/api/agent/run/route.ts` → traceName: `expert-mode`
- `/api/public/ats-check/route.ts` → traceName: `ats-check`

---

## Implementation steps

### Step 0 — Read PostHog docs first
Before writing any code, fetch the current PostHog Node.js AI observability docs:
- https://posthog.com/docs/ai-observability/start-here
- Look for the OpenAI wrapper pattern (likely `posthog.wrapOpenAI(client, options)`)
- Confirm the exact import and the `distinctId` / `traceId` API

### Step 1 — Install posthog-node
Check if `posthog-node` is already in package.json. If not, ask before installing.
The PostHog web SDK (`posthog-js`) is for browsers; the server SDK is `posthog-node`.

### Step 2 — Create a PostHog server singleton
Create `src/lib/posthog.ts`:
```ts
// Server-only PostHog client — never import in client components
import { PostHog } from 'posthog-node'

let instance: PostHog | null = null

export function getPostHog(): PostHog {
  if (!instance) {
    const key = process.env.POSTHOG_API_KEY
    if (!key) throw new Error('POSTHOG_API_KEY is not set')
    instance = new PostHog(key, { host: 'https://us.i.posthog.com' })
  }
  return instance
}
```

Environment variable needed: `POSTHOG_API_KEY` — value is the project API key from
us.posthog.com/project/270848/settings/project (the `phc_...` key, not the personal key).

### Step 3 — Wrap the singleton in src/lib/openai.ts
Replace the raw `new OpenAI(...)` with a PostHog-wrapped version. The wrapper must accept
`distinctId` (Supabase user ID) and an optional `traceName` so the caller can identify the feature.

Pseudocode pattern (confirm exact API from docs in Step 0):
```ts
export function getTrackedOpenAI(distinctId: string, traceName?: string) {
  const posthog = getPostHog()
  const openai = getOpenAI()
  return posthog.wrapOpenAI(openai, { distinctId, traceId: crypto.randomUUID(), traceName })
}
```

If the PostHog wrapper does not support a `traceName` field at this level, set it as a
property on the `$ai_trace` event instead — check the docs for how to do this.

### Step 4 — Propagate distinctId through the call sites
The three P0 files need to receive a `distinctId`. The user ID is available from Supabase auth
in every route that requires sign-in. Thread it through:
- `getOpenAI()` callers in route files → pass the user's Supabase `userId`
- `createAIClient()` and `getChatResponse()` in `ai-client.ts` → extend `AIClientConfig` to include `distinctId`
- For unauthenticated routes (`/api/public/ats-check`) → use `'anonymous'` or a session ID

### Step 5 — Verify in PostHog
After deploying or running locally:
1. Trigger one call of each type (optimize, chat, refine-section)
2. Go to us.posthog.com/project/270848 → LLM Observability (or AI Traces)
3. Confirm traces appear with: input prompt visible, model shown, cost calculated, traceName set

### Step 6 — Serverless shutdown
In Next.js serverless functions, add `await posthog.shutdown()` before the response returns,
or PostHog may not flush the event before the function exits. Check if the existing routes
already handle this pattern for `posthog-js`; if so, mirror it for `posthog-node`.

---

## Scope gates

Do NOT do any of these in this work packet:
- Add intent classification / tagging (`$ai_tag`) — that is WP-22
- Change prompt content or system prompts
- Add new AI features
- Modify route logic beyond threading `distinctId`
- Change the PostHog web (browser) SDK setup — that is separate

---

## Acceptance criteria

- [ ] `$ai_generation` events appear in PostHog for optimize, chat, and refine-section calls
- [ ] Each trace has `distinctId` set (not `anonymous` for signed-in users)
- [ ] Each trace has `traceName` identifying the feature
- [ ] Token counts and cost appear on the trace (auto-calculated by PostHog from the model name)
- [ ] No regression in existing LLM features (optimize, chat, refine-section still work)
- [ ] `POSTHOG_API_KEY` added to `.env.local` and documented in `.env.example`
- [ ] Lint and type-check pass

---

## Return format (for Codex to fill in)

- Files changed:
- PostHog traces confirmed visible: yes/no
- Any calls not yet instrumented and why:
- Risks or skipped checks:
