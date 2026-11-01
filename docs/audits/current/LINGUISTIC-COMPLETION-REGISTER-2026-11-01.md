# Burmese linguistic completion register — 2026-11-01

**Baseline:** `main` `4ddb9d3f10427275ce75c7ae73270468d3721106`.
**Latest exact-main engineering evidence:** tests [41326473323](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41326473323) and Pages/deployed smoke [41326473352](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41326473352) succeeded.
**Scope:** continue the existing master handoff; this register does not replace it.

## Evidence-based task ledger

| ID | Status | Work remaining | Acceptance |
|---|---|---|---|
| MYA-GOLD-001 | BLOCKED | No independent expert-adjudicated lexical IPA gold exists; `data/benchmark/gold.tsv` contains only its header. | At least two independent qualified Burmese phonetic annotators, adjudication, dialect/speaker metadata, audio/source locators and frozen held-out split. |
| MYA-PHON-001 | PARTIAL | Full vowel-combination derivation, coda/checked-syllable realization, tone/register/phonation inference and contextual allophony remain incomplete. | Source-located, expert-reviewed rule matrix with minimal pairs, explicit dialect scope and fail-closed unresolved cases. |
| MYA-IPA-001 | PARTIAL | Phonological vs phonetic IPA conventions and analysis of tone/register/phonation require specialist adjudication. | Versioned IPA convention, syllable/segment alignment, tone/phonation fields and adjudicated alternatives. |
| MYA-ROM-001 | PARTIAL | MLCTS inventory/crosswalk and MLCTS → Ukrainian adapter remain incomplete; 94 rime keys derive from Mya2Rom rather than a fully verified primary MLC publication. | Primary MLC/official source evidence for rules, complete orthographic matrix, source-aware adapter and explicit ambiguity handling. |
| MYA-G2P-001 | DONE_VERIFIED (diagnostic harness only) | Goruut has 55/100 partial-coverage outputs; myG2P is CC BY-NC-SA 4.0 and temporary test-only. | No production promotion or source-data import without independent gold and explicit rights clearance. |
| MYA-UI-001 | TODO | Manual visual, keyboard, assistive-technology and mobile QA is not established by CI. | Recorded test matrix and deployed-site results. |
| MYA-REL-001 | PARTIAL | Production readiness blocked by gold, phonological coverage and external asset licensing. | All release gates met; owner makes any project-license decision; no restricted data/model bundled. |

## Current diagnostic evidence

The latest recorded myG2P v2.0/Goruut 100-row comparison is 98 outputs, 2 none; 43 complete, 55 partial, 2 unknown/no output; 98 stable; 69 unphonemized source fragments; strict source-label matches 0/100 and limited-notation matches 17/100. Epitran 1.35.3 had 0 exact source-label matches. These are diagnostic results, not accuracy. myG2P labels are not independent gold and the source is CC BY-NC-SA 4.0; temporary testing only is authorized. Independent gold remains 0; accuracy remains null.

## Open PR and branch reconciliation

PR [#53](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/53) remains open and untouched. Its branch is 5 commits ahead and 38 behind current main, changes only `index.html`, `system.html` and `src/web/styles.css`, and replaces the stylesheet wholesale. It is not safe to merge as-is; re-evaluate only if a fresh visual audit identifies a still-missing requirement, then port focused CSS changes on current main with browser tests. No existing user branch was deleted or rewritten.

## Execution order

1. Preserve fail-closed phonetic behavior.
2. Commission independently double-annotated Burmese IPA from licensed audio, with speaker/dialect and timestamp metadata.
3. Resolve the phonemic/phonetic convention and the interaction of tones, register, phonation and checked syllables with specialists.
4. Complete vowel/medial/coda derivation and the orthography-to-IPA matrix.
5. Verify MLCTS against primary Myanmar Language Commission sources; finish the separate MLCTS → Ukrainian adapter.
6. Conduct deployed UI/accessibility QA and asset-rights review.

## External dependencies / blockers

- Qualified Burmese phonologist/phonetic annotators and adjudicator.
- Licensed audio and permission for derived labels; myG2P cannot be redistributed commercially under its current CC BY-NC-SA terms absent permission.
- Primary MLC publication access for MLCTS rule confirmation.
- No local checkout was available to this execution; exact-main GitHub Actions are the engineering evidence. Run documented local release commands in a clean checkout before release.

## Method constraints

Preserve `Burmese orthography → structural/medial analysis → Burmese phonology → typed IPA → Ukrainian adaptation`. MLCTS remains a separate orthographic mode. Do not collapse register/phonation distinctions into guessed tone values.


## Independent IPA gold corpus implementation — 2026-11-01

| Task | Status | Evidence / remaining acceptance |
|---|---|---|
| IPA-GOLD-SCHEMA-001 | DONE_VERIFIED | Record, annotation, adjudication, split and license schemas plus cross-file validator |
| IPA-GOLD-DOUBLE-ANNOTATION-001 | PARTIAL | Two distinct annotators enforced; blind intake requires external controlled collection |
| IPA-GOLD-ADJUDICATION-001 | PARTIAL | Agreement/resolved/unresolved logic and feature-complete IPA comparison; no real adjudicated rows |
| IPA-GOLD-RIGHTS-001 | DONE_VERIFIED (mechanism) | Allowlisted licenses, required rights evidence and rejection of unregistered/non-redistributable licenses; source-by-source legal review still required |
| IPA-GOLD-SPLIT-001 | DONE_VERIFIED | Deterministic hash-based, frozen lexeme-group split and leakage checks |
| IPA-GOLD-EXPORT-001 | DONE_VERIFIED | Rights-filtered typed IPA export retaining source/license/evidence locators |
| IPA-TYPED-BENCHMARK-001 | DONE_VERIFIED | Different or missing IPA kind cannot count as an exact match |
| IPA-GOLD-RELEASE-GATE-001 | PARTIAL | Tag/manual workflow requires 100/25/25 adjudicated train/dev/test; owner must require the check in release rulesets/procedure |

**Current gold:** zero independent expert-adjudicated records; `gold.tsv` remains header-only; accuracy=null. The new schemas, fixtures and source-attested literature are not gold labels. No phonetic data was invented.


**Research evidence artifact:** [Burmese vowel × medial × checked-syllable × prosody evidence matrix](BURMESE-VOWEL-MEDIAL-PROSODY-EVIDENCE-MATRIX-2026-11-01.md). It separates Green's four-tone analysis, the eight-tone/two-register proposal, consonantal voicelessness and written medial parsing.


**Source reconciliation:** Green (2002 ROA paper; published 2005 chapter) now anchors the 50-rhyme analysis. Repetti-Ludlow (2023) tests a restricted subset of voiceless sonorants and finds variable spread-glottis realization (78% present); Duan & Zhu (2025) proposes an eight-tone/two-register alternative but is not yet independently adjudicated.


**2026-11-01 closeout:** PR [#84](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/84) is the comprehensive implementation and research-matrix change. PR CI passed 121 Python tests + 31 subtests, four generated-data tests and 54 Playwright browser tests; optional Epitran diagnostic passed. Main remains at 4ddb9d3. Gold remains 0; tone/register/phonation adjudication remains blocked.


## 2026-11-01 final IPA-kind consistency verification

- Added fail-closed cross-annotation consistency: both independent annotations for one record must use the same `ipa.kind`, and a `RESOLVED` adjudicated result must preserve that kind. This prevents phonemic-vs-phonetic representation differences from being misclassified as pronunciation disagreements.
- Regression evidence: both new tests failed against the pre-fix validator on the test-only commit, then passed after the validator change.
- New task `IPA-GOLD-REPRESENTATION-KIND-001`: **DONE_VERIFIED** (mechanism and exact-head CI). Blindness, annotator qualifications and independent adjudicator competence remain external operational evidence, not properties CI can prove.
- Final PR head: `5aa4463b70599f36ea287d62ed07d0fd69b3dac1`; CI run [41338466798](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41338466798) SUCCESS — 124 Python tests + 31 subtests; generated-data checks, production build and 54 built-browser Playwright tests passed. Optional Epitran diagnostic run 41338466820 also passed.
- The Burmese matrix remains PARTIAL: Green's extracted 50-rhyme table still needs manual primary-PDF transcription; tone/register/phonation analyses remain competing evidence, not implementation consensus.
- Gold remains zero; `gold.tsv` remains header-only; empirical accuracy remains null. No IPA labels were generated.


## IPA gold split-manifest runtime/schema parity — 2026-11-01

| ID | Priority | Status | Scope / evidence | Acceptance criteria / dependencies |
|---|---|---|---|---|
| BUR-IPA-SPLIT-STRICT-001 | P1 | DONE_VERIFIED | RED test on commit `3f20dcc5f2f90940b600fdb2fd378d4976d3a098` failed as expected; GREEN code commit `76af91582a760b44ce18f029f80dbf9a35f7a4c7`; exact-head CI [41340417848](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41340417848) passed | The split generator and corpus validator share the closed split-field contract; unknown prior-manifest properties are rejected rather than silently dropped. No expert gold is created by this change. |


## Product-corpus license eligibility — 2026-11-01

| ID | Priority | Status | Scope / evidence | Acceptance criteria / dependencies |
|---|---|---|---|---|
| BUR-IPA-LICENSE-ELIGIBILITY-001 | P1 | DONE_VERIFIED | RED tests on `53964d81fdfca19314fbf911dcc424cd3be20027`; GREEN code/schema commit `7383191ca2ca9e8c24099ae2f55483c6f6351d68`; exact-head CI [41341030962](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41341030962) passed | Registry and schema fail closed unless a redistributable product-corpus license explicitly permits commercial use and defines attribution/share-alike obligations. Human source-by-source rights review remains required. |


## Release-gate threshold validation — 2026-11-01

| ID | Priority | Status | Scope / evidence | Acceptance criteria / dependencies |
|---|---|---|---|---|
| BUR-IPA-RELEASE-THRESHOLDS-001 | P1 | DONE_VERIFIED | RED test on `52fbfd77a12ef2e592debbaea7e07b0650d5fd3b`; GREEN code commit `fc77d3e8073e58ae75a86693db971ff3fc0a162a`; exact-head CI [41341757201](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41341757201) passed | All split minimums reject zero and negative values; threshold errors aggregate with other release-gate findings. Default minimums remain 100/25/25. |


## Audio-source review update — 2026-11-01

OpenSLR 80 (SLR80) is now the leading documented Burmese audio candidate: https://openslr.org/80. The primary paper (Oo et al. 2020, https://aclanthology.org/2020.lrec-1.777.pdf, corpus section pp. 6333–6334) reports 2,528 utterances from 20 female native Burmese speakers aged 25–35, recorded in Yangon at 48 kHz mono, with hand-curated word-segmented transcripts and native-speaker audio/transcript QC. The resource is CC BY-SA 4.0. Only female recordings were released at the time of the paper.

This is **not IPA gold**. The line index contains orthographic transcripts; the paper's FST G2P is a pronunciation-generation/lexicon-bootstrapping tool, not independent adjudicated truth. The recording location does not by itself establish every speaker's dialect. No word-level acoustic timestamps are supplied, so any token selection requires manual alignment verification. The female-only sample cannot support gender-balanced generalization.

Use SLR80 for a separately labelled contextual phonetic pilot after specialist profile review. For lexical citation-form G2P gold, arrange controlled elicitation from qualified target-variety speakers. Keep contextual and citation-form corpora/splits separate.

Status remains `MYA-GOLD-001 = BLOCKED`: no annotations, annotators or adjudications have been created. Independent gold remains 0 and accuracy remains null.


## Final exact-head verification — 2026-11-01

Branch `feat/ipa-gold-corpus-20261101-review`, source-audit content commit `083ddb740d825b2c1e227cd0f19d051beba097a6`. Burmese exact-head CI: tests [41344959952](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41344959952) SUCCESS; optional Goruut [41344959963](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41344959963) SUCCESS; optional Epitran [41344959950](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41344959950) SUCCESS. Core job passed corpus structure validation, pytest, npm build, generated-data drift check, npm tests and built-browser Playwright tests.

These checks validate the committed repository and its automated engineering contracts. They do **not** validate the linguistic correctness of future human annotations, create gold labels, or change the release blocker. Gold remains empty and accuracy remains null.


## Follow-up handoff-head CI — 2026-11-01

The subsequent documentation-only handoff/register state at commit `0021dae7ea3450b99f63509c39d3dd384241284e` was also checked on its exact head: tests [41345383752](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41345383752) SUCCESS; optional Goruut [41345383729](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41345383729) SUCCESS; optional Epitran [41345383623](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41345383623) SUCCESS. These runs validate the updated documentation and existing automated checks, not future IPA annotations. Any later branch update must be checked again on its new exact head.


## Open-rights redistributability invariant — 2026-11-01

| Task | Status | Evidence / acceptance |
|---|---|---|
| BUR-IPA-RIGHTS-OPEN-001 | DONE_VERIFIED | A test-first regression rejected a source with `rights_status=OPEN` and `redistributable=false`; the runtime validator and record JSON Schema now both require `redistributable=true` for OPEN. Test-only RED commit: `644d897cefeb613a74aaa6ea9110ba4e9a5303e2`. Fix/schema code head: `0f0a8a013887a7366aea2424935b0252f5b11778`; exact-head CI run [41348005124](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41348005124) passed: 129 pytest tests + 41 subtests; npm build, generated-data drift, npm tests and 54 built-browser Playwright tests passed; optional Goruut and Epitran diagnostics passed. |

This is a consistency/eligibility invariant, not a new legal determination. It does not change source licenses, rights evidence, gold labels or measured accuracy. Independent adjudicated gold remains 0; accuracy remains null.

## Exact current-head engineering checkpoint — 2026-11-01

- Current code checkpoint: `a8b71b536f93da586e16dfcc91a5db9a8be1f573`; exact-head core CI [41348246731](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41348246731) **SUCCESS**. 129 pytest tests + 41 subtests; npm build, generated-data drift check, npm tests and 54 built-browser Playwright tests passed. Optional Goruut Burmese and Epitran diagnostics passed.
- The `OPEN` / `redistributable` consistency regression is present in runtime validation, JSON Schema and tests.
- Independent expert gold remains 0 and accuracy remains null. Human annotation/profile/convention gates remain open; CI is not linguistic validation.

 
## Nested IPA record contract closure — 2026-11-01

| Task | Status | Evidence / acceptance |
|---|---|---|
| IPA-GOLD-NESTED-STRICT-001 | DONE_VERIFIED (engineering contract) | Test-first RED: [run 41352936278](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41352936278); GREEN exact-code-head CI: [run 41353062069](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41353062069). Runtime validator and JSON Schema both reject undeclared fields in `orthography`, `profile`, `source` and `source.rights_evidence`. 131 pytest tests + 48 subtests; npm build, generated-data drift, npm tests and 54 built-browser Playwright tests passed. |

This closes only the nested-object shape contract. It does not establish the truth of source metadata, rights determinations, speaker profiles, IPA, or expert adjudication. Independent gold remains 0 and accuracy remains null.


## Validator duplicate-call cleanup — 2026-11-01

| Task | Status | Evidence / acceptance |
|---|---|---|
| IPA-GOLD-DUPLICATE-VALIDATION-001 | DONE_VERIFIED | Removed four consecutive duplicate `reject_unknown_properties` calls from nested `orthography`, `profile`, `source`, and `source.rights_evidence` validation. Code commit: `76c2639c57dfdf7da5a4a39a3fae999f2a646532`; resulting shared validator blob SHA: `a072297e320b4b91a36c59fc90328b6ff98d2a5f`. - Core PR CI: https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41354250746 (SUCCESS); core push CI: https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41354246209 (SUCCESS); optional language diagnostics: https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41354250460, https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41354250457 (SUCCESS). |

This is dead-code cleanup only: each contract check remains once; no validation rule, schema, IPA value, phonology rule, or corpus row changed. The shared validator remains identical across Lao, Khmer and Burmese. Hosted CI only; no local checkout or local test command is claimed. Independent expert-adjudicated gold remains 0 and empirical accuracy remains null.


## Methodology source refresh — 2026-11-02

| ID | Status | Evidence / acceptance |
|---|---|---|
| ENGINEERING-METHOD-REFRESH-001 | DONE_VERIFIED | Updated `AGENTS.md` and canonical handoff to pin Superpowers 7.0.1, mattpocock/skills current main, and Ponytail 5.3.3. Exact-head CI on methodology commit `+q.head+`: [PR tests 41356409847](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41356409847) and [push tests 41356404196](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41356404196) SUCCESS; 131 tests + 48 subtests and 54 Playwright tests; [Goruut 41356409749](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41356409749) and [Epitran 41356409786](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41356409786) SUCCESS. No runtime dependencies or copied skill bundles were added. |

