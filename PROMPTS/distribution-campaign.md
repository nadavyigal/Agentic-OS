# Distribution Campaign Prompt

Thin pointer into the Distribution OS for a single-product campaign.

## Use

```
Read and execute: distribution-os/prompts/create-campaign.md
```

That prompt produces a campaign brief, channel-specific drafts, and a scored experiment row.

## Pre-Flight Inputs

- Product
- Campaign name (slug)
- Goal in one sentence with a metric
- Audience
- Channels in scope
- Start and end dates
- Any constraints you want enforced

## Constraints The Agent Will Apply

- One hypothesis per campaign
- One product
- Free / low-cost channels first
- Each asset labeled `draft` until you approve

## Where Output Lands

- Campaign folder: Drive `03 Campaigns/{product}/{slug}/`
- Drafts: per-channel inside the campaign folder
- Notion: Campaign Calendar + Experiment Backlog + Content / Asset Pipeline rows
- Logs: `distribution-os/experiment-log.md`

## When To Run

When a coordinated push across more than one channel is justified. Otherwise a single-skill workflow is enough.
