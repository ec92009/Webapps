# Conversation Summary

Date: 2026-05-02

## Scope

The Webapps repo acted as the hub for the Photos By Elie work. The hub now links to the standalone PhotosByElie GitHub Pages site and also carries a mirrored `PhotosByElie/` folder for direct hub-relative access.

## Hub Updates

- Added Photos By Elie as a top-level hub card alongside the existing web apps.
- Kept the hub card pointed at `https://ec92009.github.io/PhotosByElie/`.
- Updated the hub card version through the PhotosByElie iterations, ending at `v63.8`.
- Synced the mirrored `PhotosByElie/` folder after each standalone site change.

## Mirrored PhotosByElie State

- Collections: France, USA, Spain, Mexico, AI.
- AI remains last in the collection order.
- AI gallery uses eight resized Leonardo-generated JPGs in `PhotosByElie/assets/ai/`.
- `photo.html` detail pages auto-sync checkbox changes to the basket.
- `basket.html` is localStorage-backed and treats one photo as one charge row.
- Resolution choices can be changed from either detail or basket.

## Deployment

- Repo: `https://github.com/ec92009/Webapps.git`
- GitHub Pages: `https://ec92009.github.io/Webapps/`
- Latest relevant hub version: `v63.8`
- Latest conversation push before this summary: `be14482 hub: sync Photos By Elie auto basket`
