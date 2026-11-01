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
