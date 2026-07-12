# Portfolio HQ Site

Private, responsive ChatGPT Site for Nadav's cross-product command center.

- Hosted Site: <https://nadav-portfolio-hq.nadav-yigal.chatgpt.site>
- Access: private allowlist, not public
- Authoritative operating view: `dashboard/portfolio-hq.html`
- Site-safe founder dataset: `data/portfolio-hq-founder.json`
- Generated source dataset: `dashboard/site-data/portfolio-hq-founder.json`

The Agentic OS refresh pipeline regenerates three audience-specific payloads: founder, team, and public. The Site currently uses the founder payload. Generated payloads remove local paths, emails, command prompts, branch details, and credential-shaped values before content reaches the hosting project.

## Local checks

```bash
npm install
npm run dev
npm test
npm run lint
```

Run `./agentic-os refresh` from the repository root before publishing a new Site version. Publishing is a separate, deliberate action and must keep the Site's private access policy.
