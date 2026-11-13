# Burmese phonology coverage audit

Review date: 2026-10-20  
Repository: https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-

## Scope and interpretation

This is an implementation audit, not a claim that all standard Burmese pronunciations have been surveyed. "Implemented and tested" means an executable behavior has regression coverage; it does not mean the linguistic claim is empirically validated. A source listed in the bibliography does not, by itself, establish that code implements its findings.

Statuses:
- **Implemented and tested** — an executable behavior has regression coverage.
- **Partially implemented** — a limited representation or subset exists and has some tests.
- **Documented only** — the issue or analysis is described, but no complete implementation is verified.
- **Absent / not established** — no adequate implementation or independent evidence-backed evaluation is currently verified.

## Layer-by-layer inventory

| Layer | Status | What is present | What is still missing |
|---|---|---|---|
| Unicode normalization | Partially implemented | Python normalization exposes NFC/NFD/NFKC/NFKD; browser normalizer uses NFC. | Equivalence tests across canonical spellings, full normalization contract across runtimes, and policy on compatibility normalization. |
| Myanmar block recognition | Implemented and tested (bounded contract) | Python and browser recognize Myanmar, Extended-A/B and U+116D0–U+116FF ranges; shared JSON fixture tests unsupported script characters. | Range recognition is not proof that every code point is Burmese or supported by the parser. |
| Grapheme/syllable segmentation | Partially implemented | Conservative segmentation and structural parser; browser has a separate parser. | Independent annotated boundary corpus; differential Python/browser tests for punctuation, mixed scripts, combining marks and ambiguous boundaries. |
| Main consonants | Partially implemented | Graphemic inventory and a small onset IPA table. | Complete phoneme inventory, lexical/phonological conditions, contrast validation and coverage accounting. |
| Kinzi | Partially implemented | Explicit sequence recognition in parser and browser. | Source-backed cases for onset/medial/coda contexts; consistent phonological interpretation across runtimes. |
| Medials and complex onsets | Partially implemented | Four medial signs and structural combination handling; browser derives some contextual IPA. | Complete combination inventory, source-anchored IPA, competing analyses and a cross-runtime gold set. |
| Dependent and inherent vowels | Partially implemented | Vowel signs are parsed; inherent-vowel state exists; Python maps only a small set of vowel IDs. | Full vowel combinations, context rules, length/quality contrasts and independent word-level validation. |
| Finals/codas and checked syllables | Partially implemented | Parser records some coda structures; browser has contextual coda/rime rules. | Complete coda inventory, checked-syllable realization and validated lexical examples. |
| Tone | Documented only / not established in runtime | Analysis registries retain traditional four-way and eight-tone/register analyses. | Source-backed tone-labelled examples, F0/phonation/duration interpretation, dialect/scope metadata and calibrated output. |
| Phonation/register | Documented only | The literature registry includes competing register/phonation accounts. | No complete evidence-gated implementation or benchmark verified. |
| Allophony and phonological rules | Partially implemented in browser; not established as a complete model | Hand-written contextual cases exist. | Rule-by-rule source mapping, environments, counterexamples and cross-runtime tests. |
| IPA | Partially implemented | Python IPA uses a small onset/vowel seed map and marks output conservative_partial or analysis_dependent; browser has a separate, richer handwritten derivation. | No validated comprehensive IPA layer; no independent gold set; no guarantee the two runtimes agree. |
| IPA → Ukrainian | Partially implemented | Table-driven candidate registry and explicit not_established fallback; Russian rules are kept as a comparison layer. | Independent validation of every correspondence, contextual Ukrainian spelling policy and name-level benchmark. |
| Unknown/ambiguous inputs | Partially implemented | Parser and practical layer have uncertainty/unsupported outcomes. | One cross-runtime status contract, no-confident-output guarantee, and adversarial tests for every API path. |
| Citation and licensing metadata | Citation metadata added in this audit; project license unresolved | CITATION.cff declares the work as a research prototype and license NOASSERTION. | A maintainer must choose and document a project license after separating code, corpus and third-party data rights. No license is inferred from public visibility. |

## Evidence-gated output contract

Use statuses at the layer where uncertainty originates. Do not collapse them into one success flag.

- SUPPORTED: the specific analysis is covered by a source-backed rule and an applicable regression/gold test.
- UNCERTAIN: more than one plausible analysis remains, source scope does not settle the case, or the runtime has only a hypothesis.
- UNSUPPORTED: the input or construction is outside the implemented inventory.
- NOT_ESTABLISHED: the system has no defensible output mapping.

A successful Unicode parse must not imply supported phonology. Supported IPA must not automatically imply a single Ukrainian spelling. A placeholder such as ? is diagnostic output, not a transcription.

## Current independent-corpus measurement

The repository has literature/source registries and structural regression fixtures, but this review did not verify a complete independently adjudicated lexical IPA corpus. Therefore:
- phonological gold-corpus size: **0 verified entries** in this audit;
- validated word-level IPA accuracy: **not measured**;
- Ukrainian name-level accuracy: **not measured**;
- browser/Python phonological agreement: **not measured**.

These are unknown measurements, not 0% accuracy. The shared Unicode JSON fixture is explicitly a structural/status contract and must not be counted as phonological gold data.

## Next acceptance gates

1. Add source-located examples with the exact source page/table/entry and a documented IPA convention.
2. Require a second source or independent reviewer for disputed lexical/tonal analyses where possible.
3. Separate phonemic/broad IPA from surface phonetic detail.
4. Compare Python, browser and external engines only on the same adjudicated examples.
5. Report coverage as supported examples / eligible examples, with unresolved and unsupported cases shown separately.
6. Keep tone, phonation and dialect claims analysis-dependent until the evidence supports a narrower conclusion.

## Sources

See docs/references.md, data/burmese/sources.csv, data/burmese/source_claims.csv, and data/burmese/tone_analyses.csv.


## Evidence update — 2026-11-13

- **Segmentation:** Python now recognizes a base consonant + U+103A ASAT as a final/coda in the preceding syllable, matching the browser parser. Tests cover မြန် (one syllable), မြန်မာ (two) and ကတ်. Overall segmentation remains partial because there is no independent annotated boundary corpus.
- **Medials:** the orthographic inventory is now source-verified as four basic signs plus seven combinations. Phonetic behavior remains partial/context-dependent; the existence of a combination is not an IPA rule.
- **Coda:** Green's placeless /N/ analysis requires nasalization/approximate place realization, not an unconditional independent [ɴ]. The Ukrainian /ɴ/ target rule remains conditional on the selected IPA representation.
- **External models:** Google Thrax /m j àɴ/ and Epitran /məjaɴ/ disagree on မြန်; both have zero gold. CRF source concordance is not empirical accuracy.
- **Tone:** four-tone and eight-tone/register analyses remain separate. No tone rule is enabled.
- **Release boundary:** independent adjudicated IPA gold remains zero; word-level accuracy remains unmeasured.


### Typed IPA metadata gap — 2026-11-13

The IPA gold schema can preserve nasalization in its literal IPA value, but has no separate typed nasalization property. This is not a current transcription blocker if the literal string is preserved; it is a downstream-query limitation. Defer schema expansion until the phonemic /N/ vs surface nasalization convention is expert-approved.


## Text-only historical and contextual evidence update — 2026-11-13

- **Historical medial structure:** STEDT (1996), Nishi (1997) and Matisoff (2003) show that Written Burmese periodization, proto-medial reconstruction and modern spoken correspondences must remain separate. Historical WB *-r- > Modern Burmese -y- is documented, but no direct mapping to current Unicode U+103B/U+103C is established.
- **Written/spoken distinction:** Nishi (1997) explicitly distinguishes written H and spoken L systems and their non-coterminous periods. A written romanization or historical spelling cannot alone establish modern Yangon IPA.
- **Contextual voicing:** Nishi (1998) describes two Standard Burmese voicing-sandhi patterns, but documents optionality, exceptions and regional differences. Both remain analysis-dependent; no global runtime rule is enabled.
- **Text corpora:** Myanglish and orthographic correction datasets may support romanization diagnostics or spelling-normalization research after schema and row review; neither supplies IPA gold. Okell text corpus is authorized for research by the project owner; its bytes remain inaccessible in this execution environment.
- **Measurement:** independent expert-adjudicated text-based IPA gold remains **0**; word-level accuracy remains **null/unmeasured**. No audio is part of the active scope or acceptance criteria.


### Nishi full-text evidence and text-corpus status — 2026-11-13

- Nishi (1998), *Old Burmese: Toward the History of Burmese*, is now inspected in full. It distinguishes historical -h as a voiceless/aspirated sonorant marker from actual -r/-l/-y/-w medial clusters; documents OWB -l- and later conditioned reflexes; places the MB -r-/-y- merger in Standard EModWB; and compares cluster reflexes across WB, SB, Arakanese, Tavoyan, Intha and Minor Taungyo.
- These are historical written/phonological correspondences, not direct modern Unicode mappings. Four historical rules and thirteen new matrix rows are source-linked and tested; every such row remains WITHHELD.
- Nishi (1998) voicing paper contributes seven source-phonemic sandhi examples. They follow Okell 1995's source transcription convention and are explicitly NOT project IPA; IPA field is empty.
- Text-use permissions for external resources are confirmed by the project owner. Okell and SEAlang remain blocked only by actual byte/entry retrieval and schema access, not by permission.
- Myanglish raw CSV vs dataset metadata has an unresolved 2-column/3-feature discrepancy. The myX orthography corpus has sampled target_words misalignment and multi-substitution examples; quarantine pending full row audit and deduplication.
- Exact-head CI 43393402710: 217 Python tests + 66 subtests, 20 Node tests and 58 browser tests passed; build, generated-data freshness and IPA schema validation passed. Gold remains 0 and accuracy null.

### Final verified state — 2026-11-13

Exact head c03706474cf67b480c449790c9592e5fe0e53fd4 passed CI run 43394274053: 217 Python tests + 66 subtests, 20 Node tests, 58 browser tests, IPA-gold schema validation, build and generated-data freshness. Diagnostic run 43394274111 also passed, but it has no gold and no accuracy result.

The registries contain 56 sources, 71 claims, 42 medial rows, 28 phonological rules and 7 source-phonemic sandhi examples. Nishi (1998) historical and dialect evidence is now more fully represented; all such rows remain WITHHELD. Nishi (1976) is a registered but unread primary-source target.

Text research permissions are confirmed by the project owner; remaining external-source blockers are retrieval/schema and dataset quality, not permission. No audio was used. IPA gold=0, empirical accuracy=null, no runtime rules promoted.


### Okell (1995) regional medial profiles — 2026-11-13

Full text of *Three Burmese Dialects* inspected. It explicitly separates Written Burmese from Standard spoken Burmese and documents distinct Arakanese, Intha and Tavoyan profiles:
- Arakanese preserves WB r/y, which SB merges in speech; the registered AR profile is specifically high-prestige Sit-twe, not all Arakanese varieties.
- Intha and Tavoyan have restricted medial /l/ combinations; Tavoyan /-l/ is explicitly absent from SB.
- The book's transcribed texts are phonemic with limited allophonic approximations, not project IPA gold.
Added source OKELL1995_THREE_DIALECTS, seven claims, two dialect-dependent rules and three withheld medial rows. No audio was accessed. No regional rule was enabled for Yangon.
