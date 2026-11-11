# Burmese → Ukrainian practical transcription

## Purpose and pipeline

This is the practical target layer after source-language analysis:

**Burmese orthography → graphemic/syllabic analysis → Burmese phonology → IPA → Ukrainian target-language adaptation → Ukrainian practical orthography**

It is intended for personal names, geographical names, institutions, cultural/historical names and reference use. It is a project proposal, not an official Ukrainian transcription standard.

The deterministic engine now exposes the practical rendering after IPA in its result fields: ukrainian, ukrainian_status and ukrainian_segments. The whole-string adapter is transcribe_ipa(). IPA remains the inspectable boundary; unsupported segments withhold the complete practical string.

## 1. Russian predecessor

A dedicated Russian practical tradition exists. V. G. Epstein's 1959 Rules of Russian Transcription of Burmese Geographical Names was published by the Institute of Oriental Studies of the USSR Academy of Sciences and was intended for Burmese geographical names, with application to personal names and other terms noted in the bibliographic record. A further 1978 institutional instruction for Russian transmission of Burmese geographical names is also documented. A 1958 Epstein bibliographic lead is retained separately but is not treated as independently verified article-level evidence.

A modern documentary table preserves the same family of rules: positional consonants, medial rules, vowel/rime tables, final neutralization and non-marking of tone. The Russian system is a control system, not the target specification.

Its strongest properties:
- onset/final distinction;
- explicit medials;
- checked-syllable treatment;
- nasal-final treatment;
- vowel/rime registry;
- tone outside ordinary practical spelling;
- special orthographic rules.

Its main limitation for Ukrainian is that it is optimized for Russian phonology and orthography.

## 2. Ukrainian consonant target

| Source IPA | Russian comparator | Ukrainian project target |
|---|---|---|
| /k/ | к | к |
| /kʰ/ | кх | к' |
| /t/ | т | т |
| /tʰ/ | тх | т' |
| /p/ | п | п |
| /pʰ/ | пх | п' |
| /sʰ/ | сх | с' |
| /bʰ, dʰ/ | бх, дх | б', д' |
| /ɡ/ (ASCII alias /g/) | г | ґ* |
| /h, ɦ/ | х (Russian /h/) | г |
| /x/ | х | х |
| /z/ | з | з |
| /ɲ/ | нь | нь |
| /ŋ, ɴ/ | нг | нг |
| /w, ʋ/ | у/в | в |
| /j/ | й | context-sensitive й / я / є / ї / ю / йо |
| /ɹ/ | й or р by convention | р* |
| /l/ | л | л |
| /ʃ/ | ш | ш |
| /ʔ/ | ∅ | ∅ (omitted in practical text, retained in IPA/trace) |
| /θ/ | т | т* |
| /ð/ | т | з* |

Asterisks mark explicit project target choices or approximations, not claims of exact phonetic identity.

### /h/, /ɦ/, /ɡ/ and /x/

The system keeps four source values distinct in IPA:
- /h/ → г;
- /ɦ/ → г;
- /ɡ/ (and the ASCII fallback /g/) → ґ under the project's contrast-preserving policy;
- /x/ → х.

The 2026 Ukrainian Orthography §122 says foreign [g] is usually adapted with г, while allowing ґ as an imitation of foreign [g] in personal names. This project deliberately selects ґ for IPA /ɡ/ to preserve the requested distinction from /h/; this is a project-specific research convention, not the only normatively valid Ukrainian rendering of foreign /g/. Genuine /x/ remains х.

### Affricates

| IPA | Ukrainian practical form |
|---|---|
| /t͡s/ | ц |
| /d͡z/ | дз |
| /t͡ʃ/ | ч |
| /d͡ʒ/ | дж |
| /tɕ, t͡ɕ/ | ч |
| /dʑ, d͡ʑ/ | дж |

The tied IPA forms are treated as single affricates by longest-match tokenization. Plain /t/ + /s/ remains тс, not ц; plain /d/ + /z/ remains дз only as two separately traced segments, not an affricate token. These general target correspondences do not imply that all listed affricates are native Burmese phonemes.

## 3. Aspiration

The Russian system preserves /kʰ pʰ tʰ/ as кх пх тх. The project preserves aspiration in IPA and marks it in Ukrainian practical output with an ASCII apostrophe:

- /k/ → к; /kʰ/ → к'
- /t/ → т; /tʰ/ → т'
- /p/ → п; /pʰ/ → п'
- /s/ → с; /sʰ/ → с'
- /bʰ/ → б'; /dʰ/ → д'
- /tɕ/ → ч; /tɕʰ/ → ч' where the source phonological analysis establishes the aspirated affricate.

The apostrophe is a project notation for aspiration, not the Ukrainian orthographic apostrophe rule. It does not represent /ʔ/ and does not replace the upstream IPA feature.

## 4. /j/ and Ukrainian yotation

At the beginning of a syllable, /j/ plus a following vowel is adapted using Ukrainian yotated spelling:

| IPA onset | Practical Ukrainian |
|---|---|
| /ja/ | я |
| /je, jɛ/ | є |
| /ji/ | ї |
| /jo, jɔ/ | йо |
| /ju/ | ю |
| /jɯ/ | йи (analysis-dependent approximation) |

Medial/coda /j/ is rendered as й. The adapter resets syllable-initial handling at spaces and explicit syllable dots. The Burmese engine currently separates its syllable IPA values with spaces; this is a syllable-delimited diagnostic rendering, not a claim that lexical word boundaries have been recovered.

## 5. Vowels

| Burmese IPA | Russian | Ukrainian |
|---|---|---|
| /a/ | а | а |
| /ɛ/ | э | е |
| /i/ | и | і |
| /ɯ/ | ы/у | и* |
| /u/ | у | у |
| /e/ | е | е |
| /o/ | о | о |
| /ɔ/ | о | о |
| /ɪ/ | и | и* |
| /ʊ/ | у | у* |
| /eɪ/ | ей | ей* |
| /oʊ/ | оу | оу* |
| /aɪ/ | ай | ай* |
| /aʊ/ | ау | ау* |

The /ɯ/, /ɪ/, /ʊ/ and diphthong mappings remain analysis-dependent until checked against a dialect-matched lexical gold set. Practical spelling may merge distinctions, but IPA and trace retain them.

## 6. Finals, glottal closure and checked syllables

Written Burmese finals are not copied mechanically. The practical layer distinguishes oral checked syllables, nasal finals, glide finals and orthographic markers.

Where the Burmese phonological analysis gives glottal closure rather than a released final consonant, the ordinary Ukrainian practical string does not print a standalone /ʔ/. The glottal stop remains in IPA and the segment trace. Nasal finals may remain visible.

Pali/Sanskrit stacks are not allowed to enlarge the native Burmese phoneme inventory automatically.

## 7. Tone, register and phonation

The Russian practical system does not encode Burmese tone in ordinary Cyrillic output. The Ukrainian project follows that practical principle but keeps the analytical layer richer:

- practical mode: Ukrainian spelling only;
- research mode: Ukrainian spelling + Burmese tone/register/phonation metadata;
- IPA mode: full evidence-backed phonological/phonetic annotation.

Tone and phonation diacritics, stress marks and vowel length are retained in the adapter's prosody trace and omitted from ordinary practical spelling. Burmese tone must never be converted automatically into Ukrainian stress.

## 8. Executable adapter examples

The following are segment-sequence adapter examples, not lexical gold labels:

| IPA input | Ukrainian output |
|---|---|
| /h ɦ ɡ g x/ | г г ґ ґ х |
| /t͡s d͡z t͡ʃ d͡ʒ tɕ dʑ/ | ц дз ч дж ч дж |
| /ja je ji jo ju/ | я є ї йо ю |
| /kʰàː/ | к'а (tone and length remain in trace) |
| /ʔa/ | а (glottal stop remains in trace) |

An unknown IPA segment withholds the complete Ukrainian string; the adapter does not replace it with a question mark inside an otherwise plausible output.

## 9. Ukrainian orthography and sources

The current Ukrainian state standard is the 2026 edition of Ukrainian Orthography, effective from 2026-03-28. The 2019 edition is historical provenance only. Relevant guidance:
- §122: foreign [g] and [h] adaptation; the usual [g] → г rule and the permitted imitation choice ґ in personal names;
- §124: English [w], [θ] and [ð] adaptation as target-language examples;
- §126: [j] and Ukrainian yotated vowel spellings.

The Ukrainian standard informs the target orthography; it is not evidence about Burmese source phonology. The Russian tables remain comparison material only.

Sources:
- [Official Ukrainian Orthography, 2026 PDF](https://mon.gov.ua/static-objects/mon/sites/1/zagalna%20serednya/Pravopys.2019/ukrayinskii-pravopis-oficiine-vidannia-2026.pdf)
- [Burmese–Russian practical transcription](https://ru.wikipedia.org/wiki/Бирманско-русская_практическая_транскрипция)
- Epstein, V. G. (1959), Rules of Russian Transcription of Burmese Geographical Names (institutional comparator; see source registry).

## 10. Validation

Gold data should cover:
- geographical names;
- personal names;
- institutional names;
- cultural/historical names;
- common lexical items;
- checked syllables;
- nasal finals;
- medials;
- kinzi and stacks;
- Pali/Sanskrit-derived spellings;
- prosodic contrasts;
- established Ukrainian forms.

Report exact string match, syllable-level match, segment-level accuracy, unresolved rate and construction-specific error taxonomy with explicit denominators. The current mapping tests establish deterministic adapter behavior only; they do not prove the phonetic accuracy of the upstream Burmese IPA engine or the empirical correctness of every Ukrainian candidate.
