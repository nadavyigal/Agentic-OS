# Google Drive Map

Google Drive is the document, asset, and source-material store for the Distribution OS. It is not the planning layer (Notion) and not the operating system (this repo). The Drive holds source material in, finished assets out, and a working folder for everything in between.

## Actual Structure (as connected, iOS-first)

The founder created product-level folders inside the Distribution OS parent. The OS populates subfolders inside each product folder, plus a single shared inbox at the parent level.

```
Google Drive/
└── Distribution OS/                                  (1uH_CHtd0wY-qaAHGO3SbVjTdRkXdRRJO)
    ├── 00 Source Material/                          (shared inbox, created by OS)
    ├── RunSmart IOS Marketing/                      (1CwUokNhjI1ZZLrsMNbr_WYssj9yg4E4s)
    │   ├── 01 Product Docs/
    │   ├── 02 Market Research/
    │   │   ├── Competitors/
    │   │   ├── Customer Research/
    │   │   ├── Channel Research/
    │   │   └── partnerships/
    │   ├── 03 Campaigns/
    │   ├── 04 Content Assets/
    │   │   ├── ASO Assets/
    │   │   ├── LinkedIn/
    │   │   ├── SEO Briefs/
    │   │   ├── Email/
    │   │   └── Directory Submissions/
    │   ├── 05 Metrics Exports/
    │   │   ├── PostHog/
    │   │   ├── App Store Connect/
    │   │   ├── Search Console/
    │   │   ├── Vercel/
    │   │   └── Stripe or Payments/
    │   └── 06 Weekly Reports/
    └── ResumeBuilder IOS Marketing/                 (1a-kjPMRIK1ndEou4e75waiYXTANou59s)
        ├── 01 Product Docs/
        ├── 02 Market Research/
        │   ├── Competitors/
        │   ├── Customer Research/
        │   ├── Channel Research/
        │   └── partnerships/
        ├── 03 Campaigns/
        ├── 04 Content Assets/
        │   ├── ASO Assets/
        │   ├── LinkedIn/
        │   ├── SEO Briefs/
        │   ├── Email/
        │   └── Directory Submissions/
        ├── 05 Metrics Exports/
        │   ├── PostHog/
        │   ├── App Store Connect/
        │   ├── Search Console/
        │   ├── Vercel/
        │   └── Stripe or Payments/
        └── 06 Weekly Reports/
```

ASO Assets is new vs the original spec because both products are iOS-first now.

## Folder Contracts

### `00 Source Material/`

Anything raw the founder drops in. Interview transcripts, external articles to read, screenshots, ideas captured on the go. The agent treats this as inbox; nothing here is authoritative until it is referenced in another folder.

### `01 Product Docs/{product}/`

Product positioning canon, feature lists, integration descriptions. The single agent-facing copy of "what this product is." If the project repo's `.agent-os/distribution/product-positioning.md` is current, this folder mirrors it. If both exist, repo wins on conflict.

### `02 Market Research/`

- `Competitors/{product}/` — competitor profiles, snapshots
- `Customer Research/{product}/` — interview notes, themes, quotes (anonymized)
- `Channel Research/` — notes on specific channels, directories, communities

### `03 Campaigns/{product}/{slug}/`

One folder per campaign. Inside:

- `brief.md`
- `assets/` (drafts per channel)
- `measurement.md`
- `notes.md`

### `04 Content Assets/{type}/{product}/`

Reusable per-type drafts. Each draft has a header with status (`draft` / `reviewed` / `approved`) and a `last_updated` date.

### `05 Metrics Exports/{tool}/`

Weekly or monthly raw exports. Filenames include date. Keep only the last 12 weeks at most; archive older to `_archive/` subfolders.

### `06 Weekly Reports/`

A copy of each entry in `weekly-growth-review.md`. Useful for sharing with future advisors or partners.

## How Agents Use Drive

- Pull source material when relevant
- Pull product docs before generating assets
- Pull metric exports for the analytics prompt
- Write drafts to the right folder
- Mark approval status in file headers, not by moving files
- Move only when archiving

## Status Header Format

Every asset file in Drive starts with:

```markdown
---
product: RunSmart | ResumeBuilder
channel: <channel>
status: draft | reviewed | approved | published | archived
hypothesis_id: <experiment ID from experiment-log.md, if any>
last_updated: YYYY-MM-DD
---
```

## Rules

- No secrets in Drive (API keys, env vars, credentials)
- No user PII without explicit founder approval
- Drive is not the source of truth for product facts — the project repo is
- Drive is not the planning layer — Notion is
- Drive is the document layer

## Connector Behavior

If a Google Drive connector is present at runtime (Claude Desktop, Codex, etc.):

- The agent may read and write inside `Agentic OS/Distribution OS/` only
- The agent must not modify files outside that path without explicit founder go-ahead
- If no connector is present, fall back to writing drafts inside `distribution-os/projects/{product}/scaffold/drafts/` and note in the reply that Drive sync is pending

## Founder Workflow Hint

When Drive is the destination, the founder review motion is:

1. Open the Drive folder
2. Skim the file header
3. Comment with edits or change status to `approved`
4. Notify the agent (chat) which path is approved and ready to publish (or which to publish where)
