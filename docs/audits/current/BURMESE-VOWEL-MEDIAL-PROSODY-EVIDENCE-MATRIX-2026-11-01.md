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


## 6. Consonantal phonation and voiceless sonorants

Green's 2002 analysis (also published as a 2005 chapter) argues that the contrast between voiced and voiceless sonorants is probably [spread glottis], i.e. phonological aspiration, rather than simply [voice] (Green §1.2, pp. 4–5). This is a consonant-level laryngeal contrast and must remain distinct from vowel breathiness or a lower register.

Repetti-Ludlow (2023), [full text](https://d-nb.info/1311139060/34), supplies an acoustic test but has a narrow sample:

| Design/result | Evidence |
|---|---|
| Target sonorants | /w, w̥, l, l̥, ŋ, ŋ̥, m, m̥/ |
| Prosodic controls | monosyllabic minimal pairs, high and low tones, one nucleus vowel /a/ |
| Position | phrase-medial tokens only |
| SG realization | spread-glottis gesture in 78% of voiceless-sonorant tokens; no SG gesture in 22% |
| Strong cues | SG duration, sonorant F0 and duration, strength of excitation in following vowel |
| Limitation | does not test all six voiced/voiceless sonorant pairs, all vowels, all tones or all syllable positions |

The paper therefore supports a typed distinction between phonemic voicelessness and its variable phonetic realization; it does not justify turning every voiceless sonorant into a fixed aspirated sequence in all contexts.

## 7. Source reconciliation and licensing

- Green (2002) is the October 2002 ROA paper; Green (2005) is the published chapter in *Studies in Burmese Linguistics*, pp. 1–25. Both are the same research line; cite the exact edition used.
- LREC 2020 is CC BY-NC. Its phonological description is usable as research evidence, but its corpus and resource package must not be copied into a commercial project without a separate rights review.
- Duan & Zhu (2025) is an open-access CC BY 4.0 article. The publisher abstract and article outline establish the eight-tone/two-register proposal; the full empirical tables have not been extracted in this pass, so it remains a competing analysis, not implemented consensus.
- Repetti-Ludlow (2023) is a production study of a restricted subset of sonorants and contexts, not a general register or tone study.


## 8. LREC 2020's explicit open/closed vowel partition

The LREC 2020 paper gives a second, distinct inventory following Watkins (2000/2001). It should not be merged silently with Green's 50-rhyme analysis.

| Set | Distribution | Reported inventory | Evidence locator |
|---|---|---|---|
| Open, non-nasal set | Orthographically open syllables, not nasalized | Eight vowels including /ə/ | LREC 2020 §4.3, pp. 6331–6332 |
| Closed/nasal set | Nasalized syllables or syllables closed by /ʔ/ | Four vowels; /ɛ/ and /a/ overlap with the first set, while /ɛ/ is restricted to non-nasalized syllables | LREC 2020 §4.3 |
| Diphthongs | Only in the second set | Four diphthongs; must be closed by /ʔ/ or placeless /N/ | LREC 2020 §4.3 |
| Tone categories | Low, high, creaky, checked | Four categories | LREC 2020 §3 |
| Checked tone | Always has final /ʔ/; unavailable with nasal rhymes | Segmental coda + tone interaction | LREC 2020 §4.3 |

LREC 2020 explicitly describes tone cues as pitch, contour, length and phonation type. It also describes 34 consonants. This is a system-description/G2P analysis, not an independent gold dataset.

## 9. Rights boundary for LREC 2020 resources

The paper states that the authors' in-house Burmese speech corpora and segmentation corpus are not in the public domain (pp. 6328–6330). The article itself is CC BY-NC, but that does not grant redistribution rights to the underlying speech data. Do not copy or train on the in-house speech corpus. The Google language-resource grammar/code must be rights-reviewed separately from the speech data; the project does not import either as production assets in this change.
