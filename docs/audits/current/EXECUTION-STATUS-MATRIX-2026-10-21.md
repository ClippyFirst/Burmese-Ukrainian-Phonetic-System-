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
| Unicode normalization | Python NFC/NFD/NFKC/NFKD entry points; browser NFC entry point | Partial; shared normalization equivalence and compatibility-policy tests not established | Not applicable to pronunciation | PARTIAL | Specify supported normalization contract and test canonical equivalence and compatibility characters in both runtimes |
| Myanmar block recognition | Bounded Myanmar/Extended block recognition | Structural fixture tests reported by audit | Not phonological evidence | DONE_VERIFIED (bounded contract only) | Keep block recognition distinct from parser/phonology support |
| Grapheme and syllable segmentation | Conservative Python parser and separate browser parser | Existing structural tests; annotated differential corpus absent | 0 lexical gold entries established | PARTIAL | Add boundary-annotated corpus covering punctuation, mixed scripts, combining marks, malformed sequences; compare runtimes |
| Consonant/onset inventory | Small Python onset IPA table and graphemic inventory | Existing parser/IPA regression coverage is limited | No independently adjudicated inventory-wide lexical set | PARTIAL | Source-map each onset and test legal/unsupported contexts |
| Kinzi | Explicit structural recognition and role metadata | Structural regression coverage exists; contextual phonological tests incomplete | None established | PARTIAL | Source-located onset/medial/coda-context cases and cross-runtime assertions |
| Medials / complex onsets | Four medial signs parsed; some browser contextual derivation | Partial; full combination gold set absent | None established | PARTIAL | Inventory combinations, competing analyses, environments, counterexamples and paired Python/browser tests |
| Dependent/inherent vowels | Vowel signs parsed; small vowel-ID-to-IPA map | Structural tests exist; derivation coverage incomplete | None established | PARTIAL | Evidence-backed combination table and context/length/quality tests; no extrapolation from unverified patterns |
| Codas / checked syllables | Some final structures parsed; browser rime rules reported | Incomplete | None established | PARTIAL | Enumerate coda/rime classes, mark checked-syllable conditions, test each sourced class |
| Tone | Analysis registries document competing traditional and eight-tone/register analyses; no established runtime realization | Not adequately tested as a phonological layer | 0 tone-labelled gold entries established | TODO | Add scoped, source-located tone examples and separate phonemic category from surface F0 realization |
| Register / phonation | Competing literature descriptions documented | No complete runtime model verified | 0 independently adjudicated register/phonation entries | TODO | Model alternatives explicitly with dialect/scope and phonetic evidence; avoid consensus claims where sources disagree |
| Contextual rules / allophony | Partial browser hand-written cases | Rule-complete regression suite absent | None established | PARTIAL | Rule registry with source, environment, output, counterexamples and Python/browser parity tests |
| IPA result/status contract | Python emits conservative partial strings or analysis-dependent status; browser has separate derivation | No full cross-runtime contract verified | No lexical IPA gold entries | PARTIAL | Every result exposes phonological status independently of parse status; partial IPA must never be labelled complete |
| IPA → Ukrainian target adapter | Canonical external inventory boundary and candidate registry; explicit unavailable/not-established paths | Practical regression tests exist | No Ukrainian name-level gold evaluation | PARTIAL | Validate adapter against canonical inventory schema and all correspondence policies; test unavailable dependency behavior |
| Feature-distance ranking | Candidate ranking implementation exists | Limited regression tests; final schema/feature validation not established | No empirical target-ranking validation | PARTIAL | Validate feature definitions and weights against canonical inventory; test deterministic ranking, ties, unknown features and missing inventory |
| Comparative Russian/Ukrainian policies | Comparative registries and documentary layer present | Practical tests cover selected correspondences | No independent name-level benchmark | PARTIAL | Check every rule provenance, target-language rationale, uncertainty and non-inheritance from Russian |
| Malformed/unsupported input | Structural and practical uncertainty outcomes exist | Some malformed virama and unknown-target tests | Not a lexical accuracy measure | PARTIAL | Adversarial tests for all API/CLI/browser entry points; no confident output after malformed or incomplete parse |
| JSON schemas / data validation / generated artifacts | Schemas and registries exist per audit/README | Full current validation run not performed in this remote editing session | Not applicable | PARTIAL | Run every validator/generator, schema validation and generated-drift check in a checkout |
| Python/browser parity | Separate implementations exist | Phonological differential coverage not established | None established | TODO | Shared fixtures and parity tests for structural state, uncertainty, IPA, and unsupported cases |
| Lexical IPA gold corpus | Six rows in data/burmese/phonology_corpus.csv are explicitly STRUCTURAL_ONLY | Benchmark gating prevents scoring them as gold | 0 verified gold entries; accuracy not measured | BLOCKED by source-located/adjudicated entries | Add independently sourced broad-IPA entries with exact source locators, transcription convention and review; keep structural probes separate |
| Epitran comparator | Optional scripts/benchmark_g2p.py; static Epitran v1.35.0 map/pre/post review documented | Runner not executed in an Epitran-installed environment per audit | No accuracy can be calculated with zero gold entries | BLOCKED by comparator environment and gold corpus | Run pinned comparator; record version, map/pre/post hashes, raw output, configuration and disagreement categories |
| myG2P data | License risks documented; dictionary not bundled | Licensing review is documentary | Not applicable | DONE_VERIFIED (non-bundling guardrail) | Do not import dictionary material absent separate permission and rights review |
| Project license | No root LICENSE; CITATION.cff uses NOASSERTION | Presence/absence documented | Not applicable | BLOCKED — owner decision | Owner selects code license and separately resolves corpus/data/model rights; do not infer from public visibility |
| CI / release readiness | CI configuration exists | CI status not re-run from this remote editing session | No end-to-end phonological validation | PARTIAL | Run clean install, pytest, browser tests, schemas, generators, parity and benchmark gates in a local checkout |

## Gold-corpus rules
1. Keep the six existing seed cases labelled STRUCTURAL_ONLY; they are not phonological gold.
2. A scoreable row must have GOLD_VERIFIED, non-empty expected broad IPA, a registered source ID, and a precise non-pending source locator.
3. Store IPA convention, scope/dialect, analysis level (phonemic vs surface phonetic), reviewer and uncertainty/alternative analysis.
4. Never fill expected IPA from the system under test, Epitran, or myG2P and then use that same output as independent truth.
5. Report exact-match and feature/category metrics only over the eligible gold set; show unresolved and unsupported cases separately.

## Reproducibility and license gates
- Epitran is a pinned comparator only. Do not promote it to the primary engine based on agreement with its own mapping or unverified outputs.
- Preserve raw Epitran output and separately hash installed package metadata, map, preprocessor and postprocessor where available.
- Keep third-party code, maps, dictionary, model weights, source text and generated artifacts as separate rights-bearing categories.
- No root license should be added until the owner decides. A public repository is not a license grant.

## Execution evidence and limitations
This register was prepared from the current README, both named audits, the seed corpus, src/burmese_ukrainian/ipa.py, src/burmese_ukrainian/parser.py, tests/test_parser.py, tests/test_practical.py, and scripts/benchmark_g2p.py. Remote inspection confirmed branches main, final-hardening, fix/adversarial-burmese-phonology, and service-ready; no open PRs were returned by the repository-scoped query. These branches were not modified or merged.

Automated CI run 39561213616 (commit c4f5d03d6c0de1c47c385f12cd4feb208219cb47): editable package install PASS; pytest PASS; npm install PASS; npm run build PASS; npm test PASS. Playwright browser installation PASS and npm run test:browser PASS (same CI run 39561213616). Dedicated schema/generator/drift validation and the Epitran benchmark were not evidenced by this workflow. The project remains a partial research prototype, not release-ready. Epitran benchmarking and independent gold validation remain blocked; project licensing remains an owner decision.