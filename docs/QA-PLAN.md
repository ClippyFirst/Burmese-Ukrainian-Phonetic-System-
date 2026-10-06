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
