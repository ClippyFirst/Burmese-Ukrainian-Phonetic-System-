# Burmese phonology execution status matrix

Updated: 2026-10-21
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
| Grapheme and syllable segmentation | Conservative Python parser and separate browser parser | Shared Unicode contract is exercised in Python and browser for supported-block vs unsupported-inventory cases; annotated differential corpus absent | 0 lexical gold entries established | PARTIAL | Add boundary-annotated corpus covering punctuation, mixed scripts, combining marks, malformed sequences; compare runtimes |
| Consonant/onset inventory | Small Python onset IPA table and graphemic inventory | Existing parser/IPA regression coverage is limited | No independently adjudicated inventory-wide lexical set | PARTIAL | Source-map each onset and test legal/unsupported contexts |
| Kinzi | Explicit structural recognition and role metadata | Structural regression coverage exists; contextual phonological tests incomplete | None established | PARTIAL | Source-located onset/medial/coda-context cases and cross-runtime assertions |
| Medials / complex onsets | Four medial signs parsed; some browser contextual derivation | Partial; full combination gold set absent | None established | PARTIAL | Inventory combinations, competing analyses, environments, counterexamples and paired Python/browser tests |
| Dependent/inherent vowels | Vowel signs parsed; small vowel-ID-to-IPA map | Structural tests exist; derivation coverage incomplete | None established | PARTIAL | Evidence-backed combination table and context/length/quality tests; no extrapolation from unverified patterns |
| Codas / checked syllables | Some final structures parsed; browser rime rules reported | Incomplete | None established | PARTIAL | Enumerate coda/rime classes, mark checked-syllable conditions, test each sourced class |
| Tone | Analysis registries document competing traditional and eight-tone/register analyses; no established runtime realization | Not adequately tested as a phonological layer | 0 tone-labelled gold entries established | TODO | Add scoped, source-located tone examples and separate phonemic category from surface F0 realization |
| Register / phonation | Competing literature descriptions documented | No complete runtime model verified | 0 independently adjudicated register/phonation entries | TODO | Model alternatives explicitly with dialect/scope and phonetic evidence; avoid consensus claims where sources disagree |
| Contextual rules / allophony | Partial browser hand-written cases | Rule-complete regression suite absent | None established | PARTIAL | Rule registry with source, environment, output, counterexamples and Python/browser parity tests |
| IPA result/status contract | Python and browser now both withhold IPA for unresolved anusvara (U+1036) rather than silently deleting it; exact regression covers `ကံ` | Targeted cross-runtime case passes in [CI run 40196136958](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40196136958); broad parity still incomplete | No lexical IPA gold entries | PARTIAL | Every result exposes phonological status independently of parse status; partial IPA must never be labelled complete; expand shared fixtures across coda, vowel, tone and malformed cases |
| IPA → Ukrainian target adapter | Canonical external inventory boundary and candidate registry; explicit unavailable/not-established paths | Practical regression tests exist | No Ukrainian name-level gold evaluation | PARTIAL | Validate adapter against canonical inventory schema and all correspondence policies; test unavailable dependency behavior |
| Feature-distance ranking | Candidate ranking implementation exists | Limited regression tests; final schema/feature validation not established | No empirical target-ranking validation | PARTIAL | Validate feature definitions and weights against canonical inventory; test deterministic ranking, ties, unknown features and missing inventory |
| Comparative Russian/Ukrainian policies | Comparative registries and documentary layer present | Practical tests cover selected correspondences | No independent name-level benchmark | PARTIAL | Check every rule provenance, target-language rationale, uncertainty and non-inheritance from Russian |
| Malformed/unsupported input | Structural and practical uncertainty outcomes exist | Some malformed virama and unknown-target tests | Not a lexical accuracy measure | PARTIAL | Adversarial tests for all API/CLI/browser entry points; no confident output after malformed or incomplete parse |
| JSON schemas / data validation / generated artifacts | Two JSON Schemas, canonical CSV registries and generated web data | CI validates parser records against the syllable schema, checks schema definitions, runs web CSV validation, and verifies generated-data drift | Structural/schema-contract checks only; no complete source-claim registry-to-schema mapping | PARTIAL | Define explicit schema mappings for all source/claim registries and validate every canonical record, not only parser fixtures |
| Python/browser parity | Separate implementations exist | Phonological differential coverage not established | None established | TODO | Shared fixtures and parity tests for structural state, uncertainty, IPA, and unsupported cases |
| Lexical IPA gold corpus | Six rows in data/burmese/phonology_corpus.csv remain STRUCTURAL_ONLY; columns now explicitly reserve IPA convention, scope, analysis level, reviewer and uncertainty notes | Benchmark gate and regression tests require all adjudication metadata plus registered source and non-pending locator | 0 verified gold entries; accuracy not measured | BLOCKED by source-located/adjudicated entries | Add independently sourced broad-IPA entries with exact source locators, transcription convention, scope, analysis level, reviewer and uncertainty notes; keep structural probes separate |
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
