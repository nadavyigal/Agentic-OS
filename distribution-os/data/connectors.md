# Connectors — Notion + Google Drive IDs

Runtime lookup file. The agent reads this when it needs to write into Notion or Drive. Update this file when a new database is created or a folder is moved.

Last verified: 2026-05-27.

## Notion

Workspace parent: **Distribution OS** page
- URL: https://www.notion.so/36d5ef7c64bc8111bea4dd4348f0cef8
- Page ID: `36d5ef7c-64bc-8111-bea4-dd4348f0cef8`

### Databases

| Database | URL | Data Source ID (for queries / page creates) |
|---|---|---|
| Distribution Command Center | https://www.notion.so/d4c5fbe9d6704a558a7e6981a5179ba6 | `55180488-2f3a-4528-bce5-419d49b9bd7a` |
| Experiment Backlog | https://www.notion.so/9784346d4124430e9533d851596ab391 | `caeab2f8-40ca-432c-9707-8567eca0f13f` |
| Campaign Calendar | https://www.notion.so/9f80e93011f7483fbcfa336692f831b5 | `ac7adc74-c471-43e6-8e08-6c9df4706c2e` |
| Content Asset Pipeline | https://www.notion.so/5ce7cfe4e8764577ae3cc4107efedda5 | `7606d2e3-43b1-40f4-bd38-ebd0f05497dd` |
| Metrics Log | https://www.notion.so/4027df1722774c72b9492662a03d5fa7 | `7c7619a3-fe66-4d1a-a64a-9c04e56f6c7a` |
| Lessons Learned | https://www.notion.so/68d376ea8d904f6ea18aeb140f710bfc | `087b8ee2-0d56-4b68-87e0-e04d145b0948` |

### Existing (Founder Owned)

| Database | URL | Use |
|---|---|---|
| Social Media Calendar | https://www.notion.so/16e5ef7c64bc800691b3ffff8d2bdf1e | LinkedIn cadence; not the OS source of truth. Content Asset Pipeline is the OS source. |

### Property Cheat Sheet

Common values used across databases:

- **Product** select options: `RunSmart`, `ResumeBuilder` (Lessons Learned also has `Both`)
- **Channel** options (single-select on Experiment Backlog / Content Asset Pipeline / Lessons; multi-select on Command Center / Campaign Calendar):
  `ASO`, `Web landing`, `Free tool`, `Directory`, `Lifecycle email`, `CRO app`, `CRO web`, `Programmatic SEO`, `Bespoke SEO`, `LinkedIn`, `Partnerships`, `Launch`, `Community research`, `Hebrew market`
- **Status** values (Experiment Backlog): `proposed`, `approved`, `queued`, `running`, `paused`, `done-worked`, `done-failed`, `rejected`
- **Status** values (Campaign Calendar): `drafting`, `awaiting review`, `approved`, `scheduled`, `live`, `complete`
- **Status** values (Content Asset Pipeline): `draft`, `in review`, `approved`, `scheduled`, `published`, `archived`
- **Status** values (Command Center): `planning`, `in progress`, `review`, `done`
- **Approval status** (Campaign Calendar): `not yet`, `founder reviewed`, `approved`, `rejected`
- **Funnel stage** (Content Asset Pipeline): `acquisition`, `activation`, `retention`, `monetization`
- **Source** (Metrics Log): `PostHog`, `App Store Connect`, `Search Console`, `Vercel`, `Stripe`, `Manual`
- **Asset type** (Campaign Calendar, multi-select): `ASO listing`, `Landing page`, `LinkedIn post`, `Email`, `SEO brief`, `Directory pack`, `Free tool`, `Other`

### Score Formula (Experiment Backlog)

```
prop("Impact") + prop("Confidence") + prop("Speed") + prop("Founder fit") + prop("Strategic fit") - prop("Effort")
```

Computed automatically. Decision thresholds in `experiment-log.md`: `Score >= 15` do-now, `10–14` later, `< 10` reject.

## Google Drive

### Parent

| Folder | ID | URL |
|---|---|---|
| Distribution OS | `1uH_CHtd0wY-qaAHGO3SbVjTdRkXdRRJO` | https://drive.google.com/drive/folders/1uH_CHtd0wY-qaAHGO3SbVjTdRkXdRRJO |
| 00 Source Material (shared inbox) | `1HCnwli8dmx-8TXBV3XUlrMYvLkEKv5GR` | https://drive.google.com/drive/folders/1HCnwli8dmx-8TXBV3XUlrMYvLkEKv5GR |

### RunSmart IOS Marketing

Parent: `1CwUokNhjI1ZZLrsMNbr_WYssj9yg4E4s` — https://drive.google.com/drive/folders/1CwUokNhjI1ZZLrsMNbr_WYssj9yg4E4s

| Folder | ID |
|---|---|
| 01 Product Docs | `1aU6FotAsk-uwKP1xoyevRqWYKU5xkWnB` |
| 02 Market Research | `1dvSVn6zP_e2NgZNpcdUklmqRHwKhbrSo` |
| → Competitors | `1KqDpHpNDDOkuOLtgJF_BdkEu-uuisqMc` |
| → Customer Research | `1-cfC00oQh0FJft1sD8QfkK6xeYdMf0GZ` |
| → Channel Research | `1xiOMyx50u_Z_ooh89Pk0hcaIhl1JJ-9z` |
| → Partnerships | `1xZyd3I8mJbRcLOK98NLO4JgKcJzFzBEw` |
| 03 Campaigns | `1zFs25bRrWI-1uTiPRZ4VU8QXi2LpOJCD` |
| 04 Content Assets | `1_e517dxY1PbZlPk0bRITtwU3xpxEil7K` |
| → ASO Assets | `1AY1jW1TMBWpMpAqe4x6euhx_pJVl_CJJ` |
| → LinkedIn | `1e2Nqh29SBkNqmqmhRrsrdIhCOMgTBBa5` |
| → SEO Briefs | `1K4Fdcdz3c9HZXN7DeL_6Znpvd88vaMgm` |
| → Email | `110lsyZleQRHjajUXeERN2_zW5cEbKLEV` |
| → Directory Submissions | `1OdaVkxx3kqWX7bR9vFRfUdK_wiELwihw` |
| 05 Metrics Exports | `1ouUpihorcz6hNUN55DWIwTt8ADGc2QiE` |
| → PostHog | `17vcxXm2RXsxbhbFHEE2mUSfutZwLtHOn` |
| → App Store Connect | `1Iw9RNBfr67C1Vf5J0UEgcOs4QfMrV5qn` |
| → Search Console | `1jNfXBj1O2O3QBVDjSQwTJmarnrCySFFH` |
| → Vercel | `1dasD1bITq1Di6zWTJgHWYi4EZSYf1wqc` |
| → Stripe or Payments | `1L8c3RKkm-pnqQ9Pc9lElUjfupONaSPoR` |
| 06 Weekly Reports | `1ZECE9J5J-aT85UyxiRD2HLTIQbpDURFz` |

### ResumeBuilder IOS Marketing

Parent: `1a-kjPMRIK1ndEou4e75waiYXTANou59s` — https://drive.google.com/drive/folders/1a-kjPMRIK1ndEou4e75waiYXTANou59s

| Folder | ID |
|---|---|
| 01 Product Docs | `1mU8ivIZXwN5FkgQP4Knzg4on5WS1Dg0B` |
| 02 Market Research | `1a9NVfTpklh88s8Kkj0TuZkEDt-oGXgrQ` |
| → Competitors | `162_d6gSv2UaEehLFcWHAvMF38DlNmd_m` |
| → Customer Research | `1gtdDjAn2xR8-_lHQAhV0vJ8cTEG6RMEu` |
| → Channel Research | `1p0w5eLRFgOJ94228Ixy-t-lNJmM3KtQn` |
| → Partnerships | `1tmEetJ2vbbW2qmgzC4KsaV2UgsWpMOXr` |
| 03 Campaigns | `1cyLCfqhwWiS-c7tnRS3fS_X9fYKommeo` |
| 04 Content Assets | `1ULjAVbefWMghtiAG7urzRTabHOKmsL5p` |
| → ASO Assets | `1BK72D0ntGJJMP3lkfu6SfCjrFA9KRtIF` |
| → LinkedIn | `1XuYmlP5-LBMu8tTx1b6KhUcVFHs7hUKo` |
| → SEO Briefs | `1ZbD_739_95R5wnSVlVWkXel-mhggPMZm` |
| → Email | `1Uz-d7KH3qm5wXU0LymyxNd8HrB4NO1Tm` |
| → Directory Submissions | `1RjFBHjs4lNw8eZDW88-QlgHEqL1wnuGV` |
| 05 Metrics Exports | `1TL4JJ3Bj3WlQq5FOewp6mbtdNiLbZwmt` |
| → PostHog | `1g_PdCYU1ZNkUGr3q8QuL7vqtfS3ZyOUi` |
| → App Store Connect | `1y_8lNK4zaJhEzGMNKb1j9jD0FeAFrk6k` |
| → Search Console | `16oBYN_ZlvUQLpffsDsiiwskTjp-JJEnK` |
| → Vercel | `1eqPBb7yMtU9eZoySujYywZqL0Izfm5fF` |
| → Stripe or Payments | `1DrCZ189LGRbzEvwzah--FGxKsECuHFnV` |
| 06 Weekly Reports | `11jblv-RrEEqGPzC3s4XbFOYDB3BJqTax` |

## How The Agent Uses This

1. To **create a Notion page** in a database: pass `parent.data_source_id` = the data source ID from the table above
2. To **add a Drive file** in a specific folder: pass `parentId` = the folder ID from the table above
3. When **creating a campaign asset**: drop the draft into the right product's `03 Campaigns/{slug}/` folder (create the slug folder first, then the file)
4. When **logging a metric**: append a row in the Metrics Log database with the canonical metric name from `metrics-schema.md`
5. When **scoring an experiment**: write to Experiment Backlog; the `Score` column computes automatically
