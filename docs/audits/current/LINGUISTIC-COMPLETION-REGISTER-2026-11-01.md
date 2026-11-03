# Burmese linguistic completion register — 2026-11-01

**Baseline:** `main` `aab45f9165d7f9cd7423425ff28186e1c29af0bf`.
**Latest exact-main engineering evidence:** tests [41424921603](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41424921603) and Pages/deployed smoke [41424921607](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41424921607) succeeded.
**Scope:** continue the existing master handoff; this register does not replace it.

## Evidence-based task ledger

| ID | Status | Work remaining | Acceptance |
|---|---|---|---|
| MYA-GOLD-001 | BLOCKED | No independent expert-adjudicated lexical IPA gold exists; `data/benchmark/gold.tsv` contains only its header. | At least two independent qualified Burmese phonetic annotators, adjudication, dialect/speaker metadata, audio/source locators and frozen held-out split. |
| MYA-PHON-001 | PARTIAL | Full vowel-combination derivation, coda/checked-syllable realization, tone/register/phonation inference and contextual allophony remain incomplete. | Source-located, expert-reviewed rule matrix with minimal pairs, explicit dialect scope and fail-closed unresolved cases. |
| MYA-IPA-001 | PARTIAL | Phonological vs phonetic IPA conventions and analysis of tone/register/phonation require specialist adjudication. | Versioned IPA convention, syllable/segment alignment, tone/phonation fields and adjudicated alternatives. |
| MYA-ROM-001 | PARTIAL | MLCTS inventory/crosswalk and MLCTS → Ukrainian adapter remain incomplete; 94 rime keys derive from Mya2Rom rather than a fully verified primary MLC publication. | Primary MLC/official source evidence for rules, complete orthographic matrix, source-aware adapter and explicit ambiguity handling. |
| MYA-G2P-001 | DONE_VERIFIED (diagnostic harness only) | Goruut has 55/100 partial-coverage outputs; myG2P is CC BY-NC-SA 4.0 and temporary test-only. | No production promotion or source-data import without independent gold and explicit rights clearance. |
| MYA-UI-001 | PARTIAL | Existing Playwright Chromium suite exercises the built app and result panels (54 tests pass on the exact review head). Manual visual, keyboard, assistive-technology, mobile and external public-URL interaction QA remain open. | Run browser interaction tests against the deployed Pages URL; record human keyboard, screen-reader and mobile results. |
| MYA-REL-001 | PARTIAL | Production readiness blocked by gold, phonological coverage and external asset licensing. | All release gates met; owner makes any project-license decision; no restricted data/model bundled. |

## Current diagnostic evidence

The latest recorded myG2P v2.0/Goruut 100-row comparison is 98 outputs, 2 none; 43 complete, 55 partial, 2 unknown/no output; 98 stable; 69 unphonemized source fragments; strict source-label matches 0/100 and limited-notation matches 17/100. Epitran 1.35.3 had 0 exact source-label matches. These are diagnostic results, not accuracy. myG2P labels are not independent gold and the source is CC BY-NC-SA 4.0; temporary testing only is authorized. Independent gold remains 0; accuracy remains null.

## Open PR and branch reconciliation

PR [#53](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/53) was closed without merge on 2026-11-02 (the former layout branch is not open). The responsive UI work was subsequently ported onto current main by merged PR [#87](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/87), and the cache-busted CSS Pages smoke test was fixed by merged PR [#88](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/88). These are the current-main replacements; do not revive the stale whole-stylesheet branch. As of this register update, the only open PR is the present quality-review PR [#89](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/89). No existing branch was deleted or rewritten.

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
| IPA-GOLD-RELEASE-GATE-001 | PARTIAL | Numeric tag/manual gate checks 100/25/25 adjudicated train/dev/test, rights and frozen splits; it does not calculate language-specific contrast coverage. Owner must require the check in release rulesets/procedure and obtain separate expert sign-off on a versioned feature-coverage matrix. |

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
| ENGINEERING-METHOD-REFRESH-001 | DONE_VERIFIED | Updated `AGENTS.md` and canonical handoff to pin Superpowers 7.0.1, mattpocock/skills current main, and Ponytail 5.3.3. Exact-head CI on methodology commit `8bdcf3e07ed1359d443aad21b53d00b6db3812f2`: [PR tests 41356409847](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41356409847) and [push tests 41356404196](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41356404196) SUCCESS; 131 tests + 48 subtests and 54 Playwright tests; [Goruut 41356409749](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41356409749) and [Epitran 41356409786](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41356409786) SUCCESS. No runtime dependencies or copied skill bundles were added. |



## Methodology source refresh follow-up — 2026-11-02

| ENGINEERING-METHOD-REFRESH-002 | DONE_VERIFIED | Updated `AGENTS.md` and canonical handoff to mattpocock/skills v1.3.2 (`d1478fcb140db0b93c0c8df17bcfd311844749d0`); added two-axis review, genuine-RED evidence, template/ownership, and safe worktree-cleanup guidance. Verified documentation checkpoint `b5c50772c3d8f1494bb68d0a85a41b6fee82d1ec`: [tests 41358676730](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41358676730) SUCCESS; optional [41358676910](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41358676910) and [41358676749](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41358676749) SUCCESS. | No third-party code, data, skill bundle, or runtime dependency copied. |

## IPA gold adjudication required-field parity — 2026-11-02

| ID | Priority | Status | Scope / evidence | Acceptance criteria / dependencies |
|---|---|---|---|---|
| IPA-GOLD-ADJUDICATION-FINAL-IPA-001 | P1 | DONE_VERIFIED | A test-first regression demonstrated that an `UNRESOLVED` adjudication with the `final_ipa` property omitted was accepted by the Python runtime even though the JSON Schema requires the property (nullable). Test-only RED commit `2c1897567b1c108a7c587307a01cc79c857f4450`; failing exact-head PR CI [41407021855](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41407021855). Runtime fix commit `030d5255eb81400781f6961b53bc5f0d76a85f8c`; exact-head PR CI [41407123331](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41407123331) SUCCESS. 132 pytest tests + 48 subtests; npm build, generated-data drift, npm tests and 54 built-browser Playwright tests passed. |

The validator now requires the `final_ipa` key to be present for every adjudication. `UNRESOLVED` must supply explicit JSON `null`; `AGREEMENT` and `RESOLVED` still require a typed IPA object. No phonology rules, corpus labels, source data or benchmark scores changed. Optional diagnostic runs: [41407123332](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41407123332), [41407123343](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41407123343). Gold remains 0 and empirical accuracy remains null.


### Unresolved adjudication explicit-null positive-path coverage — 2026-11-02

The regression suite now also proves the valid complementary case: `decision=UNRESOLVED` with an explicitly present `final_ipa: null` is accepted and remains excluded from adjudicated gold. Test commit `72d4664d0d1d21872fde11c492d3fd8194b0290f`; exact-head PR CI [41407404042](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41407404042) SUCCESS. 133 pytest tests + 48 subtests; npm build, generated-data drift check, npm tests and 54 built-browser Playwright tests passed. Optional diagnostics: [41407410734](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41407410734), [41407410747](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41407410747) SUCCESS. This does not create IPA labels or change the gold count (still 0) or accuracy (still null).

## External G2P engine coverage audit — 2026-11-02

- **PARTIAL (DONE_VERIFIED diagnostic execution):** Epitran 1.35.3 returned six structural-only probe outputs, with no verified gold. Goruut source snapshot `b224bde` on 100 source-attested myG2P rows produced 0/100 exact and 17/100 limited-normalized matches, 2 failures, 43 complete / 55 partial / 2 unknown coverage, and 69 unphonemized fragments. See `docs/research/external-g2p-benchmark-and-engine-coverage-2026-11-02.md` and Actions runs 41409098332 / 41409098207.
- **NOT SCORED:** independent expert-adjudicated IPA gold remains 0; neither the structural Epitran smoke test nor limited-normalized Goruut concordance establishes accuracy.
- **TODO:** investigate Burmese phonation/tone/register and vowel/coda mismatches; recover language-specific CRF/WFST/FST baselines from myG2P and LREC 2020; fix the absent upstream Goruut `weights9.bin.zlib` asset.


## Goruut language-bundle asset status correction — 2026-11-02

The previous TODO wording suggesting that this repository can simply recover or fix `weights9.bin.zlib` is superseded. Inspection of the exact upstream Goruut source tree at `b224bde02151f8f86d0fe260804e4ca743bda620` shows no `weights9.bin.zlib` in `dicts/lao/`, `dicts/khmer/central/`, or `dicts/burmese/`; the earlier `weights7` and `weights8` assets are present. This is an upstream language-bundle omission in the pinned snapshot, not a missing project-owned file. Status: **BLOCKED (upstream dependency)**. Acceptance: upstream publishes the asset or documents the expected model-tier fallback, and a controlled same-input comparison plus independent expert IPA gold establishes whether the asset changes relevant language coverage. Do not synthesize weights, download unpinned substitutes, or treat the warning as a failed workflow. See the external-engine research audit and canonical handoff for the evidence.


## Additional Burmese CRF baseline inventory — 2026-11-02

| ID | Priority | Status | Evidence / acceptance |
|---|---|---|---|
| BUR-CRF-G2P-001 | P1 | PARTIAL (DONE_VERIFIED raw-output probe) | Added `scripts/benchmark_burmese_crf.py`, six focused unit tests, and a `crf-baseline` job in `.github/workflows/optional-epitran-benchmark.yml`. Pinned model/data/CRFsuite commits: `de0f06056cf334b8cdd5a1efd1226f01c8162b77`, `54b5c76bb5a87fdbaaeddc1892e6ebd8f97ee225`, `a2a1547727985e3aff6a35cffe073f57f0223e9d`. The original pytest import failure in run [41415624611](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41415624611) was fixed by `pythonpath = ["."]`; full tests/build/generated-data/JS/Playwright workflow [41417982342](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41417982342) passed. Optional CRF + Epitran [41417982199](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41417982199) and Goruut [41417982213](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41417982213) passed. Inspected artifact `burmese-crf-raw-output` (SHA-256 `0119281f9bd3d946a36dad1299f530b629599cfd26146ce190ea34f7c707ddd6`): 100/100 predictions, 84/100 source-concordant diagnostic, `gold_count=0`, `accuracy=null`, status `NOT_SCORED_POSSIBLE_TRAINING_OVERLAP`; model SHA-256 `f66571b7632eed2e94878278702654ce0a4b25fcab18720af60d3cfe00b011ce`. Probe uses supplied syllable segmentation and source-attested labels; no accuracy is inferred. Further acceptance requires verified train/test disjointness, held-out lexical groups, profile/IPA-convention review and independent expert adjudication. Upstream myG2P source declares CC BY-NC-SA 4.0; artifact is diagnostic only and not redistributed as product data. |


## Main publication reconciliation — 2026-11-02

Supersedes earlier handoff statements that the review branch was still ahead of `main` and unmerged: the CRF benchmark test-import defect was fixed in PR [#86](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/86), merged into the review branch as `db183681eb1fc66e1b513623e08e75d5f8842220`, then the complete language PR [#84](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/84) was merged into `main` as `8cffc508ffaf5ab1b54f3b9276034838d24057ae`; this was the repository's current `main` tip at reconciliation. On the complete feature plus fix, the required workflow passed: tests/build/generated-data check/JS tests/Playwright built-browser tests [41417982342](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41417982342) SUCCESS; the optional CRF and Epitran jobs [41417982199](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41417982199) SUCCESS; optional Goruut [41417982213](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41417982213) SUCCESS. The original required test failure [41415624611](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41415624611) was specifically `ModuleNotFoundError: No module named 'scripts'`; the pytest `pythonpath = ["."]` fix was verified by the successful full run. The Pages workflow is configured to deploy from `main` and includes a deployed-site/runtime-asset smoke test. The public deployment result could not be independently inspected from this session, so deployment status remains **BLOCKED (external verification/network access)**, not claimed successful. Independent expert-adjudicated gold remains 0 and accuracy remains null; the project is still a research prototype.


## Current-main UI publication — 2026-11-02

The older design PR [#53](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/53) was not merged because its branch had diverged (5 commits ahead / 187 behind current `main`). Its responsive CSS and cache-busting intent were ported onto a fresh branch from the then-current `main`; PR [#87](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/87) was merged as `930ec6b66b4ec5fb280d3c926b8d307a23551998`. The current-main CI [41424015018](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41424015018) passed IPA gold-corpus structure validation, Python tests, generated-web-data drift check, npm tests, production build and Playwright browser tests. The Pages workflow is configured for pushes to `main`; actual deployment completion and public-site smoke-test result remain **BLOCKED (external verification/network/DNS unavailable in this session)**. This UI change improves presentation only and does not improve linguistic accuracy. Independent adjudicated gold remains 0; accuracy remains null; research-prototype status is unchanged.

### Pages smoke-test compatibility follow-up — 2026-11-02

The cache-busted stylesheet URL introduced by the UI polish exposed an overly strict CSS-link extractor in the deployed-site smoke test. Fixed in PR [#88](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/88), merge `fea5f6e44680b6202e07e5e896eb175699c101c2`; the extractor now accepts an optional query string. PR CI passed (41424690731). The Pages workflow is now compatible with the deployed CSS URL. The post-merge Pages deployment and live-site smoke-test result are still **BLOCKED for independent verification** because external DNS/network access and a workflow-run listing endpoint were unavailable; do not infer deployment success from a merged PR or a successful pull-request CI run.


## Quality/profile review update — 2026-11-02

- Current main: `aab45f9165d7f9cd7423425ff28186e1c29af0bf`; exact-main tests [41424921603](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41424921603) and Pages/deployed smoke [41424921607](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41424921607) SUCCESS.
- Overall status: research prototype. Structural/engineering contracts are materially stronger, but phonological realization, tone/register/phonation, MLCTS-to-Ukrainian completeness and independent gold remain incomplete.
- Gold: 0 independent expert-adjudicated lexical IPA records; accuracy=null. Keep MYA-GOLD-001 BLOCKED, MYA-PHON-001 and MYA-IPA-001 PARTIAL, MYA-ROM-001 PARTIAL, MYA-UI-001 PARTIAL.
- No phonological labels or mappings were added in this review. The external G2P runs remain diagnostics and licensing-limited, not gold or production approval.



## Pilot profile decision — 2026-11-02

| ID | Status | Decision / evidence | Remaining acceptance |
|---|---|---|---|
| MYA-PROFILE-001 | DONE_VERIFIED (pilot-scope decision only) | Contemporary Standard Burmese, Yangon reference variety, careful citation forms; project-local ID `my-yangon-careful-citation-v1`. Oxford-hosted overview identifies Standard Burmese with Lower Burma/Yangon; grammar literature documents regional and speaker-sensitive variation. Issue #85 and canonical handoff updated. | Approve IPA convention for tone/register/phonation, vowels, codas, medials and minor syllables; recruit two annotators + independent adjudicator; curate rights-cleared 30-item sample; blind dry-run and adjudicate. No claim of runtime completeness or linguistic accuracy. |


## Engineering-method integration — 2026-11-02

| ID | Status | Evidence | Remaining acceptance |
|---|---|---|---|
| ENG-METHODS-001 | DONE_VERIFIED (repository-context integration) | Added GLOSSARY.md, docs/agents/issue-tracker.md and docs/agents/codebase-map.md; linked them from AGENTS.md; refreshed exact upstream method pins. Exact-head CI before handoff closeout: [41468949170](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41468949170) SUCCESS. | Re-check these maps whenever entry points, data ownership or test commands change. This task does not establish linguistic accuracy or independent gold. |

The three references are used as methods, not runtime dependencies: Superpowers for explicit scoped execution and verification; Matt Pocock Skills for domain vocabulary, clear interfaces, source-backed research and two-axis review; Ponytail for real-flow mapping, minimal complete changes and residual-risk reporting. No production code or linguistic labels were changed by this task.


## Benchmark and corpus review — 2026-11-02

| ID | Status | Evidence | Remaining acceptance |
|---|---|---|---|
| BENCH-REVIEW-001 | PARTIAL (existing diagnostic evidence reviewed) | Reviewed fixtures, corpus files, gold lifecycle files, benchmark harnesses and external raw-output reports. Exact-head engineering CI: https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41469225580 SUCCESS. | Independent expert gold remains 0; resolve profile/convention, rights, held-out split and double-annotation/adjudication blockers before accuracy scoring. |

Comparator concordance is not accuracy. See the dated benchmark review in the canonical master handoff for language-specific results and acceptance criteria.


| BENCH-MYG2P-001 | PARTIAL | Direct upstream README confirms IPA-output ver2, known sentence-level failures for particles/postpositions, and CC BY-NC-SA 4.0; WSSANLP 2016 primary paper compares CRF/PBSMT/WFST and manually inspects tone, voicing, consonant and vowel errors. | Recover exact model/training membership and a disjoint lexical-group held-out split; test sentence particles/postpositions separately; approve Yangon tone/register/phonation IPA convention; obtain independent adjudication. Existing 84/100 concordance remains unscored and cannot be called accuracy; commercial reuse remains blocked absent permission. |


## Upstream methodology pin reconciliation — 2026-11-02

| ID | Status | Evidence | Acceptance / limitation |
|---|---|---|---|
| ENG-METHOD-PIN-002 | DONE_VERIFIED (documentation provenance correction) | Corrected `AGENTS.md` and the canonical handoff to distinguish `mattpocock/skills` release v1.3.2 (`d1478fcb140db0b93c0c8df17bcfd311844749d0`) from the latest inspected `main` snapshot (`4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`, 2026-10-31). The newer main commit adds the `software-factory` glossary/design skill; no unrelated factory workflow was imported. | Methodology metadata only. No runtime, linguistic rules, corpus, license grants or accuracy metrics changed. Recheck upstream pins when methodology sources are intentionally refreshed. |


## Late-session verification checkpoint — 2026-11-02

| Evidence | Result |
|---|---|
| Review PR | [#89](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/89) on `research/burmese-quality-review-20261102` |
| Base / exact head | `aab45f9165d7f9cd7423425ff28186e1c29af0bf` / `8ee56594856b91bda6063c94413440d4c51ba4d0` |
| Branch divergence | 21 ahead, 0 behind |
| Exact-head hosted workflow | [41476262272](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41476262272) — SUCCESS (`tests`) |
| GitHub review state | No submitted reviews or unresolved review threads returned |
| Local clean checkout | BLOCKED: `git clone` could not resolve `github.com`; no local test execution claimed |

This is an engineering-state recheck only. Independent expert-adjudicated IPA gold remains 0; empirical pronunciation accuracy remains null. Existing linguistic, source-rights, held-out-split, human-adjudication and manual accessibility acceptance criteria remain unchanged. No linguistic labels or runtime rules were altered by this checkpoint.


## Public website verification — 2026-11-02

Burmese: DONE_VERIFIED — current-main Pages build/deploy smoke and Playwright Chromium result-path tests passed (run 41424921607); exact review-head CI is running as 41531149722 at this checkpoint. PARTIAL — Playwright covers built-app interaction and output panels, but post-deploy public-URL browser interaction and manual assistive/mobile QA remain unverified. BLOCKED — direct live-site access from this runner failed at DNS resolution; this is not evidence of a site outage. TODO — add a post-deploy browser interaction smoke and complete manual keyboard/screen-reader/mobile QA. See master handoff for evidence and acceptance criteria.


## Browser interaction verification — 2026-11-03

| ID | Status | Evidence | Remaining acceptance |
|---|---|---|---|
| MYA-UI-001 | PARTIAL | Exact review-head CI [41531295647](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41531295647) SUCCESS; the existing Playwright Chromium suite passed 54 tests against the built site, including result rendering and fail-closed input cases. | Verify the public Pages URL after deployment and complete manual keyboard, screen-reader and mobile QA. This is UI engineering evidence, not phonetic accuracy. |


## New source-level evidence — Burmese tone, lexicon and speech resources (2026-11-03)

| ID | Status | New evidence | Acceptance / limitation |
|---|---|---|---|
| MYA-PHONETIC-PROFILE-SOURCE-001 | PARTIAL | Watkins (2001), DOI [10.1017/S0025100301002122](https://doi.org/10.1017/S0025100301002122), describes one Yangon male reading slowly/deliberately; broad transcription combines pitch, phonation and length in tone diacritics. Gruber (2011), DOI [10.3765/EXABS.V0I0.557](https://doi.org/10.3765/EXABS.V0I0.557), supports joint perceptual contribution of duration, pitch and phonation. | Freeze an explicit project annotation convention; retain separate tone category, phonation, duration and pitch fields where evidenced. Do not treat the JIPA broad notation as exhaustive narrow IPA gold. |
| MYA-G2P-2016-EVIDENCE-001 | PARTIAL | Thu et al. (2016), [ACL Anthology W16-3702](https://aclanthology.org/W16-3702): 25,300 MLC dictionary entries; 25,000 train and three 100-word open test sets; own phoneme inventory/PER; no documented independent adjudication or project-compatible IPA standard. | Historical baseline only. MLC dictionary data rights are not established by the article; no redistribution/import until rights are verified. |
| MYA-SLR80-CORPUS-001 | PARTIAL | Oo et al. (2020), [ACL Anthology 2020.lrec-1.777](https://aclanthology.org/2020.lrec-1.777): 2,528 utterances, 20 female Yangon speakers, 22,443 word tokens, 9,941 unique words; speech corpus CC BY-SA 4.0; separate Thrax/WFST pronunciation grammar. | Corpus transcriptions are word-level orthography, not IPA; no public train/dev/test split or dialect-stratified metadata established. Review grammar licensing separately; not IPA gold. |
| MYA-GOLD-PILOT-001 | BLOCKED | No annotations or adjudications created by this audit. | Require frozen IPA/profile conventions, source-rights checks, two independent qualified annotators, separate adjudicator, blind intake and explicit uncertainty. Gold remains 0; accuracy null. |

No dataset was imported and no model was promoted. Concordance/PER from published studies is not repository accuracy.


## Follow-up source corrections and annotation acceptance — 2026-11-03

| ID | Status | Evidence update | Acceptance / limitation |
|---|---|---|---|
| MYA-ORTHO-SYLLABIFICATION-001 | PARTIAL (external evidence reviewed; not implemented as ClippyFirst G2P) | Hlaing & Mikami (2013; published online 2014), DOI [10.4038/ICTER.V6I2.7150](https://doi.org/10.4038/ICTER.V6I2.7150), full-text review: rule-based FST; 11,732 orthographic words; 99.93% word-syllabification; the consonant-stacking subset is 245/253 correct (96.83%); the text also discusses a free-standing-vowel error. Count discrepancy 32,238 vs 32,283 syllables. | This metric is strictly orthographic segmentation, not G2P, phoneme or IPA accuracy. Do not use as a pronunciation benchmark score. |
| MYA-TONE-VOWEL-ANALYSIS-001 | PARTIAL | Mooney & Repetti-Ludlow (2021), DOI [10.3765/plsa.v6i1.4900](https://doi.org/10.3765/plsa.v6i1.4900): two acoustic experiments with one female native Yangon consultant in her late 20s; duration/voice-quality measures distinguish four categories in isolation, F0 distinguishes selected pairs; in sentential frames duration largely neutralizes and pitch remains robust. Vowel alternations are argued to be coda/sonority-conditioned. Four surface categories are retained; killed H→HL and creaky HL are proposed underlying analyses, explicitly left for further work. | Preserve as a narrow-sample competing analysis. Do not encode as a universal rule or replace the four-category surface model without independent expert evidence. |
| MYA-GOLD-AGREEMENT-001 | TODO | Annotation-method evidence: Cucchiarini (1996), DOI [10.3109/02699209608985167](https://doi.org/10.3109/02699209608985167); Oller & Ramsdell (2006), DOI [10.1044/1092-4388(2006/100)]. | Pilot must report exact normalized agreement plus alignment-aware feature-weighted agreement, separate tone/duration/phonation/vowel/coda/boundary metrics, unresolved alternatives and adjudication rate. Raw percent agreement is supplementary only. |

No labels, lexemes or corpus data added. Independent expert gold remains 0; accuracy null.

## Bibliographic correction — 2026-11-03

- Hlaing & Mikami's article is assigned to *The International Journal on Advances in ICT for Emerging Regions*, Vol. 6 No. 2 (2013); the journal page gives an online publication date of 2014-01-03. The source-level note now cites it as 2013 (published online 2014), avoiding a false year conflict. The reported 99.93% remains orthographic syllabification, not G2P/IPA.
- Duan & Zhu (2025) is now fully identified as “Double registers and eight tones in Burmese: From the perspective of The Syllabic Phonology and tono-typology”, *Language and Linguistics* 26(3), 387–430, DOI 10.1075/lali.00203.dua. It remains a competing analysis, not settled runtime consensus.


## Citation metadata reconciliation — 2026-11-03

| ID | Status | Work remaining | Acceptance |
|---|---|---|---|
| MYA-CITE-001 | PARTIAL | Oo et al. (2020) and Ye Kyaw Thu et al. (2016) records were corrected/expanded; repository-wide citation completeness and claim-level evidence audit remain open. | Every in-text citation maps to complete source metadata; claims distinguish corpus/G2P evidence from independent IPA gold and retain exact source scope. |

The Oo et al. (2020) paper documents corpus and FST G2P resources, not independent project IPA gold. Current code verification remains runs [41605477450](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41605477450) and [41605470641](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41605470641) on `b0f83165b4f6a9271f3f6d7ad1598b944ac03a07`; later documentation commits did not change code. Independent gold remains 0; accuracy null.

## Parallel open-PR reconciliation — 2026-11-03

- [PR #90](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/90) independently fixes manifest-wide IPA-gold split identity: every row across all lexeme groups must share one frozen `(seed, version)`; extending a manifest inherits it; conflicting overrides and empty explicit values fail. Exact-head tests [41615796407](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41615796407) passed. It changes `scripts/ipa_gold_corpus.py` and its tests, not the current #89 research work; do not duplicate the implementation.
- [PR #91](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/91) adds the missing WSSANLP 2016 source-registry record and author–year G2P benchmark citations. Exact-head tests [41615159273](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41615159273) passed. Optional Epitran/CRF raw-output workflow [41615159106](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41615159106) also passed operationally, but its artifact reports 100 predictions, 84 source-concordant rows, gold_count 0, `accuracy: null`, and `NOT_SCORED_POSSIBLE_TRAINING_OVERLAP`; it is not an accuracy result.
- Both #90 and #91 are open, mergeable, based on current main with zero behind commits. The current #89 branch corrects the playbook citation but does not contain the W16 source-registry row or benchmark audit document; keep the changes complementary and avoid duplicate source records. No PR was merged in this pass.