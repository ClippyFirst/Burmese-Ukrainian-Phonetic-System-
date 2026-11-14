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


## Burmese transcription level: medial signs and nasal coda

An orthographic medial sign is not an IPA segment by name: U+103C MEDIAL RA is commonly described as /j/ in relevant contexts, with onset-specific alternatives; U+103D can participate in glide or rime behavior; U+103E can alter aspiration/phonation or fuse with an onset. The orthographic parser must preserve the sign and codepoint sequence, while the phonological layer resolves the context.

The output contract must distinguish phonemic/broad IPA from narrow surface phonetics. Green's abstract placeless nasal /N/ may be realized through preceding-vowel nasalization and approximate place articulation; it must not be silently rewritten as an independent [ɴ]. The Ukrainian rule for IPA /ɴ/ applies only if the selected source analysis explicitly yields that segment. Preserve nasalization, coda identity, tone/register and uncertainty until the target policy explicitly handles them.


## Typed nasalization and abstract coda

If a source analysis posits a placeless nasal /N/ and describes a surface nasalized vowel, preserve both levels rather than substituting an independent /ɴ/ without evidence. The current IPA gold schema can store nasalization in the literal IPA value but has no separate typed nasalization property. This is a documented analytics limitation; a schema change is deferred until the expert convention sheet selects the transcription level and representation.
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


## Burmese transcription level: medial signs and nasal coda

An orthographic medial sign is not an IPA segment by name: U+103C MEDIAL RA is commonly described as /j/ in relevant contexts, with onset-specific alternatives; U+103D can participate in glide or rime behavior; U+103E can alter aspiration/phonation or fuse with an onset. The orthographic parser must preserve the sign and codepoint sequence, while the phonological layer resolves the context.

The output contract must distinguish phonemic/broad IPA from narrow surface phonetics. Green's abstract placeless nasal /N/ may be realized through preceding-vowel nasalization and approximate place articulation; it must not be silently rewritten as an independent [ɴ]. The Ukrainian rule for IPA /ɴ/ applies only if the selected source analysis explicitly yields that segment. Preserve nasalization, coda identity, tone/register and uncertainty until the target policy explicitly handles them.


## Typed nasalization and abstract coda

If a source analysis posits a placeless nasal /N/ and describes a surface nasalized vowel, preserve both levels rather than substituting an independent /ɴ/ without evidence. The current IPA gold schema can store nasalization in the literal IPA value but has no separate typed nasalization property. This is a documented analytics limitation; a schema change is deferred until the expert convention sheet selects the transcription level and representation.


## Romanization is not pronunciation-based transcription

Mya2Rom exposes separate modes: MLCTS (orthographic), MLCTS2 (more phonetic romanization), and IPA. The current browser romanization adapter explicitly requests MLCTS. Thus Latin→Ukrainian crosswalk outputs are orthographic transliteration candidates, not a pronunciation model. Do not infer IPA or surface sounds from an MLCTS string; the IPA-first path must remain independent.
