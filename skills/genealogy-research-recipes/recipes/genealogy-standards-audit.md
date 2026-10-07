# Recipe: Auditing a genealogy research package against professional standards

## Goal

Find the exact point where an asserted identity, relationship or event stops
being traceable to examined evidence and explained reasoning. Return a gap report
and an appropriately scoped writing recommendation. A populated log, polished
footnote or completed checklist does not establish the Genealogical Proof Standard
(GPS). The researcher owns the final ruling on evidentiary sufficiency.

Use this when reviewing a dossier, research report, proof draft or documented tree
before relying on its conclusions. For evidence interpretation, use
[evidence-proof-judgment](evidence-proof-judgment.md). The existing `source-citation`
and `research-documentation` recipes can construct citations and research artifacts
when available; this recipe checks the connections between those artifacts.

## Fix the question and the audit boundary

Identify the exact question, people, relevant place and period, packet revision,
author and review date. List which source images, transcriptions, search logs and
draft sections you can actually inspect. Separate an absent item from an item
supplied but inaccessible to the reviewer. If only a narrative or tree export is
available, audit that material and identify what remains unassessed.

Prior research and locality context must explain the selected record systems and
historical jurisdictions. An exhausted budget or completed five-item plan is a
finished research phase, not a demonstrated reasonably exhaustive investigation.
Apply archive-specific citation conventions where relevant; do not present one
English-language style or worksheet as universally mandatory.

## Trace claims across artifacts

Build one row per material assertion, including claims that connect records to a
person or establish parentage. Split a sentence when its information comes from
different records or informants. Use stable local identifiers only as a convenient
way to cross-reference the supplied packet.

| Claim | Source actually consulted and pinpoint locator | Extracted information | Reasoning passage | Gap and next action |
| --- | --- | --- | --- | --- |
| Exact assertion, person and event | Packet file or source ID; record/page/leaf/image/entry; consulted version | What the source says, with transcription/translation identified | Where the author connects this information to the asserted answer | Exact missing link; a concrete verification or research step |

Walk each row in both directions: from the claim to the cited item, then from that
item back to the claim. Check these failure points:

- **Version substitution:** an index-only observation is described as an examined
  original. Identify the version actually seen; distinguish provider-reported
  archival details from personally checked ones. A source-of-source reference
  does not imply that the researcher visited that repository.
- **Locator drift:** an image number is treated as a page or leaf number, or a
  bibliography points to a collection without locating the cited assertion.
  Attach each locator to its actual document, film or digital presentation.
- **Extraction drift:** a translation, normalized date or expanded abbreviation
  appears as literal source text. Keep the source wording and researcher additions
  distinguishable; check the original when it is supplied.
- **Inference omission:** the citation identifies a record but the text never
  explains why it concerns this person or supports this relationship. Request
  the missing reasoning; do not invent it or merge identities to fill the row.
- **Independence inflation:** several citations repeat the same information
  stream. Record that dependence and route its evidentiary assessment to the
  judgment recipe; citation count is not witness count.

An inaccessible original leaves original-image validation unassessed. It does not
automatically erase the value of a honestly identified index or derivative source.

## Audit the searches behind an absence claim

Keep search history distinct from an event timeline: the log can contain searches
for same-named candidates, associates and sources yielding no findings. For each
absence used in the written reasoning, locate the actual search date, collection
and coverage, query or browsing procedure, variants and inspected range.

Distinguish `no match returned`, `no relevant entry in the inspected range` and
`records unavailable`. A report saying only `NIL` or listing a website lacks enough
detail to reproduce the attempt. Request the missing search scope. For an absence
presented as evidence, point to the author's explanation of why the information
should appear under the historical recording practice and what competing causes
were considered. If that explanation is missing, flag the inferential gap rather
than writing that the event did not happen.

## Replace GPS checkmarks with evidence pointers

For each component, record a concrete packet passage or artifact, what it
demonstrates, and the remaining gap. Use local audit labels `supported`, `gap` or
`unassessed`; these describe the review, not official GPS grades. `Supported` means
that the reviewer can inspect the material addressing that component, not that an
AI has certified its sufficiency.

| GPS component | Material to inspect | A consequential gap to expose |
| --- | --- | --- |
| Reasonably exhaustive research | Question-specific coverage rationale, relevant record systems, search log and remaining-source assessment | Significant relevant sources or jurisdictions are unexplained; a time limit is used as the completeness argument |
| Complete and accurate citations | Claim rows, consulted versions and pinpoint source references | The reader cannot locate the assertion or the citation overstates what was examined |
| Analysis and correlation | Linked extracts, comparisons and explicit inference passages | Sources are listed without explaining how their information answers the question |
| Conflict resolution | Contrary evidence, explanation and its supporting references | A material conflict is omitted or a preferred value is selected without explanation |
| Reasoned written conclusion | The actual answer and the chain supporting it | The conclusion is stronger than the analysis, or depends on an unsupported premise |

If no material conflict was found, inspect the basis for that assessment rather
than inventing a conflict to fill the worksheet. Review completeness relative to
the question, not by an arbitrary document total or searches-per-person threshold.
When a premise changes, identify dependent passages that require reconsideration;
independently supported observations are retained with their original attribution.

## Choose the writing product after the audit

| Situation | Appropriate product |
| --- | --- |
| Work completed for a bounded phase, with unanswered questions or unavailable evidence | Research report: work performed, findings, limits and specific next steps |
| At least two supporting citations in the statement or its broader documented context support a directly evidenced conclusion that needs no explanatory discussion; that context demonstrates adequate research scope | Proof statement in that context |
| Direct evidence supports a relatively straightforward answer; any small inconsistencies can be explained briefly | Proof summary with the supporting references and explanation |
| Direct evidence is absent, significant conflicts must be resolved, or the identity/relationship depends on substantial correlation | Proof argument organized around the reasoning and relevant alternatives |

Locate those supporting citations before recommending a proof statement. The
two-citation condition selects a writing form; it does not establish source
independence or evidentiary sufficiency. If the packet supplies only one, identify
the missing support and retain a research report or qualified draft while it is
addressed; do not add a token citation to meet a count.

Summary and argument are a continuum, not word-count categories. More explanation
is useful only when it makes the inferential chain visible. A proof draft organized
solely in search order should be reorganized around the steps that establish the
answer; the log preserves the search order separately.

If an essential gap remains, retain a research report or clearly qualified draft.
Do not relabel unresolved alternatives as a finished proof. A complete audit can
recommend a draft for human review; it cannot certify BCG status or declare a
relationship proven on the researcher's behalf. A valid GEDCOM file represents
data and does not establish the sufficiency of its supporting evidence.

## Deliver a reviewable handoff

Return the exact question and inspected revision; the claim traceability rows;
the five GPS evidence-pointer rows; and a short list of consequential gaps with
specific next actions. State the recommended writing product and which judgments
still belong to the researcher. Do not invent probabilities or a numerical proof
grade. When no consequential gap was observed in supplied material, state that
bounded finding and list any unassessed material separately.

Suggested prompt:

> Audit this research packet for the stated question. Identify the version and
> locator actually consulted for each material claim; locate the extraction and
> inferential passage. For every GPS component, give an inspectable evidence
> pointer or a specific gap. Separate unsuccessful searches from inaccessible
> records. Recommend the appropriate writing product and concrete next actions.
> Do not supply missing evidence or decide evidentiary sufficiency for me.
