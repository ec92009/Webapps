# Webapps Codex Review 2026-05-14

Review timestamp: 2026-05-14, Europe/Madrid.

1/ General architecture

- The repo now functions as a static hub plus a few local standalone apps; canonical client projects have been moved to their own repos.
- The README's canonical-project section is important and should remain the source of truth for what belongs here.
- A manifest-driven hub would reduce manual drift between cards, logos, project URLs, and archive state.

2/ UI

- Hub cards should be grouped by purpose so visitors can scan client sites, games, tools, and external/canonical projects separately.
- Logos are useful, but missing or stale logo assets need automated detection.
- Static games/tools should retain clear individual visual identities while the hub remains quiet and navigational.

3/ UX

- The hub should make active versus archived versus external/canonical destinations unambiguous.
- External canonical links need last-reviewed or version hints so users know when a card may be stale.
- Avoid mirroring full standalone sites in this repo unless there is a deliberate deployment reason.

4/ Testing

- Add static link, asset, and HTML validity checks for the hub and local app pages.
- Add a check that canonical project links match README metadata.
- Add screenshot smoke checks for the root hub and at least one local app.

5/ Everything else

- The repo uses lowercase `archive/` for review history; keep that consistent or document why it differs from other repos.
- `scripts/root_dependency_audit.py` is a good start; expand this maintenance script rather than adding ad hoc checks.
- Keep old mirrors under archive and out of the live navigation.

6/ My suggetions:

1. Add a `sites.json` manifest and generate the root hub cards from it.
2. Extend static QA to check links, local assets, canonical URLs, and HTML validity.
3. Group hub cards by client sites, games, tools, and external/canonical projects.
4. Add last-reviewed/version metadata for canonical external links.
5. Normalize review archive naming or document the lowercase `archive/` convention.
6. Add a root-hub mobile screenshot smoke check.
