# Recipe: Practical Geni research workflows

## Goal

Produce a reproducible Geni investigation packet: identified profiles, checked relationship paths,
fact-linked sources, an intentional project, resolved or recorded conflicts, and a scoped export.
Choose the procedure that answers the current question; running every procedure is unnecessary.

The failure to prevent is confusing a feature's output with what it establishes. A displayed name
depends on language; a relationship path depends on a focus profile and the current tree;
tagging a document is different from citing a fact; a merge request is different from a completed
merge; a report and a GEDCOM have different scopes.

## Inputs and routing

Start with a research question, the relevant profile URLs, available source records and the
account's actual viewing/editing permissions. Preserve URLs as the working identity keys;
display names alone cannot distinguish same-named people.

These procedures own Geni operations. Use [Evidence and proof judgment](../../dna-research-recipes/recipes/evidence-proof-judgment.md)
for identity decisions and relationship conclusions, and [Y-DNA and mtDNA interpretation](../../dna-research-recipes/recipes/ydna-mtdna-interpretation.md)
for lineage-test interpretation. Follow your citation guide for record citations.
A tree path or inherited haplogroup label does not replace those
investigations.

Each schema below is an investigator-created register, not a Geni upload format. Record a dated
observation, the input/profile URLs, the saved artifact, its scope and the next unresolved action.

## 1. Recover a profile through name variants without creating duplicates

1. Search for the recorded name and then its supported birth, later, transliterated and
   original-script forms. Inspect parents, partners, children, dates and places on every plausible
   candidate. Search existing profiles before creating a branch. [S1, S2, H1]
2. Record each spelling with the record that actually uses it. Keep candidates separate until the
   family and records discriminate them; a search miss does not establish that a profile is absent.
3. For a profile you can edit, open **Edit Profile → Add Language** to put names in separate
   language entries. Geni uses English as the default name language; the displayed name may change
   with the viewer's selected language. Preserve that setting in a before/after comparison. [H2]
4. Keep the birth name, later name and **Also Known As** entries distinguishable. Use aliases for
   supported alternatives instead of packing every spelling into one surname. Explain a
   patronymic or title in the notes rather than inventing a hereditary surname. [S2]
5. Reopen the saved profile and verify the entered forms and profile URL. Try a search with a
   supported alternate name and record the result; do not promise that every language entry is
   indexed by every search route.

**Artifact schema:** `observed_at, query, search_route, language, candidate_profile_url,
recorded_name, name_source, family_comparison, disposition, next_action`.

**Checkpoint:** each name form has a source; a language-dependent display change has not been
mistaken for a different person or a duplicate profile.

## 2. Pin the intended pair and inspect blood and in-law paths separately

1. Open person A's profile and select its green pushpin as the relationship focus. Open person B
   and use the relationship button, documented as **How are they related?** Save both URLs and
   verify that A remains the displayed focus. [S3, H3]
2. Inspect the blood and in-law results separately. Geni seeks the closest path in each category;
   the feature is not an enumeration of every common ancestor or every transmission route. A
   cached result or a pending/recent merge can affect what is shown. [S3, H4]
3. Expand the path and save its ordered profile URLs. Use the path's **Consistency Check** link to
   identify structural problems. Check the documentary support for each parent-child or partner
   link needed by the proposed connection. An empty inconsistency list is not a proof of those
   links. [H5]
4. For a suspected stale path, record the displayed calculation information and use the available
   refresh control. The help page documents refresh eligibility after a week and curator help for
   an earlier recalculation. Do not edit correct relationships just to force a different label. [H4]
5. Save the result and remaining unsupported links. Reset the pushpin to your own profile after
   the comparison so the next task does not silently use A as its focus. [H3]

**Artifact schema:** `observed_at, focus_profile_url, target_profile_url, path_category,
ordered_profile_urls, calculation_information, inconsistency_results, unsupported_links,
saved_path, next_action`.

**Checkpoint:** both endpoints and the path category are explicit; a tree connection remains a
dated tree observation until its required links are supported.

## 3. Attach a document to the facts and relationships it supports

1. On the relevant profile, open **Sources → Add Source**. Select an existing document or add one
   you are authorized to upload. If an existing upload is missing from the selection, use **Show
   all documents**; the default selection is restricted to documents already tagged to that
   profile. [H6]
2. On **Basic Information**, select only the facts the document supports. Enter the value as it
   appears in the document and a fact-specific note, including uncertainty or a conflicting value.
   Preserve a record citation and locator beside the source. [H6]
3. On **Relationships**, select the particular immediate-family relationship and its supported
   facts. Saving relationship sources also tags the related profiles to the document. Merely
   uploading or tagging a document is not the same operation as citing a relationship. [H6]
4. Save, reopen **Sources** and use **View Facts** to inspect the linkage. Compare the displayed
   profile value with the source information. Record discrepancies rather than silently rewriting
   the document's wording to agree with the profile. [H6]

**Artifact schema:** `profile_url, document_url, record_citation, locator, fact_or_relationship,
value_in_document, current_profile_value, source_note, saved_link_verified, next_action`.

**Checkpoint:** another researcher can identify which statement the document supports and where
that statement appears; a document attached to a profile does not support every fact on it.

## 4. Use a locality project for collaboration and a private workspace for unfinished leads

1. Search existing projects for the town, community, institution or research topic before creating
   another. Inspect its scope, documents, discussions and attached profiles. A locality project
   can expose related families under different surnames. [S1, S4, H7]
2. For a public project, join or request collaboration as appropriate. On an eligible existing
   profile, use **Actions → Add to Project**; where you lack the applicable rights, the documented
   **Invite to Project** route requests the managers' participation. Record whether the profile was
   added or a request remains pending. [H8]
3. Keep unpublished hypotheses in a local register or, with an active Geni Pro subscription, a
   **Pro Workspace** note, to-do or private project. Private projects can be tagged with public or
   private profiles, but tagging does not grant new viewing or editing permissions. [H9, H10]
4. Record the project's actual public/private type before adding research material. The older
   project tutorial's statement that all projects are public predates Pro Workspace; it does not
   describe private projects. [H7, H9, H10]
5. Give each lead a concrete next action and supporting record URL. Project membership is a
   research grouping, not evidence that its members belong to one family.

**Artifact schema:** `project_url, project_type, topic_or_locality, profile_url, inclusion_reason,
record_url, contribution_or_request_status, next_action, observed_at`.

**Checkpoint:** collaboration material goes to the intended public project; a private project's
tagged profiles retain their existing permissions and privacy settings.

## 5. Compare duplicates, then resolve field conflicts separately

1. Preserve both candidate URLs, immediate families and sources. Open the second candidate before
   starting **Actions → Merge This Profile** on the first; the documentation recommends this to
   populate the recently viewed selection. [H11]
2. Select the other profile and open **Compare Profiles**. Decide identity from the family and
   records. Use the different-person or decide-later option when identity is contradicted or
   unresolved. Do not create a duplicate merely to acquire control of an existing profile. [H1, H11]
3. If identity is supported, perform the merge or submit the permitted request. Record the actual
   state; a requested merge has not yet combined the profiles. Save the surviving URL after a
   completed merge. [H11]
4. Handle field disagreements through **Actions → Resolve Conflicting Data** or the Match Center's
   **Data Conflicts** view. Choose the supported value for each field and retain the rejected
   alternative and its source in the register. Editing rights are required; for a claimed profile,
   its owner handles the conflicting information. [H12]
5. Reopen the combined profile and review the immediate family as well as the saved fields. A
   completed merge and resolved dates do not establish that duplicate relatives or competing
   parents have been resolved; use the next procedure for those structural conflicts.

**Artifact schema:** `profile_a_url, profile_b_url, identity_basis, merge_or_request_status,
surviving_profile_url, conflicting_field, candidate_values_and_sources, selected_value,
unresolved_family_conflicts, observed_at`.

**Checkpoint:** identity was decided before combining people; merge completion, field choices and
family-structure review are recorded as separate outcomes.

## 6. Diagnose tree conflicts and recover a mistaken merge through its history

1. Open a **Tree Conflict** from the Match Center, the profile notification or the tree's yellow
   triangle. Inspect the immediate family before acting. Tree conflicts can involve duplicate
   relatives, competing parents or multiple spouses; they are distinct from field conflicts. [H13]
2. Stack only relatives demonstrated to be duplicates and use **Merge Duplicates** to reach the
   comparison page. Before completing the merge, an accidentally stacked pair can be unstacked
   with **unlink**. This is not an undo for a completed merge. [H13]
3. For competing parent sets or non-biological links, open **edit this profile's relationships**
   and compare the records for each relationship. Several spouses can be legitimate; the help
   page describes **Cancel** for clearing that notification when there are no duplicates.
   Preserve unresolved parentage instead of removing an inconvenient candidate to clear a
   warning. [H13]
4. For a suspected bad completed merge, open **Revisions**, locate the merge event and select
   **view**. Inspect both profiles and their immediate families as shown at the merge. From that
   page, use **View revision history** for the profile merged into the primary one; its older
   history is not all visible on the combined profile's ordinary revision list. [H14]
5. Prepare a curator request containing the merge event, profile URLs, the demonstrated mismatch,
   source locators and the intended separation. Geni documents curator assistance to undo a bad
   merge through its linked assistance discussion. Keep private details out of a public request.
   After the curator acts, recheck family links and fields and record any remaining conflicts. [H15]

**Artifact schema:** `conflicted_profile_url, conflict_type, implicated_profile_urls, merge_event,
evidence_for_each_link, proposed_action, curator_request_status, post_action_family_check,
remaining_conflicts, observed_at`.

**Checkpoint:** clearing a notification has not substituted for deciding identity or parentage;
unstacking an uncompleted merge has not been mistaken for reversing a completed one.

## 7. Import onto the intended focus and resolve stopped branches deliberately

1. Preserve the original GEDCOM and identify its intended focus person. Search Geni first. When
   that person already exists and your permissions allow it, begin **Import GEDCOM** from that
   profile's Actions menu; match the correct GEDCOM record to the selected Geni profile. [H16]
2. For a genuinely new, unconnected branch, use **Research → Create a Branch**. Enter the focus
   person's details, tick **Import a GEDCOM for this person**, and save the form. In the importer,
   select the GEDCOM record corresponding to that new profile. Use an existing tree location when
   the connection is already established. Creating a branch does not make its contents private;
   check the profile settings and keep speculative notes in the separate private register or
   Workspace. [H1, H9, H16]
3. Read the current importer restrictions and record the offered generation scope before starting.
   Geni limits historical imports and stops a branch when it finds candidate matches already in
   the tree. An import need not load the entire file in one operation. [H16]
4. Inspect each stopped match. Merge only supported duplicate identities; reject a match only when
   the evidence supports different people. Record unresolved matches and permissions that prevent
   progress. Do not reject a plausible duplicate merely to make the importer continue. [H16]
5. Compare the resulting family against the original file, including sources, notes and
   relationships. Save an exception list of omitted, changed or unresolved material; do not assume
   that a completed import preserves every field or media attachment.

**Artifact schema:** `original_file, focus_profile_url, focus_gedcom_id, initial_scope,
stopped_branch_or_match, identity_decision, import_status, field_and_source_exceptions,
next_action, observed_at`.

**Checkpoint:** the file's focus record matches the intended Geni person; stopped branches and
unresolved duplicates are visible in the register.

## 8. Preserve a scoped GEDCOM or a readable ancestor/descendant report

1. Decide whether the output must be a portable tree file or a readable report. For native GEDCOM,
   use your own profile, a profile you added, or an eligible immediate-family profile as the focus,
   then its **Actions → Export GEDCOM** route. The export FAQ includes immediate-family profiles
   unless blocked by the person or manager; the overview gives the narrower added-profile rule.
   Check the offered export on the intended focus. Viewing or managing a profile alone does not
   establish export eligibility. Basic and Pro accounts have limits tied to additions. [H16, H18]
2. Choose the offered export group and primary-name language. **Blood Relatives** and **DNA
   Relatives** are tree-based groups, not measured DNA-match lists; the FAQ includes adopted
   relatives in the former and excludes them from the latter. For a sharing copy, consider
   **Obscure private profiles** and still inspect the resulting file. Record the focus, offered
   scope, selected options and retrieval date. [H18] Save the resulting file
   unchanged. Open a copy in a trusted local genealogy program and inspect the focal person,
   representative parent-child and partner links, and source/note coverage. Preserve the original
   export if the receiving program normalizes or modifies it.
3. For a readable list, use **Actions → Ancestor Report** or **Descendant Report**, choose the
   generations and select **Export PDF**. Record the chosen depth and report direction. The report
   is not a GEDCOM and is not a complete export of the surrounding World Family Tree. [H17]
4. Reconcile the output with the chosen scope and the live profiles. Record restrictions or missing
   people as export exceptions, not as evidence that the relationship is absent. Retain the source
   URLs for links whose documentation must still be retrieved.
5. Before sharing either artifact, inspect its actual contents for living/private people and
   private notes. A viewable report or a successful export does not establish that every contained
   fact should be republished.

**Artifact schema:** `exported_at, focus_profile_url, artifact_type, direction, selected_scope,
original_file, receiving_program, inspected_people_and_links, source_and_note_exceptions,
sharing_review`.

**Checkpoint:** the output matches its declared focus and scope; a PDF has not been presented as
a portable tree file, and an export limit has not been presented as missing genealogy.

## Prompt pattern

"For these Geni profile URLs and this question, perform only procedure [number]. Return its
register, saved artifact and checkpoint result. Keep the relationship focus explicit. Distinguish
tree assertions, source-supported statements, pending requests and completed changes. Draft any
manager or curator request for my review; do not send it. Report unavailable access separately
from an unsuccessful search."
