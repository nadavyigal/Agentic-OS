---
name: portfolio-site
description: Refresh, validate, and privately publish the sanitized Portfolio HQ Site. Use for Portfolio HQ hosting, audience contracts, or Site updates.
---

# Portfolio Site

The local dashboard remains authoritative. The hosted Site is a reduced snapshot.

1. Run the Portfolio HQ unit tests and refresh script.
2. Verify founder, team, and public audience contracts contain no local paths, prompts, branch details, email addresses, or credential-shaped values.
3. Build and test `sites/portfolio-hq`.
4. Review the trust banner and contradiction list before publishing.
5. Save a version and deploy owner-only. Never change Site access to workspace-wide or public without explicit approval in the current request.
6. Return the private production URL and the evidence timestamp.
