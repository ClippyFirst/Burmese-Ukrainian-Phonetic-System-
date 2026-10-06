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

## Second hardening pass — closed rimes, codas, and adversarial corrections

The first pass exposed a second-order error: some contextual fixes were still too coarse.

### 5. Closed /i/ is not uniformly /eɪ/

The earlier seed rule "closed i → eɪ" was too broad. Lexical checks show at least two distinct patterns:

- `ပင်` → /pɪ̀ɴ/
- `တင်` → /tɪ̀ɴ/
- `စိတ်` → /seɪʔ/

Therefore the engine now distinguishes nasal-final and checked/glottal-final syllables:

- /i/ + nasal final → /ɪ/
- /i/ + checked final → /eɪ/

This removes a concrete false generalization.

### 6. Burmese final nasals are not simply written /ŋ/

The broad phonological layer frequently represents Burmese final nasal realization as /ɴ/. The engine therefore distinguishes:

- onset /ŋ/ → /ŋ/
- final nasal realization → /ɴ/

The Ukrainian practical layer maps /ɴ/ conservatively to `нг` and keeps this as a project-level proposed correspondence.

### 7. Checked codas are not the written consonant's full phonetic value

For the common checked-final series, the engine now derives a glottal closure /ʔ/ rather than appending the onset consonant's IPA value. This is necessary for examples such as:

- `စိတ်` → /seɪʔ/
- `ပိုက်` → /paɪʔ/
- `ပက်` → /pɛʔ/

This is a major correction because a character-by-character engine would otherwise produce outputs such as seɪt or paɪk.

### 8. Medial `ွ` changes the rime

The medial `ွ` cannot be treated as a literal +w segment in every syllable.

Adversarial examples show contextual rime changes:

- `ကွက်` → /kwɛʔ/
- `ကွန်` → /kʊ̀ɴ/
- `ဆွမ်း` → /sʰʊ́ɴ/

The implementation now has conservative rules for common closed `ွ` patterns and refuses to invent a pronunciation for unresolved combinations.

### 9. `ကိုင်` / `ကိုက်` distinguish nasal and checked closure

The spelling `ိ + ု` forms a diphthongal rime in closed syllables:

- `ကိုင်` → /kàɪɴ/
- `ကိုက်` → /kaɪʔ/

This is represented as /aɪ/ plus the appropriate nasal or glottal coda, rather than two independent vowel segments.

## Corrected regression corpus

| Burmese | Expected structural IPA | Why it is adversarial |
|---|---|---|
| `ပင်` | `pɪɴ` | catches overgeneralized closed /i/ → /eɪ/ |
| `တင်` | `tɪɴ` | same nasal-final distinction |
| `စိတ်` | `seɪʔ` | checked /i/ contrast |
| `ပိုက်` | `paɪʔ` | diphthong + checked coda |
| `ကိုင်` | `kaɪɴ` | diphthong + nasal coda |
| `ကုန်` | `koʊɴ` | closed /u/ + nasal |
| `ကွက်` | `kwɛʔ` | medial-wa rime alternation |
| `ကွန်` | `kwʊɴ` | medial-wa + nasal rime |
| `ကျောင်း` | `tɕaʊɴ` | compound vowel + nasal final |
| `မင်္ဂလာ` | separate `မင်္` + `ဂ` | kinzi boundary |
| `ရှ` | contains `ʃ` | ha-to contextual realization |

### Evidence boundary

The new rules are not a claim that every Burmese closed rime has now been solved. They cover only patterns for which the current evidence supports a deterministic rule. The remaining vowel/rime space stays explicitly incomplete.

This is preferable to a superficially "complete" transliterator whose hidden defaults create systematic phonetic errors.
