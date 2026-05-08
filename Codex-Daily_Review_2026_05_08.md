# Codex Daily Review — 2026-05-08 (Webapps)

## Architecture
- This is a static-site workspace hub (HTML/CSS/JS) with no build step, which keeps deploy friction near zero.
- The mirrored `PhotosByElie/` inside this repo is convenient, but duplication risk is real (version skew is inevitable).
- Scripts/docs exist, but the repo is “many small sites”; consider a simple index of each sub-app’s entrypoint + purpose.

## UI
- Hub approach (`index.html` + shared `assets/`) is straightforward; ensure cards stay scannable as the list grows.

## UX
- Local preview via `python3 -m http.server` is a good default; add a short “ports + caching gotchas” note if it bites often.
- External links (standalone GitHub Pages projects) keep the hub lightweight; keep link health checked occasionally.

## Misc
- Naming is slightly inconsistent (`archive/` vs `Archived/`); pick one convention to avoid “where did it go?” friction.
- If the mirror stays, document the update workflow (copy vs sync) so it doesn’t silently rot.
