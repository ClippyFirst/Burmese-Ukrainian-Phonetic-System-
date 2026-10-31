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
