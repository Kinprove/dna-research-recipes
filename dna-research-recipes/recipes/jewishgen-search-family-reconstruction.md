# Recipe: JewishGen searches that recover families missed by a name-and-town query

## Goal

Turn an unsuccessful JewishGen search into a sequence of discriminating queries. Recover competing family candidates without assuming a fixed surname, a literal name match, one town, one birth year or a known husband. This recipe owns retrieval and comparison; identity and relationship rulings belong to [evidence-proof-judgment](evidence-proof-judgment.md) and [Russian-Empire identity attribution](russian-empire-jewish-identity-attribution.md).

## The matching unit comes before the query

Read the target collection's instructions: what is searchable, whose name each field represents, whether matching returns individuals or households, which years and populations are included, and how to reach the original. Unified Search is an entry point; preserve the collection name behind each result.

Three documented traps change how a result must be read:

- **Exact does not always mean literal.** Production Unified Search expands some given-name and town synonyms even under Exact. Record both the submitted form and the returned form. [Unified Search](https://www.jewishgen.org/databases/all/).
- **AND does not always mean the same person.** In Belarus Revision Lists, surname and given-name conditions can be satisfied by different members of one household. Inspect individual rows before treating the conjunction as a person's identity. [Belarus search instructions](https://www.jewishgen.org/databases/Belarus/BelarusRevisionLists.htm).
- **A participant is not necessarily the record subject.** A birth's father field ordinarily describes the child's father; it is not automatically the mother's father. To find a woman as a mother, use the collection's maternal fields or inspect a broader extract. Verify labels before composing the query.

## A query ladder, with an explicit reason for every change

Save the broad results first. Apply one new constraint at a time and compare what disappeared; retain that rejected set for checking filter effects. These are query plans, not universal UI or CLI commands. Use only methods offered and documented for the selected database.

| Problem | Next search | What it tests |
| --- | --- | --- |
| Known surname, uncertain spelling | Exact; Phonetically Like; Sounds Like in separate passes | Literal/synonym behavior versus two phonetic candidate sets |
| Stable beginning, changing ending | Starts With on the bare stem | Suffix and transliteration variants; do not append an invented wildcard |
| Uncertain beginning, stable internal fragment | Contains when supported, or a documented wildcard query | Prefix loss or an internal spelling fragment |
| One or two suspect letters | Fuzzy, then plausible transcription variants | Edit-distance errors versus a different naming form |
| Double given name | Both components separately; full forms in both orders | An omitted component or reversed order |
| Two words might be given name plus patronymic | Search both parses separately | A compound name misread as two generations |
| Father known, surname unknown | Given-name variants plus the collection's father/patronymic field; omit surname | Alternative family surnames or missing surnames |
| Expected town produces nothing | Remove Town; search the town in Any Field where available | Origin, residence or transfer recorded outside the indexed Town field |
| No reliable surname, one small community | Bounded town/collection extract, then local name/age/household filtering | Records inaccessible through the expected name field |
| Woman disappears after childhood | Search her as mother in children's births and as wife in household lists | A married household under an unknown surname |

**Do not substitute one phonetic pass for a variant matrix.** Hungarian census instructions distinguish Phonetically Like (Beider–Morse), Sounds Like (Daitch–Mokotoff) and fuzzy (Damerau–Levenshtein). Belarus instructions specifically warn that Chaia will not retrieve Khaika through the phonetic methods. Diminutives, religious/secular forms and double-name components need explicit passes. Build the matrix from attested name forms, preserving the source for each variant. [Hungarian methods](https://www.jewishgen.org/databases/Hungary/CensusOther.htm), [Belarus given names](https://www.jewishgen.org/databases/Belarus/BelarusRevisionLists.htm).

**Do not improvise Boolean or wildcard syntax.** Production Unified Search documents comma as OR and space as AND. A multiword name is therefore not automatically a literal phrase. Wildcard availability varies: the Anglo-Jewry 1851 instructions permit `*` and `?` under Is Exactly, while Starts With uses a bare beginning. Check the chosen interface before reusing either convention. [Unified Search](https://www.jewishgen.org/databases/all/), [1851 search instructions](https://www.jewishgen.org/jcr-uk/1851/How_to_use_the_Database.htm).

Keep an actual query ledger: database, access path, fields, methods, Boolean relation, date, result status/count and reason for the next query. A listed query that was never executed is a plan. If using a search tool or CLI, read its current documentation, inspect the returned datasets and applied filters, and preserve partial-result or authentication errors; unsupported or ignored filters cannot certify a negative.

### Mixed-field batches to try

These combinations are retrieval plans, not results from completed searches. Use separate methods per field only where the interface supports them; otherwise split the passes and compare the remaining values locally. Begin without an age or Town restriction when those are uncertain.

| Batch | Combination with AND | Purpose |
| --- | --- | --- |
| A | Surname Phonetically Like + Given Name Starts With | Variable surname spelling and a stable beginning of the given name |
| B | Surname Starts With + Given Name Sounds Like | Stable surname stem and several given-name spellings |
| C | Surname Sounds Like + Any Field exact/text place | A spelling variant with a geographic mention outside the main locality column |
| D | Given Name Sounds Like + supported father/patronymic field Exact | Unknown surname, relatively secure paternal-name form |
| E | Given Name Exact + supported father/patronymic field Phonetically Like | Secure given-name form, variable paternal-name spelling |
| F | One component of a double name + supported father field; repeat with the other component | An omitted or misparsed component without treating the words as a literal phrase |

For D–F, verify whose father the field represents. For every batch, inspect which actual person supplied each match; the household-level AND trap still applies. Union the candidates from A–F and deduplicate by source record reference, not normalized name. Tighten a field only after checking that an already known row survives that constraint.

## Geography has several roles

Maintain separate columns for registration, residence, event location, birthplace/origin and a place mentioned in comments. Belarus revision-list Town can be registration rather than residence. GeneaVlogger's 2025 demonstration retrieves an Odessa record whose ancestral town appears in comments. That displayed position does not establish whether Town searching includes it: JewishGen permits hidden Other Towns columns for indexing embedded place names. Compare **surname + Town place**, **surname + Any Field place** and **surname without Town**, then inspect the place role and the difference between returned rows. [Belarus Town instructions](https://www.jewishgen.org/databases/Belarus/BelarusRevisionLists.htm), [GeneaVlogger demonstration](https://www.youtube.com/watch?v=8qIa8Sij4F0), [indexing guidelines](https://www.jewishgen.org/databases/%24transcription.html).

The same indexing distinction applies to names: a surname mentioned inside free text is not automatically searchable phonetically as a surname. Hidden Other Surnames/Other GivenNames can supply that mapping. For a name in comments, compare an Any Field text query with the typed surname/name query before interpreting a negative; do not assume the collection populated those hidden fields. [Indexing guidelines](https://www.jewishgen.org/databases/%24transcription.html).

Resolve ambiguous place names with historical jurisdiction, coordinates and nearby communities before applying a geographic restriction. Communities supplies historical Jewish names and jurisdictions; Gazetteer serves a broader set of localities. For vital records, also identify the community or registration office responsible for the village: a nearby settlement can hold its registers. An administrative catchment is a different search from an arbitrary radius. [Communities/Gazetteer](https://www.jewishgen.org/Communities/), [Polish records questions](https://jewishgen.org/InfoFiles/Poland/Questions.htm).

When a record names an origin or transfer destination, pivot to that collection and its additional lists. When a family merely vanishes, leave migration, missing coverage and name changes as separate retrieval branches. Do not turn an unexecuted all-region search into a claim that the family was absent.

## Ages: choose the observation date before choosing the search window

For each age preserve **raw age; age-column heading; date that column describes; date of the individual entry; title year; event date; registration date; source reference**. Derive a birth interval only after choosing the correct observation date. If an age is exact in completed years but only the observation year is known, year minus age and the preceding year are candidate birth years. Approximate ages require a wider, explicitly justified retrieval window. Never turn one estimated year into an initial veto or average contradictory ages into a fictional birthday.

Check these mechanisms before proposing intentional falsification:

1. **Previous versus current revision age.** Bessarabian revision-list documentation exposes both fields; the previous-revision age is described for men. J-Roots 1107 raises confusion between those columns as a possible translation error. Compute each against its own year. [Bessarabia schema](https://www.jewishgen.org/Bessarabia/files/databases/BessarabiaRevisionListsIntroduction.pdf), [J-Roots 1107](https://forum.j-roots.info/viewtopic.php?f=9&t=1107).
2. **A book's title year versus a later entry.** J-Roots 4667 discusses a family list opened in 1874 and supplemented later. Another apparent female-age conflict disappears when the original entry's later date is restored. Read the dated line and marginal additions before subtracting from the cover year. [J-Roots 4667](https://forum.j-roots.info/viewtopic.php?f=4&t=4667).
3. **Event versus registration, and dual calendars.** Preserve both dates and their labels. Russian-Polish records can carry Julian and Gregorian dates; delayed registration is another mechanism. Neither justifies applying a fixed offset to every discrepancy. [Polish records questions](https://jewishgen.org/InfoFiles/Poland/Questions.htm).
4. **Documentary versus apparent age.** J-Roots 4667 describes separate columns based on previous documents and outward appearance. Their disagreement is not automatically the person's lie. [J-Roots 4667](https://forum.j-roots.info/viewtopic.php?f=4&t=4667).

**Search the later registration years too.** J-Roots 4667 reports daughters whose births were entered decades later, shortly before marriage, and siblings registered together years after their births. If a birth-year search fails, inspect later additions around a known wedding or a younger sibling's registration. Preserve the actual birth date and the later entry date; do not move the birth to the registration year. These are specific forum observations, not a frequency estimate or a universal explanation for missing births. [Delayed-registration cases](https://forum.j-roots.info/viewtopic.php?f=4&t=4667).

**Recruit evasion is a testable explanation, not an age correction rule.** Keep the recorded age intact, broaden candidate retrieval, then seek the relevant recruit/family list, marginal note or documented re-registration. A military-age male and an age discrepancy do not themselves establish a motive. For the historical mechanism and attribution sequence, use [Russian-Empire identity attribution](russian-empire-jewish-identity-attribution.md).

## Double names and ambiguous patronymics

For an attested double name such as Abram Moshe, create distinct retrieval lanes for Abram, Moshe, Abram Moshe and Moshe Abram. JewishGen's name guidance documents component omission and order changes. This is a search expansion, not a rule that any Abram and any Moshe are the same person. [Double-name guidance](https://www.jewishgen.org/infofiles/givennames/slide16.html).

When an index has two name-like tokens, retain both interpretations: **compound given name** and **given name + patronymic**. A hyphen or an indexer's suffix does not settle the parse. J-Roots 4667 demonstrates this ambiguity; 3733 shows why all children's records are useful for comparing their mother's name forms. [J-Roots 4667](https://forum.j-roots.info/viewtopic.php?f=4&t=4667), [J-Roots 3733](https://forum.j-roots.info/viewtopic.php?f=9&t=3733).

For Polish women, a name-like surname can represent the father's given name, a grammatical form of a surname, or an andronym identifying her through her husband. JewishGen gives Avram Moshe → Sara Abramówna or Sara Moszkówna: either component of the father's double name may supply the patronymic. Retain both component-derived Polish search lanes where the records warrant them. Preserve each raw form and check additional records before choosing its role. [Polish women's names, question 6](https://jewishgen.org/InfoFiles/Poland/Questions.htm).

If a metrical record has parallel Russian and Hebrew text, inspect the original names on both sides. J-Roots 4667 proposes this specifically when a woman's name changes between lists. A second language can supply another search form; it does not automatically resolve the identity or establish that the two halves agree. [Women's-name discussion](https://forum.j-roots.info/viewtopic.php?f=4&t=4667).

## A wife's natal family when the marriage entry is unavailable

This sequence generates competing families; it does not assign parents.

1. Collect her forms and ages from **all available children's births**, later household entries and death records. Record whether the father's name is explicitly written, inferred by an indexer, absent, or possibly another name role. One child's index entry must not dictate her patronymic. [J-Roots 3733](https://forum.j-roots.info/viewtopic.php?f=9&t=3733).
2. Search her given-name variants plus each supported paternal-name variant, without a presumed maiden surname. Use a justified age window and separate natal-place, registration-place and residence searches. If the necessary maternal/paternal fields are not searchable, retrieve a bounded collection and filter locally.
3. Search candidate fathers' households for a daughter with compatible forms and chronology. Compare siblings, mother, addresses, former household numbers and transfer notes. Search a brother's or sister's documented surname as a new candidate lane; keep the reason for the pivot.
4. Return a candidate table: raw names; father's-name source; age basis; place role; siblings/household; direct support; conflicts; missing link; next record that would separate the candidates. A common given name + patronymic + approximate age alone does not choose a natal family.

When those records do not name her natal family, pivot to siblings, residence/house books, a surviving work autobiography or an identified family file. J-Roots 5084 recommends these routes in a concrete missing-maiden-name question; the advice is not a reported successful identification. An alphabetic finding aid may show only a name while the underlying file contains family details. [Missing maiden-name discussion](https://forum.j-roots.info/viewtopic.php?f=20&t=5084), [citizenship-option dossiers](https://forum.j-roots.info/viewtopic.php?f=197&t=9279).

## A daughter's married household when neither husband nor married surname is known

Reverse the search role: **daughter → mother**. In collections with searchable maternal names, search births for her given-name and paternal-name variants over the relevant adult period, omitting the unknown husband/surname. Otherwise locally inspect a bounded extract with the relevant maternal columns.

Group candidate births by repeated parental pair, maternal name forms, residence and source series. Retain each competing group. Then retrieve the groups' household, later child, death or marriage records to connect the adult mother to the earlier daughter. The same maternal patronymic in two households is not a link; remarriage and homonyms remain candidates.

The strategy is a synthesis of the repeated-maternal-name case in J-Roots 3733 and the collection-specific patronymic/house-number reconstruction in Kraków's help file. It is not a published case proving an otherwise undocumented marriage. [J-Roots 3733](https://forum.j-roots.info/viewtopic.php?f=9&t=3733), [Kraków patronymic research](https://kehilalinks.jewishgen.org/krakow/kra_pathelp.htm).

**Worked field plan, not an executed search:** suppose the earlier daughter is Sora, daughter of Abram; her married surname is unknown. The documented Belarus birth schema distinguishes Mother's Given Name and Mother's Patronymic from Father's Given Name and Father's Patronymic. Retrieve a covered, bounded birth collection using supported name/place fields, then locally select maternal given-name variants Sora/Sorka and a supported Abram patronymic. Group retained rows by the child's paternal names, maternal forms and locality. Two paternal groups remain two candidate households. A hit on Father's Patronymic=Abram identifies the child's paternal grandfather and does not satisfy the mother's paternal-name condition. A displayed maternal column is not a guarantee of a dedicated search selector. [Belarus birth schema](https://www.jewishgen.org/belarus/belarus_births.html).

Before declaring the marriage missing, inspect how the original marriage index is arranged. Polish guidance describes indexes under the groom's surname, brides in later columns and some brides omitted from the index entirely. An unsuccessful bride-name query is therefore a reason to inspect the actual register or another index, rather than invent a husband. [Polish index guidance](https://jewishgen.org/InfoFiles/Poland/Questions.htm).

## Further pivots that a single person search misses

- **A household's former number is a search key.** Bessarabian revision-list documentation includes previous registration numbers and transfer/origin comments. Follow the cited earlier list rather than equating identical numbers across unrelated years. [Bessarabia schema](https://www.jewishgen.org/Bessarabia/files/databases/BessarabiaRevisionListsIntroduction.pdf).
- **No index hit does not mean no scan.** A GeneaVlogger demonstration explains that JewishGen entries can lead to FamilySearch images that may lack their own name index. Follow film/page/archive references; the demonstration does not establish the indexing status of every linked image. [Bukovina demonstration](https://www.youtube.com/watch?v=UoLx2KVd0bM).
- **A copy is not a second witness or guaranteed equivalent search.** Compare the originating regional project, JewishGen and a commercial copy by coverage and fields; do not assume their updates and algorithms coincide. This is a collection check, not a claim about today's partnership status. [Genealogy Gems interview](https://www.youtube.com/watch?v=eB5KRGKSC1M), [MyHeritage collection demonstration](https://www.youtube.com/watch?v=66schOTVGtk).
- **Coverage can exclude the person's role.** The demonstrated 1875 military collection contains men. Yizkor name indexes cover translated portions or necrologies; JOWBR requires a cemetery-coverage check. Test the relevant denominator before recording a negative. [Military example](https://www.youtube.com/watch?v=Jjie6pD0TGo), [Yizkor Names](https://www.jewishgen.org/databases/Yizkor/Names/), [Necrology](https://www.jewishgen.org/databases/Yizkor/), [JOWBR inventory](https://www.jewishgen.org/databases/Cemetery/tree/CemList.php).
- **Researcher and tree matches supply leads.** JGFF records research interests; FTJP submissions are not validated by JewishGen. Ask for the underlying record only if contact is authorized. [JGFF FAQ](https://www.jewishgen.org/jgff/FAQ/), [FTJP FAQ](https://www.jewishgen.org/gedcom/faq/search.html).
- **Repeat the saved query after a relevant indexing update.** Preserve its previous date and coverage; an expanded dataset can change the result. For an unindexed list, a town/project specialist can point to the surviving source. Contact is a separate action requiring authorization. [Ukraine indexing demonstration](https://www.youtube.com/watch?v=NsdlMwZX9yg), [Genealogy Gems interview](https://www.youtube.com/watch?v=eB5KRGKSC1M).

## Prompt-craft and output contract

> Build a JewishGen retrieval plan from the supplied records. Preserve raw names and dates. For every proposed query give collection, person's role, fields, match methods, Boolean logic, geography role and reason. Mark proposed versus executed queries. Generate competing natal/married-household candidates without assuming the unknown surname or husband. For ages identify the actual column and observation date. Return supporting rows, counterevidence, coverage gaps and the next discriminating query or original record. Do not convert a phonetic, household or age match into a relationship.

The assistant can generate variants, execute authorized bounded searches, compare extracts and prepare this table. The researcher owns name-role interpretation, any calendar conversion not checked against the document, age-falsification allegations and the final relationship ruling. Keep raw Family Finder/tree results and living-person contact details out of public artifacts.
