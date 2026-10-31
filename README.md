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
| /kʰ/ | кх | к' |
| /tʰ/ | тх | т' |
| /pʰ/ | пх | п' |
| /sʰ/ | сх | с' |
| /i/ | и | і |
| /ɛ/ | э | е |
| /ɯ/ | ы/у | и* |
| /ŋ/ | нг | нг |
| /w/ | у | в |
| /h/ | х | г |
| /ɡ/ | г | ґ |
| /x/ | х | х |
| /r/ | й/r-dependent | р |
| tone | not encoded | not encoded |

Aspiration is preserved with an apostrophe in the Ukrainian practical layer; /ʔ/ does not trigger it. The distinctions /h/ → г, /ɡ/ → ґ and /x/ → х are project-wide target conventions, not claims that foreign /h/ is identical to Ukrainian /ɦ/.

The shared target conventions are documented in the canonical [foreign IPA → Ukrainian adaptation policy](https://github.com/ClippyFirst/Ukrainian-Phonetic-Inventory/blob/main/docs/foreign-target-adaptation.md). This repository's executable Burmese correspondences and regression tests implement the aspiration apostrophe, /h/ → г, /ɡ/ → ґ and /x/ → х distinctions without changing Burmese IPA.

## Serbian and Bulgarian comparators

A dedicated Burmese-specific Serbian or Bulgarian practical transcription system of comparable codified status was NOT_ESTABLISHED in the present review.

Serbian scholarship is nevertheless retained as a methodological comparator for target-language adaptation: pronunciation, established usage, natural target-language clusters, simplicity and consistency matter, and another language's transcription should not be imported blindly.

Bulgarian remains NOT_ESTABLISHED until a primary Burmese-specific source is located.

## Usage

Install the package with test-only dependencies and run the test suite:

```bash
pip install -e ".[test]"
pytest
```

The test extra includes `pytest` and `jsonschema`; schema validation is test-only and is not a runtime dependency. CI also checks that regenerating web data leaves `src/web/generated/data.js` unchanged:

```bash
npm run generate:web
git diff --exit-code -- src/web/generated/data.js
```

Structural Burmese parsing is available directly through the Python package.
The Ukrainian target adapter intentionally requires a local checkout of the
canonical ClippyFirst/Ukrainian-Phonetic-Inventory repository; the Burmese
repository does not vendor or duplicate that inventory.

Without the external inventory, the adapter returns
`inventory_unavailable` rather than falling back to a hidden Ukrainian map.

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
- V. G. Epstein (1958), bibliographic lead on Burmese proper-name transcription (article-level verification remains uncertain).
- V. G. Epstein (1959), Rules of Russian Transcription of Burmese Geographical Names.
- K. T. Boyko & A. V. Samarkin (1978), Instruction for Russian transmission of geographical names of Burma.
- Ukrainian Orthography 2026, practical-transcription provisions for geographical names.

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

ESTABLISHED · WELL_SUPPORTED · PROPOSED · ANALYSIS_DEPENDENT · DIALECT_DEPENDENT · CONTEXT_DEPENDENT · UNCERTAIN · DISPUTED · NOT_ESTABLISHED · UNSUPPORTED

The implementation intentionally returns uncertainty instead of silently inventing a linguistic analysis.

## Core principle

The Russian system is a documented predecessor/control layer.

The Ukrainian system is defensible only when every divergence from Russian can be explained through:

1. Burmese phonology;
2. Burmese orthography;
3. Ukrainian phonology;
4. Ukrainian orthography;
5. evidence strength.


## Current evidence and license audits

- [Phonology coverage audit](docs/audits/current/PHONOLOGY-COVERAGE-AUDIT-2026-10-20.md): implementation status by layer and current coverage limits.
- [External G2P and licensing audit](docs/audits/current/G2P-ENGINE-AND-LICENSING-AUDIT-2026-10-20.md): Epitran and myG2P roles, restrictions and benchmark gates.
- [Third-party notices](THIRD_PARTY_NOTICES.md): code/data/model licensing review.
- [Seed corpus](data/burmese/phonology_corpus.csv): structural probes explicitly marked as not phonological gold data.
- [Citation metadata](CITATION.cff).

**Current measurement:** no independently adjudicated lexical IPA gold entries are verified yet. Word-level IPA accuracy and Ukrainian name-level accuracy are therefore not measured. The six rows in the seed corpus are structural probes only; blank IPA and Ukrainian fields are intentional, not missing results to be inferred.

The repository currently has no root project license. Do not assume the source code or data are licensed for reuse merely because the repository is public. CITATION.cff uses NOASSERTION until the owner chooses a license.

### Optional Epitran baseline

`scripts/benchmark_g2p.py` can capture raw output from an independently installed Epitran `mya-Mymr` transducer without making Epitran a runtime dependency:

```bash
python scripts/benchmark_g2p.py --engine epitran --output epitran-benchmark.json
```

Run it in an environment where Epitran is installed separately. The report records engine/version and hashes where available. It does not score structural probes as phonological gold data; accuracy remains `null` until rows are independently source-located and marked `GOLD_VERIFIED`. See the [G2P and licensing audit](docs/audits/current/G2P-ENGINE-AND-LICENSING-AUDIT-2026-10-20.md) before redistributing third-party data.



## External IPA renderers and G2P candidates

The research registry records external pronunciation engines, IPA dictionaries, and Unicode IPA display fonts without treating unvalidated output as ground truth. See [`docs/external-ipa-renderers.md`](docs/external-ipa-renderers.md) and the machine-readable [`data/external-ipa-renderers.json`](data/external-ipa-renderers.json). These are candidate inventories only; no third-party engine is enabled by default, and the ClippyFirst IPA → Ukrainian adapter remains the sole target adaptation boundary.


## Two output methods

The service separates the orthographic MLCTS romanization route from the IPA-first phonetic route. The romanization tab currently exposes a PARTIAL Ukrainian crosswalk and never falls back to phonetic output. See the [romanization → Ukrainian research matrix](docs/romanization-to-ukrainian-matrix.md) for the selected profile, source comparison and onset table.


## Production build and GitHub Pages

The production build includes both the service and methodology pages and copies the Mya2Rom browser assets into the Vite artifact. Playwright runs against the built preview, not only the development server.


## Live service

GitHub Pages: https://clippyfirst.github.io/Burmese-Ukrainian-Phonetic-System-/

The production build contains both the service and methodology pages and the Mya2Rom assets. Playwright runs against the built Vite preview. The romanization tab is separate from the IPA-first phonetic tab; its Ukrainian crosswalk is still marked PARTIAL.
