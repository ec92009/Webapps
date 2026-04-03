from __future__ import annotations

from collections import defaultdict, deque
from html.parser import HTMLParser
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
START = ROOT / "index.html"
IGNORED_TOP_LEVEL_DIRS = {"archive"}

FOLLOW_EXTENSIONS = {".html", ".css", ".js"}
CONSIDER_EXTENSIONS = {
    ".html",
    ".css",
    ".js",
    ".png",
    ".jpg",
    ".jpeg",
    ".svg",
    ".pdf",
    ".md",
    ".py",
}
NON_RUNTIME_NAMES = {".gitignore", "AGENTS.md", "README.md"}


class HtmlRefParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._collect(tag, attrs)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._collect(tag, attrs)

    def _collect(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key: value for key, value in attrs if value is not None}

        for key in ("href", "src", "data-href", "action", "poster"):
            value = attr_map.get(key)
            if value:
                self.refs.append(value)

        if tag == "meta":
            http_equiv = attr_map.get("http-equiv", "").lower()
            content = attr_map.get("content", "")
            if http_equiv == "refresh" and content:
                match = re.search(r"url=([^;]+)$", content, re.IGNORECASE)
                if match:
                    self.refs.append(match.group(1).strip())

        style = attr_map.get("style")
        if style:
            self.refs.extend(find_css_urls(style))


def find_css_urls(text: str) -> list[str]:
    return [match.strip().strip("\"'") for match in re.findall(r"url\(([^)]+)\)", text)]


def clean_ref(ref: str) -> str | None:
    ref = ref.strip().strip("\"'")
    if not ref or ref.startswith("#"):
        return None
    if ref.startswith(("http://", "https://", "//", "mailto:", "tel:", "javascript:", "data:")):
        return None
    return ref.split("#", 1)[0].split("?", 1)[0]


def resolve_ref(base_file: Path, ref: str) -> Path | None:
    cleaned = clean_ref(ref)
    if not cleaned:
        return None

    resolved = (base_file.parent / cleaned).resolve()
    try:
        resolved.relative_to(ROOT)
    except ValueError:
        return None

    if resolved.is_dir() or cleaned.endswith("/"):
        resolved = resolved / "index.html"

    return resolved if resolved.exists() else None


def scan_local_refs(path: Path) -> list[Path]:
    text = path.read_text(errors="ignore")
    refs: list[str] = []

    if path.suffix.lower() == ".html":
        parser = HtmlRefParser()
        parser.feed(text)
        refs.extend(parser.refs)
        refs.extend(find_css_urls(text))
    elif path.suffix.lower() == ".css":
        refs.extend(find_css_urls(text))

    resolved: list[Path] = []
    for ref in refs:
        target = resolve_ref(path, ref)
        if target:
            resolved.append(target)
    return resolved


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def node_id(path: Path) -> str:
    return "n_" + re.sub(r"[^a-zA-Z0-9_]", "_", rel(path))


def classify_isolated(paths: list[Path]) -> dict[str, list[Path]]:
    groups: dict[str, list[Path]] = defaultdict(list)
    for path in paths:
        relative = rel(path)
        name = path.name
        suffix = path.suffix.lower()

        if name in NON_RUNTIME_NAMES:
            groups["Repo support files"].append(path)
        elif relative.startswith("oleamediaco/source/"):
            groups["Source inputs and PDF tooling"].append(path)
        elif relative.startswith("oleataxco/concepts/"):
            groups["Legacy Olea Tax concept pages"].append(path)
        elif relative in {
            "Codex/index.html",
            "OleaMedia/index.html",
            "OleaTax/index.html",
            "oleataxco/Codex/index.html",
            "oleataxco/OleaMedia/index.html",
            "oleataxco/OleaTax/index.html",
        }:
            groups["Redirect pages not linked from the root site"].append(path)
        elif relative.startswith("oleamediaco/v4/") or relative.startswith("oleamediaco/v5/"):
            groups["Unlinked Olea Media variants"].append(path)
        elif relative in {"oleamediaco/script.js", "oleamediaco/styles.css"}:
            groups["Unlinked Olea Media root assets"].append(path)
        elif relative.startswith("byElie/assets/"):
            groups["Unused By Elie assets"].append(path)
        elif relative.startswith("oleataxco-v25/") and suffix == ".pdf":
            groups["Unlinked Olea Tax v25 PDFs"].append(path)
        elif suffix in {".md", ".py"}:
            groups["Project docs and helper scripts"].append(path)
        else:
            groups["Other isolated files"].append(path)
    return dict(groups)


def suggested_action(group: str) -> str:
    actions = {
        "Repo support files": "Keep. These are repo-operational files, not site runtime files.",
        "Source inputs and PDF tooling": "Keep or move into a future `archive/source/` folder if you want a cleaner published tree.",
        "Legacy Olea Tax concept pages": "Good archive candidates if the current Olea Tax homepage is the only intended live path.",
        "Redirect pages not linked from the root site": "Safe to archive if you do not rely on old direct URLs.",
        "Unlinked Olea Media variants": "Strong archive candidates. Nothing in the root crawl points to these variants.",
        "Unlinked Olea Media root assets": "Archive or delete after a quick visual grep check; they have no inbound links in the root crawl.",
        "Unused By Elie assets": "Archive first. These look safe to remove from the live tree if no future page will use them.",
        "Unlinked Olea Tax v25 PDFs": "Either add links from the page or archive them beside other v25 reference material.",
        "Project docs and helper scripts": "Keep. These are support files outside the live site graph.",
        "Other isolated files": "Review manually before moving.",
    }
    return actions[group]


def main() -> None:
    all_files = sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and not any(part in IGNORED_TOP_LEVEL_DIRS for part in path.relative_to(ROOT).parts[:1])
    )
    considered = {
        path
        for path in all_files
        if path.suffix.lower() in CONSIDER_EXTENSIONS or path.name in NON_RUNTIME_NAMES
    }

    reachable: set[Path] = set()
    edges: set[tuple[Path, Path]] = set()
    queue = deque([START])
    queued: set[Path] = {START}

    while queue:
        current = queue.popleft()
        queued.discard(current)
        if current in reachable or not current.exists():
            continue

        reachable.add(current)
        for target in scan_local_refs(current):
            if target == current:
                continue
            edges.add((current, target))
            if target.suffix.lower() not in FOLLOW_EXTENSIONS:
                reachable.add(target)
            if target.suffix.lower() in FOLLOW_EXTENSIONS and target not in reachable and target not in queued:
                queue.append(target)
                queued.add(target)

    isolated = sorted(considered - reachable, key=rel)
    isolated_groups = classify_isolated(isolated)

    root_children = sorted(
        target for source, target in edges if source == START and target.suffix.lower() == ".html"
    )
    root_assets = sorted(
        target for source, target in edges if source == START and target.suffix.lower() != ".html"
    )

    print("# Root Dependency Audit")
    print()
    print("Generated from a local crawl that starts at `index.html` and follows local HTML/CSS/JS references only.")
    print()
    print("## Summary")
    print()
    print(f"- Reachable local files from root crawl: `{len(reachable)}`")
    print(f"- Isolated local files in repo scope: `{len(isolated)}`")
    print(f"- Root-linked project entry pages: `{len(root_children)}`")
    print()
    print("External URLs like Google Fonts, mailto links, and WhatsApp links are intentionally excluded from the local graph.")
    print("The `archive/` folder is also excluded so this report describes the live tree only.")
    print()
    print("## Graph")
    print()
    print("```mermaid")
    print("flowchart TD")
    for source, target in sorted(edges, key=lambda pair: (rel(pair[0]), rel(pair[1]))):
        print(f'  {node_id(source)}["{rel(source)}"] --> {node_id(target)}["{rel(target)}"]')
    print("```")
    print()
    print("## Root Entry Points")
    print()
    print("- Root page: `index.html`")
    for child in root_children:
        print(f"- Root-linked page: `{rel(child)}`")
    for asset in root_assets:
        print(f"- Root-linked asset: `{rel(asset)}`")
    print()
    print("## Isolated Files")
    print()
    for group, paths in isolated_groups.items():
        print(f"### {group}")
        print()
        print(suggested_action(group))
        print()
        for path in paths:
            print(f"- `{rel(path)}`")
        print()


if __name__ == "__main__":
    main()
