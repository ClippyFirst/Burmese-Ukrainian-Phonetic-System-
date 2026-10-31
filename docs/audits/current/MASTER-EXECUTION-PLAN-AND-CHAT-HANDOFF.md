# Burmese → Ukrainian: Master Execution Plan and Chat Handoff

Last reviewed: 2026-10-21
Repository: https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-
Default branch used for this review: `main`; the prior audit baseline was `5bc93e81d07d6afbad366c300eae321790b91893`. Later commits added normalization regressions, audit corrections, and an optional evidence-gated G2P benchmark runner; see the dated sections below for the exact revision and CI state.
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

The handoff file exists at `docs/audits/current/MASTER-EXECUTION-PLAN-AND-CHAT-HANDOFF.md`; `CITATION.cff` exists and uses `NOASSERTION` pending an owner license decision. `docs/references.md`, `data/burmese/sources.csv`, and `data/burmese/source_claims.csv` are the current source registries. Both `.github/workflows/test.yml` and `.github/workflows/pages.yml` exist. The separate `test.yml` workflow runs `pytest`, `npm run build`, `npm test`, and `npm run test:browser`. The Pages workflow runs the Node build/unit/browser checks and deployment, but does not run `pytest` itself.

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
| 8. IPA | IN_PROGRESS | Python `ipa.py` is a small onset+vowel seed mapper; browser `src/web/app.js` has a separate, more elaborate hand-written contextual IPA derivation. These runtimes do not share one authoritative phonology engine and may disagree. Neither is a validated complete surface-phonetic system. |
| 9. Ukrainian adaptation | IN_PROGRESS | Separate table-driven layer exists with explicit uncertain/not-established outcomes. Its inputs must be validated IPA, not guessed values; test independent from IPA. |
| 10. Unknown/ambiguous/unsupported inputs | IN_PROGRESS | Parser has malformed/unsupported states; practical layer returns `not_established` for unmapped IPA. Ensure all APIs consistently preserve unknowns and never present placeholders as confident output. |
| 11. Sources, tests, docs, UI, CI, deployment | IN_PROGRESS | `docs/references.md`, `data/burmese/sources.csv`, and `data/burmese/source_claims.csv` exist; `CITATION.cff` exists with `NOASSERTION` while licensing remains unresolved. Latest pre-handoff commit passed Python, Node and browser CI; latest Pages build and deployment succeeded. The current handoff-only commit's new workflow runs are in progress. Public page response has not been independently verified. |

## Prioritized task registry

Statuses allowed: `TODO`, `IN_PROGRESS`, `BLOCKED`, `DONE_VERIFIED`, `DEFERRED`, `NOT_APPLICABLE`.

### Gate 0 — repository integrity and reproducibility
- **BUR-001 — DONE_VERIFIED — P0 — Establish reproducible baseline.** Verified default branch `main`, current head, recursive repository tree, source registry and workflows; latest completed test run passed `pytest`, `npm run build`, `npm test`, and `npm run test:browser`. The handoff-only commit's new CI run remains pending at last poll. Dependency: none.
- **BUR-002 — IN_PROGRESS — P0 — Inspect actual CI workflow and deployment configuration.** Latest completed test and Pages runs succeeded. The public Pages URL itself was not independently fetchable in the available web check, and the newest documentation commit's CI runs are still pending. Keep these distinct from the successful prior commit. Depends on BUR-001.
- **BUR-003 — IN_PROGRESS — P0 — Add/maintain this handoff after every work cycle.** This cycle's findings and exact run IDs are appended below; refresh CI results after the current commit completes.

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
- Historical missing-file finding superseded: the handoff now exists, and `CITATION.cff` is present with `NOASSERTION`.
- `.github/workflows/ci.yml` — not found at that exact path.
- `.github/workflows/pages.yml` — verified; latest run `39482511514` on `main` commit `e5bbf24049ec5bb7f6480435e2ea3e07f3e236b8` succeeded, including build, Node tests, browser tests, artifact upload and deployment.
- `package.json` — version 0.2.2; scripts include `build`, `test`, `test:browser`, `validate:data`, and `check`.
- `tests/test_unicode.py` — basic NFC idempotence, dependent-e vowel segmentation and kinzi segmentation tests exist.
- Local test suite/build: NOT RUN in this environment. The remote connector did not expose a local checkout or execute commands.
- Current repository head after this handoff update is `5bc93e81d07d6afbad366c300eae321790b91893`. The prior head `e5bbf24049ec5bb7f6480435e2ea3e07f3e236b8` passed `pytest`, `npm run build`, `npm test`, and `npm run test:browser` in run `39482511445`; Pages build/deployment succeeded in run `39482511514`. The new head's runs `39483042395` (tests) and `39483042499` (Pages) were in progress at last poll. This verifies CI workflow behavior only, not linguistic correctness.

## Exact next step

BUR-001 is now `DONE_VERIFIED` for repository/tree/workflow discovery and remote CI baseline. Next: inspect the two separate runtime paths (Python library vs browser engine), then add shared golden/adversarial fixtures so both paths have comparable, explicitly scoped expected outputs. Do not claim phonetic completeness or merge old divergent branches wholesale.


## Audit cycle 2026-10-20 — verified baseline and branch reconciliation

### Verified repository state

- Default branch: `main`; current head `e5bbf24049ec5bb7f6480435e2ea3e07f3e236b8`.
- Repository tree fetched recursively; no truncation reported.
- Current files include both `.github/workflows/test.yml` and `.github/workflows/pages.yml`.
- Latest test run: [39482511445](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39482511445) — success. Verified steps include `pytest`, `npm run build`, `npm test`, and `npm run test:browser`.
- Latest Pages run: [39482511514](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39482511514) — success. Both build and deploy jobs succeeded; browser test, artifact upload and deployment steps all succeeded.
- The earlier missing-file finding was superseded by later repository state: `CITATION.cff` exists and uses `NOASSERTION`; `docs/references.md`, `data/burmese/sources.csv`, and `data/burmese/source_claims.csv` are present.

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

- BUR-001 — `DONE_VERIFIED`: recursive tree, default branch/head, workflows and latest completed remote CI baseline checked.
- BUR-002 — `IN_PROGRESS`: prior Pages build/deploy and test workflow succeeded; public URL response is not independently verified and current-head workflow runs were pending at last poll.
- BUR-003 — `IN_PROGRESS`: handoff updated; poll current-head runs and record final status.
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


## Audit cycle 2026-10-20 — Unicode script-range parity fix

### Concrete code change

- Updated `src/burmese_ukrainian/unicode.py` so `is_myanmar()` recognizes U+116D0–U+116FF (Myanmar Extended-C), matching the wider block recognition already used by the browser's `isMyanmarCodePoint()`.
- Added `test_myanmar_extended_c_is_recognized_as_script_not_foreign_text` in `tests/test_unicode.py`, using U+116D0. The test explicitly distinguishes script-block recognition from linguistic support: a recognized Myanmar character is not thereby assigned a Burmese IPA value.
- Code commit: `f76e2476a5a953af5ccb1ad463896578570aecc6`.
- Test commit: `ba7aafa22a7903747c2cc14905f80b3b236b5c57`.
- These are separate sequential commits to `main`; no local test execution is available in this connector environment. CI is the verification gate.

### Why this is in scope

The browser's Myanmar block predicate already included U+116D0–U+116FF, while Python's predicate did not. This was a concrete cross-runtime script-detection inconsistency. The fix aligns block recognition without pretending that Myanmar Extended-C characters belong to the supported Standard Burmese grapheme/pronunciation inventory.

### Current follow-up

- The `tests` workflow for handoff commit `5ad517106dd159232dca0c4d5eae227aa871abc9` completed successfully: [run 39483567569](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39483567569). Verified steps: `pytest`, `npm run build`, `npm test` and `npm run test:browser`.
- The Pages workflow for the same commit was still `in_progress` when polled: [run 39483567533](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39483567533). Do not record deployment success until that run completes.
- The main architectural gap remains duplicated browser and Python phonology. Next: add a shared, versioned adversarial fixture corpus and differential/contract tests without forcing unsupported IPA values.

## Follow-up cycle — Extended-C unsupported-status contract

- Test workflow for commit `5ad517106dd159232dca0c4d5eae227aa871abc9` completed successfully: [39483567569](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39483567569). All listed steps passed, including `pytest`, build, Node tests and Playwright browser tests.
- Pages workflow for that commit remained in progress at last poll: [39483567533](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39483567533). Deployment is not yet recorded as successful.
- Added a second regression to `tests/test_unicode.py` on commit `b93e30cb59e563782216e9b86895fa5bb7f08ab1`: U+116D0 must be recognized as Myanmar script but parsed as `unsupported_or_malformed`, with top-level uncertainty and the original grapheme preserved. This guards the distinction between broad Unicode script detection and actual Burmese inventory support.
- CI for `b93e30c` has not yet been polled; this change is pending remote verification.
- Next engineering milestone remains the shared adversarial fixture corpus and differential tests between Python and browser engines. Avoid inventing IPA expectations for fixtures unless a source-backed gold analysis exists.

## Follow-up cycle — CI caught a test-fixture escaping error

- Investigated failing Python CI on `ddad3bc4`: `pytest` reported 1 failed / 17 passed. The new test passed the literal ten-character string `\\U000116D0` rather than the actual supplementary Myanmar code point; this was a test construction bug, not evidence that the parser failed to preserve the character.
- Corrected the test in commit `0f5a7217973bb908e4186ce0516b534ba237be0c` to use `character = chr(0x116D0)`, and assert that the parser preserves that actual character. This avoids Python-source escaping ambiguity.
- The corrected commit's CI is pending and must be polled. The earlier Extended-C parser contract is not considered verified until this corrected test passes.
- CI runs for `b93e30cb` and `ddad3bc4` failed at `pytest` for the same escaping issue. The Pages run for `ddad3bc4` succeeded, but that does not override the failing test workflow.


## Follow-up cycle — shared Unicode contract fixture (2026-10-20)

- The corrected Extended-C parser test and handoff commit `1c81088356907c8f6665dcc32d17b00a9a2a49bc` passed the test workflow: [39484295230](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39484295230). This confirms the parser contract test is now green; it does not establish support for Extended-C pronunciation.
- Added `tests/fixtures/shared_unicode_contract.json` with a versioned, source-neutral contract for U+116D0: Myanmar-script recognition is broad, while Burmese inventory analysis remains explicitly unsupported. The fixture stores separate Python and browser expectations because their APIs and analysis depth currently differ.
- Added `tests/test_shared_unicode_contract.py` to read the JSON fixture and assert Python structural status, code point identity, and grapheme preservation.
- Updated `tests/browser/converter.spec.js` to consume the same fixture and assert browser `UNSUPPORTED` status without ordinary passthrough diagnostics. Updated `tests/adversarial/README.md` to document the fixture contract and prohibit unsupported IPA gold labels.
- These changes are sequential commits: fixture `cd7204ee`, Python consumer `021ab06b`, browser consumer `c598c69d`, fixture documentation `2fbb39df`.
- CI for the browser-consumer commit is running as [39484565457](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39484565457); Pages is queued. Poll both before marking this milestone verified. Later commits may supersede these run results.
- Scope limitation: this is a shared regression contract, not yet a full differential test of linguistic outputs. It deliberately does not prescribe IPA or Ukrainian transcription for U+116D0. Next: expand fixture categories only where expectations are defensible, then add more robust API-level contract comparisons between the Python parser and browser engine.


### Verification update and corpus expansion — 2026-10-20

- CI and Pages both succeeded for commit `289765d9`: [tests 39484629387](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39484629387), [Pages 39484629321](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39484629321). The first shared-fixture implementation is verified on that commit.
- Expanded `tests/fixtures/shared_unicode_contract.json` in commit `990a150a3305ddb75f32259e6b5c32e5cef10b99` with U+A9E0 (`ꩠ`), complementing U+116D0. Both are broad Myanmar-script code points that must remain explicitly unsupported by the current Burmese analysis inventory. The existing browser suite already has direct coverage for U+A9E0; the new shared fixture now ties it to the Python parser test as well.
- CI for `990a150a` has not yet been polled. Do not call the expansion verified until the latest workflow completes successfully.
- This fixture corpus currently covers Unicode support-boundary contracts, not complete phonological differential testing. Next priority is to add a small, carefully scoped structural corpus for malformed virama and canonical normalization, with only expectations supported by the parser's documented structural model; then investigate shared browser/Python result schema without fabricating identical outputs where implementations are intentionally different.


### Fixture correction — Unicode block label/code point mismatch

- CI for expanded fixture commit `990a150a` caught a real test-data error: the visible character `ꩠ` normalizes to / is represented as U+AA60 in the Python parser, not U+A9E0. The failure was in the fixture's asserted code point, not in parser support detection: [CI run 39484941062](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39484941062) reported 18 passed, 1 failed.
- Corrected the fixture case to `myanmar-extended-b-aa60` with expected `U+AA60` in commit `4c9ba6f36abbc61780f8253a2c39526567da474a`. The case remains explicitly unsupported by the current Burmese inventory. Do not claim this correction is verified until CI on the corrected commit succeeds.
- This illustrates why fixture code points are asserted from actual code points, not inferred from a glyph's appearance or a previous test's label.



## Evidence-gated phonology and external G2P cycle — 2026-10-20

### Files added
- CITATION.cff: citation metadata for the research prototype; license is NOASSERTION pending an owner decision.
- docs/audits/current/PHONOLOGY-COVERAGE-AUDIT-2026-10-20.md: layer-by-layer implementation status and measurable coverage limits.
- docs/audits/current/G2P-ENGINE-AND-LICENSING-AUDIT-2026-10-20.md: Epitran and myG2P assessment and a reproducible benchmark protocol.
- THIRD_PARTY_NOTICES.md: separates project license status from third-party code/data/model rights.
- data/burmese/phonology_corpus.csv: six structural probe rows; all are explicitly STRUCTURAL_ONLY and have no IPA or Ukrainian gold label.
- README.md: links the audits and states that word-level IPA and Ukrainian name accuracy are not measured.

### Current layer inventory
- Unicode normalization: partial; Python supports NFC/NFD/NFKC/NFKD while browser uses NFC. Cross-runtime canonical-equivalence tests remain needed.
- Myanmar block recognition: shared structural/status contract tests cover unknown code points in extended blocks; this is not phonology.
- Segmentation, consonants, kinzi, medials, vowels and codas: partial; structural parser and browser engine are separate implementations.
- Tone/register/phonation: documented competing analyses only; no complete runtime derivation verified.
- Allophony: some browser contextual rules, not a complete evidence-traced rule engine.
- IPA: partial seed mapper in Python and a separate richer browser derivation; no independent gold corpus and no measured agreement.
- IPA-to-Ukrainian: table-driven partial policy with uncertainty states; many choices remain project hypotheses, not official norms.
- Uncertainty handling: partial; align status contracts and test that no unsupported case receives a confident-looking string.

### External engine decision
Epitran lists mya-Mymr but classifies Burmese as limited support due to orthographic ambiguity. It is retained as a candidate control/baseline, not accepted as primary G2P. The package-code metadata reports MIT-Modern-Variant, but mapping/data provenance still needs component-level review. myG2P declares CC BY-NC-SA 4.0 for its pronunciation dictionary; do not bundle or copy its entries without a separate compatibility/rights review. No external engine has been benchmarked against a verified independent corpus in this cycle.

### License decision
GitHub reports no detected license and there is no root LICENSE file. This cycle intentionally did not choose a license on behalf of the project owner. CITATION.cff uses NOASSERTION. The next release gate is an explicit maintainer decision on source-code licensing and a separate corpus/data policy.

### Corpus measurement
Six seed rows exist but all are structural probes, not phonological gold entries. Verified independently adjudicated lexical IPA gold entries: 0. Word-level IPA accuracy, Ukrainian name-level accuracy and browser/Python agreement: not measured. Do not interpret "not measured" as 0% accuracy.

### CI
The earlier commit 2e1729d5 passed tests and Pages:
- tests: https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39485011447
- Pages: https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39485011474

New audit files triggered several workflows because each file was committed independently. At the time of this handoff update, the latest README commit 4ba1b812 had queued tests run https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39487858083 and Pages run https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39487858082. Poll the latest runs before claiming the audit-file set passes CI.

### Next work
1. Poll the latest tests and Pages deployment for the final commit; fix any failures rather than treating queued runs as success.
2. Obtain exact source page/table/entry locators and build the first independently adjudicated lexical IPA gold entries; do not fill blank seed IPA fields from intuition.
3. Run the optional Epitran benchmark in a separate, pinned environment and preserve raw outputs plus artifact hashes; current repository CI does not install Epitran.
4. Establish layer-specific statuses and differential tests; do not force Python and browser into identical outputs where their intended contracts differ.
5. Decide project code/corpus licensing with the maintainer before adding third-party dictionary data or a root LICENSE.


### Canonical normalization regression and CI correction — 2026-10-20

- Added a Python regression in `tests/test_unicode.py` for canonical equivalence U+1026 versus U+1025 U+102E; it checks normalization and segmentation equality only, not a phonetic claim.
- Added a Playwright regression in `tests/browser/converter.spec.js` comparing browser syllable and IPA displays for the two canonical spellings.
- The first browser assertion used Playwright `toHaveText` against a value captured with `innerText`. CI exposed whitespace normalization by the matcher, not a phonology mismatch. The test now compares exact `innerText` values.
- Fix commit: `46a57a4b7cf37aa39fa5cafaacf7589c1927698a`.
- CI for that commit: tests workflow passed, including pytest, npm build, npm unit tests and all 40 Playwright tests: https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39494898579. Pages build/browser checks passed; deployment was still in progress at the time of this note: https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39494898537.
- The test demonstrates equivalence of the current browser display for this one canonical pair only. It does not establish lexical IPA accuracy, complete Burmese normalization coverage, or full Python/browser phonological agreement.

### Evidence and corpus guardrail

- `data/burmese/phonology_corpus.csv` contains six structural regression probes, not six gold IPA entries. Their IPA and Ukrainian target fields remain blank intentionally.
- The current audited count of independently adjudicated lexical IPA gold entries remains **0 verified**. Word-level IPA accuracy, Ukrainian name-level accuracy and full cross-runtime phonological agreement remain unmeasured.
- Epitran `mya-Mymr` is a candidate baseline only: upstream describes Burmese support as limited due to orthographic ambiguity. Any benchmark must pin versions, record exact raw outputs and use independently adjudicated source-located targets.
- Do not copy/bundle `myG2P` dictionary entries without a licensing/compatibility review; its repository declares CC BY-NC-SA 4.0. Keep engine code, mapping files and lexical data licenses separate.
- Project license remains unresolved; `CITATION.cff` uses `NOASSERTION` rather than guessing an owner decision.

### Epitran inspection and benchmark harness — 2026-10-20

- Inspected Epitran v1.35.0's release-tagged `mya-Mymr` map, preprocessor and postprocessor files. The map is a compact orthography/chunk substitution table; the preprocessor is empty; postprocessing handles medial insertion and selected schwa deletion but does not reconstruct tone. This is static inspection, not an executed engine benchmark.
- Added `scripts/benchmark_g2p.py`, an optional local runner that imports Epitran only when invoked, preserves raw outputs, records package/corpus/mapping hashes when available, and leaves accuracy `null` when there are no verified gold rows.
- Benchmark scoring requires `GOLD_VERIFIED`, non-empty expected IPA, a source ID present in `data/burmese/sources.csv`, a precise non-pending source locator, and non-empty IPA convention, scope, analysis level, reviewer and uncertainty notes. Structural-only probes cannot be counted as accuracy examples.
- Added contract tests for structural-only non-scoring, source-located gold scoring, and corpus status integrity.
- Related changes include the G2P audit, README usage instructions, `scripts/benchmark_g2p.py`, and `tests/test_contracts.py`. The runner has not yet been executed against an installed Epitran environment.
- CI for the source-registry guard commit `e257cc89` was still running at the time this handoff was prepared: tests https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39495318894; Pages https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39495318893. An earlier benchmark-runner test run on `6d73bf23` passed, but it predates the source-registry guard and is not a substitute for the latest run.



### Continuation execution — 2026-10-21

- Dedicated branch: `feat/burmese-phonology-coverage-gates-2026-10-21`, based on `main` at `81ad16ff252c0e8c59d3e5118b58216e5bad70bf`. The branch is carried by draft PR [#4](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/4); it has not been merged. Existing branches `final-hardening`, `fix/adversarial-burmese-phonology`, and `service-ready` were inspected and left untouched.
- Added `docs/audits/current/EXECUTION-STATUS-MATRIX-2026-10-21.md` as the canonical status ledger and `tests/test_ipa_status_contract.py` to keep parse success separate from phonological certainty.
- Extended `data/burmese/phonology_corpus.csv` with explicit `ipa_convention`, `scope`, `analysis_level`, `reviewer`, and `uncertainty_notes` columns. All six rows remain `STRUCTURAL_ONLY`; their new metadata fields remain blank intentionally.
- Tightened `scripts/benchmark_g2p.py`: a `GOLD_VERIFIED` label is insufficient by itself; rows missing any adjudication metadata are excluded from scoring. Raw outputs and metadata are retained in the benchmark report.
- Added `tests/test_benchmark_g2p.py` for three cases: all current structural probes remain unscored, incomplete adjudication metadata remains unscored, and a fully documented synthetic unit-test fixture can be scored. The synthetic fixture is not Burmese linguistic evidence and is not part of the corpus.
- Preserved and verified the existing browser test that consumes `tests/fixtures/shared_unicode_contract.json` and checks that recognized Myanmar-script characters outside the supported Burmese inventory are marked `UNSUPPORTED`, not passed through as ordinary foreign text. The complete existing browser suite was restored after an intermediate edit accidentally omitted its final tests; no existing browser regressions are intentionally removed.
- Verified CI run #259 at implementation commit `1045735c244e96c898c3a675f15ad68f6b79151a`: `pip install -e ".[test]"`, `pytest` (**32 passed**), `npm install`, `npm run build`, canonical web-data validation, generated-data drift check, Playwright installation, and `npm run test:browser` (**40 passed**) all succeeded. Run: https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/39571014041.
- Added `tests/test_schema_validation.py` and made CI install the `.[test]` extra. CI now checks the schema definitions, validates representative parser outputs, runs web-data validation/build, and verifies that regenerating `src/web/generated/data.js` leaves no diff. These checks passed in run #251; schema validation still does not cover every source/claim registry row. The optional Epitran benchmark remains unrun, and no Epitran accuracy or phonological accuracy is claimed.
- Gold-corpus status remains **0 verified lexical IPA entries**. The next linguistic acceptance gate is exact source locators plus independent adjudication for each candidate entry; do not promote `ကေ`, `ကော်`, `ကြည်`, `စွယ်`, `မြန်`, or `ယူ` from structural probes without that evidence. Root code/corpus licensing remains an owner decision.


### Website publication update

- The homepage now prominently identifies the converter as a research preview and warns that there are no independently verified lexical IPA gold entries, so output may be incomplete or hypothetical.
- `system.html#validation-status` now publishes the current validation state: 0 verified lexical IPA gold entries, 6 structural-only probes, and the last verified CI suite counts (32 Python tests and 40 browser tests). It links to the execution matrix.
- Added a browser regression that checks the public warning, corpus counts, and matrix link. These changes are on the same feature branch and will be published to GitHub Pages after the reviewed PR is merged and the Pages workflow succeeds.
- The public site is intentionally described as a research prototype, not a validated transcription standard. The linguistic acceptance blocker remains independent adjudication of source-located lexical IPA examples.


## Handoff update — pinned Epitran smoke workflow (2026-10-24)

- Branch: `ci/optional-epitran-smoke-2026-10-24`.
- Added `.github/workflows/optional-epitran-benchmark.yml`: installs `epitran==1.35.3` only in an isolated GitHub Actions job, runs `scripts/benchmark_g2p.py`, and uploads `artifacts/burmese-epitran-raw-output.json` for 30 days.
- Existing strict score gate is retained: current corpus rows are STRUCTURAL_ONLY; no gold row means accuracy, exact-match count and denominator remain null/zero as appropriate. Epitran remains a candidate baseline only, especially given limited Burmese support and absent tone reconstruction.
- Update the execution matrix in place; task status is IN_PROGRESS pending workflow run and artifact inspection. Gold-corpus work remains BLOCKED until exact source locators and independent adjudication exist. Do not copy myG2P data.


## Handoff update — Epitran smoke verified; scoring still blocked (2026-10-24)

- First workflow [40092549134](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40092549134) exposed a real harness bug: local `import importlib.resources` shadowed the module used for `importlib.metadata.version`, causing `UnboundLocalError` after Epitran ran. Fixed by `from importlib import resources`; added a regression test.
- Successful rerun: [40092717790](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40092717790). Epitran 1.35.3 / Python 3.12.15; 6 raw outputs, 0 runtime errors; corpus SHA-256 `bc7d4f138581b7cfd48594b41891a26ec45123ea4488af977b48567201f0b19b`; mapping SHA-256 `de8660a0cdccb4192993d423342ad775a59ade19b8081829eb70da18f291dfe4`; artifact SHA-256 `1ca54b638897f41f124147df0744f9929e651757b720552082d701748794e475`.
- Raw candidate outputs: `ကေ → ke`; `ကော် → kaʊʔ`; `ကြည် → t͡ɕi`; `စွယ် → səwɛ`; `မြန် → məjaɴ`; `ယူ → ju`. All six rows remain STRUCTURAL_ONLY. Report confirms `eligible_verified_gold_count=0`, `exact_match_count=null`, `exact_match_accuracy=null`.
- Raw-output smoke is DONE_VERIFIED; linguistic scoring remains BLOCKED by exact source locators and independent adjudication. No engine promoted to production and no myG2P entries copied.


## Final checkpoint — Burmese Epitran smoke and test suite (2026-10-24)

Code branch merged to main at `b71e2075b1e7dcebd17b54164bc017eb99eececd`; the last code-tested head was `fa5a5e7dbb292b88d05bc8cadb3e35ac2809c08d`. Verification run 40093021155 passed: pytest, npm build, generated-data drift validation, npm tests, and Playwright browser tests. Optional Epitran run 40093021146 passed using Epitran 1.35.3 and Python 3.12.15.

The six structural probes produced raw candidate outputs ke, kaʊʔ, t͡ɕi, səwɛ, məjaɴ, ju. Corpus SHA-256 bc7d4f138581b7cfd48594b41891a26ec45123ea4488af977b48567201f0b19b; mapping SHA-256 de8660a0cdccb4192993d423342ad775a59ade19b8081829eb70da18f291dfe4; empty preprocessor SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; postprocessor SHA-256 0eac185c50b19b7c2682d1395afad97a7662a5ff22e2344195eb0d3ffcbed7af; artifact ZIP SHA-256 6abad56759caa47868dee8af5e82068c143f810336454099ba9c149dc74e8f09. Gold count is zero and accuracy is null. This remains a raw-output smoke run only; no production dependency was added.


## Final merge checkpoint — Burmese Epitran raw-output harness (2026-10-24)

- PR [#9](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/9) merged to main at `b71e2075b1e7dcebd17b54164bc017eb99eececd`.
- Code-tested head `fa5a5e7dbb292b88d05bc8cadb3e35ac2809c08d`: full test/build/browser suite [40093021155](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40093021155) passed; pinned Epitran run [40093021146](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40093021146) passed and artifact inspected.
- Artifact SHA-256 `6abad56759caa47868dee8af5e82068c143f810336454099ba9c149dc74e8f09`; Epitran 1.35.3, Python 3.12.15; corpus SHA-256 `bc7d4f138581b7cfd48594b41891a26ec45123ea4488af977b48567201f0b19b`; mapping SHA-256 `de8660a0cdccb4192993d423342ad775a59ade19b8081829eb70da18f291dfe4`; preprocessor empty hash `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; postprocessor hash `0eac185c50b19b7c2682d1395afad97a7662a5ff22e2344195eb0d3ffcbed7af`.
- Six structural probes, zero runtime errors, verified gold count zero, exact-match count and accuracy null. External Epitran remains a candidate-only comparator; no data was copied from myG2P and no production dependency was added.


Authoritative readiness checkpoint — 2026-10-24 12:38 UTC

- Current main HEAD: b7a44e6e0ff7ec0010d58c30c2ceb0101e72761b.
- Current-main test run 40093806758 and deployment 40093806746 passed.
- The Epitran 1.35.3 smoke is repeatable but unscored: six structural probes, zero runtime errors, independent gold count 0, accuracy null. Artifact SHA-256 6abad56759caa47868dee8af5e82068c143f810336454099ba9c149dc74e8f09.
- Remaining blocker: source-adjudicated lexical corpus and tone-aware evaluation. No Epitran production dependency; no gold IPA inferred from grapheme mapping.

## Authoritative current-head checkpoint — 2026-10-25

This note supersedes earlier handoff statements that current-main checks or the Epitran smoke were still pending.

- Current `main`: `32f6f3da9328aa96e746d63b63912c4e64793646`.
- Main tests [40128844973](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40128844973), Pages deployment [40128844976](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40128844976), and optional Epitran smoke [40128845097](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40128845097) all completed successfully.
- This verifies software checks and candidate raw-output execution, not phonological accuracy. Six structural probes; independent gold count 0; accuracy null. The separate source-adjudicated corpus, tone/phonation and contextual phonology work remains open. Do not copy unlicensed external corpora or enable Epitran in production.

## Final current-main verification and smoke checkpoint — 2026-10-25

- Workflow-trigger fix PR #24 merged as `c012023e5ae4fdd4257d2c59b0cbbbb369021f8b`. It removes evidence-only registry/benchmark-doc changes from automatic Epitran smoke triggers while retaining manual dispatch and executable input/source/script changes.
- Post-merge current-main tests and deployment are still being verified separately; do not claim them green until their push runs finish.
- Current-main optional Epitran smoke [40134067758](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40134067758) passed. Inspected artifact [12576415800](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40134067758/artifacts/12576415800), ZIP SHA-256 `6ff7fd5d70f386d76eefb37d50d2718d9de3f4e410749cf94848af9afeab788c`; Epitran 1.35.3 / Python 3.12.15; 6 outputs, 0 runtime errors. Corpus/mapping/pre/post hashes are recorded in the registry. Gold count remains 0 and accuracy null.
- This is raw-output smoke evidence only. Phonological coverage, tone-aware evaluation, source-located lexical gold, Python/browser parity and owner licensing decisions remain open.


## IPA withholding for unresolved coda/prosody — 2026-10-25

- PR #26: https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/26
- The IPA adapter now withholds a syllable-level IPA result when parsed coda/asat or prosodic marks lack an evidence-backed surface realization, rather than silently dropping that material. Regression tests cover a dangling virama, unresolved asat coda and unresolved prosodic mark.
- Workflow for the original test-only commit [40192527691](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40192527691) passed. The follow-up implementation/test commit `495d34517c29540982791653f5e4b35bc2a1a856` had workflow `40192661638` still in progress at this checkpoint; do not mark this follow-up verified until that run completes successfully.
- This is conservative correctness hardening, not a claim of complete Burmese phonology. Independent gold count remains 0; contextual vowel realization, tone/phonation and source-adjudicated lexical data remain open.


## Anusvara IPA-withholding correction — 2026-10-25

- Branch: `fix/burmese-withhold-unresolved-anusvara-20261025`; PR [#28](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/28).
- Defect: `VOWEL_SIGNS` parses U+1036 ANUSVARA as an orthographic vowel sign, while `ipa.py` used an empty-string placeholder for it and filtered empty mapped values. Consequently `to_ipa("ကံ")` returned `k`, silently deleting unresolved nasal/coda material.
- Test-first evidence: [run 40195598572](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40195598572) failed on the new regression as expected: actual syllable IPA was `k` instead of `None`.
- Fix: both the Python IPA adapter and browser `deriveIpa()` now withhold the whole syllable whenever an anusvara sign is present, until its contextual nasal/coda realization has an evidence-backed rule. The browser regression also verifies `#ipa` shows the unresolved placeholder, Ukrainian output remains unavailable, and aggregate status is `NOT_ESTABLISHED`. Neither runtime guesses a nasal consonant or claims a new IPA mapping.
- Verification: post-fix Python-only run [40195614032](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40195614032) passed. After adding the browser guard and Playwright regression, exact branch-head run [40196136958](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40196136958) **passed** pytest, npm build, generated-web-data check, npm tests, and Playwright browser tests.
- This closes one conservative adapter defect only. Complete contextual vowels, codas, tone/phonation, Python/browser parity, independent lexical IPA gold, and accuracy measurement remain open; gold count is still 0.


## Inherent-vowel withholding correction — 2026-10-25

- Follow-up defect found while checking the Python/browser boundary: Python emitted `k?` for bare `က`, while the browser supplied an unqualified `a` and returned `ka`. The current adapter has not yet established the inherent-vowel realization for every context, so these outputs contradicted the conservative evidence gate.
- Fix: Python now returns no IPA when the parsed vowel object is absent or has no explicit signs; browser removes the unconditional open-syllable `a` fallback. Separately licensed contextual patterns remain available; this change does not erase those rules.
- Regression coverage: `tests/test_ipa_status_contract.py` asserts bare `က` has no syllable IPA, status `analysis_dependent`, and aggregate placeholder `?`; Playwright checks browser IPA is withheld, Ukrainian output is `—`, and status is `NOT_ESTABLISHED`.
- Exact-head CI is pending at [run 40196926842](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40196926842) for code commit `7cfbe105e6e26b0321bf07013748e9f1eea77f0c). Do not call the change verified until Python, generated-data, npm, and browser checks finish.
- This is a conservative adapter correction, not a claim that every Burmese inherent vowel is unresolved. Context-specific rules must be separately source-adjudicated and tested. Independent gold remains 0 and accuracy remains unmeasured.


### Follow-up: preserve contextual inherent-vowel rules

- The first attempt to remove the browser's generic inherent-vowel fallback failed existing browser regressions for `ရှ` and `မင်္ဂလာ` (run [40196926842](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40196926842)). That change was too broad: it suppressed contextual cases already represented by the engine.
- Narrowed the guard to an **isolated one-codepoint bare consonant input only**. Existing contextual fallbacks remain intact for multi-grapheme input; Python and browser both withhold the isolated bare-consonant result. This is a deliberate conservative boundary, not a general claim that inherent vowels are unresolved in all contexts.
- Exact revised code-head CI is [40197108302](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40197108302); pending at this checkpoint. Earlier failures are retained as honest regression evidence, not hidden.


## Post-merge checkpoint — 2026-10-25

- PR #28 merged to `main` as `62cb4ab49bd88736faea89f2b378d10b009ce640`.
- Exact PR-head workflow [40197390660](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40197390660) passed after the inherent-vowel guard was narrowed to isolated bare consonants; contextual fallbacks remain intact.
- This verifies the specific anusvara-loss and isolated-bare-input contracts. It does not establish the contextual vowel/coda system, tone/phonation, full Python/browser parity, or independent accuracy. Independent gold remains 0.


## Empty-input contract regression — 2026-10-25

- `parse_burmese` previously treated empty input as successful because `all([])` is true. It now returns explicit `empty_input` for empty or whitespace-only strings and does not synthesize grapheme/syllable records.
- Regression tests cover `""`, ordinary spaces, and tab/newline-only input. The phonological IPA status remains unchanged for non-empty input.


- Post-merge evidence: PR #30 merged as `6d1ecc79d8dff72cd8a6476bd832a5047515c720`; exact-head CI [40209303104](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40209303104) passed. The fix corrects only the empty-input API status and does not change phonological output for non-empty inputs.


## Boundary-aware bare consonants and Unicode control rejection — 2026-10-25

- The first browser run for the boundary-aware bare-consonant guard failed only because the assertion expected the English string `not established` while the UI correctly displays Ukrainian `не встановлено`. Updated the test to match the user-facing language; no runtime behavior changed for that assertion.
- Also fixed a Python/browser gap: DEL/C1 controls were treated as ordinary non-Myanmar text in the browser and copied through, while Python marked them unsupported. Browser segmentation now isolates C0/C1 controls except tab/LF/CR and routes them through the unsupported-input status path.
- Shared Unicode fixture cases cover U+007F and U+009F and are consumed by Python and Playwright tests. This is input integrity/parity, not phonological gold.
- Exact-head CI [40211417858](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40211417858) passed Python tests, web data validation/build, generated-data drift and Playwright browser tests. This was a standard CI run, not an external Epitran smoke.


## Burmese source-to-rule evidence traceability gate — 2026-10-25

- PR [#37](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/37) merged as `7afa5fd727051f9904a83d817761434c3fad1c4a`.
- Added `CLM-PHON-001` for Mooney & Repetti-Ludlow (2021) and extended `data/burmese/phonological_rules.csv` with `claim_id`, `source_locator`, `scope`, and `test_reference`. The existing `NO_DIRECT_TONE_VOWEL_RULE` remains `analysis_dependent`; the claim is scoped to the vowel alternations analyzed in that paper and is not a universal prohibition on tone-segment interactions.
- Added `tests/test_source_rule_evidence.py`, which verifies unique rule IDs, registered source/claim references, source-ID agreement, a non-empty locator and scope, valid evidence status, and existence of a referenced test file.
- Exact-head full test workflow [40220190045](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40220190045) passed. This is provenance/contract evidence, not a phonological accuracy benchmark. Independent adjudicated Burmese IPA gold remains 0.
- Matrix status: source → claim → rule → test traceability is `DONE_VERIFIED` for the current rule rows. The broader tone/register/phonation model, vowel/coda coverage and independent lexical gold corpus remain unresolved.


## Unicode-backed misplaced-virama evidence link — 2026-10-25

- Added `CLM-ORTH-001` to `data/burmese/source_claims.csv`, scoped to modern Burmese orthographic structure and U+1039, using Unicode 18.0.0 §16.3.1 / Table 16-4. The claim is structural; it does not assert IPA for the affected forms.
- Added `MALFORMED_VIRAMA_WITHHOLD_IPA` to `data/burmese/phonological_rules.csv` as a traceable guard: U+1039 not immediately followed by a base consonant in the parsed conjunct must remain invalid and must not be silently discarded into plausible IPA/Ukrainian output.
- Extended `tests/test_source_rule_evidence.py` to assert source/claim/rule/test linkage and distinguish the orthographic source from phonetic evidence.
- Exact-head CI is pending. No local test execution is claimed. Acceptance: all schema/source-rule tests, Python tests, build and browser tests pass on this exact branch head.
- This documents an existing malformed-input guard; it adds no phonetic realization and no independent Burmese IPA gold. Independent gold remains 0.


## Romanization → IPA → Ukrainian result order — 2026-10-29

- Open draft PR [#47](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/47) adds a separate Burmese romanization result before IPA and Ukrainian practical transcription.
- Engine: vendored Mya2Rom 0.4.4, profile `MLCTS2` (modified MLC/SEALang transcription), licensed CC-BY-SA-4.0 with upstream license and attribution notice preserved. The upstream project documents limitations for stacked forms, some asat forms, sandhi, alternate pronunciations, and Pali/Sanskrit-derived words. The output is not a pronunciation gold standard.
- Exact-head CI for `e79c03aa97f7a7e171e8477e6488c7007d45b69c`: [tests run 40780283987](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40780283987) **passed**, including existing Python/web checks and Playwright browser tests. Added browser regression checks the documented `မြို့ → mjou.` output and the visible Romanization → IPA → Ukrainian order.
- Status: UI/engine integration **PARTIAL / CI-PASS**. Existing Burmese IPA and Ukrainian candidate limitations are unchanged; romanization is an independent output and does not repair the unresolved lexical IPA gold gap.
- Next acceptance gates: broaden source-backed MLCTS2 fixtures, manually inspect punctuation/mixed-script behavior and copy controls, review share-alike attribution obligations, and retain the research-grade warning. Keep PR draft pending owner review.


## Publication checkpoint — 2026-10-29

This checkpoint supersedes earlier notes in this handoff saying the romanization PR was open/draft.

- PR #47 was merged to main as 977548d3044ff0645ec80e96886f59983243b4b8.
- Exact post-merge tests [40782829530](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40782829530) passed, including npm build/tests and Playwright browser regression.
- Exact post-merge GitHub Pages deployment [40782829421](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40782829421) passed and reported URL: https://clippyfirst.github.io/Burmese-Ukrainian-Phonetic-System-/
- Published output order: Burmese romanization (MLCTS2) → IPA → Ukrainian practical transcription. Mya2Rom profile and phonological coverage limitations remain as documented above.
- Remaining acceptance gates include more sourced MLCTS2 fixtures, manual punctuation/mixed-script/copy QA, and licensing review. Publication does not mean linguistic completeness.


## Cross-language Ukrainian target policy checkpoint — 2026-10-30

The shared target conventions are now explicit in the central Ukrainian Phonetic Inventory and implemented in the Burmese practical layer:

- aspiration is marked after the corresponding Ukrainian consonant with ASCII apostrophe: к', т', п', с', ч';
- /h/ → г, /ɡ/ → ґ, genuine /x/ → х;
- Burmese /tɕ/ → ч and /dʑ/ → дж;
- /ʔ/ is not aspiration and never triggers the apostrophe marker;
- /θ~ð/ remains a conservative, explicitly ANALYSIS_DEPENDENT candidate, not a claimed exact Ukrainian equivalent.

The exact PR #49 head `e43c4e0121d9f29bc942e5f470d795c114c2085e` passed the full workflow [41075332863](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41075332863): Python tests, generated browser data, build, Node tests and Playwright. Current continuation branch is `fix/shared-ukrainian-phonetics-2026-10-30`; PR #49 is draft. PR #48 remains untouched.

This is a target orthography policy update only. It does not increase the count of independently adjudicated Burmese IPA gold examples (still 0), does not establish accuracy, and does not close the previously listed phonology, tone/register, corpus or licensing tasks. Keep the research-grade limitation visible.


## Final main / Pages checkpoint — 2026-10-31

- Final main commit: fff943db823ae5ca0f4fed50b572cc75cb743f84.
- PR #54: MLCTS profile and onset matrix; PR #55: two separate method tabs; PR #56: production asset copy, multi-page build and preview-based browser tests.
- PR #48 was closed as superseded by #56; its old branch was left intact. PR #53 styling work remains open and untouched.
- Main verification [41231199684](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41231199684) passed: pytest 63 + 29 subtests; Node 3/3; Playwright 48 against the built artifact.
- Pages deployment [41231199596](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41231199596) succeeded: https://clippyfirst.github.io/Burmese-Ukrainian-Phonetic-System-/ .
- Final statuses: MYA-ROM-PROFILE-001 DONE_VERIFIED; MYA-ROM-MATRIX-ONSET-001 DONE_VERIFIED; MYA-ROM-MATRIX-001 PARTIAL; MYA-ROM-UA-001 TODO; MYA-PAGES-ARTIFACT-001 DONE_VERIFIED; MYA-PHONETIC-COVERAGE PARTIAL/BLOCKED pending independent lexical gold and expert adjudication.
- The romanization tab's Ukrainian result is intentionally PARTIAL. Do not claim full romanization coverage until a complete source → MLCTS → Ukrainian syllable matrix and adapter pass exact coverage tests.


## Browser output integrity regression — 2026-10-31

- PR [#64](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/64) merged as `d0b7f6351a4151b974ec9ee379f81f7a06da9613`.
- Root cause: `convert()` concatenated `s.uk?.text || ""`; a Myanmar segment with no established Ukrainian candidate therefore vanished from the aggregate output. The browser reproduced this with `ကာ ꩠ` → `ка ` while the second unit was explicitly UNSUPPORTED.
- Fix: the browser output now preserves unresolved/unsupported source units as `⟦source⟧`; the status rank also withholds partially mapped syllables instead of emitting a misleading partial candidate. The contextual initial `/j/` + vowel rule is treated as one target unit so the existing `/juː/ → ю` behavior remains valid.
- The user-supplied Burmese greeting sentence is now a Playwright regression. It reconstructs the normalized source exactly from rendered analysis rows; it does not assert unreviewed IPA or Ukrainian gold. Unsupported target units remain marked.
- Exact PR-head workflow [41238825573](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41238825573) passed pytest 64 + 29 subtests, Node 4/4, Vite build, generated-data drift check and Playwright 50/50 against the built artifact.
- Status: output-integrity and sentence-source-reconstruction tasks DONE_VERIFIED; full sentence-level phonetic accuracy remains BLOCKED/EVIDENCE_LIMITED by absent independent lexical IPA gold and incomplete target mapping. The MLC primary-source blocker and MLCTS-to-Ukrainian adapter TODO are unchanged.
- Pages deployment [41238926334](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41238926334) completed successfully and published `d0b7f6351a4151b974ec9ee379f81f7a06da9613` at https://clippyfirst.github.io/Burmese-Ukrainian-Phonetic-System-/. Main workflow [41238926148](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41238926148) passed after merge.
