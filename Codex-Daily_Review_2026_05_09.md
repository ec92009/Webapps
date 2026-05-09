# Codex Daily Review — 2026-05-09

## Architecture
- Nice “static workspace hub” concept; the mirrored `PhotosByElie/` inside this repo risks divergence from the standalone repo—prefer a single source of truth.
- Consider normalizing folder naming and entrypoints so each sub-app has the same “open index.html, works” guarantee.

## UI
- The hub’s job is fast routing; prioritize clear cards, short descriptions, and a consistent “open in new tab” behavior for external GitHub Pages sites.

## UX
- Add a tiny “local preview” hint on the hub page (port + command) so this repo remains easy to pick up on a fresh machine.
- If any sub-app depends on runtime fonts/assets, make the failure mode graceful (fallback fonts, clear missing-asset styling).

## Misc
- Keep “no build step required” true: resist creeping per-subfolder tooling unless it’s clearly worth it.
