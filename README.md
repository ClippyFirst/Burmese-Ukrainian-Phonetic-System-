# Burmese → Ukrainian Phonetic-Graphemic Correspondence System

Research-grade Burmese (Myanmar script) → Ukrainian correspondence scaffold.

## Scientific pipeline

Burmese Unicode → normalization → graphemic/syllable structure → onset/conjunct/kinzi/medials/vowel/inherent-vowel analysis → prosodic analysis → Burmese phonology → surface phonetics → IPA → feature space → Ukrainian target.

## Scope

The default scope is contemporary Standard Burmese. Yangon-oriented claims are used only where the cited source supports that scope. Myanmar script is not treated as synonymous with Burmese.

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
- Ukrainian target adapter that does not duplicate the canonical Ukrainian inventory.
- JSON Schemas, benchmark seeds, adversarial-test specification and CI.

Not yet established as complete:
- full Burmese vowel-combination derivation;
- complete coda and checked-syllable realization;
- complete tone/register/phonation realization;
- full allophony and phonological-rule engine;
- corpus-backed lexical validation;
- final feature-distance ranking against the canonical Ukrainian-Phonetic-Inventory schema.

## Evidence policy

Unicode is treated as authoritative for encoding and script mechanics, not as automatic authority for every phonological analysis.

The prosodic layer retains competing analyses. Traditional four-way descriptions and newer eight-tone double-register proposals are not averaged into a false consensus.

## Sources

- Unicode Standard, Chapter 16, Myanmar.
- Unicode Technical Note #11, Representing Myanmar in Unicode.
- Green (2002), Word, Foot, and Syllable Structure in Burmese.
- Mooney & Repetti-Ludlow (2021), Sonority and syllable structure: The case of Burmese tone.
- Duan & Zhu (2025), Double registers and eight tones in Burmese.
- Tun et al. (2011), Myanmar text-to-speech system with rule-based tone synthesis.

## Status labels

ESTABLISHED · WELL_SUPPORTED · ANALYSIS_DEPENDENT · DIALECT_DEPENDENT · CONTEXT_DEPENDENT · UNCERTAIN · DISPUTED · NOT_ESTABLISHED · UNSUPPORTED

The implementation intentionally returns uncertainty instead of silently inventing a linguistic analysis.
