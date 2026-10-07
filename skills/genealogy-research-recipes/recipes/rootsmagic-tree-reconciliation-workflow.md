# RootsMagic: Reconcile a Local Tree with Ancestry and FamilySearch

## Goal

Share selected, supported facts and sources between a RootsMagic database, an Ancestry
tree and FamilySearch without treating them as an automatic three-way mirror. The output
is a person crosswalk, a transfer register and explicit unresolved exceptions.

## The failure to prevent

A matching value or a completed transfer does not demonstrate that its citation,
record URL, event association, note or media survived. Repeatedly copying differently
represented sources can accumulate duplicates. Choose the destination and operation for
each object, then inspect the saved result. The practitioner's citation-duplication case
motivates this check; it is not evidence that every RootsMagic version has the same defect.
[S1, S2, H1, H2, H3]

Use the existing source-citation workflow to build citations and the evidence/proof
judgment recipe to decide identity or contested relationships. This recipe carries an
already-supported decision through the three systems.

## 1. Establish the master and a small working scope

1. Name the database that will hold the current research record. Choosing RootsMagic as
   the master is an explicit project decision, not a requirement that it outrank a better
   documented source found elsewhere. Record its file path and application version. [S1]
2. Back up that database before linking or transferring. Preserve its media files too;
   inspect the installed edition's backup options rather than assuming a database-only
   backup contains media. [H4]
3. Choose a small person/family set and the facts needed for this task. Keep unrelated
   notes and speculative branches outside the proposed sharing scope. [S2]
   This person set scopes subsequent exchanges through an existing connection. A first
   TreeShare upload sends the RootsMagic file, not only this working list. Inspect the
   entire upload file before creating a new Ancestry tree. If its people exceed the
   intended sharing scope, prepare and inspect a separate scoped database first; record
   that the resulting connection belongs to that file. [H1]
4. Confirm authorized editing access to the intended Ancestry tree and FamilySearch
   profiles. Record the target Ancestry tree and its sharing settings before any new-tree
   upload; source, note, media and private-content options are independent choices. [H1]

**Artifact:** `master_database, rootsmagic_version, edition, backup_path_and_time,
media_preservation, working_person_set, initial_upload_file_scope, ancestry_tree_id,
intended_sharing_scope`.

**Checkpoint:** the backup can be located, the media preservation method is explicit and
the receiving tree/profile is named before the first mutation.

## 2. Map the actual people before comparing facts

1. Map each RootsMagic record to the intended Ancestry profile and FamilySearch PID.
   Compare immediate family and identifying records, not only the displayed name.
2. For Ancestry, use TreeShare from the Publish page. Initial upload creates a new
   Ancestry tree; downloading an existing tree creates a new RootsMagic database.
   Do not describe those operations as attaching any existing local file to any tree.
   Record which local file the connection belongs to. [H1]
3. Review a proposed person link before accepting it. Leave competing identities deferred.
   A record appearing in only one tree does not justify adding or deleting a person. [H1]
4. Enable FamilySearch support and sign in if needed. Review the matched FamilySearch
   person before Share Data. AutoMatch establishes links; it does not exchange facts.
   Check generated links before using them to move information. [H5, H6]

**Artifact:** `rootsmagic_record_ref, ancestry_tree_id, ancestry_profile_url,
familysearch_pid, identity_basis, link_state, checked_at, unresolved_candidate`.

**Checkpoint:** every proposed transfer has a verified person pair and direction.
An unresolved identity blocks transfers for that pair.

## 3. Make a separate decision for every object

1. Open the matched pair's comparison. In TreeShare, inspect the fact and the offered
   source/media options before staging an addition or update. Pending changes are not
   saved changes; review them before Accept Changes. [H1]
2. In FamilySearch Share Data, inspect both fact details and the proposed operation.
   Distinguish adding from replacing; some basic events allow only one value, so an
   existing value may have to be replaced rather than preserved as another event. [H2]
3. Record `accept`, `defer` or `already_equivalent`, the direction, source basis and
   proposed add/update operation. Keep both competing values and the reason when deferring.
4. Review sources separately from facts. FamilySearch Sources supports source copying and
   association changes; WebTag URLs are mapped across this transfer. Inspect the citation
   details and the fact/relationship association instead of relying on source counts. [H3]
5. Enter a specific reason when the FamilySearch operation requests one. Deletion,
   detachment and person-merge repair are separate tasks, not shortcuts to make the
   comparison display agree. [H2, H3]

**Artifact:** one row per object: `person_crosswalk_ref, object_type, source_system,
destination_system, original_value, destination_before, record_locator,
decision, operation, reason, attempted_at, result_state`.

**Checkpoint:** every staged change has a destination and a reason. A color or difference
marker identifies a comparison result; it does not decide which fact is supported.

## 4. Reopen the destination and check what arrived

1. Accept only the reviewed batch, then reopen each affected destination profile.
2. Check the saved date/place/name or relationship; then inspect its attached citation,
   URL, source text, note and media when those objects were selected.
3. Compare source content and associations before importing another copy. In S2's worked
   case, custom citations and directly linked Ancestry records were represented differently;
   copying both lists increased the local count without resolving the correspondence.
   Preserve a duplicate candidate rather than repeatedly copying to make counts equal.
4. Open a transferred media item or record link with the intended access. A source URL
   does not by itself establish that an image was copied or is readable locally.
5. Record `verified`, `partial`, `failed` or `deferred` and the exact missing/changed
   field. Correct the supported exception deliberately before starting the next provider
   transfer. [S1, S2]

**Artifact:** `transfer_row_ref, reopened_destination, value_check, citation_field_check,
event_association_check, url_check, media_open_check, duplicate_candidate,
exception, correction_or_next_action`.

**Checkpoint:** success means the selected content is verified in its destination.
Unselected or unavailable objects stay explicit; do not call the whole person synchronized.

## 5. Resume from changed people, preserving the decisions

Use TreeShare's changed-person view or FamilySearch Central's updates list to identify
the next bounded comparison. Recheck the linked person and current destination before
reusing an earlier decision; another FamilySearch contributor may have changed the profile.
Do not disconnect and reconnect a tree merely to clear comparison markers. The current
RootsMagic help warns that disconnecting its Ancestry link cannot simply be undone. [H1, H6, H7]

Stop when the agreed batch is verified and every exception has a next action, or when
access, unresolved identity or the batch budget prevents further supported transfers.

## Prompt pattern

> Prepare a transfer register for this RootsMagic master and these mapped online profiles.
> Keep Ancestry and FamilySearch operations separate. Compare facts, citations, URLs,
> event associations, notes and media individually. For each proposed change show direction,
> add/update choice, evidence and reason. Preserve unsupported differences as deferred.
> Return destination checks and concrete exceptions; do not equate source counts or
> comparison colors with a successfully synchronized person.
