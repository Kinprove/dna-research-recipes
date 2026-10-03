# Recipe: MyHeritage DNA match investigation playbook

## Goal

Produce a small, reproducible investigation packet: a match shortlist, dated notes and labels,
specific shared-match or segment observations, checked theory paths, and a follow-up queue.
Choose the workflow that answers the current question; running all nine is unnecessary.

Use the companion **DNA data export** procedure for export schemas and **DNA match clustering**
for Leeds, AutoClusters and network mechanics. These separate procedures are outside this
playbook; check their availability in your research workspace before delegating those tasks.
Use [DNA research judgment](../../dna-research-recipes/recipes/ai-for-dna-research.md) for
relationship inference, endogamy and evidence weighting. This playbook supplies the MyHeritage
working loop and records, rather than another clustering or cM interpretation method.

## 1. Start with the right kit and preserve theories before relinking

**Use when:** managing several relatives' kits, or a kit appears disconnected from its tree.

1. Select the tested person's kit. Record the tested person, kit identifier as displayed, manager,
   linked tree/profile URL, and research question. Keep manager and tested person separate.
2. Inspect the linked profile before interpreting surnames or theories. Compare its identity,
   parents and tree context with the intended tested person; a matching display name is insufficient.
3. Record which tools this kit can open. An inaccessible tree, Shared DNA Matches panel or theory
   is an access limitation, not an empty result. Advanced-tool access depends on the current
   subscription or the kit's existing unlock status; check the current entitlement page.
4. Before correcting a wrong assignment, save every theory you need: match URL, proposed
   relationship, each path and its component links, displayed confidence, review status and date.
   **MyHeritage says reassignment permanently deletes existing Theory of Family Relativity data.**
5. For a genealogy kit, use Manage DNA kits → kit menu → Re-assign kit to a different person,
   selecting the correct existing profile where available. Recheck the association after saving.
   The documented reassignment procedure does not apply to DNA Health kits.

**Output:** one session header plus a saved theory packet before any reassignment.

## 2. Build a shortlist without losing matches behind an old filter

**Use when:** too many matches, a new branch question, or a surname search seems unexpectedly empty.

1. Start from the selected kit's DNA Matches list. Clear the text search and explicitly inspect
   and remove every unrelated active filter, including labels. Clearing a search is not evidence
   that all filters reset.
2. Write one research question: for example, “Which matches could help identify this grandparent's
   parental village?” Choose a documented relative as an anchor when one is available.
3. Make separate passes for relevant surnames and useful tree information using available
   search/filter controls; inspect ancestral places within match review. Try recorded spelling
   variants. Combined filters use AND: adding a tree or label condition narrows the search.
   The Location filter describes the match's country of residence, not ancestral origin.
   Log the exact query and active filters for each pass; one pass is not whole-list coverage.
4. For a distant-branch question, the tutorial's practical preset is Relationship → Extended
   Family, then Sort by → Largest segments, where those controls are available. Inspect the
   tree-bearing candidates and record the chosen sort; this preset is not a relationship cutoff.
   Save a manageable shortlist with match links, total shared cM, largest segment and segment count
   where displayed, tree availability, reason selected, and next action. A tree or relevant place
   can make a moderate match more useful for this question than an uninformative higher-cM match.
5. Save empty results with their actual query, kit, filters and date. Do not fill an unshown DNA
   measurement with zero or infer that a person outside the list has no shared DNA.

**Output:** shortlist rows and a search log, including filtered negative searches.

## 3. Use labels for branches, notes for evidence, and favorites for follow-up

**Use when:** revisiting the same matches or sorting observations into several possible branches.

1. Define a small label key before assigning colors: e.g. `maternal`, `paternal`,
   `candidate:grandparent-A`, `documented:grandparent-A`, and `needs-tree`. Use names to express
   meaning; colors alone do not explain whether an assignment is tentative.
2. Apply multiple labels when a match belongs in several working groups. MyHeritage supports
   bulk label edits; inspect the selected matches and intended label before applying a batch.
   Only the first seven label dots are displayed, so hidden dots do not establish missing labels.
3. Put the reason and next action in the match note; use this compact template:
   `DATE | question | observation + source URL | branch: candidate/documented | next action`.
   Read and preserve an existing note before updating it. Notes have a documented 2,000-character
   limit; keep the longer evidence record in the investigation packet.
4. Favorite the matches requiring a near-term action. A favorite is a queue marker, not a
   relationship conclusion. Filter by the relevant branch label when resuming work.
5. When evidence changes, update the label and note together, recording why. Keep the dated old
   assessment in the packet so a tentative label cannot later masquerade as original evidence.

**Output:** label key, dated match notes, and a follow-up queue.

## 4. Turn shared matches into specific comparison candidates

**Use when:** an interesting match has too little tree information on its own.

1. Open Review DNA Match for match A and inspect Shared DNA Matches. Record focal kit, A and each
   candidate B as three distinct people; the manager's name is not a substitute for a tested person.
2. For each useful B, copy the displayed relationships and DNA values with the pair they describe:
   focal–A, focal–B or A–B. If a pair's measurement is not displayed, record `not_observed`.
3. Prefer a B who can answer the question: a documented relative, a useful pedigree, or a relevant
   surname/place. Record why B is an anchor or lead before assigning a branch label.
4. Inspect A's and B's trees for specific people and relationships to investigate. Save the
   relevant profile links and the next record or question required.
5. If the next question is about a shared segment, use workflow 5. Being shared matches does not
   establish that all three share the same segment, nor name the ancestor who supplied it.

**Output:** a triplet record with pair-labeled measurements and one concrete next comparison.

## 5. Use the triangulation shortcut, then compare smaller subsets

**Use when:** testing whether a candidate shares a particular segment with a documented relative.

1. In Shared DNA Matches, look for the triangulation indicator. On desktop, hover to see the
   reported number of triangulated segments; click it to load the focal kit, A and B directly
   into the chromosome browser. This avoids manually reconstructing that three-person selection.
2. If using the browser directly, start with the focal kit, one documented relative and one
   candidate. Verify the selected people before reading the display.
3. Record the focal kit, browser's triangulated interval and its exact comparison set. Copy chromosome,
   start/end, cM, SNP count and coordinate build only where shown; otherwise use `not_observed`.
   Do not substitute the endpoints of one person's larger pairwise segment for the group's
   common interval or silently guess a coordinate build.
4. The browser supports up to seven matches plus the focal kit. Adding another match changes
   the group being tested. If the larger group shows no common triangulated interval, return to
   the informative three-person set and test additions separately. Keep each result tied to its
   exact members; a failed larger set does not erase a previously observed smaller set.
5. Record `triangulation_observed` or `no_triangulation_displayed` for that comparison. Overlapping
   bars alone do not establish triangulation. Use the documented relative as a lead to a branch;
   identifying a particular ancestor still requires the pedigree and record investigation.

**Output:** one segment observation per exact comparison set, with display evidence and date.

## 6. Audit a Theory of Family Relativity one connection at a time

**Use when:** MyHeritage proposes a common ancestor or relationship path.

1. Save the proposed relationship, common ancestor, complete path and alternative paths before
   changing its review state. Overall displayed confidence is the lowest confidence of the
   component Smart/Record Match links, not a probability that the relationship is true.
   Record confidence at the connection it describes. Alternative path tabs are different
   evidence routes for the summarized theory; they are not automatically independent proof.
2. Follow every connection into its underlying tree or record. Distinguish a tree-to-tree identity
   match from a parent–child relationship: inspect identity evidence and the parentage asserted
   on either side of the join. Smart Matches and Record Matches can be wrong.
3. Create one row per connection with person/profile links, claim, underlying source, disposition
   (`supported`, `unresolved`, `contradicted`) and the exact next check. A copied claim in two
   trees is one assertion repeated, not two independent records.
4. Compare the proposed relationship with the observed DNA using the judgment recipe; do not
   replace a missing record with the theory's displayed confidence. An unresolved connection
   leaves that path provisional; inspect alternative paths separately.
5. Confirm or reject only after review. Save the reason in the packet. Confirmation tracks your
   assessment; it neither supplies documentary proof nor automatically updates the family tree.
   No theory means no generated suggestion currently visible, not no biological relationship.

**Output:** theory packet, connection ledger and recorded review decision.

## 7. Recover genealogical leads when the match's tree is missing or private

**Use when:** a useful match has no accessible pedigree.

1. Record whether the tree is absent, private, or inaccessible with the present account. Keep
   those states separate; do not invent ancestors from a surname or ethnicity display.
2. Use the match-review features available to the kit: ancestral surnames/places and useful
   shared matches. Save the actual observation and its source, even if it is only a research lead.
3. Look for a shared match with an accessible relevant pedigree and investigate that person's
   branch. Pedigree View shows direct ancestors and leaves out siblings and spouses; open the
   fuller tree when the question needs collateral relatives. Record which kit the accessible
   tree belongs to; it is not automatically A's tree.
4. Form one bounded question for A or the manager, such as a grandparent's birth surname and
   birthplace, or whether a specified documented ancestor appears in their tree.

**Output:** an access-state record, a linked lead, and one answerable question.

## 8. Send a message the match or manager can answer

**Use when:** a particular pedigree detail could resolve the next investigation step.

1. Use Contact on the DNA-match card. Identify whether the recipient manages another person's
   kit; address the tested person's relationship in the question.
2. Draft a short message naming the tested people, displayed shared DNA, research question, one
   relevant surname/place or profile link, and the one requested detail. Offer the equivalent
   detail from your own research. Contact from DNA-match cards is documented as free; access
   rules for other contact routes or private trees can differ.
3. Save the draft and obtain the researcher's approval before an assistant sends it. Record the
   sent date, recipient and question; keep reply/no reply separate from an evidence conclusion.
4. On a reply, attach its source and date, then update the next action. A reported family story
   starts a record search; an unanswered message does not contradict a relationship.

**Output:** approved message and correspondence row.

## 9. Resume with comparable snapshots and a preserved evidence packet

**Use when:** returning after weeks, a theory update, or a change in access/tool availability.

1. Reopen the same kit and research question. Record today's access state, queries and filters;
   compare with the saved session header before comparing lists.
2. Review the branch label and favorite queue, read the notes, and perform the recorded next
   actions. Check unresolved theory connections rather than accepting a new badge as validation.
3. Save the shortlist, comparison sets, theory paths and correspondence with dates and source
   links. Use available exports only after verifying their presence and actual coverage for this
   kit. If an export is unavailable, preserve the selected displayed evidence manually and mark
   the packet's scope as `selected_matches`, never `complete_match_list`.
4. Match observations across sessions using stable match links/identifiers where available.
   Record additions, changes and unavailable observations. A disappeared row under changed
   filters or access is not evidence that shared DNA became zero.

**Output:** dated packet and a next-session queue with its actual coverage.

## Artifact schemas

These are investigator-created schemas, not claims about native MyHeritage CSV headers.
Use ISO dates and `not_observed` for unshown values. Keep personal match data in the researcher's
private workspace; the recipe and its examples contain no real match records.

| Artifact | Required fields, in order |
| --- | --- |
| Session | `observed_at, focal_kit_ref, tested_person, manager_ref, linked_profile_url, question, access_state, query, active_filters, sort_by, coverage` |
| Search log | `observed_at, focal_kit_ref, question, query, active_filters, sort_by, coverage, result_state, shortlist_refs, next_action` |
| Match shortlist | `focal_kit_ref, match_ref, match_url, observed_at, shared_cm, largest_segment_cm, segment_count, tree_state, labels, selection_reason, evidence_ref, next_action` |
| Label key/history | `observed_at, focal_kit_ref, match_ref, label_name, color, meaning, prior_label, new_label, reason, evidence_ref` |
| Triplet | `observed_at, focal_kit_ref, match_a_ref, match_b_ref, focal_a_cm, focal_a_relationship, focal_b_cm, focal_b_relationship, a_b_cm, a_b_relationship, anchor_basis_ref, source_url, next_action` |
| Segment observation | `observed_at, focal_kit_ref, comparison_set_refs, chromosome, start_bp, end_bp, segment_cm, snp_count, coordinate_build, triangulation_state, evidence_ref, branch_hypothesis, next_action` |
| Theory packet | `observed_at, focal_kit_ref, match_ref, match_url, theory_ref, proposed_relationship, common_ancestor_ref, path_refs, saved_evidence_refs, displayed_confidence, review_state, decision_reason` |
| Theory connection | `observed_at, match_ref, theory_ref, path_ref, connection_ref, claim, profile_urls, underlying_source_ref, displayed_confidence, disposition, next_check` |
| Correspondence | `match_ref, recipient_ref, draft_ref, approved_at, sent_at, question, reply_state, reply_source_ref, next_action` |

Completion means the selected workflow has its output record, source links, observation date and
next action. An inaccessible tool stays recorded as inaccessible; it is never a completed check.
