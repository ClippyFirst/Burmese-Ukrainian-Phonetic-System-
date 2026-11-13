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
| IPA → Ukrainian target adapter | Canonical candidate inventory plus executable whole-string IPA → Ukrainian adapter in Python and browser; longest-match affricates, h/ɦ → г, ɡ/g → ґ (project choice), x → х, explicit ц/дз/ч/дж, aspiration notation, contextual /j/ yotation, prosody trace, fail-closed unknown segments; post-IPA integration in deterministic engine and public service | Python sequence tests; browser adapter tests include spaced IPA, untied consonant sequences and fail-closed unsupported structures; generated-data freshness, Node tests and built-site Playwright rerun queued on PR #133 (run 43095497303) | No Ukrainian name-level or independent lexical IPA gold evaluation | PARTIAL pending exact-head CI | Pass the full exact-head CI including built-site Playwright; retain empirical gold evaluation as separate blocker |
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
| Build MLCTS → Ukrainian syllable crosswalk | PARTIAL | Onset + 94 vendor-rime target rows are populated and tested on the task branch; complete source-verified Myanmar structures and a runtime syllable adapter remain open. Do not reuse IPA mapper. |
| Ukrainian target matrix coverage | DONE_VERIFIED | Exact-head test run [43221074232](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43221074232) passed: 187 Python tests + 66 subtests, 54 Node tests, build, generated-data freshness and built-site Playwright. 35 onset + 94 vendor-rime target rows are populated; source inventory remains EVIDENCE_LIMITED. |
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
| MYA-PHONETIC-GOLD-001 | BLOCKED / TEXT-ONLY EXPERT REVIEW | Current source and phonology audits | Create independently reviewed IPA examples from written dictionaries, lexical entries and published phonological descriptions, with source locators and a versioned broad/narrow convention. |

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
| Independent lexical IPA gold | BLOCKED | data/benchmark/gold.tsv is header-only; independent gold=0 and accuracy=null. Requires source-located written IPA/phonological evidence, a defined target variety, two independent text-based reviewers and adjudication. No audio. |
| Consonant, kinzi and medial phonology | PARTIAL | Structural parsing exists; source-backed contextual phonological coverage and a differential corpus remain incomplete. |
| Vowel combinations and coda realization | PARTIAL | Full vowel derivation, checked-syllable and contextual coda realization are not implemented. |
| Tone/register/phonation | TODO | Specialist adjudication of competing analyses and scoped implementation are required; do not infer or collapse them. |
| IPA → Ukrainian | PARTIAL | Canonical external inventory boundary exists; target policies remain proposal-level and need expert review. |
| MLCTS → Ukrainian | PARTIAL | Separate orthographic adapter is integrated for supported onset/rime combinations and y/r/w medials; unsupported forms are visibly withheld. Full acceptance requires primary MLC source verification and coverage of kinzi/asat/devoicing/independent-vowel structures. |
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


## Focused source audit and evidence-gate refinements — 2026-11-03

| Evidence / task | Status | Verified source result | Consequence / acceptance |
|---|---|---|---|
| MYA-ORTHO-SYLLABIFICATION-001 | PARTIAL (external evidence reviewed; not implemented as ClippyFirst G2P) | Hlaing & Mikami (2014), [Automatic syllable segmentation of Myanmar texts using finite state transducer](https://doi.org/10.4038/ICTER.V6I2.7150): rule-based FST; 11,732 orthographic words; 99.93% word-syllabification; consonant-stacking subset 245/253 correct (96.83%); text also discusses a free-standing-vowel error; article count inconsistency 32,238 vs 32,283 syllables. | This is orthographic segmentation, not G2P, phoneme or IPA accuracy. Use only as structural-parser comparator; test kinzi/stacked consonants explicitly. |
| MYA-TONE-VOWEL-ANALYSIS-001 | PARTIAL | Mooney & Repetti-Ludlow (2021), [Sonority and syllable structure: The case of Burmese tone](https://doi.org/10.3765/plsa.v6i1.4900): acoustic experiments from one Yangon speaker; proposes syllable-structure/sonority-conditioned vowel alternations and a competing underlying-tone analysis. | Preserve as competing analysis; do not collapse vowel quality into tone or replace traditional surface categories without qualified review. |
| MYA-CORPUS-SLR80-001 | PARTIAL | Oo et al. (2020), [Burmese Speech Corpus, Finite-State Text Normalization and Pronunciation Grammars with an Application to Text-to-Speech](https://aclanthology.org/2020.lrec-1.777): 2,528 utterances, 20 female Yangon speakers, 22,443 tokens, 9,941 unique words; corpus CC BY-SA 4.0; separate Thrax/WFST G2P grammar. | Orthographic speech corpus, not IPA gold; no public train/dev/test split or speaker-balanced IPA benchmark established. Verify grammar license separately. |
| MYA-PHONETIC-PROFILE-001 | PARTIAL | Watkins (2001), [Burmese](https://doi.org/10.1017/S0025100301002122), JIPA profile from one 30-year-old Yangon male reading slowly; Gruber (2011), [Perceptual Cues to Lexical Tone in Burmese](https://doi.org/10.3765/EXABS.V0I0.557), reports joint pitch/duration/phonation cues. | Use as profile and feature evidence, not multi-speaker population gold. Keep tone, phonation and duration typed and separately testable. |
| MYA-GOLD-AGREEMENT-001 | TODO | Cucchiarini (1996), DOI [10.3109/02699209608985167](https://doi.org/10.3109/02699209608985167); Oller & Ramsdell (2006), DOI [10.1044/1092-4388(2006/100)]. | Pilot reports exact normalized agreement plus alignment-aware feature-weighted agreement, separate tone/duration/phonation/vowel/coda/boundary diagnostics, unresolved alternatives and adjudication rate. Raw percentage agreement supplementary only. |

No lexicon rows, IPA labels, or model predictions were imported. Gold remains 0; accuracy remains null. The detailed source audit is also recorded in the current top-level handoff and linguistic completion register.


## Engineering test-harness status — 2026-11-04

| Layer / acceptance gate | Implemented coverage | Tested coverage | Independently validated coverage | Status | Next acceptance criterion |
|---|---|---|---|---|---|
| IPA corpus test-fixture language identity | Fixture uses Myanmar-script sample, `test-burmese` profile and neutral variety label; shared script-range constants are explicit in the test module | Regression asserts all fixture characters are in the Myanmar Unicode block and profile metadata matches the repository language; exact-main tests [41847895975](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41847895975) SUCCESS | Not applicable; this is test-data integrity, not phonological validation | DONE_VERIFIED | Preserve language-specific fixtures when adding shared corpus tests; do not infer phonological coverage from this check |

This engineering correction does not change the language-layer statuses above. Independent Burmese IPA gold remains 0; accuracy remains null.


## IPA gold release-gate corpus identity — 2026-11-04

| Task | Status | Evidence | Remaining acceptance |
|---|---|---|---|
| BURMESE-IPA-GOLD-PROFILE-GATE-001 | DONE_VERIFIED (engineering guard) | PR #117 merged as `085ce5a2da4a07dfbf606a9892c78a4d3bbb9d91`; exact-head tests [41870132273](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41870132273), post-merge tests [41870579420](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41870579420), and Pages [41870579398](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41870579398) SUCCESS. Shared validator rejects mixed adjudicated target profiles and mixed IPA kinds; positive regression confirms speaker/audio IDs may vary. | Human approval of Standard Yangon profile/convention, blind double annotation, independent adjudicator, rights-cleared source set, and specialist-reviewed onset × medial × vowel × coda × prosodic coverage remain outstanding. This guard does not create gold or prove accuracy. |

## Deterministic rule engine — 2026-11-11

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-DETERMINISTIC-RULE-ENGINE-001 | DONE_VERIFIED (engineering); linguistic coverage PARTIAL | PR #128 merged as `cd3a1503e79d32b09a6d2d5206340a37cfd3283b`; main tests [43018103155](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43018103155) and Pages smoke [43018103391](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43018103391) SUCCESS; live site published. | Deterministic engine published. Expert-adjudicated Yangon IPA gold still required for phonetic correctness/accuracy claims. |

## Final deterministic-engine verification — 2026-11-11

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-DETERMINISTIC-RULE-ENGINE-001 | DONE_VERIFIED (engineering); linguistic coverage PARTIAL | Final main head `9bece0a50a367f3f58336d2aba7016ac4af86156`; tests [43019216137](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43019216137) and Pages + smoke [43019216297](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43019216297) SUCCESS. | Deterministic runtime published; independent expert-adjudicated Yangon IPA gold remains outstanding. |


## Ukrainian practical transcription — 2026-11-11 continuation

- Python and browser output are both post-IPA adapters; the browser imports the generated correspondence and rule tables rather than maintaining a separate linguistic mapping table.
- The browser adapter uses longest-match for explicit affricates, preserves word spaces, treats syllable dots as boundaries, and applies Ukrainian yotation to /j/ at the start of each IPA syllable.
- The target policy distinguishes /h, ɦ/ → г, /ɡ/ (ASCII /g/) → ґ as a project-specific choice, and /x/ → х. It maps explicit /t͡s, d͡z, t͡ʃ, d͡ʒ/ to ц, дз, ч, дж; /tɕ, dʑ/ are practical approximations. Plain adjacent consonants are not collapsed into affricates.
- Aspiration is marked with a project apostrophe; /ʔ/ is omitted from ordinary practical spelling but remains in IPA/trace. Tone and length are retained analytically, not converted to Ukrainian stress or vowel doubling.
- Unknown IPA withholds the complete Ukrainian string. Burmese parser structures not yet supported by phonological rules (medials, conjuncts, kinzi) are withheld in both Python and browser paths.
- PR #133 is the active practical-system PR; PR #132 was superseded after its browser test exposed fail-open handling. The exact-head test run [43095497303](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43095497303) is queued. No independent adjudicated lexical IPA gold set exists; empirical accuracy remains unmeasured.


## 2026-11-11 — Ukrainian practical adapter task update

| Task | Status | Evidence / acceptance |
|---|---|---|
| Add Python whole-IPA → Ukrainian adapter and integrate after deterministic IPA | DONE_VERIFIED | `src/burmese_ukrainian/practical.py`, `rule_engine.py`; previous Python suite 180 + 66 subtests |
| Generate browser mapping from canonical practical CSV/rule data | DONE_VERIFIED | `src/web/ukrainian-adapter.js`; previous build, generated-data freshness and Node tests passed |
| Map /h, ɦ/ → г, /ɡ/ → ґ (project choice), /x/ → х, /w/ → в, syllable-initial /j/ yotation, affricates → ц/дз/ч/дж | DONE_VERIFIED | Canonical practical table and tests; /ɡ/ → ґ is not claimed as universal orthographic norm |
| Preserve tone/length in IPA trace; join syllable-level Ukrainian output into one word | DONE_VERIFIED | Python engine output and regression tests |
| Browser fail-closed behavior for kinzi/medials/conjuncts | PARTIAL | Implemented; final Playwright run 43095883419 queued with no jobs |
| Final browser/Playwright acceptance | BLOCKED | Acceptance: current PR head completes all Chromium tests successfully |
| Independent empirical IPA/Ukrainian accuracy evaluation | BLOCKED | No independent text gold set yet; requires source provenance, dialect scope and adjudication |
| Audio validation | DEFERRED | Outside user-requested text-only scope |


### Exact-head verification refresh — 2026-11-11

- PR #133 is the authoritative continuation branch; its live head is recorded in GitHub PR metadata. The practical adapter code remains at `e9bd12819ed692d7be2607356008217de9430dca`; subsequent commits are documentation-only.
- Exact-head workflow [43095883419](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43095883419) is queued with no jobs started. Final browser/Playwright verification is therefore still PARTIAL/BLOCKED pending the run.
- No audio is required for this task. The remaining accuracy blocker is an independently sourced, text-only Yangon IPA/Ukrainian adjudication set; without it, accuracy remains unmeasured.


### Provisional onset fallback continuation — 2026-11-11

| Task | Status | Evidence / blocker |
|---|---|---|
| Python onset-only fallback for unresolved syllables | PARTIAL | RuleBasedBurmeseEngine now exposes separate provisional IPA/Ukrainian preview and trace; canonical fields remain withheld |
| Browser onset-only fallback | PARTIAL | Browser parser reuses onset IPA and target adapter; unresolved remainder receives ? |
| Python/browser parity | TODO | Add shared fixture with exact matching status, IPA hint, Ukrainian rendering and trace |
| Exact-head CI / Chromium | BLOCKED | No workflow run returned for head 36b6ebf5a1d5a03b0c4d7a95aae2d842046e4152 |
| Complete Yangon positional fallback registry | TODO | Evidence-gated; onset-only partial coverage is not a full grapheme fallback |


### Verification result — provisional onset preview, 2026-11-11

| Task | Status | Evidence / blocker |
|---|---|---|
| Python onset-only preview for isolated bare consonants | DONE_VERIFIED (engineering behavior) | Head aac1d6834b4c29e04f01477af1583a2be9eba485; 182 tests + 66 subtests passed |
| Browser preview in analysis details; canonical output unchanged | DONE_VERIFIED (engineering behavior) | Playwright 54/54; same workflow 43101914347 |
| Build, generated data and Node tests | DONE_VERIFIED | Workflow 43101914347 all pass |
| Optional Epitran raw-output comparator | DONE_VERIFIED (comparator only) | Workflow 43101914423 pass; not accuracy evidence |
| Functional Python/browser shared fixture | TODO | Still needs matching structured fallback output and trace across runtimes |
| Full positional Myanmar fallback inventory | BLOCKED by evidence | Requires exact Yangon-profile positional IPA sources for vowels, codas/asat, medials, kinzi, conjuncts and tone |


### Complete Myanmar grapheme accounting — 2026-11-12

| Layer / acceptance gate | Implemented coverage | Tested coverage | Independently validated coverage | Status | Next acceptance criterion |
|---|---|---|---|---|---|
| Unicode L/M input accounting across Myanmar blocks | Parser preserves each assigned letter/combining mark in U+1000–109F, U+A9E0–A9FF, U+AA60–AA7F, U+116D0–116FF; exact U+ code points retained in records | Exhaustive Python sweep added in PR #134; exact-head test workflow [43184645239](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43184645239) PASS | Not phonological evidence; no pronunciation gold inferred | DONE_VERIFIED (structural accounting only) | Keep unsupported Myanmar-language extensions explicit; build source-backed Yangon positional IPA inventory before expanding phonology |
| Complete Yangon-profile pronunciation/IPA for all letters and contexts | Only narrow onset/rime rules plus isolated bare-consonant provisional preview; context-dependent medials, vowels, codas, kinzi, conjuncts and tone remain unresolved | Existing parser/withholding tests plus the new exhaustive source-accounting sweep | Independent adjudicated Yangon-profile gold remains 0 | PARTIAL / BLOCKED | Require source-located onset × medial × vowel × coda × prosody evidence, shared Python/browser fixtures, independent annotation/adjudication and held-out accuracy evaluation |


### Burmese onset registry parity — 2026-11-12

| Layer / acceptance gate | Implemented coverage | Tested coverage | Independently validated coverage | Status | Next acceptance criterion |
|---|---|---|---|---|---|
| Provisional onset hint registry completeness | Python map now includes U+1009 `ဉ → ɲ`, matching the existing analysis-dependent CSV/browser registry | Exact-head workflow [43185426033](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43185426033) PASS: Python, generated-data freshness, Node and built Chromium | Not independent gold; this is registry parity only | DONE_VERIFIED for U+1009 hint | Add a shared structured Python/browser fixture for every provisional onset candidate |
| `ရ` candidate IPA parity | CSV/browser registry uses `r`; Python candidate map uses `ɹ`; both are analysis-dependent | Difference identified by source-table/code comparison; no adjudicating test should encode either as truth yet | None | PARTIAL / EVIDENCE-LIMITED | Resolve with source-located Yangon-profile phonetic evidence and record an explicit broad/narrow IPA policy before aligning |


## MLCTS → Ukrainian target matrix — 2026-11-12

- Branch `feat/burmese-romanization-ukrainian-matrix-completion-2026-11-12` adds explicit Ukrainian target candidates to all 35 onset rows and all 94 vendor-derived rime rows.
- `MYA-ROM-UA-TARGET-001` is DONE_VERIFIED on exact-head test run [43221074232](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43221074232); the target mapping is a project orthographic convention. `MYA-ROM-UA-001` remains TODO because no runtime syllable adapter consumes the MLCTS string yet.
- `MYA-ROM-MATRIX-001` remains PARTIAL: the 94-rime source inventory is Mya2Rom-derived and not individually verified against the original MLC publication; medials, kinzi, asat, independent vowels, numerals, punctuation and legal syllable coverage are still incomplete.


## Post-merge mainline verification — MLCTS Ukrainian target matrix — 2026-11-12

- PR #138 merged as `1d7045d9695d571017633a2e294b718a13ee5bce`.
- Mainline test [43221871111](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43221871111) and Pages deployment [43221870932](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43221870932) passed.
- `MYA-ROM-UA-TARGET-001` remains DONE_VERIFIED; the runtime adapter and full source orthographic inventory remain open as separately classified above.


## MLCTS romanization → Ukrainian runtime adapter — 2026-11-12

| ID | Status | Evidence / blocker |
|---|---|---|
| MYA-ROM-UA-TARGET-001 | DONE_VERIFIED | Existing 35 onset and 94 vendor-derived rime target rows are populated. |
| MYA-ROM-UA-001 | PARTIAL | PR #141 adds the runtime adapter and UI. Exact-head tests [43226578745](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43226578745) and push [43226566617](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43226566617) pass: 187 Python tests + 66 subtests, 18 Node tests, 55 Playwright tests, build and generated-data freshness. Remaining: all legal syllable structures and primary MLC verification. |
| MYA-ROM-MATRIX-001 | PARTIAL | Runtime supports all current rime rows and onset combinations with supported y/r/w medials; unsupported structures remain visibly bracketed. Full orthographic inventory, kinzi/asat/devoicing and MLC primary-source adjudication remain open. |


Latest final exact-head verification after adding explicit withholding for Myanmar code points outside the romanization support inventory: [tests 43227199213](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43227199213) SUCCESS on `4a2cb24ae9af2bc5e4d9341de65d0a55e07b6e09`: 187 Python tests + 66 subtests, 19 Node tests, 55 Playwright browser tests, production build and generated-data freshness. Unsupported Myanmar code points are now explicitly bracketed in the Ukrainian romanization output.


## MLCTS Ukrainian runtime adapter — mainline post-merge verification — 2026-11-12

- PR [#141](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/141) merged as `3fa33864b774c716da5bf6c9778a963148fb9974`.
- Mainline tests [43227806284](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43227806284) and Pages deployment [43227806266](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43227806266) both SUCCESS.
- Mainline test evidence: 187 Python tests + 66 subtests, 19 Node tests, 55 Playwright browser tests, production build and generated-data freshness all passed.
- Acceptance remains PARTIAL: current Mya2Rom-derived rime inventory is EVIDENCE_LIMITED, and unrepresented legal syllable structures remain visibly unsupported rather than guessed.


## MLCTS → Ukrainian mainline status refresh — 2026-11-12

The earlier TODO row is superseded by the integrated runtime in PR #141. Current `main` is `718dc4b2c1424651b32bc63b0202f5d08a067bc7`; exact-main tests [43228612973](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43228612973) and Pages [43228612998](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43228612998) passed. Status is PARTIAL, not DONE: 35 onset and 94 vendor-rime targets are mapped, but the rime inventory is vendor-derived/EVIDENCE_LIMITED and legal structures outside the supported adapter inventory remain withheld. This is orthographic rendering, not IPA validation.


## Browser structural-analysis numbering correction — 2026-11-13

| Work item | Status | Evidence / acceptance |
|---|---|---|
| Whitespace excluded from Myanmar syllable numbering while preserved in source reconstruction | DONE_VERIFIED | PR [#146](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/146), merged as `85dab8bdd08576c1cd112552f68092182bd9a8fa`. Regression for `ကာ မြန်မာ` asserts contiguous Myanmar syllable numbers `01`, `02`, `03`, retained separator, and unchanged fail-closed phonetic output. Exact merged-head test run [43318947338](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43318947338): 187 Python tests + 66 subtests, 19 Node tests, 56 Chromium Playwright tests, build and generated-data freshness all SUCCESS. |
| Yangon IPA coverage for medial-ra/rime in `မြန်` | PARTIAL | Still intentionally withheld: the current positional IPA rule inventory does not establish this combination. No grapheme-only guess was introduced. Acceptance: source-backed positional analysis and independent expert adjudication for the selected Yangon profile, followed by shared Python/browser fixtures. |

The initial regression run [43318664262](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43318664262) exposed an incorrectly escaped whitespace-detection regex; this was corrected before merge. The successful run above is on the final merged code head. Mainline Pages deployment [43319186954](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43319186954) was triggered after merge; deployment status is tracked separately and must not be inferred from the test result.


## Burmese medial and G2P evidence review — 2026-11-13

| Work item | Status | Evidence / acceptance |
|---|---|---|
| Four medial signs as orthographic slots | DONE_VERIFIED as source registry | Unicode 18 Table 16-4 plus WG2 N2827; establishes orthographic identities/order, not IPA values. |
| YA/RA medial phonology | PARTIAL / ANALYSIS_DEPENDENT | Ishida 2026 describes /j/ default and velar-conditioned palatalization; Watkins 2001 describes secondary articulation in phonological /j,w/ clusters. Full onset × rime × prosody inventory and independent Yangon adjudication remain absent. |
| WA medial | PARTIAL / CONTEXT_DEPENDENT | /w/ glide and /ʊ/ vowel/rime alternatives documented; no complete environment table. |
| HA medial | PARTIAL / CONTEXT_DEPENDENT | Aspiration/devoicing and selected /ʃ/ fusion documented; no full onset-class inventory. |
| Multiple medials | PARTIAL | MLC 1986 orthographic inventory of eleven forms reported in WG2 N2827; no complete modern native/loan distribution or IPA gold. |
| Lexical IPA for မြန် | CANDIDATE / NOT GOLD | English Wiktionary lists /mjàɴ/ and a compound contains /mjàɴmà/. This supersedes “no lexical lead found” but does not approve a general rule or runtime output. |
| Shared runtime implementation | TODO | Browser has dormant candidate derivation behind an all-medials guard; Python adapter independently withholds medials/codas. Require shared fixtures and parity before enabling. |
| myG2P dictionary reuse | BLOCKED pending permission for commercial integration | CC BY-NC-SA 4.0; Myanmar README says commercial use is not granted without maintainer permission. |
| Oo et al. Thrax grammar reuse | BLOCKED pending license verification | Paper describes public GitHub grammar but does not specify its license. |
| Independent Yangon IPA gold | BLOCKED / NOT ESTABLISHED | No controlled speaker recordings, independent annotation or adjudication for target medial combinations. |

Detailed review: docs/research/BURMESE-MEDIALS-AND-G2P-EVIDENCE-REVIEW-2026-11-13.md. Evidence registry: data/burmese/medial_evidence_matrix.csv. Automated traceability: tests/test_medial_evidence_matrix.py.

The previous handoff statement that no word-level pronunciation lead was found for မြန် is superseded: a lexical IPA candidate is now documented. Runtime abstention remains unchanged until the candidate is independently validated and the phonemic-vs-phonetic output contract is fixed.


## Burmese medial/G2P research reconciliation — 2026-11-13 (expanded)

| Work item | Status | Evidence / acceptance |
|---|---|---|
| Eleven MLC medial forms | DONE_VERIFIED as orthographic inventory | Hlaing (2014) Table 5 lists four basic signs plus seven codepoint combinations; WG2 N2827 independently states eleven total. The thesis has a duplicated description typo on the final RA+WA+HA row; codepoints are authoritative. |
| YA/RA and glide onset | PARTIAL / ANALYSIS_DEPENDENT | Green (2002) gives /mj/ onset examples; Ishida 2026 and pinned Google Thrax describe /j/ behavior with onset-specific exceptions. No complete expert-adjudicated grapheme × onset matrix. |
| Nasal coda in မြန် | PARTIAL / CROSS-SOURCE CANDIDATE | Wiktionary /mjàɴ/, Google WFST raw output m j àɴ, and Green's /mj/ plus placeless /N/ model converge. Still no independent text-based expert adjudication; Green treats /N/ as vowel nasalization, not necessarily [ɴ]. |
| Google Thrax source/license | DONE_VERIFIED | Pinned grammar and repository LICENSE both Apache-2.0 at a90601024f07ab7e96c911243324e0adeb16da96. Run 43084508359 build/raw-output smoke succeeded, zero gold; optional comparator only. |
| Hlaing orthographic FST | DONE_VERIFIED as published structural baseline | 11,732 words / 32,283 syllables; initial 99.93% word-level syllabification; not G2P or IPA accuracy. |
| Burmese tone inventory | PARTIAL / COMPETING ANALYSES | Green and Oo et al. (2020) describe four categories; Duan & Zhu (2025) full text (44 pp., CC BY 4.0) proposes eight categories across modal/lower registers. Its sample is five speakers from Yangon, Taunggyi and Mandalay region (not Yangon-only); 89 words / 694 valid tokens; individual T1/T3 variation documented. |
| Open PR #129 | LEFT OPEN / NOT MERGED | Draft hybrid-engine research PR is 53 commits ahead and 17 behind current main, divergent and non-mergeable. Its source-backed Google FST and raw-output evidence were reused in this research report; the broad hybrid implementation was not ported or merged. |

Detailed evidence: docs/research/BURMESE-MEDIALS-AND-G2P-EVIDENCE-REVIEW-2026-11-13.md. New rows: data/burmese/medial_evidence_matrix.csv. Traceability tests: tests/test_medial_evidence_matrix.py.


### Cross-runtime coda segmentation correction — 2026-11-13

- Python previously split an asat-marked final consonant as a new syllable onset. For မြန်, it produced two structural records (မြ + န်), while the browser correctly kept မြန် as one syllable.
- Python segmentation now treats a base consonant followed by U+103A as a coda within the preceding syllable, and the parser records the final consonant and ASAT codepoint explicitly.
- Regression coverage: မြန် is one orthographic syllable; မြန်မာ is two; ကတ် retains final တ+ASAT. Browser tests lock the same visible syllable boundaries.
- Phonetic status is unchanged: medial/coda syllables remain withheld from IPA until source-backed phonological rules and parity fixtures are accepted.


### External raw-engine diagnostics — 2026-11-13

- Epitran 1.35.3 returned məjaɴ for the structural-only probe မြန်, while Google Thrax returned m j àɴ. Both runs had zero gold and null accuracy; the disagreement is unresolved.
- CRFsuite v2 returned 84/100 source-concordant predictions on a 100-row sample of myG2P v2.0. Medial-bearing sample counts: YA 10/14, RA 17/20, WA 13/15, HA 7/8 (overlapping categories). The exact word မြန် was not in the sample; training overlap is possible and the input syllable boundaries were supplied.
- These outputs are diagnostic only, not gold, not accuracy, and not approved runtime rules. The myG2P source dataset remains CC BY-NC-SA 4.0.


## Final exact-head verification — 2026-11-13

- Research branch head before this documentation reconciliation: 5eff1f3d052e775026ffff0fa0b3edd00512224d.
- Required workflow [43325991671](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43325991671) SUCCESS: independent IPA gold schema validation, Python tests, npm build, generated web-data freshness, Node tests, Chromium/Playwright built-site tests.
- Optional raw-output workflow [43325991496](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43325991496) SUCCESS: Epitran and CRFsuite diagnostics; artifacts are recorded with SHA-256 in the source registry.
- Exact final CI is engineering/provenance verification only. Gold remains zero and accuracy null.


### Nasal-coda evidence and IPA schema boundary — 2026-11-13

- Added Green-based phonotactic rows for placeless /N/ and nasal-rhyme tone restrictions. These are analysis-dependent source records, not active runtime rules.
- Clarified that the proposed Ukrainian /ɴ/ → нг rule applies only when the selected IPA convention explicitly emits /ɴ/; it must not be used automatically for abstract /N/ or nasalized-vowel realizations.
- The IPA gold schema preserves literal IPA, kind, syllable boundaries, tone, vowel length and phonation, but has no typed nasalization property. Literal IPA remains sufficient for transcription; a structured field is deferred until expert convention approval.


### UCSY-SC1 corpus lead — 2026-11-13

UCSY-SC1 is historical corpus metadata only and excluded from current text-only scope; rights details do not create an active task or blocker.


## Final one-pass verification — 2026-11-13

- Base/default-branch starting commit: dc90463bdd734867308f03cb627eb8941efc19d6.
- Latest code/data-bearing research head: 826601139fd73a5152b6b37a5ed3574f3fca18a5.
- Dedicated branch: research/burmese-medials-g2p-evidence-2026-11-13.
- Draft PR: #147. It is intentionally not merged while independent linguistic adjudication remains absent.
- Required exact-head CI 43327571175 SUCCESS: 201 Python tests + 66 subtests; independent IPA gold schema validation; npm build; generated web-data freshness; 19 Node tests; 58 Chromium/Playwright tests.
- Optional raw comparator/CRF workflow 43327570809 SUCCESS. Outputs remain non-gold and accuracy remains null.
- Intermediate CI failures were fixed and rerun: 43324492175 exposed Python coda segmentation and matrix CSV issues; 43326933757 exposed a temporary practical_rules.csv path-mapping overwrite during documentation work. The table was restored from main, the conditional /ɴ/ note reapplied, and the final required CI passed.
- No runtime medial IPA rule was enabled. The structural coda fix is verified; phonological coverage remains PARTIAL.
- Independent expert-adjudicated IPA gold for the medial/coda cells: 0. Empirical accuracy: null.
- PR #129 remains open/draft and untouched as a code branch (53 commits ahead / 17 behind current main, non-mergeable); its source-backed research findings were reconciled into this branch, but its broad hybrid-engine code was not ported.
- Release assessment: PARTIAL PROTOTYPE, not linguistically release-ready. Research dossier is ready for specialist review and data-rights resolution.
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
| IPA → Ukrainian target adapter | Canonical candidate inventory plus executable whole-string IPA → Ukrainian adapter in Python and browser; longest-match affricates, h/ɦ → г, ɡ/g → ґ (project choice), x → х, explicit ц/дз/ч/дж, aspiration notation, contextual /j/ yotation, prosody trace, fail-closed unknown segments; post-IPA integration in deterministic engine and public service | Python sequence tests; browser adapter tests include spaced IPA, untied consonant sequences and fail-closed unsupported structures; generated-data freshness, Node tests and built-site Playwright rerun queued on PR #133 (run 43095497303) | No Ukrainian name-level or independent lexical IPA gold evaluation | PARTIAL pending exact-head CI | Pass the full exact-head CI including built-site Playwright; retain empirical gold evaluation as separate blocker |
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
| Build MLCTS → Ukrainian syllable crosswalk | PARTIAL | Onset + 94 vendor-rime target rows are populated and tested on the task branch; complete source-verified Myanmar structures and a runtime syllable adapter remain open. Do not reuse IPA mapper. |
| Ukrainian target matrix coverage | DONE_VERIFIED | Exact-head test run [43221074232](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43221074232) passed: 187 Python tests + 66 subtests, 54 Node tests, build, generated-data freshness and built-site Playwright. 35 onset + 94 vendor-rime target rows are populated; source inventory remains EVIDENCE_LIMITED. |
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
| MYA-PHONETIC-GOLD-001 | BLOCKED / TEXT-ONLY EXPERT REVIEW | Current source and phonology audits | Create independently reviewed IPA examples from written dictionaries, lexical entries and published phonological descriptions, with source locators and a versioned broad/narrow convention. |

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
| Independent lexical IPA gold | BLOCKED | data/benchmark/gold.tsv is header-only; independent gold=0 and accuracy=null. Requires source-located written IPA/phonological evidence, a defined target variety, two independent text-based reviewers and adjudication. No audio. |
| Consonant, kinzi and medial phonology | PARTIAL | Structural parsing exists; source-backed contextual phonological coverage and a differential corpus remain incomplete. |
| Vowel combinations and coda realization | PARTIAL | Full vowel derivation, checked-syllable and contextual coda realization are not implemented. |
| Tone/register/phonation | TODO | Specialist adjudication of competing analyses and scoped implementation are required; do not infer or collapse them. |
| IPA → Ukrainian | PARTIAL | Canonical external inventory boundary exists; target policies remain proposal-level and need expert review. |
| MLCTS → Ukrainian | PARTIAL | Separate orthographic adapter is integrated for supported onset/rime combinations and y/r/w medials; unsupported forms are visibly withheld. Full acceptance requires primary MLC source verification and coverage of kinzi/asat/devoicing/independent-vowel structures. |
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


## Focused source audit and evidence-gate refinements — 2026-11-03

| Evidence / task | Status | Verified source result | Consequence / acceptance |
|---|---|---|---|
| MYA-ORTHO-SYLLABIFICATION-001 | PARTIAL (external evidence reviewed; not implemented as ClippyFirst G2P) | Hlaing & Mikami (2014), [Automatic syllable segmentation of Myanmar texts using finite state transducer](https://doi.org/10.4038/ICTER.V6I2.7150): rule-based FST; 11,732 orthographic words; 99.93% word-syllabification; consonant-stacking subset 245/253 correct (96.83%); text also discusses a free-standing-vowel error; article count inconsistency 32,238 vs 32,283 syllables. | This is orthographic segmentation, not G2P, phoneme or IPA accuracy. Use only as structural-parser comparator; test kinzi/stacked consonants explicitly. |
| MYA-TONE-VOWEL-ANALYSIS-001 | PARTIAL | Mooney & Repetti-Ludlow (2021), [Sonority and syllable structure: The case of Burmese tone](https://doi.org/10.3765/plsa.v6i1.4900): acoustic experiments from one Yangon speaker; proposes syllable-structure/sonority-conditioned vowel alternations and a competing underlying-tone analysis. | Preserve as competing analysis; do not collapse vowel quality into tone or replace traditional surface categories without qualified review. |
| MYA-CORPUS-SLR80-001 | PARTIAL | Oo et al. (2020), [Burmese Speech Corpus, Finite-State Text Normalization and Pronunciation Grammars with an Application to Text-to-Speech](https://aclanthology.org/2020.lrec-1.777): 2,528 utterances, 20 female Yangon speakers, 22,443 tokens, 9,941 unique words; corpus CC BY-SA 4.0; separate Thrax/WFST G2P grammar. | Orthographic speech corpus, not IPA gold; no public train/dev/test split or speaker-balanced IPA benchmark established. Verify grammar license separately. |
| MYA-PHONETIC-PROFILE-001 | PARTIAL | Watkins (2001), [Burmese](https://doi.org/10.1017/S0025100301002122), JIPA profile from one 30-year-old Yangon male reading slowly; Gruber (2011), [Perceptual Cues to Lexical Tone in Burmese](https://doi.org/10.3765/EXABS.V0I0.557), reports joint pitch/duration/phonation cues. | Use as profile and feature evidence, not multi-speaker population gold. Keep tone, phonation and duration typed and separately testable. |
| MYA-GOLD-AGREEMENT-001 | TODO | Cucchiarini (1996), DOI [10.3109/02699209608985167](https://doi.org/10.3109/02699209608985167); Oller & Ramsdell (2006), DOI [10.1044/1092-4388(2006/100)]. | Pilot reports exact normalized agreement plus alignment-aware feature-weighted agreement, separate tone/duration/phonation/vowel/coda/boundary diagnostics, unresolved alternatives and adjudication rate. Raw percentage agreement supplementary only. |

No lexicon rows, IPA labels, or model predictions were imported. Gold remains 0; accuracy remains null. The detailed source audit is also recorded in the current top-level handoff and linguistic completion register.


## Engineering test-harness status — 2026-11-04

| Layer / acceptance gate | Implemented coverage | Tested coverage | Independently validated coverage | Status | Next acceptance criterion |
|---|---|---|---|---|---|
| IPA corpus test-fixture language identity | Fixture uses Myanmar-script sample, `test-burmese` profile and neutral variety label; shared script-range constants are explicit in the test module | Regression asserts all fixture characters are in the Myanmar Unicode block and profile metadata matches the repository language; exact-main tests [41847895975](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41847895975) SUCCESS | Not applicable; this is test-data integrity, not phonological validation | DONE_VERIFIED | Preserve language-specific fixtures when adding shared corpus tests; do not infer phonological coverage from this check |

This engineering correction does not change the language-layer statuses above. Independent Burmese IPA gold remains 0; accuracy remains null.


## IPA gold release-gate corpus identity — 2026-11-04

| Task | Status | Evidence | Remaining acceptance |
|---|---|---|---|
| BURMESE-IPA-GOLD-PROFILE-GATE-001 | DONE_VERIFIED (engineering guard) | PR #117 merged as `085ce5a2da4a07dfbf606a9892c78a4d3bbb9d91`; exact-head tests [41870132273](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41870132273), post-merge tests [41870579420](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41870579420), and Pages [41870579398](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41870579398) SUCCESS. Shared validator rejects mixed adjudicated target profiles and mixed IPA kinds; positive regression confirms speaker/audio IDs may vary. | Human approval of Standard Yangon profile/convention, blind double annotation, independent adjudicator, rights-cleared source set, and specialist-reviewed onset × medial × vowel × coda × prosodic coverage remain outstanding. This guard does not create gold or prove accuracy. |

## Deterministic rule engine — 2026-11-11

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-DETERMINISTIC-RULE-ENGINE-001 | DONE_VERIFIED (engineering); linguistic coverage PARTIAL | PR #128 merged as `cd3a1503e79d32b09a6d2d5206340a37cfd3283b`; main tests [43018103155](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43018103155) and Pages smoke [43018103391](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43018103391) SUCCESS; live site published. | Deterministic engine published. Expert-adjudicated Yangon IPA gold still required for phonetic correctness/accuracy claims. |

## Final deterministic-engine verification — 2026-11-11

| ID | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| MYA-DETERMINISTIC-RULE-ENGINE-001 | DONE_VERIFIED (engineering); linguistic coverage PARTIAL | Final main head `9bece0a50a367f3f58336d2aba7016ac4af86156`; tests [43019216137](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43019216137) and Pages + smoke [43019216297](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43019216297) SUCCESS. | Deterministic runtime published; independent expert-adjudicated Yangon IPA gold remains outstanding. |


## Ukrainian practical transcription — 2026-11-11 continuation

- Python and browser output are both post-IPA adapters; the browser imports the generated correspondence and rule tables rather than maintaining a separate linguistic mapping table.
- The browser adapter uses longest-match for explicit affricates, preserves word spaces, treats syllable dots as boundaries, and applies Ukrainian yotation to /j/ at the start of each IPA syllable.
- The target policy distinguishes /h, ɦ/ → г, /ɡ/ (ASCII /g/) → ґ as a project-specific choice, and /x/ → х. It maps explicit /t͡s, d͡z, t͡ʃ, d͡ʒ/ to ц, дз, ч, дж; /tɕ, dʑ/ are practical approximations. Plain adjacent consonants are not collapsed into affricates.
- Aspiration is marked with a project apostrophe; /ʔ/ is omitted from ordinary practical spelling but remains in IPA/trace. Tone and length are retained analytically, not converted to Ukrainian stress or vowel doubling.
- Unknown IPA withholds the complete Ukrainian string. Burmese parser structures not yet supported by phonological rules (medials, conjuncts, kinzi) are withheld in both Python and browser paths.
- PR #133 is the active practical-system PR; PR #132 was superseded after its browser test exposed fail-open handling. The exact-head test run [43095497303](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43095497303) is queued. No independent adjudicated lexical IPA gold set exists; empirical accuracy remains unmeasured.


## 2026-11-11 — Ukrainian practical adapter task update

| Task | Status | Evidence / acceptance |
|---|---|---|
| Add Python whole-IPA → Ukrainian adapter and integrate after deterministic IPA | DONE_VERIFIED | `src/burmese_ukrainian/practical.py`, `rule_engine.py`; previous Python suite 180 + 66 subtests |
| Generate browser mapping from canonical practical CSV/rule data | DONE_VERIFIED | `src/web/ukrainian-adapter.js`; previous build, generated-data freshness and Node tests passed |
| Map /h, ɦ/ → г, /ɡ/ → ґ (project choice), /x/ → х, /w/ → в, syllable-initial /j/ yotation, affricates → ц/дз/ч/дж | DONE_VERIFIED | Canonical practical table and tests; /ɡ/ → ґ is not claimed as universal orthographic norm |
| Preserve tone/length in IPA trace; join syllable-level Ukrainian output into one word | DONE_VERIFIED | Python engine output and regression tests |
| Browser fail-closed behavior for kinzi/medials/conjuncts | PARTIAL | Implemented; final Playwright run 43095883419 queued with no jobs |
| Final browser/Playwright acceptance | BLOCKED | Acceptance: current PR head completes all Chromium tests successfully |
| Independent empirical IPA/Ukrainian accuracy evaluation | BLOCKED | No independent text gold set yet; requires source provenance, dialect scope and adjudication |
| Audio validation | DEFERRED | Outside user-requested text-only scope |


### Exact-head verification refresh — 2026-11-11

- PR #133 is the authoritative continuation branch; its live head is recorded in GitHub PR metadata. The practical adapter code remains at `e9bd12819ed692d7be2607356008217de9430dca`; subsequent commits are documentation-only.
- Exact-head workflow [43095883419](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43095883419) is queued with no jobs started. Final browser/Playwright verification is therefore still PARTIAL/BLOCKED pending the run.
- No audio is required for this task. The remaining accuracy blocker is an independently sourced, text-only Yangon IPA/Ukrainian adjudication set; without it, accuracy remains unmeasured.


### Provisional onset fallback continuation — 2026-11-11

| Task | Status | Evidence / blocker |
|---|---|---|
| Python onset-only fallback for unresolved syllables | PARTIAL | RuleBasedBurmeseEngine now exposes separate provisional IPA/Ukrainian preview and trace; canonical fields remain withheld |
| Browser onset-only fallback | PARTIAL | Browser parser reuses onset IPA and target adapter; unresolved remainder receives ? |
| Python/browser parity | TODO | Add shared fixture with exact matching status, IPA hint, Ukrainian rendering and trace |
| Exact-head CI / Chromium | BLOCKED | No workflow run returned for head 36b6ebf5a1d5a03b0c4d7a95aae2d842046e4152 |
| Complete Yangon positional fallback registry | TODO | Evidence-gated; onset-only partial coverage is not a full grapheme fallback |


### Verification result — provisional onset preview, 2026-11-11

| Task | Status | Evidence / blocker |
|---|---|---|
| Python onset-only preview for isolated bare consonants | DONE_VERIFIED (engineering behavior) | Head aac1d6834b4c29e04f01477af1583a2be9eba485; 182 tests + 66 subtests passed |
| Browser preview in analysis details; canonical output unchanged | DONE_VERIFIED (engineering behavior) | Playwright 54/54; same workflow 43101914347 |
| Build, generated data and Node tests | DONE_VERIFIED | Workflow 43101914347 all pass |
| Optional Epitran raw-output comparator | DONE_VERIFIED (comparator only) | Workflow 43101914423 pass; not accuracy evidence |
| Functional Python/browser shared fixture | TODO | Still needs matching structured fallback output and trace across runtimes |
| Full positional Myanmar fallback inventory | BLOCKED by evidence | Requires exact Yangon-profile positional IPA sources for vowels, codas/asat, medials, kinzi, conjuncts and tone |


### Complete Myanmar grapheme accounting — 2026-11-12

| Layer / acceptance gate | Implemented coverage | Tested coverage | Independently validated coverage | Status | Next acceptance criterion |
|---|---|---|---|---|---|
| Unicode L/M input accounting across Myanmar blocks | Parser preserves each assigned letter/combining mark in U+1000–109F, U+A9E0–A9FF, U+AA60–AA7F, U+116D0–116FF; exact U+ code points retained in records | Exhaustive Python sweep added in PR #134; exact-head test workflow [43184645239](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43184645239) PASS | Not phonological evidence; no pronunciation gold inferred | DONE_VERIFIED (structural accounting only) | Keep unsupported Myanmar-language extensions explicit; build source-backed Yangon positional IPA inventory before expanding phonology |
| Complete Yangon-profile pronunciation/IPA for all letters and contexts | Only narrow onset/rime rules plus isolated bare-consonant provisional preview; context-dependent medials, vowels, codas, kinzi, conjuncts and tone remain unresolved | Existing parser/withholding tests plus the new exhaustive source-accounting sweep | Independent adjudicated Yangon-profile gold remains 0 | PARTIAL / BLOCKED | Require source-located onset × medial × vowel × coda × prosody evidence, shared Python/browser fixtures, independent annotation/adjudication and held-out accuracy evaluation |


### Burmese onset registry parity — 2026-11-12

| Layer / acceptance gate | Implemented coverage | Tested coverage | Independently validated coverage | Status | Next acceptance criterion |
|---|---|---|---|---|---|
| Provisional onset hint registry completeness | Python map now includes U+1009 `ဉ → ɲ`, matching the existing analysis-dependent CSV/browser registry | Exact-head workflow [43185426033](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43185426033) PASS: Python, generated-data freshness, Node and built Chromium | Not independent gold; this is registry parity only | DONE_VERIFIED for U+1009 hint | Add a shared structured Python/browser fixture for every provisional onset candidate |
| `ရ` candidate IPA parity | CSV/browser registry uses `r`; Python candidate map uses `ɹ`; both are analysis-dependent | Difference identified by source-table/code comparison; no adjudicating test should encode either as truth yet | None | PARTIAL / EVIDENCE-LIMITED | Resolve with source-located Yangon-profile phonetic evidence and record an explicit broad/narrow IPA policy before aligning |


## MLCTS → Ukrainian target matrix — 2026-11-12

- Branch `feat/burmese-romanization-ukrainian-matrix-completion-2026-11-12` adds explicit Ukrainian target candidates to all 35 onset rows and all 94 vendor-derived rime rows.
- `MYA-ROM-UA-TARGET-001` is DONE_VERIFIED on exact-head test run [43221074232](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43221074232); the target mapping is a project orthographic convention. `MYA-ROM-UA-001` remains TODO because no runtime syllable adapter consumes the MLCTS string yet.
- `MYA-ROM-MATRIX-001` remains PARTIAL: the 94-rime source inventory is Mya2Rom-derived and not individually verified against the original MLC publication; medials, kinzi, asat, independent vowels, numerals, punctuation and legal syllable coverage are still incomplete.


## Post-merge mainline verification — MLCTS Ukrainian target matrix — 2026-11-12

- PR #138 merged as `1d7045d9695d571017633a2e294b718a13ee5bce`.
- Mainline test [43221871111](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43221871111) and Pages deployment [43221870932](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43221870932) passed.
- `MYA-ROM-UA-TARGET-001` remains DONE_VERIFIED; the runtime adapter and full source orthographic inventory remain open as separately classified above.


## MLCTS romanization → Ukrainian runtime adapter — 2026-11-12

| ID | Status | Evidence / blocker |
|---|---|---|
| MYA-ROM-UA-TARGET-001 | DONE_VERIFIED | Existing 35 onset and 94 vendor-derived rime target rows are populated. |
| MYA-ROM-UA-001 | PARTIAL | PR #141 adds the runtime adapter and UI. Exact-head tests [43226578745](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43226578745) and push [43226566617](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43226566617) pass: 187 Python tests + 66 subtests, 18 Node tests, 55 Playwright tests, build and generated-data freshness. Remaining: all legal syllable structures and primary MLC verification. |
| MYA-ROM-MATRIX-001 | PARTIAL | Runtime supports all current rime rows and onset combinations with supported y/r/w medials; unsupported structures remain visibly bracketed. Full orthographic inventory, kinzi/asat/devoicing and MLC primary-source adjudication remain open. |


Latest final exact-head verification after adding explicit withholding for Myanmar code points outside the romanization support inventory: [tests 43227199213](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43227199213) SUCCESS on `4a2cb24ae9af2bc5e4d9341de65d0a55e07b6e09`: 187 Python tests + 66 subtests, 19 Node tests, 55 Playwright browser tests, production build and generated-data freshness. Unsupported Myanmar code points are now explicitly bracketed in the Ukrainian romanization output.


## MLCTS Ukrainian runtime adapter — mainline post-merge verification — 2026-11-12

- PR [#141](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/141) merged as `3fa33864b774c716da5bf6c9778a963148fb9974`.
- Mainline tests [43227806284](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43227806284) and Pages deployment [43227806266](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43227806266) both SUCCESS.
- Mainline test evidence: 187 Python tests + 66 subtests, 19 Node tests, 55 Playwright browser tests, production build and generated-data freshness all passed.
- Acceptance remains PARTIAL: current Mya2Rom-derived rime inventory is EVIDENCE_LIMITED, and unrepresented legal syllable structures remain visibly unsupported rather than guessed.


## MLCTS → Ukrainian mainline status refresh — 2026-11-12

The earlier TODO row is superseded by the integrated runtime in PR #141. Current `main` is `718dc4b2c1424651b32bc63b0202f5d08a067bc7`; exact-main tests [43228612973](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43228612973) and Pages [43228612998](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43228612998) passed. Status is PARTIAL, not DONE: 35 onset and 94 vendor-rime targets are mapped, but the rime inventory is vendor-derived/EVIDENCE_LIMITED and legal structures outside the supported adapter inventory remain withheld. This is orthographic rendering, not IPA validation.


## Browser structural-analysis numbering correction — 2026-11-13

| Work item | Status | Evidence / acceptance |
|---|---|---|
| Whitespace excluded from Myanmar syllable numbering while preserved in source reconstruction | DONE_VERIFIED | PR [#146](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/pull/146), merged as `85dab8bdd08576c1cd112552f68092182bd9a8fa`. Regression for `ကာ မြန်မာ` asserts contiguous Myanmar syllable numbers `01`, `02`, `03`, retained separator, and unchanged fail-closed phonetic output. Exact merged-head test run [43318947338](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43318947338): 187 Python tests + 66 subtests, 19 Node tests, 56 Chromium Playwright tests, build and generated-data freshness all SUCCESS. |
| Yangon IPA coverage for medial-ra/rime in `မြန်` | PARTIAL | Still intentionally withheld: the current positional IPA rule inventory does not establish this combination. No grapheme-only guess was introduced. Acceptance: source-backed positional analysis and independent expert adjudication for the selected Yangon profile, followed by shared Python/browser fixtures. |

The initial regression run [43318664262](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43318664262) exposed an incorrectly escaped whitespace-detection regex; this was corrected before merge. The successful run above is on the final merged code head. Mainline Pages deployment [43319186954](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43319186954) was triggered after merge; deployment status is tracked separately and must not be inferred from the test result.


## Burmese medial and G2P evidence review — 2026-11-13

| Work item | Status | Evidence / acceptance |
|---|---|---|
| Four medial signs as orthographic slots | DONE_VERIFIED as source registry | Unicode 18 Table 16-4 plus WG2 N2827; establishes orthographic identities/order, not IPA values. |
| YA/RA medial phonology | PARTIAL / ANALYSIS_DEPENDENT | Ishida 2026 describes /j/ default and velar-conditioned palatalization; Watkins 2001 describes secondary articulation in phonological /j,w/ clusters. Full onset × rime × prosody inventory and independent Yangon adjudication remain absent. |
| WA medial | PARTIAL / CONTEXT_DEPENDENT | /w/ glide and /ʊ/ vowel/rime alternatives documented; no complete environment table. |
| HA medial | PARTIAL / CONTEXT_DEPENDENT | Aspiration/devoicing and selected /ʃ/ fusion documented; no full onset-class inventory. |
| Multiple medials | PARTIAL | MLC 1986 orthographic inventory of eleven forms reported in WG2 N2827; no complete modern native/loan distribution or IPA gold. |
| Lexical IPA for မြန် | CANDIDATE / NOT GOLD | English Wiktionary lists /mjàɴ/ and a compound contains /mjàɴmà/. This supersedes “no lexical lead found” but does not approve a general rule or runtime output. |
| Shared runtime implementation | TODO | Browser has dormant candidate derivation behind an all-medials guard; Python adapter independently withholds medials/codas. Require shared fixtures and parity before enabling. |
| myG2P dictionary reuse | BLOCKED pending permission for commercial integration | CC BY-NC-SA 4.0; Myanmar README says commercial use is not granted without maintainer permission. |
| Oo et al. Thrax grammar reuse | BLOCKED pending license verification | Paper describes public GitHub grammar but does not specify its license. |
| Independent Yangon IPA gold | BLOCKED / NOT ESTABLISHED | No controlled speaker recordings, independent annotation or adjudication for target medial combinations. |

Detailed review: docs/research/BURMESE-MEDIALS-AND-G2P-EVIDENCE-REVIEW-2026-11-13.md. Evidence registry: data/burmese/medial_evidence_matrix.csv. Automated traceability: tests/test_medial_evidence_matrix.py.

The previous handoff statement that no word-level pronunciation lead was found for မြန် is superseded: a lexical IPA candidate is now documented. Runtime abstention remains unchanged until the candidate is independently validated and the phonemic-vs-phonetic output contract is fixed.


## Burmese medial/G2P research reconciliation — 2026-11-13 (expanded)

| Work item | Status | Evidence / acceptance |
|---|---|---|
| Eleven MLC medial forms | DONE_VERIFIED as orthographic inventory | Hlaing (2014) Table 5 lists four basic signs plus seven codepoint combinations; WG2 N2827 independently states eleven total. The thesis has a duplicated description typo on the final RA+WA+HA row; codepoints are authoritative. |
| YA/RA and glide onset | PARTIAL / ANALYSIS_DEPENDENT | Green (2002) gives /mj/ onset examples; Ishida 2026 and pinned Google Thrax describe /j/ behavior with onset-specific exceptions. No complete expert-adjudicated grapheme × onset matrix. |
| Nasal coda in မြန် | PARTIAL / CROSS-SOURCE CANDIDATE | Wiktionary /mjàɴ/, Google WFST raw output m j àɴ, and Green's /mj/ plus placeless /N/ model converge. Still no independent text-based expert adjudication; Green treats /N/ as vowel nasalization, not necessarily [ɴ]. |
| Google Thrax source/license | DONE_VERIFIED | Pinned grammar and repository LICENSE both Apache-2.0 at a90601024f07ab7e96c911243324e0adeb16da96. Run 43084508359 build/raw-output smoke succeeded, zero gold; optional comparator only. |
| Hlaing orthographic FST | DONE_VERIFIED as published structural baseline | 11,732 words / 32,283 syllables; initial 99.93% word-level syllabification; not G2P or IPA accuracy. |
| Burmese tone inventory | PARTIAL / COMPETING ANALYSES | Green and LREC 2020 describe four categories; Duan & Zhu (2025) propose eight tones across modal/lower registers; full empirical tables not independently reviewed here. |
| Open PR #129 | LEFT OPEN / NOT MERGED | Draft hybrid-engine research PR is 53 commits ahead and 17 behind current main, divergent and non-mergeable. Its source-backed Google FST and raw-output evidence were reused in this research report; the broad hybrid implementation was not ported or merged. |

Detailed evidence: docs/research/BURMESE-MEDIALS-AND-G2P-EVIDENCE-REVIEW-2026-11-13.md. New rows: data/burmese/medial_evidence_matrix.csv. Traceability tests: tests/test_medial_evidence_matrix.py.


### Cross-runtime coda segmentation correction — 2026-11-13

- Python previously split an asat-marked final consonant as a new syllable onset. For မြန်, it produced two structural records (မြ + န်), while the browser correctly kept မြန် as one syllable.
- Python segmentation now treats a base consonant followed by U+103A as a coda within the preceding syllable, and the parser records the final consonant and ASAT codepoint explicitly.
- Regression coverage: မြန် is one orthographic syllable; မြန်မာ is two; ကတ် retains final တ+ASAT. Browser tests lock the same visible syllable boundaries.
- Phonetic status is unchanged: medial/coda syllables remain withheld from IPA until source-backed phonological rules and parity fixtures are accepted.


### External raw-engine diagnostics — 2026-11-13

- Epitran 1.35.3 returned məjaɴ for the structural-only probe မြန်, while Google Thrax returned m j àɴ. Both runs had zero gold and null accuracy; the disagreement is unresolved.
- CRFsuite v2 returned 84/100 source-concordant predictions on a 100-row sample of myG2P v2.0. Medial-bearing sample counts: YA 10/14, RA 17/20, WA 13/15, HA 7/8 (overlapping categories). The exact word မြန် was not in the sample; training overlap is possible and the input syllable boundaries were supplied.
- These outputs are diagnostic only, not gold, not accuracy, and not approved runtime rules. The myG2P source dataset remains CC BY-NC-SA 4.0.


## Final exact-head verification — 2026-11-13

- Research branch head before this documentation reconciliation: 5eff1f3d052e775026ffff0fa0b3edd00512224d.
- Required workflow [43325991671](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43325991671) SUCCESS: independent IPA gold schema validation, Python tests, npm build, generated web-data freshness, Node tests, Chromium/Playwright built-site tests.
- Optional raw-output workflow [43325991496](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43325991496) SUCCESS: Epitran and CRFsuite diagnostics; artifacts are recorded with SHA-256 in the source registry.
- Exact final CI is engineering/provenance verification only. Gold remains zero and accuracy null.


### Nasal-coda evidence and IPA schema boundary — 2026-11-13

- Added Green-based phonotactic rows for placeless /N/ and nasal-rhyme tone restrictions. These are analysis-dependent source records, not active runtime rules.
- Clarified that the proposed Ukrainian /ɴ/ → нг rule applies only when the selected IPA convention explicitly emits /ɴ/; it must not be used automatically for abstract /N/ or nasalized-vowel realizations.
- The IPA gold schema preserves literal IPA, kind, syllable boundaries, tone, vowel length and phonation, but has no typed nasalization property. Literal IPA remains sufficient for transcription; a structured field is deferred until expert convention approval.


### UCSY-SC1 corpus lead — 2026-11-13

UCSY-SC1 is historical corpus metadata only and excluded from current text-only scope; rights details do not create an active task or blocker.


## Final one-pass verification — 2026-11-13

- Base/default-branch starting commit: dc90463bdd734867308f03cb627eb8941efc19d6.
- Latest code/data-bearing research head: 826601139fd73a5152b6b37a5ed3574f3fca18a5.
- Dedicated branch: research/burmese-medials-g2p-evidence-2026-11-13.
- Draft PR: #147. It is intentionally not merged while independent linguistic adjudication remains absent.
- Required exact-head CI 43327571175 SUCCESS: 201 Python tests + 66 subtests; independent IPA gold schema validation; npm build; generated web-data freshness; 19 Node tests; 58 Chromium/Playwright tests.
- Optional raw comparator/CRF workflow 43327570809 SUCCESS. Outputs remain non-gold and accuracy remains null.
- Intermediate CI failures were fixed and rerun: 43324492175 exposed Python coda segmentation and matrix CSV issues; 43326933757 exposed a temporary practical_rules.csv path-mapping overwrite during documentation work. The table was restored from main, the conditional /ɴ/ note reapplied, and the final required CI passed.
- No runtime medial IPA rule was enabled. The structural coda fix is verified; phonological coverage remains PARTIAL.
- Independent expert-adjudicated IPA gold for the medial/coda cells: 0. Empirical accuracy: null.
- PR #129 remains open/draft and untouched as a code branch (53 commits ahead / 17 behind current main, non-mergeable); its source-backed research findings were reconciled into this branch, but its broad hybrid-engine code was not ported.
- Release assessment: PARTIAL PROTOTYPE, not linguistically release-ready. Research dossier is ready for specialist review and data-rights resolution.


### Romanization/G2P boundary — 2026-11-13

The browser romanization adapter explicitly requests Mya2Rom MLCTS, which the upstream README defines as orthographic. MLCTS2 is a more phonetic romanization but not standardized IPA. The Latin→Ukrainian crosswalk remains a separate orthographic mode and must not be used as a G2P/IPA oracle.


## Final exact-head verification — 2026-11-13

- Starting default-branch commit: dc90463bdd734867308f03cb627eb8941efc19d6.
- Latest code/data-bearing research head: fef242e4d4cc978823e4133f65abe48224355c13.
- Dedicated branch: research/burmese-medials-g2p-evidence-2026-11-13; draft PR #147 is open and not merged.
- Required exact-head CI 43328423650 SUCCESS: 201 Python tests + 66 subtests; independent IPA gold schema validation; npm build; generated web-data freshness; 20 Node tests; 58 Chromium/Playwright tests. The new Node regression asserts that the romanization adapter explicitly requests MLCTS, not MLCTS2 or IPA.
- Optional raw comparator/CRF workflow 43328423664 SUCCESS. These artifacts remain non-gold; no accuracy is reported.
- Intermediate CI failures were fixed and rerun: 43324492175 exposed Python coda segmentation and matrix CSV issues; 43326933757 exposed a temporary practical_rules.csv path-mapping overwrite during documentation work. The table was restored from main, the conditional /ɴ/ note reapplied, and final exact-head CI passed.
- Structural coda parsing is verified: မြန် is one syllable; မြန်မာ is two; ကတ် retains final consonant + ASAT. Browser/Python tests pass.
- No runtime medial IPA rule was enabled. Independent expert-adjudicated IPA gold for the medial/coda cells remains 0; empirical accuracy remains null.
- PR #129 remains open/draft and untouched as a code branch (53 commits ahead / 17 behind current main, non-mergeable); its source-backed research findings were reconciled here, but its broad hybrid-engine code was not ported.
- UCSY-SC1 remains historical metadata only; it is excluded from active text-only research.
- Release assessment: PARTIAL PROTOTYPE, not linguistically release-ready. The research dossier is ready for specialist review and data-rights resolution.

### Text-only source research continuation — 2026-11-13

| Task | Status | Evidence / acceptance boundary |
|---|---|---|
| Register Myanglish text candidate | PARTIAL | MYX_MYANGLISH_2026 and CLM-MYX-MYANGLISH-001 registered. 2,121 text pairs; informal non-standard romanization, predominantly one author's style; viewer/README field-count discrepancy (3 vs 2); CC BY-SA 4.0 declared. Do not use as IPA gold. Acceptance: inspect pinned raw CSV, reconcile all columns, sample and manually adjudicate text-only correspondences, document attribution/share-alike compatibility. |
| Register orthographic correction corpus | PARTIAL | MYX_ORTHO_2026 and CLM-MYX-ORTHO-001 registered. 4,800 rows; orthographic noisy-to-clean data; "phonetic" refers to confusion class, not IPA. Acceptance: inspect row quality and identify any actual medial examples before considering regression fixtures. |
| Assess John Okell text corpus | BLOCKED | OKELL_TEXT_2018 registered. Zenodo has 8.8 MB text file and blank Rights/License field; ELG catalogue lists CC BY 4.0. Acceptance: obtain direct rights clarification or corrected Zenodo/DataCite metadata before copying or redistributing. |
| Enforce text-only continuation scope | DONE_VERIFIED (documentation) | Corpus triage, research report, master matrix and handoff now explicitly exclude audio acquisition, processing and annotation. Existing SLR80/UCSY-SC1 entries remain historical metadata only. |

No corpus rows or pronunciation labels were imported. No runtime G2P rule was enabled. Independent expert-adjudicated IPA gold remains 0; empirical accuracy remains null. This source review does not change release status: **PARTIAL PROTOTYPE**.

### Historical medial-analysis reconciliation — 2026-11-13

- Added STEDT Monograph 3 (1996), pp.61-66, to the source and claim registries. It preserves one Written Burmese analysis (Benedict 1976, with Matisoff's additional notes) and two distinct Rangoon profiles (Burling 1967; Roop 1972).
- Written Burmese entry: /-w-/ is assigned to the rhyme; /-y-/ and /-r-/ to initial clusters. Rangoon entries list /-y-/ and /-w-/ with source-specific restrictions; Roop describes /r/ only in borrowings.
- Added two source-specific evidence-matrix entries, two evidence-only phonological-rule records and regression checks. Both remain WITHHELD and do not map directly to U+103B/U+103C/U+103D or authorize runtime output.
- Acceptance blocker: reconcile the underlying historical notation with modern Unicode spellings and the intended current Yangon profile using further written primary sources; retain the three source profiles separately.
- STEDT volume copyright is All Rights Reserved; only factual claims and locators are registered, no tables or source data copied.

### Written Burmese periodization and historical medial changes — 2026-11-13

- Registered Nishi (1997), *The Orthographic Standardization of Burmese*, and Matisoff (2003), *Handbook of Proto-Tibeto-Burman*.
- Nishi distinguishes OWB, MWB, EModWB and ModWB; records the replacement of OWB -l- by MWB -r-/-v- and later insertion of -y- after k-/kh- before written -i. He explicitly separates written H and spoken L phonological systems.
- Matisoff records WB *-r- > Modern Burmese -y- and warns that Written Burmese does not reliably preserve distinctions among proto-medials *-r-, *-l- and *-y-; orthographic shifts and exceptions are documented.
- Added two evidence-matrix entries, two evidence-only rules and regression tests. Both entries remain WITHHELD; no current Unicode-to-IPA or runtime rule is inferred.
- Acceptance criterion: reconcile Nishi's full 1976 "Medials in Burmese" treatment, historical inscriptional spellings, later written standards, and modern standard Yangon phonology using source-specific profiles and specialist review.

### Contextual voicing sandhi — 2026-11-13

- Registered Nishi (1998), *The Development of Voicing Rules in Standard Burmese* (DOI 10.15021/00004129), with three documentary claims.
- Added two source-linked evidence-only rule records: atonic C1aC2 voicing and voicing after non-stop tonal rhymes in close juncture.
- The paper reports substantial variation and exceptions and warns that Standard Burmese is not a well-defined variety. Regional dialects differ in rule presence.
- Both rules remain analysis-dependent and are not enabled globally. Acceptance requires a selected runtime profile, lexical/context coverage, written-source cross-checks and tests for optionality/exceptions. No audio evidence is part of the acceptance path.



- **Hill (2019) chapter 2** — BLOCKED / ACCESS. Cambridge confirms the Burmese historical-phonology chapter (pp.46-83), but only a short §44 preview was accessible. No medial-specific claim has been made. Acceptance: authorized full text, exact page locators and source-specific reconciliation before adding evidence.

### Exact-head verification checkpoint — 2026-11-13

| Check | Status | Evidence |
|---|---|---|
| Independent IPA gold structure validation | DONE_VERIFIED | CI run 43389272448, exact tested head 4145126ec65b834df96fc7ed57749a719daa27c2 |
| Python tests | DONE_VERIFIED | 206 passed + 66 subtests passed |
| npm build and generated-data freshness | DONE_VERIFIED | Both successful in run 43389272448 |
| Node tests | DONE_VERIFIED | 20 passed, 0 failed |
| Playwright/Chromium browser tests | DONE_VERIFIED | 58 passed |
| Optional Epitran/CRF diagnostics | DONE_VERIFIED (diagnostic only) | Run 43389279081; CRF 100/100 outputs, 84 source-concordant, 0 gold, accuracy null, possible training overlap; Epitran raw artifact only |
| Source registry integrity | DONE_VERIFIED | 51 sources, 55 claims, 28 medial rows, 19 phonological rules; no CSV width, duplicate-ID or traceability errors |
| Text-only scope | DONE_VERIFIED (documentation) | Handoff, corpus triage, completion register and source registry mark legacy non-text corpus records as excluded/deferred; no audio work |

The successful CI applies to exact head 4145126ec65b834df96fc7ed57749a719daa27c2. This checkpoint is documentation-only; any subsequent commit requires its own exact-head verification. Release status remains PARTIAL PROTOTYPE because independent text-adjudicated IPA gold is 0 and empirical accuracy is null.

### Green 2005 and SEAlang text-source gates — 2026-11-13

- Registered Green (2005), “Word, foot and syllable structure in Burmese”, an online CC BY-SA 4.0 source with broad IPA-style spoken transcription and separate ALA-LC orthographic transliteration. Added source-linked claims for CG onsets, major/minor syllables and /N/ nasalization. One medial evidence row and three evidence-only rules added; all remain WITHHELD/analysis-dependent.
- Registered SEAlang dictionary, Burmese Text Corpus and Burmese Bitext Corpus as text-only candidates. Dictionary transcription semantics are unresolved (IPA search/display metadata vs MLCTS2 documentation); corpora lack explicit reuse licenses. No rows imported.
- Acceptance: inspect SEAlang entries through an accessible interface, resolve the transcription encoding, obtain rights for any bulk extraction, and validate actual row schema. Green's phonological facts do not directly map Unicode medials.

### Final exact-head verification — 2026-11-13

| Area | Status | Evidence |
|---|---|---|
| Python + subtests | DONE_VERIFIED | 209 passed + 66 subtests, CI 43390071180 |
| IPA gold schema | DONE_VERIFIED | Independent structure validation passed; gold corpus remains header-only / 0 entries |
| Build and generated-data freshness | DONE_VERIFIED | npm run build and generated-data freshness check passed |
| Node tests | DONE_VERIFIED | 20 passed, 0 failed |
| Browser tests | DONE_VERIFIED | 58 Playwright/Chromium tests passed |
| Optional diagnostics | DONE_VERIFIED (not accuracy evidence) | CI 43390071177; CRF 100 predictions, 84 source-concordant, gold 0, accuracy null; Epitran raw artifact only |
| Registry integrity | DONE_VERIFIED | 55 sources, 62 claims, 29 medial rows, 22 phonological rules; no schema-width, duplicate-ID or traceability errors |
| Text-only scope | DONE_VERIFIED (documentation) | Legacy non-text records are historical-only and deferred; no audio work or data import |

Exact tested head: d2800ce458ea3c08c3fecb9e61ad170502837343. PR #147 remains Draft and is not release-ready. Linguistic gold=0 and empirical accuracy=null; classification remains PARTIAL PROTOTYPE.

### Final PR-head check — 2026-11-13

- PR #147 head 18b42a7415d3323220d09c0aacf2a17a3c6ff07d, 92 commits ahead of main / 0 behind, 25 files; OPEN / DRAFT / mergeable. No submitted reviews. PR #129 remains untouched.
- Exact-head run 43390340513: SUCCESS (209 Python + 66 subtests, IPA gold structure, build, generated-data freshness, 20 Node, 58 Playwright).
- Optional diagnostics run 43390071177: SUCCESS; CRF 100 predictions / 84 source-concordant / 0 gold / null accuracy / possible training overlap; Epitran raw-output artifact only.
- Registry integrity: 55 sources, 62 claims, 29 medial rows, 22 phonological rules; no CSV width, duplicate-ID or traceability issues.
- Text-only scope remains enforced; no audio, no corpus imports, no runtime rules promoted. Release status: PARTIAL PROTOTYPE.

### Nishi full-text and text-only corpus continuation — 2026-11-13

| Work item | Status | Evidence / acceptance boundary |
|---|---|---|
| Nishi (1998) Old Burmese historical medial analysis | DONE_VERIFIED (source evidence) | Full text inspected; source NISHI1998_OLDBURMESE; four claims/rules and 13 new medial/dialect rows; all historical rows WITHHELD from runtime. |
| Nishi (1998) voicing examples | DONE_VERIFIED (source phonemic, not IPA) | Seven examples in data/burmese/sandhi_evidence.csv; source transcription convention explicit; ipa_value empty; regression tests. |
| Myanglish corpus | PARTIAL / SCHEMA UNCERTAIN | Raw CSV has 2 columns, metadata/viewer expose third official_standard feature; informal romanization only, not IPA. |
| myX orthography corpus | PARTIAL / QUARANTINED_FOR_QUALITY_REVIEW | Sample target_words misalignment, multiple simultaneous substitutions and templated duplicates; permission confirmed, quality review required. |
| John Okell text corpus | BLOCKED / TOOL ACCESS | Research/ingestion permission confirmed by project owner; 8.8 MB file not retrievable in this execution environment. |
| SEAlang text and dictionary | BLOCKED / TOOL ACCESS + SCHEMA | Permission confirmed; direct entry/corpus retrieval unavailable; dictionary IPA vs MLCTS2 representation unresolved. |
| Hill (2019) chapter 2 | BLOCKED / TOOL ACCESS | Permission confirmed; only publisher excerpt for introduction/Tibetan chapter accessible, not Burmese chapter. |
| Text-only authorization | DONE_VERIFIED (project owner confirmation) | Research-use and project-ingestion permission confirmed for textual resources; no audio in scope. |

### Exact code/data-head verification — 2026-11-13

- Tested head: 4835a0abc3e7e4a18c9d0bda35f554031912d570.
- GitHub Actions run 43393402710: SUCCESS — 217 Python tests + 66 subtests; independent IPA-gold structure validation; npm build; generated-data freshness; 20 Node tests; 58 Playwright/Chromium tests.
- Earlier runs 43393310910 and 43393302505 failed only on a case-sensitive assertion expecting lower-case “historical merger only”; corrected to match the stored capitalized scope. Exact corrected-head run above passed.
- Registry integrity: 55 sources, 71 claims, 42 medial evidence rows, 28 phonological rules, 7 source-phonemic sandhi examples. Manual CSV parser verified row widths and all source/claim/rule/matrix links; no duplicate IDs or broken traceability.
- Independent expert-adjudicated IPA gold remains 0; empirical IPA accuracy remains null. No runtime medial/voicing rule promoted. Classification remains PARTIAL PROTOTYPE.

### Final exact-head verification — 2026-11-13 (supersedes earlier snapshots)

- Final tested head: c03706474cf67b480c449790c9592e5fe0e53fd4.
- Main CI run 43394274053: SUCCESS — 217 Python tests + 66 subtests; independent IPA-gold schema validation; npm build; generated-data freshness; 20 Node tests; 58 Playwright/Chromium tests.
- Optional diagnostics run 43394274111: SUCCESS — CRF 100 predictions / 84 source-concordant / gold_count 0 / accuracy null / NOT_SCORED_POSSIBLE_TRAINING_OVERLAP; Epitran raw-output artifact only.
- Final registry counts: 56 sources, 71 claims, 42 medial evidence rows, 28 phonological rules, 7 source-phonemic sandhi examples. Manual CSV integrity check found no malformed widths, duplicate IDs or broken source/claim/rule/matrix references.
- Nishi (1976) Medials in Burmese is registered as a primary-source target, but its full text was not retrieved. Nishi (1998) Old Burmese is a separate full-text source and only a secondary summary of Nishi 1976.
- Project owner confirms text-only research and project-ingestion permissions. No audio used. External corpus access/schema and quality gates remain.
- PR #147 OPEN / DRAFT / mergeable, 135 commits ahead, 0 behind, 28 files. PR #129 untouched.
- Gold remains 0; accuracy remains null; no runtime medial or voicing rule promoted. Repository remains PARTIAL PROTOTYPE.


### Okell (1995) dialect evidence — 2026-11-13

| Work item | Status | Evidence / acceptance boundary |
|---|---|---|
| Okell (1995) WB/SB and regional medial profiles | DONE_VERIFIED (source evidence) | Full text; AR preserves WB r/y, SB merges; IT/TV have medial /l/ absent in SB; three matrix rows, seven claims, two dialect rules and regression tests. |
| Modern Yangon medial profile | PARTIAL / EVIDENCE-LIMITED | Do not infer from Arakanese, Intha, Tavoyan or historical OWB; requires current Yangon-specific text evidence and independently adjudicated examples. |
| Okell transcription convention | DONE_VERIFIED (source scope) | Texts are phonemic with limited allophonic approximations; not project IPA gold. No audio accessed. |


| Okell (1969) Reference Grammar | BLOCKED / TOOL ACCESS | Bibliographically verified; cited for Standard/Colloquial Burmese phonology and voicing sandhi, but full text unavailable in this execution. Permission confirmed; exact section/page evidence still required. |


### Consolidated text-only research snapshot — 2026-11-13

- Exact tested code/data head: 2a96f4121a43f704a8f0d2eb6d81cb343fba47db.
- Main CI 43395906072 SUCCESS: 219 Python tests + 66 subtests; IPA-gold structure validation; npm build; generated-data freshness; 20 Node tests; 58 Playwright/Chromium tests.
- Optional diagnostic 43395906100 SUCCESS: CRF 100 predictions, 84 source-concordant, gold_count=0, accuracy=null, NOT_SCORED_POSSIBLE_TRAINING_OVERLAP; Epitran raw-output artifact only.
- Registries: 58 sources, 78 claims, 45 medial evidence rows, 30 phonological rules, 7 source-phonemic sandhi examples. Manual CSV validation found no malformed widths, duplicate IDs or broken references.
- Okell (1995) dialect profiles and Nishi (1998) historical medials are source-evidenced and tested; all remain withheld from runtime. Okell (1969) and Nishi (1976) are registered full-text targets, not yet retrieved.
- Owner confirms text-only research and project-ingestion permissions. No audio used. Okell/SEAlang/Okell1969/Nishi1976/Hill retrieval and corpus schema/quality gates remain.
- PR #147 OPEN / DRAFT / mergeable, 0 commits behind main and 28 files; current ahead count is tracked on the PR; PR #129 untouched.
- IPA gold remains 0, accuracy null, no runtime rules promoted. Status PARTIAL PROTOTYPE.


### Final text-only evidence snapshot — 2026-11-13

- Exact tested code/data head: cda73ccb7fa80a0404fed5a65588ebd690253f94.
- Main CI run 43397172081 SUCCESS: 220 Python tests + 66 subtests; independent IPA-gold structure validation; npm build; generated-data freshness; 20 Node tests; 58 Playwright/Chromium tests.
- Optional diagnostics run 43397181331 SUCCESS: CRF 100 predictions, 84 source-concordant, gold_count=0, accuracy=null, NOT_SCORED_POSSIBLE_TRAINING_OVERLAP; Epitran 1.35.3 raw-output artifact only.
- Final registries at the 2026-11-13 continuation: 59 sources, 83 claims, 45 medial evidence rows, 30 phonological rules, 7 source-phonemic sandhi examples, 9 orthographic-only Okell corpus profile rows. Manual CSV validation found no malformed widths, duplicate IDs or broken references.
- Okell (1995) dialect profiles and Nishi (1998) historical medials are source-evidenced/tested; all remain withheld from runtime. SEAlang 2008 confirms IPA query/display at interface level, but internal storage remains unresolved against Mya2Rom MLCTS2. Okell (1969) and Nishi (1976) remain registered but unread full-text targets.
- Project owner confirms text-only research and project-ingestion permissions. No audio used. Corpus byte access, internal SEAlang schema, Myanglish metadata reconciliation and myX quality remain gates.
- PR #147 remains OPEN / DRAFT / mergeable, 0 commits behind main, 28 files. Current ahead count is tracked on the PR.
- IPA gold remains 0, accuracy null, no runtime rules promoted. Status PARTIAL PROTOTYPE.


### Okell text corpus — access status correction (2026-11-13)

| Work item | Status | Evidence / acceptance boundary |
|---|---|---|
| Okell *A Corpus of Modern Burmese* content access | PARTIAL / CONTENT AND BYTE INTEGRITY VERIFIED | Zenodo direct file endpoint HTTP 200, text/plain UTF-8; provider MD5 f020d7bbcf9857631094a8861143d18f matched; 8,809,265 bytes; SHA-256 6bbafd699c587876317f6e0535b9dd8f9ec87c15efe4b7e65a8c7362ebcdbf4c; 19,565 CRLF-terminated lines (19,566 split segments including the final empty segment), 67 numbered heading lines, valid UTF-8, Myanmar Unicode, Burmese/English mixed content, dialogue/speech transcripts and prose. |
| Okell corpus integrity and quality | PARTIAL / TEXT_QUALITY_AUDIT_PENDING | Byte identity is verified (Zenodo MD5 match; SHA-256 6bbafd699c587876317f6e0535b9dd8f9ec87c15efe4b7e65a8c7362ebcdbf4c); 21 BOM markers, one NUL, non-NFC, 295 repeated nonblank line forms / 1,008 excess occurrences and 23 repeated paragraph forms profiled. Acceptance: map embedded boundaries to original documents, classify repeated passages, inspect corruption/NUL without altering source, document segment provenance. |
| Okell corpus as IPA/G2P gold | DEFERRED / NOT GOLD | No IPA annotation schema or independently adjudicated IPA values identified. Do not import as IPA gold or score predictions against it. |

No corpus rows were imported and no audio was accessed or used. This correction supersedes prior BLOCKED_TOOL_ACCESS classification; SEAlang entry/schema access remains separately unresolved.


### Okell corpus structure and duplicate-line profile — 2026-11-13

| Work item | Status | Evidence / acceptance boundary |
|---|---|---|
| Byte/Unicode integrity | DONE_VERIFIED (retrieved-byte profile) | Zenodo MD5 matched; SHA-256 6bbafd699c587876317f6e0535b9dd8f9ec87c15efe4b7e65a8c7362ebcdbf4c; 8,809,265 bytes; valid UTF-8; 19,565 CRLF-terminated lines (19,566 split segments including the final empty segment); 21 BOM markers; one NUL; non-NFC; zero U+FFFD. |
| Structural/duplicate profile | PARTIAL | 67 numbered heading lines; 295 repeated nonblank line forms / 1,008 excess occurrences; 23 repeated paragraph forms. Repeated poem/title/header/divider lines mean these are not duplicate-document counts. |
| Provenance and text quality | TODO | Map embedded BOM/title boundaries to original documents; inspect line 9,300 NUL and localized glyph corruption; classify duplicate passages and source provenance before any extraction. |

No deduplication or normalization was applied to the source copy; no audio or IPA gold was used.


### Okell corpus orthographic-only profile — 2026-11-13

| Metric | Count | Status |
|---|---:|---|
| U+103B | 50,072 | ORTHOGRAPHIC_ONLY |
| U+103C | 73,107 | ORTHOGRAPHIC_ONLY |
| U+103D | 49,248 | ORTHOGRAPHIC_ONLY |
| U+103E | 50,869 | ORTHOGRAPHIC_ONLY |
| `မြန်` substring | 659 | ORTHOGRAPHIC_ONLY |
| `မြန်မာ` substring | 288 | ORTHOGRAPHIC_ONLY |

Full profile: `data/burmese/okell_text_corpus_orthographic_profile.csv`. These are raw codepoint/substring counts, not token or phonological frequencies; no IPA or runtime rule follows from them.


## Final exact-head verification — 2026-11-13

Final branch head `601cf85a5c740627848f9eff1fa1f0911cf03796` on `research/burmese-medials-g2p-evidence-2026-11-13`, based on unchanged main `dc90463bdd734867308f03cb627eb8941efc19d6`. PR #147 is open/draft/mergeable, 195 commits ahead and 0 behind, 29 files. PR #129 is open/draft and untouched, diverged 53 ahead / 17 behind and non-mergeable.

Exact-head CI: `43449980180` and `43449989336` SUCCESS — 222 Python tests + 66 subtests; IPA schema validator ran with zero gold records; npm build and generated-data freshness passed; 20 Node and 58 Playwright/Chromium tests passed. Optional diagnostics `43449989348` SUCCESS — CRF 100 predictions, 84 source-concordant, 0 gold, null accuracy, NOT_SCORED_POSSIBLE_TRAINING_OVERLAP; Epitran raw output only. No audio, no runtime medial rules, no merge/release.

The Okell corpus byte identity and orthographic-only profile are now documented in the root handoff and research review. Final assessment remains PARTIAL PROTOTYPE, not release-ready.


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
| 94 MLCTS rime vendor audit | PARTIAL / PRIMARY-SOURCE EVIDENCE GATE | 94/94 keys and MLCTS column values match vendored Mya2Rom 0.4.4; 25 collision groups are machine-readable. Original MLC primary tables and word-level adjudication remain unverified; all Ukrainian candidates remain PROPOSED/EVIDENCE_LIMITED. |

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


## MLCTS collision lexical cross-check — 2026-11-13

| Task | Status | Evidence | Acceptance boundary |
|---|---|---|---|
| 25-group collision evidence ledger | PARTIAL | Added data/burmese/romanization_rime_collision_lexical_audit.csv with one row per existing collision group. All 25 source-unit pairs are preserved. | This is a triage ledger, not a primary-source adjudication. |
| am / မ်;ံ comparison | PARTIAL — SECONDARY TABLE MATCH | Wiktionary's comparative rhyme table gives ကမ် and ကံ the same /kàɴ/ and MLCTS kam in the က-onset examples. | Do not generalize to all words or claim MLC dictionary headword attestation. |
| any / ဉ်;ည် comparison | BLOCKED — SOURCE CONFLICT | Wiktionary's table distinguishes ကဉ် (kañ‘; /kɪ̀ɴ/) and ကည် (kany; /kì/, /kè/, /kɛ̀/), while Mya2Rom maps both isolated keys to any. | Primary MLC table/entry verification is required before correcting vendor data. |
| Other 22 collision groups | TODO — LEXICAL EVIDENCE | No direct primary-source lexeme pairs checked. | Record MLC dictionary headword, exact page/entry locator, source spelling, IPA/MLCTS fields and contextual analysis for representative examples in each group. |
| Special u. / ့;ု group | PARTIAL — CONTEXT-DEPENDENT | ့ is an auk-myit-induced vendor fallback, not an ordinary independent rime. | Exclude it from ordinary lexical equivalence decisions; analyze its syllabic context separately. |

Registry integrity on this continuation: 62 source records, 114 claim records; 25 collision groups; 25 lexical-audit rows. CSV parsing confirms consistent widths, unique source/claim IDs, and no broken claim-to-source references. New Python regression coverage is committed; exact-head CI run 43491503349 was still in progress at the time of this matrix update. No local test execution is claimed. No runtime or Ukrainian candidate changes; no audio used.


## Nasal-final secondary-source reconciliation — 2026-11-13

- Added Wikipedia's MLC-system overview as a secondary source and registered claim CLM-WIKI-MLCTS-NASAL-FINALS-001. It lists shared -any, -am and -um spellings for the paired finals.
- Reclassified the am and um groups as SECONDARY_SYSTEM_EQUIVALENCE (supported by both secondary tables), and any as SECONDARY_SOURCE_CONFLICT (Wiktionary detailed table vs Wikipedia's MLC summary vs vendor). No primary MLC adjudication is claimed.
- Lexical ledger now has 21 unadjudicated, 2 secondary-equivalence, 1 secondary-conflict and 1 special non-rime group. Totals: 63 sources / 115 claims. No runtime or Ukrainian candidate changes. CI on the preceding head was still in progress; final exact-head verification pending.


## Exact-head CI result — 2026-11-13

- Code/data head: 46b7da6afd7ecc94e4dcac87c7f759132c74bc6b.
- Required workflow run 43491799213: SUCCESS. Python 229 passed + 66 subtests passed; Node 20 passed / 0 failed; Playwright 58 passed. Gold validator executed and correctly returned NOT_READY_NO_ADJUDICATED_GOLD. npm install, production build, generated-data freshness, Chromium install and browser suite all passed.
- npm install still reports 1 high-severity dependency vulnerability; no forced dependency upgrade applied.
- Optional diagnostics run 43491799196: SUCCESS (raw-output and CRF diagnostic jobs). These are raw diagnostic artifacts only, not an IPA accuracy benchmark; independent adjudicated IPA gold remains 0.
- Final linguistic status remains PARTIAL PROTOTYPE. No runtime rule or Ukrainian candidate promoted.



## MLCTS primary-source provenance check — 2026-11-13

- Added **OHNMAR_HTUN_2013**, the Nagaoka University of Technology doctoral dissertation *Development of Cross-Lingual Phonetic Similarity Metrics*. Its §5.1.2.3 (p.80) labels MLCTS as the 1980 Myanmar Language Commission system and gives three sample romanizations. Crucially, its bibliography entry [47] (p.122) cites the Wikipedia MLC Transcription System page, accessed 2012-10-12, rather than identifying or reproducing an MLC primary publication. This is a secondary provenance trail, not independent confirmation of the full 1980 table.
- Added **ALA_LC_BURMESE_2011**, the Library of Congress *Burmese Romanization Table* (2011). It is an ALA-LC table, not MLCTS; keep its forms separate and do not use it to adjudicate MLCTS collision rows.
- New claims: CLM-MLCTS-SECONDARY-PROVENANCE-001 and CLM-ALA-LC-NOT-MLCTS-001. Registry totals: **66 nonblank source records / 118 claims**.
- This search did not recover the primary MLC 1980 specification or primary word-level dictionary entries. The MLC-primary-source task remains **BLOCKED / EVIDENCE GATE**; acceptance remains direct inspection of the actual MLC tables and properly located dictionary entries, with the transcription field distinguished as MLCTS vs MLCTS2.
- No vendor mapping, runtime rule, IPA gold label or Ukrainian candidate changed. No audio accessed.

## Registry count reconciliation — 2026-11-13

A fresh parse of the current CSV registries, counting only nonblank source rows and requiring unique IDs, finds **66 source records and 117 claim records**. The previous continuation note's 65-source count was one too low; the current source registry contains 66 nonblank IDs. Two pre-existing blank CSV records in `sources.csv` are ignored for this count. All 117 claim IDs are unique and every claim's `source_id` resolves to a registered source. The two new provenance records and claims are included in these totals.

A regression test now protects the distinction between the Htun secondary provenance trail and the LOC ALA-LC table. Test/CI status for the final code-bearing commit is pending verification; no local checkout was available in this connector session.

## MLC dictionary bibliographic cross-check — 2026-11-13

- Added **UNICODE_REFERENCE_LISTS_2022** and claim **CLM-MLC-DICT-BIB-UNICODE-001**. The Unicode Consortium's *Other Script Sources* bibliography lists the Myanmar-English Dictionary as a 1993 work compiled and edited by the Myanmar Language Commission, and a 1996 Myanmar orthography treatise (PDF lines 681–690).
- This independently strengthens the bibliographic locator for MLC primary material, but the Unicode bibliography does not reproduce dictionary entries or MLCTS/MLCTS2 tables. It therefore does not clear the primary-source evidence gate.
- Added regression assertions for the new bibliography record and its narrow evidential scope. No linguistic mapping was changed.
- Registry totals after this addition: **66 nonblank source records / 118 claims**.

## Final verification boundary for this continuation — 2026-11-13

- Registry parse on the current branch: **66 nonblank source records / 118 claim records**; all IDs unique, all row widths conform to their CSV headers, and every claim source reference resolves. Two blank CSV records are ignored by the count.
- The provenance regression test was added to `tests/test_romanization_rime_inventory.py`. The GitHub connector exposed no workflow runs and no commit status checks for final code/documentation head `caf66d5a6b58522ca33715654c38b075c1d1fc21`; therefore this latest test change is **NOT YET CI-VERIFIED**. Earlier successful CI on prior code/data head `46b7da6afd7ecc94e4dcac87c7f759132c74bc6b` does not cover this added test.
- No local checkout or local Python test execution was available. Do not claim the new test passed.

## MLC dictionary physical-access leads — 2026-11-13

- Added **WHO_MLC1993_DICT_CATALOG**: WHO Myanmar Library record 487 identifies the 1993 MLC dictionary (635 pages) and lists a physical copy as available at WHO Myanmar.
- Added **NDL_MLC1996_DICT_CATALOG**: National Diet Library record 000003254368 identifies the 1996 Dunwoody Press reprint (xxiii, 635, iii pages), call number KL42-A3, with Tokyo Main and Kansai-kan holdings and one cooperating Japanese library holding.
- New claims: CLM-MLC-DICT-1993-PHYSICAL-HOLDING-001 and CLM-MLC-DICT-1996-NDL-HOLDING-001. Registry totals: **68 nonblank source records / 120 claims**.
- These are concrete acquisition/consultation leads, not evidence from the book's contents. WHO and NDL catalogue records do not provide the MLCTS table or word-level entries. The MLC-primary-source acceptance gate remains blocked until the physical/authorized text is inspected and the transcription field is distinguished as MLCTS vs MLCTS2.
- Regression assertions now cover both catalogue records and explicitly preserve their access-only scope. No linguistic mapping or runtime behaviour changed.

## MLC dictionary transcription-purpose evidence — 2026-11-13

- Added **BURMA_DEBATE_1996_MLC_DICT_NOTICE** and claim **CLM-MLC-DICT-PRON-GUIDE-001**. A contemporaneous notice for the Dunwoody Press reprint says the dictionary uses a transcription system as an aid to pronunciation for English speakers and contains nearly 35,000 entries (Burma Debate, Nov/Dec 1996, p.40).
- This is a useful clue about the dictionary field's purpose, but it does not name the system. It cannot establish MLCTS2, nor can it substitute for inspecting the dictionary's own front matter and entries.
- Registry totals: **69 nonblank source records / 121 claims**. Regression assertions preserve the ambiguity explicitly. No mapping or runtime change.

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

## MLCTS vs modified-column collision crosswalk — 2026-11-13

- Added **MOW_2017_MLCTS_VARIANTS** and claim **CLM-MOW-MLCTS2-VARIANTS-001**. MOW's own project page says v0.1.2 added romanized variants searchable via both MLCTS and “MLCTS 2”, explicitly describing the latter as the version used in the MLC Myanmar-English Dictionary; MOW v0.1.3 is a CC BY 4.0 downloadable semantic wordnet. This is corroboration of the distinction and a lexical-resource lead, not an MLC primary specification.
- Audited the actual Mya2Rom v0.4.4 third array column for all 25 MLCTS collision groups and added `data/burmese/romanization_rime_mlcts2_crosswalk.csv`. Results: **21 groups retain identical third-column output; 4 groups differ**: `any` (ဉ်/ည်: `in/i`), `any:` (ဉ်း/ည်း: `in:/i:`), `any.` (ဉ့်/ည့်: `in./i.`), and `ui` (ို်/ို: `ai'/ou`). The vendor's IPA column also differs for these four pairs. This shows the modified column is more discriminating for these particular source-unit pairs; it does not establish primary MLC lexical correctness or independent IPA gold.
- Important naming detail: Mya2Rom v0.4.4 README/API calls the third column `mlcts2`; `mya2rom.js` maps that mode to array index 2; the `romanisations.js` header labels the same column **MLCTS-SL** and describes it as the SEAlang/MLC dictionary modification. Added claim **CLM-MYA2ROM-COLUMN3-NAMING-001** to record this internal nomenclature discrepancy; no evidence of two separate columns in this version.
- Added exact-source regression coverage that derives all 25 crosswalk rows from the vendored array and guards the four distinct groups, special `့` fallback, and non-primary evidence boundary.
- Registry totals after additions: **70 nonblank source records / 123 claims**. No runtime mapping, IPA gold label or Ukrainian candidate changed. All 94 Ukrainian candidates remain PROPOSED / EVIDENCE_LIMITED.

## Earlier MLC Concise Burmese Dictionary access lead — 2026-11-13

- Added **ALLOTT1985_BURMA_LANGUAGE_POLICY** and **OKELL1982_BURMESE_DICTIONARY_REVIEW** with claims **CLM-MLC-CONCISE-DICT-1978-80-001** and **CLM-MLC-CONCISE-DICT-BIB-001**.
- Allott's 1985 chapter (p.145) reports that the MLC Concise Burmese Dictionary was published in five parts from late 1978 through 1980, standardized the official orthography of its entries, and supplied pronunciations. Okell's 1982 bibliography independently lists it as five volumes, Rangoon, Mranmācā Aphwai.
- This identifies a potentially earlier MLC primary lexicon with pronunciation information. Neither secondary source reproduces the dictionary's pronunciation key, any romanization table, or the relevant lexical entries. It is not yet established that this dictionary uses MLCTS/MLCTS2; inspect the front matter and representative entries before claiming that.
- Registry totals: **72 nonblank source records / 125 claims**. New regression assertions preserve the secondary-only status.

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

## MOW lexical word-form coverage for collision endings — 2026-11-13

- Retrieved the official MOW 0.1.3 release TSV from `myanmaropenwordnet/mow`; upstream blob SHA `0c97fc4e98b3827dae0bc667858993037496ca58`. The release header and repository README state CC BY 4.0. It contains 1,476 `mya:lemma` rows and 1,041 distinct Burmese lemma strings.
- Added `data/burmese/mow_rime_orthographic_coverage.csv` (50 source-unit rows) and `data/burmese/mow_rime_orthographic_matches.csv` (508 exact source-unit/lemma pairs). The matching operation is strictly Unicode string `endsWith(source_unit)`; it does not syllabify, identify lexical rimes, or provide pronunciations.
- The 508 pairs cover 442 distinct lemma strings and 547 synsets; 35/50 source-unit variants occur at least once. Both variants of 11/25 collision groups occur in MOW (`a`, `a:`, `am`, `am:`, `am.`, `any`, `any:`, `au`, `auk`, `aung:`, `u.`); only one side occurs for 13/25 groups; neither side occurs for `um.` in this small resource.
- These are lexical orthographic search leads only. They do not adjudicate the MLCTS collision, prove that two spellings are homophonous, or establish source-language phonology. Absence from this limited wordnet is not evidence that a form does not exist. The 21 collision groups remain unadjudicated; the prior two secondary equivalence groups, one secondary conflict and one special non-rime remain unchanged.
- Reused the canonical reproducible generator `scripts/analyze_mow_orthographic_rime_coverage.py` and vendored CC BY 4.0 source snapshot `data/burmese/external/mow-0.1.3-mya_20171005165336.tab`; regression tests invoke the generator in `--check` mode and assert coverage totals. Redundant parallel CSV exports were removed. Registry totals: **73 nonblank sources / 126 claims**; unique IDs and claim references validated. CI for the latest test-bearing commit is pending.

## Reproducible MOW orthographic coverage audit — 2026-11-13

- Vendored the exact upstream MOW v0.1.3 TSV at `data/burmese/external/mow-0.1.3-mya_20171005165336.tab`; its original header is preserved: `## MOW 0.1.3 / mya / CC BY 4.0`. Source ID **MOW_2017_0_1_3_DATASET** and claim **CLM-MOW-ORTHOGRAPHIC-RIME-COVERAGE-001** were added in the concurrent continuation commits already on this branch.
- Added deterministic stdlib-only generator `scripts/analyze_mow_orthographic_rime_coverage.py` with `--check` mode, plus generated files `mow_rime_orthographic_matches.csv` (508 exact source-unit/lemma pairs) and `mow_rime_orthographic_coverage.csv` (50 source-unit rows).
- Recomputed results from the vendored file: 1,476 MOW `mya:lemma` rows, 1,041 distinct lemma forms, 1,198 synsets; 508 suffix-match pairs across 35/50 source-unit variants; 442 distinct matched lemmas and 547 distinct matched synsets. For the 25 collision groups: both variants occur in 11 groups, one side in 13, neither in 1.
- These are exact Unicode orthographic suffix matches, not Burmese syllabification or pronunciation. They do not confirm homophony, MLCTS equivalence, MLC system correctness, or Ukrainian outputs. The generator/test preserve this limitation. The raw upstream license header and source attribution are retained.
- Added two tests: source/license header preservation and reproducible output/count/evidence-boundary validation. Exact-head CI pending.

### Schema-gate correction for MOW dataset-derived claim — 2026-11-13

The first CI attempt after registering the MOW orthographic coverage claim (workflow 43499220650) correctly rejected the locally invented evidence status `DATASET_DERIVED`, because the canonical claim schema does not allow that value. The claim was corrected to the existing schema-supported status `ANALYSIS_DEPENDENT` (commit 5e12f86e21f5576efee44afe84f80759e3799a9e); its scope remains orthographic suffix analysis only. The subsequent exact-head workflow is running with the schema correction, canonicalized test placement and reproducible generator check.

## Final MOW reuse reconciliation and exact-head verification — 2026-11-13

- Canonical MOW analysis is `scripts/analyze_mow_orthographic_rime_coverage.py`, using vendored CC BY 4.0 source `data/burmese/external/mow-0.1.3-mya_20171005165336.tab`; canonical outputs are `data/burmese/mow_rime_orthographic_matches.csv` and `data/burmese/mow_rime_orthographic_coverage.csv`. Removed the parallel duplicate exports and their duplicate test module. The retained regression test invokes the canonical generator with `--check`.
- Exact final code/test head: **c76fab9e4e4a910170a26dd8ed89a95790c7973d**. Required CI run **43499475187** (push) and **43499485256** (pull request) both SUCCESS: **236 Python tests + 66 subtests**, **20 Node tests**, **58 Playwright tests**, Chromium installation, production build and generated-web-data freshness all PASS. Optional diagnostics run **43499485104** SUCCESS for raw-output and CRF diagnostic jobs only; no scored accuracy benchmark.
- IPA validator runs successfully but continues to report **NOT_READY_NO_ADJUDICATED_GOLD** (zero independently adjudicated gold records). `npm install` reports **one high-severity vulnerability** and recommends `npm audit fix --force`; no forced dependency upgrade was applied.
- Source registry revalidated: **73 sources / 126 claims**, unique source IDs and claim IDs, valid claim→source references and expected CSV widths.
- SEAlang remains a viable authorized derivative access route according to its metadata, and its API is documented as accepting orthography/IPA. However, direct Burmese dictionary/API retrieval returned 502/timeout/400-timeout in this pass; connected page-retrieval credits were exhausted, so **no SEAlang entry text was inspected**. Do not treat interface metadata as entry-level phonetic evidence.
- Final branch head after this status entry will be docs-only; code/test evidence above applies to exact code/test head `c76fab9e...`. PR #147 remains OPEN / DRAFT / mergeable; branch is 386 commits ahead of main and 0 behind at the time of verification.

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

## MLC 1986 orthography book — National Library catalog locator (2026-11-13)

- Added **MLC_1986_ORTHOGRAPHY_NLMNPT_189** and claim **CLM-MLC-1986-ORTHOGRAPHY-CATALOG-001**. The National Library of Myanmar E-Resources record 189 lists *မြန်မာစာလုံးပေါင်းသတ်ပုံကျမ်း*, author/publisher Myanmar Language Commission, Yangon 1986, second edition, 292 pages, 23 cm, and a PDF option.
- This catalog record aligns with Unicode WG2 N2827's statement that the MLC's *Myanmar Orthography* was published in October 1986 and prescribed as the national standard. It is a strong primary-book locator, not inspection of the book. The bibliographic page returned 502 in this pass; no PDF pages, foreword, tables or pronunciation key were inspected.
- Added regression coverage that prevents the catalog record from being treated as content evidence. Registry totals: **77 sources / 130 claims**; IDs unique, CSV widths valid and all claim→source references resolve. CI on test-bearing head `a824fe13c3671b5f02d37c3dc9127ffc460ac1a8` is pending.

## Partial primary scan of the 1986 Myanmar Spelling Dictionary — 2026-11-13

- Added **UNICODE_L2_2010_MLC_SPELLING_1986** and **CLM-UNICODE-L2-2010-MLC-SPELLING-SCAN-001**. Unicode WG2 paper L2/10-360 identifies a *Myanmar Spelling Dictionary* published in 1986 and reproduces an image of original page 1, headed “Characters pronunciation List”, plus images of pages 2-9. The explanatory note says the character pronunciation list corresponds to a Myanmar Language Character Map and discusses sorting.
- This is the first directly viewable partial scan of a 1986 Myanmar spelling reference found in this pass. It is not a complete book; the visible tables are orthographic character/pronunciation-list material, not an MLCTS/IPA rime table or word-level dictionary entries. Its identity with the MLC *Myanmar Orthography* in N2827 and National Library record 189 remains unconfirmed.
- The National Library of Myanmar E-Resources catalog record 189 separately lists the MLC 1986 orthography book as a second edition, 292 pages, with a PDF option; the catalog page itself timed out. The Unicode partial scan is a concrete additional source lead but does not clear the primary transcription evidence gate.
- Added regression assertions for the partial-scan status and non-MLCTS/IPA boundary. Registry totals: **78 sources / 131 claims**; IDs unique, CSV widths valid, and all claim→source references resolve.

## Final checkpoint — 2026-11-13

- Dedicated branch `research/burmese-medials-g2p-evidence-2026-11-13`: **445 commits ahead of main / 0 behind**. PR **#147** is **OPEN / DRAFT / mergeable**, unmerged; 40 changed files. PR #129 remains untouched (divergent/non-mergeable at last review); PR #146 remains merged. Main and release state unchanged.
- Latest required CI on code/test head `8e8448b70549062636c3f1c539ee1010f93a86cb`, run **43501650235 SUCCESS**: **241 Python + 66 subtests**, **20 Node**, **58 Playwright**, Chromium, production build and generated-data freshness all passed. Optional diagnostics **43501650409 SUCCESS** (raw-output + CRF; not an accuracy score).
- Source registries: **78 sources / 131 claims**, all IDs unique, valid row widths, all source references resolve.
- Remaining blockers: obtain and inspect complete MLC orthography/1993 dictionary contents and identify the exact transcription field; adjudicate the 25 collision groups from primary lexical evidence; build independent IPA gold and validate tone/prosody; resolve one high-severity npm vulnerability. Status remains **PARTIAL PROTOTYPE / NOT RELEASE-READY**.

## Structural parser coverage for all MLC medial forms — 2026-11-13

- Added `tests/test_parser.py::test_mlc_medial_inventory_is_parsed_structurally_without_phonetic_guessing`. It exercises the four basic medial signs, five two-medial forms and two three-medial forms listed in N2827 using a real Burmese onset. It verifies one orthographic syllable, ordered medial IDs, established structural parse, and that `ipa` remains `None` and `phonology` remains empty.
- This is a real executable improvement to the orthographic parser's regression coverage. It does **not** enable medial-to-IPA rules, resolve context-dependent allophony, or promote any candidate pronunciation. All medial phonological behavior remains withheld.
- Exact test-bearing code head **29add5691bee13a544568fb9edec2587e447c44f**; CI run **43502733106 SUCCESS**: **242 Python tests + 66 subtests**, **20 Node tests**, **58 Playwright tests**; Chromium, production build and generated-data freshness all pass. IPA gold remains `NOT_READY_NO_ADJUDICATED_GOLD`; npm install still reports one high-severity vulnerability.

## MOW v0.1.3 lexical orthographic coverage — verified implementation reconciliation (2026-11-13)

- Existing generator `scripts/analyze_mow_orthographic_rime_coverage.py` and generated outputs were inspected and preserved. Exact Unicode suffix matching yields 508 source-unit/lemma pairs over 50 collision source-unit variants; output records explicitly label every match `ORTHOGRAPHIC_SUFFIX_MATCH_ONLY`.
- Coverage: 11/25 MLCTS collision groups have both source units found in MOW, 13/25 have one, and 1/25 has neither. This measures only MOW's lexical coverage; no pronunciation, phonological rime, syllable segmentation, or equivalence is inferred. The 1,476 lemma rows / 1,041 unique forms / 1,198 synsets are small-resource counts, not a census of Burmese.
- Exact-head CI on PR #147 head `50a29bb880256fbd0c977bc9dc1f45bb4ad49d2d`, run **43503144848**, passed: 242 Python + 66 subtests, 20 Node, 58 Playwright, production build, generated-data freshness. IPA gold gate remains `NOT_READY_NO_ADJUDICATED_GOLD`; one high-severity npm vulnerability remains.
- PR #147 remains open/draft/mergeable; branch is 455 ahead / 0 behind. No linguistic candidate or runtime behavior promoted.

## MLC 1978 spelling-book catalogue lead — 2026-11-13

- Added a separate NDL catalogue source for *မြန်မာစာလုံးပေါင်းသတ်ပုံကျမ်း*, a Burmese-language MLC orthography/spelling reference published in 1978. Allott's inspected 1985 chapter separately reports a spelling book published in 1978 and a five-part Concise Burmese Dictionary issued from late 1978 to 1980 (ANU PDF lines 10082–10113).
- This raises a bibliographic hypothesis that the spelling book and Concise Dictionary are distinct publications. Exact title identity and relationship remain to be checked against title pages; catalogue metadata alone does not prove the contents or any pronunciation notation.
- Registry updated: 80 sources / 132 claims (historical checkpoint; source count corrected after blank-row cleanup). Added a regression test protecting the distinction and evidence boundary. No runtime, MLCTS, IPA or Ukrainian mapping changed. Exact-head CI pending.

## MLC spelling-book retrieval routes — 2026-11-13

- CiNii Books record BA69415754 gives a fuller physical description (28, 379 pages, 17 cm) and lists three Japanese library holdings, including Osaka University and Tokyo University of Foreign Studies. Google Books record _V1LAAAAMAAJ identifies a University of Michigan original and a digitized 379-page scan from 2007, but the surfaced access is snippet-view metadata, not a verified full-text download.
- Added a separate catalogue/digitization source and regression test. Registry totals: 80 sources / 133 claims (verified nonblank, unique source IDs). The primary book remains uninspected; request a copy or inspect accessible pages before making any pronunciation/MLCTS claim.

## Crosswalk consistency validation — 2026-11-13

- Added `tests/test_rime_crosswalk_consistency.py` for the three existing 25-group rime crosswalks. It checks shared key coverage and Myanmar source-unit alignment, per-source-unit MLCTS2/IPA array alignment, R12A comparison-state counts (18 same, 3 distinct, 2 partial, 1 absent, 1 special), and lexical audit evidence-state counts (21 unadjudicated, 2 secondary equivalence, 1 secondary conflict, 1 special).
- This is data-integrity verification, not phonological adjudication. It adds no new IPA gold, no primary MLC evidence and no runtime rule. Status: implementation committed; CI pending.

## Rime crosswalk integrity and evidence triage — 2026-11-13

- Added `tests/test_rime_crosswalk_consistency.py` for the three existing 25-row tables. It checks exact MLCTS-key and source-unit alignment, two-value MLCTS2/R12A array alignment, enumerated evidence states and exact distribution counts.
- Verified required CI run **43507606882 SUCCESS** on code commit `de7abaea084515c5ef814575656ede8b83369a6a`: **248 Python + 66 subtests**, **20 Node**, **58 Playwright**, production build and generated-data freshness all passed. npm install still reports **one high-severity vulnerability**. Optional diagnostic workflow on the same commit completed successfully; raw model output is not an accuracy score.
- Triage from existing evidence: `any`/`any:`/`any.` are distinguished by both MLCTS2 and R12A; `any` has a secondary-source IPA conflict. `ui` is distinguished by MLCTS2 and only partially covered by R12A. `u.` is special/context-dependent, not an ordinary rime. `am` and `um` have secondary equivalence examples but no primary adjudication. The other groups remain unadjudicated.
- This is data-integrity and research prioritization only. No primary-source claim, IPA gold entry, phonological rule or Ukrainian output was promoted.

## MOW text-lookup candidates for `any` and `ui` — 2026-11-13

- Existing MOW generated data exposes 6 lemmas ending in ဉ် and 13 ending in ည် for `any`; 1 ending in ဉ်း and 6 in ည်း for `any:`; 0 ending in ဉ့် and 5 in ည့် for `any.`; and 0 ending in ို် versus 15 in ို for `ui`.
- Candidate strings include `ဥယျာဉ်`, `တိရစ္ဆာန်ဥယျာဉ်`, `ယာဉ်`, `ပြည်`, `မြန်မာပြည်`, `လက်ဖက်ရည်`, `အကျဉ်း`, `ချို`, `ငို`, `ဆို`, `တို`, and `မှို`.
- This turns the prior collision triage into concrete textual lookup keys. The evidence remains exact orthographic suffix matching only; no syllabification, pronunciation or homophony conclusion. No source/runtime status promoted.

## Source registry row-count correction — 2026-11-13

Append a correction note: `sources.csv` had three internal blank separator lines; earlier row counting included those as empty rows. Removed blank lines and added `test_source_registry_has_no_blank_rows_or_duplicate_source_ids`. Current validated registry: 80 unique nonblank sources / 133 claims.

## Source registry hygiene — 2026-11-13

- Removed three internal blank lines from `data/burmese/sources.csv`; added a regression test requiring every source row to have a nonblank unique `source_id`.
- Verified current registry: **80 unique nonblank source rows / 133 claims**. Required CI run **43508294905 SUCCESS** on code commit `62f59f177b15e2df54ace464056df7932058bffb`: 249 Python + 66 subtests, 20 Node, 58 Playwright, production build and generated-data freshness passed.
- Corrects the earlier 82/132 and 83/133 counts, which included blank separator rows. No source or linguistic claim was removed; only empty lines were deleted.

## Word-level Wiktionary examples for `any`, `any:` and `ui` — 2026-11-13

- Added three documentary claims under the existing Wiktionary snapshot and updated the lexical collision audit plus MLCTS2 crosswalk evidence-state labels.
- `any`: `ဥယျာဉ်` (`u.yyany`, `/ʔṵjɪ̀ɴ/` or `/ʔújɪ̀ɴ/`) vs `ပြည်` (`prany`, `/pjì/`).
- `any:`: `အကျဉ်း` (`a.kyany:`, `/ʔət͡ɕɪ́ɴ/`) vs `နည်း` (`nany:`, `/nɛ́/` or `/ní/`, sense-dependent).
- `ui`: `ချို`, `ဆို`, `တို` provide examples for `ို` only; no `ို်` MOW suffix match exists, so no comparison is possible.
- Required CI run **43509339740 SUCCESS** on code commit `191501979a2c5d8b7c0db9a00af5600b7266201f`: **251 Python + 66 subtests**, **20 Node**, **58 Playwright**, build and generated-data freshness passed. One high-severity npm vulnerability remains.
- Updated lexical-audit distribution: 19 unadjudicated / 2 secondary equivalence / 1 secondary conflict / 1 secondary distinction / 1 one-side-only / 1 special non-rime. The new evidence is secondary and lexical; it does not authorize runtime, IPA gold or Ukrainian promotion. Current registry: **80 sources / 136 claims**.

## Additional Wiktionary lexical attestation for `any.` — 2026-11-13

- Added word-level secondary entries for `စဉ့်` (MLCTS `cany.`, IPA `/sɪ̰ɴ/`) and `ကြည့်` (MLCTS `krany.`, IPA `/t͡ɕḭ/`), covering ဉ့် and ည့် endings respectively. Only `ကြည့်` is a MOW suffix candidate; `စဉ့်` was found independently in Wiktionary.
- Added `CLM-WIKTIONARY-ANY-DOT-WORD-LEVEL-EXAMPLES-001`; updated lexical audit, MLCTS2 status parity and regression tests.
- Distribution: 18 unadjudicated / 2 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 1 secondary one-side-only / 1 special non-rime. Registry: 80 sources / 137 claims.
- Status remains secondary lexical evidence only; no primary MLC adjudication, IPA gold, runtime or Ukrainian mapping promotion. Exact-head CI pending.

## Additional lexical examples for `aung` — 2026-11-13

- Wiktionary text entries list `ပေါင်` (`paung`, `/pàʊɴ/`) with ending ေါင် and `တောင်` (`taung`, `/tàʊɴ/`) with ending ောင်. Their onsets differ but the secondary IPA rime sequence `/àʊɴ/` matches. Only `တောင်` is a MOW suffix candidate.
- Added `CLM-WIKTIONARY-AUNG-WORD-LEVEL-EXAMPLES-001`; lexical audit and MLCTS2 crosswalk statuses synchronized; regression coverage expanded.
- Current distribution: 17 unadjudicated / 3 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 1 secondary one-side-only / 1 special non-rime. Registry: 80 sources / 138 claims.
- Secondary evidence only; not a controlled minimal pair or primary MLC adjudication. No IPA gold, runtime or Ukrainian output promotion. CI pending.

## Exact-head verification — secondary lexical collision audit — 2026-11-13

- Verified code/data snapshot `eb81bd29e9417ddbd6d541d54fce6d754b0bb8bd`; required CI **43513203135 SUCCESS** (duplicate **43513212043 SUCCESS**): 251 Python + 66 subtests, 20 Node, 58 Playwright; build, generated-data freshness and Chromium install passed.
- Optional Epitran raw-output diagnostic **43513212088 SUCCESS**, not an accuracy score. IPA-gold validator remains `NOT_READY_NO_ADJUDICATED_GOLD`; independent gold count 0. npm install reports one high-severity vulnerability.
- Registry 80 sources / 138 claims. Collision evidence distribution: 17 unadjudicated / 3 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 1 secondary one-side-only / 1 special non-rime.
- This verifies code/data/test consistency only. Secondary Wiktionary examples do not adjudicate primary MLC policy and do not enable runtime or Ukrainian mapping changes.

## Additional lexical evidence for `aung:` — 2026-11-13

- Added MOW-listed `ပေါင်း` (`paung:`, `/páʊɴ/`) and `ကျောင်း` (`kyaung:`, `/t͡ɕáʊɴ/`) as Wiktionary word-level examples for ေါင်း and ောင်း. The onsets differ but the secondary IPA rime sequence `/áʊɴ/` matches.
- Added claim `CLM-WIKTIONARY-AUNG-COLON-WORD-LEVEL-EXAMPLES-001`; updated lexical audit, MLCTS2 status parity and regression tests.
- Current distribution: 16 unadjudicated / 4 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 1 secondary one-side-only / 1 special non-rime. Registry: 80 sources / 139 claims.
- This is secondary lexical evidence, not a minimal pair or primary MLC adjudication. No IPA gold, runtime or Ukrainian output promotion. CI pending.

## Additional lexical evidence for `auk` — 2026-11-13

- Added MOW-listed `ပေါက်` (`pauk`, `/paʊʔ/`) and `ကျောက်` (`kyauk`, `/t͡ɕaʊʔ/`) as Wiktionary word-level examples for ေါက် and ောက်. Their onsets differ but the secondary IPA rime sequence `/aʊʔ/` matches.
- Added claim `CLM-WIKTIONARY-AUK-WORD-LEVEL-EXAMPLES-001`; updated lexical audit, MLCTS2 status parity and regression tests.
- Current distribution: 15 unadjudicated / 5 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 1 secondary one-side-only / 1 special non-rime. Registry: 80 sources / 140 claims.
- This is secondary lexical evidence, not a minimal pair or primary MLC adjudication. No IPA gold, runtime or Ukrainian output promotion. CI pending.

## Additional lexical evidence for `a`, `a:` and `au` — 2026-11-13

- Added MOW-listed Wiktionary word pairs: `အဝါ` (`a.wa`, `/ʔəwà/`) / `အစာ` (`a.ca`, `/ʔəsà/`) for `a`; `ခါး` (`hka:`, `/kʰá/`) / `ကား` (`ka:`, `/ká/`) for `a:`; `ပေါ်` (`pau`, `/pɔ̀/`) / `ကြော်` (`krau`, `/t͡ɕɔ̀/`) for `au`. Same secondary IPA rime within each pair, different onsets.
- Added three source claims and updated lexical audit, MLCTS2 parity and regression tests. MOW coverage data unchanged.
- Current distribution: 12 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 1 secondary one-side-only / 1 special non-rime. Registry: 80 sources / 143 claims.
- Secondary evidence only; not minimal pairs or primary MLC adjudication. No IPA gold, runtime or Ukrainian output promotion. CI pending.

## One-sided lexical evidence for `aung.` — 2026-11-13

- Added MOW-listed Wiktionary lemma `စောင့်` (`caung.`, `/sa̰ʊɴ/`) for ောင့်. No example for ေါင့် was located. Added claim `CLM-WIKTIONARY-AUNG-DOT-ONE-SIDE-EXAMPLE-001`; synchronized lexical audit and MLCTS2 status, and expanded tests.
- Current distribution: 11 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 2 secondary one-side-only / 1 special non-rime. Registry: 80 sources / 144 claims.
- This is secondary evidence for one side only, not a collision adjudication or primary MLC specification. No IPA gold, runtime or Ukrainian output promotion. CI pending.

## One-sided lexical examples for `um:` and `un` — 2026-11-13

- Added MOW-listed Wiktionary lemma `နှလုံး` (`hna.lum:`, `/n̥əlóʊɴ/`) for `ုံး` and `ကုန်` (`kun`, `/kòʊɴ/`) for `ုန်`; the opposite sides remain unobserved. Added two documentary claims and updated lexical audit, MLCTS2 parity and regression tests.
- Current distribution: 9 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 4 secondary one-side-only / 1 special non-rime. Registry: 80 sources / 146 claims.
- Secondary one-sided evidence only; not collision adjudication or primary MLC specification. No IPA gold, runtime or Ukrainian output promotion. CI pending.
