# External IPA renderers and G2P candidates — Burmese (Myanmar script)

**Status: research registry only.** This document records candidate tools discovered during the ClippyFirst IPA-renderer survey. It does not claim that these tools are integrated, accurate, licensed for redistribution, or accepted as pronunciation gold data.

## Required integration boundary

`source orthography → source-language structure and phonology → typed IPA result → ClippyFirst IPA → Ukrainian adapter → Ukrainian practical orthography`

External systems must be treated as upstream phonetic-result providers or benchmark comparators. They must **not** bypass this repository's IPA-to-Ukrainian adapter or introduce direct source-script-to-Ukrainian fallback. Keep source output, normalized IPA, provenance, dialect/profile, syllable boundaries, tone, length, uncertainty, and competing analyses inspectable.

## Language-specific candidates

### 1. [mya2rom](https://github.com/myanmaropenwordnet/mya2rom)

- **Role:** Myanmar script to romanization/IPA
- **Status:** candidate
- **Output/validation:** Early-stage; Wikipedia-flavor IPA with known convention differences (including nasalization notation); compare before acceptance
- **License:** Verify repository license and attribution of imported sources
- **Repository integration:** not yet enabled; upstream behavior and license must be checked before dependency, data, or code reuse.

### 2. [myG2P](https://github.com/ye-kyaw-thu/myG2P)

- **Role:** dictionary / G2P research resource
- **Status:** candidate
- **Output/validation:** Inspect structured pronunciation/IPA fields, lexicon version, coverage and provenance
- **License:** Verify exact version and dictionary license
- **Repository integration:** not yet enabled; upstream behavior and license must be checked before dependency, data, or code reuse.

### 3. [burmese-G2P](https://github.com/kyaw-yethu/burmese-G2P)

- **Role:** CRFSuite G2P
- **Status:** candidate
- **Output/validation:** Versioned output conventions differ; validate IPA and service-particle errors
- **License:** CC BY-NC-SA 4.0 reported upstream; non-commercial restriction blocks commercial reuse unless separately resolved
- **Repository integration:** not yet enabled; upstream behavior and license must be checked before dependency, data, or code reuse.

### 4. [Goruut](https://github.com/neurlang/goruut)

- **Role:** multilingual IPA phonemizer
- **Status:** candidate
- **Output/validation:** Burmese support is claimed; verify standard/dialect, tones, register/phonation and IPA convention
- **License:** Verify current upstream license and model/data terms
- **Repository integration:** not yet enabled; upstream behavior and license must be checked before dependency, data, or code reuse.

### 6. [Epitran](https://github.com/dmort27/epitran)

- **Role:** grapheme-to-IPA transliteration library
- **Status:** candidate / raw-output benchmark baseline only
- **Output/validation:** The repository already contains an optional benchmark script using the `mya-Mymr` mapping. This is not proof of standard Burmese coverage or accurate tone, phonation, dialect, or IPA convention. Treat output as diagnostic until independently adjudicated.
- **License:** Verify the exact pinned release and the license/provenance of the language mapping data before reuse or redistribution.
- **Repository integration:** not enabled in the runtime; the benchmark requires separate installation and does not change the production IPA-to-Ukrainian path.

### 5. [eSpeak NG](https://github.com/espeak-ng/espeak-ng)

- **Role:** speech engine / phoneme output
- **Status:** candidate
- **Output/validation:** Check Burmese voice, phoneme inventory and explicit IPA output; don't treat engine codes as IPA without conversion
- **License:** GPL-3.0; assess distribution implications
- **Repository integration:** not yet enabled; upstream behavior and license must be checked before dependency, data, or code reuse.


## Shared IPA display fonts

These fonts render IPA; they do **not** generate pronunciations. Prefer Unicode fonts rather than legacy non-Unicode IPA encodings.

- [Charis SIL](https://software.sil.org/charis/) — Recommended font candidate for readable IPA and combining diacritics. License: SIL Open Font License; verify current release metadata.
- [Doulos SIL](https://software.sil.org/doulos/) — IPA-focused font candidate; verify combining-diacritic rendering in target browsers. License: SIL Open Font License; verify current release metadata.
- [DejaVu Sans](https://dejavu-fonts.github.io/) — Broad Unicode/IPA fallback candidate; test exact glyph coverage on target devices. License: DejaVu license; retain upstream notices.

For the live browser UI, use a CSS font stack with an IPA-capable primary font and system fallbacks; test combining diacritics, tie bars, length marks, stress marks, tone marks, and syllable boundaries on Windows, Linux, and mobile. Do not add binary fonts to this repository until the exact font release, license notices, and distribution strategy are reviewed.

## Acceptance gates before runtime integration

1. Record the upstream commit/version, exact license, model/dictionary licenses, and source provenance.
2. Pin the dependency or provide a reproducible adapter installation procedure; no unpinned network downloads at runtime.
3. Store the external raw output separately from any normalized IPA.
4. Add language-specific conversion tests for Unicode, tones, vowel length, syllable boundaries, diacritics, unsupported input, and malformed output.
5. Compare each candidate against the same versioned, independently reviewed gold set. Report exact-match and feature-level errors separately; do not treat agreement between tools as ground truth.
6. Confirm that only a validated typed IPA result reaches the existing ClippyFirst Ukrainian adapter.
7. Keep optional tools optional: a missing third-party dependency must not break the core engine or silently trigger a fallback.

## Machine-readable registry

The companion `data/external-ipa-renderers.json` is the canonical candidate inventory for this repository. Every entry currently has `verified_in_repo: false` and `enabled_by_default: false` until an implementation and its verification evidence are committed.


## Source-script display fonts (not IPA engines)

These resources are relevant to the UI's display of the source writing system; they do not generate IPA and must not be treated as phonemizers.

- [Inter Font Extensions](https://github.com/grab/inter-font-extensions) — May improve display of the source scripts in interfaces; does not generate IPA and is not a replacement for an IPA-capable Latin font. License: Verify current upstream font and repository license.
- [Padauk](https://software.sil.org/padauk/) — Useful for Myanmar-script text shaping and coverage; not an IPA transcription engine. License: SIL Open Font License; verify current release metadata.
- [Busra](https://software.sil.org/busra/) — Khmer-script display font only; not an IPA transcription engine. License: SIL Open Font License; verify current release metadata.
- [Mondulkiri](https://software.sil.org/mondulkiri/) — Khmer-script display font only; not an IPA transcription engine. License: SIL Open Font License; verify current release metadata.

## Additional Burmese G2P and benchmark resources — 2026-11-11

### Google Language Resources Burmese WFST

- Upstream grammar: [google/language-resources/my/burmese.grm](https://github.com/google/language-resources/tree/a90601024f07ab7e96c911243324e0adeb16da96/my), pinned to commit `a90601024f07ab7e96c911243324e0adeb16da96`.
- It is a Thrax grammar compiled to a weighted OpenFst transducer. The 2020 LREC paper explicitly states that the input tape accepts Unicode Myanmar characters and the output tape emits phonemes represented in IPA.
- The paper reports 195 states, 2,966 arcs and an 88-symbol inventory (34 consonants + 54 vowels), with tone/phonation variants. Processing includes medial reordering, spelling-variant unification, vowel normalization, complex-stack handling, syllable-position rewrites, phonological changes and exceptions.
- The Google repository declares Apache-2.0. Its legacy WORKSPACE contains unpinned upstream dependencies; the optional CI workflow pins the language-resources commit and a compatibility Abseil commit, but this is not yet a fully hermetic dependency lock.
- It is an optional external comparator, not enabled in the product runtime.

### Benchmark references (not interchangeable)

- [WSSANLP 2016 Myanmar G2P comparison](https://aclanthology.org/W16-3702/) evaluates seven methods on 25,300 MLC dictionary words (25,000 train, three 100-word open test sets, plus a 100-word closed test). The paper reports PER for WFST of 14.7%, 11.4% and 15.7% on open1–open3; CRF reaches 15.7% on open3; PBSMT reports 16.1%, 13.1% and 22.0%. Phone labels are romanized notation, not the project's IPA convention. The paper's closed-test zero scores are not open-test performance.
- [OpenSLR SLR80](https://www.openslr.org/80/) is a CC BY-SA 4.0 Burmese audio/transcript corpus: 2,528 utterances from 20 female native speakers, 9,941 unique words and 22,443 total words. It contains orthographic word-segmented transcripts, not IPA labels; it is a future audio-review/annotation resource, not a G2P gold set.

The 2016 PER table and the 2020 Google FST description are research evidence, not performance claims for the current ClippyFirst implementation. Rights and annotation boundaries remain explicit.
