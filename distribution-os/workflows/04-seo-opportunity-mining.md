# SEO Opportunity Mining Workflow

Find pages worth writing or programmatic page templates worth building. Primary user is ResumeBuilder; RunSmart uses a lighter version for web landing pages.

## Inputs

- `distribution-os/projects/{product}.md`
- Search Console export (Drive `05 Metrics Exports/Search Console/`)
- Current sitemap or site architecture notes
- Latest market research snapshot

## Steps

### 1. Load skills

In order:

1. `marketingskills/skills/seo-audit/SKILL.md` (for diagnostics on existing pages)
2. `marketingskills/skills/content-strategy/SKILL.md` (for topic clustering)
3. `marketingskills/skills/programmatic-seo/SKILL.md` (only if scale is in play)
4. `marketingskills/skills/site-architecture/SKILL.md` (if URL structure is in question)

### 2. Pull Search Console signals

For the last 90 days:

- Queries with impressions > 0 but position > 10 (almost ranking)
- Pages with high impressions but low CTR (title or meta gap)
- New queries appearing for the first time

### 3. Identify three buckets

| Bucket | What |
|---|---|
| Quick wins | Existing pages that need a title, intro, or schema tweak to move up |
| New pages | Specific queries with clear intent that need a dedicated page |
| Programmatic sets | Patterns ("X resume example for Y industry") that justify a template |

### 4. Filter for quality

Reject:

- Topics that don't fit the product
- Topics where the page would be thin
- Programmatic sets where the underlying data is weak (no real examples, no real variety)

### 5. Pick the next 3 SEO bets

For each, use `templates/seo-brief-template.md` to produce a brief:

- Target query
- Search intent
- Page type (article, landing, programmatic)
- Internal links from / to
- Outline
- Schema choice
- Definition of done

### 6. Output

- 3 SEO briefs in Drive `04 Content Assets/SEO Briefs/{product}/`
- Rows added to `experiment-log.md` and Notion Experiment Backlog
- Update to the project's `.agent-os/distribution/seo-program.md`

### 7. Hand off

Briefs are draft. Founder reviews. On approval, the page work moves into the product repo via the standard project planning protocol — this OS does not write production code.
