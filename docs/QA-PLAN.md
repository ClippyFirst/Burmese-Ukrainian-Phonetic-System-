# Burmese → Ukrainian — QA Plan

## Test layers

### Data
Validate all canonical CSV files used by the web build.

### Unit
Cover Unicode normalization, Myanmar grapheme segmentation, kinzi, virama/subjoined consonants, medials, dependent vowels, malformed clusters, practical rule lookup, deterministic conversion and status propagation.

### Browser
Cover initial empty state, example conversion, copy, clear, source preservation, punctuation/whitespace, narrow mobile viewport, scientific-page navigation and reduced-motion preference.

### Adversarial
Include isolated non-Myanmar text, mixed Burmese/Latin, punctuation-heavy text, malformed virama, unsupported vowel combinations, kinzi sequences, zero-width/control characters where relevant, and IPA values with no established Ukrainian mapping.

## Invariants

- Input is never mutated.
- Unsupported material is preserved.
- No unknown IPA value becomes a confident Ukrainian output.
- Repeated conversion is deterministic.
- Generated mapping data is deterministic.
- UI never invents a source or rule.
- Russian mappings are never used as an implicit fallback.

## Accessibility

Check keyboard order, focus visibility, semantic labels, live status, contrast, zoom and mobile overflow.

## Release evidence

The release report must distinguish local unit-test result, browser-test result, build result and CI result. Never report CI as green without an actual workflow result.


## IPA fail-closed regression — 2026-10-24

The IPA adapter must not emit a plausible-looking partial transcription from a cluster the parser did not fully consume. `src/burmese_ukrainian/ipa.py` now returns no segment IPA unless the parser status is exactly `established`. The top-level serializer keeps an explicit `?` placeholder for unresolved syllables, rather than leaking a partial onset-based string such as `k?` from malformed input. A regression assertion covers the malformed virama sequence `က္`; the existing partial-inherent-vowel case `က` remains explicitly partial and is not upgraded to supported IPA.

This change does not fill the known phonology gaps for medials, codas, tones, or inherent-vowel realization. PR-head CI [40112716801](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40112716801) passed on `96143ad7569c65c6e0692836d7f3fcfcb6ae0697`: pytest, generated-data drift check, npm build/tests, and Playwright browser tests all passed. Empirical accuracy remains unmeasured.
