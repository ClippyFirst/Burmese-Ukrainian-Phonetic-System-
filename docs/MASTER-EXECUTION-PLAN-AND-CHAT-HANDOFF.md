# Master execution plan and chat handoff — Burmese → Ukrainian

**Last reviewed:** 2026-10-25  
**Repository:** https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-  
**Default branch:** `main`  
**Baseline SHA for this checkpoint:** `e7ade446b06cd11f2f97ae28905e1aee9f6d1f48`  
**Status:** research prototype; not release-ready; no independently adjudicated IPA gold entries verified.

## Operating contract

Preserve the pipeline:

Myanmar orthography → grapheme/syllable structure → source-language phonology → typed IPA/phonetic result → Ukrainian target adaptation → Ukrainian practical orthography.

A valid Unicode cluster is not proof of a Standard Burmese word, a structural parse is not a phonological analysis, and a candidate Ukrainian spelling is not evidence of correct pronunciation. Keep uncertainty and unsupported states explicit. Do not fill missing outputs with guesses.

## Task ledger

| ID | Priority | Status | Scope and evidence | Acceptance criteria / blocker |
|---|---|---|---|---|
| BUR-STRUCT-001 | P0 | PARTIAL | Python parser recognizes Myanmar blocks, kinzi, virama/subjoined consonants, medials, vowel signs and malformed states; `tests/test_parser.py` covers basic structures. | Build an independently annotated segmentation corpus and verify Python/browser parity across combining marks, mixed scripts and ambiguous boundaries. |
| BUR-INV-001 | P0 | PARTIAL | Main consonant, medial and vowel-sign inventories are represented. | Enumerate valid/invalid combinations and support each phonological generalization with a source-located example and counterexample. |
| BUR-VOW-001 | P0 | TODO | Dependent and inherent vowels are structurally represented; full combination derivation is not implemented. | Implement only source-backed context rules; test length, quality, medials, coda and lexical exceptions against a reviewed reference set. |
| BUR-CODA-001 | P0 | TODO | Some coda structure is parsed, but complete checked-syllable realization is not established. | Establish final inventory and checked-syllable behavior with source-located, variety-labelled examples and regression tests. |
| BUR-PROS-001 | P0 | BLOCKED | Traditional tone and newer register/tone analyses are documented as competing accounts; runtime does not implement a validated tone/register/phonation model. | Specialist adjudication and suitable source data are required before a deterministic full prosodic model can be accepted. |
| BUR-IPA-001 | P0 | PARTIAL | Conservative IPA seed exists; browser has a separate handwritten derivation. | Define one inspectable IPA contract, preserve broad vs surface IPA and provenance, and verify cross-runtime parity on an adjudicated corpus. |
| BUR-UA-001 | P1 | PARTIAL | Practical candidates are table-driven and use explicit not-established fallback; canonical Ukrainian inventory is external. | Validate feature-distance ranking and every target policy choice against the canonical inventory; do not infer official normativity. |
| BUR-GOLD-001 | P0 | BLOCKED | `data/burmese/phonology_corpus.csv` has six structural probes, not phonological gold; verified independent IPA gold count is 0. | Create a rights-cleared, independently adjudicated lexical corpus with source locator, dialect, transcription convention, IPA, uncertainty and review status before reporting accuracy. |
| BUR-LIC-001 | P1 | BLOCKED | No root project license is declared; `CITATION.cff` uses `NOASSERTION`. The myG2P dictionary is CC BY-NC-SA 4.0. | Owner must select the code/data licensing policy. Do not bundle myG2P data or infer reuse permission from public visibility. |
| BUR-BOUNDARY-001 | P1 | DONE_VERIFIED | PR [#33](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/33) merged as `e374266af5e8fe67e779d01be6d29a56a33d1578`. The U+AA60 Khamti letter is recognized as Myanmar-block text but remains outside the Standard Burmese onset inventory. | Exact-head CI [40215282144](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40215282144) passed pytest, npm build, generated-data drift check, npm tests and Playwright browser tests. This is a script/language boundary test, not phonological gold and not an accuracy improvement. |

## Existing work to preserve

- Unicode normalization entry point and conservative grapheme/syllable parser.
- Explicit kinzi, conjunct/subjoined consonant and four-medial representation.
- Evidence and competing-analysis datasets.
- Conservative IPA seed and separate practical target adapter.
- Russian practical transcription as documentary comparator, not as Ukrainian truth.
- Explicit `inventory_unavailable` and `not_established` fallbacks; no hidden Ukrainian fallback table.
- External Epitran benchmark harness as an optional comparator, not a runtime dependency.
- Existing license audit: do not copy myG2P dictionary entries into tests, corpus or generated artifacts without a rights/compatibility review.

## Verification state

- Main CI runs [40211924300](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40211924300) and [40211924324](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40211924324) were reported successful in the prior checkpoint. They validate the then-current code and test suite, not linguistic completeness.
- PR #33 initially failed in run [40215189582](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40215189582) because the test expected `None` while the documented model serializes an absent onset as an empty object. The assertion was corrected to the model contract, then exact-head run [40215282144](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40215282144) passed all Python, build, generated-data, Node and browser checks. PR #33 merged as `e374266af5e8fe67e779d01be6d29a56a33d1578`.
- No local test run is claimed for this checkpoint.
- Independent gold-corpus size: **0 verified entries**. Word-level IPA accuracy and Ukrainian name-level accuracy are **not measured**.

## Next actions, in dependency order

1. Finish exact-head CI for PR #33; fix and rerun if it fails, then merge only after checks pass.
2. Add a machine-checkable source/claim-to-rule link audit, ensuring every implemented phonological rule has a scope, source locator, uncertainty label and test reference.
3. Define a cross-runtime structural contract for normalization, token boundaries, unknown code points and unsupported combinations; test Python and browser against the same fixtures.
4. Build a small, rights-cleared adjudicated lexical corpus before extending deterministic IPA rules. Keep structural probes separate from gold.
5. Implement vowels and codas in evidence-backed slices, one accepted environment at a time; add negative cases for plausible but unsupported spellings.
6. Address tone/register/phonation only after source and specialist adjudication; preserve competing analyses rather than averaging them.
7. Revisit release readiness only after the IPA contract, independent corpus, target-inventory integration, license decision, reproducible tests and release metadata all meet their acceptance criteria.

## Readiness rule

Do not mark the repository 80% ready based on file count, test count, UI completeness or successful CI alone. A readiness estimate must be tied to explicit layer-level acceptance criteria. Until independent lexical IPA gold and comprehensive source-phonology coverage exist, this remains a **partial research prototype**, not a release-ready transcription engine.


## Burmese misplaced-virama fail-closed guard — 2026-10-25

- Adversarial parser review found that U+1039 (virama) is correctly consumed in the onset/conjunct loop but was also accepted by the generic trailing-special-sign loop. A misplaced virama after a vowel could therefore leave the syllable marked structurally established and let the conservative IPA adapter emit a plausible-looking prefix.
- The trailing-special parser now treats virama outside the conjunct position as invalid and returns before IPA generation. Added a regression for `ကာ္` that requires invalid status and withheld IPA.
- This is malformed-input integrity, not a new phonological rule or accuracy claim. Exact-head CI must pass Python tests, schema checks, generated-data drift, and browser/build checks where configured. Independent adjudicated Burmese IPA gold remains 0.


## Post-merge current-head checkpoint — 2026-10-25

- Misplaced-virama fail-closed fix merged as `8b96926897f54841daf442ff67ee0f73593004f2` via [PR #35](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/35).
- Exact PR-head tests [40216523493](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40216523493) passed. Post-merge `main` tests [40216622672](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40216622672) and Pages deployment [40216622638](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40216622638) passed.
- U+1039 outside the conjunct sequence is now invalid rather than silently consumed as a trailing sign. This is malformed-input integrity, not phonological coverage. Independent adjudicated gold remains 0; vowel combinations, coda/checked syllables, tone/register/phonation and target-policy adjudication remain open.


## Evidence-registry schema checkpoint — 2026-10-25

- Main commit after PR [#39](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/39): `8a2482535c463a9371f7c0c6ac32c15880b7485c`.
- Every row in `sources.csv`, `source_claims.csv`, and `phonological_rules.csv` now validates against explicit JSON Schemas; IDs are unique and each rule's source and claim are checked for referential consistency. Exact-head test workflow [40222099466](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40222099466) passed.
- Remaining data-integrity work: schema and validation of `phonology_corpus.csv`, including enforcement that `STRUCTURAL_ONLY` entries cannot contain asserted IPA or Ukrainian gold fields. This must not be confused with source-language phonological validation.
- Linguistic blockers remain unchanged: 0 independent lexical IPA gold entries, incomplete source-adjudicated vowels/codas, no complete tone/register/phonation runtime model, and no Ukrainian name-level gold.


## Corpus evidence-schema checkpoint — 2026-10-25

- Main commit after PR [#41](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/41): `3c8f03957fb3d8b8201bafac0dcdc819f50b8fe1`.
- Added `schemas/phonology_corpus.schema.json`; every corpus row now validates against a schema. The contract prevents structural probes from carrying expected IPA/Ukrainian outputs and requires adjudication metadata before any row can be labeled `GOLD_VERIFIED`.
- Exact-head full workflow [40222516985](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40222516985) passed tests, build, generated-data checks and browser tests.
- Linguistic evidence is unchanged: six structural probes, zero independently adjudicated lexical IPA gold entries, no word-level accuracy estimate. Next genuine blocker is specialist/source-located adjudication, not additional schema machinery.


## Unicode corpus locator checkpoint — 2026-10-25

- Main commit after PR [#43](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/43): `0c793b76f45261c9d9044e0eac01245a8afef54f`.
- The three Unicode-sourced structural rows now point to §16.3.1 / Table 16-4 in Unicode 18.0.0. Their status remains structural-only; no IPA/Ukrainian expected values were added.
- Exact-head test/build/generated-data/browser verification passed in [40223402689](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40223402689). Optional Epitran comparison [40223406632](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40223406632) is not gold evidence.
- Remaining source-data work: inspect Green 2002 at exact source pages, then obtain independent IPA adjudication. No accuracy estimate is currently justified.


## Romanization standard and crosswalk checkpoint — 2026-10-31

- Added [romanization-to-ukrainian-matrix.md](romanization-to-ukrainian-matrix.md) with the standard decision, licensing notes, initial onset/rhyme crosswalk and explicit task ledger.
- Selected MLCTS as the separate orthographic romanization profile. Mya2Rom documentation identifies MLCTS as an orthographical transcription system created by the Myanmar Language Commission and distinguishes it from modified MLCTS / MLCTS2, described as more phonetic. This matches the product contract: written-form romanization is separate from IPA-first phonetic adaptation.
- The browser now calls mya2rom(part, "mlcts") and the result card is labelled MLCTS. The regression uses the Mya2Rom documented sample မြို့: MLCTS must return mrui., while MLCTS2 returns mjou.
- Test-first RED: workflow [41228903857](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41228903857) failed only the new profile assertion as intended (expected mrui., received mjou.; 46 browser tests passed, 1 failed).
- Exact-head GREEN: workflow [41229019002](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41229019002) passed: pytest 61 passed / 29 subtests passed; npm build; generated web data drift check; Node tests; Playwright 47 passed. This verifies the profile selection and UI label, not complete MLCTS coverage or a Ukrainian romanization adapter.
- PR #54 contains the standard decision, crosswalk, test-first regression and MLCTS runtime switch.
- The existing Mya2Rom vendor files and CC-BY-SA-4.0 notice are preserved. The upstream README identifies Wikipedia/Wiktionary-derived table material; row-level source scope and attribution must remain explicit.
- Task statuses: MYA-ROM-STD-001 DONE_VERIFIED (source review); MYA-ROM-PROFILE-001 TODO; MYA-ROM-UA-001 TODO; MYA-ROM-MATRIX-001 PARTIAL; MYA-ROM-LIC-001 PARTIAL; Burmese contextual IPA and independent lexical gold remain PARTIAL.
- Branch: work/romanization-matrix-completion-20261031. No runtime code changed in this checkpoint; no new test result is claimed.


## MLCTS onset crosswalk data checkpoint — 2026-10-31

- Added data/burmese/romanization_ukrainian.csv with all 35 source consonant/onset graphemes present in the vendored Mya2Rom MLCTS column. Every row records source form, MLCTS form, Ukrainian candidate, evidence status, source URL and a source locator.
- Added tests/test_romanization_matrix.py. It checks exact onset inventory and MLCTS values against the reviewed table, unique source-unit keys, HTTPS provenance, locators, allowed statuses and non-empty values for PROPOSED rows.
- Test-first RED: workflow [41229203729](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41229203729) failed because the canonical CSV did not yet exist (61 prior Python tests passed; 2 new tests failed for the intended missing-file reason).
- Exact-head GREEN: workflow [41229245383](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41229245383) passed: pytest 63 passed / 29 subtests passed; npm build; generated web data drift check; Node tests; Playwright 47 passed.
- The CSV intentionally leaves several Ukrainian onset candidates EVIDENCE_LIMITED; this is not a missing-data bug. It prevents guessed values for MLCTS units such as g/gh, c/hc, j/jh and dh until source phonology and Ukrainian target adaptation are adjudicated.
- MYA-ROM-MATRIX-ONSET-001 is DONE_VERIFIED as an engineering/source-table inventory. MYA-ROM-MATRIX-001 remains PARTIAL because medial, vowel, coda, independent-vowel, kinzi, asat, numeral and punctuation rows and the syllable adapter remain outstanding.


## Two-method result UI checkpoint — 2026-10-31

- Added an accessible two-button method switch: **Фонетичний** and **За романізацією**. The default remains phonetic.
- The phonetic panel contains IPA, Ukrainian phonetic output, structural analysis and phonetic issue notices.
- The romanization panel contains MLCTS output and a clearly labelled PARTIAL Ukrainian crosswalk state linked to the canonical matrix. It does not reuse IPA or phonetic Ukrainian output as a fallback.
- Test-first RED: workflow [41230002926](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41230002926) failed because the method controls and panel IDs did not exist.
- The first implementation run [41230226358](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41230226358) passed Python, build, generated-data and Node tests plus 47 browser tests, but an existing browser assertion still expected the old card order. The assertion was updated to include the new romanization→Ukrainian status card.
- Exact-head GREEN [41230424775](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41230424775): pytest 63 passed / 29 subtests passed; npm build; generated-data drift check; Node tests; Playwright 48 passed.
- The MLCTS → Ukrainian syllable adapter remains incomplete; the tab shows PARTIAL rather than falling back to IPA. The MLCTS romanization output itself is kept separate from phonetic analysis.


## Production Pages artifact correction — 2026-10-31

- Audited open PR #48 (Fix MLCTS2 romanizer asset in GitHub Pages build). It was 4 commits behind main, had merge conflicts, and its proposed changes were not merged blindly. Ported only the necessary production-artifact behavior to this fresh branch.
- Added scripts/copy-vendor-assets.mjs to copy both Mya2Rom browser files into Vite's public output; Vite now builds both index.html and system.html; Playwright now tests the built preview rather than the dev server.
- Added a production-artifact test requiring dist/index.html, dist/system.html, dist/vendor/mya2rom/romanisations.js and dist/vendor/mya2rom/mya2rom.js, plus a browser assertion that window.mya2rom is loaded from the built artifact.
- Updated test:browser to build before preview; CI uses test:browser:built after its single explicit build, so build/test/deploy use the same artifact without duplicate builds.
- Test-first RED: workflow [41230779647](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41230779647) failed as intended because dist/system.html was absent from the previous production build.
- Exact-head GREEN: workflow [41230976020](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41230976020) passed: pytest 63 passed / 29 subtests passed; production build; generated-data drift check; Node 3/3 passed including the new artifact test; Playwright 48 passed against Vite preview.
- This proves the production build contains the service page, methodology page and both Mya2Rom assets. A post-merge GitHub Pages deployment is still required before claiming the live site has the corrected artifact.


## Final main / Pages checkpoint — 2026-10-31

- Final main commit: fff943db823ae5ca0f4fed50b572cc75cb743f84.
- PR #54: MLCTS profile and onset matrix; PR #55: two separate method tabs; PR #56: production asset copy, multi-page build and preview-based browser tests.
- PR #48 was closed as superseded by #56; its old branch was left intact. PR #53 styling work remains open and untouched.
- Main verification [41231199684](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41231199684) passed: pytest 63 + 29 subtests; Node 3/3; Playwright 48 against the built artifact.
- Pages deployment [41231199596](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41231199596) succeeded: https://clippyfirst.github.io/Burmese-Ukrainian-Phonetic-System-/ .
- Final statuses: MYA-ROM-PROFILE-001 DONE_VERIFIED; MYA-ROM-MATRIX-ONSET-001 DONE_VERIFIED; MYA-ROM-MATRIX-001 PARTIAL; MYA-ROM-UA-001 TODO; MYA-PAGES-ARTIFACT-001 DONE_VERIFIED; MYA-PHONETIC-COVERAGE PARTIAL/BLOCKED pending independent lexical gold and expert adjudication.
- The romanization tab's Ukrainian result is intentionally PARTIAL. Do not claim full romanization coverage until a complete source → MLCTS → Ukrainian syllable matrix and adapter pass exact coverage tests.


## MLCTS rime inventory continuation — 2026-10-31

- User confirmed the two-method contract: orthographic MLCTS → Ukrainian table adapter must be independent from phonetic IPA → Ukrainian adaptation. The romanization route is intended to cover supported written units; the phonetic route may withhold unsupported pronunciation.
- Added `data/burmese/romanization_rimes_inventory.csv` with **94 rime keys** and their exact MLCTS column values extracted from the vendored Mya2Rom 0.4.4 `vowels` object. Every row records the upstream repository, file/object locator and an explicit warning that Mya2Rom's extended tables are not direct proof of an original MLC publication. No Ukrainian candidate is assigned; every row remains `EVIDENCE_LIMITED` pending source-level and target-language adjudication.
- Added `tests/test_romanization_rime_inventory.py` to verify the inventory count, unique source keys, non-empty MLCTS values, provenance, explicit evidence status and the absence of unsupported Ukrainian candidates.
- Existing 35-row onset crosswalk, MLCTS profile, method tabs and production Pages asset-copy fix are preserved. This new inventory does not complete the MLCTS → Ukrainian syllable adapter or the medial/coda/contextual orthographic coverage audit.
- Status: MYA-ROM-RIME-INVENTORY-001 = implementation added, CI verification pending; MYA-ROM-MATRIX-001 remains PARTIAL; MYA-ROM-UA-001 remains TODO; full IPA/phonological coverage remains PARTIAL/BLOCKED pending independent lexical gold and specialist adjudication.
- Branch: `work/romanization-evidence-completion-20261031`. Changes are isolated from `main`; do not mark the new tests DONE_VERIFIED until the exact PR-head workflow passes.

- Added `tests/web/romanization-rime-inventory.test.mjs` to compare all 94 CSV source keys and MLCTS strings directly against the vendored Mya2Rom `vowels` object, so the inventory cannot silently drift from its attributed upstream implementation.


## MLCTS rime parity test correction — 2026-10-31

- The first PR workflow [41232402326](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41232402326) passed Python (64 tests + 29 subtests), build and generated-data drift checks, then failed the new Node parity test at parse time because an escaped quote was expressed as an invalid Unicode-mode regular-expression escape.
- Removed the unnecessary quote-unescape regex; the vendored MLCTS strings in the source table do not require it. The parity test still checks every source key and MLCTS value against the vendor table. Exact-head rerun is pending.
- The official BGN/PCGN 1970 guide and UNGEGN Burmese report were inspected. They establish BGN/PCGN 1970 as a geographical-name system and state that the system is not reversible; Mya2Rom documentation distinguishes MLC-created orthographic MLCTS from the more phonetic modified variant. The matrix now records why standard MLCTS is selected for the orthographic mode, while the original MLC publication remains a source-retrieval blocker.


## Verified MLCTS rime inventory and standard rationale — 2026-10-31

- Exact PR-head workflow [41232548770](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41232548770) checked out merge commit for head `a514943e96d8e2b5bc5fc8815898cb96aae39721` and passed: pytest **64 passed / 29 subtests passed**; Vite build; generated web-data drift check; Node **4/4** tests (including the 94-row vendor parity test); Playwright **48 passed** against the built artifact.
- The preceding workflow [41232402326](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41232402326) passed Python/build/drift checks but failed the new Node test due an invalid Unicode-mode regex escape. The unnecessary quote-unescape regex was removed; the exact-head run above is green.
- `MYA-ROM-RIME-INVENTORY-001` is `DONE_VERIFIED` as a vendor-derived inventory and parity-tested dataset. `MYA-ROM-MATRIX-001` remains `PARTIAL`; `MYA-ROM-UA-001` remains `TODO`; `MYA-ROM-LIC-001` remains `PARTIAL` pending original MLC source and full attribution scope review.
- The matrix now explains why MLCTS (the orthographic MLC transcription profile) is selected over BGN/PCGN 1970 for general written-text mode. BGN/PCGN 1970 remains a useful geographical-name comparator, but UNGEGN says it is not reversible and PCGN notes that some choices depend on pronunciation. The original MLC publication has not yet been obtained; Mya2Rom's vendor data remains a secondary implementation source.
- No runtime files changed in this PR; no new Pages deployment is required. Existing site: https://clippyfirst.github.io/Burmese-Ukrainian-Phonetic-System-/.
- Verification PR: [#59](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/59), branch `verify/romanization-evidence-20261031`. PR #58 contains the earlier test attempt and is superseded by #59.


## Post-merge main checkpoint — 2026-10-31

- PR #59 merged by squash as `d468c6ec16289009da553ed4696932e7c7f7d79f`; this is the main-branch implementation merge SHA for the romanization evidence inventory.
- Exact code-verification workflow [41232548770](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41232548770) passed: 64 Python tests + 29 subtests; Vite build; generated-data drift check; Node 4/4; Playwright 48 against the built artifact passed. The exact code-verification run checked out head `a514943e96d8e2b5bc5fc8815898cb96aae39721`; subsequent changes before merge were documentation-only.
- The bounded source inventory and its tests are now on `main`. The overall orthographic matrix and runtime adapter remain incomplete; see the PARTIAL/TODO statuses above.
- No runtime behavior or Pages build inputs changed in this PR; the already deployed GitHub Pages site remains the existing public service. A new Pages deployment was not necessary for these data/documentation-only changes.


## Final main SHA and merged MLCTS inventory — 2026-10-31

- The 94-row MLCTS rime inventory, Python provenance tests, Node vendor-parity test and standard-selection rationale were merged by PR #59 as `d468c6ec16289009da553ed4696932e7c7f7d79f`; the post-merge handoff checkpoint PR #60 merged as `085c2a7bdf7aae3292122a17552bfc92af6d726c`. This is the main head before this final handoff-only update.
- Exact-head workflow [41232548770](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41232548770) passed: pytest 64 + 29 subtests; Vite build; generated-data drift; Node 4/4; Playwright 48.
- Remaining acceptance: obtain and verify original MLC source; complete medial/vowel/coda/marker inventory; adjudicate Ukrainian rime candidates; implement independent MLCTS syllable → Ukrainian adapter; expand IPA lexical gold. No runtime changes or new Pages deployment were made.


## Open styling PR reconciliation — 2026-10-31

- Rechecked open PR #53 (`design/burmese-layout-20261030`) against current `main` `edbd9d52c280968592e2b84c19e4d8a8fc2bf614`: branch is diverged, 5 commits ahead and 7 behind; merge base is `272da3970c0e8791c5bc5406cc4289e2c841eeef`. Its changes are limited to `index.html`, `system.html`, `src/web/styles.css`; the layout-contract test is present in its diff.
- PR #53 remains open and untouched. Do not merge blindly: first rebase/port the CSS and test changes onto a fresh branch from current `main`, then run current browser tests and review the built Pages artifact. No styling work was cherry-picked in this checkpoint.
- The MLCTS rime inventory and its 64 Python tests + 29 subtests, Node 4/4, Playwright 48 and Vite build verification remain preserved on `main`; the MLCTS → Ukrainian adapter and primary MLC source remain open research/implementation blockers.

 
## Responsive layout merge and verification — 2026-10-31

- PR [#62](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/62) was merged by squash as `78f56512f59bbfa6fc881ccd35e34c4bf1fff7b1`.
- The PR adds 36 focused responsive CSS override lines in `src/web/styles.css`, preserving current IPA typography and method-switch styles instead of replacing the stylesheet from diverged PR #53.
- Exact PR-head tests workflow [41234651088](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41234651088) completed successfully. The job passed `pytest`, Vite build, generated-data drift check, `npm test`, Playwright Chromium installation, and `npm run test:browser:built`.
- PR #53 remains open and untouched: its branch is diverged; the focused responsive behavior was ported without merging the older stylesheet/test snapshot wholesale.
- This UI-only merge does not complete original MLC source retrieval, full MLCTS rime/medial inventory, Ukrainian syllable adapter, or independent phonetic gold. Research prototype status remains unchanged.
- A new Pages deployment after this merge has not yet been verified; inspect the deployment workflow before claiming the live site contains this CSS.


## MLC primary-source retrieval follow-up — 2026-10-31

- A further source search located the Library of Congress 2011 *Burmese Romanization Table* PDF. It is an ALA-LC table, not the original MLC/MLCTS publication; it was explicitly excluded as evidence for MLCTS values. It does document separate conventions for medials, conjuncts, finals, tone marks, punctuation, numerals and word division, but those rules must not be silently imported into the MLCTS profile.
- The SIL catalogue link surfaced by secondary bibliographic metadata returned HTTP 403 in this environment. No original Myanmar Language Commission publication or primary MLCTS table was obtained in this pass.
- Therefore the MLC-source task remains BLOCKED/EVIDENCE_LIMITED. The 94-row inventory remains a vendor-derived Mya2Rom parity inventory, not a primary-source-verified MLC transcription table. No new Ukrainian candidate or pronunciation was inferred.


## Browser output integrity regression — 2026-10-31

- PR [#64](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/64) merged as `d0b7f6351a4151b974ec9ee379f81f7a06da9613`.
- Reproduced a real browser data-loss bug: `ကာ ꩠ` yielded only `ка `; the unsupported Myanmar unit disappeared from the Ukrainian output. The fix now renders unresolved/unsupported units as `⟦source⟧` and withholds incomplete syllable-level mappings.
- Corrected contextual initial `/j/` + vowel status aggregation so the established project behavior `/juː/ → ю` remains visible without requiring a separate standalone `/j/` mapping.
- Added Playwright coverage for the exact full Burmese greeting sentence. The test reconstructs the normalized input from rendered segment rows and verifies that no source unit, whitespace or punctuation is lost; it explicitly checks the unresolved marker and does not assert unsupported linguistic gold.
- Exact-head CI [41238825573](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41238825573) passed pytest 64 + 29 subtests, Node 4/4, production Vite build, generated-data drift, and Playwright 50/50.
- New tasks: `MYA-OUTPUT-PRESERVATION-001` DONE_VERIFIED; `MYA-SENTENCE-INTEGRITY-001` DONE_VERIFIED. Full sentence-level phonetic accuracy remains BLOCKED/EVIDENCE_LIMITED; `MYA-ROM-UA-001` remains TODO; primary MLC source retrieval remains BLOCKED.
- Pages deployment [41238926334](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41238926334) completed successfully and published `d0b7f6351a4151b974ec9ee379f81f7a06da9613` at https://clippyfirst.github.io/Burmese-Ukrainian-Phonetic-System-/. Main workflow [41238926148](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41238926148) also passed.

## Full-sentence MLCTS and Myanmar punctuation/numeral preservation — 2026-10-31

- Main head: \`b6ce024a26bef44c76744aa231b52de551c12c16\` (PR #69).
- PR #68 added a full Burmese greeting sentence to the browser MLCTS route. Its exact-head workflow [41240518900](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41240518900) passed the Python, Vite build, generated-data, Node, and built-artifact Playwright gates.
- PR #69 fixed a confirmed source-loss bug. The app previously treated Basic Myanmar digits U+1040–1049 and punctuation U+104A–104B as romanizable script, then passed those code points to Mya2Rom; sentence stops and numerals could disappear. The shared segment predicate now preserves those as non-romanized text, and \`romanizeTextPreservingNonMyanmar\` passes only contiguous Myanmar text runs to Mya2Rom while preserving Latin text, numerals, whitespace, and punctuation around them.
- The new browser regressions cover the supplied four-sentence greeting, the four U+104B sentence stops, and a mixed-script sample containing Latin \`ABC\`, Myanmar digits \`၁၂၃\`, comma U+104A, and full stop U+104B in both output modes.
- Exact-head workflow [41241791556](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41241791556) passed: Python tests, Vite production build, generated-data drift check, Node tests, Playwright Chromium setup, and **52/52 built-artifact browser tests**. The earlier test assumption that MLCTS periods must equal sentence punctuation was rejected: some vendor MLCTS forms themselves contain periods; the correct assertions distinguish those from the preserved Myanmar punctuation.
- This is a bounded Basic Myanmar punctuation/numeral and mixed-text fix, not a full Myanmar Unicode inventory guarantee. Mya2Rom's 94-row table remains vendor-derived; the original MLC primary publication remains BLOCKED/EVIDENCE_LIMITED; MLCTS → Ukrainian syllable adaptation remains TODO; independent lexical IPA gold remains 0.
- PR #53 remains open and untouched because its branch is diverged and replaces the stylesheet wholesale. At the time of this checkpoint, no post-PR #69 deployment run was yet accessible. A later check verified the Pages deployment at [41242001050](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41242001050), including deployed HTML, script, CSS and vendor-asset smoke checks; see the cross-mode integrity checkpoint below.


## Cross-mode Myanmar source-integrity completion — 2026-10-31

- PR #72 merged by squash as `257db544ccb09bb9b51e5cfdf882b12f5b08b7a2`. It closes a second, narrower source-loss case left by the earlier PR #64 fix: an unsupported Myanmar code point adjacent to a valid syllable could be absorbed into the same phonetic segment, leaving only the valid prefix in Ukrainian output. The segmenter now isolates unsupported code points; `ကာꩠ` renders as `ка⟦ꩠ⟧`.
- The MLCTS browser route now derives a conservative supported-character/base inventory from canonical consonant, independent-vowel, vowel-sign, medial, asat and virama registries plus the vendor's explicit tone/special symbols. Basic Myanmar digits U+1040–1049 and punctuation U+104A–104B remain passthrough material, not syllabic text. Unsupported Myanmar code points and orphan signs are rendered as visible `⟦source⟧` markers rather than silently dropped or guessed.
- Exact PR-head workflows [41243831142](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41243831142) and [41243825927](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41243825927) passed. The job ran pytest (**64 passed + 29 subtests**), generated-data reproducibility, Node tests, Vite production build, Chromium setup and Playwright against the built artifact (**53 passed**).
- PR #69's post-merge main Quality workflow [41242001075](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41242001075) and Pages deployment [41242001050](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41242001050) both succeeded; the deployment includes the HTML, script, CSS and vendor-asset smoke checks. This corrects the earlier checkpoint's statement that no post-PR #69 deployment was accessible.
- PR #72 post-merge main verification [41244193538](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41244193538) passed: pytest 64 + 29 subtests, Node tests, production Vite build, generated-data reproducibility and Playwright 53/53. Pages deployment [41244193576](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41244193576) completed successfully; the deploy job's `Smoke-test deployed site and runtime assets` step passed. Main commit `257db544ccb09bb9b51e5cfdf882b12f5b08b7a2` is published at https://clippyfirst.github.io/Burmese-Ukrainian-Phonetic-System-/.
- Ledger: `MYA-OUTPUT-PRESERVATION-001` remains DONE_VERIFIED and now covers adjacent unsupported units in both phonetic and MLCTS modes; `MYA-ROM-OUTPUT-INTEGRITY-001` DONE_VERIFIED for the bounded supported inventory, digits/punctuation, mixed text and visible unsupported markers. Full Unicode/MLCTS coverage is not claimed. `MYA-ROM-UA-001` remains TODO; the 94-row vendor-derived rime inventory remains PARTIAL/EVIDENCE_LIMITED; original MLC primary source remains BLOCKED; independent lexical IPA gold remains 0.
- Open layout PR #53 remains untouched because its branch is diverged and its wholesale stylesheet replacement risks current IPA typography and method-switch styles. No CSS change was needed for these engine fixes.


## Python parser source-preservation parity checkpoint — 2026-10-31

- PR [#74](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/74) merged by squash as `6ec5c6a15af45fce5d993933c3c429d8e9a82c79`.
- Added Python parser regressions in `tests/test_parser.py`: (1) an unsupported Myanmar Extended-A code point adjacent to a valid syllable remains in the exact raw source cluster and yields `partially_unparsed`; (2) a mixed sentence containing Burmese text, Latin text, ASCII digits, Burmese digits and Myanmar punctuation reconstructs exactly from the parser's source units. Both tests assert normalized source equality and exact concatenation of graphemes/source spans.
- Exact PR-head workflow [41244535813](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41244535813) passed all configured steps: pytest, Vite build, generated-web-data drift check, Node tests, Playwright Chromium setup and built-artifact browser tests. This verifies the test-only change on the exact PR head; no linguistic mapping or IPA gold was added.
- Post-merge main runs [41245969998](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41245969998) (tests) and [41245969938](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41245969938) (Pages) were queued when this checkpoint was prepared. Do not mark post-merge main CI or deployment complete until those exact runs finish successfully.
- Ledger: `MYA-PY-SOURCE-PRESERVATION-001` DONE_VERIFIED for exact source reconstruction and malformed-adjacent-codepoint withholding on the Python parser. Cross-runtime token boundaries are intentionally not claimed identical: Python retains the whole affected raw cluster as partial, while the browser can split a supported prefix and visible unsupported marker. Phonetic accuracy remains BLOCKED/EVIDENCE_LIMITED; independent lexical IPA gold remains 0.


## Post-merge verification correction — 2026-10-31

- The previously queued post-merge runs for PR #74 have now completed successfully on exact main SHA `6ec5c6a15af45fce5d993933c3c429d8e9a82c79`: tests [41245969998](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41245969998) and Pages [41245969938](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41245969938). The test job passed pytest, Vite build, generated-data drift, Node tests and built-artifact Playwright; Pages build/deploy and deployed-site/runtime smoke test passed.
- Documentation PR #75 merged by squash as `48bb45cf2a5c6cc95057fecacdfbc6e852b760b1`. Its exact-head tests workflow [41246079334](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41246079334) passed all configured steps.
- The new exact-main workflows for PR #75's merge commit `48bb45cf2a5c6cc95057fecacdfbc6e852b760b1` are [41246294703](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41246294703) (tests) and [41246294821](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41246294821) (Pages). They were still in progress when this note was authored; inspect their final conclusions before claiming final-main verification or deployment for this documentation head.
- No linguistic implementation changed in PR #74 or #75. MYA-PY-SOURCE-PRESERVATION-001 remains DONE_VERIFIED for bounded source reconstruction; independent lexical IPA gold remains 0 and MLCTS → Ukrainian remains TODO.


## Final main verification for documentation PR #75 — 2026-10-31

- The exact-main test run [41246294703](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41246294703) and Pages deployment [41246294821](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41246294821) have now both completed successfully on main SHA `48bb45cf2a5c6cc95057fecacdfbc6e852b760b1`. Pages build, deploy and deployed-site/runtime smoke test passed.
- Therefore the post-PR #75 main checkpoint is DONE_VERIFIED. The only remaining CI status for this documentation sequence is the exact PR-head workflow for this follow-up documentation PR; its result must be inspected before merge.
