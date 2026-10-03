# Recipe: Ashkenazi given-name variants from Beider's indexes

## Goal

Find an ancestor or a DNA match's documentary family under another recorded given-name
form. Use the male and female J-Roots indexes to expand a search, preserving the distinction
between an index entry, a dictionary article and the identity of a person.

These indexes are a useful starting point, **not final or exhaustive lists of names or
their variants**. Add forms found in the person's documents to the search inventory;
absence from an index does not invalidate a documented spelling.

## Load only the requested name

The complete indexes are **external resources**, described in
[`../resources/beider-name-indexes.json`](../resources/beider-name-indexes.json).
Do not preload either index, paste a whole forum page into context, or read all variant
groups when this recipe is selected. The lookup helper fetches and parses the requested
index inside its process; only a bounded result enters the conversation.

Run from this skill's directory:

```sh
python3 scripts/lookup_beider_name.py --sex male --name "Гершель"
python3 scripts/lookup_beider_name.py --sex female --name "Песя"
```

Use `--sex both` when the sex is unknown. Use `--key BASHEVE` when the dictionary article
is already known. Each result includes the source, all matching article keys, the total
variant count and whether the returned variants were truncated. The default limit is 20;
request more only for the current name, up to 50. No full-index output mode is provided.

If the source cannot be read, report **source unavailable**. A successful lookup with no
entry means **not in this index**, not "this name did not exist" or "this person is absent."

## What the index changes in a search

The label in parentheses is the **dictionary article where a form is discussed**, not a
unique person's name or an instruction to replace every occurrence with one canonical form.
The index describes traditional Jewish names from sixteenth- through nineteenth-century
documents in several languages; names that became traditional only after 1917 are outside
its stated scope. It does not supply a universal map of Soviet or American name substitutions.

These compact examples illustrate why the lookup matters; fetch the needed group for work:

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
2. Search the returned recorded forms in the appropriate name field. Keep article alternatives
   separate when an exact spelling has more than one interpretation. A bounded list with
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
