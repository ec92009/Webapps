# Codex Review - 2026.05.02

## Architecture

- Webapps is intentionally simple: mostly static HTML/CSS/JS projects with a root index and a small dependency-audit script.
- The current branch is `codex/byelie-viewport-sizing`, not `main`, and it is current with its configured upstream.
- The main architectural risk is repo sprawl. The root index, active projects, archived copies, and audit docs need clear boundaries so small site fixes do not become cross-project churn.

## UI

- The individual apps are lightweight and easy to serve locally, which is the right posture for this collection.
- The root index should keep acting as a practical launcher rather than a marketing page.
- Archive styling and active project styling should not drift into each other unless the archive is intentionally revived.

## UX

- A no-build static workflow keeps the sites easy to inspect and recover.
- The useful next UX improvement is consistency: each active app should have a predictable landing state, keyboard behavior where relevant, and obvious back-navigation to the root index.
- The root dependency audit script is a good maintenance affordance and should stay small.

## Misc

- No pre-existing local dirty state was present before this review.
- No code changes were made as part of this review.
- Suggested next low-risk task: document which project folders are active versus archived in the root README.
