# Recipe: Recovering historical records with MyHeritage

## Goal

Recover candidate historical records when a MyHeritage search fails or returns too much.
Diagnose coverage, indexed fields and restrictions; preserve what was searched and what changed.
All worked examples below are synthetic.

## The mental model

Collections, indexes/OCR, supplied fields, matching rules and displayed presentation can each hide
or distort a relevant record. Change one layer at a time and compare the returned evidence.
A successful retrieval still needs identity verification.

## Operating rules

- Separate **documented facts, estimates and hypotheses** before constructing a query. Do not
  require a guessed maiden name, calculated birth year or uncertain birthplace in every search.
- Check the collection description and actual form. Categories and individual collections offer
  different fields; a field offered by the general search is not a promise of complete indexing.
- Names are optional search inputs. Use the offered spelling, initials and additional-field
  controls deliberately; do not assume an old demonstration describes today's defaults. [H1]
- Preserve the sparse baseline before tightening it. If a tighter query fails, relax one condition
  at a time and record the reason; changing everything together conceals what excluded the record.
- Verify original wording and the person's role. Transliterated results, OCR, extracted relatives,
  inferred dates, trees and automated matches are finding aids, not independently established facts.
- Route AI transcription/translation to `ai-for-documentary-records.md`, bounded Ashkenazi given-name
  lookup to `beider-given-name-variants.md`, and identity/conflict/negative-evidence rulings to
  `evidence-proof-judgment.md`. This recipe prepares candidates and search coverage, not a verdict.

## Fourteen practical howtos

### 1. Search the catalog for record sets before searching their people

Clear previous catalog filters, then try jurisdiction and record-type words in the collection
title/description search: school, register, passport, probate, newspaper. These keywords locate
collections; they are not a search for every personal name inside their records. [S2, H2]

For Jewish research, try Jewish-related descriptions alongside the relevant town and civil,
religious or national record groups. A neutral collection title may contain relevant material.
Neither a keyword match nor its absence establishes complete coverage of a community. [S4]

### 2. Check coverage and remove filters that hide useful collections

Use catalog type, location and time filters to discover plausible sets, then read their descriptions.
Check date span, locality, record type, source institution, image availability and update information.
A broad title is not assurance that every town, year or surviving volume is included. [H2, H3]

Repeat discovery without an images restriction: an index may provide the locator needed elsewhere.
A collection-level image indicator does not guarantee an image for every entry. Clear accumulated
filters when changing jurisdictions, and preserve promising index-only collections in the ledger.

### 3. Run a sparse → tight → relaxed ladder

Start sparsely, select a suitable collection, then add one supported event or relative.
If candidates disappear, remove the weakest condition first. [S1, S6, H1]

**Synthetic walk-through:** Anna Weiss's marriage in 1911 is documented; birth in 1887 and
Millford birthplace are estimates. Suppose requiring exact spelling and both estimates fails.

1. **Sparse:** In a suitable marriage collection, search Anna Weiss without birth year/place;
   keep exact given-name matching enabled.
2. **Tight:** Keep that exact-name constraint and add only the documented marriage year, 1911;
   compare the returned candidates.
3. **Relax:** Keep the collection and 1911; loosen exact given-name matching to admit initials
   or variants where the form supports them. Inspect each candidate's original wording.

These are proposed queries, not reported results. Keep each attempt and its reason in the ledger.

### 4. Search the name as it might actually have appeared

Create a short variant list: native spelling, maiden and married surnames, familiar given name,
initials and middle names. Try fictional Anna Maria Weiss as Anna Weiss and Maria Weiss, then the
documented married surname. Use offered initials matching or exact-spelling controls consciously. [H1]

An exact form can reduce a common-name result set, but also exclude abbreviated or reordered text.
In newspapers, a woman may appear under her husband's name or an honorific. Test those forms as
separate leads; do not turn a familiar name or shared surname into an identity conclusion. [S1, S3, H5]

### 5. Preserve native names beneath translated results

MyHeritage's Global Name Translation can match name versions, nicknames and different alphabets,
and transliterate returned names into the query language. That convenience can hide the precise
original spelling. Save the native name alongside the displayed version. [S1, S4, H4]

Where possible, inspect the original record and retry a documented native spelling separately.
Treat plausible name equivalents as search alternatives, not interchangeable evidence. Ask a
qualified reader about ambiguous letters; verify transcription and translation as separate tasks.

### 6. Attach every date to the event it describes

Distinguish birth, marriage, death, residence and publication dates before choosing a field.
Current search forms support year or full-date entry; use the precision the evidence warrants.
If a range control is unavailable, test neighboring years separately or omit the weak date. [H1]

A school yearbook's publication year differs from a pupil's birth year. A birth year inferred from
grade or age remains an estimate. An obituary's publication date may follow the death; an article
can commemorate an event decades earlier. Do not force all those dates into birth-year search. [S3, S6]

In a civil registration index, verify whether a quarter denotes registration rather than birth;
keep certificate volume/page locators. A pension file can be created years after military service:
do not restrict discovery to the war years alone. [S5, S9]

### 7. Separate the person's place from the record's place

Identify birthplace, residence, event location, publication town and collecting jurisdiction.
A fictional death in Millford may be reported by a newspaper published in nearby Ashbridge.
Try Millford as a keyword while broadening the publication-place restriction. [S6]

Check neighboring towns, historical spellings and jurisdictions created by border changes.
Search the countries under which the locality's records might be cataloged, then inspect the
collection description. A modern national filter can conceal records organized another way. [S1, S5]

The German-records tutorial uses a US census entry for someone born in Germany to explain why
a Germany place filter need not identify a German source: event geography does not establish
source custody. Likewise, an American who served with Canadian forces may appear
in Canadian military records. Read the originating collection and recorded role separately. [S8, S9]

### 8. Find the target through a better-documented relative

Use the additional-fields control, currently labelled **+More**, for relatives, life events,
keywords or gender where offered. Test a known parent or spouse when the target's own name or
dates are missing. Avoid filling every relative field with guesses. [S1, H1]

Alternatively search the relative directly, then inspect their household or named associates.
In passenger records a person can appear as a destination contact or relative remaining abroad,
as well as a traveler. Read the role and column: a name hit does not establish immigration. [S5]

### 9. Replace a weak name with a distinctive contextual clue

In a text-searchable collection, try an address, occupation, employer, school activity, place,
relative or unusual event. For fictional Samuel Reed, compare his name plus Oak Street with his
name plus a documented workshop. Search the strongest clues separately when their combination fails.

A property advertisement or legal notice may identify an address without naming the ancestor.
Use period occupation terms, street-name variants and relevant local vocabulary. A contextual hit
locates a page to read; it does not establish who occupied the address at another date. [S2, S3, S6]

### 10. Move from a person-name index to full text when available

Check whether the same material has a structured name index and a full-text counterpart.
Names can be visible on a page but absent from the extracted name index. Search an available
text version with a surname, nickname, school or activity, then inspect the page. [S6]

Record that these are two retrieval routes into the same underlying material, not two independent
witnesses. Do not presume that every collection offers both. If the catalog or description gives
only an index, follow its source information rather than inventing a hidden full-text interface.

### 11. Diagnose OCR with the page, then change the query

Compare a returned page with its OCR text when available. Look for damaged print, misread letters,
columns read out of order and names split across lines. A printed Rosen- at one line's end and
berg at the next can defeat a search that expects the joined spelling. [S1, S3]

Try another documented name form, drop an exact-name restriction, or replace the name with a
distinctive contextual keyword. Adapt to a misreading actually observed on the page rather than
generating endless arbitrary typos. If text recovery fails, browse the likely issue or section.
Do not assume wildcard, Boolean or quoted-phrase syntax works without current documentation.

### 12. Search newspaper images and extracted records as complementary routes

MyHeritage's **Names & Stories** collections offer structured records extracted from newspapers;
OldNews offers newspaper material to search and read. For covered material, try structured event
and relative fields. Follow the record's OldNews link or **View full newspaper page** control to
read the printed article; record any access restriction. If one route fails, try the other with
name variants or contextual words. [S7, H6, H7]

Extracted event dates or expanded relatives' names can be inferred from the article's wording.
Compare each field with the printed statement and label an inference instead of treating it as a
verbatim fact. Check each service's actual title/date coverage; their holdings need not coincide.

For example, a printed age can produce an indexed birth year that never appears in the article.
Search the literal name and reported age or relative in full text, rather than requiring that
derived year. An expanded parent's surname also need not occur as a complete printed name.

### 13. Read beyond the highlighted hit

Read the whole article, continuation, page heading and surrounding entries. In censuses, inspect
the preceding and following pages for household continuation and nearby relatives. In yearbooks,
inspect other pages and adjacent years for the same pupil's activities and name forms. [S1, S6]

For a death or unusual incident, search later issues and other local papers: the first report may
precede a fuller obituary or correction. Preserve newspaper title, publication date, page and a
full-page copy when available, alongside any clipping. Copied reports are not independent witnesses.

### 14. Turn an index-only hit or automated match into a retrievable lead

If no image is supplied, save the collection citation, originating institution, reference number,
volume/page and original-source link that are actually provided. Use that locator to seek the image
or request the record from its custodian. State explicitly when the original remains unavailable.

Treat record matches, related-record suggestions and tree matches as new searches to evaluate.
Compare names, roles, dates, places and relationships against the source; retain competing candidates.
End with the coverage ledger and next discriminating search, not “MyHeritage has no such record.”
Use the evidence/proof recipe for any proposed identity or negative-evidence conclusion. [S1, S5]

## Prompt-craft

Supply sourced facts with uncertainty labels, catalog descriptions, available fields,
previous queries and candidate images. Then ask:

> Build a controlled MyHeritage recovery sequence. Separate documented facts from estimates.
> Identify which collection and field could hold each clue. Keep a sparse baseline; tighten one
> condition, then state which weak condition to relax if it fails. Include name/native-script,
> date-role, geography, relatives and text/image pivots only where useful. For each candidate,
> preserve original wording, identify inferred fields and record what remains unverified.
> Return the query ledger and next discriminating search. Do not conclude identity or absence.

Without verified access, an assistant prepares queries rather than claiming it searched.
Use offered controls or separate attempts instead of undocumented platform syntax.

## Pitfalls worth internalizing

- More facts can reduce recall when they are estimates, wrong event types or unindexed fields.
- Global results and relevance order do not establish complete archival coverage or correct identity.
- A catalog keyword searches collection metadata; a personal-name search searches different material.
- Translated display names and inferred newspaper fields can look more definite than the original.
- Publication place/date need not equal the person's residence or event place/date.
- A shared source republished elsewhere is another access route, not another independent witness.
- Image restrictions, stale filters and a missing text counterpart can manufacture apparent absence.
- OCR recovery ends at the readable original; no general OCR-accuracy percentage settles a particular hit.
