# WikiTree: Link DNA Tests to the Correct Tester and External Kit

## Goal

Make a WikiTree profile and its external DNA-test links point to the actual tested person,
then preserve what each displayed DNA connection represents. The output is a private
tester/link register plus a source-linked list of pedigree leads.

## The failure to prevent

Adding test details to WikiTree does not upload genotype data or establish a DNA match.
A DNA Connections list follows the tree and registered tests. An external tree link can
open the right website while pointing to the wrong relative. Verify the person, provider
and link destination independently. [S1, S2, S3]

Use the existing AncestryDNA match-investigation workflow for general tester-versus-manager
identity checks and cross-site kit confirmation. Use the DNA research judgment recipes for
measured sharing, inheritance-path eligibility and relationship conclusions.

## 1. Register the test on the tested person's profile

1. Establish which WikiTree profile represents the tester. Preserve its ID and the
   documentary identity basis; the signed-in member and kit manager can be different people.
2. Open that person's DNA Tests page. Read the named person in the page header before
   selecting an existing test or adding one. Confirm permission to edit both this profile
   and the test information. [S2, S3]
3. Select the testing company and actual test type/level. Enter only verified provider
   identifiers, usernames and haplogroup labels in the applicable fields. Keep a reported
   haplogroup's laboratory/test basis beside it; a consumer autosomal haplogroup label
   does not become a dedicated Y-DNA or mtDNA test.
4. For a transferred test, keep the original testing company and the external uploaded-kit
   association distinct. Add the GEDmatch kit ID in the applicable WikiTree test field;
   do not describe GEDmatch as the laboratory that performed the original test. [S3]
5. Save, reopen the test entry and check the company, type, identifier and tester again.
   Repeat for a genuinely separate test or provider registration, without counting the
   same person's repeated registrations as independent evidence. [S2, S4]

**Artifact:** `tested_person_handle, wikitree_id, manager_handle, permission_reference,
provider, test_type_and_level, external_kit_reference, username_if_required,
haplogroup_report_reference, saved_at, reopened_entry_check`.

**Checkpoint:** the DNA Tests header names the tester; every entered value can be traced
to that person's provider account or report. Keep kit numbers and living-person details
in the private register.

## 2. Verify the correct external linking mechanism

These routes use different inputs. Completing one does not establish that the other link
works or that a pedigree connection is genetically confirmed.

| Provider | Connection route | Destination check |
| --- | --- | --- |
| FamilyTreeDNA | In the intended kit's Account Settings → Genealogy → Family Tree area, enter the tester's WikiTree ID in the WikiTree field and save. This can coexist with a connected MyHeritage or archived FamilyTreeDNA tree. [S1] | Reopen the setting. Where an authorized match/profile view offers the tree, select WikiTree and verify the tester's ID and expected immediate family. |
| GEDmatch | Enter the correct GEDmatch kit ID on the tester's WikiTree test entry. The documented integration uses that association to link GEDmatch results to the WikiTree compact pedigree. [S2, S3] | After the link appears, follow it from the intended kit's available view. Inspect the kit's current public-link/alias settings and the actual displayed visibility before broadening sharing. |

For FamilyTreeDNA, a tree menu may offer several trees; selecting the first icon without
checking its destination is insufficient. The vendor also documents a WikiTree link on
the match's Profile Card. A missing option means the view supplied no usable link; record
that state before investigating the saved ID and access. [S1]

For GEDmatch, the older tutorial shows alias settings affecting whether a WikiTree link
is public. Preserve the current setting and inspect the offered control; do not change an
alias or expose a link merely to make the tutorial's screenshot match. Test registration
and external link visibility can update separately. Record `pending` and a later check
date rather than promising the tutorial's historical processing time. [S3]

**Artifact:** one row per provider: `tested_person_handle, provider, private_kit_reference,
link_input_type, saved_input, previous_setting, saved_at, observed_at, view,
link_status, destination_wikitree_id, visibility_checked, remaining_action`.

**Checkpoint:** each observed link reaches the intended tester. A saved setting,
an unavailable match view and a verified destination are different completion states.

## 3. Turn propagated connections into a bounded research queue

1. On one relevant ancestor's profile, inspect DNA Connections or the Ancestors/Descendants
   view. Record the ancestor and tester IDs, displayed test/company and the tree path
   connecting them. [S2]
2. Preserve the date and exact view. Inspect the parent-child links needed by the path and
   mark undocumented links for research. Adding a test and extending a tree can populate
   further connections; that propagation supplies candidates for investigation. [S2]
3. Open an external company link only with authorized access. Save an actual comparison
   separately with its tested pair, tool and settings when one is obtained.
4. Keep separate columns for `tree-derived_connection`, `measured_comparison_available`
   and `relationship_confirmation_basis`. Leave unavailable comparisons unavailable.
   Do not mark a relationship DNA-confirmed solely because a tester appears in a list
   or because the external tree link works.
5. Hand the relevant pedigree paths and actual comparison records to the existing
   autosomal, Y/mtDNA or X-DNA judgment recipe. Stop this workflow once the registrations,
   observed links and remaining research tasks are recorded.

**Artifact:** `ancestor_wikitree_id, tester_wikitree_id, observed_at, view,
registered_test, displayed_path, unsupported_links, external_comparison_reference,
confirmation_basis, next_document_or_comparison`.

**Checkpoint:** a reader can distinguish a registered test, a pedigree-derived display
and a measured DNA observation without inferring one from another.

## Prompt pattern

> Build a WikiTree tester/link register for these authorized profiles and kit records.
> Verify the DNA Tests header and distinguish tester from manager. Use the provider-specific
> linking route, then record saved settings and independently observed destinations.
> Return pending, inaccessible and verified links separately. Extract pedigree-derived
> DNA Connections as leads; attach measured comparisons only when their actual records
> are supplied. Do not infer a DNA match or confirmed parent-child link from a tree icon.
