# Recipe: Working reproducibly with GEDmatch

## Goal

Run GEDmatch comparisons, targeted segment searches, triangulation, parental phasing and Lazarus
reconstruction with enough recorded information to repeat the analysis. Each workflow produces
an artifact and a completion check. Examples and field schemas are original synthesis; example
kit handles are fictional.

## The failure to prevent

A match-list row, a pairwise segment, a shared-match list, a triangulation result and a generated
kit answer different questions. Keep their tool, inputs and settings attached to every result.
Report an absent row as absent from that particular run. A generated kit remains a generated
kit, even when GEDmatch assigns it a normal-looking kit number.

## Before starting

Use kits you are authorized to analyze and keep kit identifiers, contact details and raw files
in the private working dataset. Find each named tool in the current account; capture its actual
controls and access requirements. Tutorials below describe historical interfaces. An unavailable
tool is an access limitation, not a completed comparison. Do not substitute remembered default
thresholds, match limits, kit prefixes or processing times for what the current screen reports.

Use separate workflows for general spreadsheet export and cluster construction. This recipe
owns the GEDmatch run and comparison records.

## Eight workflows

### 1. Establish a kit registry and a comparable run baseline

1. Record each kit's tested person, testing source and whether it is measured, phased or
   reconstructed. Keep multiple tests of one person as separate kit records. Preserve the
   original download and the upload receipt; use the vendor's current upload instructions. [H1]
2. Record the readiness state actually shown. After processing, use a known relative as a
   comparison control. Save its baseline One-to-One result rather than treating an upload
   receipt as evidence that matching is ready. [H2]
3. Start a run record before every subsequent workflow. Capture the precise tool name/version
   shown, input kit numbers, displayed coordinate build, cM/SNP thresholds, match-count cap,
   chromosome/window filters, exclusions and other changed options. Mark controls the tool
   does not expose as `not exposed`; save the parameter screen with the result.

**Artifact:** private kit registry: `kit_id, person_handle, source, kit_type, input_kits,
upload_receipt, readiness, baseline_run_id`. Run manifest: `run_id, retrieved_at, tool_label,
input_kits, build, cm_min, snp_min, match_cap, chromosome, window_start, window_end, exclusions,
other_options, parameter_capture, result_file, row_count, outcome`.

**Complete when:** each used kit has an identified origin and readiness observation, and the
known-relative control has a saved result. Record unavailable controls explicitly.

### 2. Follow a One-to-Many candidate into One-to-One

1. Run One-to-Many for the focal kit and preserve the candidate row, including the match kit,
   total/longest-segment values, source and reported overlap when present. Use kit IDs as keys;
   display names are labels. [H3]
2. Open the candidate's direct comparison, or enter the two kit IDs into One-to-One. Save the
   position table and, when useful, the graphics. Historical tutorials demonstrate using the
   match-list link to prefill the pair and a positions-only view for copying. [S1, H2]
3. Record every reported segment: kit pair, chromosome, start/end, cM and SNP count, with its
   run ID. Keep X comparisons in separately labeled rows.
4. When reports disagree, first verify the kit pair, exact tool/algorithm label, build, thresholds,
   match-list scope and readiness. Re-run with comparable exposed controls; retain both original
   reports. Do not lower the threshold simply to recover a desired match.

**Artifact:** candidate-to-comparison ledger: `candidate_run_id, pair_run_id, kit_a, kit_b,
chromosome, start, end, cm, snps, comparison_type, status, discrepancy_reason`.

**Complete when:** each investigated candidate has a saved direct result, an explicit
`no segment reported under these settings`, or `unavailable`. A blank ledger cell is unfinished.

### 3. Turn a match-both lead into a checked three-kit comparison

1. Use the current match-one-or-both/shared-match tool to collect candidate C for focal kits A
   and B. Save that run's settings and the original membership list. [S2]
2. Run A–B, A–C and B–C One-to-One comparisons. The membership list does not supply the
   three chromosome-level results. [S3, H4]
3. For intervals on the same chromosome and coordinate build, record their common core:
   `core_start = max(pair_starts)` and `core_end = min(pair_ends)`. Require a nonempty interval
   in all three saved comparisons. Compute base-pair overlap only; do not convert its fraction
   into a guessed cM value or claim that a segment threshold applies to the core itself.
4. Record the status as `three pairwise intervals overlap`, `no common core`, `pair missing`
   or `unavailable`. Send the measured intervals to the interpretation recipe before assigning
   an ancestor. [H4]

**Artifact:** triplet table: `kit_a, kit_b, kit_c, ab_run, ac_run, bc_run, chromosome, build,
pair_intervals, core_start, core_end, status, interpretation_ref`.

**Complete when:** all three pair results and the common-core check are present. An unchecked
B–C comparison cannot be replaced by two overlaps with A.

### 4. Search one locus, then investigate the overlapping candidates

1. Choose a saved segment, then enter its focal kit, chromosome and coordinate window in
   Segment Search. Capture the display build, match cap, thresholds and exclusions shown. [H5]
2. Save the returned CSV when offered; otherwise preserve the table and report with their
   run manifest. Treat every returned interval as a candidate: the search can return a segment
   that overlaps only part of the requested window. Its display color is not a pairwise test. [H5]
3. Sort by chromosome/start/end and record the actual overlap with the target window. Select
   useful candidates for Multiple Kit Analysis or workflow 3; retain the selection list. [H5]
4. If a known direct match is absent, check the run's cap, exclusions, thresholds and tool label
   against its saved One-to-One result. Compare that exact pair again. Keep an unresolved
   absence as `not returned by this search`, with both run IDs.

**Artifact:** locus-search ledger: `search_run_id, focal_kit, chromosome, build, target_start,
target_end, match_kit, returned_start, returned_end, overlap_start, overlap_end, followup_run_id,
status`.

**Complete when:** the search scope and output are preserved and every selected candidate has
its follow-up result or explicit access limitation. Do not call a bounded search exhaustive.

### 5. Freeze a tag group before Multiple Kit Analysis

1. Create a tag group for a specific comparison question, or select a fixed kit subset from a
   result table. Record the exact roster; a color or group name alone does not preserve it. [S4]
2. Open Multiple Kit Analysis for that roster. Capture the autosomal matrix and, for
   cross-source comparisons, the SNP-overlap matrix. These report shared-DNA amounts and
   common assayed-marker counts respectively; neither replaces chromosome-level pair results.
   Save row/column kit identities with the matrix. [H6]
3. Use the group's chromosome/segment views to select direct pairwise checks. Its Segment
   Search is restricted to the group rather than the broader search roster. Record that scope
   difference before comparing results with workflow 4. [H7]
4. If the group changes, give the new roster a revision and preserve the old matrix. Re-run the
   affected comparison rather than pasting fresh cells into an older snapshot.

**Artifact:** group manifest: `group_id, roster_revision, kit_ids, selection_basis, created_at,
matrix_run_ids, segment_run_ids`. Matrix cells retain `row_kit, column_kit, value, metric,
run_id`; missing/unavailable cells remain explicit.

**Complete when:** the saved matrix has a fixed identifiable roster, labeled metrics and a
recorded scope. A matrix cluster remains a lead for pairwise investigation.

### 6. Preserve and check a triangulation run

1. Enter the focal kit in Triangulation. Capture the maximum kit count, upper close-match
   cutoff, minimum segment setting, chromosome, build and cross-matching option actually used.
   Start with one chromosome when investigating a specific interval. [H4]
2. Decide explicitly whether close relatives belong in this run. Excluding them can reduce
   repetitive groups; retaining a documented side-specific relative serves a different question.
   Save the chosen cutoff and excluded roster where available. A tutorial's cutoff does not
   reliably exclude every member of a relationship category. [H4]
3. Preserve the original result rows and grouping display. For a triplet you intend to use,
   collect the three direct pair results through workflow 3. Before treating a larger set as
   one all-pairs group on a common core, check every unordered pair on that core; connected
   triplets and similar coordinates alone do not establish that property. [S3, H4]
4. Store a candidate ancestral path separately from the tool result. Naming the ancestor
   requires the documented pedigrees and interpretation review.

**Artifact:** triangulation ledger: `triangulation_run_id, focal_kit, group_label, member_kits,
chromosome, build, reported_interval, checked_pair_run_ids, common_core, unchecked_pairs,
candidate_path_ref, status`.

**Complete when:** the claimed group property is supported by the saved pair checks; otherwise
retain only the verified triplets and label the larger set `partially checked`.

### 7. Make a parental-phasing experiment reproducible

1. Supply the child and its actual tested parent(s) to the current Phasing tool. Identify the
   parent roles from the input pedigree and tool output. Save the submitted form and generated
   kit IDs; do not infer the roles from a remembered prefix convention. [S5, S6]
2. Register each output as `phased`, with the input kits and parent role attached. The output
   represents an inferred parental contribution to that child, not a measured full parental kit.
   Keep the original child's kit as the comparison baseline. [S5]
3. Compare the original and generated kits against documented relatives from each parental
   side using recorded One-to-One settings. Preserve missing and contradictory results along
   with positive ones; send them to `xdna-phasing-judgment.md` for assessment. [S6]

**Artifact:** phasing experiment: `experiment_id, child_kit, maternal_input, paternal_input,
tool_options, output_kit, output_role, baseline_run, control_kit, documented_side,
output_comparison_run, observed_result, unresolved_issue`.

**Complete when:** every generated ID has its inputs and role, plus saved control comparisons
or an explicit `no independent control available` limitation. Generating an ID alone does not
validate the phased data.

### 8. Trial a Lazarus reconstruction with an input-group ledger

1. Choose the target and list documented relationships for every proposed input. In the
   demonstrated Lazarus grouping, group 1 contains descendants; group 2 contains relatives of
   the target who are not descendants; optional group 0 contains the spouse or relatives of that
   spouse unrelated to the target, to remove spouse-side contributions. Verify the current
   form's group definitions before entry. Do not populate a group by matching surname alone. [H8]
2. Select descendants from distinct available branches. A tested child already carries what
   that child's children inherited from the target; grandchildren help cover a branch whose
   relevant parent is unavailable. Log every input's branch and any additional relationship. [H8]
3. Run the trial mode first, when offered. Save inputs, sex/X setting, thresholds, processing
   choice and coverage report. Revise one input or setting at a time and preserve each run.
   Coverage describes reconstruction output, not its accuracy. [H8]
4. Use a tested target, when available for a control experiment, or reserve a documented relative
   outside the construction inputs for comparison. Record what that control can check; sharing
   a segment with one held-out relative does not validate the whole kit. Without a control,
   mark the output `unvalidated`. Register it as `reconstructed` and review genotype quality
   through `xdna-phasing-judgment.md` before using it as research evidence.

**Artifact:** reconstruction ledger: `experiment_id, target_handle, input_kit, group,
documented_relationship, branch, additional_paths, settings_capture, trial_run, coverage_report,
output_kit, validation_control, validation_run, validation_status`.

**Complete when:** each input has a justified role, the trial is preserved and validation limits
are stated. Full database processing requires a separate explicit decision by the kit manager;
the recipe does not change anyone's kit visibility or permissions.

## Hand off interpretation

Use `genealogy-research-recipes` → `xdna-phasing-judgment.md` for segment trust, triangulation, X,
phasing and reconstructed-kit quality; `ai-for-dna-research.md` for endogamy, multiple descent
paths and selecting relatives; `unknown-parentage-wato.md` for placement hypotheses; and
`evidence-proof-judgment.md` for documentary identity and conclusions. Pass the preserved
run records with those requests. Pass verified measurements to the painting workflow in
DNA Painter.
