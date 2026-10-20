# Burmese → Ukrainian: Master Execution Plan and Chat Handoff

Last reviewed: 2026-10-20
Repository: https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-
Default branch used for this review: repository default (previously reported as `main`; branch head SHA was not exposed by the available file-fetch response).
Working title: “Burmese-to-Ukrainian Transcription: Graphemic Analysis and an Evidence-Gated Phonological Model”.

## Operating rule

Do not describe the current implementation as a complete phonetic transcription engine. The inspected `ipa.py` contains a small, direct onset/vowel seed map and emits `?` for absent vowel analysis; its output status is `conservative_partial` or `analysis_dependent`. The parser is explicitly structural. The repository is currently best described as a **structural graphemic/syllabic parser with a conservative partial IPA seed layer and a separate practical Ukrainian correspondence layer**. This is not yet a complete phonological analysis or surface-phonetic transcription model.

## Latest verified repository evidence

Read on 2026-10-20:
- `README.md` (blob SHA `6ff0e347b553515372e2646271a229905faac28a`)
- `pyproject.toml` (blob SHA `11f6f48f3e79bb183af29a1d43039438268cc5a1`)
- `src/burmese_ukrainian/parser.py` (blob SHA `bb5c52a6d7a2fa36eb6172cf66232449ec57f701`)
- `src/burmese_ukrainian/unicode.py` (blob SHA `2bd992a35da001b46c4e9835f4ef40f74623ec05`)
- `src/burmese_ukrainian/model.py` (blob SHA `eb167ae15f73089c4bfa58f5ceba47db3f27aa55`)
- `src/burmese_ukrainian/ipa.py` (blob SHA `6769c01f148b797b6d4a0bd9e8180bc39d268931`)
- `src/burmese_ukrainian/practical.py` (blob SHA `63528876198a3cd0d60bab2e847b103ce80c81a5`)
- `src/burmese_ukrainian/__init__.py` (blob SHA `0504c70084baa3b95b70078ce17d5f12de2c79a7`)
- `tests/test_parser.py` (blob SHA `8d395d60138fbeec5931bb2ade1212bcbc09f1d`)
- `tests/test_practical.py` (blob SHA `98f68effde325ed20c51a7d5c73bfaed71ea1fe4`)
- `docs/practical-transcription.md` (blob SHA `989b30829c9c02161863056416f7064c0b6b40fe`)
- `docs/russian-vs-ukrainian.md` (blob SHA `5bbdeecb4b3f4e69cdbc0c089cb2cdfcb828cdcd`)

The expected handoff paths `docs/audits/current/MASTER-EXECUTION-PLAN-AND-CHAT-HANDOFF.md`, `docs/MASTER-EXECUTION-PLAN-AND-CHAT-HANDOFF.md`, and `CITATION.cff` returned not found during this review. The expected `.github/workflows/ci.yml` path also returned not found; inspect actual workflow filenames before making any CI claims.

Historical context (not reverified against current branch): on 2026-10-09, prior work reported fixes to `ေ`/`ော်`, `ကြည်`, `ြ`, `စွယ်`, contextual /j/, separate phonetic/Ukrainian statuses, diagnostics, and Unicode code-point handling; Python/build/unit/browser CI was reported passing at that time. Live GitHub Pages deployment was still to be confirmed, including adversarial cases `ကေ`, `ကော်`, `ကြည်`, `စွယ်`, `မြန်`, `ယူ`. Treat these as historical leads, not current verification.

## Layer audit (current evidence-based assessment)

| Layer | Status | Evidence / gap |
|---|---|---|
| 1. Unicode normalization and grapheme structure | IN_PROGRESS | `unicode.py` supports NFC/NFD/NFKC/NFKD and a Myanmar-range predicate. Parser normalizes input and segments runs conservatively. Need test normalization equivalence, Unicode block edge cases, punctuation/mixed scripts, and cluster boundaries. |
| 2. Kinzi, medials, conjuncts, mark order | IN_PROGRESS | Kinzi sequence and four medials are represented; parser handles virama/subjoined consonants. Structural tests are sparse. Do not infer pronunciation from structural recognition alone. |
| 3. Vowels and contextual realizations | TODO | `ipa.py` maps only a small set of parser vowel IDs directly. Complete vowel combinations and contextual/inherent-vowel derivation are explicitly not established. |
| 4. Codas and checked syllables | TODO | Model has a coda field, but inspected IPA layer does not implement a complete coda/checked-syllable realization. |
| 5. Tone | TODO | Model contains tone/prosody slots; README says competing analyses are retained. No complete tone derivation should be claimed. |
| 6. Phonation contrasts | TODO | No complete evidence-gated implementation verified. |
| 7. Allophony/contextual realization | TODO | No complete phonological-rule engine verified. |
| 8. IPA | IN_PROGRESS | Partial seed mapping exists. It is not a complete broad IPA system and does not constitute validated surface phonetics. Audit the entire mapping and status semantics. |
| 9. Ukrainian adaptation | IN_PROGRESS | Separate table-driven layer exists with explicit uncertain/not-established outcomes. Its inputs must be validated IPA, not guessed values; test independent from IPA. |
| 10. Unknown/ambiguous/unsupported inputs | IN_PROGRESS | Parser has malformed/unsupported states; practical layer returns `not_established` for unmapped IPA. Ensure all APIs consistently preserve unknowns and never present placeholders as confident output. |
| 11. Sources, tests, docs, UI, CI, deployment | IN_PROGRESS | Source bibliography and practical documentation exist; handoff and citation file not found at expected paths. Current workflow names, full tests, UI/mobile behavior, Pages deployment, license/data provenance remain unverified in this audit. |

## Prioritized task registry

Statuses allowed: `TODO`, `IN_PROGRESS`, `BLOCKED`, `DONE_VERIFIED`, `DEFERRED`, `NOT_APPLICABLE`.

### Gate 0 — repository integrity and reproducibility
- **BUR-001 — IN_PROGRESS — P0 — Establish reproducible baseline.** Identify actual default branch/head commit, list repository tree, find workflows and handoff/audit/source registry; run tests and build against that exact commit. Acceptance: commit SHA and exact commands/results recorded. Dependency: none.
- **BUR-002 — TODO — P0 — Inspect actual CI workflow and deployment configuration.** Acceptance: workflow paths, triggers, latest run/check results, Pages source and live URL status evidenced; no assumptions from old reports. Depends on BUR-001.
- **BUR-003 — TODO — P0 — Add/maintain this handoff after every work cycle.** Acceptance: exact commit/branch, evidence read, edits, commands/results, IDs, blockers, next command kept current.

### Stage A — scientifically honest research prototype
- **BUR-010 — IN_PROGRESS — P0 — Harden Unicode and grapheme segmentation.** Test NFC/NFD equivalence, Myanmar block boundaries, mixed-script text, punctuation, malformed virama, reordered marks and adversarial cluster sequences. Acceptance: no crashes or silent deletion; stable, documented segmentation; regressions for each confirmed bug. Depends on BUR-001.
- **BUR-011 — IN_PROGRESS — P0 — Validate kinzi/medial/conjunct parsing.** Build independent fixtures for all four medials, kinzi, subjoined consonants, legal and malformed mark sequences. Acceptance: structural fields and diagnostics match explicit fixture expectations. Depends on BUR-010.
- **BUR-012 — TODO — P0 — Make analysis layers and confidence explicit in API output.** Distinguish graphemic status, phonological status, IPA status and Ukrainian adaptation status; no successful build or parse implies phonological certainty. Acceptance: schema/tests demonstrate independent status fields and uncertainty propagation. Depends on BUR-010.
- **BUR-013 — TODO — P1 — Create an independent adversarial regression corpus.** Include `ကေ`, `ကော်`, `ကြည်`, `စွယ်`, `မြန်`, `ယူ`, all medials, kinzi, vowel combinations, codas, tone marks, mixed scripts, loanwords, names, malformed inputs. Every expected phonetic output needs a source and confidence; structural-only cases must be labeled as such. Depends on BUR-010/BUR-011.
- **BUR-014 — TODO — P1 — Keep IPA explicitly partial and evidence-gated.** Unsupported sequences return unknown/analysis-dependent rather than plausible invented IPA. Acceptance: rule table ties each implemented mapping to source, scope, confidence, counterexamples/limits and tests. Depends on BUR-012.
- **BUR-015 — TODO — P1 — Audit Ukrainian adaptation independently.** Validate each IPA-to-Ukrainian correspondence as a target-language policy; retain hypotheses such as /h/ → г and /ɯ/ → и as hypotheses unless evidence supports them. Acceptance: table-driven tests cover mapped, uncertain and unknown inputs. Depends on BUR-014.
- **BUR-016 — TODO — P1 — Document prototype scope and limitations in UI and README.** State that the prototype parses graphemic structure and provides a limited IPA seed, not complete phonetic transcription. Acceptance: UI/API/README terminology is consistent. Depends on BUR-012.
- **BUR-017 — TODO — P1 — Verify source and data provenance.** Record bibliographic metadata, stable URLs/DOIs/pages where available, license/permission and source-to-rule links. Acceptance: no unsupported rule is presented as established; data licensing is documented.

### Stage B — expanded evidence-backed phonological model
- **BUR-020 — TODO — P2 — Complete vowel/rime and inherent-vowel derivation.** Source-backed inventory and context-conditioned rules; lexical exceptions explicit. Depends on BUR-017 and Stage A corpus.
- **BUR-021 — TODO — P2 — Model codas and checked syllables.** Explicit orthographic coda classes and evidence-backed surface outcomes. Depends on BUR-020.
- **BUR-022 — TODO — P2 — Model tone/register/phonation alternatives.** Preserve disputed analyses rather than averaging them; define dialect/speaker scope and the evidence that resolves each branch. Depends on BUR-017.
- **BUR-023 — TODO — P2 — Add contextual phonological and allophonic rules.** Every rule must specify domain, ordering/interaction, exceptions, confidence and evidence. Depends on BUR-020/BUR-021/BUR-022.
- **BUR-024 — TODO — P2 — Validate against independent lexical/audio or expert-annotated data.** Separate train/development fixtures from held-out evaluation. Do not claim measured accuracy without a defined reference set and reproducible scoring. Depends on BUR-020–BUR-023.
- **BUR-025 — TODO — P2 — Publish reproducible release.** Fix version, changelog, `CITATION.cff`, license, methods/limitations note, tagged release and Zenodo archive only after repository provenance and release metadata are verified. Depends on BUR-001, BUR-017, and selected release scope.

## Scientific rules of engagement
1. Unicode documentation supports encoding and script mechanics, not by itself the phonological value of every spelling.
2. Keep graphemic parsing, phonological representation, phonetic realization, broad IPA, and Ukrainian practical orthography as separate stages.
3. Do not infer tone, phonation, or allophony from a grapheme pattern unless a source explicitly supports that inference.
4. Every implemented phonetic rule should have source, scope/dialect, confidence/status, counterexamples/limits and regression coverage.
5. Unknown is a valid output. Do not use a successful parser/build as evidence of phonetic completeness.
6. Historical CI claims and old branch notes must be rerun/rechecked before being described as current.

## Checks run in this cycle

- GitHub file fetch: README, pyproject, parser, Unicode module, model, IPA seed, package exports, practical adapter, parser tests, practical tests, practical-transcription documentation, Russian-vs-Ukrainian documentation — successful reads.
- Expected handoff paths and `CITATION.cff` — not found.
- `.github/workflows/ci.yml` — not found at that exact path; workflow discovery still required.
- Local test suite/build: NOT RUN in this environment.
- Current commit/head SHA, latest CI run, live Pages deployment: NOT VERIFIED in this cycle.

## Exact next step

Run BUR-001: enumerate the current repository tree and branch head; locate the real audit/handoff/source registry, test and workflow files; then run the suite/build against the exact commit and update this registry with results. Do not start broad phonological expansion until parser and baseline evidence are reproducible.
