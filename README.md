# Burmese → Ukrainian Phonetic-Graphemic Correspondence System

Research-grade Burmese (Myanmar script) → Ukrainian correspondence system with an evidence-gated practical transcription layer.

## Scientific pipeline

Burmese Unicode → normalization → graphemic/syllable structure → onset/conjunct/kinzi/medials/vowel/inherent-vowel analysis → prosodic analysis → Burmese phonology → surface phonetics → IPA → feature space → Ukrainian target → Ukrainian practical orthography.

The practical output is never produced by direct Myanmar-character substitution.

## Scope

The default scope is contemporary Standard Burmese. Yangon-oriented claims are used only where the cited source supports that scope. Myanmar script is not treated as synonymous with Burmese.

## Cyrillic comparative layer

The project now explicitly reproduces the comparative methodology used in the Thai project:

Burmese phonology/IPA → Russian practical control → Ukrainian target-language policy → Ukrainian practical output

A dedicated Russian practical tradition is documented. The principal historical source located is V. G. Epstein, Rules of Russian Transcription of Burmese Geographical Names (1959). A further institutional instruction from 1978 is also documented, demonstrating continuity of the Russian geographical-name tradition. The repository records this tradition as a control/predecessor layer, not as the source of truth for Ukrainian.

The comparison shows several systematic target-language differences:

| Burmese | Russian practical | Ukrainian project baseline |
|---|---|---|
| /kʰ/ | кх | к |
| /tʰ/ | тх | т |
| /pʰ/ | пх | п |
| /sʰ/ | сх | с |
| /i/ | и | і |
| /ɛ/ | э | е |
| /ɯ/ | ы/у | и* |
| /ŋ/ | нг | нг |
| /w/ | у | в |
| /h/ | х | г* |
| /r/ | й/r-dependent | р |
| tone | not encoded | not encoded |

The starred choices are project hypotheses/target-language decisions and are not presented as official Ukrainian norms.

## Serbian and Bulgarian comparators

A dedicated Burmese-specific Serbian or Bulgarian practical transcription system of comparable codified status was NOT_ESTABLISHED in the present review.

Serbian scholarship is nevertheless retained as a methodological comparator for target-language adaptation: pronunciation, established usage, natural target-language clusters, simplicity and consistency matter, and another language's transcription should not be imported blindly.

Bulgarian remains NOT_ESTABLISHED until a primary Burmese-specific source is located.

## Current implementation

Implemented:
- NFC/NFD normalization entry point.
- Conservative Myanmar grapheme/syllable segmentation.
- Explicit kinzi detection.
- Virama/subjoined-consonant parsing.
- Four-medial parsing.
- Dependent-vowel parsing.
- Explicit inherent-vowel state.
- Explicit malformed/unsupported states.
- Evidence and competing-analysis datasets.
- Structural syllable generator.
- Prosody analysis slots that do not invent tone values.
- Conservative IPA seed layer.
- Canonical Ukrainian target adapter boundary.
- Burmese→Russian documentary correspondence registry.
- Burmese→Ukrainian practical correspondence registry.
- Machine-readable practical rule registry and provenance claims.
- Executable Ukrainian practical target layer.
- Comparative Russian-vs-Ukrainian documentation.
- Serbian/Bulgarian comparator audit.
- Practical-layer regression tests.
- JSON Schemas, benchmark seeds, adversarial-test specification and CI.

Not yet established as complete:
- full Burmese vowel-combination derivation;
- complete coda and checked-syllable realization;
- complete tone/register/phonation realization;
- full allophony and phonological-rule engine;
- corpus-backed lexical validation;
- final feature-distance ranking against the canonical Ukrainian-Phonetic-Inventory schema;
- empirical adjudication of project-specific choices such as /h/ → г and /ɯ/ → и.

## Evidence policy

Unicode is authoritative for encoding and script mechanics, not automatic authority for every phonological analysis.

The prosodic layer retains competing analyses. Traditional descriptions and newer double-register/eight-tone proposals are not averaged into a false consensus.

Russian practical transcription is documentary evidence for Russian practice. It is not evidence that the Russian target is optimal for Ukrainian.

## Sources

- Unicode Standard, Chapter 16, Myanmar.
- Unicode Technical Note #11, Representing Myanmar in Unicode.
- Green (2002), Word, Foot, and Syllable Structure in Burmese.
- Mooney & Repetti-Ludlow (2021), Sonority and syllable structure: The case of Burmese tone.
- Duan & Zhu (2025), Double registers and eight tones in Burmese.
- Tun et al. (2011), Myanmar text-to-speech system with rule-based tone synthesis.
- V. G. Epstein (1958), К вопросу о транскрибировании бирманских собственных имен.
- V. G. Epstein (1959), Rules of Russian Transcription of Burmese Geographical Names.
- K. T. Boyko & A. V. Samarkin (1978), Instruction for Russian transmission of geographical names of Burma.
- Ukrainian Orthography 2019, practical-transcription provisions for geographical names.

## Research artifacts

- data/burmese/cyrillic_systems.csv
- data/burmese/russian_practical_transcription.csv
- data/burmese/ukrainian_practical.csv
- data/burmese/practical_rules.csv
- data/burmese/source_claims.csv
- docs/practical-transcription.md
- docs/russian-vs-ukrainian.md
- docs/serbian-bulgarian-comparison.md
- src/burmese_ukrainian/practical.py
- tests/test_practical.py

## Status labels

ESTABLISHED · WELL_SUPPORTED · ANALYSIS_DEPENDENT · DIALECT_DEPENDENT · CONTEXT_DEPENDENT · UNCERTAIN · DISPUTED · NOT_ESTABLISHED · UNSUPPORTED

The implementation intentionally returns uncertainty instead of silently inventing a linguistic analysis.

## Core principle

The Russian system is a documented predecessor/control layer.

The Ukrainian system is defensible only when every divergence from Russian can be explained through:

1. Burmese phonology;
2. Burmese orthography;
3. Ukrainian phonology;
4. Ukrainian orthography;
5. evidence strength.
