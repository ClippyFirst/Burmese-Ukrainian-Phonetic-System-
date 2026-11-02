# Burmese phonology execution status matrix

Updated: 2026-11-01
Base branch at start: main (latest visible commit: 81ad16ff252c0e8c59d3e5118b58216e5bad70bf)
Scope: executable status ledger reconciled with the 2026-10-20 phonology and G2P/licensing audits. This is a continuation register, not a claim of full phonological coverage.

## Status vocabulary
- DONE_VERIFIED — implementation and relevant automated verification both exist.
- PARTIAL — some executable behavior exists, but the layer acceptance criteria are incomplete.
- TODO — no sufficient implementation or verification is established.
- BLOCKED — an external decision, dependency, or missing independent evidence prevents defensible completion.
- DEFERRED — explicitly outside this iteration.
- Coverage counts distinguish implemented behavior, regression-tested behavior, and independently validated lexical evidence. Structural tests do not validate phonological analyses.

## Layer-by-layer ledger

| Layer / acceptance gate | Implemented coverage | Tested coverage | Independently validated coverage | Status | Next acceptance criterion |
|---|---|---|---|---|---|
| Unicode normalization | Python NFC/NFD/NFKC/NFKD entry points; browser NFC entry point | Python NFC idempotence and one canonical-equivalence pair are tested; browser checks the same pair's normalized analysis; broader compatibility-character policy and corpus coverage remain absent | Not applicable to pronunciation | PARTIAL | Specify the supported normalization contract and expand canonical-equivalence/compatibility tests in both runtimes |
| Myanmar block recognition | Bounded Myanmar/Extended block recognition | Structural fixture tests reported by audit | Not phonological evidence | DONE_VERIFIED (bounded contract only) | Keep block recognition distinct from parser/phonology support |
| Grapheme and syllable segmentation | Conservative Python parser and separate browser parser | Shared Unicode contract covers supported-block vs unsupported-inventory cases; PR #30 fixes empty/whitespace-only input. PR #77 adds Python whole-message reconstruction with unsupported Myanmar Extended-C between valid Burmese units, mixed scripts, numerals, punctuation, CRLF and U+200B. PR #78 adds built-browser parity: source reconstruction under textarea CRLF→LF canonicalization, visible unsupported Myanmar unit and preserved foreign text/numerals. Exact PR-head CI [41289738055](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41289738055) and [41290257958](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41290257958) passed pytest, build, generated-data drift, Node and Playwright browser checks. Annotated differential corpus remains incomplete. | 0 lexical gold entries established | PARTIAL | Expand boundary-annotated cases across combining-mark orders, malformed clusters and all API/service entry points; independently adjudicate phonological examples |
| Consonant/onset inventory | Small Python onset IPA table and graphemic inventory | Existing parser/IPA regression coverage is limited | No independently adjudicated inventory-wide lexical set | PARTIAL | Source-map each onset and test legal/unsupported contexts |
| Kinzi | Explicit structural recognition and role metadata | Structural regression coverage exists; contextual phonological tests incomplete | None established | PARTIAL | Source-located onset/medial/coda-context cases and cross-runtime assertions |
| Medials / complex onsets | Four medial signs parsed; some browser contextual derivation | Partial; full combination gold set absent | None established | PARTIAL | Inventory combinations, competing analyses, environments, counterexamples and paired Python/browser tests |
| Dependent/inherent vowels | Vowel signs parsed; small vowel-ID-to-IPA map | Structural tests exist; derivation coverage incomplete | None established | PARTIAL | Evidence-backed combination table and context/length/quality tests; no extrapolation from unverified patterns |
| Codas / checked syllables | Some final structures parsed; browser rime rules reported | Incomplete | None established | PARTIAL | Enumerate coda/rime classes, mark checked-syllable conditions, test each sourced class |
| Tone | Analysis registries document competing traditional and eight-tone/register analyses; no established runtime realization | Not adequately tested as a phonological layer | 0 tone-labelled gold entries established | TODO | Add scoped, source-located tone examples and separate phonemic category from surface F0 realization |
| Register / phonation | Competing literature descriptions documented | No complete runtime model verified | 0 independently adjudicated register/phonation entries | TODO | Model alternatives explicitly with dialect/scope and phonetic evidence; avoid consensus claims where sources disagree |
| Contextual rules / allophony | Partial browser hand-written cases | Rule-complete regression suite absent | None established | PARTIAL | Rule registry with source, environment, output, counterexamples and Python/browser parity tests |
| IPA result/status contract | Python and browser withhold IPA for unresolved anusvara (U+1036) and for a bare consonant that is an isolated token, including when surrounded by whitespace/Latin text; contiguous Myanmar clusters retain the existing contextual path | PR #28 merged as `62cb4ab49bd88736faea89f2b378d10b009ce640`; PR #32 adds boundary-aware withholding and regression tests for `က A` vs contiguous `ကမ`. Boundary-aware bare-consonant regression was found to assert an English phrase against Ukrainian UI text; the assertion now checks the existing Ukrainian uncertainty wording. New shared DEL/C1 fixtures are included; exact-head CI [40211417858](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40211417858) passed Python tests, web validation/build, generated-data checks and Playwright browser tests. Earlier anusvara parity passed in [CI run 40197390660](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40197390660). | No lexical IPA gold entries | PARTIAL | Expand shared fixtures across inherent-vowel environments, coda, tone and malformed cases; verify broader status parity |
| Misplaced U+1039 virama evidence | Parser already rejects virama not consumed as a conjunct; Unicode structural claim and test trace now recorded | Regression tests in `tests/test_malformed_ipa_withholding.py` and provenance test | Unicode 18.0.0 §16.3.1 / Table 16-4; structural evidence only | DONE_VERIFIED for source-to-test traceability; phonology still TODO | Keep IPA withheld; do not treat structural validation as a pronunciation rule or gold IPA |
| IPA → Ukrainian target adapter | Canonical external inventory boundary and candidate registry; explicit unavailable/not-established paths | Practical regression tests exist | No Ukrainian name-level gold evaluation | PARTIAL | Validate adapter against canonical inventory schema and all correspondence policies; test unavailable dependency behavior |
| Feature-distance ranking | Candidate ranking implementation exists | Limited regression tests; final schema/feature validation not established | No empirical target-ranking validation | PARTIAL | Validate feature definitions and weights against canonical inventory; test deterministic ranking, ties, unknown features and missing inventory |
| Comparative Russian/Ukrainian policies | Comparative registries and documentary layer present | Practical tests cover selected correspondences | No independent name-level benchmark | PARTIAL | Check every rule provenance, target-language rationale, uncertainty and non-inheritance from Russian |
| Malformed/unsupported input | Structural and practical uncertainty outcomes exist | Some malformed virama and unknown-target tests | Not a lexical accuracy measure | PARTIAL | Adversarial tests for all API/CLI/browser entry points; no confident output after malformed or incomplete parse |
| Phonological source → claim → rule → test traceability | Every current rule row links to a registered source and scoped claim, locator, evidence status and existing regression-test file | `tests/test_source_rule_evidence.py` checks unique rule IDs, source/claim existence, matching source IDs, non-empty locators/scopes and valid statuses | Provenance contract only; no independent lexical IPA gold or accuracy claim | DONE_VERIFIED (current rule rows only) | Add source/claim/locator/test metadata to each new rule; independently adjudicate phonological outputs before expanding the rule inventory |
| JSON schemas / data validation / generated artifacts | Canonical source, source-claim and phonological-rule CSV registries; syllable schema; generated web data | PR #39 adds `source_record.schema.json` and `phonological_rule.schema.json`, expands `source.schema.json` to the actual claim fields, and validates every source/claim/rule row plus unique IDs and source→claim→rule links. Exact-head tests [40222099466](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40222099466) and web/deploy workflow [40222096239](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40222096239) passed. | Provenance/schema integrity only; lexical IPA gold remains 0 | PARTIAL | Extend schema-backed checks to phonology-corpus records and source/claim locator quality; keep linguistic adjudication separate |
| Python/browser parity | Separate implementations exist | Phonological differential coverage not established | None established | TODO | Shared fixtures and parity tests for structural state, uncertainty, IPA, and unsupported cases |
| Lexical IPA gold corpus | Three U18 structural probes now have exact Unicode 18.0 §16.3.1 / Table 16-4 locators; three Green 2002 probes remain pending | PR #43 replaced stale Unicode locators for `ကေ`, `ကော်`, and `ယူ`; exact-head full workflow [40223402689](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40223402689) passed pytest, build, generated-data checks, Node tests and Playwright browser tests. Optional Epitran raw-output workflow [40223406632](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40223406632) is a comparison artifact, not gold evaluation. | 0 independently adjudicated lexical IPA gold entries | BLOCKED for accuracy evaluation; PARTIAL for source locator cleanup | Inspect the Green 2002 source at exact pages/examples, then obtain expert IPA adjudication; do not promote source examples directly to gold |
| Epitran comparator | Optional scripts/benchmark_g2p.py; pinned Epitran 1.35.3 raw-output workflow on ci/optional-epitran-smoke-2026-10-24 | Workflow [40092717790](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40092717790) and artifact inspected; six outputs, zero errors; package/mapping hashes recorded | 0 verified gold entries; exact-match count/accuracy null | DONE_VERIFIED for raw-output smoke; BLOCKED for accuracy by gold corpus | Preserve artifact; obtain exact source locators and independent adjudication before any scoring; do not infer accuracy from these six structural probes |
| myG2P data | License risks documented; dictionary not bundled | Licensing review is documentary | Not applicable | DONE_VERIFIED (non-bundling guardrail) | Do not import dictionary material absent separate permission and rights review |
| Project license | No root LICENSE; CITATION.cff uses NOASSERTION | Presence/absence documented | Not applicable | BLOCKED — owner decision | Owner selects code license and separately resolves corpus/data/model rights; do not infer from public visibility |
| CI / release readiness | CI configuration now includes schema and generated-artifact gates | CI run #259 passes: pytest (32), web data validation/build, generated-data drift, npm unit tests, and browser tests (40) | No end-to-end phonological validation | PARTIAL | Extend schema validation to all canonical evidence registries; obtain independent lexical IPA gold entries; run pinned Epitran only in a separate environment |

## Gold-corpus rules
1. Keep the six existing seed cases labelled STRUCTURAL_ONLY; they are not phonological gold.
2. A scoreable row must have GOLD_VERIFIED, non-empty expected IPA, a registered source ID, and a precise non-pending source locator.
3. The benchmark enforces non-empty IPA convention, scope/dialect, analysis level (phonemic vs surface phonetic), reviewer and uncertainty/alternative notes. Unit tests verify incomplete metadata is not scored.
4. Never fill expected IPA from the system under test, Epitran, or myG2P and then use that same output as independent truth.
5. Report exact-match and feature/category metrics only over the eligible gold set; show unresolved and unsupported cases separately.

## Reproducibility and license gates
- Epitran is a pinned comparator only. Do not promote it to the primary engine based on agreement with its own mapping or unverified outputs.
- Preserve raw Epitran output and separately hash installed package metadata, map, preprocessor and postprocessor where available.
- Keep third-party code, maps, dictionary, model weights, source text and generated artifacts as separate rights-bearing categories.
- No root license should be added until the owner decides. A public repository is not a license grant.

## Execution evidence and limitations
This register was prepared from the current README, both named audits, the seed corpus, src/burmese_ukrainian/ipa.py, src/burmese_ukrainian/parser.py, tests/test_parser.py, tests/test_practical.py, and scripts/benchmark_g2p.py. Remote inspection confirmed branches main, final-hardening, fix/adversarial-burmese-phonology, and service-ready; they were not modified or merged. This work is on feat/burmese-phonology-coverage-gates-2026-10-21 and is tracked by open draft PR #4; it has not been merged.

Automated CI run #259 (commit 1045735c244e96c898c3a675f15ad68f6b79151a) completed SUCCESS: editable package install PASS; pytest PASS (32 tests, including JSON Schema checks); npm install PASS; npm run build PASS; canonical web-data validation PASS; generated-data drift check PASS; Playwright installation PASS; npm run test:browser PASS (40 tests). The shared Unicode fixture is exercised in the browser. The Epitran benchmark was not run. The project remains a partial research prototype, not release-ready. Independent gold validation remains blocked; project licensing remains an owner decision.

## Website publication

| Layer | State | Evidence | Remaining acceptance criterion |
|---|---|---|---|
| Public disclosure | PARTIAL pending deployment | Homepage and methodology page now disclose the research-preview status, 0 verified lexical IPA gold entries, and 6 structural-only probes; a browser regression asserts the notice and matrix link | Merge only after CI passes, verify GitHub Pages deployment and live page content |


## External comparator execution update — 2026-10-24

A manually dispatchable/path-triggered workflow was added on branch ci/optional-epitran-smoke-2026-10-24 to install Epitran 1.35.3 in an isolated CI job and preserve the raw JSON report as an artifact. This improves reproducibility of the candidate smoke run but does not change the research status: the six current rows remain STRUCTURAL_ONLY, verified gold count remains zero, and accuracy must remain null. Mark the smoke run DONE_VERIFIED only after CI succeeds and the artifact's raw outputs, version, mapping hash, and error status are inspected.


## Epitran smoke run — 2026-10-24

- The first optional workflow run [40092549134](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40092549134) failed after package installation due an `UnboundLocalError`: an in-function `import importlib.resources` shadowed the module used for `importlib.metadata.version`. Fixed by importing `resources` directly, then added a regression guard.
- Successful rerun: [40092717790](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40092717790), Epitran 1.35.3 / Python 3.12.15, 6/6 raw outputs, 0 errors. Corpus SHA-256 `bc7d4f138581b7cfd48594b41891a26ec45123ea4488af977b48567201f0b19b`; mapping SHA-256 `de8660a0cdccb4192993d423342ad775a59ade19b8081829eb70da18f291dfe4`; artifact SHA-256 `1ca54b638897f41f124147df0744f9929e651757b720552082d701748794e475`.
- Raw outputs include `ကေ → ke`, `ကော် → kaʊʔ`, `ကြည် → t͡ɕi`, `စွယ် → səwɛ`, `မြန် → məjaɴ`, `ယူ → ju`. These are preserved as candidate outputs, not adjudicated IPA truth. Verified gold count is 0; exact-match count and accuracy are null. Epitran does not reconstruct tone in this mapping and the present corpus cannot support an accuracy claim.


## Final reproducibility record — 2026-10-24

- Current-head verification [40093021155](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40093021155) passed: pytest, web build, generated-data drift check, npm tests and Playwright browser tests all succeeded.
- Current-head raw-output run [40093021146](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40093021146) passed. Epitran 1.35.3 / Python 3.12.15; corpus path `data/burmese/phonology_corpus.csv`; corpus SHA-256 `bc7d4f138581b7cfd48594b41891a26ec45123ea4488af977b48567201f0b19b`; mapping SHA-256 `de8660a0cdccb4192993d423342ad775a59ade19b8081829eb70da18f291dfe4`; empty preprocessor SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; postprocessor SHA-256 `0eac185c50b19b7c2682d1395afad97a7662a5ff22e2344195eb0d3ffcbed7af`; artifact ZIP SHA-256 `6abad56759caa47868dee8af5e82068c143f810336454099ba9c149dc74e8f09`.
- Six structural probes yielded `ke`, `kaʊʔ`, `t͡ɕi`, `səwɛ`, `məjaɴ`, `ju`. Gold count 0; exact-match count and accuracy null. This is a reproducible smoke run, not an accuracy result.


## Final reproducibility record — 2026-10-24

Current-head verification run 40093021155 passed: pytest, web build, generated-data drift check, npm tests, and Playwright browser tests. Current-head raw-output run 40093021146 passed with Epitran 1.35.3 / Python 3.12.15. The six structural probes produced raw candidate outputs only; verified gold count is zero and accuracy remains null.

Corpus path is relative: data/burmese/phonology_corpus.csv. Corpus SHA-256: bc7d4f138581b7cfd48594b41891a26ec45123ea4488af977b48567201f0b19b. Mapping SHA-256: de8660a0cdccb4192993d423342ad775a59ade19b8081829eb70da18f291dfe4. Preprocessor is empty (SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855). Postprocessor SHA-256: 0eac185c50b19b7c2682d1395afad97a7662a5ff22e2344195eb0d3ffcbed7af. Artifact ZIP SHA-256: 6abad56759caa47868dee8af5e82068c143f810336454099ba9c149dc74e8f09. This is a reproducible smoke run, not an accuracy result.


## Merge and final acceptance record — 2026-10-24

PR #9 merged at `b71e2075b1e7dcebd17b54164bc017eb99eececd`. The raw-output smoke and full verification suite passed on the code-tested head; the report hashes the corpus and Epitran mapping/pre/post resources and keeps the gold denominator at zero. The raw-output task is DONE_VERIFIED; accuracy and source-adjudicated corpus tasks remain BLOCKED/TODO.


Authoritative readiness checkpoint — 2026-10-24 12:38 UTC

- Current main HEAD: b7a44e6e0ff7ec0010d58c30c2ceb0101e72761b.
- Engineering verification: DONE_VERIFIED. Current-main tests 40093806758 and Pages deploy 40093806746 both passed. Test suite includes Python, generated-data drift, npm, build and Playwright checks.
- Epitran smoke: DONE_VERIFIED as raw-output execution only. Pinned Epitran 1.35.3 / Python 3.12.15; six structural probes; zero runtime errors; artifact SHA-256 6abad56759caa47868dee8af5e82068c143f810336454099ba9c149dc74e8f09. Verified independent gold count 0 and accuracy null.
- Remaining TODO/BLOCKED: independent IPA gold corpus, tone-aware validation, lexical/context coverage, and source adjudication of candidate outputs. Do not add Epitran as a runtime dependency or call these six probes an accuracy benchmark.
- Readiness: engineering prototype verified; not empirically accuracy-certified or release-ready as a complete transcription engine.

## Authoritative current-head checkpoint — 2026-10-25

This checkpoint supersedes older baseline SHAs and statements that the current-head smoke/CI were still pending.

- Current `main`: `32f6f3da9328aa96e746d63b63912c4e64793646`.
- Current-main tests [40128844973](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40128844973): `success`; Pages deployment [40128844976](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40128844976): `success`; optional Epitran smoke [40128845097](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40128845097): `success`.
- PR #22's documentation correction is merged. The earlier stale instruction to run Epitran has been replaced with observed smoke evidence.
- Epitran remains a raw-output comparator only: six structural probes, zero runtime errors, no adjudicated gold, and no accuracy estimate. No production dependency or external corpus was added.
- Engineering workflow is DONE_VERIFIED for the recorded current head. Phonological coverage, Python/browser engine parity, independent source-adjudicated gold, tone-aware evaluation and license-owner decisions remain PARTIAL/BLOCKED as recorded above. The repository is not an accuracy-certified general-purpose transcription engine.

## Latest verified smoke evidence — 2026-10-25

- Current-main smoke [40134067758](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40134067758) and artifact [12576415800](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40134067758/artifacts/12576415800) were inspected. ZIP SHA-256: `6ff7fd5d70f386d76eefb37d50d2718d9de3f4e410749cf94848af9afeab788c`; 6/6 outputs, 0 runtime errors, Epitran 1.35.3 / Python 3.12.15.
- All six corpus rows remain STRUCTURAL_ONLY, so verified gold count is 0 and accuracy null. Raw-output execution is DONE_VERIFIED; phonological accuracy remains BLOCKED by missing source-located independent adjudication.
- PR #24 narrowed automatic smoke triggers to executable input/source/script/workflow changes; evidence-only registry/doc updates no longer trigger another optional run.


## Empty-input API contract — 2026-10-25

- Found a top-level API bug: `parse_burmese("")` previously returned `status="ok"` because Python's `all([])` is true, even though no syllable was analyzed.
- Empty and whitespace-only input now return `status="empty_input"`, preserving normalized input but producing no graphemes/syllables.
- This is an API status correction, not a pronunciation rule. Exact-head CI must pass Python tests, schema checks, build and browser tests.


## Evidence-registry schema checkpoint — 2026-10-25

- PR [#39](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/39) merged as `8a2482535c463a9371f7c0c6ac32c15880b7485c`.
- Added explicit JSON Schemas for source registry records and phonological rule records; expanded the existing claim schema to match the canonical `source_claims.csv` fields (`evidence_type` and `scope` included).
- The test now validates every canonical source, claim and implemented rule row, unique identifiers, and referential integrity from source → claim → rule. The test-first checkpoint failed for the intended missing-schema reason in [40222025229](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40222025229); final exact-head verification passed in [40222099466](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40222099466) and [40222096239](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40222096239).
- This closes a provenance validation gap, not a phonological one. The six corpus rows remain structural-only; independent lexical IPA gold count is still 0. Next acceptance criterion: add a schema and integrity checks for `phonology_corpus.csv`, with explicit allowed evidence statuses and a rule that structural-only rows cannot carry gold IPA or Ukrainian output.


## Corpus evidence-schema checkpoint — 2026-10-25

- PR [#41](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/41) merged as `3c8f03957fb3d8b8201bafac0dcdc819f50b8fe1`.
- Added `schemas/phonology_corpus.schema.json` and validates every row of `data/burmese/phonology_corpus.csv`. The schema constrains evidence statuses and enforces that `STRUCTURAL_ONLY` records have empty IPA/Ukrainian gold fields; `GOLD_VERIFIED` records require IPA convention, scope, analysis level, reviewer and uncertainty metadata. Tests also check unique case IDs, source references and non-pending locators for gold rows.
- Exact-head full workflow [40222516985](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40222516985) passed pytest, npm build, generated-data checks, Node tests and Playwright browser tests.
- All six existing rows remain `STRUCTURAL_ONLY`; the new schema deliberately does not promote them to phonological gold. Independent lexical IPA gold count remains 0 and accuracy remains unmeasured.


## Unicode corpus locator checkpoint — 2026-10-25

- PR [#43](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/43) merged as `0c793b76f45261c9d9044e0eac01245a8afef54f`.
- Updated the U18 source registry title/scope and replaced the three stale locator placeholders with exact `Unicode 18.0.0 Chapter 16 §16.3.1, Table 16-4` references for `ကေ`, `ကော်`, and `ယူ`.
- These rows remain `STRUCTURAL_ONLY`; expected IPA and Ukrainian fields remain empty. The Unicode chapter's example `ကော် /kaw/` is cited as a locator, not copied as gold.
- Exact-head full CI [40223402689](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40223402689) passed all tests, generated-data checks, Node and browser tests. Optional Epitran raw-output comparison [40223406632](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40223406632) completed successfully but is not an accuracy benchmark.
- Green 2002 rows remain source-locator-pending; independent lexical IPA gold remains 0.


## Evidence update — 2026-10-25

The misplaced-virama guard now has an explicit source → claim → rule → test link through `CLM-ORTH-001` / `MALFORMED_VIRAMA_WITHHOLD_IPA`. Unicode establishes script/syllable structure, not the pronunciation of malformed input. The implementation continues to return invalid status and withhold IPA.


## Shared Ukrainian target adaptation — 2026-10-30

| Task | Status | Evidence / acceptance |
|---|---|---|
| Preserve Burmese aspirated IPA in Ukrainian practical output | DONE_VERIFIED | /kʰ tʰ pʰ sʰ/ → к' т' п' с'; /tɕʰ/ → ч'. Source IPA remains unchanged. |
| Distinguish /h/, /ɡ/ and /x/ | DONE_VERIFIED | /h/ → г, /ɡ/ → ґ, genuine /x/ → х in the canonical practical registry and rules. |
| Preserve affricate identity | DONE_VERIFIED | /tɕ/ → ч, /dʑ/ → дж; no grapheme-based inference. |
| Preserve /ʔ/ as distinct from aspiration | DONE_VERIFIED | /ʔ/ remains ∅ in practical output and never receives the aspiration apostrophe. |
| Keep the dental-fricative candidate evidence-gated | DONE_VERIFIED | The existing grouped /θ~ð/ → т candidate is restored as ANALYSIS_DEPENDENT with its comparator provenance; no claim of exact phonetic identity. |

Exact PR-head workflow [41075332863](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41075332863) passed pytest, generated-web-data drift, production build, Node tests and Playwright browser tests. PR #49 remains draft; existing PR #48 was left untouched. Branch head: `e43c4e0121d9f29bc942e5f470d795c114c2085e`.

These are owner-approved Ukrainian target-policy decisions, not external linguistic sources or a normative Ukrainian standard. The change does not add Burmese phonological gold. Independent adjudicated lexical IPA gold remains 0; accuracy remains unmeasured. Remaining TODO/BLOCKED work on full Burmese tone/register/phonation, coda/vowel coverage and independent lexical validation is unchanged.


## Romanization profile and crosswalk decision — 2026-10-31

| Task | Status | Evidence / acceptance |
|---|---|---|
| Select orthographic Burmese romanization profile | DONE_VERIFIED (source review) | MLCTS is explicitly described by Mya2Rom upstream as an orthographic transcription system created by the Myanmar Language Commission; modified MLCTS / MLCTS2 is more phonetic. |
| Align browser romanization mode with selected MLCTS profile | TODO | Change mya2rom(..., "mlcts2") to "mlcts", update UI label and exact-output browser regression; run full exact-head CI and Pages checks. |
| Build MLCTS → Ukrainian syllable crosswalk | TODO | Separate adapter and provenance-bearing source → MLCTS → Ukrainian rows; do not reuse IPA mapper. |
| Complete MLCTS correspondence inventory | PARTIAL | Cover consonants, medials, vowels, codas, independent vowels, kinzi, asat, numerals and punctuation with source locators and explicit unsupported states. |
| Audit Mya2Rom provenance and redistribution | PARTIAL | Preserve CC-BY-SA-4.0 notices; verify each copied code/data component and upstream-derived table source. |

This is a method-selection and research-matrix update only. It does not add IPA gold or claim phonological accuracy. Current independent adjudicated lexical IPA gold count remains 0.


## Production Pages artifact gate — 2026-10-31

| Task | Status | Evidence / acceptance |
|---|---|---|
| Copy Mya2Rom browser assets into Vite public output | DONE_VERIFIED (PR candidate) | scripts/copy-vendor-assets.mjs copies romanisations.js and mya2rom.js; artifact test verifies both files in dist |
| Include methodology page in production build | DONE_VERIFIED (PR candidate) | Vite multi-page input includes index.html and system.html; artifact test verifies dist/system.html |
| Test browser behavior against production artifact | DONE_VERIFIED (PR candidate) | Playwright preview server uses vite preview; browser asserts window.mya2rom exists and methodology navigation works |
| Post-merge GitHub Pages deployment | DONE_VERIFIED | Main commit fff943db823ae5ca0f4fed50b572cc75cb743f84 deployed successfully by workflow 41231199596 to https://clippyfirst.github.io/Burmese-Ukrainian-Phonetic-System-/ |

Test-first RED: [41230779647](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41230779647) failed because the production artifact omitted system.html. Exact-head GREEN: [41230976020](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41230976020) passed: pytest 63 + 29 subtests; Node 3/3; Playwright 48.




## Final main / Pages checkpoint — 2026-10-31

- Final main commit: fff943db823ae5ca0f4fed50b572cc75cb743f84.
- PR #54: MLCTS profile and onset matrix; PR #55: two separate method tabs; PR #56: production asset copy, multi-page build and preview-based browser tests.
- PR #48 was closed as superseded by #56; its old branch was left intact. PR #53 styling work remains open and untouched.
- Main verification [41231199684](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41231199684) passed: pytest 63 + 29 subtests; Node 3/3; Playwright 48 against the built artifact.
- Pages deployment [41231199596](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41231199596) succeeded: https://clippyfirst.github.io/Burmese-Ukrainian-Phonetic-System-/ .
- Final statuses: MYA-ROM-PROFILE-001 DONE_VERIFIED; MYA-ROM-MATRIX-ONSET-001 DONE_VERIFIED; MYA-ROM-MATRIX-001 PARTIAL; MYA-ROM-UA-001 TODO; MYA-PAGES-ARTIFACT-001 DONE_VERIFIED; MYA-PHONETIC-COVERAGE PARTIAL/BLOCKED pending independent lexical gold and expert adjudication.
- The romanization tab's Ukrainian result is intentionally PARTIAL. Do not claim full romanization coverage until a complete source → MLCTS → Ukrainian syllable matrix and adapter pass exact coverage tests.


## Browser output integrity and full-sentence regression — 2026-10-31

| Task | Status | Evidence |
|---|---|---|
| Preserve unresolved/unsupported Burmese source units in Ukrainian browser output | DONE_VERIFIED | PR [#64](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/64) merged as `d0b7f6351a4151b974ec9ee379f81f7a06da9613`; unresolved units now render as `⟦source⟧` rather than disappearing or exposing incomplete per-syllable mappings |
| Preserve supported contextual initial /j/ + vowel rendering | DONE_VERIFIED | Existing `/juː/ → ю` browser regression remains green after correcting status aggregation for the contextual target |
| Full user-supplied Burmese greeting sentence source reconstruction | DONE_VERIFIED | Playwright reconstructs the normalized sentence from rendered source-unit rows and asserts exact equality; unresolved Ukrainian units remain explicitly marked |
| Full Burmese phonetic/target accuracy for the sentence | BLOCKED / EVIDENCE_LIMITED | No independent lexical IPA gold and no complete Ukrainian mapping inventory; do not infer missing pronunciations or spellings to force a full output |

Exact final PR-head workflow [41238825573](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41238825573) passed: pytest 64 + 29 subtests, Node 4/4, Vite build, generated-data drift check, and Playwright 50/50 against the built artifact. The Pages workflow [41238926334](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41238926334) completed successfully and deployed merged main `d0b7f6351a4151b974ec9ee379f81f7a06da9613` to https://clippyfirst.github.io/Burmese-Ukrainian-Phonetic-System-/. Main verification [41238926148](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41238926148) also completed successfully.


## Mixed-text and unsupported-source preservation — 2026-10-31

| Task | Status | Evidence / acceptance |
|---|---|---|
| Python parser exact source reconstruction for mixed sentences | DONE_VERIFIED (PR-head evidence) | PR #74 merged as `6ec5c6a15af45fce5d993933c3c429d8e9a82c79`; exact-head workflow [41244535813](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41244535813) passed all configured Python, Node, build, generated-data and Playwright steps. Tests cover Latin text, ASCII digits, Burmese digits, Myanmar punctuation and exact source-unit reconstruction. |
| Python withholding for unsupported Myanmar Extended-A adjacent to a valid syllable | DONE_VERIFIED (bounded parser behavior) | Regression asserts the complete raw cluster is preserved and status is `partially_unparsed`; no unsupported unit is silently dropped or promoted to IPA. |
| Exact post-merge main verification and Pages deployment | IN_PROGRESS / BLOCKED pending CI | Main SHA `6ec5c6a15af45fce5d993933c3c429d8e9a82c79`; runs [41245969998](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41245969998) and [41245969938](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41245969938) were queued at checkpoint time. Acceptance: both exact-SHA workflows complete successfully; Pages smoke test confirms deployed runtime assets. |

These are source-integrity regressions, not evidence of Burmese IPA accuracy, full Unicode coverage, or completion of the MLCTS → Ukrainian adapter. Independent lexical IPA gold remains 0.


## Post-merge CI evidence correction — 2026-10-31

- PR #74's post-merge main tests [41245969998](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41245969998) and Pages deployment [41245969938](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41245969938) completed successfully on `6ec5c6a15af45fce5d993933c3c429d8e9a82c79`; deployed-site/runtime smoke test passed. This supersedes the earlier queued status in the preceding checkpoint.
- The subsequent documentation-only PR #75 merged as `48bb45cf2a5c6cc95057fecacdfbc6e852b760b1`; exact PR-head tests [41246079334](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41246079334) passed. Its post-merge exact-main tests [41246294703](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41246294703) and Pages [41246294821](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41246294821) were still running at this checkpoint.


## Final main verification correction — 2026-10-31

- Exact-main tests [41246294703](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41246294703) and Pages [41246294821](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41246294821) completed successfully on `48bb45cf2a5c6cc95057fecacdfbc6e852b760b1`. The earlier in-progress note above is superseded; deployed-site/runtime smoke test passed.
- Follow-up documentation PR-head verification remains required before merge.


## External G2P candidate register update — 2026-11-01

| Candidate | Status | Evidence / acceptance |
|---|---|---|
| Goruut | PARTIAL — upstream advertised support only | Pinned source commit `b224bde02151f8f86d0fe260804e4ca743bda620`; README lists Burmese and an IPA phone set. No syllable tokens or tie bars; numbers/dates unsupported. MIT source-code license verified, embedded asset licenses not yet audited. Run in isolated optional CI and retain raw output before considering further use. |
| Epitran 1.35.3 | DONE_VERIFIED as raw-output smoke only | Existing six structural probes and resource hashes remain diagnostic; documented limited Burmese support; independent gold remains 0. |
| myG2P | BLOCKED for commercial redistribution absent rights decision | Upstream license is CC BY-NC-SA 4.0; do not vendor into the commercial runtime absent permission/legal review. |

No accuracy score or engine winner is available. Promotion requires independent expert-adjudicated IPA and a separate license/provenance audit for all model and dictionary assets.


## 2026-11-01 exact-head runtime update — Goruut

| Task | Status | Evidence | Acceptance / blocker |
|---|---|---|---|
| MYA-GORUUT-RUNTIME-001 | PARTIAL | PR #82 exact head `d8b065bc66dce5fdd9959c4f0eb932a29acaedba`; [runtime workflow 41310771082](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41310771082); artifact ZIP SHA-256 `0eb19d7079de818736ecff095f700405fc4b46de3791dd6e4fd68762346218fa` | Pinned Go build succeeds; 7/8 usable Goruut outputs, 6 stable and 1 unstable; punctuation probe has no output. Epitran 1.35.3 returns 6/6; raw exact match 0/6. Accuracy remains null, independent gold=0. |
| MYA-GORUUT-ASSET-WARNING-001 | BLOCKED | Runtime server log in artifact; `weights9.bin.zlib` missing while pinned tree has `weights8.bin.zlib` | Diagnose upstream loader/asset path and determine whether it affects output; no causal claim yet. |
| MYA-PHONETIC-GOLD-001 | TODO | Current source triage audit | Create independently double-annotated, adjudicated audio-backed IPA gold with dialect/speaker metadata; no engine scoring until then. |

The exact-head results supersede earlier one-shot claims of full stability: `ကြည်` varied between `tɕì` and `tɕɪ̀ɴ` across repeated requests. No external engine is selected as production provider.


### Goruut nondeterminism root cause and report contract

Pinned upstream `SelectE` counts multiple dictionary pronunciations and, when no homograph-model preferred entry is selected, falls through to a random dictionary pronunciation. The upstream source comment names this behavior; the response counters `RandomizationWordsCount` / `RandomizationWordsChoices` are populated by the sentence use case. Exact sources: [selector](https://github.com/neurlang/goruut/blob/b224bde02151f8f86d0fe260804e4ca743bda620/repo/services/parts_of_speech_selector_service.go#L168-L205), [counter propagation](https://github.com/neurlang/goruut/blob/b224bde02151f8f86d0fe260804e4ca743bda620/usecases/phonemize_usecase.go#L84-L85).

The latest Burmese artifact shows the only unstable input `ကြည်` carried these counters on all three repetitions (1 ambiguous word, 2 choices); the other seven inputs had no ambiguity metadata. The optional benchmark script now parses and aggregates those counters as randomized input/repetition counts while leaving accuracy null. This is an ambiguity signal, not a claim that all homographs are incorrect. The missing `weights9.bin.zlib` warning is separate and its causal relationship remains unproven.


### Source-coverage gate update — 2026-11-01

| Task | Status | Evidence | Acceptance / blocker |
|---|---|---|---|
| MYA-GORUUT-SOURCE-COVERAGE-001 | PARTIAL | Exact-head artifact 13085043436; raw-output re-analysis | 7/8 Goruut outputs passed source-field reconstruction and punctuation-field letter checks; one punctuation sentence returned no output. Eight probes do not establish broad coverage. |
| MYA-GORUUT-RANDOMIZATION-REPORT-001 | PARTIAL | Pinned upstream selector source; test-first assertions added | Harness parses RandomizationWordsCount/Choices and has coverage tests. Exact-head CI for the new parser is pending. |

The source-coverage contract reconstructs the input from PrePunct + CleanWord + PostPunct after NFC/whitespace removal and flags letters, combining marks or numbers left in PrePunct/PostPunct. This is a coverage check, not phonetic accuracy. The new implementation must pass CI before the task can be marked DONE_VERIFIED.


### myG2P v2.0 100-row comparison — PARTIAL, CI pending

| Task | Status | Evidence | Acceptance / blocker |
|---|---|---|---|
| MYA-MYG2P-PARSER-001 | PARTIAL | `scripts/prepare_myg2p_probe.py`; `tests/test_prepare_myg2p_probe.py` | Parses pinned five-column dictionary, tracks malformed/missing/duplicate rows, creates deterministic 100 unique source-located rows, and labels them SOURCE_ATTESTED_NOT_GOLD. Exact-head test CI pending. |
| MYA-MYG2P-COMPARISON-001 | PARTIAL | Optional Goruut workflow now checks out myG2P commit `54b5c76bb5a87fdbaaeddc1892e6ebd8f97ee225`; same 100 rows go to Goruut (3 repeats) and Epitran 1.35.3 | Await exact-head runtime artifact. Report raw outputs, coverage, randomization and source-attested concordance only; accuracy must remain null and independent gold=0. |

The user explicitly authorized temporary test-only use regardless of upstream license review. The dictionary is not committed to this repository or bundled into product runtime. Per-entry IPA is source-attested, not independently adjudicated gold.


### Repeat-run reconciliation — 2026-11-01

The first independent 8-probe run (artifact 13085043436) showed one unstable output for `ကြည်`; the later run [41312361052](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41312361052) showed the same word stable across three repeats but retained `RandomizationWordsCount=1` and `RandomizationWordsChoices=2` in every response. Thus a stable three-sample result does not remove the upstream ambiguity: random choice may happen to repeat the same candidate. The later run classified 7/8 as complete source coverage and one punctuation sentence as no output. The source-coverage and randomization gates must both pass before any source-attested comparison; no gold/accuracy claim.


### Final myG2P / Goruut exact-head verification — 2026-11-01

| Task | Status | Evidence | Acceptance / blocker |
|---|---|---|---|
| MYA-MYG2P-PARSER-001 | DONE_VERIFIED | PR #82 head `dcd9dfb6f1306ce01547f922238aba3fdefd6586`; tests workflow [41313487752](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41313487752) PASS; `scripts/prepare_myg2p_probe.py`; parser tests | 24,802 physical lines; 24,009 unique IPA entries; 793 duplicate headwords skipped; 0 malformed and 0 missing-IPA rows. Deterministic 100-row source-located probe generated; not gold. |
| MYA-MYG2P-COMPARISON-001 | DONE_VERIFIED | Runtime [41313487703](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41313487703) PASS; artifact [13086900774](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41313487703/artifacts/13086900774), SHA-256 `ca165ac84ee6b284a423a988a5ee32d951a883c36073b01fd5f086ba83022f77` | Goruut 98/100 outputs; 43 complete / 55 partial / 2 unknown; 98 stable; 0 randomized; 69 unphonemized fragments; strict source concordance 0/100 and limited notation diagnostic 17/100. Epitran 1.35.3 raw output captured. Accuracy=null, independent gold=0. |

**Evidence boundary:** myG2P declares CC BY-NC-SA 4.0 and remains temporary test-only input under explicit owner authorization. It is not copied into product data or runtime. Source labels are not independently adjudicated gold; neither raw engine agreement nor dictionary concordance establishes accuracy. The 8-case engineering probe separately had 7/8 outputs, 7 complete, 1 unstable/randomized and 1 no-output. Production promotion remains blocked pending qualified expert IPA gold and dialect/profile adjudication.


### Final exact-head evidence correction — 2026-11-01

The final PR #82 runtime [41324681722](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41324681722), artifact [13090128004](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41324681722/artifacts/13090128004), supersedes the previous 8-case wording: 7/8 outputs, 7/7 complete and stable, 1/8 carried upstream dictionary-randomization metadata despite identical output across the three sampled repeats, 1/8 no output. The 100-row myG2P comparison remains 98 outputs, 43 complete / 55 partial / 2 unknown, 98 stable, no randomization metadata, 69 unphonemized fragments, 0 strict and 17 limited-notation source-label matches. These are not accuracy; independent gold=0. The downloaded archive SHA-256 matches the GitHub digest.


### Session closeout — PR #82 merged, 2026-11-01

- PR #82 merged into `main` as `e9c83322f304a670dd25e121dcc5b60e1cf3a896`.
- Post-merge pytest, npm build, generated-data validation, Node tests and Playwright built-browser suite: [41326238767](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41326238767) PASS. Pages build/deploy and deployed-site/runtime smoke test: [41326238774](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41326238774) PASS.
- MYA-MYG2P-PARSER-001 and MYA-MYG2P-COMPARISON-001 remain DONE_VERIFIED as temporary research tooling, not production phonology. The 100-row diagnostic is 98/100 outputs, 43 complete / 55 partial / 2 unknown, 98 stable, 0 randomization metadata, 69 unphonemized fragments, 0 strict / 17 limited-notation matches. Source labels remain not-gold; independent gold=0, accuracy=null.
- Remaining blocker: qualified expert-adjudicated, dialect-scoped Burmese IPA gold and review of the partial-coverage cases. No model/data redistribution is authorized by test-only use.


## Current status override — 2026-11-01

This current-head reconciliation supersedes older status cells above where they conflict; the dated historical checkpoints remain intact.

| Workstream | Current status | Acceptance / blocker |
|---|---|---|
| Independent lexical IPA gold | BLOCKED | `data/benchmark/gold.tsv` is header-only; independent gold=0 and accuracy=null. Requires licensed audio/source, dialect/speaker metadata, two independent IPA annotators and adjudication. |
| Consonant, kinzi and medial phonology | PARTIAL | Structural parsing exists; source-backed contextual phonological coverage and a differential corpus remain incomplete. |
| Vowel combinations and coda realization | PARTIAL | Full vowel derivation, checked-syllable and contextual coda realization are not implemented. |
| Tone/register/phonation | TODO | Specialist adjudication of competing analyses and scoped implementation are required; do not infer or collapse them. |
| IPA → Ukrainian | PARTIAL | Canonical external inventory boundary exists; target policies remain proposal-level and need expert review. |
| MLCTS → Ukrainian | TODO | Separate source-aware orthographic adapter is not implemented; verify MLCTS rules against primary MLC sources. |
| Goruut/myG2P/Epitran harness | DONE_VERIFIED (diagnostic only) | Parser, comparison and runtime artifacts verified; 55/100 Goruut outputs partial; myG2P remains temporary test-only under CC BY-NC-SA 4.0. No accuracy or production claim. |
| Python/browser phonological parity | TODO | Existing source-preservation parity does not establish phonological result parity; add shared expert-backed phonology fixtures. |
| Manual UI/accessibility QA | TODO | Deployed visual, keyboard, screen-reader and mobile QA not evidenced by CI. |
| Release readiness | PARTIAL | Blocked by gold, phonological coverage, primary-source and asset-rights gates. |


## Independent IPA gold corpus status — 2026-11-01

| Task | Status | Acceptance / blocker |
|---|---|---|
| IPA-GOLD-SCHEMA-001 | DONE_VERIFIED | Four JSON Schemas, empty JSONL templates and cross-file validator |
| IPA-GOLD-DOUBLE-ANNOTATION-001 | PARTIAL | Enforces two distinct annotators and third adjudicator; blind human collection remains external |
| IPA-GOLD-ADJUDICATION-001 | PARTIAL | Agreement/resolved/unresolved semantics verified; no real adjudicated examples |
| IPA-GOLD-SPLIT-001 | DONE_VERIFIED | Deterministic frozen lexeme-group splits and regression tests |
| IPA-GOLD-EXPORT-001 | DONE_VERIFIED | Rights-filtered export to existing benchmark contract; current output header-only |
| IPA-TYPED-BENCHMARK-001 | DONE_VERIFIED | IPA kind mismatch is not scored as exact match |
| IPA-GOLD-RELEASE-GATE-001 | PARTIAL | Tag/manual gate requires 100/25/25 gold; repository ruleset/release procedure must require it |
| BURMESE-ORTHO-KINZI-MEDIAL-001 | PARTIAL | Unicode structure documented; complete mapping and adversarial coverage open |
| BURMESE-VOWEL-CODA-001 | PARTIAL | Sonority/coda-conditioned vowel model needs expert-backed matrix |
| BURMESE-TONE-PHONATION-001 | TODO | Tone vs phonation vs segmental glottal closure requires specialist adjudication |
| BURMESE-PYTHON-BROWSER-PHONOLOGY-PARITY-001 | TODO | Requires shared expert-backed IPA fixtures |

**Gold status:** 0 independent adjudicated records; `gold.tsv` header-only; accuracy=null. The new workpack is a research specification, not completed phonological coverage.


Additional current controls:
- `IPA-GOLD-RIGHTS-001` — DONE_VERIFIED (mechanism): allowlisted license registry, required per-record rights evidence and non-redistributable license rejection. Source-by-source legal review remains required.
- `IPA-GOLD-PROVENANCE-EXPORT-001` — DONE_VERIFIED: export and benchmark report preserve source ID, license ID and rights-evidence locator.
- `IPA-GOLD-BLIND-INTAKE-001` — BLOCKED: qualified annotators and a controlled blind intake channel are not connected; public Git history cannot enforce blinding.


## CI action runtime modernization — 2026-11-01

| ID | Status | Evidence | Scope / acceptance |
|---|---|---|---|
| BUR-CI-ACTIONS-001 | DONE_VERIFIED | Code commit `a1ef4e13105937cd282e6edd67020a74207f649b`; exact-head [tests 41339669408](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41339669408) and [Epitran diagnostic 41339669397](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41339669397) both SUCCESS | All five workflow files use current Node.js 24-compatible action majors; Python, Node, build, generated-data, and 54 Playwright browser checks passed. No phonological behavior changed. |
