# Recipe: Maintaining FamilyTreeDNA exports and tree links

## Goal

Keep a usable FamilyTreeDNA (FTDNA) match/segment dataset through exports, name collisions and tree
relinking. The output is a paired export, a name-safe joined table and a dated link/bucket inventory.
All examples are synthetic.

## The failure to prevent

A match name is a join key, not a unique person identifier. Matching Bucket and Linked Relationship
are values observed at download. Record link changes separately from the retrieval date, keep the
export choice and kit with the rows, and refresh match metadata after relinking.

## Before starting

Use authorized account access and start with the paired export in workflow 1. FTDNA downloads
require two-factor authentication. [H6]
Keep original files and profile details private; use opaque handles in shared summaries.

## Four workflows

### 1. Export the match and segment pair, and record its scope

On Family Finder Matches, use **Export CSV → All Matches** for the match list. In the Chromosome
Browser, use **Download All Segments** for all matches' segment rows; **Download Segments** produces
only the comparison subset. [S1, S2, H6, H7]

Record kit, retrieval date/time, export choice, active filters and row counts for both files. Compare
match-file rows with the displayed All Matches count; count distinct segment-file names separately
from interval rows. Compare the distinct-name sets in both directions for the all/all pair.
If names are absent from the segment file, check that **Download All Segments**, rather than
**Download Segments**, was used. If names are absent from the match file, check **All Matches**
rather than a filtered export. After correcting the export choice, re-export both files in the same
session. Resolve remaining name mismatches through the note-handle procedure below before joining. Record intentional filtered or
selected exports as subsets with their criteria and actual export choice.

**Artifact:** export manifest, one row per file: kit handle, retrieval date/time, file name, tool, export
choice, active filters, scope (`all`, `filtered: <criteria>`, `selected: <n>`), row count, interface
count, `links_as_of`, check results. **Stop when** the recorded scope, displayed match count and
cross-file name check reconcile. Carry that scope into the joined table.

**Synthetic manifest example:** kit `K1`, retrieval date/time `2026-10-03T10:00:00Z`, file `K1-matches.csv`, tool
`Family Finder Matches`, export choice `All Matches`, active filters `none`, scope `all`, row count
`240`, interface count `240`, links as of `2026-10-02`, checks `passed`.

### 2. Join matches to segments without collisions

The match file has one row per match; the segment file repeats a match for each reported interval.
Use the match CSV's full-name column, rather than its separate first/middle/last-name columns,
and compare its exact values with names in the segment CSV. [S1, S2] Use files from the same kit
and export session. Hold out duplicated names and any unmatched spelling for the note-handle
procedure below.

For each held-out person, open the separate match profiles and assign opaque local handles in the
private working ledger. Append that person's handle to their FTDNA match note, preserving the
existing note. Notes are included in the match CSV: re-export the pair through workflow 1 and
verify that each handle identifies exactly one metadata row. [S1, H7]

On the Matches page, select only the row for one handled person and click **Compare Relationship**.
In the Chromosome Browser, use **Download Segments** and label the resulting file with that handle.
Repeat for each other person. Keep the original ambiguous segment rows out of the join; replace
them with the labeled single-match files, joined to their handled metadata rows. [H6, H7]
Use the displayed **Shared DNA**, **Longest Block** and linked relationship as cross-checks; the
note handle binds the row even when those values tie. Keep views by match and by chromosome/start/end.

Carry **Linked Relationship**, **Matching Bucket** and **X-Match cM** from the match export into the
joined table. Those columns preserve the tree relationship, provider side assignment and X amount
without retyping the screen. FTDNA reports X matches only for people who also match on an autosome;
X-only relatives do not appear in this Family Finder match export. [S1] Keep the original exports and
save the join as a separate file.

**Artifact:** joined table and a collision ledger mapping note handles to selected-match files.
**Stop when** every held-out person has a unique note handle and a labeled single-match
segment file. Do not join a held-out person until both conditions hold.

### 3. Inventory links before any tree change; relink deliberately

Before connecting, switching or disconnecting the MyHeritage tree, seed a link inventory from the
match export's **Linked Relationship** and **Matching Bucket** columns, then record the corresponding
tree person from your existing link ledger and documented pedigree path for each linked match.
[S1, S4] The MyHeritage tree does not mark who is linked, so the inventory comes from the FTDNA
side. [H3] After a tree transfer, formerly linked people arrive flagged in the GEDCOM, but each must be searched and confirmed again through Account Settings → Genealogy →
Link your matches: **Search**, then confirm each suggested person. These are suggestions, not
preserved links. [H3]

To link a match: **Link on Family Tree** beside it, then search the person's name as written in
MyHeritage, including prefixes and the maiden surname. [S4, H3] Candidates return with relationship
to the kit, full name and birth/death years; choose by the documented path recorded beforehand, not the first
name hit.

**Artifact:** link ledger — match handle, tree person, relationship, side, documentary basis, date,
status (`linked`, `suggested-unconfirmed`, `not in tree`, `deliberately changed`). **Stop when**
every inventoried person is linked again, absent from the new tree, or deliberately changed with
a recorded corrected path/removal reason. There must be zero `suggested-unconfirmed` rows at
completion; those rows are work still to do.

**Synthetic link-ledger example:** match `M1`, tree person `P1`, relationship `maternal second
cousin`, side `maternal`, documentary basis `synthetic record set D1`, date `2026-10-03`, status
`suggested-unconfirmed`. Leave it in that state until its FTDNA link is confirmed.

### 4. Anchor Family Matching with side-specific relatives

Family Matching requires a Family Finder result, matches, a MyHeritage connection and at least one
linked maternal or paternal match. It uses linked testers from parent to third cousin and excludes
linked relatives whose shared DNA contradicts the stated relationship (a "parent" calculated as a
second cousin). To assign a match, FTDNA detects a shared phased DNA block between the tester,
match and linked relative: the block is carried by the same alleles and meets the special Family
Matching threshold. The linked relative's tree position supplies the parental side. ICW is not
used for bucketing. [H4, S5]

Link documented relatives who identify one side first: parents and grandparents, then aunts,
uncles and cousins. Children and full siblings share both sides and cannot split them. [S5] An
anchor linked under the wrong parent supplies the wrong side to phasing. The shared-cM relationship check does
not validate a relative's tree position: trace each anchor's path to the kit holder's mother or
father.

Capture maternal, paternal, both and unassigned counts before each anchor link. After linking,
check that the anchor's Matches row shows the expected **Linked Relationship**, then re-export
the match list. Record the link-change time separately from the export time and save the bucket
counts shown in that dated export. [H3, H4]

Compare the dated counts and known-side paths. If counts are unchanged, check H4's eligibility
conditions: the correct person linked, relationship within parent-to-third-cousin range, and
shared DNA consistent with that relationship. If a bucket conflicts with a documented path,
check the tree positions of the linked kits on the reported side and look for an additional path
through that parent. Correct or remove a misplaced link and re-export. With anchor identities and
tree positions verified, the bucket means FTDNA found a qualifying phased block shared with a
linked relative on that side. A documented relationship through the other parent does not refute
that assignment. Record both and test the additional descent path using `ai-for-dna-research.md`.
Preserve the provider's assignments exactly, including unassigned rows, in each snapshot.

**Artifact:** before-link and later dated exports, bucket counts and a `links_as_of` note.
**Stop when** each new anchor is confirmed on its match row, checked against H4's supported
relationship range and shared-DNA validation, and included in a post-link export. Record
unavailable anchors separately. Compare that export with the baseline and send any remaining
side/path conflicts to `ai-for-dna-research.md` with the two exports and the link ledger.

## Hand off interpretation

Use `myheritage-dna-match-investigation.md` first for MyHeritage work. Verify MyHeritage export
availability and coverage for the kit; if an export is unavailable, preserve the selected
displayed evidence manually and mark that recipe's packet scope as `selected_matches`, never
`complete_match_list`. For FTDNA, use the export manifest and joined-table schema above.
Before adapting those schemas to another vendor, verify its available exports and fields.
For side/path conflicts and additional descent paths, use `dna-research-recipes` →
`ai-for-dna-research.md`. For segment validity, triangulation and X, use
`dna-research-recipes` → `xdna-phasing-judgment.md`. The joined table and bucket snapshots are
inputs to the relevant interpretation.
