#!/usr/bin/env python3
"""Look up bounded Beider name variants from the indexes bundled with this skill."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

MANIFEST = Path(__file__).resolve().parents[1] / "resources" / "beider-name-indexes.json"
MAX_LIMIT = 50
DASHES = str.maketrans({char: "-" for char in "‐‑‒–—−"})


class SourceUnavailable(Exception):
    """Bundled data cannot support either a positive or a negative lookup."""


def normalize_name(value: str) -> str:
    """Match case, spacing and hyphens, retaining the distinction between ё and е."""
    value = unicodedata.normalize("NFC", value).translate(DASHES).upper()
    value = " ".join(value.split())
    return re.sub(r"\s*-\s*", "-", value)


def validate_entries(entries: list, entry_count: int) -> list[tuple[str, str]]:
    """Reject incomplete or malformed indexes instead of silently dropping rows."""
    if not isinstance(entries, list) or not entries:
        raise ValueError("index entries must be a nonempty list")
    if type(entry_count) is not int or entry_count != len(entries):
        raise ValueError("index entry count mismatch")
    rows = []
    seen = set()
    for entry in entries:
        if not isinstance(entry, list) or len(entry) != 2:
            raise ValueError("index entry must be a name/key pair")
        if any(not isinstance(value, str) or not value.strip() for value in entry):
            raise ValueError("index entry values must be nonempty strings")
        if any(any(unicodedata.category(char) == "Cc" for char in value) for value in entry):
            raise ValueError("index entry contains control characters")
        row = tuple(normalize_name(value) for value in entry)
        if not re.fullmatch(r"[A-Z][A-Z' -]*", row[1]):
            raise ValueError("invalid dictionary article key")
        if row in seen:
            raise ValueError("duplicate normalized name/key pair")
        seen.add(row)
        rows.append(row)
    return rows


def validate_index(record: dict) -> dict:
    """Validate local entries and keep source metadata for attribution only."""
    if not isinstance(record["title"], str) or not record["title"].strip():
        raise ValueError("invalid index title")
    if not isinstance(record["post_id"], str) or not re.fullmatch(r"p\d+", record["post_id"]):
        raise ValueError("invalid post id")
    if not isinstance(record["url"], str) or not record["url"].startswith("https://"):
        raise ValueError("invalid source url")
    digest = record["content_sha256"]
    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise ValueError("invalid source content hash")
    rows = validate_entries(record["entries"], record["entry_count"])
    return {**record, "entries": rows}


def load_manifest(path: Path | None = None) -> dict:
    try:
        manifest = json.loads((MANIFEST if path is None else path).read_text(encoding="utf-8"))
        if type(manifest["schema_version"]) is not int or manifest["schema_version"] != 2:
            raise ValueError("unsupported manifest")
        snapshot_date = manifest["snapshot_date"]
        if not isinstance(snapshot_date, str) or not re.fullmatch(
            r"\d{4}-\d{2}-\d{2}", snapshot_date
        ):
            raise ValueError("invalid snapshot date")
        date.fromisoformat(snapshot_date)
        indexes = manifest["indexes"]
        if not isinstance(indexes, dict) or set(indexes) != {"male", "female"}:
            raise ValueError("both indexes are required")
        return {sex: validate_index(indexes[sex]) for sex in ("male", "female")}
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


def run_query(
    indexes: dict, *, sex: str, names: list[str] | None, key: str | None, limit: int
) -> tuple[dict, int]:
    query = {
        "sex": sex,
        "limit": limit,
        **({"names": names} if names is not None else {"key": key}),
    }
    result = {"query": query, "status": "not_in_index", "results": []}
    for selected_sex in ("male", "female") if sex == "both" else (sex,):
        record = indexes[selected_sex]
        match = find_matches(record["entries"], names=names, key=key, limit=limit)
        if match:
            result["results"].append({"sex": selected_sex, "source_url": record["url"], **match})
    if result["results"]:
        result["status"] = "found"
    else:
        result["scope"] = (
            "Exact normalized query absent from the bundled Beider indexes; not evidence that a person or name did not exist."
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
