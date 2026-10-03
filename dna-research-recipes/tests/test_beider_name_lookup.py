"""Bounded lookup and source-failure checks for the Beider name index helper."""

import importlib.util
import io
import json
import unittest
from contextlib import redirect_stdout
from http.client import HTTPResponse
from pathlib import Path
from unittest.mock import Mock, patch

HELPER = Path(__file__).resolve().parents[1] / "scripts/lookup_beider_name.py"
SPEC = importlib.util.spec_from_file_location("lookup_beider_name", HELPER)
lookup = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lookup)

MALE_URL = "https://forum.j-roots.info/viewtopic.php?t=2060#p32424"
FEMALE_URL = "https://forum.j-roots.info/viewtopic.php?f=98&t=2059"
INDEXES = {
    "male": {"url": MALE_URL, "post_id": "p32424", "fallback_urls": []},
    "female": {"url": FEMALE_URL, "post_id": "p32423", "fallback_urls": []},
}


def post(post_id, content):
    return f'<div id="{post_id}" class="post"><div class="postbody"><div class="content">{content}</div></div></div>'


MALE_HTML = post(
    "p32424",
    "<span>ХАИМ <b>(KHAYEM)</b></span><br>ХАЙКЕЛЬ (KHAYEM)<br>"
    "ГЕРШЕЛЬ (GERSHN)<br>ГЕРШЕЛЬ (HIRSH)<br>"
    "ЁСЕЛЬ (YOYSEF)<br>ЕСЕЛЬ (ESEL)<br>МЕШУЛЕМ-ЗУСЯ (MESHULEM)<br>"
    "<blockquote>ПЕСЯ (PERL)</blockquote>",
) + post("p99999", "НЕВЕРНЫЙ (KHAYEM)<br>ПЕСЯ (PERL)")
FEMALE_HTML = post(
    "p32423",
    "ПЕСЯ (BASHEVE)<br>БАСЯ (BASHEVE)<br>ГОСЯ (GOLDE)<br>ГОСЯ (HODES)<br>"
    "ГОЛДА (GOLDE)<br>ГОДЕС (HODES)<br>ЦIПРА (TSIPOYRE)<br>ЦIСЦА (TSIPOYRE)",
)


def fixture_fetch(url):
    return MALE_HTML if "2060" in url else FEMALE_HTML


class BeiderLookupTests(unittest.TestCase):
    def query(self, names=None, key=None, limit=20, sex="both", fetcher=None):
        if fetcher is None:
            fetcher = fixture_fetch
        return lookup.run_query(
            INDEXES, names=names, key=key, limit=limit, sex=sex, fetcher=fetcher
        )

    def test_nested_tags_br_and_first_post_isolation(self):
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
        self.assertNotIn("НЕВЕРНЫЙ", str(result))

    def test_quoted_entries_are_excluded(self):
        result, code = self.query(names=["ПЕСЯ"], sex="male")
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "not_in_index")

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

    def test_cli_name_retains_all_variant_memberships_without_expanding_other_articles(self):
        output = io.StringIO()
        with (
            patch.object(lookup, "load_manifest", return_value=INDEXES),
            patch.object(lookup, "fetch_source", side_effect=fixture_fetch),
            redirect_stdout(output),
        ):
            code = lookup.main(["--sex", "female", "--name", "ГОЛДА"])
        self.assertEqual(code, 0)
        match = json.loads(output.getvalue())["results"][0]
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

    def test_cli_key_retains_all_variant_memberships_and_output_limit(self):
        output = io.StringIO()
        with (
            patch.object(lookup, "load_manifest", return_value=INDEXES),
            patch.object(lookup, "fetch_source", side_effect=fixture_fetch),
            redirect_stdout(output),
        ):
            code = lookup.main(["--sex", "female", "--key", "GOLDE", "--limit", "1"])
        self.assertEqual(code, 0)
        match = json.loads(output.getvalue())["results"][0]
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

    def test_index_mixed_latin_i_and_cyrillic_letters_are_preserved(self):
        result, _ = self.query(names=["ЦIПРА"], sex="female")
        self.assertEqual(result["results"][0]["dictionary_keys"], ["TSIPOYRE"])
        self.assertEqual(result["results"][0]["variant_count"], 2)
        rows = lookup.parse_index_html(post("p1", "ІЇЄ (A)<br>Я (B)"), "p1")
        self.assertEqual(rows, [("ІЇЄ", "A"), ("Я", "B")])

    def test_missing_post_and_zero_valid_rows_are_unavailable(self):
        for html, error in (
            (post("p1", "ХАИМ (KHAYEM)"), "post_missing"),
            (post("p32424", "temporarily unavailable"), "index_entries_missing"),
        ):
            with self.subTest(error=error):
                result, code = self.query(
                    names=["ХАИМ"], sex="male", fetcher=lambda url, html=html: html
                )
                self.assertEqual(code, 1)
                self.assertEqual(result["status"], "source_unavailable")
                self.assertEqual(result["errors"][0]["error"], error)

    def test_unavailable_content_is_not_a_negative_lookup(self):
        html = '<div id="p32424"><div class="other">ХАИМ (KHAYEM)</div></div>'
        result, code = self.query(names=["ХАИМ"], sex="male", fetcher=lambda url: html)
        self.assertEqual(code, 1)
        self.assertEqual(result["errors"][0]["error"], "post_content_missing")

    def test_fetch_failure_is_not_absence_and_output_is_terse(self):
        def failed_fetch(url):
            raise lookup.SourceUnavailable("fetch_failed")

        result, code = self.query(names=["ХАИМ"], fetcher=failed_fetch)
        self.assertEqual(code, 1)
        self.assertEqual(result["status"], "source_unavailable")
        self.assertLess(len(json.dumps(result)), 400)

    def test_fallback_url_is_tried_and_recorded(self):
        indexes = {
            "male": {
                **INDEXES["male"],
                "fallback_urls": ["https://www.forum.j-roots.info/viewtopic.php?t=2060"],
            }
        }

        def fetch(url):
            if url == MALE_URL:
                raise lookup.SourceUnavailable("fetch_failed")
            return MALE_HTML

        result, code = lookup.run_query(
            indexes, names=["ХАИМ"], key=None, limit=20, sex="male", fetcher=fetch
        )
        self.assertEqual(code, 0)
        self.assertIn("www.forum", result["results"][0]["source_url"])

    def test_one_unavailable_selected_index_keeps_partial_results_explicit(self):
        def fetch(url):
            if url == FEMALE_URL:
                raise lookup.SourceUnavailable("fetch_failed")
            return MALE_HTML

        result, code = self.query(names=["ХАИМ"], fetcher=fetch)
        self.assertEqual(code, 1)
        self.assertEqual(result["status"], "source_unavailable")
        self.assertEqual(len(result["results"]), 1)
        self.assertEqual(result["errors"], [{"sex": "female", "error": "fetch_failed"}])

    def test_unknown_query_has_index_scope(self):
        result, code = self.query(names=["НЕИЗВЕСТНЫЙ"])
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "not_in_index")
        self.assertIn("not evidence", result["scope"])

    def test_cli_rejects_unbounded_limit_in_json(self):
        output = io.StringIO()
        with redirect_stdout(output), self.assertRaises(SystemExit) as error:
            lookup.main(["--name", "ХАИМ", "--limit", "51"])
        self.assertEqual(error.exception.code, 2)
        self.assertEqual(json.loads(output.getvalue())["status"], "invalid_request")

    def test_cli_emits_json_and_no_page(self):
        output = io.StringIO()
        with (
            patch.object(lookup, "load_manifest", return_value=INDEXES),
            patch.object(
                lookup,
                "fetch_source",
                side_effect=lambda url: MALE_HTML if "2060" in url else FEMALE_HTML,
            ),
            redirect_stdout(output),
        ):
            code = lookup.main(["--name", "ХАИМ"])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(output.getvalue())["status"], "found")
        self.assertNotIn("postbody", output.getvalue())

    def test_truncated_http_response_is_unavailable_through_cli(self):
        body = '<div id="p32424"><div class="content">ХАИМ (KHAYEM)<br>'.encode()
        wire = (
            b"HTTP/1.1 200 OK\r\nContent-Length: 5000\r\n"
            b"Content-Type: text/html; charset=utf-8\r\n\r\n" + body
        )

        class TruncatedSocket:
            def makefile(self, *args, **kwargs):
                return io.BytesIO(wire)

        response = HTTPResponse(TruncatedSocket())
        response.begin()
        response.url = MALE_URL
        opener = Mock()
        opener.open.return_value = response
        output = io.StringIO()
        with (
            patch.object(lookup, "load_manifest", return_value=INDEXES),
            patch.object(lookup, "build_opener", return_value=opener),
            redirect_stdout(output),
        ):
            code = lookup.main(["--sex", "male", "--name", "ЛЕЙБ"])
        result = json.loads(output.getvalue())
        self.assertEqual(code, 1)
        self.assertEqual(result["status"], "source_unavailable")
        self.assertEqual(result["errors"][0]["error"], "post_content_incomplete")

    def test_http_sources_and_redirects_are_rejected(self):
        with self.assertRaisesRegex(lookup.SourceUnavailable, "https_required"):
            lookup.fetch_source("http://forum.j-roots.info/index.php")
        with self.assertRaisesRegex(lookup.SourceUnavailable, "insecure_redirect"):
            lookup.VerifiedRedirects().redirect_request(
                None, None, 302, "", {}, "http://forum.j-roots.info/index.php"
            )


if __name__ == "__main__":
    unittest.main()
