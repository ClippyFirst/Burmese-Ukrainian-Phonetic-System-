# Burmese vowel × medial × checked-syllable × prosody evidence matrix — 2026-11-01

**Profile:** Modern Standard Burmese is the initial target, but historical analyses, dialects and competing phonological conventions remain separate. This matrix records published analyses; it is not an adjudicated lexical corpus.

## 1. Syllable and rhyme baseline — Green

Antony Green, “Word, Foot, and Syllable Structure in Burmese” (revised from the 1995 Cornell Phonetics Laboratory paper), [full text](https://roa.rutgers.edu/files/551-1002/551-1002-GREEN-0-1.PDF), provides an inspectable model.

| Dimension | Green's analysis | Locator | Implementation consequence |
|---|---|---|---|
| Major syllable | Obligatory onset; C(G)V((V)C); 50 listed major-syllable rhymes | §§1.1–2 | Do not infer a vowel from orthography alone |
| Major-syllable tones | Low, high, creaky, checked | §1.1 | Retain as one four-way analysis |
| Nasal rhymes | Only low, high and creaky; checked excluded | §1.1 | No unrestricted tone × nasal-coda cross-product |
| Coda | Placeless glottal stop /ʔ/ or placeless nasal /N/ | §§1.2, 2.2 | Keep place assimilation and phonological coda separate |
| Diphthongs | /ei, ai, ou, au/ require a closed syllable | §2.2 | Do not accept these as open-syllable outputs in this analysis |
| Mid monophthongs | /e, o, ə/ occur only in open syllables in the described distribution | §2.2 | Add negative tests for closed forms |
| /ə/ distribution | Open syllable or before /ʔ/, but not before /N/ | §2.2 | Coda-specific rule |
| Vowel length | Not contrastive in Green's analysis; major syllables are bimoraic | §2.1 | Distinguish phonemic length from duration/weight |
| Duration | Checked < creaky < low < high in rhyme duration | §2.1 | Tone/phonation can condition duration without creating length contrast |
| Minor syllable | Schwa only; open, toneless, simple onset, non-final | §3 | Do not assign major-syllable tone or coda |

## 2. Competing accounts

| Source | Claim | Status |
|---|---|---|
| Green (1995/revised chapter) | Four-way low/high/creaky/checked analysis with major/minor syllables | SOURCE_ANALYSIS |
| Mooney & Repetti-Ludlow (2021), [CC BY 4.0](https://doi.org/10.3765/plsa.v6i1.4900) | Vowel alternations are argued to be tone-independent and related to sonority sequencing | PEER_REVIEWED_COMPETING_ANALYSIS |
| Duan & Zhu (2025), [publisher record](https://doi.org/10.1075/lali.00203.dua) | Two registers (modal and lower/breathy) and eight tones | PEER_REVIEWED_COMPETING_ANALYSIS; full paper/data not inspected |
| Repetti-Ludlow (2023), [Phonetica DOI](https://doi.org/10.1515/phon-2022-0026) | Voiceless sonorants show spread-glottis/turbulent cues; duration, F0 and following-vowel excitation contribute | CONSONANT_PHONATION_EVIDENCE, not vowel-tone inventory |
| LREC 2020, [paper](https://aclanthology.org/2020.lrec-1.777.pdf) | Reports 34 consonants, seven basic vowels, schwa, four diphthongs and four tone categories; tone cues include pitch, contour, length and phonation | SYSTEM_DESCRIPTION, not gold data |

Do not average four- and eight-tone inventories. Keep source terminology, speaker variety and phonetic evidence separate pending specialist adjudication.

## 3. Medials: orthographic sequence is not phonological value

| Written structure | Established | Unresolved |
|---|---|---|
| Medial ya | Unicode defines encoding/ordering; Green allows glide-bearing onsets | Modern Standard Burmese distribution and realization by base consonant |
| Medial wa | Script sequence is structurally represented; Green allows glide-bearing onsets | Whether each occurrence is /w/, part of the rhyme or context-specific |
| Medial ra | Orthographic/stacking history must be retained | Modern phonemic status, dialectal reflexes and phonetic value |
| Medial ha | Orthographic category must be parsed separately | Segmental aspiration vs register/phonation effect by environment |
| Multiple medials | Unicode stack/ordering validity is an orthographic fact | Phonological legality and lexical status require attested examples |

LREC 2020 describes the abugida, stacking, vowel/tone marks and asat/virama; Unicode describes encoding. Neither justifies mapping every written medial one-to-one to an IPA segment.

## 4. Checked syllables and vowel × coda matrix

| Rhyme environment | Green analysis | Status |
|---|---|---|
| Open major syllable | Bimoraic vowel; four tone categories | SOURCE_ANALYSIS |
| Nasal coda /N/ | Low/high/creaky only; placeless nasal | SOURCE_ANALYSIS |
| Checked coda /ʔ/ | Checked tone possible; placeless coda | SOURCE_ANALYSIS |
| Diphthong + /N/ | Permitted in listed rhyme inventory | SOURCE_ANALYSIS |
| Diphthong + /ʔ/ | Permitted in listed rhyme inventory | SOURCE_ANALYSIS |
| Diphthong with no coda | Not permitted in Green's analysis | SOURCE_ANALYSIS |
| /e,o,ə/ + coda | Not permitted for the described mid monophthongs | SOURCE_ANALYSIS |
| /ə/ + /N/ | Not permitted in the described distribution | SOURCE_ANALYSIS |
| Minor schwa + coda/tone | Not permitted | SOURCE_ANALYSIS |

Keep separate: (a) segmental checked coda /ʔ/, (b) creaky phonation, and (c) lexical tone/register. Do not collapse these into one IPA feature.

## 5. Runtime acceptance criteria

1. Every vowel rule cites a source and identifies phonemic, phonetic, orthographic or historical status.
2. Every medial rule specifies base consonant, written medial sequence, profile and source locator.
3. Every coda rule distinguishes /ʔ/, /N/, orthographic asat and other final signs.
4. Tone, register and phonation remain separately typed; broad vs narrow IPA is explicit.
5. Add positive and negative tests for each accepted vowel × coda cell.
6. No deterministic output changes until independent expert annotations cover the relevant cell and Python/browser implementations agree.

**Status:** PARTIAL. Green supplies an inspectable rhyme model, but modern dialect, medials and newer register analyses remain unresolved. Independent expert gold = 0. No IPA labels or unsupported rules were added.
