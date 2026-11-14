## Burmese Wiktionary IPA source review — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-IPA-001 | PARTIAL (discovery lead; rights conflict unresolved) | Dataset card: 22,191 records, 20,759 headwords, 113 IPA values (0.51%), snapshot 2026-08-01, CC BY 4.0 declaration. Myanmar Wiktionary local policy (last edited 2024-12-06): CC BY-SA 3.0 Unported/GFDL. No per-entry dialect/convention, audio, annotator/adjudication or detailed locators in the card. | No import into gold. Clarify rights with publisher/rightsholder; then item-level profile/source/IPA audit and independent specialist review. MLCTS is not IPA. |

## Post-merge provenance checkpoint — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-G2P-PROVENANCE-001 | DONE_VERIFIED (PR-head verified; post-merge push CI not independently surfaced) | PR [#106](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/106) merged as 76426383038ee18a4cf5f2136379b25c08a40d7e. Exact implementation/workflow-head tests [41726477853](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41726477853), optional Epitran/CRF [41726478205](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41726478205), and optional Goruut [41726477909](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41726477909) all SUCCESS; downloaded artifact contents inspected. | Report provenance, preserved Epitran resource hashes and sidecar integrity only. Gold remains 0; accuracy null. |

## External diagnostic report provenance — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-G2P-PROVENANCE-001 | DONE_VERIFIED (diagnostic reproducibility only) | PR [#106](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/106), exact head 942b6e8834878538c4e478c9195420b9618acd3d; RED [41725146714](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41725146714); tests [41726477853](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41726477853) SUCCESS (162 Python tests + 64 subtests; 54 browser tests); optional Epitran/CRF [41726478205](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41726478205) SUCCESS; optional Goruut [41726477909](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41726477909) SUCCESS. Artifact inspected: JSON + .sha256; expires 2027-02-01. | Harness SHA-256, corpus hash, engine/version, Python/platform and GitHub event metadata recorded; Epitran resource hashes preserved; integrity only. Independent adjudicated gold 0; accuracy null. |

## External diagnostic report provenance — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-G2P-PROVENANCE-001 | DONE_VERIFIED (diagnostic reproducibility only) | PR [#106](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/106), current head 8a3fd150a247144320c880756f187a256a890e2f; test-first RED [41725146714](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41725146714); exact-head tests [41725456860](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41725456860) SUCCESS (162 Python tests + 64 subtests; 54 browser tests); optional Epitran [41725456964](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41725456964) SUCCESS; optional Goruut [41725457027](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41725457027) SUCCESS. | Report records harness SHA-256, corpus hash, engine/version, Python implementation/version, platform and CI source revision; preserves Epitran resource hashes; JSON report has adjacent SHA-256 sidecar. Diagnostic integrity only. Independent adjudicated gold remains 0; accuracy null. |

## Unicode segmentation parity correction — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| UNICODE-SEGMENTATION-002 | DONE_VERIFIED | [PR #103](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/103), squash merge `8ca42933dec5f830ca70e092f25acaefe1e35ecc`; exact-head Python, Node, build, and built-site browser tests passed in [41713878227](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41713878227) and [41713891844](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41713891844). | Python now groups contiguous mixed-text runs like the browser, excludes Myanmar digits/punctuation U+1040..U+104B from phonetic text segmentation, retains unsupported Myanmar extensions as Myanmar units, and isolates C0/C1 controls. Structural parity only; no pronunciation claim. |

**Research boundary unchanged:** independent adjudicated Burmese IPA gold remains 0; empirical accuracy remains null.

# Burmese linguistic completion register — 2026-11-01

**Benchmark implementation merge:** `a5b844ec1d4f9be9264764ffa3652211fe78b6c5` (PR #100). **Handoff/register reconciliation merge:** `367819f9085eadc022079809a711b504527220ab` (PR #101).
**Latest post-merge exact-main evidence:** [engineering verification](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41707518082) SUCCESS; [Pages/deployed-site smoke](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41707518030) SUCCESS.
**Open pull requests:** none at this checkpoint.
**Research boundary:** Independent expert-adjudicated Burmese IPA gold remains 0; `data/benchmark/gold.tsv` is header-only; empirical accuracy remains null.
**Scope:** continue the existing master handoff; this register does not replace it.

## Held-out IPA benchmark integrity — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| IPA-BENCH-HELDOUT-001 | DONE_VERIFIED | PR #100 merged as `a5b844ec1d4f9be9264764ffa3652211fe78b6c5`; exact-main verification [workflow](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41707518082) SUCCESS; Pages/deployed-site smoke [workflow](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41707518030) SUCCESS. Export preserves split bucket and frozen manifest seed/version; scoring defaults to held-out test; explicit all-split mode is marked diagnostic; malformed/mixed split metadata and empty predictions fail closed. | Engineering evaluation integrity only. Independent expert-adjudicated Burmese IPA gold remains 0; `data/benchmark/gold.tsv` is header-only; empirical accuracy remains null. No gold rows, IPA labels or accuracy claims were fabricated. |


## Engineering integrity continuation — 2026-11-03

- **TSV-INPUT-001 — DONE_VERIFIED:** benchmark TSV ingestion now rejects duplicate/blank headers and nonblank rows with extra or missing fields; blank physical lines are ignored. Regression cases cover gold/prediction duplicate headers, extra gold cells, and truncated prediction rows.
- **Evidence:** test-first RED [41665726081](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41665726081); focused implementation GREEN [41665859814](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41665859814); implementation commit `f5951bb1248a0bee66a795bd375f7e4e80ce7043`.
- **Acceptance boundary:** input shape is validated before scoring. This does not create adjudicated IPA data or alter language accuracy status (gold 0; accuracy null).

## Strict JSON syntax — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| JSON-INPUT-003 | DONE_VERIFIED | Reject `NaN`, `Infinity`, and `-Infinity` in JSONL and license registry inputs. RED 41692649780; implementation CI 41694102074 SUCCESS (159 Python tests + 64 subtests; 54 built-site browser tests). | Reject non-standard JSON constants before corpus or rights validation; no linguistic labels or license terms changed. |

## License registry JSON integrity — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| JSONL-INPUT-002 | DONE_VERIFIED | Duplicate top-level and nested keys in `licenses.json` rejected. RED 41690120271; implementation CI 41690280710 SUCCESS (157 Python tests + 58 subtests; 54 built-site browser tests). | Rights registry cannot silently apply last-key-wins semantics; no license permission is inferred or broadened. |

## JSONL input integrity — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| JSONL-INPUT-001 | DONE_VERIFIED | Duplicate top-level and nested JSON object keys are rejected. RED 41687392202; exact implementation-head CI 41687710686 SUCCESS (155 Python tests + 58 subtests; 54 built-site browser tests). | Prevent silent last-key-wins corruption before corpus schema/provenance validation. No linguistic data or accuracy claims added. |

## Evidence-based task ledger

| ID | Status | Work remaining | Acceptance |
|---|---|---|---|
| MYA-GOLD-001 | BLOCKED | No independent expert-adjudicated lexical IPA gold exists; data/benchmark/gold.tsv contains only its header. | At least two independent text-based Burmese linguists, adjudication, source-located written dictionary/grammar entries, documented dialect/profile and IPA convention, and frozen held-out text fixtures. No audio. |
| MYA-PHON-001 | PARTIAL | Full vowel-combination derivation, coda/checked-syllable realization, tone/register/phonation inference and contextual allophony remain incomplete. | Source-located, expert-reviewed rule matrix with minimal pairs, explicit dialect scope and fail-closed unresolved cases. |
| MYA-IPA-001 | PARTIAL | Phonological vs phonetic IPA conventions and analysis of tone/register/phonation require specialist adjudication. | Versioned IPA convention, syllable/segment alignment, tone/phonation fields and adjudicated alternatives. |
| MYA-ROM-001 | PARTIAL | All 35 onset and 94 vendor-derived rime target rows have Ukrainian project candidates; PR #141 integrates a separate MLCTS-to-Ukrainian runtime adapter for supported syllable structures. The source rime inventory remains vendor-evidence-limited. | Verify the MLCTS inventory against primary MLC material; expand legal medial/devoicing, kinzi, asat and independent-vowel structures; retain explicit withholding for unsupported forms. |
| MYA-G2P-001 | DONE_VERIFIED (diagnostic harness only) | Goruut has 55/100 partial-coverage outputs; myG2P is CC BY-NC-SA 4.0 and temporary test-only. | No production promotion or source-data import without independent gold and explicit rights clearance. |
| MYA-UI-001 | TODO | Manual visual, keyboard, assistive-technology and mobile QA is not established by CI. | Recorded test matrix and deployed-site results. |
| MYA-REL-001 | PARTIAL | Production readiness blocked by gold, phonological coverage and external asset licensing. | All release gates met; owner makes any project-license decision; no restricted data/model bundled. |

## Current diagnostic evidence

The latest recorded myG2P v2.0/Goruut 100-row comparison is 98 outputs, 2 none; 43 complete, 55 partial, 2 unknown/no output; 98 stable; 69 unphonemized source fragments; strict source-label matches 0/100 and limited-notation matches 17/100. Epitran 1.35.3 had 0 exact source-label matches. These are diagnostic results, not accuracy. myG2P labels are not independent gold and the source is CC BY-NC-SA 4.0; temporary testing only is authorized. Independent gold remains 0; accuracy remains null.

## Open PR and branch reconciliation

PR [#53](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/53) remains open and untouched. Its branch is 5 commits ahead and 38 behind current main, changes only `index.html`, `system.html` and `src/web/styles.css`, and replaces the stylesheet wholesale. It is not safe to merge as-is; re-evaluate only if a fresh visual audit identifies a still-missing requirement, then port focused CSS changes on current main with browser tests. No existing user branch was deleted or rewritten.

## Execution order

1. Preserve fail-closed phonetic behavior.
2. Commission independent text-based IPA review of source-located Burmese dictionary and published phonological-description entries; record dialect/profile, convention, two independent reviews and adjudication.
3. Resolve the phonemic/phonetic convention and the interaction of tones, register, phonation and checked syllables with specialists.
4. Complete vowel/medial/coda derivation and the orthography-to-IPA matrix.
5. Verify MLCTS against primary Myanmar Language Commission sources; finish the separate MLCTS → Ukrainian adapter.
6. Conduct deployed UI/accessibility QA and asset-rights review.

## External dependencies / blockers

- Qualified Burmese phonologist/phonetic annotators and adjudicator.
- Rights-cleared written IPA sources and permission for derived labels; myG2P cannot be redistributed commercially under its current CC BY-NC-SA terms absent permission.
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
| IPA-GOLD-SPLIT-001 | DONE_VERIFIED | Deterministic hash-based group split; one frozen seed/version is enforced across the entire manifest, including distinct lexeme groups; new groups inherit the existing identity and conflicting overrides are rejected |
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

Historical audit note only: SLR80 is excluded from current text-only scope and is not an active source candidate.

This is **not IPA gold**. The line index contains orthographic transcripts; the paper's FST G2P is a pronunciation-generation/lexicon-bootstrapping tool, not independent adjudicated truth. The recording location does not by itself establish every speaker's dialect. No word-level acoustic timestamps are supplied, so any token selection requires manual alignment verification. The female-only sample cannot support gender-balanced generalization.

Do not acquire, process, annotate or use SLR80 recordings in this work.

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


## IPA-GOLD-SPLIT-MANIFEST-IDENTITY-001 — 2026-11-03

**Status: DONE_VERIFIED (runtime validator and split generator).** Root cause: the previous cross-file validator checked seed/version consistency only within each `lexeme_group_id`, allowing distinct groups in one corpus manifest to carry different seeds or versions. The split generator could also add a new group under a newly supplied seed while preserving older groups, silently creating a mixed manifest.

- Added regression coverage for mixed seeds and mixed versions across distinct groups, plus conflicting seed override when extending an existing manifest.
- The tests-only commits failed for the intended three behaviors: 41612967105. The implementation and assertion correction are on branch head `f1eb2af9c134`.
- Exact-head CI: [41613349719](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41613349719) SUCCESS — 142 Python tests + 48 subtests; the full repository workflow also completed successfully.
- New invariant: a single manifest has one `(seed, version)` pair globally; existing manifests retain that identity when extended; explicit conflicting overrides fail closed. A new corpus split design requires a separate versioned manifest.
- This is an engineering reproducibility fix only. It creates no linguistic labels and does not change gold count (0) or accuracy (`null`).

- Follow-up strictness regression: explicit empty `--seed` and `--version` must fail instead of falling through to defaults. Tests-only CI failed on both behaviours (41615393679); the corrected conditional default resolution passed exact-head CI 41615574734.


## Separate-manifest creation acceptance — 2026-11-03

**Status: DONE_VERIFIED on the dedicated PR branch; merge to main remains pending.** Added an acceptance test proving a genuinely new seed/version can be used when the caller supplies a separate empty JSONL input via `--splits`, while the existing frozen manifest remains untouched. Corrected the operator instructions: changing only `--output` does not reset the input manifest; the new-manifest workflow must use a new empty `--splits` file and a distinct `--output` file.

- PR [#90](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/90), final documentation head `239da6add4d23654a0cdb9ecb2a25c77fd588b58`; code/test checkpoint `acc29c519c72d9ba9cc48f30191e0c8a6ae73ae7` (the three subsequent commits are docs-only).
- Exact-head CI [41638537232](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41638537232) SUCCESS — 145 pytest tests + 48 subtests; web data validation OK; 54 browser tests passed.
- No linguistic gold rows were added; independent gold remains 0 and empirical accuracy remains `null`.


## Split-manifest integration checkpoint — 2026-11-03

**Burmese PR #90: DONE_VERIFIED on main.** Merged as `01d0d193f043508c6283ba77d70f9e9439402997`. The global manifest identity invariant and separate-manifest creation acceptance are now in the default branch. Exact-main workflow [41643388974](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41643388974) succeeded. No gold rows were added; adjudicated gold remains 0 and empirical accuracy remains `null`.


## Source-citation reconciliation — 2026-11-03

**Status: PARTIAL pending exact-head verification.** Added the WSSANLP 2016 record, exact ACL Anthology locator and scoped author–year references on a clean branch from latest main.

- Superseded PR #91 is not used as a merge candidate; this port must pass exact-head CI.
- No pronunciation labels or corpus records imported; source rights remain source-specific; independent gold remains 0 and accuracy remains `null`.


## MYA-EVIDENCE-AUDIT-001 — source scope and phonology matrix — 2026-11-03

**Status: PARTIAL pending exact-head CI and specialist review.** Updated the Burmese vowel/medial/prosody matrix and external-corpus triage with precise source scopes. Mooney & Repetti-Ludlow (2021) is a one-speaker competing analysis; Hlaing & Mikami's 99.93% is orthographic syllabification, not G2P; Oo et al. (2020) is orthographic speech, not IPA gold; Thu et al. (2016) uses a romanized inventory.

- No lexicon rows or pronunciation labels imported. License claims remain specific to individual artifacts; the LREC grammar and corpus rights are not conflated.
- Original PR #89 workflow [41631406950](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41631406950) succeeded before this clean port; fresh exact-head CI required.
- Independent gold remains 0 and empirical accuracy remains `null`.


## Continuation status sync — 2026-11-03

- Current main: `36ee99a83e6dd2bcf4670860908c3dbf53301ab8`; exact-main checks: tests 41647872126 SUCCESS; Pages/deployed-site 41647872084 SUCCESS.
- PR #89 is closed without merge; its mainline source and agent-guidance work was ported in focused commits. No open PRs were returned by the current open-PR query.
- Engineering improvements on main are verified at the stated commit; this does not promote linguistic validation or manual accessibility tasks to DONE.
- IPA gold remains 0; empirical accuracy remains null. Annotation staffing, convention approval, rights clearance, blind intake and adjudication remain BLOCKED on external human/evidence dependencies.


## BURMESE-METHOD-REFRESH-001 — upstream methodology snapshots — 2026-11-03

**Status: DONE_VERIFIED (reference audit).** Superpowers v7.0.1 current main: `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`; mattpocock/skills v1.3.2 release: `d1478fcb140db0b93c0c8df17bcfd311844749d0`, current main snapshot: `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`; Ponytail v5.3.3 release: `7801d061243d7b753bad0e0b3c057cd250b11755`, current main: `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846` (README-only post-pin change).

- Release pins and current-main snapshots are distinguished. No third-party runtime or skill files imported.

## 2026-11-03 — held-out benchmark split enforcement

| Task | Status | Evidence / remaining acceptance |
|---|---|---|
| IPA-BENCH-SPLIT-001 | DONE_VERIFIED (engineering contract) | Export preserves the frozen group-safe split; scorer defaults to test and requires explicit selection for train/dev/all. Exact-head tests [41651876020](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41651876020) SUCCESS on `af3ff6c5d3104a45ce5c1524b6083850c6dacd83`. This fixes the evaluation boundary, not linguistic gold. |

Independent gold remains 0 and accuracy remains null. No data labels were fabricated. The split-aware benchmark documentation is in `docs/benchmarking-and-external-ipa.md`.

## Frozen split manifest provenance — 2026-11-03

The export and benchmark now preserve and validate the complete frozen split identity, not only the bucket name: `split`, `split_seed`, and `split_version`. Every adjudicated row must carry non-empty seed/version metadata, and the benchmark rejects a TSV that mixes manifest identities. The report exposes the manifest seed/version and selected scoring split. This makes the evaluated test partition traceable to one exact manifest; it does not create linguistic gold or change the current zero-row accuracy status.


## 2026-11-03 — empty benchmark prediction input

| Task | Status | Evidence / remaining acceptance |
|---|---|---|
| IPA-BENCH-EMPTY-PREDICTIONS-001 | DONE_VERIFIED (engineering guard) | Header-only prediction TSV previously exited 0 and produced an empty `engines` object. Test-first regression failed on all three language repositories; the scorer now rejects an empty prediction dataset after checking gold and frozen split provenance. Missing individual predictions within a named engine remain denominator-counted. RED: [41655173696](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41655173696). Final exact-head tests: [41655504734](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41655504734) SUCCESS. |


## 2026-11-03 — benchmark identifier validation

| Task | Status | Evidence / acceptance |
|---|---|---|
| IPA-BENCH-IDENTIFIERS-001 | DONE_VERIFIED (engineering guard) | Reject whitespace-only gold IDs, prediction IDs and engine names while preserving non-empty identifiers exactly. Test-first RED: gold-ID run 41660769932; prediction-ID/engine run 41662075069. Final exact-code-head CI: 41662232565 SUCCESS (152 Python tests + 54 subtests; 54 built-site browser tests passed).  No linguistic labels or accuracy claims were added. |

## Verified continuation checkpoint — 2026-11-03 (late session)

- Default branch base: `145a24af36767e14a9f094c243c593a1a6e40af5`; continuation branch: `docs/current-state-checkpoint-20261103`.
- Latest mainline work retained: mixed-script runtime parity fix and the latest handoff/register reconciliation.
- Exact-main CI on the recorded default-branch head: tests 41714204905; Pages deploy 41714204591; all listed runs completed with SUCCESS. These are CI checks for the current implementation and deployment, not phonetic validation.
- Open pull requests: none at checkpoint time. No upstream methodology repository was modified; Superpowers, Matt Pocock Skills and Ponytail remain process references only.
- Engineering task ledger: benchmark split provenance, empty-prediction rejection and whitespace-only identifier validation remain **DONE_VERIFIED** as input-integrity safeguards. The recently merged runtime fix is verified by its own regression/CI; no new linguistic rule is inferred from it.
- Linguistic task ledger: independent adjudicated IPA gold remains **0**; gold export remains header-only and empirical accuracy remains `null`. The profile-specific IPA convention, two independent annotators, separate adjudicator, curator/blind intake and item-level rights review remain **BLOCKED** on external human decisions/resources. No labels or source-derived pronunciations were fabricated.
- Manual deployed-site keyboard, screen-reader, responsive and mobile QA remains **TODO**; automated browser checks do not satisfy these acceptance criteria.
- Local test execution was not available in this connector-only session. Verification evidence is the linked GitHub Actions CI on the exact recorded main SHA; do not report local tests as run.


## Research unblock checkpoint — 2026-11-03

- Prospective language-specific expert/researcher leads and additional candidate resources are recorded in docs/ipa-gold-collection-playbook.md with primary-source links and explicit limits.
- These are leads only: no one has been contacted or recruited; no IPA convention has been approved; no rights have been granted; no IPA labels were generated.
- The 30-item pilot remains BLOCKED until the acceptance conditions in the playbook are met. Candidate lexicon entries, phonetic respellings, model outputs, orthographic transcripts and source descriptions are not gold IPA.
- The next external action is to contact a qualified prospective reviewer and request nominations for two independent annotators plus a separate adjudicator; separately complete item-level rights review and blind-intake dry run.


## Burmese Wiktionary rights-source separation — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-RIGHTS-001 | DONE_VERIFIED (source attribution separation); rights decision remains BLOCKED | PR #111 merged at `8c323ff0d1236c5c6d36b2c2be0eac4d493163ab`; dataset-card CC BY 4.0 declaration and Myanmar Wiktionary local CC BY-SA 3.0 Unported/GFDL policy are separate source records and documentary claims. Main tests [41798078257](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41798078257), optional Epitran [41798080052](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41798080052), and Pages [41798078321](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41798078321) SUCCESS. | Provenance is correctly separated. Dataset rights remain CONFLICT/UNKNOWN until publisher/rightsholder clarification. No IPA labels, dataset imports or accuracy claims. |


## Post-merge checkpoint — Burmese Wiktionary provenance handoff (2026-11-04)

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-RIGHTS-001 | DONE_VERIFIED (documentation reconciliation); rights remain BLOCKED | PR #112 merged as `f4764d124e73005dab57512c93fdd59938e60ec3`. PR-head tests [41799540057](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41799540057) SUCCESS; post-merge main tests [41799853697](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41799853697) and Pages [41799853678](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41799853678) SUCCESS. | Handoff and register now describe the split source records. Dataset rights remain CONFLICT/UNKNOWN; 113 IPA values (0.51%) are not gold. |


## Post-merge checkpoint — Burmese Wiktionary provenance (2026-11-04)

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-RIGHTS-001 | DONE_VERIFIED (source attribution separation and handoff reconciliation); dataset rights remain BLOCKED | PR #111 merged `8c323ff0d1236c5c6d36b2c2be0eac4d493163ab`; PR #112 merged `f4764d124e73005dab57512c93fdd59938e60ec3`; PR #113 merged `040b0ea8f565ca9e443d361d1aaa658af978e9f2`. Main tests [41798078257](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41798078257), optional Epitran [41798080052](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41798080052), Pages [41798078321](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41798078321), PR-head tests [41799540057](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41799540057), post-merge tests [41799853697](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41799853697) and Pages [41799853678](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41799853678), post-PR113 tests [41800359629](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41800359629) and Pages [41800359623](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41800359623) all SUCCESS. | Dataset-card CC BY 4.0 and upstream CC BY-SA 3.0 Unported/GFDL remain conflicting; 113 IPA values (0.51%) are not gold. Obtain written rights clarification and per-entry profile/provenance before any import. |


## Language-specific IPA test fixtures — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-IPA-GOLD-FIXTURE-001 | DONE_VERIFIED | PR [#115](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/115) merged as `28ac47949efb725610023a24b69df1c584d598a7`; exact-main tests [41847895975](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41847895975) and Pages/deployed-site smoke [41847895765](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41847895765) SUCCESS. | Test fixture now uses Myanmar script and neutral test profile; regression asserts the Myanmar Unicode-block and matching profile metadata. This validates test-fixture integrity only, not phonological rules or IPA accuracy. Gold remains 0; accuracy null. |


## Burmese external pronunciation source audit — legacy non-text records excluded

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-MYG2P-SOURCE-001 | DONE_VERIFIED (source pinned and provenance/rights documented; no import) | Upstream `ye-kyaw-thu/myG2P` revision `54b5c76bb5a87fdbaaeddc1892e6ebd8f97ee225`; Version 2.0 file `ver2/myg2p.ver2.0.txt`, 2,329,808 bytes, Git blob SHA `0b2735f9a6f7fe28ae94c4baaf323d1db3015c3b`, five tab-separated fields including IPA; CC BY-NC-SA 4.0. Registered as `MYG2P2026`. | External diagnostic/comparator only. Non-commercial/share-alike terms, per-entry provenance, dialect and IPA convention must be respected. Existing test-only probe does not become gold or production approval. |
| BURMESE-OPENSLR80-AUDIO-001 | DEFERRED / OUT OF SCOPE | Historical source metadata only; not part of current text-only work. | No recording acquisition, processing, annotation or audio-derived labels. Not a blocker for text-based research. |

**Evidence boundary:** source records and provenance tests are complete; no external dictionary or corpus rows were imported. Independent adjudicated Burmese IPA gold remains 0; accuracy remains null.


## IPA gold release-gate profile consistency — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| IPA-GOLD-RELEASE-PROFILE-001 | DONE_VERIFIED (engineering guard) | Shared `scripts/ipa_gold_corpus.py` now rejects adjudicated corpora that mix target-profile identity (`id`, `variety`, `region`, `register`) or IPA kinds. New regression tests cover both failures. PR #117 merged as `085ce5a2da4a07dfbf606a9892c78a4d3bbb9d91`; exact PR-head CI [41870132273](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41870132273) SUCCESS; post-merge CI [41870579420](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41870579420) SUCCESS; Pages [41870579398](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41870579398) SUCCESS. | Does not prove profile approval, annotator qualifications, blindness, linguistic contrast coverage, or IPA accuracy. A specialist-reviewed language-specific coverage report remains required before benchmark readiness. |


## Expert recruitment lead revalidation — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-IPA-GOLD-RECRUITMENT-LEADS-001 | PARTIAL | New specialist leads: Chiara Repetti-Ludlow's 2023 Burmese sonorant acoustic study and 2021 Burmese tone/sonority paper; Yuttaporn Naksuk and Tanintorn Limpasiri's comparative phonology review across eight Burmese dialects; University of Yangon referral lead. These do not establish native Yangon annotator qualification, availability or recruitment. | No candidate has been contacted, consented, recruited or approved. Close only after two independent qualified target-variety annotators, separate adjudicator, non-annotating curator, conflict checks, secure blind intake and written role/terms confirmation are documented. |

## Deterministic rule engine — 2026-11-11

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-DETERMINISTIC-RULE-ENGINE-001 | DONE_VERIFIED (engineering); linguistic coverage PARTIAL | PR #128 merged as `cd3a1503e79d32b09a6d2d5206340a37cfd3283b`. Exact main tests [43018103155](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43018103155) and Pages + asset smoke [43018103391](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43018103391) SUCCESS; live site: https://clippyfirst.github.io/Burmese-Ukrainian-Phonetic-System-/. | Deterministic rule contract and publication verified. Expert-adjudicated Yangon IPA gold is still required before correctness/accuracy claims. |

## Final deterministic-engine verification — 2026-11-11

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-DETERMINISTIC-RULE-ENGINE-001 | DONE_VERIFIED (engineering); linguistic coverage PARTIAL | Final main head `9bece0a50a367f3f58336d2aba7016ac4af86156`; exact-head tests [43019216137](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43019216137) and Pages + smoke [43019216297](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43019216297) SUCCESS. | Deterministic implementation and publication verified. Independent expert-adjudicated Yangon IPA gold remains necessary for broader correctness/accuracy claims. |


## 2026-11-11 — Ukrainian practical transcription continuation

| Work item | Status | Evidence / acceptance |
|---|---|---|
| Python IPA → Ukrainian adapter integrated after deterministic Burmese IPA | DONE_VERIFIED | Previous code revision `530cefbfc874b777650bd7e7ccdb5888534ab348`; 180 Python tests + 66 subtests |
| Canonical CSV and generated browser adapter | DONE_VERIFIED | Generated-data freshness, build and Node tests passed on previous code revision |
| Target distinctions /h, ɦ/ → г, /ɡ/ → ґ, /x/ → х; /w/ → в, contextual /j/ yotation, affricates ц/дз/ч/дж | DONE_VERIFIED | Explicit project policy; official 2026 standard generally uses г for foreign [g], so ґ is a contrast-preserving project choice |
| Browser fail-closed behavior for kinzi, medials and conjuncts | PARTIAL | Implemented; final Playwright run is queued and unverified |
| Accuracy of proposed Ukrainian correspondences | PARTIAL | No independent adjudicated IPA/Ukrainian gold set |
| Final browser CI | BLOCKED | Run 43095578672 queued with zero jobs started |
| Independent text-only IPA gold set | BLOCKED | Requires sourced and adjudicated Yangon-profile IPA labels and held-out evaluation |
| Audio | DEFERRED | Outside current task scope |


## Provisional onset IPA fallback — 2026-11-11

| Work item | Status | Evidence / acceptance |
|---|---|---|
| Python onset-only preview for unresolved Burmese syllables | PARTIAL | Separate provisional IPA/Ukrainian fields and trace; canonical ipa/ukrainian withheld; unresolved rime marked ?. Regression added. Commit 6936f01d3ff320574b8802c7af348d687e63ce17 |
| Browser onset-only preview | PARTIAL | Reuses Yangon onset IPA and IPA adapter; displays provisional IPA and ?. Commit 5b83f5d3674b9e6d2f4114047bd67be5a5440719 |
| Browser regression | PARTIAL | Source-contract assertions added; no executed cross-runtime parity fixture yet. Commit 36b6ebf5a1d5a03b0c4d7a95aae2d842046e4152 |
| Dedicated Yangon grapheme-position evidence registry | TODO | Register primary-source locator, profile, exact onset position, rule ID, scope and reviewer status for every fallback entry |
| Exact-head CI and Chromium verification | BLOCKED pending run | No workflow run was returned for final head 36b6ebf5a1d5a03b0c4d7a95aae2d842046e4152 |
| Vowel/coda/asat/medial/kinzi/conjunct fallback | TODO | Do not extend without source-backed positional rules; no such guesses were added |


## Verification result — provisional onset preview, 2026-11-11

| Work item | Status | Evidence |
|---|---|---|
| Python fallback implementation and regression | DONE_VERIFIED (engineering behavior) | Code/test head aac1d6834b4c29e04f01477af1583a2be9eba485; workflow 43101914347 PASS: 182 tests + 66 subtests |
| Browser fallback detail and canonical fail-closed behavior | DONE_VERIFIED (engineering behavior) | Workflow 43101914347 PASS; Playwright 54/54; production build, generated-data freshness and Node tests PASS |
| Optional Epitran raw-output comparator | DONE_VERIFIED (workflow) | Run 43101914423 PASS; not an independent IPA accuracy benchmark |
| Dedicated Yangon grapheme-position evidence registry | TODO | Existing onset inventory is reused; exact per-entry primary-source locators, scope and adjudication remain required |
| Functional Python/browser parity fixture | TODO | Browser tests cover behavior, but no shared structured cross-runtime fixture yet |
| Full Myanmar grapheme fallback | DEFERRED / evidence-limited | Only isolated bare consonants receive onset-only preview; vowel/rime/coda/asat/medial/kinzi/conjunct/tone structures remain fail-closed |


## Unicode grapheme accounting sweep — 2026-11-12

| Work item | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-UNICODE-ACCOUNTING-001 | DONE_VERIFIED (structural/input accounting) | PR #134 merged as `374e1a883ffc2aea5c729377e5aabf22778cbffd`; exact-head tests [43184645239](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43184645239) SUCCESS. Exhaustive sweep covers assigned Unicode L/M code points in all four Myanmar blocks. | Lossless source and code-point trace only; no IPA value is inferred for out-of-profile characters. |
| BURMESE-PHONOLOGY-100-001 | PARTIAL / BLOCKED by evidence | Existing parser/IPA engine withholds unsupported structures; no independent Yangon-profile adjudicated gold. | Requires source-located positional evidence for each supported context, shared Python/browser fixtures, independent adjudication and held-out evaluation. |


## Burmese provisional onset registry reconciliation — 2026-11-12

| Work item | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-ONSET-HINT-REGISTRY-001 | DONE_VERIFIED (candidate registry parity) | PR #136 merged as `9931acf8c4b8b9a16d210e44eca47f1319f04be2`; exact-head workflow [43185426033](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43185426033) SUCCESS. Python provisional table now includes the existing CSV/browser candidate for U+1009 `ဉ` /ɲ/. | Provisional onset preview only. Canonical IPA remains withheld for isolated bare consonants; no gold label or accuracy claim added. |
| BURMESE-ONSET-IPA-PARITY-001 | PARTIAL / EVIDENCE-LIMITED | Existing `ရ` candidate differs: CSV/browser `r`, Python `ɹ`; both analysis-dependent. | Requires source-located Yangon-profile evidence and explicit broad/narrow IPA convention before choosing or synchronizing a value. |


## MLCTS Latin → Ukrainian target matrix — 2026-11-12

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-ROM-UA-TARGET-001 | DONE_VERIFIED | Branch `feat/burmese-romanization-ukrainian-matrix-completion-2026-11-12`; exact-head test run [43221074232](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43221074232) SUCCESS: 187 Python tests + 66 subtests, 54 Node tests, build, generated-data freshness and built-site Playwright all passed. All 35 onset and 94 vendor-rime rows have target candidates. | Table coverage verified; project orthographic rendering only, not IPA or primary-source verification of vendor rimes. Runtime adapter and full source inventory remain open. |
| MYA-ROM-UA-001 | PARTIAL | PR #141 integrates a separate MLCTS → Ukrainian runtime adapter and UI; exact-head and mainline tests pass. | Expand source-verified structures and preserve unsupported/ambiguous sequences without IPA fallback. |


## Burmese Ukrainian target matrix — post-merge evidence — 2026-11-12

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-ROM-UA-TARGET-001 | DONE_VERIFIED | Merged PR [#138](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/138), merge `1d7045d9695d571017633a2e294b718a13ee5bce`; mainline tests [43221871111](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43221871111) and Pages [43221870932](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43221870932) SUCCESS. | 35 onset + 94 vendor-rime target rows are covered. Vendor-source evidence remains EVIDENCE_LIMITED; runtime adapter and complete source inventory remain open. |


## Burmese MLCTS Ukrainian runtime adapter — 2026-11-12

| ID | Status | Evidence | Remaining acceptance |
|---|---|---|---|
| MYA-ROM-UA-TARGET-001 | DONE_VERIFIED | All 35 onset + 94 vendor-rime target rows populated; merged PR #138; matrix CI passed. | None for existing inventory rows. |
| MYA-ROM-UA-001 | PARTIAL | PR #141 adds `src/web/romanization-ukrainian.js`, syllable-level longest-match onset/medial/rime mapping, separate UI output, and tests for all 94 rime rows and all onset rows. Exact-head tests [43226578745](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43226578745) and push [43226566617](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43226566617) SUCCESS: 187 Python tests + 66 subtests, 18 Node tests, 55 Playwright tests, build and generated-data freshness. | Expand source inventory and support/adjudicate remaining medial/devoicing/kinzi/asat/independent-vowel combinations; preserve unknown sequences as explicit unsupported rather than guessing. |
| MYA-ROM-MATRIX-001 | PARTIAL | Runtime adapter covers current 94 vendor-derived rime keys plus supported onset and `y/r/w` medial sequences. | Verify complete orthographic inventory against original MLC source; include all legal Burmese sequences, numerals and punctuation. |
| MYA-ROM-LIC-001 | PARTIAL | Mya2Rom 0.4.4 attribution and CC-BY-SA-4.0 notice retained. | Audit each vendored table/data component and upstream licensing/provenance. |

All target renderings remain `PROPOSED`; vendor-derived source rime provenance remains `EVIDENCE_LIMITED`. This is orthographic MLCTS rendering, not IPA or pronunciation transcription.



Latest final exact-head verification after adding explicit withholding for Myanmar code points outside the romanization support inventory: [tests 43227199213](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43227199213) SUCCESS on `4a2cb24ae9af2bc5e4d9341de65d0a55e07b6e09`: 187 Python tests + 66 subtests, 19 Node tests, 55 Playwright browser tests, production build and generated-data freshness. Unsupported Myanmar code points are now explicitly bracketed in the Ukrainian romanization output.


## MLCTS Ukrainian runtime adapter — mainline post-merge verification — 2026-11-12

- PR [#141](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/141) merged as `3fa33864b774c716da5bf6c9778a963148fb9974`.
- Mainline tests [43227806284](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43227806284) and Pages deployment [43227806266](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43227806266) both SUCCESS.
- Mainline test evidence: 187 Python tests + 66 subtests, 19 Node tests, 55 Playwright browser tests, production build and generated-data freshness all passed.
- Acceptance remains PARTIAL: current Mya2Rom-derived rime inventory is EVIDENCE_LIMITED, and unrepresented legal syllable structures remain visibly unsupported rather than guessed.


## MLCTS runtime mainline reconciliation — 2026-11-12

| ID | Status | Current evidence | Acceptance boundary |
|---|---|---|---|
| MYA-ROM-UA-TARGET-001 | DONE_VERIFIED | 35 onset + 94 vendor-derived rime target rows populated; PR #138 merged; current-main tests [43228612973](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43228612973) and Pages [43228612998](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43228612998) SUCCESS. | Completeness of inventoried table only; vendor-rime source provenance remains EVIDENCE_LIMITED. |
| MYA-ROM-UA-001 | PARTIAL | PR #141 merged as `3fa33864b774c716da5bf6c9778a963148fb9974`; separate runtime adapter/UI executes supported onset, medial and rime mappings; unknown material remains visibly unsupported. | Full source-verified MLCTS inventory and all legal Burmese syllable structures. |
| MYA-ROM-MATRIX-001 | PARTIAL | Runtime supports the existing 94 rime rows with supported onset and y/r/w medial sequences. | Primary MLC source verification; legal medial/devoicing/kinzi/asat/independent-vowel combinations; numerals and punctuation source handling. |
| MYA-ROM-LIC-001 | PARTIAL | Mya2Rom attribution and CC-BY-SA-4.0 notice retained. | Component-by-component audit of vendored code, table data and upstream-derived sources/rights. |

No MLCTS output was promoted to IPA or pronunciation evidence. Independent expert-adjudicated IPA gold remains 0 and empirical accuracy remains null.


## Burmese medials, G2P and coda-parsing update — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-MEDIAL-INVENTORY-001 | DONE_VERIFIED (orthographic inventory) | Unicode 18, WG2 N2827 and Hlaing (2014) support four basic signs plus seven two-/three-medial codepoint combinations. The thesis has a duplicated prose label in the final RA+WA+HA row; codepoints are unambiguous. | This does not assign IPA values to all combinations. |
| MYA-MEDIAL-PHONOLOGY-001 | PARTIAL / CONTEXT_DEPENDENT | Ishida 2026 and pinned Google Thrax: YA/RA typically /j/ with onset-specific exceptions; WA /w/ vs rime /ʊ/; HA aspiration/devoicing and fused outcomes. Watkins (2001) and Green (2002) support secondary articulation /mj/ analysis. | Complete onset × medial × rime × coda × tone matrix and independent Yangon adjudication. |
| MYA-MRAN-IPA-001 | PARTIAL / CROSS-SOURCE CANDIDATE | Wiktionary /mjàɴ/; Green /mj/ plus placeless nasal /N/; Google WFST raw output m j àɴ. Epitran 1.35.3 instead returns məjaɴ. Both external outputs have zero gold and null accuracy. | Independent text-based expert review against written lexical and phonological sources; settle phonemic /N/ vs surface nasalization and schwa disagreement. |
| MYA-ASAT-CODA-001 | DONE_VERIFIED (structural parser parity) | Python now attaches base consonant + U+103A as coda within preceding syllable, matching browser. Regression cases: မြန်, မြန်မာ, ကတ်. Exact-head tests [43325991671](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43325991671) SUCCESS. | Broader segmentation remains partial pending independent annotated boundary corpus. |
| MYA-GOOGLE-FST-001 | DONE_VERIFIED (source/license and raw diagnostic) | Pinned grammar commit a90601024f07ab7e96c911243324e0adeb16da96 and root LICENSE declare Apache-2.0; raw probe run 43084508359 returned m j àɴ for မြန်, no gold. | Optional comparator only; do not replace deterministic engine or treat output as gold. |
| MYA-CRF-DIAG-001 | PARTIAL / DIAGNOSTIC ONLY | Exact branch run [43325991496](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43325991496): 84/100 source-concordant; YA 10/14, RA 17/20, WA 13/15, HA 7/8; zero gold and accuracy null; exact မြန် absent. | Train/test overlap unknown; labels are from myG2P CC BY-NC-SA 4.0. |
| MYA-TONE-001 | PARTIAL / COMPETING ANALYSES | Green and LREC 2020 use four-tone descriptions; Duan & Zhu (2025) propose eight tones across modal/lower-breathy registers. | Full empirical review, profile scope and expert-approved convention. |
| MYA-IPA-GOLD-001 | BLOCKED | No independent expert-adjudicated Burmese IPA gold for these medial/coda cells. | Two independent qualified reviewers, third adjudicator, source-located written dictionary/grammar examples, documented broad-vs-narrow IPA convention and frozen held-out text fixtures. No audio is required or in scope. |
| MYA-PR129-RECONCILIATION-001 | LEFT OPEN / NOT MERGED | Draft PR #129 is 53 commits ahead / 17 behind current main and non-mergeable; its research findings were reused, broad hybrid implementation left untouched. | Rebase/reconcile only as a separate, reviewed integration task. |

The project remains PARTIAL PROTOTYPE; empirical accuracy remains null.


## IPA nasalization metadata boundary — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-IPA-NASALIZATION-SCHEMA-001 | DEFERRED | The typed IPA schema preserves literal IPA, kind, boundaries, tone, length and phonation but has no dedicated nasalization property. Literal IPA can preserve the diacritic. | Decide after expert-approved phonemic /N/ vs surface nasalization convention; only then consider a backward-compatible optional schema field. No schema change in this research pass. |


## Legacy non-text corpus metadata — excluded from active scope (2026-11-13)

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-UCSY-SC1-AUDIO-001 | DEFERRED / OUT OF SCOPE | Rights conflict and corpus metadata retained for historical audit only. | No acquisition, processing, annotation or audio-derived IPA labels; not a blocker for text-only research. |
## Burmese Wiktionary IPA source review — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-IPA-001 | PARTIAL (discovery lead; rights conflict unresolved) | Dataset card: 22,191 records, 20,759 headwords, 113 IPA values (0.51%), snapshot 2026-08-01, CC BY 4.0 declaration. Myanmar Wiktionary local policy (last edited 2024-12-06): CC BY-SA 3.0 Unported/GFDL. No per-entry dialect/convention, audio, annotator/adjudication or detailed locators in the card. | No import into gold. Clarify rights with publisher/rightsholder; then item-level profile/source/IPA audit and independent specialist review. MLCTS is not IPA. |

## Post-merge provenance checkpoint — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-G2P-PROVENANCE-001 | DONE_VERIFIED (PR-head verified; post-merge push CI not independently surfaced) | PR [#106](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/106) merged as 76426383038ee18a4cf5f2136379b25c08a40d7e. Exact implementation/workflow-head tests [41726477853](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41726477853), optional Epitran/CRF [41726478205](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41726478205), and optional Goruut [41726477909](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41726477909) all SUCCESS; downloaded artifact contents inspected. | Report provenance, preserved Epitran resource hashes and sidecar integrity only. Gold remains 0; accuracy null. |

## External diagnostic report provenance — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-G2P-PROVENANCE-001 | DONE_VERIFIED (diagnostic reproducibility only) | PR [#106](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/106), exact head 942b6e8834878538c4e478c9195420b9618acd3d; RED [41725146714](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41725146714); tests [41726477853](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41726477853) SUCCESS (162 Python tests + 64 subtests; 54 browser tests); optional Epitran/CRF [41726478205](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41726478205) SUCCESS; optional Goruut [41726477909](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41726477909) SUCCESS. Artifact inspected: JSON + .sha256; expires 2027-02-01. | Harness SHA-256, corpus hash, engine/version, Python/platform and GitHub event metadata recorded; Epitran resource hashes preserved; integrity only. Independent adjudicated gold 0; accuracy null. |

## External diagnostic report provenance — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-G2P-PROVENANCE-001 | DONE_VERIFIED (diagnostic reproducibility only) | PR [#106](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/106), current head 8a3fd150a247144320c880756f187a256a890e2f; test-first RED [41725146714](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41725146714); exact-head tests [41725456860](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41725456860) SUCCESS (162 Python tests + 64 subtests; 54 browser tests); optional Epitran [41725456964](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41725456964) SUCCESS; optional Goruut [41725457027](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41725457027) SUCCESS. | Report records harness SHA-256, corpus hash, engine/version, Python implementation/version, platform and CI source revision; preserves Epitran resource hashes; JSON report has adjacent SHA-256 sidecar. Diagnostic integrity only. Independent adjudicated gold remains 0; accuracy null. |

## Unicode segmentation parity correction — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| UNICODE-SEGMENTATION-002 | DONE_VERIFIED | [PR #103](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/103), squash merge `8ca42933dec5f830ca70e092f25acaefe1e35ecc`; exact-head Python, Node, build, and built-site browser tests passed in [41713878227](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41713878227) and [41713891844](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41713891844). | Python now groups contiguous mixed-text runs like the browser, excludes Myanmar digits/punctuation U+1040..U+104B from phonetic text segmentation, retains unsupported Myanmar extensions as Myanmar units, and isolates C0/C1 controls. Structural parity only; no pronunciation claim. |

**Research boundary unchanged:** independent adjudicated Burmese IPA gold remains 0; empirical accuracy remains null.

# Burmese linguistic completion register — 2026-11-01

**Benchmark implementation merge:** `a5b844ec1d4f9be9264764ffa3652211fe78b6c5` (PR #100). **Handoff/register reconciliation merge:** `367819f9085eadc022079809a711b504527220ab` (PR #101).
**Latest post-merge exact-main evidence:** [engineering verification](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41707518082) SUCCESS; [Pages/deployed-site smoke](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41707518030) SUCCESS.
**Open pull requests:** none at this checkpoint.
**Research boundary:** Independent expert-adjudicated Burmese IPA gold remains 0; `data/benchmark/gold.tsv` is header-only; empirical accuracy remains null.
**Scope:** continue the existing master handoff; this register does not replace it.

## Held-out IPA benchmark integrity — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| IPA-BENCH-HELDOUT-001 | DONE_VERIFIED | PR #100 merged as `a5b844ec1d4f9be9264764ffa3652211fe78b6c5`; exact-main verification [workflow](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41707518082) SUCCESS; Pages/deployed-site smoke [workflow](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41707518030) SUCCESS. Export preserves split bucket and frozen manifest seed/version; scoring defaults to held-out test; explicit all-split mode is marked diagnostic; malformed/mixed split metadata and empty predictions fail closed. | Engineering evaluation integrity only. Independent expert-adjudicated Burmese IPA gold remains 0; `data/benchmark/gold.tsv` is header-only; empirical accuracy remains null. No gold rows, IPA labels or accuracy claims were fabricated. |


## Engineering integrity continuation — 2026-11-03

- **TSV-INPUT-001 — DONE_VERIFIED:** benchmark TSV ingestion now rejects duplicate/blank headers and nonblank rows with extra or missing fields; blank physical lines are ignored. Regression cases cover gold/prediction duplicate headers, extra gold cells, and truncated prediction rows.
- **Evidence:** test-first RED [41665726081](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41665726081); focused implementation GREEN [41665859814](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41665859814); implementation commit `f5951bb1248a0bee66a795bd375f7e4e80ce7043`.
- **Acceptance boundary:** input shape is validated before scoring. This does not create adjudicated IPA data or alter language accuracy status (gold 0; accuracy null).

## Strict JSON syntax — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| JSON-INPUT-003 | DONE_VERIFIED | Reject `NaN`, `Infinity`, and `-Infinity` in JSONL and license registry inputs. RED 41692649780; implementation CI 41694102074 SUCCESS (159 Python tests + 64 subtests; 54 built-site browser tests). | Reject non-standard JSON constants before corpus or rights validation; no linguistic labels or license terms changed. |

## License registry JSON integrity — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| JSONL-INPUT-002 | DONE_VERIFIED | Duplicate top-level and nested keys in `licenses.json` rejected. RED 41690120271; implementation CI 41690280710 SUCCESS (157 Python tests + 58 subtests; 54 built-site browser tests). | Rights registry cannot silently apply last-key-wins semantics; no license permission is inferred or broadened. |

## JSONL input integrity — 2026-11-03

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| JSONL-INPUT-001 | DONE_VERIFIED | Duplicate top-level and nested JSON object keys are rejected. RED 41687392202; exact implementation-head CI 41687710686 SUCCESS (155 Python tests + 58 subtests; 54 built-site browser tests). | Prevent silent last-key-wins corruption before corpus schema/provenance validation. No linguistic data or accuracy claims added. |

## Evidence-based task ledger

| ID | Status | Work remaining | Acceptance |
|---|---|---|---|
| MYA-GOLD-001 | BLOCKED | No independent expert-adjudicated lexical IPA gold exists; data/benchmark/gold.tsv contains only its header. | At least two independent text-based Burmese linguists, adjudication, source-located written dictionary/grammar entries, documented dialect/profile and IPA convention, and frozen held-out text fixtures. No audio. |
| MYA-PHON-001 | PARTIAL | Full vowel-combination derivation, coda/checked-syllable realization, tone/register/phonation inference and contextual allophony remain incomplete. | Source-located, expert-reviewed rule matrix with minimal pairs, explicit dialect scope and fail-closed unresolved cases. |
| MYA-IPA-001 | PARTIAL | Phonological vs phonetic IPA conventions and analysis of tone/register/phonation require specialist adjudication. | Versioned IPA convention, syllable/segment alignment, tone/phonation fields and adjudicated alternatives. |
| MYA-ROM-001 | PARTIAL | All 35 onset and 94 vendor-derived rime target rows have Ukrainian project candidates; PR #141 integrates a separate MLCTS-to-Ukrainian runtime adapter for supported syllable structures. The source rime inventory remains vendor-evidence-limited. | Verify the MLCTS inventory against primary MLC material; expand legal medial/devoicing, kinzi, asat and independent-vowel structures; retain explicit withholding for unsupported forms. |
| MYA-G2P-001 | DONE_VERIFIED (diagnostic harness only) | Goruut has 55/100 partial-coverage outputs; myG2P is CC BY-NC-SA 4.0 and temporary test-only. | No production promotion or source-data import without independent gold and explicit rights clearance. |
| MYA-UI-001 | TODO | Manual visual, keyboard, assistive-technology and mobile QA is not established by CI. | Recorded test matrix and deployed-site results. |
| MYA-REL-001 | PARTIAL | Production readiness blocked by gold, phonological coverage and external asset licensing. | All release gates met; owner makes any project-license decision; no restricted data/model bundled. |

## Current diagnostic evidence

The latest recorded myG2P v2.0/Goruut 100-row comparison is 98 outputs, 2 none; 43 complete, 55 partial, 2 unknown/no output; 98 stable; 69 unphonemized source fragments; strict source-label matches 0/100 and limited-notation matches 17/100. Epitran 1.35.3 had 0 exact source-label matches. These are diagnostic results, not accuracy. myG2P labels are not independent gold and the source is CC BY-NC-SA 4.0; temporary testing only is authorized. Independent gold remains 0; accuracy remains null.

## Open PR and branch reconciliation

PR [#53](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/53) remains open and untouched. Its branch is 5 commits ahead and 38 behind current main, changes only `index.html`, `system.html` and `src/web/styles.css`, and replaces the stylesheet wholesale. It is not safe to merge as-is; re-evaluate only if a fresh visual audit identifies a still-missing requirement, then port focused CSS changes on current main with browser tests. No existing user branch was deleted or rewritten.

## Execution order

1. Preserve fail-closed phonetic behavior.
2. Commission independent text-based IPA review of source-located Burmese dictionary and published phonological-description entries; record dialect/profile, convention, two independent reviews and adjudication.
3. Resolve the phonemic/phonetic convention and the interaction of tones, register, phonation and checked syllables with specialists.
4. Complete vowel/medial/coda derivation and the orthography-to-IPA matrix.
5. Verify MLCTS against primary Myanmar Language Commission sources; finish the separate MLCTS → Ukrainian adapter.
6. Conduct deployed UI/accessibility QA and asset-rights review.

## External dependencies / blockers

- Qualified Burmese phonologist/phonetic annotators and adjudicator.
- Rights-cleared written IPA sources and permission for derived labels; myG2P cannot be redistributed commercially under its current CC BY-NC-SA terms absent permission.
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
| IPA-GOLD-SPLIT-001 | DONE_VERIFIED | Deterministic hash-based group split; one frozen seed/version is enforced across the entire manifest, including distinct lexeme groups; new groups inherit the existing identity and conflicting overrides are rejected |
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

Historical audit note only: SLR80 is excluded from current text-only scope and is not an active source candidate.

This is **not IPA gold**. The line index contains orthographic transcripts; the paper's FST G2P is a pronunciation-generation/lexicon-bootstrapping tool, not independent adjudicated truth. The recording location does not by itself establish every speaker's dialect. No word-level acoustic timestamps are supplied, so any token selection requires manual alignment verification. The female-only sample cannot support gender-balanced generalization.

Do not acquire, process, annotate or use SLR80 recordings in this work.

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


## IPA-GOLD-SPLIT-MANIFEST-IDENTITY-001 — 2026-11-03

**Status: DONE_VERIFIED (runtime validator and split generator).** Root cause: the previous cross-file validator checked seed/version consistency only within each `lexeme_group_id`, allowing distinct groups in one corpus manifest to carry different seeds or versions. The split generator could also add a new group under a newly supplied seed while preserving older groups, silently creating a mixed manifest.

- Added regression coverage for mixed seeds and mixed versions across distinct groups, plus conflicting seed override when extending an existing manifest.
- The tests-only commits failed for the intended three behaviors: 41612967105. The implementation and assertion correction are on branch head `f1eb2af9c134`.
- Exact-head CI: [41613349719](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41613349719) SUCCESS — 142 Python tests + 48 subtests; the full repository workflow also completed successfully.
- New invariant: a single manifest has one `(seed, version)` pair globally; existing manifests retain that identity when extended; explicit conflicting overrides fail closed. A new corpus split design requires a separate versioned manifest.
- This is an engineering reproducibility fix only. It creates no linguistic labels and does not change gold count (0) or accuracy (`null`).

- Follow-up strictness regression: explicit empty `--seed` and `--version` must fail instead of falling through to defaults. Tests-only CI failed on both behaviours (41615393679); the corrected conditional default resolution passed exact-head CI 41615574734.


## Separate-manifest creation acceptance — 2026-11-03

**Status: DONE_VERIFIED on the dedicated PR branch; merge to main remains pending.** Added an acceptance test proving a genuinely new seed/version can be used when the caller supplies a separate empty JSONL input via `--splits`, while the existing frozen manifest remains untouched. Corrected the operator instructions: changing only `--output` does not reset the input manifest; the new-manifest workflow must use a new empty `--splits` file and a distinct `--output` file.

- PR [#90](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/90), final documentation head `239da6add4d23654a0cdb9ecb2a25c77fd588b58`; code/test checkpoint `acc29c519c72d9ba9cc48f30191e0c8a6ae73ae7` (the three subsequent commits are docs-only).
- Exact-head CI [41638537232](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41638537232) SUCCESS — 145 pytest tests + 48 subtests; web data validation OK; 54 browser tests passed.
- No linguistic gold rows were added; independent gold remains 0 and empirical accuracy remains `null`.


## Split-manifest integration checkpoint — 2026-11-03

**Burmese PR #90: DONE_VERIFIED on main.** Merged as `01d0d193f043508c6283ba77d70f9e9439402997`. The global manifest identity invariant and separate-manifest creation acceptance are now in the default branch. Exact-main workflow [41643388974](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41643388974) succeeded. No gold rows were added; adjudicated gold remains 0 and empirical accuracy remains `null`.


## Source-citation reconciliation — 2026-11-03

**Status: PARTIAL pending exact-head verification.** Added the WSSANLP 2016 record, exact ACL Anthology locator and scoped author–year references on a clean branch from latest main.

- Superseded PR #91 is not used as a merge candidate; this port must pass exact-head CI.
- No pronunciation labels or corpus records imported; source rights remain source-specific; independent gold remains 0 and accuracy remains `null`.


## MYA-EVIDENCE-AUDIT-001 — source scope and phonology matrix — 2026-11-03

**Status: PARTIAL pending exact-head CI and specialist review.** Updated the Burmese vowel/medial/prosody matrix and external-corpus triage with precise source scopes. Mooney & Repetti-Ludlow (2021) is a one-speaker competing analysis; Hlaing & Mikami's 99.93% is orthographic syllabification, not G2P; Oo et al. (2020) is orthographic speech, not IPA gold; Thu et al. (2016) uses a romanized inventory.

- No lexicon rows or pronunciation labels imported. License claims remain specific to individual artifacts; the LREC grammar and corpus rights are not conflated.
- Original PR #89 workflow [41631406950](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41631406950) succeeded before this clean port; fresh exact-head CI required.
- Independent gold remains 0 and empirical accuracy remains `null`.


## Continuation status sync — 2026-11-03

- Current main: `36ee99a83e6dd2bcf4670860908c3dbf53301ab8`; exact-main checks: tests 41647872126 SUCCESS; Pages/deployed-site 41647872084 SUCCESS.
- PR #89 is closed without merge; its mainline source and agent-guidance work was ported in focused commits. No open PRs were returned by the current open-PR query.
- Engineering improvements on main are verified at the stated commit; this does not promote linguistic validation or manual accessibility tasks to DONE.
- IPA gold remains 0; empirical accuracy remains null. Annotation staffing, convention approval, rights clearance, blind intake and adjudication remain BLOCKED on external human/evidence dependencies.


## BURMESE-METHOD-REFRESH-001 — upstream methodology snapshots — 2026-11-03

**Status: DONE_VERIFIED (reference audit).** Superpowers v7.0.1 current main: `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`; mattpocock/skills v1.3.2 release: `d1478fcb140db0b93c0c8df17bcfd311844749d0`, current main snapshot: `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`; Ponytail v5.3.3 release: `7801d061243d7b753bad0e0b3c057cd250b11755`, current main: `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846` (README-only post-pin change).

- Release pins and current-main snapshots are distinguished. No third-party runtime or skill files imported.

## 2026-11-03 — held-out benchmark split enforcement

| Task | Status | Evidence / remaining acceptance |
|---|---|---|
| IPA-BENCH-SPLIT-001 | DONE_VERIFIED (engineering contract) | Export preserves the frozen group-safe split; scorer defaults to test and requires explicit selection for train/dev/all. Exact-head tests [41651876020](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41651876020) SUCCESS on `af3ff6c5d3104a45ce5c1524b6083850c6dacd83`. This fixes the evaluation boundary, not linguistic gold. |

Independent gold remains 0 and accuracy remains null. No data labels were fabricated. The split-aware benchmark documentation is in `docs/benchmarking-and-external-ipa.md`.

## Frozen split manifest provenance — 2026-11-03

The export and benchmark now preserve and validate the complete frozen split identity, not only the bucket name: `split`, `split_seed`, and `split_version`. Every adjudicated row must carry non-empty seed/version metadata, and the benchmark rejects a TSV that mixes manifest identities. The report exposes the manifest seed/version and selected scoring split. This makes the evaluated test partition traceable to one exact manifest; it does not create linguistic gold or change the current zero-row accuracy status.


## 2026-11-03 — empty benchmark prediction input

| Task | Status | Evidence / remaining acceptance |
|---|---|---|
| IPA-BENCH-EMPTY-PREDICTIONS-001 | DONE_VERIFIED (engineering guard) | Header-only prediction TSV previously exited 0 and produced an empty `engines` object. Test-first regression failed on all three language repositories; the scorer now rejects an empty prediction dataset after checking gold and frozen split provenance. Missing individual predictions within a named engine remain denominator-counted. RED: [41655173696](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41655173696). Final exact-head tests: [41655504734](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41655504734) SUCCESS. |


## 2026-11-03 — benchmark identifier validation

| Task | Status | Evidence / acceptance |
|---|---|---|
| IPA-BENCH-IDENTIFIERS-001 | DONE_VERIFIED (engineering guard) | Reject whitespace-only gold IDs, prediction IDs and engine names while preserving non-empty identifiers exactly. Test-first RED: gold-ID run 41660769932; prediction-ID/engine run 41662075069. Final exact-code-head CI: 41662232565 SUCCESS (152 Python tests + 54 subtests; 54 built-site browser tests passed).  No linguistic labels or accuracy claims were added. |

## Verified continuation checkpoint — 2026-11-03 (late session)

- Default branch base: `145a24af36767e14a9f094c243c593a1a6e40af5`; continuation branch: `docs/current-state-checkpoint-20261103`.
- Latest mainline work retained: mixed-script runtime parity fix and the latest handoff/register reconciliation.
- Exact-main CI on the recorded default-branch head: tests 41714204905; Pages deploy 41714204591; all listed runs completed with SUCCESS. These are CI checks for the current implementation and deployment, not phonetic validation.
- Open pull requests: none at checkpoint time. No upstream methodology repository was modified; Superpowers, Matt Pocock Skills and Ponytail remain process references only.
- Engineering task ledger: benchmark split provenance, empty-prediction rejection and whitespace-only identifier validation remain **DONE_VERIFIED** as input-integrity safeguards. The recently merged runtime fix is verified by its own regression/CI; no new linguistic rule is inferred from it.
- Linguistic task ledger: independent adjudicated IPA gold remains **0**; gold export remains header-only and empirical accuracy remains `null`. The profile-specific IPA convention, two independent annotators, separate adjudicator, curator/blind intake and item-level rights review remain **BLOCKED** on external human decisions/resources. No labels or source-derived pronunciations were fabricated.
- Manual deployed-site keyboard, screen-reader, responsive and mobile QA remains **TODO**; automated browser checks do not satisfy these acceptance criteria.
- Local test execution was not available in this connector-only session. Verification evidence is the linked GitHub Actions CI on the exact recorded main SHA; do not report local tests as run.


## Research unblock checkpoint — 2026-11-03

- Prospective language-specific expert/researcher leads and additional candidate resources are recorded in docs/ipa-gold-collection-playbook.md with primary-source links and explicit limits.
- These are leads only: no one has been contacted or recruited; no IPA convention has been approved; no rights have been granted; no IPA labels were generated.
- The 30-item pilot remains BLOCKED until the acceptance conditions in the playbook are met. Candidate lexicon entries, phonetic respellings, model outputs, orthographic transcripts and source descriptions are not gold IPA.
- The next external action is to contact a qualified prospective reviewer and request nominations for two independent annotators plus a separate adjudicator; separately complete item-level rights review and blind-intake dry run.


## Burmese Wiktionary rights-source separation — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-RIGHTS-001 | DONE_VERIFIED (source attribution separation); rights decision remains BLOCKED | PR #111 merged at `8c323ff0d1236c5c6d36b2c2be0eac4d493163ab`; dataset-card CC BY 4.0 declaration and Myanmar Wiktionary local CC BY-SA 3.0 Unported/GFDL policy are separate source records and documentary claims. Main tests [41798078257](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41798078257), optional Epitran [41798080052](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41798080052), and Pages [41798078321](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41798078321) SUCCESS. | Provenance is correctly separated. Dataset rights remain CONFLICT/UNKNOWN until publisher/rightsholder clarification. No IPA labels, dataset imports or accuracy claims. |


## Post-merge checkpoint — Burmese Wiktionary provenance handoff (2026-11-04)

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-RIGHTS-001 | DONE_VERIFIED (documentation reconciliation); rights remain BLOCKED | PR #112 merged as `f4764d124e73005dab57512c93fdd59938e60ec3`. PR-head tests [41799540057](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41799540057) SUCCESS; post-merge main tests [41799853697](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41799853697) and Pages [41799853678](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41799853678) SUCCESS. | Handoff and register now describe the split source records. Dataset rights remain CONFLICT/UNKNOWN; 113 IPA values (0.51%) are not gold. |


## Post-merge checkpoint — Burmese Wiktionary provenance (2026-11-04)

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-RIGHTS-001 | DONE_VERIFIED (source attribution separation and handoff reconciliation); dataset rights remain BLOCKED | PR #111 merged `8c323ff0d1236c5c6d36b2c2be0eac4d493163ab`; PR #112 merged `f4764d124e73005dab57512c93fdd59938e60ec3`; PR #113 merged `040b0ea8f565ca9e443d361d1aaa658af978e9f2`. Main tests [41798078257](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41798078257), optional Epitran [41798080052](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41798080052), Pages [41798078321](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41798078321), PR-head tests [41799540057](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41799540057), post-merge tests [41799853697](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41799853697) and Pages [41799853678](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41799853678), post-PR113 tests [41800359629](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41800359629) and Pages [41800359623](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41800359623) all SUCCESS. | Dataset-card CC BY 4.0 and upstream CC BY-SA 3.0 Unported/GFDL remain conflicting; 113 IPA values (0.51%) are not gold. Obtain written rights clarification and per-entry profile/provenance before any import. |


## Language-specific IPA test fixtures — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-IPA-GOLD-FIXTURE-001 | DONE_VERIFIED | PR [#115](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/115) merged as `28ac47949efb725610023a24b69df1c584d598a7`; exact-main tests [41847895975](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41847895975) and Pages/deployed-site smoke [41847895765](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41847895765) SUCCESS. | Test fixture now uses Myanmar script and neutral test profile; regression asserts the Myanmar Unicode-block and matching profile metadata. This validates test-fixture integrity only, not phonological rules or IPA accuracy. Gold remains 0; accuracy null. |


## Burmese external pronunciation source audit — legacy non-text records excluded

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-MYG2P-SOURCE-001 | DONE_VERIFIED (source pinned and provenance/rights documented; no import) | Upstream `ye-kyaw-thu/myG2P` revision `54b5c76bb5a87fdbaaeddc1892e6ebd8f97ee225`; Version 2.0 file `ver2/myg2p.ver2.0.txt`, 2,329,808 bytes, Git blob SHA `0b2735f9a6f7fe28ae94c4baaf323d1db3015c3b`, five tab-separated fields including IPA; CC BY-NC-SA 4.0. Registered as `MYG2P2026`. | External diagnostic/comparator only. Non-commercial/share-alike terms, per-entry provenance, dialect and IPA convention must be respected. Existing test-only probe does not become gold or production approval. |
| BURMESE-OPENSLR80-AUDIO-001 | DEFERRED / OUT OF SCOPE | Historical source metadata only; not part of current text-only work. | No recording acquisition, processing, annotation or audio-derived labels. Not a blocker for text-based research. |

**Evidence boundary:** source records and provenance tests are complete; no external dictionary or corpus rows were imported. Independent adjudicated Burmese IPA gold remains 0; accuracy remains null.


## IPA gold release-gate profile consistency — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| IPA-GOLD-RELEASE-PROFILE-001 | DONE_VERIFIED (engineering guard) | Shared `scripts/ipa_gold_corpus.py` now rejects adjudicated corpora that mix target-profile identity (`id`, `variety`, `region`, `register`) or IPA kinds. New regression tests cover both failures. PR #117 merged as `085ce5a2da4a07dfbf606a9892c78a4d3bbb9d91`; exact PR-head CI [41870132273](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41870132273) SUCCESS; post-merge CI [41870579420](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41870579420) SUCCESS; Pages [41870579398](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41870579398) SUCCESS. | Does not prove profile approval, annotator qualifications, blindness, linguistic contrast coverage, or IPA accuracy. A specialist-reviewed language-specific coverage report remains required before benchmark readiness. |


## Expert recruitment lead revalidation — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-IPA-GOLD-RECRUITMENT-LEADS-001 | PARTIAL | New specialist leads: Chiara Repetti-Ludlow's 2023 Burmese sonorant acoustic study and 2021 Burmese tone/sonority paper; Yuttaporn Naksuk and Tanintorn Limpasiri's comparative phonology review across eight Burmese dialects; University of Yangon referral lead. These do not establish native Yangon annotator qualification, availability or recruitment. | No candidate has been contacted, consented, recruited or approved. Close only after two independent qualified target-variety annotators, separate adjudicator, non-annotating curator, conflict checks, secure blind intake and written role/terms confirmation are documented. |

## Deterministic rule engine — 2026-11-11

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-DETERMINISTIC-RULE-ENGINE-001 | DONE_VERIFIED (engineering); linguistic coverage PARTIAL | PR #128 merged as `cd3a1503e79d32b09a6d2d5206340a37cfd3283b`. Exact main tests [43018103155](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43018103155) and Pages + asset smoke [43018103391](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43018103391) SUCCESS; live site: https://clippyfirst.github.io/Burmese-Ukrainian-Phonetic-System-/. | Deterministic rule contract and publication verified. Expert-adjudicated Yangon IPA gold is still required before correctness/accuracy claims. |

## Final deterministic-engine verification — 2026-11-11

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-DETERMINISTIC-RULE-ENGINE-001 | DONE_VERIFIED (engineering); linguistic coverage PARTIAL | Final main head `9bece0a50a367f3f58336d2aba7016ac4af86156`; exact-head tests [43019216137](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43019216137) and Pages + smoke [43019216297](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43019216297) SUCCESS. | Deterministic implementation and publication verified. Independent expert-adjudicated Yangon IPA gold remains necessary for broader correctness/accuracy claims. |


## 2026-11-11 — Ukrainian practical transcription continuation

| Work item | Status | Evidence / acceptance |
|---|---|---|
| Python IPA → Ukrainian adapter integrated after deterministic Burmese IPA | DONE_VERIFIED | Previous code revision `530cefbfc874b777650bd7e7ccdb5888534ab348`; 180 Python tests + 66 subtests |
| Canonical CSV and generated browser adapter | DONE_VERIFIED | Generated-data freshness, build and Node tests passed on previous code revision |
| Target distinctions /h, ɦ/ → г, /ɡ/ → ґ, /x/ → х; /w/ → в, contextual /j/ yotation, affricates ц/дз/ч/дж | DONE_VERIFIED | Explicit project policy; official 2026 standard generally uses г for foreign [g], so ґ is a contrast-preserving project choice |
| Browser fail-closed behavior for kinzi, medials and conjuncts | PARTIAL | Implemented; final Playwright run is queued and unverified |
| Accuracy of proposed Ukrainian correspondences | PARTIAL | No independent adjudicated IPA/Ukrainian gold set |
| Final browser CI | BLOCKED | Run 43095578672 queued with zero jobs started |
| Independent text-only IPA gold set | BLOCKED | Requires sourced and adjudicated Yangon-profile IPA labels and held-out evaluation |
| Audio | DEFERRED | Outside current task scope |


## Provisional onset IPA fallback — 2026-11-11

| Work item | Status | Evidence / acceptance |
|---|---|---|
| Python onset-only preview for unresolved Burmese syllables | PARTIAL | Separate provisional IPA/Ukrainian fields and trace; canonical ipa/ukrainian withheld; unresolved rime marked ?. Regression added. Commit 6936f01d3ff320574b8802c7af348d687e63ce17 |
| Browser onset-only preview | PARTIAL | Reuses Yangon onset IPA and IPA adapter; displays provisional IPA and ?. Commit 5b83f5d3674b9e6d2f4114047bd67be5a5440719 |
| Browser regression | PARTIAL | Source-contract assertions added; no executed cross-runtime parity fixture yet. Commit 36b6ebf5a1d5a03b0c4d7a95aae2d842046e4152 |
| Dedicated Yangon grapheme-position evidence registry | TODO | Register primary-source locator, profile, exact onset position, rule ID, scope and reviewer status for every fallback entry |
| Exact-head CI and Chromium verification | BLOCKED pending run | No workflow run was returned for final head 36b6ebf5a1d5a03b0c4d7a95aae2d842046e4152 |
| Vowel/coda/asat/medial/kinzi/conjunct fallback | TODO | Do not extend without source-backed positional rules; no such guesses were added |


## Verification result — provisional onset preview, 2026-11-11

| Work item | Status | Evidence |
|---|---|---|
| Python fallback implementation and regression | DONE_VERIFIED (engineering behavior) | Code/test head aac1d6834b4c29e04f01477af1583a2be9eba485; workflow 43101914347 PASS: 182 tests + 66 subtests |
| Browser fallback detail and canonical fail-closed behavior | DONE_VERIFIED (engineering behavior) | Workflow 43101914347 PASS; Playwright 54/54; production build, generated-data freshness and Node tests PASS |
| Optional Epitran raw-output comparator | DONE_VERIFIED (workflow) | Run 43101914423 PASS; not an independent IPA accuracy benchmark |
| Dedicated Yangon grapheme-position evidence registry | TODO | Existing onset inventory is reused; exact per-entry primary-source locators, scope and adjudication remain required |
| Functional Python/browser parity fixture | TODO | Browser tests cover behavior, but no shared structured cross-runtime fixture yet |
| Full Myanmar grapheme fallback | DEFERRED / evidence-limited | Only isolated bare consonants receive onset-only preview; vowel/rime/coda/asat/medial/kinzi/conjunct/tone structures remain fail-closed |


## Unicode grapheme accounting sweep — 2026-11-12

| Work item | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-UNICODE-ACCOUNTING-001 | DONE_VERIFIED (structural/input accounting) | PR #134 merged as `374e1a883ffc2aea5c729377e5aabf22778cbffd`; exact-head tests [43184645239](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43184645239) SUCCESS. Exhaustive sweep covers assigned Unicode L/M code points in all four Myanmar blocks. | Lossless source and code-point trace only; no IPA value is inferred for out-of-profile characters. |
| BURMESE-PHONOLOGY-100-001 | PARTIAL / BLOCKED by evidence | Existing parser/IPA engine withholds unsupported structures; no independent Yangon-profile adjudicated gold. | Requires source-located positional evidence for each supported context, shared Python/browser fixtures, independent adjudication and held-out evaluation. |


## Burmese provisional onset registry reconciliation — 2026-11-12

| Work item | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-ONSET-HINT-REGISTRY-001 | DONE_VERIFIED (candidate registry parity) | PR #136 merged as `9931acf8c4b8b9a16d210e44eca47f1319f04be2`; exact-head workflow [43185426033](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43185426033) SUCCESS. Python provisional table now includes the existing CSV/browser candidate for U+1009 `ဉ` /ɲ/. | Provisional onset preview only. Canonical IPA remains withheld for isolated bare consonants; no gold label or accuracy claim added. |
| BURMESE-ONSET-IPA-PARITY-001 | PARTIAL / EVIDENCE-LIMITED | Existing `ရ` candidate differs: CSV/browser `r`, Python `ɹ`; both analysis-dependent. | Requires source-located Yangon-profile evidence and explicit broad/narrow IPA convention before choosing or synchronizing a value. |


## MLCTS Latin → Ukrainian target matrix — 2026-11-12

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-ROM-UA-TARGET-001 | DONE_VERIFIED | Branch `feat/burmese-romanization-ukrainian-matrix-completion-2026-11-12`; exact-head test run [43221074232](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43221074232) SUCCESS: 187 Python tests + 66 subtests, 54 Node tests, build, generated-data freshness and built-site Playwright all passed. All 35 onset and 94 vendor-rime rows have target candidates. | Table coverage verified; project orthographic rendering only, not IPA or primary-source verification of vendor rimes. Runtime adapter and full source inventory remain open. |
| MYA-ROM-UA-001 | PARTIAL | PR #141 integrates a separate MLCTS → Ukrainian runtime adapter and UI; exact-head and mainline tests pass. | Expand source-verified structures and preserve unsupported/ambiguous sequences without IPA fallback. |


## Burmese Ukrainian target matrix — post-merge evidence — 2026-11-12

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-ROM-UA-TARGET-001 | DONE_VERIFIED | Merged PR [#138](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/138), merge `1d7045d9695d571017633a2e294b718a13ee5bce`; mainline tests [43221871111](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43221871111) and Pages [43221870932](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43221870932) SUCCESS. | 35 onset + 94 vendor-rime target rows are covered. Vendor-source evidence remains EVIDENCE_LIMITED; runtime adapter and complete source inventory remain open. |


## Burmese MLCTS Ukrainian runtime adapter — 2026-11-12

| ID | Status | Evidence | Remaining acceptance |
|---|---|---|---|
| MYA-ROM-UA-TARGET-001 | DONE_VERIFIED | All 35 onset + 94 vendor-rime target rows populated; merged PR #138; matrix CI passed. | None for existing inventory rows. |
| MYA-ROM-UA-001 | PARTIAL | PR #141 adds `src/web/romanization-ukrainian.js`, syllable-level longest-match onset/medial/rime mapping, separate UI output, and tests for all 94 rime rows and all onset rows. Exact-head tests [43226578745](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43226578745) and push [43226566617](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43226566617) SUCCESS: 187 Python tests + 66 subtests, 18 Node tests, 55 Playwright tests, build and generated-data freshness. | Expand source inventory and support/adjudicate remaining medial/devoicing/kinzi/asat/independent-vowel combinations; preserve unknown sequences as explicit unsupported rather than guessing. |
| MYA-ROM-MATRIX-001 | PARTIAL | Runtime adapter covers current 94 vendor-derived rime keys plus supported onset and `y/r/w` medial sequences. | Verify complete orthographic inventory against original MLC source; include all legal Burmese sequences, numerals and punctuation. |
| MYA-ROM-LIC-001 | PARTIAL | Mya2Rom 0.4.4 attribution and CC-BY-SA-4.0 notice retained. | Audit each vendored table/data component and upstream licensing/provenance. |

All target renderings remain `PROPOSED`; vendor-derived source rime provenance remains `EVIDENCE_LIMITED`. This is orthographic MLCTS rendering, not IPA or pronunciation transcription.



Latest final exact-head verification after adding explicit withholding for Myanmar code points outside the romanization support inventory: [tests 43227199213](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43227199213) SUCCESS on `4a2cb24ae9af2bc5e4d9341de65d0a55e07b6e09`: 187 Python tests + 66 subtests, 19 Node tests, 55 Playwright browser tests, production build and generated-data freshness. Unsupported Myanmar code points are now explicitly bracketed in the Ukrainian romanization output.


## MLCTS Ukrainian runtime adapter — mainline post-merge verification — 2026-11-12

- PR [#141](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/141) merged as `3fa33864b774c716da5bf6c9778a963148fb9974`.
- Mainline tests [43227806284](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43227806284) and Pages deployment [43227806266](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43227806266) both SUCCESS.
- Mainline test evidence: 187 Python tests + 66 subtests, 19 Node tests, 55 Playwright browser tests, production build and generated-data freshness all passed.
- Acceptance remains PARTIAL: current Mya2Rom-derived rime inventory is EVIDENCE_LIMITED, and unrepresented legal syllable structures remain visibly unsupported rather than guessed.


## MLCTS runtime mainline reconciliation — 2026-11-12

| ID | Status | Current evidence | Acceptance boundary |
|---|---|---|---|
| MYA-ROM-UA-TARGET-001 | DONE_VERIFIED | 35 onset + 94 vendor-derived rime target rows populated; PR #138 merged; current-main tests [43228612973](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43228612973) and Pages [43228612998](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43228612998) SUCCESS. | Completeness of inventoried table only; vendor-rime source provenance remains EVIDENCE_LIMITED. |
| MYA-ROM-UA-001 | PARTIAL | PR #141 merged as `3fa33864b774c716da5bf6c9778a963148fb9974`; separate runtime adapter/UI executes supported onset, medial and rime mappings; unknown material remains visibly unsupported. | Full source-verified MLCTS inventory and all legal Burmese syllable structures. |
| MYA-ROM-MATRIX-001 | PARTIAL | Runtime supports the existing 94 rime rows with supported onset and y/r/w medial sequences. | Primary MLC source verification; legal medial/devoicing/kinzi/asat/independent-vowel combinations; numerals and punctuation source handling. |
| MYA-ROM-LIC-001 | PARTIAL | Mya2Rom attribution and CC-BY-SA-4.0 notice retained. | Component-by-component audit of vendored code, table data and upstream-derived sources/rights. |

No MLCTS output was promoted to IPA or pronunciation evidence. Independent expert-adjudicated IPA gold remains 0 and empirical accuracy remains null.


## Burmese medials, G2P and coda-parsing update — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-MEDIAL-INVENTORY-001 | DONE_VERIFIED (orthographic inventory) | Unicode 18, WG2 N2827 and Hlaing (2014) support four basic signs plus seven two-/three-medial codepoint combinations. The thesis has a duplicated prose label in the final RA+WA+HA row; codepoints are unambiguous. | This does not assign IPA values to all combinations. |
| MYA-MEDIAL-PHONOLOGY-001 | PARTIAL / CONTEXT_DEPENDENT | Ishida 2026 and pinned Google Thrax: YA/RA typically /j/ with onset-specific exceptions; WA /w/ vs rime /ʊ/; HA aspiration/devoicing and fused outcomes. Watkins (2001) and Green (2002) support secondary articulation /mj/ analysis. | Complete onset × medial × rime × coda × tone matrix and independent Yangon adjudication. |
| MYA-MRAN-IPA-001 | PARTIAL / CROSS-SOURCE CANDIDATE | Wiktionary /mjàɴ/; Green /mj/ plus placeless nasal /N/; Google WFST raw output m j àɴ. Epitran 1.35.3 instead returns məjaɴ. Both external outputs have zero gold and null accuracy. | Independent text-based expert review against written lexical and phonological sources; settle phonemic /N/ vs surface nasalization and schwa disagreement. |
| MYA-ASAT-CODA-001 | DONE_VERIFIED (structural parser parity) | Python now attaches base consonant + U+103A as coda within preceding syllable, matching browser. Regression cases: မြန်, မြန်မာ, ကတ်. Exact-head tests [43325991671](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43325991671) SUCCESS. | Broader segmentation remains partial pending independent annotated boundary corpus. |
| MYA-GOOGLE-FST-001 | DONE_VERIFIED (source/license and raw diagnostic) | Pinned grammar commit a90601024f07ab7e96c911243324e0adeb16da96 and root LICENSE declare Apache-2.0; raw probe run 43084508359 returned m j àɴ for မြန်, no gold. | Optional comparator only; do not replace deterministic engine or treat output as gold. |
| MYA-CRF-DIAG-001 | PARTIAL / DIAGNOSTIC ONLY | Exact branch run [43325991496](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43325991496): 84/100 source-concordant; YA 10/14, RA 17/20, WA 13/15, HA 7/8; zero gold and accuracy null; exact မြန် absent. | Train/test overlap unknown; labels are from myG2P CC BY-NC-SA 4.0. |
| MYA-TONE-001 | PARTIAL / COMPETING ANALYSES | Green and LREC 2020 use four-tone descriptions; Duan & Zhu (2025) propose eight tones across modal/lower-breathy registers. | Full empirical review, profile scope and expert-approved convention. |
| MYA-IPA-GOLD-001 | BLOCKED | No independent expert-adjudicated Burmese IPA gold for these medial/coda cells. | Two independent qualified reviewers, third adjudicator, source-located written dictionary/grammar examples, documented broad-vs-narrow IPA convention and frozen held-out text fixtures. No audio is required or in scope. |
| MYA-PR129-RECONCILIATION-001 | LEFT OPEN / NOT MERGED | Draft PR #129 is 53 commits ahead / 17 behind current main and non-mergeable; its research findings were reused, broad hybrid implementation left untouched. | Rebase/reconcile only as a separate, reviewed integration task. |

The project remains PARTIAL PROTOTYPE; empirical accuracy remains null.


## IPA nasalization metadata boundary — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-IPA-NASALIZATION-SCHEMA-001 | DEFERRED | The typed IPA schema preserves literal IPA, kind, boundaries, tone, length and phonation but has no dedicated nasalization property. Literal IPA can preserve the diacritic. | Decide after expert-approved phonemic /N/ vs surface nasalization convention; only then consider a backward-compatible optional schema field. No schema change in this research pass. |


## UCSY-SC1 historical metadata — excluded from active text-only scope (2026-11-13)

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-UCSY-SC1-AUDIO-001 | DEFERRED / OUT OF SCOPE | Rights conflict and corpus metadata retained for historical audit only. | No acquisition, processing, annotation or audio-derived IPA labels; not a blocker for text-only research. |


## Romanization/G2P mode separation — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-ROMANIZATION-SEPARATION-001 | DONE_VERIFIED (runtime contract) | Mya2Rom 0.4.4 defines MLCTS as orthographic and MLCTS2 as a more phonetic romanization; the browser adapter explicitly calls mya2rom(..., "mlcts", ...). | Preserve the Latin→Ukrainian crosswalk as orthographic transliteration. Do not treat MLCTS2 or the crosswalk as IPA/G2P gold. |


## Text-only source and historical-phonology updates — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-MYX-MYANGLISH-001 | PARTIAL / SCHEMA + QUALITY | 2,121 text pairs; raw CSV has two columns, while README dataset_info and viewer show a third official_standard field; non-standard single-author-style romanization. Project owner confirms research-use permission. | Obtain pinned raw artifact and generated Parquet, reconcile schema; use only as an informal romanization diagnostic, not IPA gold. |
| MYA-MYX-ORTHO-001 | PARTIAL / QUARANTINED_FOR_QUALITY_REVIEW | 4,800 work-in-progress noisy-to-clean text rows; sampled target_words mismatch and multi-substitution examples; not IPA. Project owner confirms research-use permission. | Obtain pinned files; audit target spans, deduplicate templates and manually review; do not use as a clean benchmark or IPA gold yet. |
| MYA-OKELL-TEXT-001 | BLOCKED / TOOL ACCESS | 8.8 MB Unicode text corpus; project owner confirms research-use and ingestion permission; current execution environment could not retrieve corpus bytes. | Obtain bytes through project-side transfer or accessible mirror, pin revision/hash, profile Unicode, duplicates and text boundaries. |
| MYA-STEDT-HISTORICAL-MEDIAL-001 | PARTIAL / HISTORICAL-SOURCE-SPECIFIC | STEDT, Nishi (1997/1998 Old Burmese) and Matisoff distinguish OWB/MWB/EModWB, historical -l/-r/-y correspondences, and dialect reflexes. Nishi 1976 itself remains unread. | Reconcile primary Nishi 1976 text and inscriptional examples with modern Yangon evidence; no direct Unicode runtime mapping. |
| MYA-NISHI98-VOICING-001 | DONE_VERIFIED (SOURCE EVIDENCE ONLY) | Full Nishi 1998 text inspected; two patterns, optionality, exceptions and dialect variation recorded; seven source-phonemic examples in sandhi_evidence.csv; tests and exact-head CI pass. | Runtime remains withheld until profile, lexical/context conditions and independent modern Yangon evidence are established. |

Independent text-adjudicated IPA gold remains 0; empirical accuracy remains null. Audio-related records are historical exclusions, not active work items.

| MYA-HILL-2019-CH2-001 | BLOCKED / TOOL ACCESS | Cambridge confirms Hill (2019), chapter 2 Burmese, pp.46-83; accessible publisher excerpt covers the introduction and Tibetan, not the Burmese chapter. Project owner confirms permission. | Obtain full chapter bytes in an accessible environment, inspect medials and written-to-spoken developments, then register exact locators. |

| MYA-GREEN2005-PHONOLOGY-001 | DONE_VERIFIED (SOURCE EVIDENCE ONLY) | Green 2005 broad IPA-style spoken transcription, separate ALA-LC written transliteration, CG onset structure and /N/ nasalization registered with tests. | Select project broad/narrow convention and adjudicate modern written examples; no direct Unicode medial rule yet. |
| MYA-SEALANG-DICT-001 | BLOCKED / ACCESS + SCHEMA | ~35,000-entry MLC-based dictionary; IPA query/display is confirmed at interface level by SHACHI and SEAlang 2008; Mya2Rom separately documents MLCTS2 use; internal record representation remains unknown. Project owner confirms permission. | Retrieve actual entries/export schema and reconcile interface IPA with stored MLCTS2; no IPA gold until inspected. |
| MYA-SEALANG-TEXT-001 | BLOCKED / TOOL ACCESS + SCHEMA | Text and bitext corpora are documented; service counts are not dataset sizes; project owner confirms research-use and ingestion permission, but stable retrieval is unavailable. | Retrieve actual records, inspect query/export schema, pin revision and verify provenance before import. |



## New verified text-evidence tasks — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-NISHI-OLDBURMESE-MEDIALS-001 | DONE_VERIFIED (HISTORICAL EVIDENCE) | Full Nishi 1998 Old Burmese article inspected; 13 new source-linked medial/dialect rows, four claims and four historical rules; tests pass. | Keep historical -h/-l/-r/-y distinctions separate from modern Unicode; all rows WITHHELD. |
| MYA-NISHI-SANDHI-EXAMPLES-001 | DONE_VERIFIED (SOURCE PHONEMIC, NOT IPA) | Seven source-faithful examples from Nishi 1998; explicit transcription-convention note; empty IPA field; tests pass. | Do not promote source phonemic strings to IPA gold or runtime outputs. |
| MYA-MYX-DATA-QUALITY-001 | DONE_VERIFIED (SAMPLED AUDIT) | Myanglish raw/metadata schema mismatch and orthography target_words/multi-substitution issues documented. | Full pinned artifacts still needed for complete row-level audit; corpora remain separate from IPA gold. |
| MYA-TEXT-RESEARCH-AUTHORIZATION-001 | DONE_VERIFIED (PROJECT OWNER CONFIRMATION) | Project owner confirms required permissions for text-only research use and project ingestion. | Preserve source attribution/provenance; no audio work is in scope. |

Exact-head CI 43393402710 on 4835a0abc3e7e4a18c9d0bda35f554031912d570: 217 Python tests + 66 subtests, 20 Node tests, 58 Playwright/Chromium tests; IPA-gold structure validation, build and generated-data freshness all passed. Independent expert-adjudicated IPA gold remains 0; empirical accuracy remains null.

## Final verification snapshot — 2026-11-13

- Exact tested head c03706474cf67b480c449790c9592e5fe0e53fd4; CI 43394274053 SUCCESS: 217 Python + 66 subtests, 20 Node, 58 Playwright, IPA schema, build and generated-data freshness.
- Diagnostics CI 43394274111 SUCCESS: CRF 100/100 outputs, 84 source-concordant, zero gold and null accuracy; Epitran raw output only.
- Registry counts: 56 sources, 71 claims, 42 medial rows, 28 rules, 7 source-phonemic sandhi examples. CSV integrity and traceability passed.
- Nishi (1976) is registered but full text remains unread; Nishi (1998) Old Burmese is a separate inspected source.
- Project owner confirms text-only research and project-ingestion permissions. No audio work.
- Okell/SEAlang/Hill remain tool-access or schema blocked; Myanglish schema is uncertain; myX orthography remains quarantined for quality.
- Independent IPA gold remains 0; accuracy null; runtime rules withheld. Status PARTIAL PROTOTYPE.


| MYA-OKELL1995-DIALECT-MEDIALS-001 | DONE_VERIFIED (SOURCE EVIDENCE ONLY) | Full Okell (1995) text inspected; WB/SB distinction, AR r/y preservation, IT/TV medial /l/, phonemic transcription convention; seven claims, two dialect rules, three matrix rows and regression tests. | All regional rows WITHHELD; do not project onto current Yangon without direct profile-specific evidence. |
| MYA-STANDARD-YANGON-PROFILE-001 | PARTIAL / EVIDENCE-LIMITED | Okell, Nishi and Green provide useful standard/regional/historical contrasts, but no complete current Yangon source-located written fixture set has been independently adjudicated. | Build a modern Yangon profile from text-only authoritative dictionaries/grammars; keep dialectal and historical correspondences separate. |


| MYA-OKELL1969-COLLOQUIAL-GRAMMAR-001 | BLOCKED / TOOL ACCESS | Two-volume reference grammar is bibliographically confirmed; Nishi 1998 cites §§17-20 for voicing sandhi; Okell 1995 identifies it as the Spoken Burmese reference. Project owner confirms permission. | Obtain full text, inspect exact phonology/sandhi sections and register page-located claims before runtime decisions. |


## Consolidated verification snapshot — 2026-11-13

- Exact tested head 2a96f4121a43f704a8f0d2eb6d81cb343fba47db; CI 43395906072 SUCCESS: 219 Python + 66 subtests, 20 Node, 58 Playwright, IPA schema, build and generated-data freshness.
- Optional diagnostics 43395906100 SUCCESS; CRF 100 predictions / 84 source-concordant / 0 gold / null accuracy; Epitran raw output only.
- Final registries: 58 sources, 78 claims, 45 medial rows, 30 rules, 7 source-phonemic sandhi rows. CSV widths, unique IDs and source/claim/rule/matrix links validated.
- Okell (1995) regional medial profiles and Nishi (1998) historical medial evidence are DONE_VERIFIED as source evidence only; runtime remains withheld.
- Okell (1969), Nishi (1976), Hill (2019) chapter 2, Okell text corpus and SEAlang records remain retrieval/schema blocked, not permission blocked.
- Myanglish remains schema-uncertain; myX orthography remains quarantined for quality review. No audio.
- IPA gold=0; accuracy=null; classification PARTIAL PROTOTYPE.


| MYA-SEALANG-IPA-INTERFACE-001 | DONE_VERIFIED (INTERFACE ONLY) | SHACHI metadata and the 2008 SEAlang project paper confirm IPA phonetic query and IPA transliteration display; actual internal record fields remain undisclosed. | Keep separate from internal storage/MLCTS2 question; inspect actual entry/export schema before gold-corpus use. |


## Final evidence and verification — 2026-11-13

- Exact tested code/data head cda73ccb7fa80a0404fed5a65588ebd690253f94; CI 43397172081 SUCCESS: 220 Python + 66 subtests, 20 Node, 58 Playwright, IPA schema, build and generated-data freshness.
- Optional diagnostics 43397181331 SUCCESS: CRF 100 predictions, 84 source-concordant, 0 gold, null accuracy; Epitran raw output only.
- Registries: 59 sources, 83 claims, 45 medial rows, 30 rules, 7 source-phonemic sandhi rows, 9 Okell orthographic-profile rows. CSV widths, unique IDs and cross-registry references validated.
- Okell (1995) and Nishi (1998) full-text evidence is DONE_VERIFIED at source-evidence level only; all historical/regional rules remain withheld.
- SEAlang IPA query/display is DONE_VERIFIED at interface level; internal entry/export representation remains PARTIAL / SCHEMA UNRESOLVED because Mya2Rom separately documents MLCTS2.
- Okell (1969), Nishi (1976), Hill (2019) chapter 2, Okell text corpus and SEAlang records remain tool-access/schema blocked, not permission blocked.
- Myanglish remains schema-uncertain; myX orthography remains quarantined for quality review. No audio.
- IPA gold=0; accuracy=null; classification PARTIAL PROTOTYPE.


## Okell corpus access status correction — 2026-11-13

| Work item | Status | Evidence / acceptance boundary |
|---|---|---|
| Okell *A Corpus of Modern Burmese* text access | PARTIAL / CONTENT AND BYTE INTEGRITY VERIFIED | Zenodo direct endpoint HTTP 200, text/plain UTF-8; 8,809,265 bytes; provider MD5 matched; SHA-256 6bbafd699c587876317f6e0535b9dd8f9ec87c15efe4b7e65a8c7362ebcdbf4c; 19,565 CRLF-terminated lines (19,566 split segments including the final empty segment), 67 numbered heading lines, modern Myanmar Unicode, mixed Burmese/English, dialogue/speech transcripts and prose. |
| Corpus text quality and provenance | PARTIAL / TEXT_QUALITY_AUDIT_PENDING | Byte identity verified (MD5 matched; SHA-256 recorded); 21 BOM markers, one NUL, non-NFC text, repeated-line/paragraph counts profiled. Remaining acceptance: map embedded boundaries, document segment provenance, classify repeats, inspect corrupted technical terms and preserve exact source. |
| Corpus as pronunciation gold | DEFERRED / NOT GOLD | No IPA annotation schema or independent IPA labels identified; no G2P scoring. |

Acceptance: retain byte-identical pinned text, compute SHA-256, inspect document boundaries/duplicates/Unicode/corruption and record section locators before importing any lexical examples. No audio.


## Okell corpus structural-quality follow-up — 2026-11-13

| Work item | Status | Evidence / acceptance boundary |
|---|---|---|
| Exact retrieved-byte integrity | DONE_VERIFIED | Zenodo MD5 matched; SHA-256 6bbafd699c587876317f6e0535b9dd8f9ec87c15efe4b7e65a8c7362ebcdbf4c; 8,809,265 bytes; UTF-8 valid; 19,565 CRLF-terminated lines (19,566 split segments including the final empty segment). |
| Unicode/structure profile | PARTIAL | 21 BOM markers, one NUL at line 9,300, non-NFC text, 0 U+FFFD, 67 numbered heading lines, 73 unique Myanmar code points. |
| Duplicate/provenance audit | TODO | 295 repeated nonblank line forms / 1,008 excess occurrences and 23 repeated paragraph forms; determine source-level duplication vs recurring titles, headers and dividers. Map embedded boundaries and segment provenance. |

Do not normalize or deduplicate the archival source automatically. No audio.


## Okell corpus orthographic profile — 2026-11-13

Created `data/burmese/okell_text_corpus_orthographic_profile.csv` with four raw medial codepoint counts and five target substring counts. It is pinned to the verified source SHA-256 and explicitly classified ORTHOGRAPHIC_ONLY. Added claim `CLM-OKELL-TEXT-MEDIAL-FREQ-001` and a regression test. The profile does not assert tokenization, syllabification, pronunciation or IPA gold and does not change the runtime.


## Final exact-head continuation — 2026-11-13

- Branch head: `601cf85a5c740627848f9eff1fa1f0911cf03796`; base main: `dc90463bdd734867308f03cb627eb8941efc19d6`; main unchanged.
- PR #147: OPEN / DRAFT / mergeable, ahead / 0 behind (exact ahead count is maintained by PR #147), 29 files. PR #129: OPEN / DRAFT, untouched, 53 ahead / 17 behind, diverged/non-mergeable.
- Registry totals: 59 sources, 83 claims, 45 medial rows, 30 rules, 7 sandhi examples, 9 Okell orthographic profile rows.
- Okell corpus: 8,809,265 bytes; Zenodo MD5 matched; SHA-256 6bbafd699c587876317f6e0535b9dd8f9ec87c15efe4b7e65a8c7362ebcdbf4c; 21 BOM markers, one NUL, non-NFC, 67 numbered headings, repeated line/paragraph counts profiled. Remaining text-quality/provenance work is PARTIAL.
- Exact-head CI runs 43449980180 and 43449989336 SUCCESS: 222 Python + 66 subtests, 20 Node, 58 Playwright; build and generated freshness pass. IPA gold validator correctly reports zero adjudicated gold. Optional run 43449989348 SUCCESS; CRF remains unscored with zero gold and null accuracy; Epitran is raw-output-only.
- No audio, no runtime medial rules, no merge or release. Classification: PARTIAL PROTOTYPE, not release-ready.


## Full-text G2P and syllabification audit — 2026-11-13

| Work item | Status | Evidence / acceptance boundary |
|---|---|---|
| Thu et al. (2016) full-text benchmark audit | DONE_VERIFIED (methodology evidence) | 25,300 MLC dictionary words; 25,000 train, three 100-word open sets and 100-word closed set drawn from training. 2,393 graphemes, 1,864 pronunciations, 113 reported phonemes; romanized examples are not specified IPA. SCLITE phoneme-level Levenshtein PER on syllable-segmented words. Claims CLM-THU16-PER-001 and CLM-THU16-PHONESET-001. |
| Hlaing & Mikami (2014) orthographic FST paper | DONE_VERIFIED (structural evidence only) | New source HLAING_MIKAMI2014_FST; 11,732 MLC orthography words; 99.93% word-level orthographic segmentation, not G2P. Internal discrepancies: 32,238 vs 32,283 syllables; 8 vs 9 stacking errors. Claims CLM-HLAING14-ORTHOGRAPHIC-001 and CLM-HLAING14-METRIC-001. |
| Oo et al. (2020) text-side G2P full text | DONE_VERIFIED (architecture and source-specific phonology) | Thrax weighted FST graphemes→IPA; 34 consonants, 54 vowels; four-tone account; /N/ notation; Yangon recording location without explicit dialect label. Restricted web segmentation corpus and grammar-license uncertainty recorded. Claims CLM-OO20-TONE-001, CLM-OO20-NASAL-001, CLM-OO20-SEG-RESTRICTED-001, CLM-OO20-DIALECT-001. |
| Nishi (1998) Development of Voicing Rules PDF | DONE_VERIFIED | Full PDF retrieved and inspected; four new claims and corrected seven-row example/transcription provenance. No runtime rule activated. |
| Runtime promotion | DEFERRED / evidence gate | No new medials, tone, coda, /N/ or voicing rule activated. Independent expert-adjudicated IPA gold remains 0; empirical accuracy null. |

### Interpretation safeguards

- Thu et al.'s closed test overlaps training and cannot support independent accuracy claims.
- Thu et al.'s romanized phone strings are not project IPA.
- Hlaing & Mikami's 99.93% is orthographic word segmentation only.
- Oo et al.'s four-tone account is one source-specific model, not resolution of the four-vs-eight/register question.
- The phrase "open-source" in Oo et al. does not establish a separate license for the G2P grammar files.
- No audio was used.


## Nishi (1998) voicing paper — full text verified — 2026-11-13

| Work item | Status | Evidence / acceptance boundary |
|---|---|---|
| Nishi (1998), The Development of Voicing Rules in Standard Burmese | DONE_VERIFIED (full-text source evidence) | Full PDF from National Museum of Ethnology repository, DOI 10.15021/00004129, pp.253–260. Two synchronic sandhi patterns, four-stage historical account, optionality, exceptions and dialect comparison. |
| Example/transcription provenance reconciliation | DONE_VERIFIED | Nishi's notation follows Okell (1995), but footnote 3 says all examples are quoted from Okell (1969), §§17–20. Seven sandhi rows now record both layers; IPA values remain empty. |
| Atonicization versus voicing | DONE_VERIFIED (source claim) | Nishi says atonicization is unpredictable and sometimes optional and should not be stated with voicing sandhi. Preserve separate operations/conditions. |
| Runtime voicing promotion | DEFERRED / evidence gate | First pattern explicitly non-obligatory with variables/exceptions; Standard Burmese is heterogeneous; no independent modern Yangon adjudicated gold. |
| Nishi (1976/1977) Medials in Burmese full text | BLOCKED / source file not located | Bibliographic metadata and secondary citations found, but no complete primary text retrieved. Acceptance: inspect all pages, establish original edition/page numbering, and record direct evidence before updating medial rules. |
| Okell (1969) §§17–20 full text | BLOCKED / paywalled or preview-limited | Full book metadata and Google Books/National Library catalogue records found; no accessible complete text verified. Acceptance: inspect the actual cited sections and compare every sandhi example and exception directly. |

Four claims added: CLM-NISHI98-EXAMPLE-PROVENANCE-001, CLM-NISHI98-ATONICIZATION-001, CLM-NISHI98-DIALECT-PATTERNS-001, CLM-NISHI98-EXCEPTIONS-001. Registry totals: 60 sources, 96 claims; 30 phonological rules, 45 medial evidence rows, 7 source-phonemic sandhi examples and 9 orthographic-only Okell profile rows.

## Nishi (1997) orthographic-standardization paper — full text verified — 2026-11-13

Status: DONE_VERIFIED as historical orthographic evidence. Full PDF inspected (BNME 22(4), pp.975–999; DOI 10.15021/00004135). It distinguishes OWB, MWB, EModWB and ModWB; reports OWB -l replacement by -r/-v by initial class and later -y insertion after velars before written -i. It explicitly distinguishes written High and spoken Low varieties. The article focuses on rhyme systems and discusses initials only when necessary; it is not a comprehensive medial inventory or modern Unicode-to-IPA source. Added CLM-NISHI97-SCOPE-001. No runtime mapping activated.


## Duan & Zhu (2025) Burmese tone study — full-text audit — 2026-11-13

| Work item | Status | Evidence / acceptance boundary |
|---|---|---|
| Duan & Zhu (2025), *Double registers and eight tones in Burmese* | DONE_VERIFIED (FULL-TEXT SOURCE EVIDENCE ONLY) | Full 44-page article inspected from the Academia Sinica journal download page; *Language and Linguistics* 26(3), pp.387–430; CC BY 4.0. The authors propose four traditional tone classes split into eight yin/yang categories (1a–4a, 1b–4b), with modal and lower/breathy registers and pitch, phonation/register and length as dimensions. |
| Empirical sample and dialect scope | DONE_VERIFIED (SOURCE SAMPLE DESCRIPTION) | §1.2 p.392: five speakers aged 22–38, two from Yangon, two from Taunggyi and one from the Mandalay region; 89 words (80 monosyllabic, 9 disyllabic), each read twice; 694 valid word tokens. This is a mixed regional sample, not a Yangon-only sample. |
| Individual variation | DONE_VERIFIED (SOURCE EVIDENCE) | §5.3 Figure 7 and discussion report speaker variation, particularly in T1 and T3; preserve within-source variability rather than forcing one invariant pitch contour. |
| Runtime promotion / four-vs-eight reconciliation | PARTIAL / COMPETING ANALYSES | The paper advances an eight-category compound tone analysis, while Green and Oo et al. (2020) describe four categories. The new paper is a significant peer-reviewed competing analysis, not by itself a project-wide adjudication. No runtime tone model changed. |

Claims added: CLM-DUAN25-MODEL-001, CLM-DUAN25-SAMPLE-001, CLM-DUAN25-VARIATION-001. Existing DUAN2025 source record updated from abstract-only to full-text inspected. Review was text-only: no source recordings were accessed or analyzed. Independent project IPA gold remains 0; empirical G2P accuracy remains null.


## Okell (1999) Myanmar final and syllable-boundary proposal — full-text audit — 2026-11-13

| Work item | Status | Evidence / acceptance boundary |
|---|---|---|
| ISO/IEC WG2 N2033, *Proposal for Extension of Myanmar Coded Set* | DONE_VERIFIED (FULL-TEXT ORTHOGRAPHIC EVIDENCE) | Full 18-page document inspected. Appendix 2 contains John Okell's 1999-05-11 research/chart of vowel-sign, tone-mark and final combinations. It separates the regular Burmese open/closed syllable system from added finals used for non-Burmese words and names. |
| Added finals and syllable-boundary method | DONE_VERIFIED (SOURCE EVIDENCE ONLY) | Okell reports that added finals may follow regular finals and tone marks, occasionally with two or three finals; enumerating possible syllable endings is insufficient for boundary detection, and he suggests identifying the beginnings of new syllables. This is a text-processing proposal, not a ready-made phonological syllabifier. |
| Open/closed syllable tone encoding | DONE_VERIFIED (ORTHOGRAPHIC EVIDENCE ONLY) | §§3–5 distinguish tone-mark arrangements in open and closed syllables; absence of an explicit mark has different interpretations in the two structures. This does not resolve the modern four-vs-eight tone analysis. |
| 94 MLCTS rime vendor audit | PARTIAL / PRIMARY-SOURCE EVIDENCE GATE | 94/94 non-empty source keys and MLCTS column values now match vendored Mya2Rom 0.4.4; 25 two-key collision groups are registered. This verifies vendor transcription fidelity, not the primary MLC table. Keep all Ukrainian candidates PROPOSED/EVIDENCE_LIMITED; complete primary-source and word-level adjudication before promotion. |

Claims added: CLM-OKELL99-ADDED-FINALS-001, CLM-OKELL99-SYLLABLE-BOUNDARY-001 and CLM-OKELL99-OPEN-CLOSED-TONE-ORTHOGRAPHY-001. Added regression coverage in `tests/test_source_rule_evidence.py`. Review used document text only; no audio.

Current registry totals after this update: **61 sources, 102 claims**, 30 phonological rules, 45 medial evidence rows, 7 source-phonemic sandhi examples and 9 Okell orthographic-profile rows. CSV validation and CI for this exact head are pending.


## Hill (2019) Burmese historical-phonology chapter — full-text access correction — 2026-11-13

| Work item | Status | Evidence / acceptance boundary |
|---|---|---|
| Hill (2019), Chapter 2: Burmese, pp.46–83 | DONE_VERIFIED (SECONDARY HISTORICAL ANALYSIS) | Full chapter text inspected from a third-party mirror; title, DOI, chapter pagination and bibliographic identity checked against Cambridge metadata. The mirror is not the publisher source; publisher copyright notice retained, no redistribution. |
| Old Burmese medials and Written Burmese scope | DONE_VERIFIED (SECONDARY SOURCE EVIDENCE) | §46: Old Burmese y-, r-, l-; -w- is derived from -o1- > -wa- and excluded from the historical medial inventory; limited double-medial evidence is noted but excluded from the figure. §47: Written Burmese is an idealized standard, not tied to one specific time/place; historical -l- merges with -y- after velars and -r- after labials. |
| Old Burmese tone notation | DONE_VERIFIED (SOURCE-SPECIFIC RECONSTRUCTION) | §46: Old Burmese does not regularly mark tones; Hill projects Written Burmese tone marking backwards for reconstruction. Do not mistake this analytical choice for regular attested Old Burmese tone marking. |
| Runtime promotion | DEFERRED / HISTORICAL ONLY | Use Hill to triangulate Nishi and other historical sources; no modern Unicode mapping or Yangon G2P rule is licensed. Nishi (1976) itself remains unread as a primary source. |

Claims added: CLM-HILL2019-OB-MEDIALS-001, CLM-HILL2019-WB-SCOPE-001, CLM-HILL2019-OB-TONE-001 and CLM-HILL2019-OB-ORTHO-CAUTION-001. Review was text-only; no audio. Current registry totals: **61 sources, 106 claims**, 30 phonological rules, 45 medial evidence rows, 7 source-phonemic sandhi examples and 9 Okell orthographic-profile rows.


## Primary-source access investigation: Okell 1969 and Nishi 1976/1977 — 2026-11-13

| Work item | Status | Evidence / acceptance boundary |
|---|---|---|
| Okell (1969), *A Reference Grammar of Colloquial Burmese* edition structure | DONE_VERIFIED (BIBLIOGRAPHIC METADATA) | Two-volume work confirmed independently by Glottolog, Open Library and Indiana University catalogue: vol.1 pp.xvii + 1–240; vol.2 pp.241–482 (482 numbered pages; 498 total physical pages). A reference-material guide describes vol.1 as “Sounds” and vol.2 as alphabetical particles/common words. Nishi (1998) cites the relevant examples to §§17–20. |
| Okell (1969) §§17–20 full text | BLOCKED (ACCESS) | National Library of Myanmar catalogue lists a PDF, but “View Resources” is paid. No open full text of §§17–20 was retrieved. Acceptance: inspect actual section pages, record examples/conditions and compare directly against Nishi 1998. Do not infer section contents from citations or catalogue metadata. |
| Nishi (1976/1977), *Medials in Burmese* archival locator | DONE_VERIFIED (PHYSICAL HOLDING DESCRIPTION) | Cornell University Library finding aid for Nicholas C. Bodman Papers, Collection 14-13-3031, Box 8 Folder 148, lists a July 1977 copy of “Medials in Burmese”, pp.41–52. This verifies an archival copy and pagination, not its contents or online access. |
| Nishi (1976) book chapter and 1977 journal reprint | DONE_VERIFIED (EDITION RECONCILIATION) | 1976 chapter in M. Hashimoto (ed.), pp.15–29; 1977 journal reprint in *Historical Science Reports of Kagoshima University* 26, pp.41–52. These are publication versions of the same study, not independent sources. |
| Nishi (1976/1977) full text | BLOCKED (PHYSICAL ACCESS REQUIRED) | No full text or scan found. Acceptance: request/consult Cornell Box 8 Folder 148 or locate a complete journal scan; inspect all 12 pages, verify page-by-page claims and distinguish original chapter pagination from reprint pagination. |

Claims added: CLM-OKELL1969-EDITION-STRUCTURE-001 and CLM-NISHI1977-ARCHIVAL-ACCESS-001. Source records updated with exact access limitations. Added regression test `test_okell_1969_edition_and_nishi_1977_archival_access_are_not_mistaken_for_full_text()`. No new linguistic rule or medial inventory claim was promoted. Current totals: **61 sources, 108 claims**, 30 phonological rules, 45 medial evidence rows, 7 source-phonemic sandhi examples and 9 Okell orthographic-profile rows. Review remained text-only; no audio.


## Mya2Rom 0.4.4 — complete 94-key vendor audit and MLCTS collision analysis — 2026-11-13

| Work item | Status | Evidence / acceptance boundary |
|---|---|---|
| Inventory-to-vendor fidelity | DONE_VERIFIED (SOURCE-CODE MATCH) | All **94/94 non-empty** Myanmar keys in `data/burmese/romanization_rimes_inventory.csv` match the vendored Mya2Rom 0.4.4 `vowels` object; all 94 MLCTS values match array column 2 (index 1). The upstream object has 95 keys including an empty-key fallback, intentionally excluded from the 94-row inventory. Vendored `romanisations.js` is byte-identical to upstream master at review. |
| MLCTS-to-source invertibility | PARTIAL / NON-INJECTIVE | **25 MLCTS collision groups**, each mapping two different Myanmar keys to the same MLCTS string. Added `data/burmese/romanization_rime_collisions.csv`. Preserve the Myanmar key; do not reverse-map a Latin MLCTS string to a unique source spelling. Collisions alone do not establish homophony or interchangeable spelling. |
| MLCTS vs MLCTS2 identity | DONE_VERIFIED (VENDOR DOCUMENTATION) | Upstream README distinguishes MLCTS (orthographic) from MLCTS2 (modified, more phonetic, reported as used by the MLC Myanmar-English Dictionary and SEAlang). The project's 94-row table uses the MLCTS column, not MLCTS2. Mya2Rom itself says its expanded tables also draw on Wikipedia and Wiktionary, so it is not a primary MLC publication. |
| Special auk-myit key | PARTIAL / CONTEXT-DEPENDENT | Upstream comments identify the standalone key `့` as an auk-myit-induced creaky-tone provision; the algorithm applies it in syllable matching. Its row now warns that this is not an independent vowel or coda. Do not treat it as a regular rime or infer a free-standing Ukrainian syllable. |
| Primary MLC written-source adjudication | BLOCKED / EVIDENCE GATE | Vendor fidelity is now verified, but the original MLC primary transcription table and every orthographic/rime distinction have not been checked against a primary MLC source or word-level dictionary entries. Acceptance: locate the actual MLC system tables and representative written dictionary entries for each collision group; reconcile orthographic variants, asat, anusvara, tone marks, and special cases. Keep all 94 Ukrainian candidates PROPOSED / EVIDENCE_LIMITED until that work and target-language adjudication are complete. |

Added claims: CLM-MYA2ROM-RIME-EXACT-MATCH-001, CLM-MYA2ROM-MLCTS-COLLISIONS-001, CLM-MYA2ROM-MLCTS-VS-MLCTS2-001 and CLM-MYA2ROM-AUKMYIT-FALLBACK-001. Added a machine-readable 25-group collision audit and regression tests for 94/94 vendor fidelity, collision preservation and the special auk-myit key. No runtime phonological or transcription rule was changed. Current totals: **61 sources, 112 claims**, 30 phonological rules, 45 medial evidence rows, 7 sandhi examples and 9 Okell orthographic-profile rows. No audio was accessed.


## Exact-head verification after 94-key MLCTS audit — 2026-11-13

- Final verified code/data head: `3ab1fb3d4359ede4f9f98ea02b608354268eeef1` on `research/burmese-medials-g2p-evidence-2026-11-13`.
- Main baseline remains `dc90463bdd734867308f03cb627eb8941efc19d6`; branch comparison: **270 commits ahead, 0 behind**. PR #147 remains OPEN / DRAFT / mergeable, 32 changed files; not merged. PR #129 remains untouched. No release or deployment published.
- Main CI run **43477600192**: SUCCESS. Python **228 passed + 66 subtests passed**; Node **20 passed, 0 failed**; Playwright **58 passed**; IPA-gold validator completed with `NOT_READY_NO_ADJUDICATED_GOLD`; package installation, production build, generated-data freshness and Chromium installation passed.
- Duplicate push-triggered CI run **43477590198** also completed successfully. Optional raw-output diagnostics **43477600305** completed successfully; diagnostics are not an accuracy benchmark.
- `npm install` reports **1 high-severity vulnerability**. No `npm audit fix --force` or broad dependency upgrade was applied. Separate dependency review remains required.
- Final registry totals: **61 sources, 112 claims**, 30 phonological rules, 45 medial evidence rows, 7 sandhi evidence rows, 9 Okell orthographic-profile rows; 94 vendor rime keys, 25 MLCTS collision groups. All Ukrainian rime candidates remain PROPOSED / EVIDENCE_LIMITED. No runtime phonological rule changed in this continuation.
- Earlier CI attempt failed only because the newly qualified auk-myit note no longer contained the existing vendor-provenance phrase expected by a test. The note was corrected without removing the linguistic caveat; exact-head CI above passed afterward.
- Repository remains a **PARTIAL PROTOTYPE**: primary MLC rime source, Okell §§17–20, Nishi 1976/1977 full text, independent modern Yangon IPA gold (0), tone model reconciliation and /N/ surface analysis remain open.


## Burmese MLCTS collision lexical evidence — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-MLCTS-COLLISION-LEXICAL-001 | PARTIAL | 25-row ledger added. The am pair has a secondary rhyme-table parallel (ကမ်/ကံ: /kàɴ/, MLCTS kam). The any pair has a secondary-table discrepancy (ကဉ်: kañ‘ vs ကည်: kany) against the vendor's shared any mapping. | Secondary table only. No primary MLC entry pairs verified. No vendor table correction, runtime mapping, or Ukrainian candidate promotion until MLC primary evidence is checked. |
| BURMESE-MLC-DICTIONARY-ACCESS-001 | BLOCKED / ACCESS | SEAlang metadata confirms the 1993 MLC dictionary basis and 1986 standard orthography. Direct live dictionary retrieval timed out; Firecrawl retrieval could not run because connected-service credits were exhausted. | Obtain accessible MLC primary table/dictionary entry text and record entry locators for all 25 groups; confirm the exact transcription field (MLCTS vs MLCTS2) before using it. |

Evidence source WIKTIONARY_BURMESE_TRANSLITERATION_2026; claims CLM-WIKT-RIME-AM-001 and CLM-WIKT-RIME-ANY-001. Totals: 62 sources / 114 claims. The 94 Ukrainian candidates remain PROPOSED / EVIDENCE_LIMITED; independent adjudicated IPA gold remains 0; accuracy remains null. No audio used.


## Secondary-source reconciliation — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-MLCTS-NASAL-FINALS-002 | PARTIAL — SECONDARY SOURCE AGREEMENT | Wikipedia's MLC-system summary lists shared -any, -am and -um mappings for the respective final pairs. Wiktionary's detailed rhyme examples agree for am and um, but differ for any. | This does not replace the original MLC publication or word-level MLC dictionary entries. Keep any conflict unresolved. |
| BURMESE-MLC-PRIMARY-TRANSCRIPTION-001 | BLOCKED / PRIMARY SOURCE | Original MLC system table and direct SEAlang dictionary entries were not retrieved. | Verify actual MLC table and representative entries, then resolve the any discrepancy and all remaining collision groups. |

Current ledger: 63 sources / 115 claims; 25 collision groups; 21 unadjudicated, 2 secondary-equivalence, 1 secondary-conflict, 1 special non-rime. No runtime change; no Ukrainian candidate promotion; no audio.


## Exact-head verification — MLCTS lexical audit (2026-11-13)

- Tested code/data snapshot: 46b7da6afd7ecc94e4dcac87c7f759132c74bc6b; research branch remains based on main dc90463bdd734867308f03cb627eb8941efc19d6.
- CI run 43491799213 SUCCESS: 229 Python tests passed + 66 subtests; 20 Node tests passed; 58 Playwright tests passed; production build, generated-data freshness, dependency install and Chromium install passed. Gold schema validator runs successfully but reports NOT_READY_NO_ADJUDICATED_GOLD (0 adjudicated records).
- Optional diagnostic run 43491799196 SUCCESS; outputs are not scored against independent gold and must not be represented as accuracy.
- npm install reports 1 high-severity vulnerability; dependency review remains open.
- Registry: 63 sources / 115 claims; 25 collision groups; lexical audit partition 21 unadjudicated / 2 secondary-equivalence / 1 secondary-source conflict / 1 special non-rime.
- No audio, runtime mapping changes or Ukrainian candidate promotions. Repository remains a PARTIAL PROTOTYPE.



## MLCTS primary-source provenance check — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-MLCTS-PRIMARY-SOURCE-PROVENANCE-002 | PARTIAL — SECONDARY PROVENANCE ONLY | Ohnmar Htun (2013), §5.1.2.3 p.80, identifies MLCTS [1980] and gives three examples; bibliography [47] p.122 cites the Wikipedia overview accessed 2012-10-12, not a directly identified MLC primary publication. | Do not treat the dissertation as the original specification. Obtain the MLC table itself and verify its exact edition, table rows and publication provenance. |
| BURMESE-ALA-LC-SYSTEM-SEPARATION-001 | DONE_VERIFIED | LOC's 2011 Burmese Romanization Table is explicitly a Library of Congress ALA-LC table and is recorded separately from MLCTS. | Keep ALA-LC correspondences out of MLCTS adjudication; use only for system comparison where explicitly labelled. |
| BURMESE-MLC-PRIMARY-TRANSCRIPTION-001 | BLOCKED / PRIMARY SOURCE | No direct MLC 1980 transcription table or word-level MLC dictionary entries were recovered in this pass. | Inspect primary MLC table and representative entries for all collision groups; distinguish MLCTS from MLCTS2 before adjudication. |

Registry now contains **66 nonblank source records / 118 claims**. No MLCTS/vendor correction, runtime mapping, IPA gold annotation or Ukrainian candidate promotion was made. No audio used.

## Registry count reconciliation — 2026-11-13

A fresh parse of the current CSV registries, counting only nonblank source rows and requiring unique IDs, finds **66 source records and 117 claim records**. The previous continuation note's 65-source count was one too low; the current source registry contains 66 nonblank IDs. Two pre-existing blank CSV records in `sources.csv` are ignored for this count. All 117 claim IDs are unique and every claim's `source_id` resolves to a registered source. The two new provenance records and claims are included in these totals.

A regression test now protects the distinction between the Htun secondary provenance trail and the LOC ALA-LC table. Test/CI status for the final code-bearing commit is pending verification; no local checkout was available in this connector session.

## MLC dictionary bibliographic cross-check — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-MLC-DICTIONARY-BIBLIOGRAPHY-003 | PARTIAL — BIBLIOGRAPHICALLY CORROBORATED | Unicode Consortium's Other Script Sources bibliography lists the 1993 Myanmar-English Dictionary as compiled and edited by MLC, alongside a 1996 Myanmar orthography treatise. | This is bibliographic confirmation only. Obtain and inspect the actual MLC dictionary entries and identify the transcription field before using any values. |

Registry totals: **66 nonblank source records / 118 claims**. A regression test protects the source record and the limitation that this bibliography does not expose entry text or transcription values.

## Final verification boundary for this continuation — 2026-11-13

- Registry parse on the current branch: **66 nonblank source records / 118 claim records**; all IDs unique, all row widths conform to their CSV headers, and every claim source reference resolves. Two blank CSV records are ignored by the count.
- The provenance regression test was added to `tests/test_romanization_rime_inventory.py`. The GitHub connector exposed no workflow runs and no commit status checks for final code/documentation head `caf66d5a6b58522ca33715654c38b075c1d1fc21`; therefore this latest test change is **NOT YET CI-VERIFIED**. Earlier successful CI on prior code/data head `46b7da6afd7ecc94e4dcac87c7f759132c74bc6b` does not cover this added test.
- No local checkout or local Python test execution was available. Do not claim the new test passed.

## MLC dictionary physical-access leads — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-MLC-DICTIONARY-ACCESS-ROUTE-004 | PARTIAL — PHYSICAL ACCESS LOCATED | WHO Myanmar Library record 487 lists an available 1993 MLC dictionary copy (635 pages); NDL record 000003254368 lists the 1996 Dunwoody reprint at Tokyo Main and Kansai-kan and a cooperating Japanese library. | Catalogue holdings are not text access. Obtain authorized consultation or page-level copies, then record exact entries and MLCTS/MLCTS2 field semantics. |

Registry totals: **68 nonblank source records / 120 claims**. The new regression assertions verify the two catalogue records while explicitly rejecting any inference that the contents have been inspected.

## MLC dictionary transcription-purpose evidence — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-MLC-DICT-TRANSCRIPTION-FIELD-005 | PARTIAL — PURPOSE CLUE ONLY | A 1996 Burma Debate notice says the MLC dictionary uses a transcription system to help English speakers pronounce entries. | The notice does not name MLCTS or MLCTS2. Inspect the dictionary's own front matter and representative entries before classifying its transcription field. |

Registry totals: **69 nonblank source records / 121 claims**. No transcription system was inferred from the advertisement.

## Final exact-head CI — provenance and registry tests (2026-11-13)

Code/test head **508816dcddf22272e98647625b657bc79712817e** completed required CI successfully:
- Workflow **43496624771**: SUCCESS.
- Python: **231 passed + 66 subtests passed**.
- Node: **20 passed, 0 failed**.
- Playwright: **58 passed**.
- Chromium install: PASS.
- Production build: PASS.
- Generated web-data freshness: PASS.
- IPA-gold validator: executed successfully, but reports **0 records / 0 annotations / 0 adjudicated records** and `NOT_READY_NO_ADJUDICATED_GOLD`; this is a data-readiness blocker, not a validator failure.
- Optional diagnostics workflow **43496624752**: SUCCESS for raw-output and CRF-baseline jobs. These remain diagnostics only, not scored accuracy.
- `npm install` still reports **1 high-severity vulnerability**; no forced dependency upgrade was made.
- Source registry integrity rechecked: **69 nonblank sources / 121 claims**, unique IDs, valid CSV row widths and all claim-to-source references resolve.
- The latest changes after code/test head are documentation-only. Final branch tip will be recorded after this handoff update.

## MLCTS/modified-column distinction — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-MLCTS2-COLLISION-CROSSWALK-006 | DONE_VERIFIED — VENDOR-DERIVED ONLY | Added a 25-row crosswalk comparing the MLCTS collision groups with Mya2Rom v0.4.4 third-column values. 21 pairs have the same value; four groups differ: any, any:, any., ui. A regression test compares every row to the vendored array. | This is implementation provenance, not MLC primary evidence. Do not promote lexical equivalence, pronunciation or Ukrainian output until dictionary entries / independent phonological evidence are inspected. |
| BURMESE-MLCTS2-NAMING-RECONCILIATION-007 | DONE_VERIFIED — SOFTWARE DOCUMENTATION SCOPE | README/API calls the third mode mlcts2; the implementation indexes array column 2; romanisations.js labels the column MLCTS-SL. The discrepancy is now explicit in source claims and tests. | Keep both names in provenance; do not silently relabel the upstream source table or infer that it is a separate system. |
| BURMESE-MOW-MLCTS2-RESOURCE-008 | PARTIAL — SECONDARY RESOURCE | MOW v0.1.2 documents MLCTS and MLCTS 2 romanized search variants; v0.1.3 is CC BY 4.0. | The small semantic wordnet can support lexical lookup and variant discovery, not primary MLC table adjudication or a pronunciation gold set. |

Registry totals: **70 nonblank source records / 123 claims**. The crosswalk test is added; CI status for this latest code/test commit is pending.

## Earlier MLC Concise Dictionary — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-MLC-CONCISE-DICTIONARY-ACCESS-009 | PARTIAL — PRIMARY WORK IDENTIFIED, CONTENT NOT INSPECTED | Allott 1985 reports five parts published 1978-1980 and says the work gives pronunciations; Okell 1982 bibliography identifies a five-volume Rangoon edition from Mranmācā Aphwai. | Locate an authorized physical or digital copy. Inspect title pages, pronunciation key and entries. Do not assume its pronunciation notation is MLCTS or MLCTS2. |

Registry totals: **72 nonblank sources / 125 claims**; source IDs and claim IDs unique, all claim source references resolve, and CSV widths validate.

## Complete Mya2Rom vendor-system inventory — 2026-11-13

- Added `data/burmese/romanization_rimes_vendor_systems.csv`, a 94-row companion inventory that records the exact vendor IPA, MLCTS, modified MLCTS/MLCTS2, Simple and Simple2 values for every non-empty rime key. It is separate from the Ukrainian candidate inventory and does not change runtime behaviour.
- All 94 source keys are present in the vendored Mya2Rom table. The only key whose array has four values rather than five is `ေါင်း`: its Simple2 value is not provided by the upstream array. This missing value is recorded as missing, not guessed.
- Added regression coverage that parses the vendored JS array and compares all 94 rows/columns, while preserving the evidence boundary that these are vendor mappings, not a primary MLC table or independent IPA gold.
- Registry remains **72 nonblank sources / 125 claims**; no new source claim was needed because this artifact is a deterministic extraction of already registered Mya2Rom v0.4.4.
- Exact-head CI for this latest added full crosswalk test is pending.

## Full crosswalk exact-head CI result — 2026-11-13

Code/test commit **c35a7ae0255725aa85cf5f836c64b4ed1fa5b731** completed required CI successfully:
- Workflow **43498396994**: SUCCESS.
- Python: **233 passed + 66 subtests passed** (includes full 94-key and 25-collision crosswalk checks).
- Node: **20 passed, 0 failed**.
- Playwright: **58 passed**; Chromium installation passed.
- Production build: PASS.
- Generated web-data freshness: PASS.
- IPA-gold structural validator executed, but gold remains **NOT_READY_NO_ADJUDICATED_GOLD** (0 independent adjudicated records); successful execution is not evidence that a gold set exists.
- `npm install` still reports **1 high-severity vulnerability**. No dependency force-upgrade was made.
- Latest branch changes after the tested code commit are documentation-only.

## Branch/PR reconciliation after crosswalk work — 2026-11-13

- Dedicated branch: `research/burmese-medials-g2p-evidence-2026-11-13`; current branch comparison before this documentation update: **351 commits ahead of main / 0 behind**.
- PR **#147** remains **OPEN / DRAFT / mergeable**, unmerged; 35 changed files at this checkpoint. Main was not modified.
- PR #129 remains untouched because it was previously found divergent and not mergeable; PR #146 remains merged.
- Latest required CI is green on code/test commit `c35a7ae0255725aa85cf5f836c64b4ed1fa5b731` (run 43498396994). Optional raw-output diagnostic passed; optional CRF-baseline job is still in progress and is not an acceptance benchmark.
- Current source registries: **72 sources / 125 claims**, all IDs unique, CSV widths valid and all claim-to-source references resolve.
- Release readiness remains **PARTIAL PROTOTYPE / NOT RELEASE-READY**: primary MLC source text, independent IPA gold, tone/prosody model validation and npm high-severity dependency finding remain unresolved.

## MOW orthographic lemma coverage — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-MOW-RIME-LEXICAL-COVERAGE-010 | DONE_VERIFIED — ORTHOGRAPHIC STRING MATCH ONLY | Official MOW v0.1.3 CC BY 4.0 lemma release; 1,476 lemma rows / 1,041 distinct forms. Added 50-unit summary and 508 unit/lemma hits (442 distinct forms, 547 synsets); both sides occur for 11/25 collision groups, one side for 13/25, neither for 1/25. Regression tests validate table consistency and scope. | Exact word-final substring matches only. No syllabification, pronunciation, MLCTS primary adjudication or homophony claim. Do not promote runtime or Ukrainian outputs. |
| BURMESE-MLCTS-COLLISION-LEXEME-ADJUDICATION-011 | TODO — PRIMARY DICTIONARY / PHONOLOGICAL EVIDENCE | MOW gives orthographic search leads but no pronunciations. | Use these lemmas to locate candidate entries in MLC primary dictionaries; inspect entry headwords and pronunciation key. Confirm exact lexical pairs and pronunciation independently before changing the 25-group ledger. |

The collision-ledger statuses are unchanged: 21 unadjudicated, 2 secondary equivalence, 1 secondary-source conflict, 1 special non-rime. Registry totals: **73 nonblank sources / 126 claims**.

## Reproducible MOW orthographic coverage audit — 2026-11-13

- Vendored the exact upstream MOW v0.1.3 TSV at `data/burmese/external/mow-0.1.3-mya_20171005165336.tab`; its original header is preserved: `## MOW 0.1.3 / mya / CC BY 4.0`. Source ID **MOW_2017_0_1_3_DATASET** and claim **CLM-MOW-ORTHOGRAPHIC-RIME-COVERAGE-001** were added in the concurrent continuation commits already on this branch.
- Added deterministic stdlib-only generator `scripts/analyze_mow_orthographic_rime_coverage.py` with `--check` mode, plus generated files `mow_rime_orthographic_matches.csv` (508 exact source-unit/lemma pairs) and `mow_rime_orthographic_coverage.csv` (50 source-unit rows).
- Recomputed results from the vendored file: 1,476 MOW `mya:lemma` rows, 1,041 distinct lemma forms, 1,198 synsets; 508 suffix-match pairs across 35/50 source-unit variants; 442 distinct matched lemmas and 547 distinct matched synsets. For the 25 collision groups: both variants occur in 11 groups, one side in 13, neither in 1.
- These are exact Unicode orthographic suffix matches, not Burmese syllabification or pronunciation. They do not confirm homophony, MLCTS equivalence, MLC system correctness, or Ukrainian outputs. The generator/test preserve this limitation. The raw upstream license header and source attribution are retained.
- Added two tests: source/license header preservation and reproducible output/count/evidence-boundary validation. Exact-head CI pending.

### Schema-gate correction for MOW dataset-derived claim — 2026-11-13

The first CI attempt after registering the MOW orthographic coverage claim (workflow 43499220650) correctly rejected the locally invented evidence status `DATASET_DERIVED`, because the canonical claim schema does not allow that value. The claim was corrected to the existing schema-supported status `ANALYSIS_DEPENDENT` (commit 5e12f86e21f5576efee44afe84f80759e3799a9e); its scope remains orthographic suffix analysis only. The subsequent exact-head workflow is running with the schema correction, canonicalized test placement and reproducible generator check.

## Final MOW reconciliation and remaining SEAlang access blocker — 2026-11-13

| ID | Status | Evidence | Acceptance criterion |
|---|---|---|---|
| BURMESE-MOW-CANONICAL-GENERATOR-013 | DONE_VERIFIED | The repository's canonical Python generator and vendored CC BY 4.0 MOW release produce the committed 508-pair / 50-unit orthographic coverage outputs. The test suite runs generator `--check`; duplicate parallel exports and duplicate test module were removed. | Keep one canonical generator/output path. Treat results only as orthographic suffix search leads. |
| BURMESE-SEALANG-ENTRY-ACCESS-014 | BLOCKED — SERVICE RETRIEVAL | SHACHI/SEAlang metadata and the 2008 interface description establish an MLC 1993 dictionary derivative, IPA search/display capability and project-level permission; direct Burmese dictionary/API requests timed out or returned 502/400-timeout, and no entry text was retrieved. | Retrieve actual entries for selected MOW lemma leads with headword, dictionary transcription and IPA fields; record exact source locators and adjudicate against the MLC dictionary/primary key. Interface screenshots and metadata alone do not satisfy this. |

Exact code/test head **c76fab9e4e4a910170a26dd8ed89a95790c7973d**: CI runs 43499475187 and 43499485256 SUCCESS — 236 Python + 66 subtests, 20 Node, 58 Playwright; build and generated-data freshness PASS. IPA gold remains NOT_READY_NO_ADJUDICATED_GOLD. npm install still reports one high-severity vulnerability. Registry: 73 sources / 126 claims.

## MOW reproducibility and schema-corrected exact-head CI — 2026-11-13

- The MOW-derived claim status was changed from unsupported `DATASET_DERIVED` to schema-supported `ANALYSIS_DEPENDENT`; the scope remains the same orthographic string-match analysis.
- Required CI on code/test head `c76fab9e4e4a910170a26dd8ed89a95790c7973d`, workflow **43499485256**, completed **SUCCESS**:
  - Python: **236 passed + 66 subtests passed** (includes MOW generator `--check`, dataset/license guard, crosswalks and schema validation).
  - Node: **20 passed, 0 failed**.
  - Playwright: **58 passed**; Chromium install passed.
  - Production build and generated web-data freshness: PASS.
  - `npm install`: **1 high-severity vulnerability** remains.
- Optional diagnostics workflow **43499220654**: both raw-output and CRF-baseline jobs passed. They remain raw diagnostic artifacts, not an accuracy score or evidence for Ukrainian output.
- The generated MOW pair/coverage files are reproducible from the vendored CC BY 4.0 TSV using the stdlib script; test checks committed artifacts against regenerated output.

## Latest branch state after MOW coverage completion — 2026-11-13

- Final documentation/PR-body checkpoint before this note: branch `research/burmese-medials-g2p-evidence-2026-11-13`, **395 commits ahead of main / 0 behind**; PR #147 **OPEN / DRAFT / mergeable**, 39 changed files. The branch remains unmerged; main is unchanged.
- Required CI run **43499485256** passed on code/test commit `c76fab9e4e4a910170a26dd8ed89a95790c7973d`: 236 Python + 66 subtests, 20 Node, 58 Playwright; build, generated-data freshness and Chromium installation passed. Optional raw-output + CRF diagnostic jobs both passed in run **43499485104**.
- The earlier schema failure was only the unsupported claim status `DATASET_DERIVED`; corrected to `ANALYSIS_DEPENDENT`, and the full schema-validation suite passed on the rerun.
- Registry: **73 sources / 126 claims**, unique IDs, valid CSV widths and all claim-to-source references resolved.
- Remaining blockers unchanged: inspect primary MLC dictionary/MLCTS source pages; independently adjudicate IPA gold and tone/prosody; resolve one high-severity npm finding. Project remains **PARTIAL PROTOTYPE / NOT RELEASE-READY**.

## SEAlang API request-pattern lead — 2026-11-13

- Added **SEALANG_SHORTCUT_2022** and **CLM-SEALANG-API-REQUEST-PATTERN-001**. A third-party open-source Burmese shortcut constructs dictionary requests using `http://sealang.net/api/api.pl?service=dictionary&lang=burmese&query=<word>`; the source code also distinguishes the dictionary `query` parameter from the Google `text` parameter.
- This corrects the request template for future attempts, but it does not prove the endpoint is currently available or expose the response schema. Exact request attempts through the web reader still returned 502/inaccessible; Firecrawl could not run because its connected account had exhausted credits. No dictionary entry text was retrieved and no transcription field was adjudicated.
- Added a regression assertion for the API pattern and its limitation. Registry now contains **74 sources / 127 claims**; all IDs remain unique, CSV widths valid and claim source references resolve.
- Next access attempt should use the exact lowercase `lang=burmese` parameter and test the endpoint from a permitted browser/client when connectivity is available; do not treat the third-party wrapper as an authoritative API specification.

## R12A secondary phonological crosswalk and final CI — 2026-11-13

- Reviewed the existing 25-row `romanization_rime_r12a_secondary_phonology_crosswalk.csv` against the current R12A public page. It distinguishes the `any`, `any:` and `any.` groups: the ဉ-series is nasalised (IPA values use archiphoneme `N`), while ည်-series has three non-nasal outcomes. It also gives 18 same-value groups, two partial-coverage groups (`ui`, `un`), one unlisted group (`a.`) and the special non-rime `u.` fallback.
- This strengthens the secondary evidence that the any-series is not a single phonological value, but it does not resolve the MLCTS orthographic collision or replace the MLC primary table. R12A explicitly does not account for vowel reduction and cites secondary phonology sources; no runtime, IPA gold or Ukrainian candidate was changed.
- Latest code/test head `1f6f6a33c1a7c783e921bcf5edada4f05cfa3c6d`, required CI **43500600771 SUCCESS**: **237 Python + 66 subtests**, **20 Node**, **58 Playwright**; Chromium, build and generated-data freshness passed. `npm install` still reports **1 high-severity vulnerability**.
- Optional diagnostics **43500600533 SUCCESS**: raw-output and CRF diagnostic jobs passed; not an accuracy benchmark.

## Latest R12A + SEAlang checkpoint — 2026-11-13

- Registry now contains **75 sources / 128 claims**, including the R12A secondary orthography notes and third-party SEAlang API request-pattern source; all IDs are unique, all CSV widths valid and every claim source reference resolves.
- Branch comparison at this checkpoint: **414 ahead of main / 0 behind**. PR #147 remains **OPEN / DRAFT / mergeable**, unmerged. No main changes or release publication.
- Required CI on latest code/data commit `1f6f6a33c1a7c783e921bcf5edada4f05cfa3c6d`, run **43500600771**, passed: 237 Python + 66 subtests, 20 Node, 58 Playwright, build and generated-data freshness. Optional raw-output/CRF diagnostics run **43500600533** also passed, diagnostic-only.
- One high-severity npm vulnerability remains; primary MLC dictionary transcription field and independent IPA gold remain blocked.
- R12A source and claim are registered as **R12A_BURMESE_ORTHOGRAPHY_2026 / CLM-R12A-RIME-CROSSWALK-2026-001**. Final registry totals after this addition: **75 sources / 128 claims**; source IDs and claim IDs are unique, all claim→source references resolve, and CSV row widths validate.

## MLC 1986 orthography standard — Unicode WG2 corroboration — 2026-11-13

- Added **UNICODE_N2827_MYANMAR_SEMIVOWELS_2004** and claim **CLM-UNICODE-N2827-MLC-MEDIALS-001**. This 2004 national contribution from the Myanmar Unicode and NLP Research Center to ISO/IEC JTC1/SC2/WG2 states that the MLC published *Myanmar Orthography* in October 1986 and that the Ministry of Education prescribed it as the national standard. It describes four basic medial signs and combinations totalling eleven symbols, and explains that medials change pronunciation and are structurally distinct from stacked consonants.
- This is useful documentary evidence for the structural-analysis stage of the pipeline, but it is not the MLC book itself and contains no MLCTS/IPA rime transcription table. The original 1986 orthography book remains uninspected.
- Added a regression assertion that protects the structural-only evidence boundary. Registry totals: **76 sources / 129 claims**; IDs unique, CSV widths valid, all claim source references resolve. Exact-head CI pending.

## MLC 1986 orthography book access — 2026-11-13

| ID | Status | Evidence | Acceptance criterion |
|---|---|---|---|
| BURMESE-MLC-1986-ORTHOGRAPHY-ACCESS-015 | BLOCKED — CATALOG PAGE / PDF NOT RETRIEVED | National Library of Myanmar E-Resources record 189 lists the MLC 1986 second edition, 292 pages, with a PDF option; this aligns with Unicode WG2 N2827's reference to the October 1986 national orthography standard. The bibliographic page returned 502; no book content was inspected. | Retrieve the listed PDF or an authorized scan. Inspect title page, foreword, structural orthography sections and any pronunciation/transcription tables. Confirm whether this is the exact work cited by N2827; do not infer MLCTS/IPA from the catalog metadata. |

Registry totals after registering the catalog lead: **77 sources / 130 claims**, unique IDs and all claim source references valid. CI on test-bearing head `a824fe13c3671b5f02d37c3dc9127ffc460ac1a8` pending.

## Partial primary scan of the 1986 Myanmar Spelling Dictionary — 2026-11-13

- Added **UNICODE_L2_2010_MLC_SPELLING_1986** and **CLM-UNICODE-L2-2010-MLC-SPELLING-SCAN-001**. Unicode WG2 paper L2/10-360 identifies a *Myanmar Spelling Dictionary* published in 1986 and reproduces an image of original page 1, headed “Characters pronunciation List”, plus images of pages 2-9. The explanatory note says the character pronunciation list corresponds to a Myanmar Language Character Map and discusses sorting.
- This is the first directly viewable partial scan of a 1986 Myanmar spelling reference found in this pass. It is not a complete book; the visible tables are orthographic character/pronunciation-list material, not an MLCTS/IPA rime table or word-level dictionary entries. Its identity with the MLC *Myanmar Orthography* in N2827 and National Library record 189 remains unconfirmed.
- The National Library of Myanmar E-Resources catalog record 189 separately lists the MLC 1986 orthography book as a second edition, 292 pages, with a PDF option; the catalog page itself timed out. The Unicode partial scan is a concrete additional source lead but does not clear the primary transcription evidence gate.
- Added regression assertions for the partial-scan status and non-MLCTS/IPA boundary. Registry totals: **78 sources / 131 claims**; IDs unique, CSV widths valid, and all claim→source references resolve.

## 1986 source access lead and exact-head verification — 2026-11-13

- National Library of Myanmar catalog record 189 lists the MLC 1986 orthography work as a second edition, 292 pages, with a PDF option. Unicode WG2 L2/10-360 separately provides a partial scan of a 1986 *Myanmar Spelling Dictionary* (original pages 1-9, including a “Characters pronunciation List”). Their exact bibliographic identity is not confirmed; the catalog page timed out.
- The partial scan is orthographic character/pronunciation-list material, not an MLCTS/IPA rime table or word-level dictionary. No transcription field or candidate pronunciation was inferred.
- Required CI on code/test commit `8e8448b70549062636c3f1c539ee1010f93a86cb`, workflow **43501650235**, completed **SUCCESS**: **241 Python + 66 subtests**, **20 Node**, **58 Playwright**; Chromium, production build and generated-data freshness passed. Optional raw-output/CRF diagnostics **43501650409** passed but are not accuracy scores.
- Registry: **78 sources / 131 claims**, unique IDs, valid CSV widths and all claim source references resolve. One high-severity npm vulnerability remains; IPA gold is still `NOT_READY_NO_ADJUDICATED_GOLD`.
- Branch comparison at the preceding checkpoint: **440 ahead / 0 behind**. PR #147 remains open, draft, mergeable and unmerged; main unchanged.

## Final checkpoint — 2026-11-13

- Dedicated branch `research/burmese-medials-g2p-evidence-2026-11-13`: **445 commits ahead of main / 0 behind**. PR **#147** is **OPEN / DRAFT / mergeable**, unmerged; 40 changed files. PR #129 remains untouched (divergent/non-mergeable at last review); PR #146 remains merged. Main and release state unchanged.
- Latest required CI on code/test head `8e8448b70549062636c3f1c539ee1010f93a86cb`, run **43501650235 SUCCESS**: **241 Python + 66 subtests**, **20 Node**, **58 Playwright**, Chromium, production build and generated-data freshness all passed. Optional diagnostics **43501650409 SUCCESS** (raw-output + CRF; not an accuracy score).
- Source registries: **78 sources / 131 claims**, all IDs unique, valid row widths, all source references resolve.
- Remaining blockers: obtain and inspect complete MLC orthography/1993 dictionary contents and identify the exact transcription field; adjudicate the 25 collision groups from primary lexical evidence; build independent IPA gold and validate tone/prosody; resolve one high-severity npm vulnerability. Status remains **PARTIAL PROTOTYPE / NOT RELEASE-READY**.

## MLC medial structural parser coverage — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-MLC-MEDIAL-STRUCTURAL-PARSER-016 | DONE_VERIFIED — ORTHOGRAPHIC_ONLY | `tests/test_parser.py::test_mlc_medial_inventory_is_parsed_structurally_without_phonetic_guessing` covers all 11 MLC medial forms (4 basic + 5 pairs + 2 triples), preserving ordered medial IDs in one syllable and asserting no IPA/phonology assignment. Exact-head CI 43502733106 SUCCESS: 242 Python + 66 subtests, 20 Node, 58 Playwright; build and generated-data freshness pass. | Structural parser regression only. All medial phonological rules remain withheld pending source-specific onset × rime × prosody evidence and adjudicated IPA gold. |

Project status remains **PARTIAL PROTOTYPE / NOT RELEASE-READY**: IPA gold is not ready and one high-severity npm vulnerability remains.

## MOW orthographic lexical coverage — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-MOW-ORTHOGRAPHIC-COVERAGE-017 | DONE_VERIFIED — ORTHOGRAPHIC_SUFFIX_ONLY | Generator `scripts/analyze_mow_orthographic_rime_coverage.py`, two committed CSV outputs, reproducibility `--check` test. 508 source-unit/lemma pairs, 50 source-unit rows; 11 collision groups both sides found, 13 one side, 1 neither. Exact-head CI 43503144848 SUCCESS: 242 Python + 66 subtests, 20 Node, 58 Playwright, build and generated-data freshness pass. | Do not treat suffix matches as syllable segmentation, pronunciation, MLCTS correctness or homophony. MOW is not exhaustive; absence is not evidence of nonexistence. Primary MLC lexical and pronunciation evidence is still required. |

Project remains PARTIAL PROTOTYPE / NOT RELEASE-READY. IPA gold is `NOT_READY_NO_ADJUDICATED_GOLD`; one high-severity npm vulnerability remains.

## MLC 1978 spelling-book catalogue lead — 2026-11-13

| ID | Status | Evidence | Acceptance criterion |
|---|---|---|---|
| BURMESE-MLC-SPELLING-BOOK-1978-ACCESS-018 | PARTIAL — CATALOGUE LEAD ONLY | National Diet Library of Japan record R100000136-I1970023484907173422 records a Burmese-language MLC orthography/spelling reference published in 1978. Allott (1985, p.145) independently reports that the MLC spelling book was published in 1978, while separately describing the five-part Concise Burmese Dictionary as issued from late 1978 through 1980. New registry records: NDL_MLC_SPELLING_1978_CATALOG / CLM-MLC-SPELLING-BOOK-1978-CATALOG-001. | Obtain title page and contents; verify exact identity of the catalogue title with Allott's spelling book and distinguish it from the Concise Dictionary. Inspect whether any pronunciation or transcription material exists. No MLCTS/IPA inference from catalogue metadata. |

This is a new access route, not newly inspected primary content. Existing Allott/Okell Concise Dictionary records remain separate. Registry totals after update: 80 sources / 132 claims (before CiNII record; historical checkpoint). Exact-head CI pending.

## MLC 1978 spelling-book retrieval routes — 2026-11-13

| ID | Status | Evidence | Acceptance criterion |
|---|---|---|---|
| BURMESE-MLC-SPELLING-BOOK-ACCESS-019 | PARTIAL — RETRIEVAL ROUTES IDENTIFIED | CiNii Books NCID BA69415754 records 28, 379 pages, 17 cm and holdings at three Japanese libraries (Osaka University and Tokyo University of Foreign Studies). Google Books record _V1LAAAAMAAJ identifies a 379-page scan originating from the University of Michigan, digitized 2007, but exposes snippet-view metadata only. Added CINII_MLC_SPELLING_1978_HOLDINGS / CLM-MLC-SPELLING-BOOK-ACCESS-002. | Request a copy from one of the holding libraries or inspect any accessible Google Books pages. Capture title page, contents and relevant spelling/pronunciation sections with page locators. No claim about actual book contents until inspected. |

Registry totals: 80 sources / 133 claims (verified nonblank, unique source IDs). Exact-head CI pending.

## Crosswalk consistency validation — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-RIME-CROSSWALK-INTEGRITY-020 | IMPLEMENTED — CI PENDING | Added `tests/test_rime_crosswalk_consistency.py` to verify that the Mya2Rom MLCTS2 crosswalk, R12A secondary phonology crosswalk and lexical audit all cover the same 25 collision groups with matching source-unit identities; validates two-position array alignment, enumerated comparison states, and explicit secondary-vs-primary boundaries. | Integrity checks validate table consistency only. They do not establish pronunciation, lexical identity, primary MLC correctness or Ukrainian output. CI must pass before DONE_VERIFIED. |

## Rime crosswalk integrity and evidence triage — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-RIME-CROSSWALK-INTEGRITY-020 | DONE_VERIFIED — DATA_INTEGRITY_ONLY | `tests/test_rime_crosswalk_consistency.py` verifies all three existing 25-row crosswalks share the same MLCTS keys and source-unit pairs, validates MLCTS2 and R12A two-position value alignment, and locks their observed status distributions. Required CI run **43507606882 SUCCESS** on code commit `de7abaea084515c5ef814575656ede8b83369a6a`: 248 Python, 66 subtests, 20 Node, 58 Playwright; build and generated-data freshness passed. | This validates table alignment and evidence labels only. It does not establish pronunciation, lexical identity, primary MLC correctness, IPA gold or Ukrainian output. |

### Cross-system triage from existing tables (no new linguistic adjudication)

- **Priority 1 — `any` / `any:` / `any.`:** Mya2Rom MLCTS2 and R12A both distinguish the paired Myanmar forms in all three groups. The lexical audit has an explicit secondary-source conflict for `any` (`/kɪ̀ɴ/` versus `/kì/, /kè/, /kɛ̀/`), while `any:` and `any.` remain unadjudicated. This is the clearest existing conflict cluster to preserve for later lexical review; it is not resolved by agreement between secondary tables.
- **Priority 1 — `ui`:** MLCTS2 distinguishes the two source units and R12A has partial coverage (`NOT_COVERED` for one side); the lexical audit has no word-level adjudication. Keep both source units separate.
- **Special handling — `u.`:** both crosswalks classify this as context-dependent/special non-rime behavior. Do not count `့` as an ordinary independent rime or force it into ordinary vowel/coda logic.
- **Secondary corroboration only — `am` and `um`:** both vendor MLCTS2 and R12A show matching outputs for the paired units; the lexical audit records secondary equivalence examples (`/kàɴ/` and `/kòʊɴ/`). These examples do not prove universal equivalence or primary MLC policy.
- **All remaining groups:** retain their existing unadjudicated state. Cross-table agreement is not primary lexical proof.

No source records or runtime rules were promoted by this triage. The first CI attempt exposed two over-specific test assertions; the assertions were corrected against the actual CSV values, and the subsequent required run passed.

## MOW orthographic candidate lists for priority collision groups — 2026-11-13

This is a targeted readout of the already-generated `mow_rime_orthographic_coverage.csv` and `mow_rime_orthographic_matches.csv`, not a new pronunciation dataset.

| MLCTS group | First source unit | MOW lemma matches | Second source unit | MOW lemma matches | Result |
|---|---|---:|---|---:|---|
| `any` | ဉ် | 6 | ည် | 13 | Both sides occur as exact Unicode suffixes |
| `any:` | ဉ်း | 1 | ည်း | 6 | Both sides occur as exact Unicode suffixes |
| `any.` | ဉ့် | 0 | ည့် | 5 | Only second side occurs |
| `ui` | ို် | 0 | ို | 15 | Only second side occurs |

Examples exposed by the existing match table include `ဥယျာဉ်`, `တိရစ္ဆာန်ဥယျာဉ်`, `ယာဉ်` for ဉ်; `ပြည်`, `မြန်မာပြည်`, `လက်ဖက်ရည်` for ည်; `အကျဉ်း` for ဉ်း; and `ချို`, `ငို`, `ဆို`, `တို`, `မှို` for ို. These are candidate lemmas for text-based dictionary lookup only. Suffix matching does not establish syllable boundaries, rime identity, tone, pronunciation or homophony.

The MOW table does not currently provide a lexeme-level adjudication for the `any` or `ui` collision. The next practical step is to use these exact lemmas as lookup keys in already-registered textual resources, recording each dictionary's spelling, entry headword, pronunciation/transcription field and page/entry locator where available. Do not populate observed IPA from MOW.

## Source registry row-count correction — 2026-11-13

Append a correction note: The source CSV contained three internal blank separator lines (plus the final newline); the earlier row-count method counted the three blank lines as empty rows. Removed all blank lines and added a regression test for nonblank unique source IDs. The actual registry contains 80 unique source records and 133 claim records. Historical row-count figures above are superseded.

## Source registry hygiene — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-SOURCE-REGISTRY-INTEGRITY-021 | DONE_VERIFIED — REGISTRY_STRUCTURE | Removed three internal blank separator rows from `data/burmese/sources.csv`; added `test_source_registry_has_no_blank_rows_or_duplicate_source_ids`. Current registry: **80 nonblank unique source records / 133 claims**. Required CI on code commit `62f59f177b15e2df54ace464056df7932058bffb`, run **43508294905 SUCCESS**: 249 Python + 66 subtests, 20 Node, 58 Playwright; build and generated-data freshness passed. | Structural registry integrity only; does not validate source quality or promote linguistic claims. |

The earlier 82/132 and 83/133 counts in preceding catalogue-lead entries were inflated by blank CSV rows and are superseded by the verified 80/133 count above.

## Wiktionary word-level secondary evidence for collision groups — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-LEXICAL-RIME-EXAMPLES-022 | DONE_VERIFIED — SECONDARY_WORD_LEVEL_EXAMPLES_ONLY | Added three source-linked claims under existing `MYWIKTIONARY2026` and enriched the 25-row lexical audit for `any`, `any:` and `ui`. Required CI run **43509339740 SUCCESS** on code commit `191501979a2c5d8b7c0db9a00af5600b7266201f`: 251 Python + 66 subtests, 20 Node, 58 Playwright; build and generated-data freshness passed. | Wiktionary is secondary evidence. No primary MLC rule, universal equivalence, IPA gold or runtime/Ukrainian mapping is authorized. `ui` remains one-side-only. |

### New word-level examples

- `any`: `ဥယျာဉ်` is listed as MLCTS `u.yyany`, IPA `/ʔṵjɪ̀ɴ/` or `/ʔújɪ̀ɴ/`; `ပြည်` is `prany`, IPA `/pjì/`. The shared MLCTS rime suffix is therefore not evidence of homophony.
- `any:`: `အကျဉ်း` is `a.kyany:` with `/ʔət͡ɕɪ́ɴ/`; `နည်း` is `nany:` with `/nɛ́/` for one sense and `/ní/` for another. This supplies secondary examples on both source-unit sides and documents sense-dependent pronunciation under one spelling/MLCTS form.
- `ui`: `ချို` (`hkyui`, `/d͡ʑò/`), `ဆို` (`hcui`, `/sʰò/`) and `တို` (`tui`, `/tò/`) attest the `ို` side only. The paired `ို်` side has no MOW suffix matches, so this is not a comparison.

Updated lexical audit distribution across 25 groups: 19 unadjudicated; 2 secondary-system equivalence; 1 secondary-source conflict (`any`); 1 secondary-source distinction (`any:`); 1 secondary one-side-only (`ui`); 1 special non-rime (`u.`). MLCTS2 crosswalk status is synchronized to the lexical audit and tested. Registry now contains **80 unique sources / 136 unique claims**; no new source record was required.

## Additional `any.` lexical examples — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-ANY-DOT-LEXICAL-023 | PARTIAL — SECONDARY_WORD_LEVEL_EXAMPLES | Added `စဉ့်` (`cany.`, `/sɪ̰ɴ/`) and `ကြည့်` (`krany.`, `/t͡ɕḭ/`) as source-linked word-level examples for ဉ့် and ည့်. Added claim `CLM-WIKTIONARY-ANY-DOT-WORD-LEVEL-EXAMPLES-001`; crosswalk status parity and regression assertions updated. Registry: 80 sources / 137 claims. | Not a minimal pair or primary MLC specification. No IPA gold, runtime or Ukrainian mapping promotion. CI pending. |

Lexical audit distribution now: **18 unadjudicated / 2 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 1 secondary one-side-only / 1 special non-rime**. `စဉ့်` is not in MOW; `ကြည့်` is a MOW-listed candidate. The MOW coverage table is unchanged.

## Additional `aung` lexical examples — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-AUNG-LEXICAL-024 | PARTIAL — SECONDARY_WORD_LEVEL_EXAMPLES | Added `ပေါင်` (`paung`, `/pàʊɴ/`) and `တောင်` (`taung`, `/tàʊɴ/`) as lexical examples for ေါင် and ောင်. Same secondary rime sequence `/àʊɴ/` with different onsets. Added claim `CLM-WIKTIONARY-AUNG-WORD-LEVEL-EXAMPLES-001`; updated audit/crosswalk parity and tests. Registry: 80 sources / 138 claims. | Secondary equivalence only; not a controlled minimal pair or primary MLC specification. No IPA gold, runtime or Ukrainian mapping promotion. CI pending. |

Lexical audit distribution now: **17 unadjudicated / 3 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 1 secondary one-side-only / 1 special non-rime**.

## Exact-head verification — lexical collision audit continuation — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-RIME-LEXICAL-AUDIT-VERIFICATION-025 | DONE_VERIFIED — DATA_AND_TEST_INTEGRITY | Code/data snapshot `eb81bd29e9417ddbd6d541d54fce6d754b0bb8bd`; required CI **43513203135 SUCCESS** (duplicate **43513212043 SUCCESS**): 251 Python + 66 subtests, 20 Node, 58 Playwright; production build, generated-data freshness and Chromium install passed. Optional raw-output diagnostic **43513212088 SUCCESS**. | Verifies registry/crosswalk parity and application test suite only. IPA gold remains 0; accuracy null; secondary lexical entries are not primary MLC adjudication. One high-severity npm vulnerability remains. |

Current collision ledger: **17 unadjudicated / 3 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 1 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 138 claims**.

## Additional `aung:` lexical examples — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-AUNG-COLON-LEXICAL-025 | PARTIAL — SECONDARY_WORD_LEVEL_EXAMPLES | Added MOW-listed `ပေါင်း` (`paung:`, `/páʊɴ/`) and `ကျောင်း` (`kyaung:`, `/t͡ɕáʊɴ/`) for ေါင်း and ောင်း. Same secondary IPA rime sequence `/áʊɴ/`, different onsets. Added claim `CLM-WIKTIONARY-AUNG-COLON-WORD-LEVEL-EXAMPLES-001`; updated audit/crosswalk parity and tests. Registry: 80 sources / 139 claims. | Secondary equivalence only; not a controlled minimal pair or primary MLC specification. No IPA gold, runtime or Ukrainian mapping promotion. CI pending. |

Current collision ledger: **16 unadjudicated / 4 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 1 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 139 claims**.

## Additional `auk` lexical examples — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-AUK-LEXICAL-026 | PARTIAL — SECONDARY_WORD_LEVEL_EXAMPLES | Added MOW-listed `ပေါက်` (`pauk`, `/paʊʔ/`) and `ကျောက်` (`kyauk`, `/t͡ɕaʊʔ/`) for ေါက် and ောက်. Same secondary IPA rime sequence `/aʊʔ/`, different onsets. Added claim `CLM-WIKTIONARY-AUK-WORD-LEVEL-EXAMPLES-001`; updated audit/crosswalk parity and tests. Registry: 80 sources / 140 claims. | Secondary equivalence only; not a controlled minimal pair or primary MLC specification. No IPA gold, runtime or Ukrainian mapping promotion. CI pending. |

Current collision ledger: **15 unadjudicated / 5 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 1 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 140 claims**.

## Additional `a`, `a:` and `au` lexical examples — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-A-AU-LEXICAL-027 | PARTIAL — SECONDARY EVIDENCE RECONCILED | Earlier MOW-listed pairs across `a`, `a:` and `au` remain; `a.` now also has both-side examples: `ငါ့` `/ŋa̰/` (`ါ့`) and first syllable `တာ့` `/ta̰/` in `တာ့တာ` (`ာ့`). Registry: 80 sources / 164 claims. | Secondary only, not a controlled minimal pair or primary MLC adjudication. No IPA gold, runtime or Ukrainian mapping promotion. |

Current collision ledger: **12 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 1 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 143 claims**.

## One-sided `aung.` lexical example — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-AUNG-DOT-LEXICAL-028 | PARTIAL — SECONDARY_ONE_SIDE_ONLY | Added MOW-listed `စောင့်` (`caung.`, `/sa̰ʊɴ/`) for ောင့်. ေါင့် remains unobserved. Added claim `CLM-WIKTIONARY-AUNG-DOT-ONE-SIDE-EXAMPLE-001`; updated audit/crosswalk parity and regression tests. Registry: 80 sources / 144 claims. | Secondary evidence for one side only; not collision adjudication or primary MLC specification. No IPA gold, runtime or Ukrainian mapping promotion. |

Current collision ledger: **11 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 2 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 144 claims**.

## One-sided `um:` and `un` lexical examples — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-UM-UN-LEXICAL-029 | PARTIAL — SECONDARY_ONE_SIDE_ONLY | Added MOW-listed `နှလုံး` (`hna.lum:`, `/n̥əlóʊɴ/`) for `ုံး` and `ကုန်` (`kun`, `/kòʊɴ/`) for `ုန်`. Opposite sides remain unobserved. Added claims `CLM-WIKTIONARY-UM-COLON-ONE-SIDE-EXAMPLE-001` and `CLM-WIKTIONARY-UN-ONE-SIDE-EXAMPLE-001`; updated audit/crosswalk parity and tests. Registry: 80 sources / 146 claims. | Secondary evidence for one side only; not collision adjudication or primary MLC specification. No IPA gold, runtime or Ukrainian mapping promotion. |

Current collision ledger: **9 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 4 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 146 claims**.

## One-sided `au:`, `im` and `im.` lexical examples — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-WIKTIONARY-AU-IM-LEXICAL-030 | PARTIAL — SECONDARY_ONE_SIDE_ONLY | Added MOW-listed `ကျော` (`kyau:`, `/t͡ɕɔ́/`) for ော; `အိမ်` (`im`, `/ʔèɪɴ/`) for ိမ်; and `စိမ့်` (`cim.`, `/sḛɪɴ/`) for ိမ့်. Opposite sides remain unobserved. Added three claims; updated audit/crosswalk parity and regression tests. Registry: 80 sources / 149 claims. | Secondary evidence for one side only; not collision adjudication or primary MLC specification. No IPA gold, runtime or Ukrainian mapping promotion. |

Current collision ledger: **6 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 7 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 149 claims**.

## Final exact-head verification — 2026-11-13

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-RIME-LEXICAL-AUDIT-EXACT-HEAD-031 | DONE_VERIFIED — DATA_AND_TEST_INTEGRITY | SHA `62bea5a26012cb1ace4ce11579e17f4a780c3e1e`; CI **43516197628 SUCCESS** and duplicate exact-SHA run **43516203122 SUCCESS**: 251 Python + 66 subtests, 20 Node, 58 Playwright; build, generated-data freshness and Chromium install passed. Optional raw-output diagnostic **43516203133 SUCCESS**. | Verifies code/data/registry/test integrity only. IPA gold remains 0; accuracy null; all lexical additions remain secondary. One high-severity npm vulnerability remains. |

Final collision ledger: **6 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 7 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 149 claims**.

## `am:` one-side lexical attestation — 2026-11-14

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-RIME-AM-COLON-LEXICAL-025 | PARTIAL — SECONDARY_ONE_SIDE_ONLY | Wiktionary `လမ်း` (`lam:`, `/láɴ/`) ends in `မ်း`; no MOW suffix-match candidate for `ံး` located. Claim `CLM-WIKTIONARY-AM-COLON-ONE-SIDE-EXAMPLE-001` registered; audit, crosswalk and tests updated. | Secondary one-side evidence only; not collision adjudication or primary MLC evidence. No IPA gold, runtime or Ukrainian output promotion. CI pending. |

Current collision ledger: **5 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 8 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 150 claims**.

## Exact-head verification — `am:` lexical continuation — 2026-11-14

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-RIME-AM-COLON-LEXICAL-025 | DONE_VERIFIED — DATA_AND_TEST_INTEGRITY | SHA `73bfbd7d82f69bfa0e306d984a40fe2324fc3515`; required CI runs **43519075644 SUCCESS** and **43519083741 SUCCESS**: 251 Python + 66 subtests, 20 Node, 58 Playwright; build, generated-data freshness and Chromium installation passed. | Confirms registry, crosswalk and test integrity only. IPA gold remains 0; accuracy null; secondary example is one-side-only and not primary MLC adjudication. One high-severity npm vulnerability remains. |

Current collision ledger: **5 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 8 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 150 claims**.

## `am.` secondary lexical distinction — 2026-11-14

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-RIME-AM-DOT-LEXICAL-025 | PARTIAL — SECONDARY_SOURCE_DISTINCTION | Wiktionary `စိမ့်` (`cim.`, `/sḛɪɴ/`) and `ကြံ့` (`kram.`, `/t͡ɕa̰ɴ/`) represent final မ့် and ံ့; claim `CLM-WIKTIONARY-AM-DOT-LEXICAL-DISTINCTION-001` registered. Audit and crosswalk now flag secondary distinction. | Secondary evidence conflicts with vendor MLCTS2/IPA same-output mapping. Not a minimal pair or primary MLC adjudication; no IPA gold, runtime or Ukrainian mapping promotion. CI pending. |

Current collision ledger: **4 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 3 secondary distinction / 8 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 151 claims**.

## `au.` one-side lexical attestation — 2026-11-14

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-RIME-AU-DOT-LEXICAL-025 | PARTIAL — SECONDARY_ONE_SIDE_ONLY | Wiktionary `ဝပ်ရှော့` (`waphrau.`, `/waʔʃɔ̰/`) attests source unit `ော့`; claim `CLM-WIKTIONARY-AU-DOT-ONE-SIDE-EXAMPLE-001` registered. | `ေါ့` remains unobserved; not primary MLC adjudication or collision resolution. No IPA gold, runtime or Ukrainian mapping promotion. CI pending. |

Current ledger: **3 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 3 secondary distinction / 9 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 152 claims**.

## Exact-head verification — `au.` lexical continuation — 2026-11-14

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-RIME-AU-DOT-LEXICAL-025 | DONE_VERIFIED — DATA_AND_TEST_INTEGRITY | SHA `ffd08d7ae8e227ee19a86859de00b7d52f456ecf`; CI **43519887514 SUCCESS**: 251 Python + 66 subtests, 20 Node, 58 Playwright; build, generated-data freshness and Chromium installation passed. | Confirms data/test integrity only. The lexical example is one-side secondary evidence; opposite source unit remains unobserved. IPA gold remains 0; no primary MLC, runtime or Ukrainian mapping promotion. One high-severity npm vulnerability remains. |

Current ledger: **3 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 3 secondary distinction / 9 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 152 claims**.


## `um.` one-side secondary lexical attestation — 2026-11-14

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-RIME-UM-DOT-LEXICAL-025 | PARTIAL — SECONDARY_ONE_SIDE_ONLY | Wiktionary `အုံ့` (`um.`, `/ʔo̰ʊɴ/`) attests ုံ့; claim `CLM-WIKTIONARY-UM-DOT-ONE-SIDE-EXAMPLE-001` registered. Not a MOW suffix candidate. | ုမ့် remains unobserved; secondary evidence only, not primary MLC adjudication or collision resolution. No IPA gold, runtime or Ukrainian mapping promotion. CI pending. |

Current ledger: **2 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 3 secondary distinction / 10 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 153 claims**.


## `im:` secondary compound-level lexical attestation — 2026-11-14

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-RIME-IM-COLON-LEXICAL-025 | PARTIAL — SECONDARY_ONE_SIDE_ONLY | Wiktionary compound `တစ်သဝေမတိမ်း` provides final-component evidence for `တိမ်း` (`tim:`, `/téɪɴ/`); MOW lists `တိမ်း` for ိမ်း. Claim `CLM-WIKTIONARY-IM-COLON-ONE-SIDE-EXAMPLE-001` registered. | Compound IPA is not a standalone entry; ိံး remains unobserved. No primary MLC adjudication, IPA gold, runtime or Ukrainian mapping promotion. CI pending. |

Current ledger: **1 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 3 secondary distinction / 11 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 154 claims**.


## MOW suffix-overlap guard — 2026-11-14

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-MOW-A-DOT-SUFFIX-OVERLAP-025 | DONE_VERIFIED — INTERPRETATION_GUARD | Regression test verifies the only MOW `a.` / `ာ့` suffix match is `ဝပ်ရှော့`, whose full ending is `ော့` and whose Wiktionary entry gives `waphrau.` / `/waʔʃɔ̰/`. | Exact Unicode suffix overlap is not syllabification or phonological-rime evidence. `a.` remains unadjudicated; no data/runtime promotion. |



## Exact-head verification — `im:` / `um.` lexical updates and `a.` suffix guard — 2026-11-14

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-RIME-IM-COLON-LEXICAL-025 / BURMESE-RIME-UM-DOT-LEXICAL-025 / BURMESE-MOW-A-DOT-SUFFIX-OVERLAP-025 | DONE_VERIFIED — DATA_AND_TEST_INTEGRITY | SHA `2b1f306b43a8a6c38e626252fb0b0b9c18501e1b`; CI **43580029898 SUCCESS**: 252 Python + 66 subtests, 20 Node, 58 Playwright; gold-structure validation, build, generated-data freshness and Chromium passed. | Confirms data/test integrity only. Both lexical attestations are secondary and one-sided; `a.` remains unadjudicated. IPA gold remains 0; no primary MLC, runtime or Ukrainian mapping promotion. One high-severity npm vulnerability remains. |

Current ledger: **1 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 3 secondary distinction / 11 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 154 claims**.


## `a.` phonetic-literature boundary — 2026-11-14

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-RIME-A-DOT-PHONETIC-CONTEXT-026 | DONE_VERIFIED — SOURCE_SCOPE_GUARD | Full texts: Mooney & Repetti-Ludlow (2021), DOI 10.3765/PLSA.V6I1.4900; Watkins (2001), DOI 10.1017/S0025100301002122. | Both provide phonetic vowel/rhyme context but no Burmese spelling-to-MLCTS mapping for the relevant examples. `a.` remains unadjudicated; no runtime promotion. |


## `a.` secondary one-side attestation — 2026-11-14

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-RIME-A-DOT-ONE-SIDE-027 | DONE_VERIFIED — SECONDARY_ONE_SIDE_ONLY | Wiktionary `ငါ့`: IPA `/ŋa̰/`, MLCTS `nga.`, source ending `ါ့`; explicitly a non-lemma induced creaky pronoun form. | Only first source-unit side attested; no lexical `ာ့` example and no primary MLC adjudication. No runtime promotion. |

Updated 25-group distribution: **0 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 3 secondary distinction / 12 secondary one-side-only / 1 special non-rime**. Source registry: **80 sources / 157 claims**.


## `a.` both-side secondary lexical equivalence — 2026-11-14

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-RIME-A-DOT-BOTH-SIDES-028 | DONE_VERIFIED — SECONDARY_SYSTEM_EQUIVALENCE | Wiktionary `ငါ့` `/ŋa̰/`, MLCTS `nga.` (`ါ့`) and `တာ့တာ` `/ta̰tà/`, MLCTS `ta.ta`, with first syllable `တာ့` (`ာ့`). | Both source units represented, same `/a̰/` rime; not a controlled minimal pair and not primary MLC adjudication. No runtime promotion. |

Updated 25-group distribution: **0 unadjudicated / 9 secondary equivalence / 1 secondary conflict / 3 secondary distinction / 11 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 158 claims**.


## Final exact-head CI and lexical ledger — 2026-11-14

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-RIME-LEXICAL-AUDIT-025 | DONE_VERIFIED — SECONDARY_EVIDENCE_LEDGER | Final SHA `e6d865e1daa191a7ecc9cd5b0025b628cc930310`; CI **43581081561 SUCCESS**: 253 Python + 66 subtests, 20 Node, 58 Playwright; build, generated-data freshness, Chromium, IPA-gold structure validation passed. | Evidence ledger integrity only. 0 groups remain without any lexical evidence, but 11 groups are still one-sided, 1 conflicting and 3 source-distinguished; all evidence is secondary. No primary MLC adjudication or runtime promotion. |
| BURMESE-RAW-G2P-DIAGNOSTICS-001 | DONE_VERIFIED — RAW_OUTPUT_ONLY | Optional run **43581085495 SUCCESS**; CRF 100 predictions / 84 source-concordant / 0 gold / `NOT_SCORED_POSSIBLE_TRAINING_OVERLAP`; Epitran raw output artifact. | No accuracy estimate. Diagnostic outputs are not gold or held-out benchmark results. |

Current ledger: **0 unadjudicated / 9 secondary equivalence / 1 secondary conflict / 3 secondary distinction / 11 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 158 claims**. Gold: 0. One high-severity npm vulnerability remains.


## Research-source reconciliation and engine integration — 2026-11-14

- Full-text Undermind review of Thu et al. (2016), Oo et al. (2020), and Hlaing (2014) corrected the evidence ledger: WSSANLP open-set PER 14.7/11.4/15.7 (WFST), 15.7 CRF tie on open3; LREC Thrax/OpenFst paper-reported 195 states/2,966 arcs and 88-symbol inventory; Hlaing 11,732 words, 99.93% orthographic segmentation accuracy with 32,238 vs 32,283 syllable-count discrepancy and 8-vs-9 stacking-error discrepancy. Source claims explicitly distinguish these from project IPA accuracy.
- PR #129 was inspected (21 files, 53 commits ahead/17 behind, non-mergeable); its useful work was selectively ported rather than blindly merged: candidate-only hybrid API, Google WFST raw-output harness/optional CI, and medials/conjunct/kinzi IPA withholding. PR #129 remains open/draft/untouched.
- Current branch now has an explicit candidate-only provider API; deterministic rule engine remains final authority. No external provider auto-runs and no provider output is promoted.


## External G2P raw-output artifacts — 2026-11-14

| Claim | Status | Result | Limit |
|---|---|---|---|
| CLM-GOOGLE-WFST-RAW-SMOKE-2026-11-14 | TESTED | Workflow 43582075278: build/symbol checks passed, 6/6 structural-only outputs, report SHA `88372233d85df73593b030ee0f91aa678fe86fd1c6d5cdc18e7c609b8eefd2c6`. | 0 gold, accuracy null. |
| CLM-EPITRAN-RAW-SMOKE-2026-11-14 | TESTED | Epitran 1.35.3, six structural-only raw outputs, report SHA `a7d93e0f04b4f4822094a36760c5376cb596db31a710aae4cdcacd14213d0b69`. | 0 gold, accuracy null. |
| CLM-CRF-MYG2P-RAW-SMOKE-2026-11-14 | TESTED | 100 predictions, 84 source-concordant, report SHA `741dc7fa1263e667cb1c51f91f7ee0a24b0bd6c2479d1efafe63798a63d73d20`. | 0 gold; possible training overlap; no accuracy. |

Current registry: **80 sources / 164 claims**. The 25-group rime ledger remains 0 unadjudicated / 9 secondary equivalence / 1 conflict / 3 distinctions / 11 one-side-only / 1 special non-rime. Independent IPA gold remains 0.


## Final exact-head diagnostic evidence — 2026-11-14

| Claim | Status | Result | Boundary |
|---|---|---|---|
| Google WFST | ESTABLISHED — RAW OUTPUT ONLY | Workflow 43582678434: 6/6 structural-only outputs, report SHA `541dbe0d70074819d006548d5eb7543822e3dae9508c47e598f08504f8d3340b`. | 0 gold; accuracy null. |
| Epitran 1.35.3 | ESTABLISHED — RAW OUTPUT ONLY | Six structural-only raw outputs, report SHA `a582039d46764f07ed509076ca0fb1542d6bdb4a358dc46aa0ad600bbbb88521`. | 0 gold; accuracy null. |
| Burmese-G2P CRF | ESTABLISHED — RAW OUTPUT ONLY | 100/100 predictions, 84 source-concordant, report SHA `741dc7fa1263e667cb1c51f91f7ee0a24b0bd6c2479d1efafe63798a63d73d20`. | 0 gold; possible training overlap; supplied syllable boundaries. |

Registry: **80 sources / 164 claims**; no independent IPA gold.


## Full-text source scope additions — 2026-11-14

Five claims added after full-text review of Hlaing & Mikami (2014), Watkins (2001), and Oo et al. (2020):

- `CLM-HLAING14-GRAMMAR-EXPR-001`: Hlaing & Mikami's orthographic FST expressions disagree on whether medials/vowels can repeat (`M? V?`, `M* V*`, and implementation `Opt(M) Opt(V)`). Preserve as a source-specification inconsistency; it is not a phonological rule.
- `CLM-HLAING14-LICENSE-001`: the paper states no reuse license for the MLC orthography corpus, digitized test words or transducer/code.
- `CLM-WATKINS2001-SPEAKER-SCOPE-001`: Watkins' broad transcription is based on one Rangoon male consultant reading deliberately; useful IPA description, not population-validated Yangon gold.
- `CLM-WATKINS2001-CODA-001`: Watkins' /ʔ/-only coda analysis and vowel subsets remain source-specific; no universal runtime promotion.
- `CLM-OO20-NO-GOLD-001`: Oo et al.'s IPA G2P creates seed pronunciations for checking; SLR80 is manually segmented Burmese text, not word-level IPA gold.

Registry: **80 sources / 169 claims**. None of these claims creates independent adjudicated gold or promotes runtime/Ukrainian output.


## `un` two-sided lexical evidence — 2026-11-14

- `CLM-WIKTIONARY-UN-SECOND-SIDE-EXAMPLE-001` records `ဂုဏ်` /ɡòuɴ/ from the Burmese pronunciation appendix and compound-initial `ဂုဏ်` /ɡòʊɴ/ from `ဂုဏ်ထူး` (MLCTS `gunhtu:`), complementing MOW-listed `ကုန်` /kòʊɴ` for the other orthographic source unit.
- `un` is now `SECONDARY_SYSTEM_EQUIVALENCE`, not primary adjudication and not a controlled minimal pair. No runtime/Ukrainian promotion.
- Registry: **80 sources / 170 claims**. 25-group distribution: **0 unadjudicated / 10 secondary equivalence / 1 secondary conflict / 3 secondary distinction / 10 secondary one-side-only / 1 special non-rime**.


## Exact final test verification — 2026-11-14

The `un` second-side lexical addition and regression changes passed exact-head required CI **43585743620 SUCCESS** on `1ce829eda10ae5c3b3e4b9772efb434043198a75`: 267 Python + 68 subtests, 20 Node, 58 Playwright; npm ci and explicit high-severity audit passed with 0 vulnerabilities. IPA gold remains 0; validator `NOT_READY_NO_ADJUDICATED_GOLD`. Registry 80 sources / 170 claims; rime ledger 0 unadjudicated / 10 secondary equivalence / 1 conflict / 3 distinctions / 10 one-side-only / 1 special non-rime.


## `au:` and `au.` two-sided secondary evidence — 2026-11-14

- `CLM-WIKTIONARY-AU-COLON-SECOND-SIDE-EXAMPLE-001`: `ပေါ` `/pɔ́/`, MLCTS `pau:`, source `ေါ`; complements `ကျော` `/t͡ɕɔ́/`, MLCTS `kyau:`, source `ော`.
- `CLM-WIKTIONARY-AU-DOT-SECOND-SIDE-EXAMPLE-001`: `ပေါ့` `/pɔ̰/`, MLCTS `pau.`, source `ေါ့`; complements final syllable of `ဝပ်ရှော့` `/ʃɔ̰/`, MLCTS `waphrau.`, source `ော့`.
- Both groups are `SECONDARY_SYSTEM_EQUIVALENCE` only. `ပေါ့` is not a MOW suffix-match candidate. Neither claim is a minimal pair or primary MLC adjudication.
- Registry: **80 sources / 172 claims**. 25-group distribution: **0 unadjudicated / 12 secondary equivalence / 1 conflict / 3 distinctions / 8 one-side-only / 1 special non-rime**.
- Required CI **43586334287 SUCCESS** on `dd494662f0c94bcf1f59170fe65ea6cd41199c64`: 267 Python + 68 subtests, 20 Node, 58 Playwright; npm audit 0 vulnerabilities.


## MLC dictionary access and secondary rime-table follow-up — 2026-11-14

- Added `GOOGLE_BOOKS_MLC1996_DIGITIZED`: Google Books identifies the 1996 Dunwoody Press reprint of the 1993 MLC Myanmar-English Dictionary as originating from the University of Michigan and digitized on 2008-05-15 (635 pages). The retrieved record is bibliographic metadata only; no page-level content, pronunciation key or MLCTS/MLCTS2 table was inspected.
- Added `SHACHI_SEALANG_DICT_2009`: independent resource metadata confirms that SEAlang's ~35,000-entry Burmese dictionary is based on the 1993 MLC dictionary (1996 reprint), supports IPA phonetic search/display, and carries copyright attribution for the MLC/Dunwoody source. It does not disclose record-level fields or prove whether entries store MLCTS or MLCTS2.
- Added `CLM-WIKTIONARY-KI-SECONDARY-RIME-TABLE-001`: Wiktionary's secondary rime table lists `ကိံ` /kèɪɴ/ MLCTS `kim` alongside `ကိမ်`. This is table-level evidence for the second orthographic side of `im`, not a lexical entry. It does **not** satisfy the lexical two-sided acceptance criterion; the `im` lexical audit status is unchanged.
- Direct SEAlang dictionary retrieval still returned HTTP 502 / inaccessible through the available web route; the historical API request endpoint was also inaccessible. No MLC entry text or internal schema was obtained.
- Registry totals: **82 sources / 175 claims**. The 25-group lexical audit remains **12 secondary equivalence / 1 secondary conflict / 3 secondary distinctions / 8 secondary one-side-only / 1 special non-rime**. No primary MLC adjudication, runtime mapping or Ukrainian candidate was promoted.
- New regression test protects the distinction between catalog/interface metadata, table-level rime evidence and lexical/primary-source acceptance. Exact-head CI must be checked after these changes; no test result is claimed here.
