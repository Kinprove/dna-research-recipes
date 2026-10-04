#!/usr/bin/env python3
"""Find bounded Beider article candidates, then retrieve a selected article's variants."""

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
CONSONANTS = str.maketrans("БВГДЖЗ", "ПФКТШС")
MATCH_ORDER = {"exact": 0, "separator_normalized": 1, "fuzzy": 2}


class SourceUnavailable(Exception):
    """Bundled data cannot support either a positive or a negative lookup."""


def normalize_name(value: str) -> str:
    """Match case, spacing and hyphens, retaining the distinction between ё and е."""
    value = unicodedata.normalize("NFC", value).translate(DASHES).upper()
    value = " ".join(value.split())
    return re.sub(r"\s*-\s*", "-", value)


def comparison_key(value: str) -> str:
    """Ignore separators for search without altering archived spellings or validation."""
    return re.sub(r"[-\s]", "", normalize_name(value))


def consonant_signature(value: str) -> str | None:
    """Coarse Cyrillic ranking signal, never a synonym or candidate-admission rule."""
    if not re.fullmatch(r"[А-ЯЁ]+", value):
        return None
    value = re.sub(r"[АЕЁИОУЫЭЮЯЬЪ]", "", value).translate(CONSONANTS)
    return re.sub(r"(.)\1+", r"\1", value) or None


def max_edits(value: str) -> int:
    return 0 if len(value) <= 2 else 1 if len(value) <= 4 else 2


def damerau_levenshtein(left: str, right: str) -> int:
    """Unrestricted edit distance; characters may participate in multiple edits."""
    if left == right:
        return 0
    sentinel = len(left) + len(right)
    distances = [[0] * (len(right) + 2) for _ in range(len(left) + 2)]
    distances[0][0] = sentinel
    for i in range(len(left) + 1):
        distances[i + 1][0] = sentinel
        distances[i + 1][1] = i
    for j in range(len(right) + 1):
        distances[0][j + 1] = sentinel
        distances[1][j + 1] = j
    last_row = {}
    for i, left_char in enumerate(left, 1):
        last_column = 0
        for j, right_char in enumerate(right, 1):
            previous_row = last_row.get(right_char, 0)
            previous_column = last_column
            cost = int(left_char != right_char)
            if cost == 0:
                last_column = j
            distances[i + 1][j + 1] = min(
                distances[i][j] + cost,
                distances[i + 1][j] + 1,
                distances[i][j + 1] + 1,
                distances[previous_row][previous_column]
                + (i - previous_row - 1)
                + 1
                + (j - previous_column - 1),
            )
        last_row[left_char] = i
    return distances[-1][-1]


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


def find_variants(rows: list[tuple[str, str]], *, key: str, limit: int) -> dict | None:
    wanted_key = normalize_name(key)
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


def match_rank(match: dict) -> tuple:
    return (
        MATCH_ORDER[match["match_type"]],
        match["edit_distance"],
        not match["phonetic_equal"],
        match["matched_name"],
    )


def search_candidates(indexes: dict, *, sex: str, names: list[str], limit: int) -> dict:
    """Return article groups, retaining each input's best source spelling per article."""
    groups = []
    for selected_sex in ("male", "female") if sex == "both" else (sex,):
        record = indexes[selected_sex]
        memberships = {}
        articles = {}
        for name, dictionary_key in record["entries"]:
            memberships.setdefault(name, set()).add(dictionary_key)
            articles.setdefault(dictionary_key, set()).add(name)
        best = {}
        for query in dict.fromkeys(names):
            normalized = normalize_name(query)
            compact = comparison_key(query)
            threshold = max_edits(compact)
            signature = consonant_signature(compact)
            for name, dictionary_keys in memberships.items():
                indexed_compact = comparison_key(name)
                if abs(len(compact) - len(indexed_compact)) > threshold:
                    continue
                distance = damerau_levenshtein(compact, indexed_compact)
                if distance > threshold:
                    continue
                match = {
                    "query": query,
                    "matched_name": name,
                    "dictionary_keys": sorted(dictionary_keys),
                    "match_type": (
                        "exact"
                        if normalized == name
                        else "separator_normalized"
                        if compact == indexed_compact
                        else "fuzzy"
                    ),
                    "edit_distance": distance,
                    "phonetic_equal": (
                        signature is not None and signature == consonant_signature(indexed_compact)
                    ),
                }
                for dictionary_key in dictionary_keys:
                    matches = best.setdefault(dictionary_key, {})
                    previous = matches.get(query)
                    if previous is None or match_rank(match) < match_rank(previous):
                        matches[query] = match
        for dictionary_key, matches in best.items():
            groups.append(
                {
                    "sex": selected_sex,
                    "source_url": record["url"],
                    "dictionary_key": dictionary_key,
                    "matches": list(matches.values()),
                    "variant_count": len(articles[dictionary_key]),
                }
            )
    groups.sort(
        key=lambda group: (
            min(match_rank(match)[:3] for match in group["matches"]),
            group["sex"],
            group["dictionary_key"],
        )
    )
    return {
        "results": groups[:limit],
        "candidate_count": len(groups),
        "truncated": len(groups) > limit,
    }


def component_queries(names: list[str]) -> list[dict]:
    queries = []
    for query in dict.fromkeys(names):
        parts = [part for part in re.split(r"[-\s]+", query.translate(DASHES).strip()) if part]
        if len(parts) > 1:
            seen = set()
            for position, part in enumerate(parts, 1):
                compact = comparison_key(part)
                if compact not in seen:
                    queries.append({"name": part, "parent_query": query, "position": position})
                    seen.add(compact)
    return queries


def run_query(
    indexes: dict, *, sex: str, names: list[str] | None, key: str | None, limit: int
) -> tuple[dict, int]:
    query = {
        "sex": sex,
        "limit": limit,
        **({"names": names} if names is not None else {"key": key}),
    }
    result = {"query": query, "status": "not_in_index", "results": []}
    if names is not None:
        query["matching_policy"] = {
            "comparison": "NFC uppercase, ignoring whitespace and hyphens/dashes",
            "distance": "unrestricted Damerau-Levenshtein",
            "max_edits_by_length": {"1-2": 0, "3-4": 1, "5+": 2},
            "phonetics": "Cyrillic consonant signature, ranking ties only",
            "limit_unit": "article groups across selected sexes and inputs, per bucket",
        }
        result.update(search_candidates(indexes, sex=sex, names=names, limit=limit))
        if result["results"]:
            result["status"] = (
                "found"
                if any(
                    match["match_type"] != "fuzzy"
                    for group in result["results"]
                    for match in group["matches"]
                )
                else "candidates_found"
            )
        components = component_queries(names)
        if components:
            result["component_search"] = {
                "queries": components,
                **search_candidates(
                    indexes, sex=sex, names=[part["name"] for part in components], limit=limit
                ),
            }
        result["scope"] = (
            "Article candidates are search leads, not source-backed synonyms of the input or identity evidence. "
            "No admitted whole-name candidate means absent under this policy in the bundled index; "
            "not evidence that a person or name did not exist. Components are separate searches."
        )
        return result, 0
    for selected_sex in ("male", "female") if sex == "both" else (sex,):
        record = indexes[selected_sex]
        match = find_variants(record["entries"], key=key or "", limit=limit)
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
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Maximum article groups per name-search bucket or variants for --key, 1 to 50",
    )
    args = parser.parse_args(argv)
    if not 1 <= args.limit <= MAX_LIMIT:
        parser.error("--limit must be between 1 and 50")
    values = args.name if args.name is not None else [args.key]
    if len(values) > 10 or any(not comparison_key(value) or len(value) > 120 for value in values):
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
