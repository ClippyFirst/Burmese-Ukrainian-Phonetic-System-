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
