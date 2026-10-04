"""Bounded offline article candidates, variant lookup and bundled-data failures."""

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
    def indexes(self, *, male=None, female=None):
        indexes = fixture_manifest()["indexes"]
        for sex, entries in (("male", male), ("female", female)):
            if entries is not None:
                indexes[sex]["entries"] = entries
                indexes[sex]["entry_count"] = len(entries)
        return indexes

    def article(self, result, key, sex="male"):
        matches = [
            group
            for group in result["results"]
            if (group["sex"], group["dictionary_key"]) == (sex, key)
        ]
        self.assertEqual(len(matches), 1, result)
        return matches[0]

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

    def test_name_returns_article_without_preloading_variants(self):
        result, code = self.query(names=["хаим"])
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "found")
        article = self.article(result, "KHAYEM")
        self.assertEqual(
            article["matches"],
            [
                {
                    "query": "хаим",
                    "matched_name": "ХАИМ",
                    "dictionary_keys": ["KHAYEM"],
                    "match_type": "exact",
                    "edit_distance": 0,
                    "phonetic_equal": True,
                }
            ],
        )
        self.assertEqual(article["variant_count"], 2)
        self.assertEqual(article["source_url"], MALE_URL)
        self.assertNotIn("variants", article)
        self.assertEqual(result["candidate_count"], 1)
        self.assertFalse(result["truncated"])
        self.assertIn("not source-backed synonyms", result["scope"])
        self.assertIn("not evidence", result["scope"])

    def test_selected_sex_excludes_other_index(self):
        result, code = self.query(names=["ПЕСЯ"], sex="male")
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "not_in_index")
        result, code = self.query(names=["ПЕСЯ"], sex="female")
        self.assertEqual(code, 0)
        self.assertEqual(self.article(result, "BASHEVE", "female")["sex"], "female")

    def test_ambiguous_spelling_retains_both_keys(self):
        result, _ = self.query(names=["ГЕРШЕЛЬ"])
        for key in ("GERSHN", "HIRSH"):
            match = self.article(result, key)["matches"][0]
            self.assertEqual(match["dictionary_keys"], ["GERSHN", "HIRSH"])
            self.assertEqual(match["match_type"], "exact")
        result, _ = self.query(names=["ГОСЯ"])
        for key in ("GOLDE", "HODES"):
            article = self.article(result, key, "female")
            self.assertEqual(article["matches"][0]["dictionary_keys"], ["GOLDE", "HODES"])
            self.assertEqual(article["variant_count"], 2)

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

    def test_cli_name_retains_memberships_on_fuzzy_article_candidates(self):
        result, code = self.cli(["--sex", "female", "--name", "ГОСА"])
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "candidates_found")
        for key in ("GOLDE", "HODES"):
            article = self.article(result, key, "female")
            match = article["matches"][0]
            self.assertEqual(match["matched_name"], "ГОСЯ")
            self.assertEqual(match["dictionary_keys"], ["GOLDE", "HODES"])
            self.assertEqual(match["match_type"], "fuzzy")
            self.assertEqual(match["edit_distance"], 1)
            self.assertNotIn("variants", article)

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
        match = self.article(result, "MESHULEM")["matches"][0]
        self.assertEqual(match["matched_name"], "МЕШУЛЕМ-ЗУСЯ")
        self.assertEqual(match["match_type"], "exact")
        result, _ = self.query(names=["ёсёль"])
        self.assertEqual(result["status"], "candidates_found")
        self.assertTrue(
            all(
                match["match_type"] == "fuzzy"
                for group in result["results"]
                for match in group["matches"]
            )
        )
        result, _ = self.query(names=["Есель"])
        self.assertEqual(self.article(result, "ESEL")["matches"][0]["match_type"], "exact")
        self.assertEqual(self.article(result, "YOYSEF")["matches"][0]["match_type"], "fuzzy")
        result, _ = self.query(names=["е\u0308сель"])
        self.assertEqual(self.article(result, "YOYSEF")["matches"][0]["match_type"], "exact")
        self.assertEqual(self.article(result, "ESEL")["matches"][0]["match_type"], "fuzzy")

    def test_repeated_raw_query_is_deduplicated_but_distinct_inputs_are_retained(self):
        names = ["хаим", "ХАЙКЕЛЬ", "хаим", "ХАИМ"]
        result, _ = self.query(names=names)
        article = self.article(result, "KHAYEM")
        self.assertEqual(result["query"]["names"], names)
        self.assertEqual([match["query"] for match in article["matches"]], names[:2] + names[3:])
        self.assertEqual(
            [match["matched_name"] for match in article["matches"]], ["ХАИМ", "ХАЙКЕЛЬ", "ХАИМ"]
        )
        self.assertEqual(result["candidate_count"], 1)

    def test_mixed_latin_i_is_preserved(self):
        result, _ = self.query(names=["ЦIПРА"], sex="female")
        article = self.article(result, "TSIPOYRE", "female")
        self.assertEqual(article["matches"][0]["matched_name"], "ЦIПРА")
        self.assertEqual(article["matches"][0]["match_type"], "exact")
        self.assertFalse(article["matches"][0]["phonetic_equal"])
        self.assertEqual(article["variant_count"], 2)
        result, _ = self.query(names=["ЦІПРА"], sex="female")
        match = self.article(result, "TSIPOYRE", "female")["matches"][0]
        self.assertEqual(result["status"], "candidates_found")
        self.assertEqual(match["match_type"], "fuzzy")
        self.assertEqual(match["edit_distance"], 1)
        self.assertFalse(match["phonetic_equal"])

    def test_unknown_query_has_bundled_index_scope(self):
        result, code = self.query(names=["НЕИЗВЕСТНЫЙ"])
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "not_in_index")
        self.assertIn("bundled", result["scope"])
        self.assertIn("not evidence", result["scope"])
        self.assertEqual(result["candidate_count"], 0)
        self.assertFalse(result["truncated"])
        self.assertEqual(
            result["query"]["matching_policy"]["max_edits_by_length"], {"1-2": 0, "3-4": 1, "5+": 2}
        )

    def test_exact_match_does_not_suppress_fuzzy_competing_articles(self):
        indexes = self.indexes(male=[["ДОВИД", "DOVID"], ["ДОВИДКА", "OTHER"]])
        result, _ = self.query(names=["Довид"], sex="male", indexes=indexes)
        self.assertEqual(result["status"], "found")
        self.assertEqual(
            [group["dictionary_key"] for group in result["results"]], ["DOVID", "OTHER"]
        )
        self.assertEqual(self.article(result, "DOVID")["matches"][0]["match_type"], "exact")
        fuzzy = self.article(result, "OTHER")["matches"][0]
        self.assertEqual(fuzzy["match_type"], "fuzzy")
        self.assertEqual(fuzzy["edit_distance"], 2)

    def test_group_uses_best_indexed_match_per_raw_input(self):
        indexes = self.indexes(male=[["ДАВИД", "DOVID"], ["ДОВИД", "DOVID"], ["ДОВ", "DOV"]])
        names = [" Довыд ", "Дови"]
        result, _ = self.query(names=names, sex="male", indexes=indexes)
        article = self.article(result, "DOVID")
        self.assertEqual([match["query"] for match in article["matches"]], names)
        self.assertEqual(
            [match["matched_name"] for match in article["matches"]], ["ДОВИД", "ДОВИД"]
        )
        self.assertEqual([match["edit_distance"] for match in article["matches"]], [1, 1])
        self.assertEqual(article["variant_count"], 2)
        dov_matches = self.article(result, "DOV")["matches"]
        self.assertEqual([match["query"] for match in dov_matches], names)
        self.assertEqual([match["edit_distance"] for match in dov_matches], [2, 1])

    def test_group_limit_is_global_across_sexes_and_inputs(self):
        entries = [["ХАИМ", "ARTICLE" + chr(65 + i // 26) + chr(65 + i % 26)] for i in range(30)]
        indexes = self.indexes(male=entries, female=entries)
        for limit in (20, 50):
            with self.subTest(limit=limit):
                result, code = self.query(names=["ХАИМ", "хаим"], limit=limit, indexes=indexes)
                self.assertEqual(code, 0)
                self.assertEqual(len(result["results"]), limit)
                self.assertEqual(
                    len({(group["sex"], group["dictionary_key"]) for group in result["results"]}),
                    limit,
                )
                self.assertEqual(result["candidate_count"], 60)
                self.assertTrue(result["truncated"])
                self.assertTrue(all(len(group["matches"]) == 2 for group in result["results"]))

    def test_adjacent_transposition_counts_as_one_edit(self):
        indexes = self.indexes(male=[["ДОВИД", "DOVID"]])
        result, _ = self.query(names=["ДОИВД"], sex="male", indexes=indexes)
        match = self.article(result, "DOVID")["matches"][0]
        self.assertEqual(match["edit_distance"], 1)
        self.assertEqual(match["match_type"], "fuzzy")

    def test_unrestricted_distance_allows_transposition_and_insertion_in_same_substring(self):
        indexes = self.indexes(male=[["МЕШАБК", "UNRESTRICTED"]])
        result, _ = self.query(names=["МЕШКА"], sex="male", indexes=indexes)
        self.assertEqual(result["status"], "candidates_found")
        self.assertEqual(self.article(result, "UNRESTRICTED")["matches"][0]["edit_distance"], 2)

    def test_short_queries_admit_only_exact_compact_spellings(self):
        indexes = self.indexes(
            male=[["Д", "ONE"], ["ДО", "TWO"], ["ДА", "NEAR"], ["ДОВ", "LONGER"]]
        )
        for query, key in (("Д", "ONE"), ("ДО", "TWO")):
            with self.subTest(query=query):
                result, _ = self.query(names=[query], sex="male", indexes=indexes)
                self.assertEqual([group["dictionary_key"] for group in result["results"]], [key])

    def test_edit_thresholds_reject_noise_beyond_length_policy(self):
        for query, near, far, distance in (
            ("ДОВ", "ДОБ", "ДАЗ", 1),
            ("ДОВИ", "ДОВ", "ДАВА", 1),
            ("ДОВИД", "ДАВИТ", "БАШАН", 2),
        ):
            with self.subTest(query=query):
                indexes = self.indexes(male=[[near, "NEAR"], [far, "FAR"]])
                result, _ = self.query(names=[query], sex="male", indexes=indexes)
                self.assertEqual([group["dictionary_key"] for group in result["results"]], ["NEAR"])
                self.assertEqual(
                    self.article(result, "NEAR")["matches"][0]["edit_distance"], distance
                )

    def test_phonetic_signature_ranks_ties_without_admitting_distant_names(self):
        indexes = self.indexes(
            male=[["БАШЯ", "OTHER"], ["ПАСЯ", "VOICE"], ["БААААААААСЯ", "OUTSIDE"]]
        )
        result, _ = self.query(names=["БАСЯ"], sex="male", indexes=indexes)
        self.assertEqual(
            [group["dictionary_key"] for group in result["results"]], ["VOICE", "OTHER"]
        )
        self.assertTrue(self.article(result, "VOICE")["matches"][0]["phonetic_equal"])
        self.assertFalse(self.article(result, "OTHER")["matches"][0]["phonetic_equal"])
        self.assertTrue(
            all(group["matches"][0]["edit_distance"] == 1 for group in result["results"])
        )

    def test_empty_consonant_signature_never_claims_phonetic_agreement(self):
        indexes = self.indexes(male=[["ААА", "VOWELS"]])
        result, _ = self.query(names=["ААЕ"], sex="male", indexes=indexes)
        self.assertFalse(self.article(result, "VOWELS")["matches"][0]["phonetic_equal"])

    def test_tie_order_does_not_depend_on_source_row_order(self):
        entries = [["ХАЙМ", "ZETA"], ["ХАИН", "ALPHA"]]
        first, _ = self.query(names=["ХАИМ"], sex="male", indexes=self.indexes(male=entries))
        second, _ = self.query(
            names=["ХАИМ"], sex="male", indexes=self.indexes(male=list(reversed(entries)))
        )
        self.assertEqual(first, second)
        self.assertEqual([group["dictionary_key"] for group in first["results"]], ["ALPHA", "ZETA"])

    def test_separator_matching_preserves_indexed_spelling_and_raw_input(self):
        for name in ("МЕШУЛЕМ-ЗУСЯ", "МЕШУЛЕМ ЗУСЯ"):
            with self.subTest(indexed_name=name):
                query = "МешулемЗуся"
                result, _ = self.query(
                    names=[query], sex="male", indexes=self.indexes(male=[[name, "MESHULEM"]])
                )
                match = self.article(result, "MESHULEM")["matches"][0]
                self.assertEqual(result["status"], "found")
                self.assertEqual(match["query"], query)
                self.assertEqual(match["matched_name"], name)
                self.assertEqual(match["match_type"], "separator_normalized")
                self.assertEqual(match["edit_distance"], 0)

    def test_exact_separator_and_fuzzy_groups_rank_in_that_order(self):
        indexes = self.indexes(male=[["ХАЙ-М", "SEP"], ["ХАЙМ", "EXACT"], ["ХАИМ", "FUZZY"]])
        result, _ = self.query(names=["ХАЙМ"], sex="male", indexes=indexes)
        self.assertEqual(
            [group["dictionary_key"] for group in result["results"]], ["EXACT", "SEP", "FUZZY"]
        )
        self.assertEqual(
            [group["matches"][0]["match_type"] for group in result["results"]],
            ["exact", "separator_normalized", "fuzzy"],
        )

    def test_component_matches_stay_separate_and_do_not_change_whole_name_status(self):
        query = " Хаим — Песя "
        result, _ = self.query(names=[query])
        self.assertEqual(result["status"], "not_in_index")
        self.assertEqual(result["results"], [])
        self.assertEqual(result["candidate_count"], 0)
        components = result["component_search"]
        self.assertEqual(
            components["queries"],
            [
                {"name": "Хаим", "parent_query": query, "position": 1},
                {"name": "Песя", "parent_query": query, "position": 2},
            ],
        )
        self.assertEqual(self.article(components, "KHAYEM")["matches"][0]["query"], "Хаим")
        self.assertEqual(
            self.article(components, "BASHEVE", "female")["matches"][0]["query"], "Песя"
        )

    def test_component_queries_are_distinct_with_original_parent_positions(self):
        query = "ХАИМ-ХАИМ ПЕСЯ"
        result, _ = self.query(names=[query, query])
        self.assertEqual(
            result["component_search"]["queries"],
            [
                {"name": "ХАИМ", "parent_query": query, "position": 1},
                {"name": "ПЕСЯ", "parent_query": query, "position": 3},
            ],
        )

    def test_components_retain_each_parent_query(self):
        names = ["ХАИМ-НЕИЗВЕСТНЫЙ", "ХАИМ-ПЕСЯ"]
        result, _ = self.query(names=names)
        queries = result["component_search"]["queries"]
        self.assertEqual(
            [part["parent_query"] for part in queries if part["name"] == "ХАИМ"], names
        )

    def test_component_bucket_has_its_own_global_article_limit(self):
        entries = [["ХАИМ", "ARTICLE" + chr(65 + i // 26) + chr(65 + i % 26)] for i in range(30)]
        result, _ = self.query(
            names=["ХАИМ-НЕИЗВЕСТНЫЙ"], indexes=self.indexes(male=entries, female=entries)
        )
        self.assertEqual(result["status"], "not_in_index")
        self.assertEqual(result["candidate_count"], 0)
        components = result["component_search"]
        self.assertEqual(len(components["results"]), 20)
        self.assertEqual(components["candidate_count"], 60)
        self.assertTrue(components["truncated"])

    def test_separator_distinct_source_rows_are_not_merged_during_validation(self):
        manifest = fixture_manifest()
        entries = [["ХАЙМ", "ARTICLE"], ["ХАЙ-М", "ARTICLE"], ["ХАЙ М", "ARTICLE"]]
        manifest["indexes"]["male"]["entries"] = entries
        manifest["indexes"]["male"]["entry_count"] = len(entries)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "indexes.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            indexes = lookup.load_manifest(path)
        self.assertEqual(indexes["male"]["entries"], [tuple(entry) for entry in entries])
        result, _ = self.query(names=["ХАЙМ"], sex="male", indexes=indexes)
        self.assertEqual(self.article(result, "ARTICLE")["variant_count"], 3)

    def test_loader_normalizes_every_pair_without_losing_memberships(self):
        manifest = fixture_manifest()
        manifest["indexes"]["male"]["entries"][0] = ["  хаим ", " khayem "]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "indexes.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            indexes = lookup.load_manifest(path)
        result, code = self.query(names=["ГЕРШЕЛЬ"], indexes=indexes)
        self.assertEqual(code, 0)
        self.assertEqual(
            self.article(result, "GERSHN")["matches"][0]["dictionary_keys"], ["GERSHN", "HIRSH"]
        )
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

    def test_cli_rejects_empty_compact_or_excessive_queries_in_json(self):
        cases = (
            ["--name", "   "],
            ["--name", " — - ‑ "],
            ["--key", "--"],
            ["--name", "А" * 121],
            [argument for _ in range(11) for argument in ("--name", "ХАИМ")],
            ["--name", "ХАИМ", "--key", "KHAYEM"],
            [],
        )
        for arguments in cases:
            with self.subTest(arguments=arguments):
                output = io.StringIO()
                with redirect_stdout(output), self.assertRaises(SystemExit) as error:
                    lookup.main(arguments)
                self.assertEqual(error.exception.code, 2)
                self.assertEqual(json.loads(output.getvalue())["status"], "invalid_request")

    def test_cli_emits_requested_article_candidates_without_variant_lists(self):
        result, code = self.cli(["--name", "ХАИМ"])
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "found")
        self.assertEqual(len(result["results"]), 1)
        self.assertEqual(result["results"][0]["variant_count"], 2)
        self.assertNotIn("variants", result["results"][0])
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
                    if "--key" in arguments:
                        self.assertEqual(set(result["results"][0]["dictionary_keys"]), keys)
                    else:
                        exact_keys = {
                            group["dictionary_key"]
                            for group in result["results"]
                            if any(match["match_type"] == "exact" for match in group["matches"])
                        }
                        self.assertEqual(exact_keys, keys)
                        self.assertLessEqual(len(result["results"]), 20)
                    self.assertEqual(completed.stderr, "")

    def test_actual_unknown_examples_return_candidates_without_changing_bundled_names(self):
        cases = (
            ("Довыд", {"DOVID"}),
            ("Дови", {"DOV", "DOVID"}),
            ("Довидл", {"DOVID"}),
            ("Довидка", {"DOVID"}),
            ("Срулик", {"ISROEL"}),
        )
        original_data = lookup.MANIFEST.read_bytes()
        indexes = lookup.load_manifest()
        self.assertEqual(len(indexes["male"]["entries"]), 1647)
        self.assertEqual(len(indexes["female"]["entries"]), 814)
        indexed_names = {name for record in indexes.values() for name, _ in record["entries"]}
        with tempfile.TemporaryDirectory() as directory:
            for query, keys in cases:
                with self.subTest(query=query):
                    self.assertNotIn(lookup.normalize_name(query), indexed_names)
                    completed = subprocess.run(
                        [sys.executable, "-B", str(HELPER), "--sex", "male", "--name", query],
                        cwd=directory,
                        capture_output=True,
                        text=True,
                        check=False,
                        timeout=10,
                    )
                    self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
                    result = json.loads(completed.stdout)
                    self.assertEqual(result["status"], "candidates_found")
                    self.assertTrue(
                        keys.issubset({group["dictionary_key"] for group in result["results"]}),
                        result,
                    )
                    self.assertTrue(
                        all(
                            match["match_type"] == "fuzzy"
                            for group in result["results"]
                            for match in group["matches"]
                        )
                    )
                    self.assertLessEqual(len(result["results"]), 20)
                    self.assertEqual(completed.stderr, "")
        self.assertEqual(lookup.MANIFEST.read_bytes(), original_data)

    def test_actual_basheve_key_retains_pesya_and_basheva(self):
        result, code = lookup.run_query(
            lookup.load_manifest(), sex="female", names=None, key="BASHEVE", limit=20
        )
        self.assertEqual(code, 0)
        self.assertEqual(result["results"][0]["dictionary_keys"], ["BASHEVE"])
        self.assertEqual(result["results"][0]["variant_count"], 15)
        self.assertFalse(result["results"][0]["truncated"])
        self.assertTrue(
            {"ПЕСЯ", "БАШЕВА"}.issubset(
                {variant["name"] for variant in result["results"][0]["variants"]}
            )
        )
        self.assertNotIn("component_search", result)
        self.assertNotIn("matching_policy", result["query"])


if __name__ == "__main__":
    unittest.main()
