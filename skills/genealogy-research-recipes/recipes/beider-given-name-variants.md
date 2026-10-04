# Recipe: Ashkenazi given-name variants from Beider's indexes

## Goal

Find an ancestor or a DNA match's documentary family under another recorded given-name
form. Use the male and female J-Roots indexes to expand a search, preserving the distinction
between an index entry, a dictionary article and the identity of a person.

These indexes are a useful starting point, **not final or exhaustive lists of names or
their variants**. Add forms found in the person's documents to the search inventory;
absence from an index does not invalidate a documented spelling.

## Load only the requested name

The recorded-name and dictionary-article mappings are bundled in
[`../resources/beider-name-indexes.json`](../resources/beider-name-indexes.json).
Do not load the JSON file or every variant group into the conversation when this recipe
is selected. The lookup helper reads the local JSON inside its process and returns only
bounded article candidates for the requested name. Lookup works offline; source URLs record attribution
and are not fetched during a query.

The bundled snapshot contains 1,647 male and 814 female name/article associations from
complete first-post archive captures dated 2024-12-25, retrieved on 2026-10-03. The JSON
records the archive URLs, capture dates and source hashes; it does not claim to reflect
later forum edits.

Run from this skill's directory:

```sh
python3 scripts/lookup_beider_name.py --sex male --name "Гершель"
python3 scripts/lookup_beider_name.py --sex female --name "Песя"
```

Use `--sex both` when the sex is unknown. Name searches return up to **20 dictionary-article
groups across the selected sexes and inputs**, including similar candidates even when an exact
match exists. Matching spellings from one article use one slot. Each group includes the source,
its key, the best indexed spelling per input, the match type, edit distance and total variant
count. `candidate_count` and `truncated` describe the full eligible group set; `--limit` can
raise the bound to 50 for the current query. Similarity is a search lead, not a source-backed
synonym of an unlisted input.

Select an article to retrieve its recorded variants separately:

```sh
python3 scripts/lookup_beider_name.py --name "Довыд"
python3 scripts/lookup_beider_name.py --key DOVID
python3 scripts/lookup_beider_name.py --key BASHEVE
```

`--key` matches an article key exactly. It returns at most 20 variants per matching index
result by default, up to 50 with `--limit`, their total count and truncation, retaining every article membership of each
returned spelling. It does not expand other articles transitively. No full-index output mode
is provided.

### How similar candidates are found

The helper compares NFC-normalized uppercase forms and ignores spaces and supported
hyphens/dashes in a separate comparison key. It preserves the raw query and indexed spelling.
`exact` means the normalized spelling matches; `separator_normalized` means only separators
differ. Thus `Довид-Лейб`, `Довид Лейб` and `Довидлейб` share a comparison key; this does not
assert that the compound form has an entry in the current index.

`fuzzy` candidates use unrestricted Damerau–Levenshtein distance: insertions, deletions,
substitutions and adjacent transpositions. Compact inputs of one or two letters require zero
edits; three or four allow one; longer inputs allow two. Exact matches rank first, then
separator-normalized matches, then fewer edits. Within an edit tie, a coarse Cyrillic
consonant signature can prioritize agreement: remove vowels and hard/soft signs, fold
Б/П, В/Ф, Г/К, Д/Т, Ж/Ш and З/С, and collapse repeated consonants. This heuristic does not
admit additional candidates or provide a confidence probability. It is not a general
cross-language phonetic encoder; `--name` expects recorded Cyrillic forms and `--key` accepts
Latin article keys.

For example, `Дови` can suggest both DOV and DOVID; `Срулик` can suggest ISROEL, RUVN and
SHMUEL. Keep the alternatives until the original document and its context distinguish them.
An approximate-only whole-name result has `status: candidates_found`; a whole-name exact or
separator match has `status: found`.

Whitespace/hyphen compounds also produce a separate `component_search`, recording each part's
parent input and position. Its article groups have their own bound, count and truncation.
Component matches never count as an exact whole-name match: `Довид-Хаим` may have useful
component results while the whole-name status remains `not_in_index`. Compare the original
document before interpreting parts as a double given name.

If the bundled JSON is missing or invalid, report **source unavailable**. A successful
lookup with no admitted whole-name candidate means **not in this index under the reported
matching policy**, not "this name did not exist" or
"this person is absent."

## What the index changes in a search

The label in parentheses is the **dictionary article where a form is discussed**, not a
unique person's name or an instruction to replace every occurrence with one canonical form.
The index describes traditional Jewish names from sixteenth- through nineteenth-century
documents in several languages; names that became traditional only after 1917 are outside
its stated scope. It does not supply a universal map of Soviet or American name substitutions.

These compact examples illustrate why the lookup matters; query the needed local group:

| Index | Recorded forms | Dictionary article |
| --- | --- | --- |
| Male | Хаим, Хайкель | KHAYEM |
| Male | Лейб, Лейба | LEYB |
| Male | Гершель | GERSHN **or** HIRSH |
| Female | Бася, Песя | BASHEVE |
| Female | Хана, Геся | KHANE |
| Female | Гося | GOLDE **or** HODES |

The last male and female examples appear under more than one article. Keep every candidate
article rather than silently choosing the first. Likewise, an unfamiliar-looking form such
as Песя is a reason to consult the entry, not to guess a connection from its sound.

## Apply the result to records and DNA research

1. Preserve the original spelling and identify the field: given name, double-name element,
   patronymic or surname. Look up each given-name element separately; this resource does not
   infer a father's name from a patronymic or a given name from a surname.
2. Retrieve each selected article's forms with `--key` and search them in the appropriate name
   field. Keep approximate suggestions and article alternatives separate, including when an
   exact spelling has more than one interpretation. A bounded list with
   `truncated: true` is a partial search inventory, not complete coverage.
3. Correlate hits by date, town, household and relatives. Two forms in one dictionary article
   create search candidates; they do not establish that two records describe the same person.
   Different articles likewise do not rule out a documented personal name change.
4. For a DNA match, use the expanded searches to document the pedigree. Name resemblance or
   article membership contributes no DNA relationship probability. Household and identity
   conflicts belong in `russian-empire-jewish-identity-attribution.md`; combining documents
   and DNA into a conclusion belongs in `evidence-proof-judgment.md`.

## Fact-check status

The examples and ambiguous entries above were checked directly against the two indexes on
2026-10-01. Their historical coverage is the index compiler's stated scope. The complete
dictionary articles and the equivalence of any particular person's records have not been
established by this lookup.
