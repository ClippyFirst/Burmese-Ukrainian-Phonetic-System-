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

The expected handoff paths `docs/audits/current/MASTER-EXECUTION-PLAN-AND-CHAT-HANDOFF.md`, `docs/MASTER-EXECUTION-PLAN-AND-CHAT-HANDOFF.md`, and `CITATION.cff` returned not found during this review. The expected `.github/workflows/ci.yml` path returned not found. Actual `.github/workflows/pages.yml` exists and runs Node 22.12.0, `npm run build`, `npm test`, and `npm run test:browser` before deployment. Python tests also exist, but this Pages workflow does not run `pytest`; discover whether a separate Python workflow exists.

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
| 11. Sources, tests, docs, UI, CI, deployment | IN_PROGRESS | Practical documentation exists; `CITATION.cff` and a sources file at `docs/sources.md` were not found. `.github/workflows/pages.yml` runs Node build/unit/browser tests but not Python pytest. Current run results, mobile behavior, Pages deployment, license/data provenance remain unverified. |

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
- `.github/workflows/ci.yml` — not found at that exact path.
- `.github/workflows/pages.yml` — verified; latest run `39482511514` on `main` commit `e5bbf24049ec5bb7f6480435e2ea3e07f3e236b8` succeeded, including build, Node tests, browser tests, artifact upload and deployment.
- `package.json` — version 0.2.2; scripts include `build`, `test`, `test:browser`, `validate:data`, and `check`.
- `tests/test_unicode.py` — basic NFC idempotence, dependent-e vowel segmentation and kinzi segmentation tests exist.
- Local test suite/build: NOT RUN in this environment. The remote connector did not expose a local checkout or execute commands.
- Current repository HEAD is `main` at `e5bbf24049ec5bb7f6480435e2ea3e07f3e236b8`. The latest `tests` run `39482511445` succeeded and explicitly passed `pytest`, `npm run build`, `npm test`, and `npm run test:browser`. The latest Pages run `39482511514` succeeded through deployment. This verifies CI and deploy workflow completion, not the linguistic correctness of every IPA result.

## Exact next step

BUR-001 is now `DONE_VERIFIED` for repository/tree/workflow discovery and remote CI baseline. Next: inspect the two separate runtime paths (Python library vs browser engine), then add shared golden/adversarial fixtures so both paths have comparable, explicitly scoped expected outputs. Do not claim phonetic completeness or merge old divergent branches wholesale.


## Audit cycle 2026-10-20 — verified baseline and branch reconciliation

### Verified repository state

- Default branch: `main`; current head `e5bbf24049ec5bb7f6480435e2ea3e07f3e236b8`.
- Repository tree fetched recursively; no truncation reported.
- Current files include both `.github/workflows/test.yml` and `.github/workflows/pages.yml`.
- Latest test run: [39482511445](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39482511445) — success. Verified steps include `pytest`, `npm run build`, `npm test`, and `npm run test:browser`.
- Latest Pages run: [39482511514](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39482511514) — success. Both build and deploy jobs succeeded; browser test, artifact upload and deployment steps all succeeded.
- `CITATION.cff` is absent from the current recursive tree. A top-level `docs/references.md`, `data/burmese/sources.csv`, and `data/burmese/source_claims.csv` do exist. The source registry is therefore not absent; it was previously checked at the wrong path/name.

### Branch reconciliation

- `fix/adversarial-burmese-phonology`: graph diverged from `main` (11 commits ahead, 3 behind), but its current `src/web/app.js` and `tests/browser/converter.spec.js` blob SHAs match `main` exactly. Do not merge this branch just to retrieve those files; no unique file changes were established in the compared runtime/test files.
- `final-hardening`: diverged and stale relative to `main` (6 commits ahead, 47 behind); only a small set of UI/spec/test files differ in the comparison. No wholesale merge recommended.
- `service-ready`: substantially diverged and stale (33 commits ahead, 50 behind), with older build/workflow/data/UI additions. Treat as historical source for selective review only, not a merge candidate.
- Branch counts are GitHub compare metadata; they are not a measure of correctness.

### Important architecture finding — duplicated runtime engines

The browser converter in `src/web/app.js` contains its own syllable segmentation, contextual rime logic, IPA derivation and Ukrainian rendering. It imports generated data tables, but the central contextual phonology logic is handwritten in JavaScript.

The Python package's `src/burmese_ukrainian/ipa.py` is a much smaller seed mapper: onset plus vowel-sign concatenation, with `conservative_partial` / `analysis_dependent` status. The Python `parser.py` is structural and does not implement the browser's contextual phonology rules. Therefore the browser and Python APIs are not yet two interfaces to one authoritative phonology engine; they have materially different coverage and can disagree on the same Burmese input.

This is the most important reproducibility risk after confirming CI: passing both suites does not establish that the two runtimes implement the same linguistic model. Resolve it before broadening the rule inventory.

### Evidence and coverage findings

- `docs/methodology.md` and `docs/limitations.md` correctly state that the system is incomplete and should preserve uncertainty.
- `data/burmese/coverage.csv` marks several areas partial, including vowels, vowel structures, finals, phonological rules, IPA and Ukrainian correspondences. Prosody/phonation have analytical metadata but only partial testing; do not infer tone or surface phonation from orthography alone.
- `data/burmese/sources.csv`, `source_claims.csv`, `analyses.csv` and `tone_analyses.csv` exist. However, the present claim registry is small compared with the runtime's many contextual exceptions. Before promoting a rule's status, each implemented exception needs traceable source, scope/dialect, uncertainty and a counterexample/limit note.
- `tests/adversarial/README.md` lists useful required categories (canonical order, kinzi, malformed virama, asat ambiguity, medial combinations, unsupported Myanmar-script material, Pali/Sanskrit, mixed scripts, spaces and U+200B), but the current named browser regression cases do not yet constitute a complete gold-standard lexical benchmark.

### Task status update

- BUR-001 — `DONE_VERIFIED`: recursive tree, default branch/head, workflows and current remote CI results checked.
- BUR-002 — `DONE_VERIFIED`: latest Pages build and deploy jobs succeeded; latest Python/Node/browser test workflow succeeded. Live URL response itself has not been independently fetched, so mark public page content verification as separate follow-up rather than assume it.
- BUR-003 — `IN_PROGRESS`: this handoff updated with baseline and branch findings.
- New P0: add a shared, versioned golden/adversarial fixture format consumed by both runtimes; compare graphemic boundaries, phonological status, IPA and Ukrainian-candidate status separately.
- New P0: make Python and browser runtime ownership explicit. Preferred long-term design is one authoritative rule engine or generated common rule data with contract tests; do not silently claim parity before a differential test demonstrates it.
- New P1: link every high-impact contextual IPA rule to one or more source claims and an explicitly limited scope; where no reliable source is found, retain a proposal/uncertain status.
- New P1: add a reproducible lexical benchmark with held-out cases and no accuracy percentage until a defensible gold set exists.

### Recommended next work cycle

1. Read the current browser rules and Python package contracts side by side.
2. Create a small shared fixture set for the existing adversarial examples, recording expected parse shape and evidence status separately from exact phonetic output.
3. Add differential/contract tests that make runtime disagreement visible without forcing unsupported IPA.
4. Decide whether the Python library becomes authoritative and the browser consumes its generated rule model, or whether shared declarative rules are generated into both runtimes.
5. Run CI; record exact run IDs and any unresolved cases here before expanding vowel/coda/tone rules.
