# Methodology

## Terminology

This project is not a pure transliteration system and not a narrow IPA
transcription table.

- **Transliteration** reproduces a source writing system through a defined
  symbol-to-symbol or grapheme-oriented convention.
- **Phonological/phonetic transcription** represents pronunciation or
  phonological structure.
- **Practical transcription** adapts source pronunciation and/or established
  source-language representation to the phonology and orthography of the target
  language for readable names and terms.
- **This project** is a hybrid practical system: Burmese orthography is parsed
  structurally, its phonological/phonetic value is represented through IPA, and
  the final form is generated under Ukrainian phonological and orthographic
  constraints.

Therefore the system must not be described simply as "Burmese transliteration"
when the intended output is a Ukrainian practical pronunciation-oriented form.

## Research pipeline

The target is contemporary Standard Burmese, with Yangon-oriented scope only
where a source supports it. Myanmar script is not treated as synonymous with
Burmese.

The pipeline is:

Unicode
→ graphemic structure
→ syllable structure
→ Burmese phonology
→ surface phonetics
→ IPA
→ Ukrainian target phonology
→ Ukrainian orthography
→ practical Ukrainian output

Russian practical transcription is a comparative control layer. It is not an
intermediate representation in the runtime pipeline.

## Evidence and decision layers

The repository separates:

1. source-language facts;
2. competing linguistic analyses;
3. target-language facts;
4. project-specific practical decisions;
5. computational implementation.

A source claim must not be converted directly into a Ukrainian output rule
without an explicit target-language decision.

## Source-language analysis

Unicode is authoritative for encoding and storage mechanics. Phonological
claims are independently sourced.

The Burmese analysis distinguishes, where relevant:

- code points;
- grapheme clusters;
- orthographic syllable structure;
- onset;
- conjunct/subjoined consonant;
- kinzi;
- medial;
- dependent vowel;
- inherent vowel;
- coda/final;
- checkedness;
- tone;
- register;
- phonation;
- surface phonetics.

Conflicting analyses are retained rather than averaged into a false consensus.

## Ukrainian adaptation

For each difficult Burmese segment or structure the project asks:

1. Is there a Ukrainian phonological analogue?
2. Is there a natural Ukrainian grapheme or sequence?
3. Would the spelling induce a misleading Ukrainian pronunciation?
4. Should the distinction be preserved or neutralized?
5. Does established Ukrainian usage constrain the result?
6. Is the resulting rule reproducible and explainable?

The current Ukrainian normative reference is the 2026 state standard
"Український правопис". The canonical computational target inventory is
maintained in the separate ClippyFirst/Ukrainian-Phonetic-Inventory repository
and is not duplicated here.

## Practicality principle

The system optimizes jointly for:

- phonetic adequacy;
- Ukrainian orthographic naturalness;
- readability;
- consistency;
- recoverability where feasible;
- usability for proper names and geographical names.

It does not preserve every Burmese contrast merely because a technical
notation exists for it.

## Prosody

Burmese tone/register/phonation are kept as source-language analytical
metadata. They are not automatically converted into Ukrainian lexical stress.

## Current implementation status

The implementation is intentionally conservative. Incomplete evidence produces
explicit uncertainty rather than invented IPA or orthography.
