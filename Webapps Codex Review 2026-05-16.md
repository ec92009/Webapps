# Webapps Codex Review 2026-05-16

Review timestamp: 2026-05-16 02:03 CEST.

1/ General architecture:
- The repo is now mostly a static hub plus a few local app folders, with canonical client projects moved to standalone repos.
- The remaining architectural opportunity is to drive the hub from a manifest so links, logos, categories, and canonical URLs do not drift by hand.

2/ UI:
- Hub cards and shared logo assets give the workspace a navigable front door.
- Grouping cards by client sites, games, tools, and external/canonical projects would make the hub easier to scan.

3/ UX:
- The README explains which projects are canonical elsewhere, which is important.
- The hub should communicate external/canonical destinations clearly so users do not mistake archives for active projects.

4/ Testing:
- No package manager is needed, but static checks would help.
- Add a link/asset checker for `index.html`, live app folders, archive boundaries, and external canonical links.

5/ Everything else:
- Archive naming is inconsistent across related projects (`Archive` vs `archive`), and this repo uses lowercase due existing structure.
- Keep old mirrors archived and avoid reintroducing duplicate canonical copies.

6/ My suggetions:
1. Create a `sites.json` manifest and generate or validate the hub from it.
2. Add a static link/asset checker for hub cards, logos, local apps, and canonical external URLs.
3. Group hub entries into client sites, games, tools, and archived/legacy references.
4. Add last-reviewed metadata for canonical external projects.
5. Keep archive content out of primary navigation unless explicitly labeled as legacy.
