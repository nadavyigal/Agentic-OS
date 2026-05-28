# Prompt: Implement Story

Use when a story is already defined and scoped.

```txt
You are implementing one development story.

Before coding:
1. Read the local project instructions.
2. Check tasks/risk-reviews/ for a risk-review file matching this plan or story.
   If one exists: read it. Respect the Smallest Safe Slice and the Mitigations column of the Risk Register.
   If the Recommendation was "split-before-implementing" or "stop-and-investigate", do not proceed. Surface this to the user.
3. Restate the story and acceptance criteria.
4. Identify the smallest safe implementation path.
5. Define verification before editing.

Then implement the story.

Return:
- Files changed
- What changed
- Evidence from tests/build/manual checks
- Visual QA evidence if UI changed
- Risks or skipped checks
- Next story recommendation
```

