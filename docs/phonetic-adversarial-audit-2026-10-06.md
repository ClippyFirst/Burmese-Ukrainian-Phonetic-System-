# Burmese phonetic adversarial audit

**Date:** 2026-10-06

This audit targets failure modes where a character-by-character transliteration can produce a formally plausible but phonetically wrong result.

## Findings

### 1. Medials are contextual

A medial is not always an independent IPA segment that can simply be concatenated to the onset.

In Standard Burmese, relevant velar + `ျ`/`ြ` combinations can be realized as palatal affricates:
- `ကျ` → /tɕ/
- `ချ` → /tɕʰ/
- `ဂျ` / `ဂြ` → /dʑ/

Ha-to `ှ` also has contextual behavior: on sonorants it can indicate devoicing; `ရှ` and `ယှ` are realized as /ʃ/ in Standard Burmese.

The web engine therefore applies contextual rules before target-language rendering.

### 2. Compound vowel signs require rime context

`ေ + ာ` (`ော`) cannot safely be rendered as `e + a`.

Its realization depends on syllable structure. In open syllables it corresponds to /ɔ/ in the relevant analysis; before a nasal/checked coda it can surface as /aʊ/. A high-value regression is:

`ကျောင်း` → /tɕaʊŋ/ (broad structural IPA; tone omitted by the current seed layer).

This is deliberately not treated as a complete vowel system. Other closed-syllable patterns still require systematic expansion.

### 3. Kinzi is a linguistic final of the preceding syllable

Unicode encodes Burmese kinzi as `င + ် + ္`, before the next written consonant. Linguistically it belongs to the preceding syllable as final /ŋ/.

Therefore `မင်္ဂလာ` must be segmented linguistically as `မင် | ဂ | လာ`, not as one giant orthographic syllable beginning with `မ` and containing `င` as a second onset.

The converter now breaks after kinzi and attaches its /ŋ/ value to the preceding parsed syllable.

### 4. Ukrainian output must follow IPA, not Cyrillic inheritance

The target layer is intentionally separate from Russian practical transcription.

Examples: /tɕ/ → ч — proposed practical target; /dʑ/ → дж — proposed practical target; /ʃ/ → ш — proposed practical target; /ŋ/ → нг — proposed practical target.

These are project policy decisions, not claims of an official Ukrainian Burmese standard. Where the target is uncertain, the status remains `analysis_dependent` or `proposed`.

## Regression corpus

| Burmese | Purpose | Expected structural IPA |
|---|---|---|
| `ကျား` | velar + medial palatalization | contains `tɕa` |
| `ကျောင်း` | compound `ော` + nasal coda | contains `tɕaʊŋ` |
| `မင်္ဂလာ` | kinzi syllable boundary | contains separate `မင်္` and `ဂ` units |
| `ရှ` | ha-to contextual realization | contains `ʃ` |
| `င်္ကာ` | kinzi + following onset | contains `ŋka` |
| `ABC 123` | unsupported non-Myanmar input | `UNSUPPORTED` |
| `မြန်မာ ABC 123!` | mixed input preservation | Latin/numbers/punctuation unchanged |

## Evidence

- Unicode Standard, Chapter 16 — Myanmar: https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-16/
- Unicode Technical Note #11 — Representing Myanmar in Unicode: https://www.unicode.org/notes/tn11/myanmar_uni-v2.pdf
- Watkins, J. — *Burmese*, Illustrations of the IPA.
- Mooney, K. & Repetti-Ludlow, C. (2021) — *Sonority and syllable structure: The case of Burmese*.
- Burmese lexical pronunciation records were cross-checked for `ကျောင်း`, `မင်္ဂလာ`, and `ကြား`.

## Remaining high-priority work

1. Complete the Burmese rime table rather than adding isolated vowel exceptions.
2. Model nasalized finals and /ɰ̃/ consistently.
3. Add tone/phonation metadata without converting Burmese tone into Ukrainian stress.
4. Expand contextual voicing/devoicing and allophony.
5. Validate against a pronunciation dictionary/corpus rather than only hand-picked examples.
6. Build a Ukrainian gold set for names and common vocabulary.
7. Keep all Ukrainian target mappings evidence-labelled until corpus evaluation supports stronger claims.

The current changes fix demonstrated structural errors; they do not claim that the project is already a complete Burmese G2P system.