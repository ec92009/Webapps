# Webapps Codex Review 2026-05-11

Review time: 2026-05-11 02:05 CEST.

1/ General architecture

- The repo is now positioned as a static webapp hub plus a few local apps, while canonical business sites have moved to their own repos. That boundary is healthy.
- The file count is still high because archive content remains nearby. Keep live app paths clearly separated from historical mirrors.
- The root dependency audit script is a good maintenance signal.

2/ UI

- The hub should be utilitarian: clear links to Conway, Reversi, sorting algorithms, Tap Me Plus 1, and canonical external sites.
- Avoid visual language that suggests archived mirrors are current products.
- Each static app should keep its own compact controls and not inherit business-site styling unless intentional.

3/ UX

- The README explains canonical project locations well. The live site should mirror that clarity so users do not land in stale copies.
- If the hub links out to canonical repos/pages, labels should clearly distinguish local demos from published projects.
- Add "last updated" or version cues only where they help avoid stale app confusion.

4/ Testing

- No automated tests were found.
- Add link checks for the hub and all live static app routes.
- Add browser smoke checks for each app's first interaction: Conway step/start, Reversi legal move, sorting start, and Tap Me increment.

5/ Everything else

- Existing review archives live under lowercase `archive/`, so today's older reviews were kept with that convention.
- Consider excluding archived mirrors from broad maintenance scripts unless explicitly requested.

6/ My suggetions:

1. Add a live-route manifest that lists only currently supported hub apps.
2. Add a link-check script for root and live app pages.
3. Add Playwright smoke tests for one core interaction per live app.
4. Ensure archived mirrors are not linked from primary navigation.
5. Keep README and hub labels aligned around canonical repo locations.
