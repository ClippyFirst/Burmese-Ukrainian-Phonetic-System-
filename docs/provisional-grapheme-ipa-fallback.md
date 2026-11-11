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


## Implementation checkpoint — 2026-11-11

A minimal onset-only fallback is now implemented in the Python rule engine and browser engine.

- Reuses the existing Yangon-profile initial-consonant IPA inventory and the existing IPA → Ukrainian adapter.
- Keeps canonical ipa and ukrainian fields withheld when any syllable remains unresolved.
- Exposes separate provisional IPA/Ukrainian previews, fallback_status and per-syllable fallback_trace in Python; the browser displays the provisional onset and a visible ?.
- Does not infer vowel, coda, asat realization, medials, kinzi, conjuncts, tone or phonation.
- Added a Python regression for a syllable with unresolved coda structure and browser source-contract assertions.

Status: PARTIAL, not DONE_VERIFIED. This reuses the existing initial-consonant IPA map; it is not a full Myanmar grapheme-position inventory. A dedicated source registry with exact per-entry evidence and Yangon-profile scope remains required. Browser tests currently assert source-level wiring, not functional Python/JavaScript parity fixtures.

Implementation commits: fe2329dc74b677bbb44a605d9c5ba10f083d58c4 (Python engine), 6936f01d3ff320574b8802c7af348d687e63ce17 (Python regression), 5b83f5d3674b9e6d2f4114047bd67be5a5440719 (browser), 36b6ebf5a1d5a03b0c4d7a95aae2d842046e4152 (browser regression). No exact-head workflow run was returned for this branch at the last check; tests are not recorded as passed.


## Scope correction — 2026-11-11

The onset-only preview is deliberately restricted to an isolated bare consonant token whose onset position is established by token boundaries. It does not run on syllables containing a vowel sign, coda/asat, medial, kinzi, conjunct, prosodic mark or other contextual structure. Canonical IPA/Ukrainian fields remain fail-closed; the browser shows the preview only in per-syllable analysis details, not in the main canonical output. This preserves existing contextual parser behavior.
