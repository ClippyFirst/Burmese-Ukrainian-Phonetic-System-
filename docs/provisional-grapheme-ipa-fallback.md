# Provisional Burmese grapheme-to-IPA fallback

Status: design contract; implementation pending.

## Purpose

Mirror the Lao hybrid's typed, low-confidence grapheme fallback while preserving the Yangon Burmese engine's existing conservative phonology. This feature improves visible output coverage; it does not certify the pronunciation of an unresolved syllable.

## Required pipeline

Myanmar grapheme cluster / recognized positional unit → provisional IPA token(s) → the existing IPA-to-Ukrainian adapter → Ukrainian text with a visible `?` uncertainty marker.

Never map Myanmar code points directly to Ukrainian letters. Provisional IPA must be typed `PROVISIONAL`, carry source grapheme, positional role, rule ID and evidence, and must not be counted as supported IPA in benchmarks.

## Eligibility and limits

- Reuse only source-backed initial consonant hints for individually recognized Myanmar consonant letters.
- Do not assume an onset hint also applies to coda position.
- Do not invent a vowel for an unresolved syllable. Vowel signs, virama/asat, medials, kinzi and stacked consonants require a complete, registered positional rule before any provisional IPA is emitted.
- Do not infer tone, phonation or vowel length from incomplete structure.
- Preserve unknown marks and unresolved grapheme clusters explicitly.
- Keep full-confidence IPA/Ukrainian fields unchanged. Expose fallback separately, e.g. `provisional_ipa`, `provisional_ukrainian`, `fallback_status`, and `fallback_trace`.

## Confidence and rendering contract

- `SUPPORTED`: normal engine path only.
- `UNCERTAIN`: structurally complete IPA with a known uncertainty.
- `PROVISIONAL`: registered grapheme-position hint, low confidence; append `?` to the Ukrainian rendering of the affected unresolved unit.
- `UNKNOWN`: no registered IPA hint; render `?` only, with the source grapheme preserved in trace.

Provisional values must not be promoted to canonical `ipa`, and must be excluded from IPA accuracy scoring. Browser and Python must return the same text and trace.

## Acceptance

1. Source registry entries for each fallback rule include Yangon profile scope, grapheme/position, IPA hint, primary source and review status.
2. Tests cover consonant initials, dependent vowels, asat/finals, medials, kinzi, stacked forms, punctuation, mixed scripts and unknown symbols.
3. Python and browser parity tests cover the same fixtures.
4. Tests assert that unsupported constructions remain visible as uncertainty and no tone/phonation is invented.
5. Full CI and built-site Chromium tests pass.
6. Report rendering coverage separately from supported IPA coverage and phonetic accuracy.

## Current evidence boundary

The Burmese IPA practical adapter only maps IPA to Ukrainian; it cannot establish Burmese grapheme-to-IPA readings. The existing conservative parser does not provide a universal fallback for all unresolved clusters. Do not manufacture provisional IPA from the target correspondence table. Until Yangon positional hints are registered and sourced, unsupported constructions remain `UNKNOWN`.
