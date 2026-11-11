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


## Burmese external pronunciation/audio source audit — 2026-11-04

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BURMESE-MYG2P-SOURCE-001 | DONE_VERIFIED (source pinned and provenance/rights documented; no import) | Upstream `ye-kyaw-thu/myG2P` revision `54b5c76bb5a87fdbaaeddc1892e6ebd8f97ee225`; Version 2.0 file `ver2/myg2p.ver2.0.txt`, 2,329,808 bytes, Git blob SHA `0b2735f9a6f7fe28ae94c4baaf323d1db3015c3b`, five tab-separated fields including IPA; CC BY-NC-SA 4.0. Registered as `MYG2P2026`. | External diagnostic/comparator only. Non-commercial/share-alike terms, per-entry provenance, dialect and IPA convention must be respected. Existing test-only probe does not become gold or production approval. |
| BURMESE-OPENSLR80-AUDIO-001 | PARTIAL (audio source registered; pilot not performed) | OpenSLR SLR80 provider record lists CC BY-SA 4.0; manually quality-checked Burmese volunteer sentence audio and orthographic transcripts; visible female subset includes 541 KB index and 948 MB WAV archive. Registered as `OPENSLR80`. | No IPA labels; dialect/profile not sufficiently established. Any pilot requires specialist screening, exact provider locators, blind double IPA annotation and independent adjudication; assess share-alike before publishing derived labels. |

**Evidence boundary:** source records and provenance tests are complete; no external dictionary or audio was imported. Independent adjudicated Burmese IPA gold remains 0; accuracy remains null.


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


## External G2P and hybrid candidate integration — 2026-11-11

| Task | Status | Evidence | Remaining acceptance criterion |
|---|---|---|---|
| BUR-GOOGLE-WFST-CANDIDATE-001 | PARTIAL | Pinned Thrax/OpenFst grammar built; 6/6 structural-only probes emitted outputs; independent gold 0. | Independent Yangon-profile IPA gold, tone/phonation adjudication and full transitive dependency pins. |
| BUR-EPITRAN-CANDIDATE-001 | PARTIAL | Epitran 1.35.3 returned 6/6 raw outputs on structural-only probes; independent gold 0. | Compare against independent gold and validate the Burmese IPA profile before promotion. |
| BUR-MYG2P-LEXICON-CANDIDATE-001 | PARTIAL | 24,009 unique dictionary entries; exact IPA-column adapter added. Prior source-concordance results are not independent accuracy and may overlap training data. | Rights review, no-overlap proof, dialect/convention mapping, and independent Yangon-profile gold. |
| BUR-HYBRID-CANDIDATE-ENGINE-001 | PARTIAL | HybridBurmeseEngine exports deterministic rules as final-output authority and exposes Google WFST, myG2P, Epitran and CLI candidates with provenance. Regression tests added. | Exact-head CI and independent adjudicated gold before external candidate promotion. |


### Verification checkpoint — MYA-HYBRID-CANDIDATE-ENGINE-001

Engineering implementation is DONE_VERIFIED on code-bearing head 17c855307be36a0735f0cd8967b988fe62053d8a: tests [43077670284](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43077670284) SUCCESS (183 Python tests + 72 subtests, npm build, generated-data drift, npm tests and 54 Playwright tests). The optional WFST comparator rerun [43077670322](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43077670322) still has its Google build job running; previous WFST smoke [42999264514](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/42999264514) succeeded. Linguistic promotion remains PARTIAL; independent Yangon-profile IPA gold is absent.


Google WFST rerun [43077670322](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43077670322) completed SUCCESS: pinned grammar built, symbol-table checks passed and 6/6 structural-only inputs produced non-empty output. Accuracy remains null because independent gold is 0.


Epitran hybrid adapter refinement: the optional Burmese adapter now explicitly requests tones=True by default and records the requested setting in candidate provenance. Regression test added; exact-head pytest passed in [43078675807](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43078675807). This does not retroactively change the earlier Epitran raw-output benchmark (which used the original smoke harness), nor establish tonal accuracy.


Latest tone-aware hybrid code verification: [43078675807](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43078675807) SUCCESS — 184 Python tests + 72 subtests, npm build, generated-data drift check, npm tests and 54 built-site Playwright tests. The final branch commit 90ec9cba295cca29c1e05b0d71d35c98f653a8ef changes documentation only. Latest optional WFST rerun 43078675829 still building at final checkpoint; prior full run 43077670322 succeeded with 6/6 raw structural probes.


## Hybrid provider-priority verification — 2026-11-11

| Task | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BUR-HYBRID-PROVIDER-PRIORITY-001 | DONE_VERIFIED (engineering ordering only) | Provider order is myG2P 10 → Google WFST 20 → Epitran 40 → CRF 60 → Goruut 90; unknown providers 50. Exact-head CI [43080511259](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43080511259) SUCCESS (185 Python tests + 72 subtests; npm build, generated-data freshness, npm tests, 54 Playwright tests); optional candidate jobs [43080510989](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43080510989) SUCCESS. | Order is diagnostic, not an accuracy ranking or promotion rule. RuleBasedBurmeseEngine remains final authority; gold=0, accuracy=null. |


## Burmese CLI adapter input-framing fix — 2026-11-11

| Task | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BUR-CLI-NEWLINE-001 | DONE_VERIFIED (unit/CI contract); live Goruut E2E BLOCKED | Regression test captures subprocess stdin. RED [43081924723](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43081924723): 1 failed as expected. Fix `fea872b176fabaddf4f0c5ff4121dcf722590ef7`; exact-head CI [43082016024](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43082016024) SUCCESS: 185 Python tests + 72 subtests and 54 browser tests. | Generic CLI adapter now appends an actual newline rather than literal `\\n`. Live Goruut smoke still depends on upstream publication/documentation of `weights9.bin.zlib`; no IPA accuracy is implied. |


## Burmese unsupported medial/stack/kinzi IPA withholding — 2026-11-11

| Task | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BUR-MEDIAL-STACK-KINZI-WITHHOLD-001 | DONE_VERIFIED (fail-closed behavior) | Regression test checks medial `ကြွေ`, stacked consonant `က္ကာ` and kinzi `င်္ဂါ`. RED [43082483864](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43082483864) confirmed medial omission; fix `20ef6ca711093b8422c7b4d3bdce0dcd5023d3de`; exact-head CI [43082565716](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43082565716) SUCCESS: 186 tests + 72 subtests and 54 browser tests. | The adapter withholds IPA for medials, conjuncts and kinzi until their Yangon-profile phonetic realizations are established. This is not a gold score or a new rule. |


## Final Burmese branch verification — 2026-11-11

| Task | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| BUR-FINAL-PR-HEAD-001 | DONE_VERIFIED (repository/CI snapshot) | PR #129 head `0b6368cab8871271c6c0a1684d926c5ec0bc3826`, open draft, 52 ahead / 0 behind current main, no reviews/comments. Required CI [43083942317](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43083942317) SUCCESS (187 tests + 72 subtests, build, generated-data, npm, 54 Playwright); optional diagnostics [43083942349](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43083942349) SUCCESS. | Not merged/published. Accuracy remains unmeasured (gold=0). Candidate providers remain diagnostic only; no output promotion. |
