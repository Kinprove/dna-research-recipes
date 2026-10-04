# Ancestry record-search recovery

## Goal

Recover an archival record when Ancestry's hints, person search or name index fails.
Choose the recovery that addresses the actual failure: hidden search settings,
catalog discovery, an overconstrained query, a transcription error, an image-only
volume or a record held elsewhere. Do not keep repeating the same name search.

This recipe owns Ancestry retrieval. For identity and negative-evidence judgments,
read [evidence-proof-judgment.md](evidence-proof-judgment.md); for AI transcription
and full-text finding aids, read [ai-for-documentary-records.md](ai-for-documentary-records.md).

## Twelve recovery methods

### 1. Reset the search state before changing the ancestor

**Trigger:** expected records disappear after research in another country or category.

Check Collection Focus and result-type settings; restore the intended collections
and historical-record categories. These settings persist between searches. Record
their state before and after resetting them, then rerun the same query: this tests
the search environment without changing the person. See [Ancestry's refinement guide](https://help.ancestry.com/hc/en-us/articles/53933347318419-Refining-Your-Search-to-Improve-Results).

Also inspect any active option that suppresses records already saved or viewed.
Ancestry's April 2026 demonstration shows its smart filter hiding other records
from an already-attached census. That demonstration is a diagnostic clue; inspect
the controls actually present in the current account before attributing missing
results to this feature. Do not remove existing tree attachments to recover a hit.

### 2. Clear catalog locality terms to recover nationwide collections

**Trigger:** a town, province or county in the catalog's Title/Keywords finds very little.

Clear or replace the locality word in Title/Keywords before running separate
state or country searches. A nationwide collection can contain that locality
without naming it in its catalog text. Compare the collection lists, open national
candidates, and then choose the locality inside the collection. The August 2026
Ancestry tutorial demonstrates countrywide Canadian censuses disappearing when
the catalog text query changes from Canada to Nova Scotia.

Inspect geographic filters separately and widen any that restrict the intended
jurisdiction. Widening a filter alone does not repair a text query that still
requires the locality word. Neither search is an exhaustive inventory of records
concerning the place.

### 3. Search catalog titles and keywords separately

**Trigger:** the expected record category is missing from the catalog results.

Try a short title fragment, then a separate keyword search. Catalog keywords can
find descriptions that a title search misses; they do not search every name or
word in the underlying images. More keyword terms narrow the catalog: retry
distinctive terms individually instead of pasting a long imagined collection
title. Try related record vocabulary in separate passes, such as electoral
registers when searching for census-like household or residence evidence.
Open each plausible collection and inspect its actual coverage.
See [the Card Catalog guide](https://help.ancestry.com/hc/en-us/articles/53933305954579-Using-the-Card-Catalog).

### 4. Revisit collections that changed after the failed search

**Trigger:** an old search log says the relevant collection produced no candidate.

Use the catalog's Last Updated ordering to identify collections worth revisiting.
Read what changed and rerun the saved query in the relevant collection. An update
date alone does not establish new coverage for the target: it can concern other
years, localities or data. Record the collection and the recheck date, rather than
carrying an old failure forward indefinitely.

### 5. Diagnose coverage inside the collection

**Trigger:** a collection title spans the right place and years, but the person is absent.

Read its Source and About sections, then inspect the available browse subdivisions
and volumes. Check the actual locality, date, record type and population covered,
including omissions or restrictions. Run a place/date query without the target
name to see what the index returns for that area. This is an **index diagnostic**:
zero results can reflect unindexed images, missing fields or restrictive settings.
Check the image inventory separately before deciding which material is absent.
See [Ancestry's collection-information guide](https://help.ancestry.com/hc/en-us/articles/53933269983507-Source-and-Collection-Information).

Keep three observations separate: no indexed candidate; no matching images in the
available inventory; and documented absence in the original surviving records.
Use the existing evidence-judgment recipe before drawing a genealogical conclusion.

### 6. Remove tree facts that belong to another life stage

**Trigger:** a tree-launched search returns nothing useful for childhood or early life.

Inspect the populated query, including relationships. Remove the later spouse,
children, later residence and uncertain facts when they constrain an early-life
search; retain appropriate parents or siblings. Use the name recorded at that
life stage. Search forms differ by collection, so use only fields that this
collection actually exposes. A missing death-date control in a census search is
not evidence that the person lacks a death record.
See [How to Search](https://help.ancestry.com/hc/en-us/articles/53933305561747-How-to-Search-Ancestry)
and [Search Tips](https://help.ancestry.com/hc/en-us/articles/53933347309331-Ancestry-Search-Tips).

### 7. Relax the place level and age separately

**Trigger:** an exact city or birth year eliminates otherwise plausible candidates.

Select a recognized place from Ancestry's suggestions, then widen its matching
level from city to county or adjacent counties. Exact Oakland excludes a record
that gives only Alameda County. Keep birthplace and residence in their own fields:
the place where a census household lived need not be where its members were born.

Then relax the year independently. A census age converted to a birth year can
shift by one year even without an erroneous age; an unreliable age requires a
wider interval. Preserve the reliable anchor while changing one constraint at a
time, and record which change recovered a candidate.
See [Ancestry's refinement guide](https://help.ancestry.com/hc/en-us/articles/53933347318419-Refining-Your-Search-to-Improve-Results).

### 8. Use wildcards for a specific spelling uncertainty

**Trigger:** a name has plausible transcription or spelling variants.

Search recorded alternatives, initials and abbreviations; then use a pattern
such as `Niels?n` or `Greenbla*`. Keep a stable fragment and test one uncertain
part at a time. Do not combine wildcard searches with Soundex. Soundex emphasizes
the name's initial letter; an incorrect initial can defeat that matching method.
Use an alternative spelling or a name-free recovery instead of repeating it.

Current Ancestry help pages disagree about wildcard minimum lengths and positioning.
The patterns above satisfy both published sets of restrictions. Do not infer a
universal short-pattern rule or require an Exact checkbox from an old tutorial;
check the current field's instructions when a pattern is rejected.
See [Spelling Variations](https://help.ancestry.com/hc/en-us/articles/53933306665107-Searching-with-Spelling-Variations)
and [Search Tips](https://help.ancestry.com/hc/en-us/articles/53933347309331-Ancestry-Search-Tips).

### 9. Recover an index entry without the target's name

**Trigger:** the right collection and locality exist, but variants still fail.

Remove the target name and retain a discriminating combination of available
fields: residence, approximate birth year, sex, birthplace or relatives. Prefer
a sibling, household head or known neighbor with a more distinctive name as an
entry point. Open the resulting image and inspect the target household or nearby
pages. Ancestry's April 2026 tutorial recovers a mistranscribed Cowan household
using non-name fields and the parents' names after direct searches fail.

Use [Ancestry's horizontal-search advice](https://help.ancestry.com/hc/en-us/articles/53933305561747-How-to-Search-Ancestry)
and, for the 1950 census, [NARA's household/neighbor search guidance](https://www.archives.gov/research/census/1950/faqs).
These are retrieval pivots; route any identity decision to the evidence-judgment
recipe. Do not add a recovered household to the tree merely because it matches
the search constraints.

### 10. Use the volume's own index and page numbering

**Trigger:** an image collection exists, but its searchable index misses the target
or the material is browse-only.

Choose the relevant locality, year and volume. Inspect the beginning and end for
a handwritten or printed index; follow its name variant and volume/page reference.
Distinguish the book's page number from the viewer's image number, and check the
volume named by the index. Maps can require direct browsing because labels are
initials or are poorly indexed. If the original book has no usable index, specify
a bounded image range and inspect it systematically.

Ancestry's probate demonstration follows an original index to a different book
and its underlying will. If the collection offers a separate index volume,
browse that too; finding the index entry is the start of retrieval, not the will.

The internal-index method is described by [Lisa Louise Cooke](https://lisalouisecooke.com/2019/11/17/browse-only-records-at-ancestry/).
Use the current viewer's available navigation; the 2019 article's screen positions
are not a current interface contract. Preserve the collection, volume, printed
page and image locator for each candidate.

### 11. Turn a census address into a bounded image search

**Trigger:** a household is expected at a known address but the name index fails.

Find a contemporary address in a directory, draft or naturalization record;
resolve it to the enumeration district for the **same census year**; browse that
district's images on Ancestry or at the archive. An earlier address is a lead to
check, and another year's district boundaries are not a substitute.
See [NARA's 1940 address-to-district method](https://www.archives.gov/research/census/1940/start-research).

For the **1950 U.S. census**, inspect sheets numbered 71 onward as well as the
ordinary sequence: these carry people enumerated out of order. The numbering jump
does not establish that images are missing. This is a year-specific convention,
not a rule for every census. Follow any "see sheet / line" reference on the
original schedule and check informant footnotes when a neighbor supplied the
household information. See [NARA's 1950 FAQ](https://www.archives.gov/research/census/1950/faqs).

### 12. Carry the original locator beyond Ancestry

**Trigger:** Ancestry has an index entry without an image, a Web Records pointer,
or a different provider finds a page that Ancestry's name search misses.

Copy the collection citation and original repository's locator. For a Web Records
entry, follow the linked source site. For an index-only collection, identify the
custodian and its image or copy-request route; an Ancestry index does not guarantee
Ancestry hosts the image. Access conditions can differ between a personal account
and a library edition. See [Ancestry's library guide](https://help.ancestry.com/hc/en-us/articles/53933331964691-Searching-on-Ancestry-at-a-Library-or-School)
and [Web Records guide](https://help.ancestry.com/hc/en-us/articles/53933331868179-Finding-Records-Online-with-Ancestry-Web-Records).

For England and Wales censuses **1841–1901**, carry the archive series, piece,
folio/page and, where applicable, book reference into a reference search or image
browse. Do not reuse that locator shape unaltered for the household schedules of
1911 or 1921. When a whole locality is missing, check the original archive's
coverage documentation before continuing name permutations.
See [The National Archives census guide, sections 10–11](https://www.nationalarchives.gov.uk/help-with-your-research/research-guides/census-records/).

## Prompt-craft and search log

> Recover this Ancestry record: [person and event], [known locality and date],
> [collection URL], [queries and settings already tried]. Diagnose the next
> retrieval failure before suggesting another name search. Give three ordered
> searches, each changing a named constraint and stating what its result tests.
> Include a national-collection catalog check, a name-free query and a bounded
> image-browse route where relevant. Record the original locator. Distinguish
> documentation-supported instructions from actions you actually executed.

For each pass, record the collection URL/ID, search date, fields and matching
settings, active result scopes, result or access failure, image range inspected
and next discriminating query. A useful handoff names the next action, rather
than merely reporting that nothing was found.
