#!/usr/bin/env zsh
# urls.sh — print byElie cycle-end URLs
# Usage: zsh urls.sh  (run from anywhere in the repo)

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
PROJECT="byElie"

# Version from index.html
VERSION=$(grep -o 'v[0-9]\+\.[0-9]\+' "$REPO_ROOT/$PROJECT/index.html" | head -1)

# LAN IP (auto-detect, fallback to known address)
LAN_IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo "192.168.1.160")

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  byElie — ${VERSION}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  localhost  http://localhost:8000/${PROJECT}/"
echo "  LAN        http://${LAN_IP}:8000/${PROJECT}/"
echo "  live       https://ec92009.github.io/Webapps/${PROJECT}/"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
