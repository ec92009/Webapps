# Webapps Codex Review 2026-05-17

Reviewed: 2026-05-17 02:04

1/ General architecture:
- The repo acts as a static hub plus archived snapshots of other projects, which can work if the manifest/canonical-source boundary is explicit.
- A generated or validated `sites.json` would prevent hub cards, logos, local paths, and canonical URLs from drifting.
- Archive content should remain discoverable but not compete with live projects.

2/ UI:
- A hub UI benefits from density, grouping, and current status metadata.
- Logos and cards should communicate category and live/archive status at a glance.
- The hub should avoid sending users into stale archived versions without clear labeling.

3/ UX:
- Users need to find the right project quickly: client sites, games, tools, and archived references should be grouped.
- Each entry should say whether it is local-only, GitHub Pages, active production, or legacy.
- Last-reviewed metadata would help decide what deserves attention.

4/ Testing:
- Add a static link/asset checker for hub cards, logos, local app paths, and external URLs.
- Add validation that every hub entry has title, category, status, target URL, and optional archive note.
- Add a smoke check for the root page and a few representative app pages.

5/ Everything else:
- The repo is ahead of origin, so GitHub handoff is incomplete.
- Archive snapshots from other repos can become confusing if not labeled with source/date.
- The root dependency audit script is a useful pattern; extend that idea to hub metadata.

6/ My suggetions:
1. Create a `sites.json` manifest and validate or generate the hub from it.
2. Add a static link/asset checker for cards, logos, app paths, and canonical URLs.
3. Group entries into client sites, games, tools, and archived/legacy references.
4. Add status and last-reviewed metadata to each hub entry.
5. Push the current local commits after hub metadata rules are documented.
