# Recipe: Practical DNA Painter chromosome-map workflows

## Goal

Build a reusable chromosome-map packet and perform the right operation on it: paint an observed match, move existing data, intersect inherited intervals, infer missing intervals, combine overlapping coordinates, or plan another descendant's test.

The failure to prevent is treating everything DNA Painter draws or calculates as an observed match. A copied segment belongs to its original comparison; an intersection is coordinate geometry; an inferred interval is a deduction; the Coverage Estimator is a pedigree-based estimate. Keep those outputs distinguishable.

## Inputs and routing

Use a named focal tester, authorized segment tables, known relatives and a specific question. A segment table needs chromosome and start/end positions; retain reported cM and SNP counts when available. Raw genotype files and a match's total cM alone are not chromosome-painting inputs. [S1, S2]

Provider download procedures belong to the relevant provider's documentation; provider investigation belongs to its own recipe. For segment validity, triangulation, X-DNA and phasing judgment use [X-DNA and phasing judgment](../../genealogy-research-recipes/recipes/xdna-phasing-judgment.md). For unknown-person placement use [Unknown parentage and WATO](../../genealogy-research-recipes/recipes/unknown-parentage-wato.md). This recipe owns the subsequent DNA Painter operations.

Keep a small operation register beside the map:

| Field | Record |
| --- | --- |
| Operation | Paint, copy, intersect, subtract, union or coverage estimate |
| People | Focal tester and both members of each source comparison |
| Inputs | Saved tables, provider, retrieval date, genome build and filters |
| Assignment | Maternal/paternal/unknown and named ancestor, couple or provisional group |
| Output | Saved map or tree, exported table and notes |
| Status | Observed coordinates, inferred assignment or planning estimate |

This register is a recommended research artifact; it is not a DNA Painter import format. A person's map is a container for research about that person's chromosomes. Do not reuse another person's coordinates merely because their map is convenient.

## 1. Paint a measured match and inspect the saved result

1. Create or open the focal tester's chromosome map. Select one identified relative with a usable pairwise segment table. Preserve the original table before editing or pasting. Require the incoming intervals and any existing painted intervals to use one verified genome build before painting. Convert differing coordinates to that common build outside DNA Painter and retain the originals and conversion record; stop if a build is unknown.
2. Open **Paint a new match**, paste the segment table and use **Preview**. Compare the parsed chromosomes and interval endpoints with the original. Record the selected cM filter; parsing successfully does not mean every source row survived it. DNA Painter's documented ordinary painting default is 7 cM, adjustable in the form. [S1, S2]
3. Enter the match identity and assign the supported parental side and ancestor or couple. If the connection is unresolved, use a provisional group. A group label describes your interpretation; it does not establish it. Save the match. [S1]
4. Click a chromosome's number to open it and inspect all painted segments. In the closed view, groups higher in the key cover lower groups at overlapping positions. Dragging a group changes the visible layer, not its coordinates or evidential strength. [S3]
5. Preserve a note explaining the assignment and its source comparison. For an apparent contradiction, inspect the underlying intervals and provider comparison before recoloring anything. DNA Painter cannot compare raw DNA between two matches; a visual overlap is a reason to investigate, not a triangulation result. [S2]

**Artifact:** source segment table, saved match and assignment note. **Checkpoint:** every retained painted interval can be traced to the correct focal-tester/match comparison; hidden layers have been inspected.

## 2. Copy or merge map data without changing whose DNA it represents

Choose the smallest transfer that answers the question. Duplicate the map for an alternative analysis; copy one match for a focused comparison; export a filtered subset for an ancestor; export the unfiltered table for a whole-map transfer. Use these as alternate maps of the same focal tester. [S4]

1. Duplicate through the settings cog if you need a working copy. Edit or remove groups in that copy.
2. For one match, click one of its segments, choose **View match**, then **Copy match segment data to clipboard**. Paste into the destination's **Paint a new match** form.
3. For one interval, click the segment, then the chromosome number inside its popup; the clipboard receives that segment's data.
4. For a map or subset, open settings → **All segment data**. Set or clear table filters deliberately, then choose **CSV file**. That CSV contains the table currently displayed. Import it through **Import segment data** where available. [S4]
5. Record the source and destination map names, filters and expected row count. Before pasting or importing into a nonempty map, require the incoming and existing intervals to use one verified genome build; convert differing coordinates outside DNA Painter with a retained conversion record, or stop if a build is unknown. Check the imported interval count, identities and assignments against the exported table; inspect duplicate-looking intervals rather than assuming import deduplicated them.

**Artifact:** original map, working copy or destination map, dated CSV and transfer register. **Checkpoint:** the subset is intentional and the destination still describes the correct tester. To derive a child's map from a parent's phased map, use the next workflow rather than copying the whole map.

## 3. Remap inherited intervals with the Common Segment Generator

Use this when the intervals' chromosome copies are already known. The [Common Segment Generator](https://dnapainter.com/tools/csg) intersects coordinates; it does not compare genotypes or establish that overlapping matches share the same DNA. [S5, H1]

1. Select a phased ancestral interval set for a tested parent and the child's measured inheritance through that parent. For example, intersect a child's match to a grandparent with the relevant parent-map intervals assigned to the child's great-grandparent.
2. Save both input sets and document why they refer to the same inherited chromosome copy. Require both sets and the destination child map to use one verified genome build before intersecting their coordinates. If builds differ, convert the coordinates to that common build outside the generator and retain the originals and conversion record. If either build or chromosome copy is unknown, stop this remapping operation.
3. Paste the two sets into the generator and record the cM cutoff. Generate the common intervals. The blog's low 3 cM default was chosen for phased known-family data; it is not a general threshold for trusting small matches. [S5]
4. Inspect output endpoints: each interval must lie inside an interval from both inputs. Review X results separately; the author's own worked use required removing false X intervals. [S5]
5. Paint the output on the child's map, naming the ancestral assignment and recording both inputs. Repeat separately for the other ancestral groups.

**Artifact:** paired inputs, intersected intervals and child-map entries. **Checkpoint:** the common genome build, chromosome copy and inheritance path are documented before any ancestral label is carried forward.

## 4. Calculate provisional missing intervals with the Inferred Segments Generator

Use subtraction when a close relative shares a known match on DNA the focal tester did not inherit. This requires the relationship path and grandparents' independence assumed by the method; coordinate subtraction alone cannot establish the ancestor. [S6]

1. Choose a match whose relevant relationship runs through one grandparent and establish that the relevant grandparents are unrelated. For example, use your sibling's comparison with a cousin who descends from your paternal grandfather's sibling. Retrieve two complete, comparable pairwise segment tables: focal tester–match and close relative–match. Record provider thresholds, genome build and comparison completeness. Require both tables and the destination map to use one verified genome build before subtraction; convert differing coordinates outside the generator and retain the conversion record, or stop if a build is unknown. A missing export or unavailable comparison is not a negative result.
2. In the [Inferred Segments Generator](https://dnapainter.com/tools/isg), put the focal tester–match intervals in **box 1** and the close relative–match intervals in **box 2**. It returns box 2 minus box 1. A partial overlap can split or shorten an interval; reversing the boxes answers another question. [H2]
3. Save the generated intervals. Their cM values are recalculated; do not expect exact agreement with the provider's original values. [H2]
4. For a suitable parent/sibling comparison, a missing interval associated with one grandparent can support a provisional assignment to the other grandparent on that parental side. With a first cousin, the inference may only exclude a particular great-grandparent. Full-aunt/uncle segments can span fully identical regions and include DNA from both grandparents, so do not apply the simple whole-interval rule indiscriminately. [S6]
5. Keep all inferred intervals provisional. Paint using a match name such as `Match A — inferred`; put exclusions in segment notes instead of inventing a positive assignment. Compare with observed intervals before promoting any inferred label. A small shared subset below a provider's reporting threshold can explain an apparent discrepancy. [S6]

For the specific tested-grandparent scenario, box 1 can contain your measured match to that grandparent and box 2 can be populated with a full chromosome set to infer the other grandparent's contribution on that parental side. Use this shortcut here for autosomes: remove X from the populated second field before generating and handle X through the linked X-inheritance recipe. Missing X comparison data or a male's paternal-grandparent path otherwise risks an erroneous full-X inference. The built-in full set accounts for unsampled starts on chromosomes 13, 14, 15, 21 and 22; do not replace it with hand-made `1–end` intervals. [S7, H2]

**Artifact:** both pairwise tables, generated intervals and visibly inferred map labels. **Checkpoint:** verify the common genome build, distinguish `no reported interval` from demonstrated absence of inherited DNA, and retain the limited conclusion justified by the relative used.

## 5. Combine overlapping comparisons with the Distinct Segment Generator

Use the [Distinct Segment Generator](https://dnapainter.com/tools/dsg) when several relatives share segments with the same target match and you want the distinct coordinate span represented across their comparisons. Pasting multiple sets returns merged distinct intervals and recalculated cM; the tool assumes build 37. [S8, H3]

1. Save one pairwise table for each relative–target comparison. Label the people and require all input coordinates to be verified build 37 before combining sets. Convert other builds outside the generator and retain the originals and conversion record; stop if a build is unknown. [H3]
2. Paste the selected sets into the single input box and generate distinct segments.
3. Save the output and total. Inspect an overlapping chromosome to confirm that the shared span is not counted repeatedly.
4. Keep the original per-person tables. The combined output is a coordinate union across these comparisons, not a measured match between an untested ancestor and the target, and not a single relative's ordinary pairwise cM total.
5. Use it to prioritize a match for further tree research while recording the proposed transmission paths and remaining alternatives. The developer presents this use as experimental, not a definitive relationship-identification method. [S8]

**Artifact:** labeled source tables, distinct intervals and a prioritization note. **Checkpoint:** no relationship or ancestral-genome coverage claim is inferred solely from the union total.

## 6. Plan the next descendant's test with the Coverage Estimator

Use the [Coverage Estimator](https://dnapainter.com/tools/coverage) for a different question: how much of an ancestor's autosomal DNA is expected to be represented by tested descendants? It takes a descendancy tree and tester marks, not a segment union. [S9, H4]

1. Start a tree with the ancestor as root; add the documented descendants or import a GEDCOM and select that ancestor. Back up an existing tree before GEDCOM import, which replaces its contents.
2. Mark the descendants whose tests you can use. Check every tester's descent paths to the root: a tester related to the root more than once must appear on each documented path and be marked as tested at each occurrence. These are occurrences of the same tester, not additional independent tests. Record database access; realizing the full represented coverage requires access to the tests in the same database. A mixed-database tree is not automatically an accessible combined research dataset. [H4]
3. Mark deceased people and known testing willingness. Note the current estimate, request next-tester suggestions and compare feasible candidates. Suggestions exclude people marked willing as well as unwilling, so compare willing candidates manually too. A tested child of an already-tested parent does not add coverage in this model. [S9]
4. Record the proposed tester and expected change, then compare feasibility with the research question. This is a planning estimate based on typical inheritance; actual inherited DNA can differ. [S9]
5. Save to the account where available and download the Coverage tree text file as a recoverable artifact. A browser-local tree can disappear when browser data is cleared. [H4]

**Artifact:** descendant tree, accessible-tester inventory, saved tree file and next-test decision. **Checkpoint:** the displayed percentage remains an estimate; the tree and available tests are checked before interpreting lack of useful matches as evidence against the ancestral hypothesis.

## Prompt pattern

“For focal tester A, perform only [operation]. Inputs are these labeled tables/tree and these documented relationships. Preserve originals. Return an operation register, the resulting intervals or tree, and the checkpoint result. Keep observed, inferred and estimated outputs distinct. Do not turn an overlap, coordinate union or coverage percentage into a new measured match.”
