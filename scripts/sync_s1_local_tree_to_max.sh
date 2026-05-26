#!/usr/bin/env bash
set -euo pipefail

peer="${1:-max}"
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
remote_root="${REMOTE_WEBAPPS_ROOT:-/Users/ecohen/Dev/Webapps}"

required_files=(
  "$repo_root/index.html"
  "$repo_root/s1/index.html"
  "$repo_root/s1/task-tree.json"
  "$repo_root/s1/task-tree.local.json"
  "$repo_root/scripts/sync_s1_local_tree_to_max.sh"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing required file: $file" >&2
    exit 1
  fi
done

ssh "$peer" "mkdir -p '$remote_root/s1' '$remote_root/scripts'"
rsync -az --checksum \
  "$repo_root/index.html" \
  "$peer:$remote_root/"
rsync -az --checksum \
  "$repo_root/s1/index.html" \
  "$repo_root/s1/task-tree.json" \
  "$repo_root/s1/task-tree.local.json" \
  "$peer:$remote_root/s1/"
rsync -az --checksum \
  "$repo_root/scripts/sync_s1_local_tree_to_max.sh" \
  "$peer:$remote_root/scripts/"

ssh "$peer" "python3 - <<'PY'
import json
from pathlib import Path

root = Path('$remote_root')
public_data = json.loads((root / 's1/task-tree.json').read_text())
local_data = json.loads((root / 's1/task-tree.local.json').read_text())
print('Max S1 public version:', public_data.get('version'))
print('Max local overlay label:', local_data.get('localOverlay', {}).get('label', {}).get('en'))
print('Max local overlay tasks:', len(local_data.get('tasks', [])))
PY"
