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
