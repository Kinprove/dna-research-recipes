# Recipe: Inventory the documents of a probate case

## Goal

Recover the available documents behind a probate index, will or administrator's bond.
Keep a case inventory and a queue of unresolved references, so finding one useful document
does not silently finish the estate search.

## Before starting

Record the deceased person's supported names, approximate death date, residences and known
property locations. Keep competing same-named people separate. Determine the relevant court,
record series and present custodian from the historical locality's descriptions or finding aids;
do not assume that a death location, an heir's residence or today's court name decides jurisdiction.

Use the existing platform workflow for opening an image-only volume and distinguishing printed
pages from viewer image numbers. This recipe manages the documents and references across volumes.

## 1. Establish the case and its record-series scope

1. Save the locator and image of the starting index, will, bond or estate entry.
2. Record the name and identifying context, the court/jurisdiction stated, the case or estate
   number when supplied, and the document and recording dates actually present.
3. List the probate-related series available for that court and period. A surviving will book,
   administration docket, probate journal and loose case file are different retrieval targets.
4. Identify the present custodian for each relevant series. Records may have moved from their
   original court to an archive or another repository.
5. If the person owned property elsewhere, inspect that locality's probate descriptions for a
   related proceeding. Add a candidate case only with its own locator and identity check;
   do not presume an ancillary proceeding must exist. [S1, S2]

**Artifact:** A case register: case ID, deceased name, identifying context, court/time,
case number, candidate related cases, relevant series, coverage and present custodian.

**Check:** A collection title or same name is not a case link. Record the stated connection
between a related proceeding and the principal case, or leave that connection unresolved.

## 2. Resolve every discovered reference into its own inventory row

1. Read the starting record for references to another volume, page, docket, journal or file.
2. Enter each reference in a queue exactly as written, including the record series and book number.
3. Open the referenced series and volume; locate the printed page using the viewer's available
   navigation. Save the image locator separately.
4. Confirm that the retrieved document concerns the intended case. Inspect its continuation,
   and record any further references it supplies.
5. Link the resolved row back to the document that cited it. If you cannot retrieve it, record
   the specific outcome: locator unreadable, series not held, access restricted, page not found,
   or request pending. Keep a tentative reading visibly tentative.
6. Continue until every discovered reference has a recorded result or an explicit next action.
   [S2]

**Artifact:** A reference queue plus document inventory:

| Field | Preserve |
| --- | --- |
| Document ID and case ID | Distinguish the document from the case and from its images |
| Type and creator | Will, bond, docket entry, appraisal, account, settlement or actual description |
| Dates | Document/action date and recording date, separately when given |
| Locator | Court, series, case/file number or book/page, repository and image link |
| Image extent | Start/end and continuation images inspected |
| Reference relationship | Referring document ID and wording; newly discovered targets |
| Retrieval result | Found and checked, uncertain target, unavailable or next action |

**Check:** A will can be indexed while a referenced docket or journal is not. A link to an
index entry is not a completed retrieval of the document it points to.

## 3. Search for later and non-will parts of the proceeding

1. Review the inventory for administration, guardianship, appraisal, accounts and settlement
   material relevant to the case. Search the series actually held; not every case has every type.
2. Try supported abbreviations and administrator or executor names when the deceased's full
   name does not recover the relevant entry. Verify each candidate from its document.
3. Do not restrict every search to the death year. Use dates already found in bonds, accounts,
   dockets or settlements to extend a bounded search into later years.
4. If a deceased person appears in a land document as a boundary reference, record that role
   separately. Follow a relevant administrator/executor deed into a probate search; do not turn
   an ordinary neighbor reference into evidence of another estate proceeding.
5. Preserve an inventory of estate documents even when no will is located. An administration
   account or appraisal remains a document to retrieve and examine, rather than a failed will
   search. Do not declare intestacy solely because a will search failed. [S1, S3]

**Artifact:** Additional document rows and a search log specifying series, names, date bounds,
results and reasons for each extension.

**Check:** A later recording date is not a later death date. Finding a settlement several years
after death demonstrates the need for that case's wider search; it supplies no universal deadline.

## 4. Reconcile retrieval coverage and hand off interpretation

1. Sort document rows by the dates of the recorded actions while preserving the original
   image order and locators.
2. Check that each image belongs to the intended document and case. Separate a different
   person's entry sharing the same page.
3. Compare the reference queue with the inventory. Mark resolved references and retain any
   missing documents or unsearched relevant series.
4. Report what was retrieved, the holdings/series searched, and the limits of the search.
   Completion means the recorded queue was handled within that scope; it does not certify
   that every historical case document survives or has been found.
5. Hand the source-linked documents to the evidence/proof workflow for identity, kinship and
   conflicts. Keep transcript uncertainty and proposed relationships separate from retrieval
   status. [S1, S2, S3]

**Artifact:** A case-document packet, resolved/unresolved reference list and retrieval-coverage note.

**Check:** “Will found,” “document packet retrieved” and “relationship established” describe
different outcomes. State only the outcome the packet supports.

## Prompt pattern

> Using these probate images and record-series descriptions, build the case register,
> reference queue and document inventory. Preserve exact book/page and file references,
> distinguish document/action dates from recording dates, and follow every supplied reference.
> Propose bounded searches for relevant later or non-will documents. Mark missing series,
> uncertain locators and access limits. Do not infer intestacy, kinship or exhaustive survival.
