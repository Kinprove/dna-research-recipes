# Newspapers.com: Recover Notices That Name Searches Miss

## Goal

Recover an ancestral newspaper notice when an exact-name search fails, and distinguish a
page containing search terms from a notice that actually reports the person's event.

Use this recipe for retrieval on Newspapers.com and for resolving an alternate holding when its
coverage is insufficient. For evaluating a recovered person's
identity, use [Evidence and Proof Judgment](evidence-proof-judgment.md). For difficult
image transcription or translation, use [AI for Documentary Records](ai-for-documentary-records.md).

## Decisive rules

1. **A failed name query is a failed retrieval attempt.** It does not establish that the
   notice was never printed. Check available issues, printed naming conventions and OCR
   separately; each failure needs a different remedy. (S1, S3, S8, S10)
2. **A listed title is not complete issue coverage.** Inspect the actual dates, editions
   and pages available for the event. A title's displayed year span does not establish
   that the required issue survives or is available to you. (S3, S8)
3. **Search the identifier the newspaper would have printed.** Read nearby notices to
   learn whether that title uses middle names, initials, married names or compressed
   surname lists. Do not keep repeating the modern full name. (S2, S5, S6)
4. **Keep printed spelling separate from OCR test strings.** A letter-substitution query
   can recover an image without demonstrating that the newspaper printed that spelling.
   A human-readable name can still be unsearchable. (S1, S10)
5. **Read the notice, not just the hit.** A surname can occur in one item and a travel
   verb in another on the same page. Confirm the subject and event within the actual
   item before assigning that event to the searched person. (S4)
6. **Publication location and date describe the newspaper.** They do not automatically
   identify the person's residence or the event's date. Travel, regional circulation,
   reprints and later proceedings can move the useful notice elsewhere. (S2, S3, S6)

## Resolve a title to a holding and an issue

Use this step when Browse lacks the expected title/issue, or when a newspaper catalog gives a
promising title without accessible pages. Keep three dates separate: the newspaper's publication
span, a repository's held span and the issues you actually inspected. A title directory or a
finding-aid collection link supplies a locator, not proof that the target issue is digitized.
(S12–S14)

1. **Resolve the historical title.** Begin with the event interval, likely publication locality
   and relevant language/community. For U.S. titles, search the
   [Directory of U.S. Newspapers in American Libraries](https://www.loc.gov/collections/directory-of-us-newspapers-in-american-libraries/).
   Open each plausible title record; record its title identifier (such as LCCN), place,
   publication span and catalog URL. Follow predecessor/successor records across a title change
   and keep their identifiers separate. A newspaper that changed its name can require a
   different title record for the target year. (S12, H1)
2. **Resolve the holder and format.** Follow the title record's holdings links and the identified
   institution's catalog. For each relevant holding, record institution, holding identifier or
   call number, format, stated held dates/gaps and access route. Print, microfilm and digital
   holdings can cover different date ranges. If you use a locality-based finding aid, follow
   its collection link to the actual provider or repository before recording coverage.
   A collection-level lead stays `holding unverified` until its holdings are checked. (S13,
   S14, H2)
3. **Verify the target issue.** For a digital holding, open its issue calendar/list and then the
   required date and edition; record the pages present and what you could inspect. For a print
   or microfilm holding, prepare a bounded request or visit plan with title identifier, call
   number, format and exact dates. Record `physical issue not inspected` until the actual issue
   has been checked. A catalog's held date span alone does not settle a particular issue/page.
   Apply the OCR/name tactics below to accessible images; an access problem needs the recorded
   alternate holding or request, rather than more spelling probes. (S14, H2; authored check)

**Artifact:** one register row for each title–holding–target-issue combination:

| Field group | Record |
| --- | --- |
| Title | Title ID/URL, printed title, publication place, publication span, predecessor/successor IDs relevant to the target year |
| Holding | Repository, holding ID/call number and catalog URL, print/microfilm/digital format, stated held dates and explicit gaps |
| Issue | Target date and edition, issue/page URL or physical locator, pages present, pages actually inspected, OCR availability observed |
| Decision | Retrieval date, status, next holding/request to check and next-check date |

Use `title lead only`, `holding unverified`, `digital issue inspected`, `physical issue inspected`,
`digital issue inaccessible`, `physical issue not inspected` or `issue absent from checked holding`.
Keep a no-match search in an inspected issue separate from those coverage/access states.
If several holders cover the interval, retain separate rows so the format and access result
remain traceable.

**Stop when** each selected title has an identified holding and an inspected target issue, or an
explicit unresolved status with its next action. If the necessary issue remains inaccessible
or absent, report that boundary and proceed only with the available scope under the stopping
rules below. Once an issue is inspected, use its identifier/URL in the recovered notice's source
record; the directory record remains the locator.

The Library of Congress migrated Chronicling America on **2025-08-04**. Its title directory is
now a separate searchable collection covering newspapers in all formats; digitized newspaper
pages are in [Chronicling America](https://www.loc.gov/collections/chronicling-america/).
The 2016/2023 tutorials' old tabs and screen positions are historical examples. Use current
collection links and inspect the destination rather than reproducing those old controls. (H1)

## Search recipes

The following names, addresses and queries are invented examples, not executed searches
or reported discoveries. Quotation marks request an exact phrase on Newspapers.com.
Other examples are simple keyword inputs; they make no promise about term proximity or
Boolean behavior. Set place and publication-date limits separately. (S9)

| # | Trigger | Search or browse plan | What to inspect before using the result |
| --- | --- | --- | --- |
| 1 | Nothing appears for the expected place and date. | Use Browse to inspect titles and the actual available issues for that interval. Check competing papers and predecessor/successor titles, including small title changes such as adding Daily. (S3, S8, S9) | Is the relevant issue, edition and page present and accessible? Record a coverage gap separately from a query that returned no match. |
| 2 | A full name returns no useful notice. | Inspect naming style in a known issue. For William Richard Evans, try `"Richard Evans"`, `"W R Evans"` and a surname-only `Evans` search in a tighter place/time scope. Also try a known nickname. (S2, S6) | Are these forms actually used by the title or plausible for this person? Initial spacing and punctuation can differ; a failed exact phrase does not eliminate the initial form. |
| 3 | A woman's own full name is missing. | Try her maiden and married surnames, then her husband's name or initials: `"Mrs Robert Evans"`, `"Mrs R Evans"`. Search surname-only lists and notices about relatives when her given name is omitted. (S5, S9, S11) | Does the item identify the wife, or only a different person sharing the surname? Read compressed lists with their heading and surrounding sentences. |
| 4 | The image looks readable but the query misses it. | Test a small set of visually plausible letter confusions, such as B/E or E/C, based on the scan. Shorten an over-specific phrase or search another intact word from the expected notice. (S1, S10) | Read the original letters. Label a distorted search form as an OCR probe, not a corrected historical name. |
| 5 | A smudged target name may be in a group notice. | Search a known relative, witness, neighbor or club member who could appear in that same item; alternatively search the known club name within the relevant title/time. (S1) | Does the recovered item actually include the target? A notice about the club alone supplies context, not personal participation. |
| 6 | A common surname produces too much noise. | Try a surname with a known occupation or address: `Evans carpenter`, `Evans "42 Oak Street"`. Run these as separate clue-based passes. (S3) | Do the clue and surname belong to the same notice and person? Inspect the full address; a reused address can lead to different occupants. |
| 7 | You need a visit, departure or migration clue. | Run one verb per pass: `Evans visited`, `Evans arrived`, `Evans left`, `Evans returned`, `Evans moved`. Read society items in both plausible departure and destination papers. (S4) | Who performed the action, when, and where? A highlighted surname beside an unrelated arrival notice is not the searched person's trip. |
| 8 | Obituary searches miss women or a legal event. | Inspect bridal showers, society columns, school/teacher/nursing news, guardianship, estate and land-sale notices. Use surname with a relevant keyword, such as `Evans guardian`, then browse the corresponding section. (S5) | Is the item an announcement, allegation, filing or outcome? A guardian notice is a court-record lead; it does not establish that both parents died. |
| 9 | You need an overlooked connection to a place. | Search `"letter list"` in a plausible locality and interval, then read the listed names, including initials and women. Browse such lists when the person's name fails OCR. (S7) | An unclaimed letter can suggest an intended destination or travel stop. It does not establish residence; shared surnames do not establish kinship. |
| 10 | The hometown paper fails or an immigrant's name is distorted. | Search neighboring towns, regional papers and former residences. Include ethnic-language papers serving the community, even when published outside its city; try attested native-language name forms. (S3, S6) | Separate publication place from event place. Inspect the actual foreign-language name and origin statement rather than assuming an English rendering preserved them. |
| 11 | One article suggests a longer story. | Search subsequent months for court proceedings, settlement or verdict; revisit former residences for a death mention. Reuse newly recovered witnesses, addresses and institutions as search clues. (S2, S3) | Record each article's publication date and reported event date separately. Do not turn the first report or filing into the final outcome. |
| 12 | Keywords still fail despite an available likely issue. | Switch retrieval mode: browse its pages directly. For an obituary or marriage item, also search the relevant Newspapers.com index on Ancestry and follow any candidate to the image. (S6, S10) | The index is another access path, not independent corroboration. Check the full notice and its boundaries; inspect missing or inaccessible pages separately. |

## Bounded execution and stopping rules

Begin with a target question, an approximate event interval, known residences, names and
two or three distinctive clues. Set a query budget and an issue-browsing budget before
starting. Choose specific titles and intervals; “browse newspapers” is not a bounded task.

Run the recovery in this order:

1. **Check availability.** Record each promising title and its relevant available issues.
   If the required issue is absent, investigate another paper or its earlier/later title.
   Libraries and historical societies may hold microfilm, originals, abstracts or clipping
   files. Repeating spelling variants cannot recover an issue absent from the venue. (S3, S8)
2. **Change the identifier.** Use the title's printed naming style, women's married forms,
   a constrained surname search and a few image-informed OCR probes. Change one useful
   dimension per pass so you know which adjustment produced a candidate. (S1, S2, S5, S6)
3. **Change the route.** Search an associate or distinctive clue; expand publication
   geography and timing when the person's movements or the story justify it. For the
   relevant event types, try the Ancestry index route. (S1, S2, S3, S6, S10)
4. **Read selected issues.** Use the expected section as an entry point. If its placement
   is unknown, browse the selected issue's pages. Record which issues and pages you
   actually examined; skipped or inaccessible pages remain unexamined. (S6)
5. **Inspect every candidate notice.** Open the page, identify the item boundaries and
   read the sentence linking the person to the event. Keep the title, publication place,
   issue date, page, URL and the notice's own stated event date. (S4)

Stop this retrieval task when the requested notice has been recovered and inspected, when
the remaining necessary material is unavailable or inaccessible, or when the agreed
search/browse budget is consumed. Report which of these conditions ended the run.

Use precise result labels:

- **Recovered candidate:** an inspected notice matches the retrieval question; state any
  remaining same-name uncertainty and hand it to the identity-evaluation recipe.
- **No match in examined scope:** list the queries, titles, intervals and issues examined.
  Do not broaden this to “no newspaper record exists.”
- **Coverage gap:** identify the absent issue, edition or page and the next holding to check.
- **Access blocked:** identify material that exists but could not be inspected.

## Prompt-craft

```text
Find a newspaper notice about [person/event], approximately [interval], associated with
[places]. Known printed names/aliases: [forms]. Distinctive clues: [relatives, address,
occupation, church, club]. Query budget: [limit]. Browse budget: [specific issues/intervals].

Check actual issue availability first. Inspect the title's naming style; try initials,
middle names and relevant maiden/married/husband-name forms. If OCR fails, search an
associate or distinctive clue, then browse selected issues. Expand place/date only with
a stated reason. Use only currently documented query syntax.

When Browse coverage is insufficient, follow the title–holding–issue workflow and
return its register with the documented fields, statuses and next action.

Inspect the complete notice before attaching an event to the person. A surname and verb
elsewhere on the same page are not a match. Treat a letter-list entry as a connection
clue, not proof of residence. Return candidate notices with title/date/page/URL, the
queries and issues actually examined, and the exact stopping condition. Label unavailable
issues separately from no-match searches. Do not invent discoveries.
```
