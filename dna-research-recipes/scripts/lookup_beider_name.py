#!/usr/bin/env python3
"""Look up a few Beider index entries without exposing the whole forum page."""

from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import unicodedata
from html.parser import HTMLParser
from http.client import HTTPException
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, HTTPSHandler, Request, build_opener

MANIFEST = Path(__file__).resolve().parents[1] / "resources" / "beider-name-indexes.json"
MAX_BYTES = 3 * 1024 * 1024
TIMEOUT_SECONDS = 15
MAX_LIMIT = 50
VOID_TAGS = frozenset(
    (
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
        "param",
        "source",
        "track",
        "wbr",
    )
)
LINE_TAGS = frozenset(("br", "div", "p", "li", "tr"))
DASHES = str.maketrans({char: "-" for char in "‐‑‒–—−"})
# Some published forms use a Latin I among Cyrillic letters. Preserve that spelling.
ENTRY = re.compile(r"^([А-ЯЁІЇЄа-яёіїєI][А-ЯЁІЇЄа-яёіїєI '\-]*)\s+\(([A-Z][A-Z' -]*)\)$")


class SourceUnavailable(Exception):
    """A source cannot support either a positive or a negative lookup."""


def normalize_name(value: str) -> str:
    """Match case, spacing and hyphens, retaining the distinction between ё and е."""
    value = unicodedata.normalize("NFC", value).translate(DASHES).upper()
    value = " ".join(value.split())
    return re.sub(r"\s*-\s*", "-", value)


class FirstPostParser(HTMLParser):
    """Extract only the selected phpBB post's content, excluding quoted replies."""

    def __init__(self, post_id: str):
        super().__init__(convert_charrefs=True)
        self.post_id = post_id
        self.stack: list[str] = []
        self.post_depth: int | None = None
        self.content_depth: int | None = None
        self.quote_depth: int | None = None
        self.found_post = False
        self.found_content = False
        self.completed_content = False
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        depth = len(self.stack)
        if attributes.get("id") == self.post_id:
            self.post_depth = depth
            self.found_post = True
        if (
            self.post_depth is not None
            and self.content_depth is None
            and "content" in (attributes.get("class") or "").split()
        ):
            self.content_depth = depth
            self.found_content = True
        if self.content_depth is not None:
            if tag == "blockquote" and self.quote_depth is None:
                self.quote_depth = depth
            if self.quote_depth is None and tag in LINE_TAGS:
                self.parts.append("\n")
        if tag not in VOID_TAGS:
            self.stack.append(tag)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in VOID_TAGS:
            self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag not in self.stack:
            return
        depth = len(self.stack) - 1 - self.stack[::-1].index(tag)
        if self.content_depth is not None and self.quote_depth is None and tag in LINE_TAGS:
            self.parts.append("\n")
        if self.quote_depth is not None and depth <= self.quote_depth:
            self.quote_depth = None
        if self.content_depth is not None and depth <= self.content_depth:
            if depth == self.content_depth:
                self.completed_content = True
            self.content_depth = None
        if self.post_depth is not None and depth <= self.post_depth:
            self.post_depth = None
        del self.stack[depth:]

    def handle_data(self, data: str) -> None:
        if self.content_depth is not None and self.quote_depth is None:
            self.parts.append(data)


def parse_index_html(html: str, post_id: str) -> list[tuple[str, str]]:
    parser = FirstPostParser(post_id)
    parser.feed(html)
    parser.close()
    if not parser.found_post:
        raise SourceUnavailable("post_missing")
    if not parser.found_content:
        raise SourceUnavailable("post_content_missing")
    if not parser.completed_content:
        raise SourceUnavailable("post_content_incomplete")
    rows = []
    seen = set()
    for line in "".join(parser.parts).splitlines():
        match = ENTRY.fullmatch(" ".join(unicodedata.normalize("NFC", line).split()))
        if match:
            row = (normalize_name(match[1]), normalize_name(match[2]))
            if row not in seen:
                seen.add(row)
                rows.append(row)
    if not rows:
        raise SourceUnavailable("index_entries_missing")
    return rows


class VerifiedRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: PLR0913, PLR0917
        # urllib's redirect-handler callback fixes this argument list.
        if urlsplit(newurl).scheme != "https":
            raise SourceUnavailable("insecure_redirect")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch_source(url: str) -> str:
    if urlsplit(url).scheme != "https":
        raise SourceUnavailable("https_required")
    opener = build_opener(VerifiedRedirects(), HTTPSHandler(context=ssl.create_default_context()))
    request = Request(url, headers={"User-Agent": "Kinprove-Name-Lookup/1.0"})
    try:
        with opener.open(request, timeout=TIMEOUT_SECONDS) as response:
            if urlsplit(response.geturl()).scheme != "https":
                raise SourceUnavailable("https_required")
            data = response.read(MAX_BYTES + 1)
            if len(data) > MAX_BYTES:
                raise SourceUnavailable("source_too_large")
            encoding = response.headers.get_content_charset() or "utf-8"
            return data.decode(encoding)
    except SourceUnavailable:
        raise
    except (
        HTTPError,
        URLError,
        OSError,
        HTTPException,
        UnicodeError,
        LookupError,
        ValueError,
    ) as error:
        raise SourceUnavailable("fetch_failed") from error


def load_manifest(path: Path = MANIFEST) -> dict:
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
        if manifest.get("schema_version") != 1:
            raise ValueError("unsupported manifest")
        indexes = manifest["indexes"]
        for sex in ("male", "female"):
            record = indexes[sex]
            if not isinstance(record.get("post_id"), str) or not re.fullmatch(
                r"p\d+", record["post_id"]
            ):
                raise ValueError("invalid post id")
            urls = [record["url"], *record.get("fallback_urls", [])]
            if not urls or any(
                not isinstance(url, str) or urlsplit(url).scheme != "https" for url in urls
            ):
                raise ValueError("invalid source urls")
        return indexes
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        raise SourceUnavailable("manifest_invalid") from error


def find_matches(
    rows: list[tuple[str, str]], *, names: list[str] | None, key: str | None, limit: int
) -> dict | None:
    if names is not None:
        wanted = {normalize_name(name) for name in names}
        keys = {dictionary_key for name, dictionary_key in rows if name in wanted}
    else:
        wanted_key = normalize_name(key or "")
        keys = {dictionary_key for _, dictionary_key in rows if dictionary_key == wanted_key}
    if not keys:
        return None
    variant_keys = {name: set() for name, dictionary_key in rows if dictionary_key in keys}
    for name, dictionary_key in rows:
        if name in variant_keys:
            variant_keys[name].add(dictionary_key)
    variants = [
        {"name": name, "dictionary_keys": sorted(dictionary_keys)}
        for name, dictionary_keys in variant_keys.items()
    ]
    return {
        "dictionary_keys": sorted(keys),
        "variants": variants[:limit],
        "variant_count": len(variants),
        "truncated": len(variants) > limit,
    }


def run_query(  # noqa: PLR0913
    indexes: dict, *, sex: str, names: list[str] | None, key: str | None, limit: int, fetcher=None
) -> tuple[dict, int]:
    fetcher = fetch_source if fetcher is None else fetcher
    query = {
        "sex": sex,
        "limit": limit,
        **({"names": names} if names is not None else {"key": key}),
    }
    result = {"query": query, "status": "not_in_index", "results": []}
    errors = []
    for selected_sex in ("male", "female") if sex == "both" else (sex,):
        record = indexes[selected_sex]
        rows = None
        source_url = record["url"]
        error_code = "fetch_failed"
        for candidate in dict.fromkeys((record["url"], *record.get("fallback_urls", []))):
            try:
                rows = parse_index_html(fetcher(candidate), record["post_id"])
                source_url = candidate
                break
            except SourceUnavailable as error:
                error_code = str(error)
        if rows is None:
            errors.append({"sex": selected_sex, "error": error_code})
            continue
        match = find_matches(rows, names=names, key=key, limit=limit)
        if match:
            result["results"].append({"sex": selected_sex, "source_url": source_url, **match})
    if errors:
        result.update(status="source_unavailable", errors=errors)
        return result, 1
    if result["results"]:
        result["status"] = "found"
    else:
        result["scope"] = (
            "Exact normalized query absent from the selected Beider indexes; not evidence that a person or name did not exist."
        )
    return result, 0


def emit_json(result: dict) -> None:
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        emit_json({"status": "invalid_request", "error": message[:240]})
        raise SystemExit(2)


def main(argv: list[str] | None = None) -> int:
    parser = JsonArgumentParser(description=__doc__)
    parser.add_argument("--sex", choices=("male", "female", "both"), default="both")
    selectors = parser.add_mutually_exclusive_group(required=True)
    selectors.add_argument(
        "--name", action="append", help="Cyrillic form; repeat for spelling variants"
    )
    selectors.add_argument("--key", help="Latin dictionary entry key")
    parser.add_argument("--limit", type=int, default=20, help="Maximum printed variants, 1 to 50")
    args = parser.parse_args(argv)
    if not 1 <= args.limit <= MAX_LIMIT:
        parser.error("--limit must be between 1 and 50")
    values = args.name if args.name is not None else [args.key]
    if len(values) > 10 or any(not value.strip() or len(value) > 120 for value in values):
        parser.error("Use 1 to 10 nonempty queries, at most 120 characters each")
    try:
        result, exit_code = run_query(
            load_manifest(), sex=args.sex, names=args.name, key=args.key, limit=args.limit
        )
    except SourceUnavailable as error:
        emit_json({"status": "source_unavailable", "error": str(error), "results": []})
        return 1
    emit_json(result)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
