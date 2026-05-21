#!/usr/bin/env python3
"""Refresh the root hub with the latest app versions."""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover - Python 3.8 fallback.
    ZoneInfo = None


ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "index.html"
VERSION_BASE_DATE = dt.date(2026, 2, 28)
DEFAULT_TIMEZONE = "Europe/Madrid"
MAX_REMOTE_PAGES = 40

VERSION_RE = re.compile(r"\bv(\d+)\.(\d+)\b", re.IGNORECASE)
HUB_VERSION_RE = re.compile(r'(<span id="hub-version">)v\d+\.\d+(</span>)')
CARD_REGION_RE = re.compile(
    r"(?P<start>\s*<!-- site-card:start -->\n)"
    r"(?P<body>.*?)"
    r"(?P<end>\n\s*<!-- site-card:end -->)",
    re.DOTALL,
)
CARD_RE = re.compile(
    r"(?ms)^[ \t]*<section class=\"card\" data-site-card\b.*?^[ \t]*</section>"
)


@dataclass
class Card:
    block: str
    site_id: str
    name: str
    sources: list[str]
    current_version: str
    new_version: str | None = None


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        for name, value in attrs:
            if name.lower() == "href" and value:
                self.hrefs.append(value)


def attr_value(text: str, name: str) -> str:
    match = re.search(rf'\b{name}="([^"]*)"', text)
    return match.group(1) if match else ""


def set_attr(text: str, name: str, value: str) -> str:
    if re.search(rf'\b{name}="[^"]*"', text):
        return re.sub(rf'(\b{name}=")[^"]*(")', rf"\g<1>{value}\2", text, count=1)
    return re.sub(r"(<section\b[^>]*)(>)", rf'\1 {name}="{value}"\2', text, count=1)


def visible_name(block: str) -> str:
    match = re.search(r"<h2>(.*?)</h2>", block, re.DOTALL)
    if not match:
        return attr_value(block, "data-site-id") or "unknown"
    return re.sub(r"<[^>]+>", "", match.group(1)).strip()


def normalize_version(major: str, minor: str) -> str:
    return f"v{int(major)}.{int(minor)}"


def version_key(version: str) -> tuple[int, int]:
    match = re.match(r"^v(\d+)\.(\d+)$", version or "", re.IGNORECASE)
    return (int(match.group(1)), int(match.group(2))) if match else (-1, -1)


def best_version(versions: list[str], fallback: str = "") -> str:
    clean = [version for version in versions if version_key(version) != (-1, -1)]
    if not clean:
        return fallback
    return max(clean, key=version_key)


def extract_versions(text: str) -> list[str]:
    return [normalize_version(match.group(1), match.group(2)) for match in VERSION_RE.finditer(text)]


def parse_cards(index_html: str) -> list[Card]:
    region = CARD_REGION_RE.search(index_html)
    if not region:
        raise RuntimeError("Could not find site-card markers in index.html")

    cards: list[Card] = []
    for match in CARD_RE.finditer(region.group("body")):
        block = match.group(0)
        current = attr_value(block, "data-version") or best_version(extract_versions(block))
        sources = [
            source.strip()
            for source in attr_value(block, "data-version-source").split(",")
            if source.strip()
        ]
        cards.append(
            Card(
                block=block,
                site_id=attr_value(block, "data-site-id"),
                name=visible_name(block),
                sources=sources,
                current_version=current,
            )
        )

    if not cards:
        raise RuntimeError("No site cards found in index.html")
    return cards


def local_source_path(source: str) -> Path | None:
    parsed = urllib.parse.urlsplit(source)
    if parsed.scheme or parsed.netloc:
        return None

    source_path = urllib.parse.unquote(parsed.path)
    path = (ROOT / source_path).resolve()
    try:
        path.relative_to(ROOT)
    except ValueError:
        print(f"Skipping local source outside repo: {source}", file=sys.stderr)
        return None
    return path


def local_versions(source: str) -> list[str]:
    path = local_source_path(source)
    if path is None:
        return []

    if path.is_dir():
        files = sorted(path.rglob("*.html"))
    else:
        files = [path]

    versions: list[str] = []
    for html_file in files:
        if not html_file.exists():
            print(f"Missing local version source: {html_file}", file=sys.stderr)
            continue
        versions.extend(extract_versions(html_file.read_text(encoding="utf-8")))
    return versions


def cache_busted(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query.append(("_hub_check", str(int(time.time()))))
    return urllib.parse.urlunsplit(
        parsed._replace(query=urllib.parse.urlencode(query), fragment="")
    )


def fetch_remote(url: str) -> str:
    request = urllib.request.Request(
        cache_busted(url),
        headers={"User-Agent": "webapps-hub-version-checker/1.0"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def page_like_url(url: str) -> bool:
    path = urllib.parse.urlsplit(url).path
    suffix = Path(path).suffix.lower()
    return not suffix or suffix in {".html", ".htm"}


def same_remote_page(candidate: str, root: urllib.parse.SplitResult) -> bool:
    parsed = urllib.parse.urlsplit(candidate)
    root_path = root.path if root.path.endswith("/") else f"{root.path}/"
    return (
        parsed.scheme in {"http", "https"}
        and parsed.scheme == root.scheme
        and parsed.netloc == root.netloc
        and parsed.path.startswith(root_path)
        and page_like_url(candidate)
    )


def remote_versions(source: str) -> list[str]:
    parsed_source = urllib.parse.urlsplit(source)
    if parsed_source.scheme not in {"http", "https"}:
        return []

    root = parsed_source._replace(query="", fragment="")
    root_url = urllib.parse.urlunsplit(root)
    queue = [root_url]
    seen: set[str] = set()
    versions: list[str] = []

    while queue and len(seen) < MAX_REMOTE_PAGES:
        url = queue.pop(0)
        key = urllib.parse.urlunsplit(urllib.parse.urlsplit(url)._replace(query="", fragment=""))
        if key in seen:
            continue
        seen.add(key)

        try:
            html = fetch_remote(url)
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            print(f"Could not fetch {url}: {error}", file=sys.stderr)
            continue

        versions.extend(extract_versions(html))

        parser = LinkParser()
        parser.feed(html)
        for href in parser.hrefs:
            candidate = urllib.parse.urljoin(url, href)
            candidate = urllib.parse.urlunsplit(
                urllib.parse.urlsplit(candidate)._replace(query="", fragment="")
            )
            if same_remote_page(candidate, root) and candidate not in seen and candidate not in queue:
                queue.append(candidate)

    return versions


def discover_version(card: Card) -> str:
    discovered: list[str] = []
    for source in card.sources:
        discovered.extend(local_versions(source))
        discovered.extend(remote_versions(source))
    return best_version(discovered, fallback=card.current_version)


def set_query_version(href: str, version: str) -> str:
    parsed = urllib.parse.urlsplit(href)
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query = [(key, value) for key, value in query if key != "v"]
    query.append(("v", version.lstrip("vV")))
    return urllib.parse.urlunsplit(parsed._replace(query=urllib.parse.urlencode(query)))


def update_card_block(block: str, version: str) -> str:
    block = set_attr(block, "data-version", version)
    block = re.sub(
        r'(<span class="version-label">)v\d+\.\d+(</span>)',
        rf"\g<1>{version}\2",
        block,
        count=1,
    )

    def replace_href(match: re.Match[str]) -> str:
        return f'{match.group(1)}{set_query_version(match.group(2), version)}{match.group(3)}'

    return re.sub(r'(<a class="btn" href=")([^"]+)(")', replace_href, block, count=1)


def current_hub_version(index_html: str) -> str:
    match = HUB_VERSION_RE.search(index_html)
    return match.group(0).split(">")[1].split("<")[0] if match else ""


def todays_version_major() -> int:
    timezone_name = os.environ.get("WEBAPPS_VERSION_TZ", DEFAULT_TIMEZONE)
    if ZoneInfo:
        today = dt.datetime.now(ZoneInfo(timezone_name)).date()
    else:
        today = dt.date.today()
    return (today - VERSION_BASE_DATE).days


def bumped_hub_version(current: str) -> str:
    current_major, current_minor = version_key(current)
    today_major = todays_version_major()
    if current_major == today_major:
        return f"v{today_major}.{current_minor + 1}"
    return f"v{today_major}.0"


def replace_hub_version(index_html: str, version: str) -> str:
    if not HUB_VERSION_RE.search(index_html):
        raise RuntimeError("Could not find hub version span in index.html")
    return HUB_VERSION_RE.sub(rf"\g<1>{version}\2", index_html, count=1)


def refresh_index(no_hub_bump: bool) -> tuple[bool, list[str]]:
    index_html = INDEX_PATH.read_text(encoding="utf-8")
    cards = parse_cards(index_html)
    changes: list[str] = []

    for card in cards:
        card.new_version = discover_version(card)
        if card.new_version != card.current_version:
            changes.append(f"{card.name}: {card.current_version} -> {card.new_version}")
            card.block = update_card_block(card.block, card.new_version)

    original_order = [card.site_id for card in cards]
    cards.sort(
        key=lambda card: version_key(card.new_version or card.current_version),
        reverse=True,
    )
    sorted_order = [card.site_id for card in cards]
    order_changed = original_order != sorted_order
    if order_changed:
        changes.append("card order refreshed")

    region = CARD_REGION_RE.search(index_html)
    if not region:
        raise RuntimeError("Could not find site-card markers in index.html")

    new_body = "\n".join(card.block for card in cards)
    updated_html = (
        index_html[: region.start("body")]
        + new_body
        + index_html[region.end("body") :]
    )

    should_bump_hub = bool(changes) and not no_hub_bump
    if should_bump_hub:
        current = current_hub_version(updated_html)
        next_version = bumped_hub_version(current)
        if next_version != current:
            updated_html = replace_hub_version(updated_html, next_version)
            changes.append(f"hub: {current} -> {next_version}")

    changed = updated_html != index_html
    if changed:
        INDEX_PATH.write_text(updated_html, encoding="utf-8")

    return changed, changes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--no-hub-bump",
        action="store_true",
        help="Update card versions/order without changing the hub version.",
    )
    args = parser.parse_args()

    changed, changes = refresh_index(no_hub_bump=args.no_hub_bump)
    if changes:
        print("\n".join(changes))
    else:
        print("No hub version changes found.")
    return 0 if changed or not changes else 0


if __name__ == "__main__":
    raise SystemExit(main())
