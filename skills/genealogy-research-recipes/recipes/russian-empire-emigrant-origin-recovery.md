# Recipe: Recovering a Russian Empire emigrant's origin locality

## Goal

Build a destination-to-origin research packet for a person who left the Russian Empire or its
successor territories, principally in 1880–1924. The five workflows below cover **United States
arrivals, including Canadian transit**. They work across confessions; the Jewish locality tools
are a branch, not a requirement for every emigrant. For another destination, retain the packet
structure and replace the arrival and citizenship repositories with that country's record system.

The output is a movement chronology, a complete arrival-record extraction, a contact worklist,
a competing-locality table and an archive handoff. An unreadable town name or a missing manifest
remains an explicit unresolved item; it does not prevent recording the other evidence.

## The failure to prevent

An index hit under a familiar name is not yet the right immigrant. A town in a manifest can be a
birthplace, last residence, relative's address or destination. Copying any one of those into a
birthplace field sends the next search to the wrong records. Preserve the wording and field role
until the movement and locality evidence resolve them. [S1–S4, H1]

Use [research-documentation.md](research-documentation.md) for the research log and report,
[source-citation.md](source-citation.md) for citations and
[evidence-proof-judgment.md](../../genealogy-research-recipes/recipes/evidence-proof-judgment.md)
for deciding identity and resolving conflicts. The tables below extend those artifacts with
migration-specific information; they do not replace their interpretation rules.

## Before starting

Choose one emigrant and one question: for example, which locality should be searched for this
person's birth or marriage record? Give people and records local handles such as `P1` and `R1`.
Keep full images, addresses and correspondence in the private working packet; shared examples
use synthetic data. Record unknown confession as unknown rather than assuming it from nationality.

Retain the standard research-log columns in this order:

```text
Date | Repository | URL / Call # / Microfilm # | Research question / what searched for | Locality | Source citation | Results / Comments / Analysis | Document number
```

Log each search, its exact parameters and the collection's relevant place/date coverage. Use
`NIL` for a completed search with no hits. Label inaccessible images, interrupted queries and
unsearched collections separately; they are not completed negative searches.

## Five workflows

### 1. Bound the movement before searching for a ship

Start in the documented destination household. Extract dated appearances from censuses, vital
records, directories, naturalization papers and children's records. Separate an event date from
the later record's reporting date. A child born abroad is a lead to family movement, not proof that
every household member traveled together. [S4]

Make one chronology row per reported or documented movement. Preserve every reported immigration
year with its source, then identify the interval supported by the dated appearances. Keep conflicting
arrival dates visible. A later return, a child's separate arrival and an onward crossing are separate
events, not corrections to one universal immigration date. [S1, S5]

For a U.S. citizenship clue, find the issuing court and retrieve the declaration and petition, plus
attached arrival evidence when present. The stages can be in different courts. Before September 27,
1906, municipal, county, state and federal courts could naturalize; a NARA miss does not exhaust
local court holdings. Later records also require checking the actual court and repository. [H2]
Do not expect every emigrant, wife or child to have a separate naturalization packet.

**Artifact — movement chronology:**

```text
event_id | person_handle | event_type | event_date_as_recorded | reporting_date | origin_as_written | destination_as_written | record_id | identity_link_basis | uncertainties
```

**Checkpoint:** the ship search has a sourced date interval and plausible route, or a specific
unknown to resolve. Distinguish `departed`, `arrived`, `admitted`, `returned` and `intended
destination`; the last does not establish settlement.

### 2. Recover an arrival record when the name search fails

Use a collection for the plausible arrival port and period. Check its description and gaps before
adding more name filters. U.S. passenger records are arranged by arrival port; New York is one
route, not the default for every Russian Empire emigrant. [H1]

Run a short, logged ladder:

1. Search the documented name variants with the chronology's date interval. Leave an uncertain
   birthplace or nationality filter off the initial searches.
2. Search a spouse, child or documented fellow traveler using their own recorded variants. A
   community case recovered the family list through a child's alternative spelling. [S3]
   Use [beider-given-name-variants.md](../../genealogy-research-recipes/recipes/beider-given-name-variants.md)
   for supported Jewish given-name variants; keep generated guesses separate.
3. If the database supports it, search the known U.S. contact's name or address. Otherwise inspect
   that contact's appearances in candidate manifests manually. The contact can locate the traveler
   without being a passenger on that voyage. [S7]
4. Try another index of the same collection and compare the images. A new provider's hit does not
   make a second independent record. If a ship/date is known, browse its arrival list and relevant
   passenger sections rather than repeating the same failed name query. [S2, S4]

For a Canadian route, distinguish **arrival in Canada** from **admission to the United States**.
Follow a U.S. border index/card's ship, port, date and record references to the linked manifest;
“St. Albans” can describe the record system rather than the traveler's crossing town. U.S.-bound
passenger lists made at Canadian seaports omit passengers who declared a Canadian destination. [H3]
Consult Library and Archives Canada's matching port/year records as well. When a 1919–1924
arrival involved Canadian immigration or a stay beyond direct U.S. transit, include LAC's Form 30A
branch; absence from its ordinary passenger-name index does not exhaust that record type.
Passengers in transit directly to the United States were not required to complete Form 30A:
prioritize U.S. Canadian-seaport/border records and do not treat a missing form by itself as a
record gap. [H3, H4, H7]

**Artifact:** research-log rows and a candidate list:

```text
candidate_id | person_handle | collection | query_or_browse_scope | ship | arrival_port | arrival_date | record_locator | corroborating_details | conflicts | next_check | status
```

Use `unresolved`, `linked-to-target` or `excluded-with-reason` as statuses. Preserve a usable
locator and rationale for each decision. **Checkpoint:** a candidate is linked through the
household/chronology evidence, or the next unresolved search branch is named. A name-only hit
stays unresolved.

### 3. Extract the complete arrival record, including its outcome

Save the full image, ship header and any continuation page required by the form. On a two-page
manifest, pair the correct halves by heading, passenger line number and surrounding names; the
next displayed image is not sufficient evidence that the halves belong together. Look for linked
detention or special-inquiry lists and preserve the passenger reference. Forms and passenger
classes differ, so transcribe the headings actually present. [S1, S2, H5]

Keep both the index spelling and your reading of the image. Preserve uncertain letters and line
references. Read the birthplace, last residence, citizenship/nationality, relative left behind and
destination contact as distinct fields. A port of embarkation is another field; it does not identify
the birth town. [S1, S2, H1]

Transcribe annotations before interpreting them. Consult Marian L. Smith's annotation guide for
the marking's position and form, including cross-references, detention and special inquiry. A
crossed-out line or inspection entry alone does not establish admission, deportation or a name
change. If the outcome record is missing, record `outcome unresolved`. [H5]

**Artifact — arrival extraction:**

```text
record_id | person_handle | collection_and_locator | ship_and_voyage_date | page_and_line | name_in_index | name_read_from_image | age_as_written | birthplace_as_written | last_residence_as_written | nationality_as_written | origin_contact_and_relationship | origin_contact_address | destination_contact_and_relationship | destination_contact_address | prior_visits_as_written | annotations_and_cross_references | outcome_evidence | image_files | unreadable_or_absent_fields
```

Write `field not on form`, `blank` and `unreadable` distinctly. **Checkpoint:** each extracted
field points to the correct image/page/line; every continuation or linked-list gap has a recorded
follow-up. Do not overwrite a missing birthplace with the last residence.

### 4. Follow the two contact leads and the traveling group

Make separate worklist rows for the relative or friend left behind and the person being joined.
Record the relationship exactly as written. Search the destination contact's household, address
and citizenship records for origin clues. Search later-arriving relatives and fellow travelers for
clearer locality wording, using the chronology to test whether they belong to the same family
network. [S1, S3, S4]

When the direct traveler has only “Russia” in the birthplace field, a sibling's full arrival or
naturalization record can supply a locality lead. Preserve the documented sibling relationship
and the sibling's own place role: their birthplace is not automatically the target's birthplace.
For destination/return newspaper searches, use the specific retrieval loops in
[newspapers-com-search-recovery.md](../../genealogy-research-recipes/recipes/newspapers-com-search-recovery.md).
For an obscured relative's birthplace or parentage, request the record that distinguishes the
possibilities rather than collecting unrelated people with the surname.

**Artifact — contact worklist:**

```text
lead_id | source_record_and_line | person_handle_or_unidentified_name | role_on_record | relationship_as_written | place_and_address_as_written | related_record_ids | locality_clue_and_its_role | conflicts | next_record | status
```

**Checkpoint:** each promising town clue has its person, source, geographic role and next check.
Keep an unidentified contact unidentified. Shared ship, address, cemetery society or hometown
guides a search; none supplies a parent-child link by itself.

### 5. Resolve the locality and hand off to the holding archive

List plausible towns for the raw place string. Separate candidates by coordinates, dated
jurisdiction and nearby places. “Russia” or “Poland” can be the jurisdiction reported at the event
or reporting date; resolve the locality before selecting a modern country's archive. For Jewish
localities, the JewishGen Communities Database supplies historical names/jurisdictions, including
Yiddish variants. Its omission of a village does not show that no Jews lived there; use its Gazetteer
and relevant historical gazetteers/maps for additional candidates. [S6, H6]

Use [jewishgen-search-family-reconstruction.md](../../genealogy-research-recipes/recipes/jewishgen-search-family-reconstruction.md)
for the Jewish place/name search ladder. For every confession, identify the register jurisdiction
or parish serving the event, then verify its surviving years and actual holding repository. Record
registration society separately from residence or birthplace; use
[russian-empire-jewish-identity-attribution.md](../../genealogy-research-recipes/recipes/russian-empire-jewish-identity-attribution.md)
when imperial Jewish registration or household placement is the unresolved issue.

**Artifact — competing localities:**

```text
locality_id | raw_place_string | place_role | candidate_name_and_variants | coordinates | historical_jurisdiction_and_date | modern_country | confession_and_register_catchment | supporting_record_ids | contradicting_record_ids | next_discriminating_record | status
```

For a synthetic example, `R1` says birthplace “Russia,” last residence “Town A,” and mother at
“Town B.” Put those in three role-specific rows. A later petition naming “Town C” creates a birth
candidate to investigate; it does not erase the Town A residence or Town B contact address.

Prepare a handoff with the person's recorded names, requested event/year interval, the
role-specific locality evidence, confession or its unresolved status, citations and image
locators. Add the current archive/catalog reference, surviving coverage and access status.
Keep archive fund/inventory/file references and a FamilySearch film/DGS identifier in separate
fields; record a documented mapping between them when available.

**Artifact — archive handoff:**

```text
person_handle | requested_event_and_years | name_variants_with_record_ids | birthplace_evidence | residence_evidence | registration_evidence | locality_candidates_and_decision_basis | confession_and_register_jurisdiction | holding_repository | fund_inventory_file | film_or_DGS | coverage_checked_and_date | access_status | requested_record_or_next_resolving_record | packet_record_ids
```

**Checkpoint:** the handoff names a supported repository/record series to search, or the precise
record needed to choose between towns. If two towns remain viable, send the competing candidates
and discriminating question. Do not issue an archive request as though the locality were settled.
The 1811 revision-list technique for earlier internal resettlement is a separate task; it is not
the starting record for an 1880–1924 overseas departure.

## Delegation boundary

An assistant can transcribe with uncertainties, normalize a working copy, build these tables and
propose the next discriminating search. Check its readings against the original images using
[ai-for-documentary-records.md](../../genealogy-research-recipes/recipes/ai-for-documentary-records.md).
The researcher owns identity decisions and the archive handoff's locality conclusion. Keep current
access requirements in the log rather than promising delivery times, fixed A-file eligibility or
one access rule for every successor country.
