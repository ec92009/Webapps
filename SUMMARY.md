# Conversation Summary

Date: 2026-05-02

## Scope

The Webapps repo acted as the hub for the Photos By Elie work. The hub now links to the standalone PhotosByElie GitHub Pages site and also carries a mirrored `PhotosByElie/` folder for direct hub-relative access.

## Hub Updates

- Added Photos By Elie as a top-level hub card alongside the existing web apps.
- Kept the hub card pointed at `https://ec92009.github.io/PhotosByElie/`.
- Updated the hub card version through the PhotosByElie iterations, ending at `v63.12`.
- Synced the mirrored `PhotosByElie/` folder after each standalone site change.

## Mirrored PhotosByElie State

- Collections: France, USA, Spain, Mexico, AI.
- AI remains last in the collection order.
- AI gallery uses eight resized Leonardo-generated JPGs in `PhotosByElie/assets/ai/`.
- `photo.html` detail pages auto-sync checkbox changes to the basket.
- `basket.html` is localStorage-backed and treats one photo as one charge row.
- Resolution choices can be changed from either detail or basket.
- Resolution choices are limited by each photo's source megapixels; 2 MP AI images only expose full/native and JPG 1 MP.
- Full resolution checkboxes show the original source size, including source description and megapixel count.
- Basket rows stay visible at `$0` when all resolutions are unchecked; only Remove deletes the row.

## Deployment

- Repo: `https://github.com/ec92009/Webapps.git`
- GitHub Pages: `https://ec92009.github.io/Webapps/`
- Latest relevant hub version: `v63.12`
- Latest conversation push before this summary: Photos By Elie `v63.12` basket empty-selection sync.
