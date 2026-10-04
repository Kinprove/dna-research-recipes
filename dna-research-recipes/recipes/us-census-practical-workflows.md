# Practical U.S. census workflows

Use these procedures to recover households, browse a bounded district, extract year-specific
fields, or produce a comparison artifact. Preserve the original census locator and keep
literal observations separate from calculations and proposed identities.

Keep a wider research plan, query log and report alongside these census working records.
Use [Ancestry search recovery](https://github.com/Kinprove/dna-research-recipes/blob/main/dna-research-recipes/recipes/ancestry-record-search-recovery.md)
or [MyHeritage record search](https://github.com/Kinprove/dna-research-recipes/blob/main/dna-research-recipes/recipes/myheritage-historical-record-search.md)
for provider-specific search controls. This recipe supplies the census working records.
Route identity, kinship and negative-evidence rulings to
[evidence and proof judgment](https://github.com/Kinprove/dna-research-recipes/blob/main/dna-research-recipes/recipes/evidence-proof-judgment.md).

## Preserve the output schema

Each procedure below produces the corresponding table. These column orders are this
recipe's proposed packaging of the source methods; the sources do not prescribe these exact
schemas. Keep a literal value alongside any interpretation. An unavailable value stays
unknown rather than becoming zero, false, or a guessed name.

Every `source_locator` or entry locator carries:
`census_year, schedule_type, state, county_as_recorded, locality_as_recorded,
enumeration_district_if_present, printed_sheet_or_page, line_numbers,
viewer_image_number, record_url_or_repository_locator, accessed_at`.
Keep fields unavailable on that schedule explicitly unknown. A viewer counter and a
printed sheet/page number are separate fields.

| Procedure | Fixed column order |
| --- | --- |
| 1: query log | `search_id, census_year, collection, member_anchor, query_text, filters, searched_at, result_status, candidate_locator, image_reading, identity_conflicts, next_action` |
| 2: location and browse log | `location_id, target_year, observed_address_or_property, observation_date, location_source_locator, historical_jurisdiction, target_year_ed, map_or_description_locator, boundary_reason, browse_image_range, browse_sheet_range, gaps, outcome` |
| 3: revisit link | `district, original_locator, original_line, reference_literal, revisit_locator, revisit_line, link_evidence, result_status` |
| 4: literal counts | `candidate_id, census_year, census_reference_date, source_locator, column_label, lower_age, upper_age, upper_bound_inclusive, recorded_count, classification_literal, overlap_note` |
| 4: proposed assignments | `candidate_id, census_year, proposed_person_id, compatible_column, birth_interval, independent_person_evidence, assignment_status, conflict, next_record` |
| 5: coverage | `record_type, jurisdiction, actual_years, repository_locator, access_status, search_performed, searched_at, result, remaining_gap` |
| 5: timeline | `person_or_household, observation_date, locality_as_recorded, event_or_residence_literal, source_locator, jurisdiction_change_note, unresolved_link` |
| 6: supplement or note | `person_as_recorded, source_locator, person_line, question_heading, field_status, answer_literal, supplement_line_or_note_reference, interpretation, unresolved_subject` |
| 7: event lead | `person_as_recorded, census_year, source_locator, field_heading, reported_value, calculation, derived_search_window, proposed_event, conflict, corroborating_locator, next_search` |
| 8: mortality entry | `person_as_recorded, source_locator, death_month_literal, stated_reporting_window, inferred_death_year, inference_basis, household_reference_literal, population_locator, identity_comparison, conflict` |
| 9: identity chain | `candidate_link_id, earlier_person_literal, earlier_locator, later_person_literal, later_locator, surname_observations, household_comparison, corroborating_document_locator, enslavement_evidence_status, link_status, next_record` |

For search and coverage outcomes distinguish `not_searched`, `searched_no_candidate`,
`candidate_found`, `inaccessible`, `incomplete`, and `illegible`.
For extracted answers distinguish `answered`, `explicit_no`, `blank`, `not_asked`, and
`unreadable`. A blank is not an explicit negative.

## Choose a recipe

| Problem | Recipe | Deliverable |
| --- | --- | --- |
| A household disappears from name searches | 1. Change the search anchor | Query log and candidate households |
| You know a location but cannot find the family | 2. Address to enumeration district | Map-backed district list and browse log |
| A 1950 entry says nobody was home | 3. Follow the revisit reference | Linked original and revisit entries |
| Most household members are unnamed | 4. Reconstruct age-bin constraints | Household matrix with explicit hypotheses |
| The 1890 gap interrupts the family | 5. Build a substitute-record timeline | Coverage table and dated residence timeline |
| An index omits extra census information | 6. Read supplements and notes | Person-linked supplementary extraction |
| You need missing children or a marriage period | 7. Extract family-event leads | Event hypotheses and targeted record searches |
| Someone may have died before enumeration | 8. Search mortality schedules | Death-window and household correlation |
| A formerly enslaved family changes surnames | 9. Track the family group | Candidate identity chain across censuses |

## 1. Recover a missing household by changing the search anchor

**Use when:** Searching the expected surname or head of household produces no plausible result.

**Inputs:** A household roster from another record; first and middle names; approximate ages; birthplaces; and independently supported locations.

1. List every expected member. Mark which names, ages, and birthplaces are best supported. Include children: their entries may be easier to recognize than the adults' entries.
2. Search each member separately in the target census. Then remove the surname from a distinctive member's query, keeping given name, age range, birthplace, and a supported search area.
3. Try a short name fragment or wildcard where the platform permits it. Change one constraint at a time and record the actual query. An unsuccessful surname search is a failed query, not evidence that the household was absent.
4. Extend the locality using relatives' marriages, residences, or other dated evidence. Do not restrict a missing household to the location where it appeared ten years earlier.
5. Open candidate images. Compare the whole roster, ages, birthplaces, and local associates. Record indexed spelling and the image reading separately. Search the apparent alternative surname locally before dismissing it as a transcription error.
6. If name searches remain unproductive, use Recipe 2. A second platform can expose a different index, but two indexes of the same census entry remain one underlying record.

**Output:** A query log containing census year, collection, query, filters, result, candidate image citation, and identity conflicts.

**Checkpoint:** Retain a candidate only after household-level comparison. A matching child or unusual first name nominates a household; it does not establish everyone's identity or relationships.

**Example prompt:** “Using this known household roster, propose an ordered census search matrix. Include searches through children, surname-free searches, and locations supported by the attached records. Keep candidate identities separate from confirmed identities.”

**Method origin:** Family Locket's case found a household through a child's given names, age, and birthplace after searches for the parents and surname failed. It also demonstrates wildcard searching and extending the locality through siblings' records. [S1](https://familylocket.com/3-tips-for-searching-the-census-when-a-family-goes-missing/)

## 2. Turn an address into an enumeration-district search

**Use when:** The index fails, or you want to inspect the actual neighborhood.

**Inputs:** Census year; a dated address or rural location; the historical jurisdiction; and nearby streets, landmarks, or property descriptions.

1. Assemble location evidence close to the census date: city directories, draft registrations, letters, school records, vital records, or other dated documents. Keep an address from a different year as a lead until supported for the target year.
2. Identify the county and locality as they existed in that year. Check boundary changes before interpreting a different county name as a move.
3. Locate enumeration-district maps and descriptions for the target census. Family Locket demonstrates using Steve Morse's One-Step resources to reach archival maps. Compare the address or property with streets and landmarks; retain every district consistent with the evidence.
4. Browse the district's population-schedule images. Record image numbers and the sheet/page numbers printed on the schedules separately. Inspect continuation pages and later sections, following any cross-references.
5. Keep a browse log: district, range inspected, street or landmark encountered, candidate households, and gaps. If the location lies near a district boundary, inspect the plausible neighboring district too.
6. Save the map or description citation alongside the census citation so another researcher can reproduce why this district was selected.

**Output:** An address-evidence table, map-backed district list, and page-browse coverage log.

**Checkpoint:** Never carry an enumeration-district number into another census year without checking that year's map. Similar numbers do not establish identical boundaries. An image-only collection also needs a browse search; a name-search failure does not cover it.

**Example prompt:** “Given these dated addresses and this target-year district map, list all plausible districts and explain the boundary evidence. Produce a page-browse log template without assuming the family stayed at its earlier address.”

**Method origin:** Family Locket demonstrates locating an Idaho household through rivers, roads, railways, and target-year maps; Who Are You Made Of explains changing district boundaries; Genealogy TV demonstrates finding census maps in image-only holdings. [S12](https://familylocket.com/rlp-191-preparing-for-the-1950-u-s-census-release/), [S15](https://whoareyoumadeof.com/blog/what-is-an-enumeration-district-on-the-census/), [S3](https://www.youtube.com/watch?v=1ectqP9Ogys)

## 3. Recover a 1950 household from the revisit sheets

**Use when:** A 1950 entry says nobody was home or directs you to another sheet.

**Inputs:** The original entry, district, printed sheet number, line number, and any handwritten cross-reference.

1. Read the entire entry, including the margin. Transcribe its sheet-and-line reference exactly.
2. Follow that reference within the same district. Amy Johnson Crow's demonstration follows an entry to sheet 71, line 12, even though the viewer contains only 24 images. The image counter and the printed sheet number use different numbering systems.
3. If no complete reference is visible, inspect the district's later sheets for the revisit section. The demonstrated revisit numbering begins at sheet 71; inspect printed headings rather than requesting viewer image 71.
4. Compare the revisit household's address, names, and other identifiers with the original entry. Save citations to both entries and explain the link.
5. If an image is blurred, covered, or folded, inspect nearby images for a repeated exposure before recording it as unreadable. Record an access or legibility gap if no usable exposure is found.

**Output:** A linked pair of citations and the completed household extraction.

**Checkpoint:** “Nobody home on the first visit” does not establish that the household was omitted. A later entry must still be linked by its reference or other identifying evidence.

**Example prompt:** “Transcribe this entry's revisit reference. Tell me which printed sheet and line to locate, distinguish them from the viewer image number, and list what must match before linking the two entries.”

**Method origin:** Amy Johnson Crow's worked example explains revisit sheet 71, the 24-image discrepancy, and looking for repeated photographic exposures. [S18](https://www.youtube.com/watch?v=4p_afzX34Uk)

## 4. Use pre-1850 age bins as constraints on candidate households

**Use when:** The relevant schedule names a household head but leaves most other people as counts in categories.

**Inputs:** Complete schedule images and headings; the census reference date; independently known family members; and all plausible heads with the same name.

1. Transcribe every relevant column from the image, including its exact age bounds and historical classification. Keep categories separate. Do not reconstruct the household from the indexed totals alone.
2. Build a matrix with one row per candidate household and one column per printed category. Read the headings afresh for each census year rather than reusing another year's bins.
3. Convert age categories into possible birth-date intervals. This calculation assumes the reported category is accurate. For an inclusive age range `a` through `b` at reference date `D`, the interval is `(D minus (b + 1) years, D minus a years]`. Interpret headings such as “under” or “of ... and under ...” literally.
4. Place independently known people into compatible bins as **hypotheses**. Preserve unmatched counts. Household membership does not automatically establish parentage, marriage, or sibling relationships.
   Use stable hypothesis IDs across census years. Within each mutually exclusive category,
   proposed assignments must not exceed its recorded count; preserve the unassigned remainder.
   Keep overlapping columns separate rather than treating them as independent capacity.
5. Compare candidate heads across adjacent censuses and other records. Track recurring associates and historical jurisdictions. Reject a candidate only for an evidenced conflict, not a surname preference.
6. Investigate a missing expected adult through alternate names, adjacent locations, property records, or another enumeration. Keep error, absence, and separate residence as distinct explanations.

**Output:** The literal count matrix, proposed person-to-bin assignments, conflicts, and next records needed to test each assignment.

**Checkpoint:** A compatible age bin supports a candidate household. It does not name the unnamed person. Check whether any columns overlap before summing totals.

**Example prompt:** “Create separate literal-count and hypothesis tables from these schedules. Use the printed age bounds, compare all same-name heads, and identify the documents needed to test each proposed assignment.”

**Method origin:** Family Locket demonstrates checking image tick marks, distinguishing same-name heads, following associates, and investigating a head found separately under another name. The interval formula and matrix schema above are analytical adaptations. [S4](https://www.youtube.com/watch?v=oBkEoVQtPcQ)

## 5. Bridge the 1890 gap with a coverage table and dated timeline

**Use when:** The missing population schedules interrupt a family between 1880 and 1900.

**Inputs:** The 1880 and 1900 households; intervening locations; historical county boundaries; and repository or collection descriptions.

1. Compare both households member by member. List people who disappeared, appeared, married, changed names, or changed recorded location. Keep each unexplained change as a separate research question.
2. Check whether surviving 1890 population fragments cover the locality. Check veterans' schedules separately when relevant; they have their own geographical and subject coverage.
3. Build a coverage table for state, territorial, local, and school censuses, directories, tax records, vital records, deeds, probate, newspapers, and other dated records. Record actual years and jurisdictions held rather than copying a broad database title.
4. Search for non-federal censuses between the two federal dates. If no state census is known, investigate municipal, township, county, or other local enumerations. Search library catalogs and finding aids when an online index is absent.
5. Add dated residence observations to a timeline. Check whether changed county boundaries explain apparently different locations. Search married children separately under supported names.
6. Reconcile the timeline with the 1880 and 1900 households. Record searches that remain incomplete because records were inaccessible, unindexed, illegible, or outside the reviewed coverage.

**Output:** A table of record type, jurisdiction, actual years, repository, access status, search performed, and result; plus a dated family timeline.

**Checkpoint:** A missing federal census does not imply a record-free decade. A directory can provide residence evidence without listing every household member, and a veterans' schedule is not a replacement population census.

**Example prompt:** “Using these two households and collection descriptions, create an 1880–1900 coverage plan. Distinguish records searched, records known but inaccessible, and records whose survival has not been established.”

**Method origin:** Sara Cochran discusses fragments, veterans, school censuses, directories, family reconstruction, and boundary changes. James Tanner demonstrates state and local census discovery and library searches. [S20](https://www.youtube.com/watch?v=NmtuDJBE5eQ), [S21](https://www.youtube.com/watch?v=DYAVc-ih68g)

## 6. Extract supplementary answers and enumerator notes

**Use when:** A standard index or household crop seems to contain too little information.

**Inputs:** The full 1940 or 1950 sheet, household line numbers, and adjacent images where an entry continues.

1. Read the whole sheet, including the top, bottom, margins, and any continuation. Record the form and printed headings actually present.
2. For each household member, check whether the line is designated for supplementary questions. Match the person to the supplementary section by its printed line number.
3. Transcribe each answer with the question it answers. Do not apply a supplementary answer to every person in the household.
4. Resolve note numbers and written line references. Attach a note to the indicated entry or field. Notes can explain revisions, unusual ages, employment details, or why an entry was struck through.
5. Keep blanks, unreadable text, questions not asked, and explicit negative answers distinct. Record uncertainty about the note's subject instead of assigning it by proximity.

**Output:** A person-linked extraction containing question, literal answer, sheet/line, supplement or note reference, interpretation, and uncertainty.

**Checkpoint:** Use the markings on the actual form. Amy Johnson Crow demonstrates a 1950 sample-line-4 example, so a summary listing only other sample lines is incomplete. A crossed-out entry needs its associated note before interpretation.

**Example prompt:** “Extract this household, its marked supplementary questions, and every linked note. Preserve the person-to-line mapping and distinguish blank, unreadable, not asked, and explicit no.”

**Method origin:** Genealogy TV demonstrates matching a 1940 person to the bottom section. Amy Johnson Crow demonstrates a 1950 sample-line-4 entry and separately discusses locating and linking enumerator notes. The note transcript is incomplete, so specific biographical details from its examples are not adopted. [S7](https://www.youtube.com/watch?v=JJY4EKK_sVg), [S19](https://www.youtube.com/watch?v=jA10V_GJcio), [S8](https://www.youtube.com/watch?v=ZzrQQz4BIT4)

## 7. Turn 1900 and 1910 family fields into targeted searches

**Use when:** You need a marriage period, missing children, or evidence that a household combines more than one family.

**Inputs:** Full household images from multiple censuses, literal relationship fields, reported marriage duration or status, and children-born/children-living fields where present.

1. Extract the reported fields without normalizing discrepancies. Include relationships to the head exactly as recorded. A list of co-residents in an 1850 or 1860 population schedule does not supply the relationship column introduced in 1880.
2. Derive a marriage-period lead from reported duration. Compare multiple enumerations and retain disagreement. A subtraction such as census year minus reported married years is an approximate search lead, not an exact marriage date.
3. Inspect indications of previous marriages using the relevant form headings and instructions. Do not assume every duration or child count refers only to the couple shown together.
4. Where both child counts are legible, calculate `reported children born minus reported children living`. Treat the result as a reported difference requiring investigation. Do not create named deceased children from it. A living child absent from the household may be living elsewhere.
5. Search for missing people through surrounding households, marriages, deaths, cemetery records, probate, and other suitable records. Compare the resulting candidates with the original households.
6. Store literal statement, calculation, proposed event, and supporting record in separate fields. Keep immigration and naturalization statements as leads to the relevant documentary records rather than exact events established by the census alone.

**Output:** A family-event hypothesis table and specific follow-up searches.

**Checkpoint:** Do not infer biological relationships from co-residence or assign a woman's reported child count to the current husband without evidence. Unreadable or missing counts do not become zero.

**Example prompt:** “Compare these households. Separate literal fields from calculated marriage-period and missing-child leads. Identify prior-marriage questions and name the records needed to resolve them; do not invent relatives.”

**Method origin:** Ancestry's worked comparison produces differing approximate marriage years from successive censuses. BlackProGen discusses children-born/living fields and previous marriages. MyHeritage explains the relationship column and immigration fields. [S6](https://www.youtube.com/watch?v=cMrTbAj5YN0), [S10](https://www.youtube.com/watch?v=Ejmjf550pHc), [S13](https://education.myheritage.com/article/the-u-s-census-tracing-your-family-in-census-records/)

## 8. Use mortality schedules with the correct death window

**Use when:** A death may fall shortly before a census, especially where civil death registration is limited.

**Inputs:** Candidate name variants, residence, approximate death period, household information, and the schedule's stated coverage.

1. Establish that mortality schedules survive for the relevant year and locality. Inspect the collection's actual contents, not just its broad title. Investigate archival holdings if online coverage excludes the locality.
2. Read the schedule's reporting window. In Amy Johnson Crow's 1850 example, it covers 1 June 1849 through 31 May 1850. A September death in that reporting window belongs to 1849.
3. Search name and locality variants, then compare age, birthplace, occupation, and other recorded details.
4. Where a mortality entry supplies a household or family reference, follow it into the corresponding population schedule. Compare the surviving household; do not assume an identical name identifies the deceased.
5. Preserve literal death month, inferred calendar year, stated reporting window, and identity reasoning separately. Retain any conflict with other death evidence.

**Output:** A cited death-window extraction and any supported link to the population household.

**Checkpoint:** Do not assign the census year automatically to a reported death month. An online collection's absence of a locality is a coverage limitation, not evidence that the person did not die there.

**Example prompt:** “Interpret this mortality entry using its stated reporting window. Separate literal month from inferred year, follow any household reference, and evaluate the identity without relying on name alone.”

**Method origin:** Amy Johnson Crow demonstrates the reporting-window calculation, household-number correlation, and checking state coverage before searching. [S9](https://www.youtube.com/watch?v=sZ1kgZLY1V0)

## 9. Track a formerly enslaved family through changing surnames

**Use when:** You have a post-emancipation household, but surname continuity is uncertain.

**Inputs:** A supported household, multiple census images, ages, birthplaces, associates, and named documentary records relevant to the family.

1. Extract the whole supported household and local associates. Make a separate list of literal surnames and spelling variants for each census.
2. Search other household members under given names, approximate ages, and birthplaces. Compare family-group composition across 1870, 1880, and 1900 where the people could still be living.
3. Investigate a surname change without requiring the family to use an alleged enslaver's surname. Keep each proposed link as a candidate until corroborated.
4. Use age and household continuity to generate searches in named post-emancipation records, such as voter registrations, and appropriate records that can identify enslaved people or establish family links.
5. When examining unnamed entries in slave schedules, record the literal demographic information and its context. An age/sex match does not name a person or establish a family.
6. Keep documentary enslavement evidence separate from census race, birthplace, age, and surname observations. A 1900 census profile alone does not establish enslavement or identify an enslaver.

**Output:** A candidate identity chain, household comparisons, surname observations, and the documentary evidence needed for each unresolved link.

**Checkpoint:** Do not attach an unnamed slave-schedule entry or an enslaver to a person solely through matching surname, age, or locality. Keep free status and unknown status open where the documents do not resolve them.

**Example prompt:** “Compare these households while allowing surname changes. Rank proposed person links using the entire family group, keep slavery-status claims separate, and specify what named records would establish each link.”

**Method origin:** Family Locket explicitly discusses surname changes, family-group and age comparison, voter registrations, and the limitations of slave schedules. Its dataset announcements are not treated as currently verified access instructions. [S11](https://familylocket.com/tracing-the-enslaved-in-the-1900-u-s-census-and-enslaved-org-project/)
