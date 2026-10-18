#!/usr/bin/env python3
"""Check static file links, fragments, page semantics, and original coverage."""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, source: str):
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.duplicates: set[str] = set()
        self.links: list[str] = []
        self.h1_count = 0
        self.main_count = 0
        self.feed(source)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        values = dict(attrs)
        if identifier := values.get("id"):
            if identifier in self.ids:
                self.duplicates.add(identifier)
            self.ids.add(identifier)
        if tag == "h1":
            self.h1_count += 1
        if tag == "main":
            self.main_count += 1
        for field in ("href", "src"):
            if target := values.get(field):
                self.links.append(target)


def main() -> None:
    pages = {path: Page(path.read_text(encoding="utf-8")) for path in ROOT.glob("*.html")}
    originals = [ROOT / "README.md", *sorted(ROOT.glob("[0-9][0-9]-*.md"))]
    errors = []
    count = 0
    for path, page in pages.items():
        if page.duplicates or page.h1_count != 1 or page.main_count != 1:
            errors.append(f"{path.name}: duplicate IDs or invalid h1/main counts")
        for target in page.links:
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if resolved.is_dir():
                resolved /= "index.html"
            count += 1
            if not resolved.exists():
                errors.append(f"{path.name}: missing file {target}")
            elif parsed.fragment and resolved in pages and unquote(parsed.fragment) not in pages[resolved].ids:
                errors.append(f"{path.name}: missing anchor {target}")
    for path in originals:
        expected = ROOT / ("index.html" if path.stem == "README" else path.with_suffix(".html").name)
        if expected not in pages:
            errors.append(f"{path.name}: no HTML counterpart")
        if "비개발자" in path.read_text(encoding="utf-8"):
            errors.append(f"{path.name}: unwanted reader classification")
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            if not (path.parent / unquote(parsed.path)).exists():
                errors.append(f"{path.name}: missing Markdown link {target}")
    if len(pages) != 16 or len(originals) != 16:
        errors.append("Expected 16 originals and 16 HTML pages")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(originals)} originals, {len(pages)} pages, {count} local file/fragment links, unique IDs, one h1/main per page.")


if __name__ == "__main__":
    main()
