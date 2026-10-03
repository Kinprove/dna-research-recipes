"""Bounded offline lookup and bundled-data failure checks for the Beider helper."""

import copy
import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

HELPER = Path(__file__).resolve().parents[1] / "scripts/lookup_beider_name.py"
SPEC = importlib.util.spec_from_file_location("lookup_beider_name", HELPER)
lookup = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lookup)

MALE_URL = "https://forum.j-roots.info/viewtopic.php?t=2060#p32424"
FEMALE_URL = "https://forum.j-roots.info/viewtopic.php?f=98&t=2059#p32423"
MALE_ENTRIES = [
    ["ХАИМ", "KHAYEM"],
    ["ХАЙКЕЛЬ", "KHAYEM"],
    ["ГЕРШЕЛЬ", "GERSHN"],
    ["ГЕРШЕЛЬ", "HIRSH"],
    ["ЁСЕЛЬ", "YOYSEF"],
    ["ЕСЕЛЬ", "ESEL"],
    ["МЕШУЛЕМ-ЗУСЯ", "MESHULEM"],
]
FEMALE_ENTRIES = [
    ["ПЕСЯ", "BASHEVE"],
    ["БАСЯ", "BASHEVE"],
    ["ГОСЯ", "GOLDE"],
    ["ГОСЯ", "HODES"],
    ["ГОЛДА", "GOLDE"],
    ["ГОДЕС", "HODES"],
    ["ЦIПРА", "TSIPOYRE"],
    ["ЦIСЦА", "TSIPOYRE"],
]


def fixture_manifest():
    return {
        "schema_version": 2,
        "snapshot_date": "2026-10-03",
        "indexes": {
            sex: {
                "title": title,
                "url": url,
                "post_id": post_id,
                "content_sha256": "a" * 64,
                "entry_count": len(entries),
                "entries": copy.deepcopy(entries),
            }
            for sex, title, url, post_id, entries in (
                ("male", "Male index", MALE_URL, "p32424", MALE_ENTRIES),
                ("female", "Female index", FEMALE_URL, "p32423", FEMALE_ENTRIES),
            )
        },
    }


class BeiderLookupTests(unittest.TestCase):
    def query(self, names=None, key=None, limit=20, sex="both", indexes=None):
        return lookup.run_query(
            fixture_manifest()["indexes"] if indexes is None else indexes,
            names=names,
            key=key,
            limit=limit,
            sex=sex,
        )

    def cli(self, arguments, indexes=None):
        output = io.StringIO()
        with (
            patch.object(
                lookup,
                "load_manifest",
                return_value=fixture_manifest()["indexes"] if indexes is None else indexes,
            ),
            redirect_stdout(output),
        ):
            code = lookup.main(arguments)
        return json.loads(output.getvalue()), code

    def assert_manifest_rejected(self, manifest):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "indexes.json"
            path.write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
            with self.assertRaisesRegex(lookup.SourceUnavailable, "manifest_invalid"):
                lookup.load_manifest(path)

    def test_name_finds_all_forms_in_article(self):
        result, code = self.query(names=["хаим"])
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "found")
        self.assertEqual(result["results"][0]["dictionary_keys"], ["KHAYEM"])
        self.assertEqual(
            result["results"][0]["variants"],
            [
                {"name": "ХАИМ", "dictionary_keys": ["KHAYEM"]},
                {"name": "ХАЙКЕЛЬ", "dictionary_keys": ["KHAYEM"]},
            ],
        )

    def test_selected_sex_excludes_other_index(self):
        result, code = self.query(names=["ПЕСЯ"], sex="male")
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "not_in_index")
        result, code = self.query(names=["ПЕСЯ"], sex="female")
        self.assertEqual(code, 0)
        self.assertEqual(result["results"][0]["sex"], "female")

    def test_ambiguous_spelling_retains_both_keys(self):
        result, _ = self.query(names=["ГЕРШЕЛЬ"])
        self.assertEqual(result["results"][0]["dictionary_keys"], ["GERSHN", "HIRSH"])
        result, _ = self.query(names=["ГОСЯ"])
        self.assertEqual(result["results"][0]["dictionary_keys"], ["GOLDE", "HODES"])
        self.assertEqual(
            result["results"][0]["variants"],
            [
                {"name": "ГОСЯ", "dictionary_keys": ["GOLDE", "HODES"]},
                {"name": "ГОЛДА", "dictionary_keys": ["GOLDE"]},
                {"name": "ГОДЕС", "dictionary_keys": ["HODES"]},
            ],
        )

    def test_same_dictionary_key_finds_variants(self):
        result, _ = self.query(key="basheve")
        self.assertEqual(
            result["results"][0]["variants"],
            [
                {"name": "ПЕСЯ", "dictionary_keys": ["BASHEVE"]},
                {"name": "БАСЯ", "dictionary_keys": ["BASHEVE"]},
            ],
        )
        self.assertEqual(result["results"][0]["source_url"], FEMALE_URL)

    def test_cli_name_retains_all_memberships_without_expanding_other_articles(self):
        result, code = self.cli(["--sex", "female", "--name", "ГОЛДА"])
        self.assertEqual(code, 0)
        match = result["results"][0]
        self.assertEqual(match["dictionary_keys"], ["GOLDE"])
        self.assertEqual(
            match["variants"],
            [
                {"name": "ГОСЯ", "dictionary_keys": ["GOLDE", "HODES"]},
                {"name": "ГОЛДА", "dictionary_keys": ["GOLDE"]},
            ],
        )
        self.assertEqual(match["variant_count"], 2)
        self.assertFalse(match["truncated"])

    def test_cli_key_retains_all_memberships_and_output_limit(self):
        result, code = self.cli(["--sex", "female", "--key", "GOLDE", "--limit", "1"])
        self.assertEqual(code, 0)
        match = result["results"][0]
        self.assertEqual(match["dictionary_keys"], ["GOLDE"])
        self.assertEqual(
            match["variants"], [{"name": "ГОСЯ", "dictionary_keys": ["GOLDE", "HODES"]}]
        )
        self.assertEqual(match["variant_count"], 2)
        self.assertTrue(match["truncated"])

    def test_limit_preserves_total_variant_count(self):
        result, _ = self.query(key="KHAYEM", limit=1)
        match = result["results"][0]
        self.assertEqual(match["variants"], [{"name": "ХАИМ", "dictionary_keys": ["KHAYEM"]}])
        self.assertEqual(match["variant_count"], 2)
        self.assertTrue(match["truncated"])

    def test_large_group_is_bounded_without_losing_total(self):
        indexes = fixture_manifest()["indexes"]
        indexes["male"]["entries"] = [["ИМЯ" + "А" * i, "GROUP"] for i in range(1, 61)]
        for limit in (20, 50):
            with self.subTest(limit=limit):
                result, code = self.query(key="GROUP", sex="male", limit=limit, indexes=indexes)
                self.assertEqual(code, 0)
                match = result["results"][0]
                self.assertEqual(len(match["variants"]), limit)
                self.assertEqual(match["variant_count"], 60)
                self.assertTrue(match["truncated"])

    def test_unicode_case_whitespace_hyphens_but_not_yo(self):
        result, _ = self.query(names=["  мешулем — зуся "])
        self.assertEqual(result["results"][0]["dictionary_keys"], ["MESHULEM"])
        result, _ = self.query(names=["ёсёль"])
        self.assertEqual(result["status"], "not_in_index")
        result, _ = self.query(names=["Есель"])
        self.assertEqual(result["results"][0]["dictionary_keys"], ["ESEL"])
        result, _ = self.query(names=["е\u0308сель"])
        self.assertEqual(result["results"][0]["dictionary_keys"], ["YOYSEF"])

    def test_repeated_names_union_keys_without_duplicate_variants(self):
        result, _ = self.query(names=["хаим", "ХАЙКЕЛЬ"])
        self.assertEqual(
            result["results"][0]["variants"],
            [
                {"name": "ХАИМ", "dictionary_keys": ["KHAYEM"]},
                {"name": "ХАЙКЕЛЬ", "dictionary_keys": ["KHAYEM"]},
            ],
        )

    def test_mixed_latin_i_is_preserved(self):
        result, _ = self.query(names=["ЦIПРА"], sex="female")
        self.assertEqual(result["results"][0]["dictionary_keys"], ["TSIPOYRE"])
        self.assertEqual(result["results"][0]["variant_count"], 2)
        result, _ = self.query(names=["ЦІПРА"], sex="female")
        self.assertEqual(result["status"], "not_in_index")

    def test_unknown_query_has_bundled_index_scope(self):
        result, code = self.query(names=["НЕИЗВЕСТНЫЙ"])
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "not_in_index")
        self.assertIn("bundled", result["scope"])
        self.assertIn("not evidence", result["scope"])

    def test_loader_normalizes_every_pair_without_losing_memberships(self):
        manifest = fixture_manifest()
        manifest["indexes"]["male"]["entries"][0] = ["  хаим ", " khayem "]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "indexes.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            indexes = lookup.load_manifest(path)
        result, code = self.query(names=["ГЕРШЕЛЬ"], indexes=indexes)
        self.assertEqual(code, 0)
        self.assertEqual(result["results"][0]["dictionary_keys"], ["GERSHN", "HIRSH"])
        self.assertEqual(indexes["male"]["entries"][0], ("ХАИМ", "KHAYEM"))
        self.assertIn(("ЁСЕЛЬ", "YOYSEF"), indexes["male"]["entries"])
        self.assertIn(("ЦIПРА", "TSIPOYRE"), indexes["female"]["entries"])

    def test_malformed_entry_is_rejected_instead_of_dropped(self):
        for entry in (
            [],
            ["ХАИМ"],
            ["ХАИМ", "KHAYEM", "extra"],
            {"name": "ХАИМ", "key": "KHAYEM"},
            [None, "KHAYEM"],
            ["ХАИМ", 1],
            [" ", "KHAYEM"],
            ["ХАИМ", ""],
            ["ХАИМ\n", "KHAYEM"],
            ["ХАИМ", "123"],
        ):
            with self.subTest(entry=entry):
                manifest = fixture_manifest()
                manifest["indexes"]["female"]["entries"].append(entry)
                manifest["indexes"]["female"]["entry_count"] += 1
                self.assert_manifest_rejected(manifest)

    def test_duplicate_normalized_pair_is_rejected_but_shared_names_are_valid(self):
        manifest = fixture_manifest()
        manifest["indexes"]["male"]["entries"].append([" хаим ", "khayem"])
        manifest["indexes"]["male"]["entry_count"] += 1
        self.assert_manifest_rejected(manifest)

    def test_empty_or_incomplete_index_is_unavailable(self):
        for entries, count in (([], 0), (None, 1), (MALE_ENTRIES, 6), (MALE_ENTRIES, True)):
            with self.subTest(entries=entries, count=count):
                manifest = fixture_manifest()
                manifest["indexes"]["male"]["entries"] = entries
                manifest["indexes"]["male"]["entry_count"] = count
                self.assert_manifest_rejected(manifest)

    def test_invalid_schema_date_or_missing_index_is_unavailable(self):
        invalid = (
            ("schema_version", 1),
            ("schema_version", 2.0),
            ("schema_version", None),
            ("snapshot_date", "2026-02-30"),
            ("snapshot_date", "20261003"),
            ("indexes", {"male": fixture_manifest()["indexes"]["male"]}),
            ("indexes", []),
        )
        for field, value in invalid:
            with self.subTest(field=field, value=value):
                manifest = fixture_manifest()
                manifest[field] = value
                self.assert_manifest_rejected(manifest)
        self.assert_manifest_rejected([])

    def test_invalid_source_metadata_is_unavailable(self):
        for field, value in (
            ("title", ""),
            ("url", "http://example.test"),
            ("post_id", "invalid"),
            ("content_sha256", "incomplete"),
        ):
            with self.subTest(field=field):
                manifest = fixture_manifest()
                manifest["indexes"]["male"][field] = value
                self.assert_manifest_rejected(manifest)

    def test_missing_or_corrupt_file_is_unavailable(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "indexes.json"
            with self.assertRaisesRegex(lookup.SourceUnavailable, "manifest_invalid"):
                lookup.load_manifest(path)
            for content in (b'{"schema_version":', b"\xff"):
                path.write_bytes(content)
                with self.assertRaisesRegex(lookup.SourceUnavailable, "manifest_invalid"):
                    lookup.load_manifest(path)

    def test_cli_bad_data_is_not_a_negative_even_for_valid_other_index(self):
        manifest = fixture_manifest()
        manifest["indexes"]["female"]["entries"].append(["BROKEN"])
        manifest["indexes"]["female"]["entry_count"] += 1
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "indexes.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            output = io.StringIO()
            with patch.object(lookup, "MANIFEST", path), redirect_stdout(output):
                code = lookup.main(["--sex", "male", "--name", "ХАИМ"])
        result = json.loads(output.getvalue())
        self.assertEqual(code, 1)
        self.assertEqual(result["status"], "source_unavailable")
        self.assertEqual(result["results"], [])
        self.assertEqual(result["error"], "manifest_invalid")

    def test_cli_rejects_invalid_limits_in_json(self):
        for limit in ("0", "51"):
            with self.subTest(limit=limit):
                output = io.StringIO()
                with redirect_stdout(output), self.assertRaises(SystemExit) as error:
                    lookup.main(["--name", "ХАИМ", "--limit", limit])
                self.assertEqual(error.exception.code, 2)
                self.assertEqual(json.loads(output.getvalue())["status"], "invalid_request")

    def test_cli_emits_only_requested_variants(self):
        result, code = self.cli(["--name", "ХАИМ"])
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "found")
        self.assertEqual(len(result["results"]), 1)
        self.assertEqual(result["results"][0]["variant_count"], 2)
        self.assertNotIn("ГЕРШЕЛЬ", json.dumps(result))

    def test_actual_bundled_cli_works_from_another_directory(self):
        cases = (
            (["--sex", "male", "--name", "Гершель"], {"GERSHN", "HIRSH"}),
            (["--sex", "female", "--name", "Гося"], {"GOLDE", "HODES"}),
            (["--sex", "female", "--key", "BASHEVE"], {"BASHEVE"}),
        )
        with tempfile.TemporaryDirectory() as directory:
            for arguments, keys in cases:
                with self.subTest(arguments=arguments):
                    completed = subprocess.run(
                        [sys.executable, "-B", str(HELPER), *arguments],
                        cwd=directory,
                        capture_output=True,
                        text=True,
                        check=False,
                        timeout=10,
                    )
                    self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
                    result = json.loads(completed.stdout)
                    self.assertEqual(result["status"], "found")
                    self.assertEqual(set(result["results"][0]["dictionary_keys"]), keys)
                    self.assertEqual(completed.stderr, "")


if __name__ == "__main__":
    unittest.main()
