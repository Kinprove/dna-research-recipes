# Recover an Irish Catholic parish entry at the NLI

## Goal

Carry an Irish Catholic baptism or marriage lead into the National Library of Ireland's register
images, inspect the actual entry and preserve the register and image locators. A transcription
can identify a parish and date without supplying an image; a baptism date remains a baptism
date unless the original separately records birth.

## Inputs and routing

Start with the candidate name, event, approximate date and supported place or parish. Keep a
transcription or commercial-index lead as a separate record of what it displayed. Use the
FamilySearch and Ancestry recipes for their own search/access tools, source-citation for citation
construction, and ai-for-documentary-records for handwriting or Latin interpretation. This recipe
adds the NLI parish, register, filter and image-recovery procedure.

## 1. Select the Catholic parish and the correct register

Search the NLI parish name or use its map to inspect the locality. Confirm the Catholic parish
and diocese before selecting a register: a civil parish or townland is a different geographic
unit. The map supports adjoining-parish discovery; it is not an exact boundary map. [O1]

Read the selected parish's register information. Record microfilm/item, event type and available
dates, then open the corresponding register image or microfilm link. A parish can have several
volumes covering different events and years, as the Ancestry demonstration shows. [P3, O1]

If the target date precedes the available register, inspect earlier-starting neighboring registers
and evidence of a predecessor parish. The demonstration shows an older parish divided when a
new parish was created. Save each candidate register and its coverage; proximity alone does not
establish where the event was recorded. [P3]

**Output:** `place lead | Catholic parish | diocese | register URL | microfilm/item |
event type | described dates | parish-history question | next register`.

**Check:** The selected series fits the event and date. A place-name match or modern parish
alone does not establish that coverage.

## 2. Use the external index to reach the image sequence

For the NLI register-image site, the documented search is by parish, not a person's name.
Use the parish/date/event from an external index or transcription to choose the image sequence,
or browse the defined register directly. [O1]

In the 2022 RootsIreland demonstration, a baptism transcription supplies the parish and a link
to NLI. In the 2024 comparison, a Findmypast transcript has both an NLI register link and a
separate original-record viewer: one opens the NLI sequence at its beginning, while the other
opens the demonstrated entry in Findmypast. These are historical examples; verify the actual
destination and access outcome instead of assuming every current index has either link. [P1, P2]

Preserve both the index URL and the opened image/register URL. If a link lands at the register's
start, the original entry remains to be located. If access fails, record the exact route and
failure; the register has not been examined through that route.

**Output:** `index/transcription URL | recorded parish/event/date | followed link |
destination | actual access result | entry located or outstanding`.

**Check:** A displayed transcription and an inspected original are different outputs.

## 3. Narrow pages by event and date, then inspect the entry

The NLI help documents **Filter Events/Dates** with event, year and month. Use the baptism or
marriage date supplied by the lead. These controls highlight corresponding pages; they do not
find or identify the named person within a page. Browse the highlighted sequence for the actual
entry. [P1, P2, O1]

Inspect pages whose dates differ from the main description. NLI explains that page-level filter
metadata can include annotations outside the register's main described dates. [O1]

Compare the name, parents or spouse, stated residence, event and date with the transcription.
Preserve the original name forms and uncertain letters. The 2022 tutorial finds a maternal-surname
transcription difference in the image. The 2024 tutorial finds a transcription that presents the
baptism date as an estimated birth date. Keep those source statements separate; do not copy the
estimate into an asserted birth. [P1, P2]

For faint text, try NLI's documented brightness, contrast or inverse-image controls. Label the
adjusted view; retain the original locator. Route disputed readings to the documentary-records
workflow. [O1]

**Output:** `register | event/year/month filter | page range inspected | exact entry |
raw names/roles | stated residence | baptism/marriage date | separately stated birth date |
transcription discrepancy | unread text`.

**Check:** The filter selects a page range. Completion requires the entry, its date label and
its register context.

## 4. Save the register identity and the exact image locator

Inspect the register's identification information as well as the target page. The citation
demonstration returns to the opening identification image for parish, diocese, event type and
dates. Save that context with the microfilm/item identifier. [P2]

Preserve the exact URL for the page actually inspected and its NLI page number. The demonstration
shows the URL changing when a different page is selected. Numbered NLI page metadata also lists
the microfilm and parish context. Keep any printed register page or entry number in a separate,
nullable field; a viewer page number is not automatically the original pagination. [P2, O2]

When a page download is offered and permitted for the intended use, retain the original image
with its locator. Reopen the saved link when access is available and compare the entry. If that
check cannot run, record it as unperformed rather than claiming the link was tested. [O2]

**Completion packet:** index lead; Catholic parish/diocese; register identity and described
coverage; microfilm/item; selected event/year/month and inspected range; exact page URL and viewer
number; original printed locator if present; raw entry reading; separately labelled event/birth
dates; discrepancy or unread text; and remaining work.

## Prompt pattern

> Recover the NLI parish-register image behind this Irish Catholic index lead. Confirm the
> Catholic parish and event/date coverage; record the microfilm/item and actual link destination.
> Use the event/year/month page selection, then locate and compare the entry. Preserve the exact
> image URL, viewer number, any printed locator and the raw names/roles. Keep baptism and birth
> statements separate. Return the inspected range, uncertainty and next register without inventing
> an image, reading or identity.
