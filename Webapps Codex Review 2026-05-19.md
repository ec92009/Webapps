# Webapps Codex Review 2026-05-19

Timestamp: 2026-05-19 02:02:56 CEST

1/ General architecture

- Webapps is now mainly a hub plus a few local static apps, with canonical client projects moved to their own repos.
- The next architecture improvement is a `sites.json` manifest that generates the hub and carries active/archived/external metadata.
- Avoid reintroducing mirrors of canonical projects unless there is a deliberate publishing reason.

2/ UI

- The hub can become easier to scan if cards are grouped by client sites, games, tools, and external apps.
- Cards should show last-reviewed or canonical-source status so stale links are obvious.
- Keep the hub visually restrained; its job is navigation, not marketing each project equally.

3/ UX

- Users need to know when a card opens a local app versus an external canonical GitHub Pages site.
- Archived content should be discoverable for recovery but not presented as active.
- URLs should be stable, especially for small games and tools.

4/ Testing

- Add a static link/asset checker for hub and active project HTML files.
- Validate that canonical external links are reachable or at least syntactically correct.
- Add a no-stale-mirror check if canonical projects must stay out of the live tree.

5/everything else

- README explains canonical project boundaries well.
- The lowercase `archive/` folder exists; future cleanup should normalize naming deliberately.
- Keep Webapps focused as an index, not a dumping ground.

6/ My suggetions:

1. Create a `sites.json` manifest and generate the root hub from it.
2. Add link and asset checking for hub and active static apps.
3. Group hub cards by client sites, games, tools, and external apps.
4. Add last-reviewed/canonical-source metadata to external project links.
5. Normalize archive naming and document what belongs there.
