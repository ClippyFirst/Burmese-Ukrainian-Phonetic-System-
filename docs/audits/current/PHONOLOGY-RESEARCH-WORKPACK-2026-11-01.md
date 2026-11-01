# Burmese phonology research workpack

**Scope:** Modern Standard Burmese as the first profile, with speaker/dialect and register metadata retained. Orthographic decomposition, phonemic representation and phonetic realization must remain separate.

## Evidence already located

1. Antony Green (1995), “The prosodic structure of Burmese: a constraint-based approach,” *Working Papers of the Cornell Phonetics Laboratory* 10, 67–96. [Full paper](https://roa.rutgers.edu/files/115-0000/115-0000-GREEN-0-0.PDF). Green explicitly notes disagreement among authors over tone labels and transcriptions; describes high, low, creaky and checked categories, C(G)V((V)C) structure, and predictable rather than phonemic vowel length in open vs closed syllables.
2. Kate Mooney & Chiara Repetti-Ludlow (2021), “Sonority and syllable structure: The case of Burmese tone,” *Proceedings of the Linguistic Society of America* 6(1), 24–38, DOI [10.3765/plsa.v6i1.4900](https://doi.org/10.3765/plsa.v6i1.4900). [Open article, CC BY 4.0](https://journals.linguisticsociety.org/proceedings/index.php/PLSA/article/view/4900). Their analysis argues that some vowel alternations are tone-independent and conditioned by sonority sequencing; it challenges a simplistic direct tone-to-vowel mapping.
3. Unicode 17 Chapter 16 documents Myanmar encoding, kinzi and medial ya/ra/wa/ha ordering. It is authoritative for code-point and orthographic structure, not for the phonological value of every sequence. [Unicode Chapter 16](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-16/).
4. [Watkins-based Burmese consonant/voicing description](https://www.degruyterbrill.com/document/doi/10.1515/phon-2022-0026/html) reports contrastive voicing among sonorants and a four-tone analysis. [Hill (2012), “Evolution of the Burmese Vowel System”](https://doi.org/10.1111/j.1467-968X.2011.01282.x) provides historical context, not a direct modern synchronic G2P rule.
5. The current myG2P v2.0 probe is temporary test material only; it is not gold and its CC BY-NC-SA 4.0 terms do not authorize inclusion in the product corpus.

## Required research matrix

| Workstream | Required matrix | Acceptance evidence |
|---|---|---|
| Orthographic structure | Kinzi × base consonant × subscript/stacking × medials × vowel marks × asat/virama | Unicode sequence and rendering tested separately from linguistic syllable segmentation |
| Onsets/medials | Base consonant × medial ya/ra/wa/ha × legal cluster restrictions | Source-backed phonemic analysis and narrow phonetic realization |
| Vowels | Vowel sign sequence × open/nasal/checked coda × tone/phonation × major/minor syllable | Separate underlying vowel category, surface quality, nasalization, diphthongization and duration |
| Checked syllables | Stop/glottal closure × vowel realization × phonation × f0 contour | Distinguish segmental /ʔ/ or historical stop reflex from suprasegmental creak |
| Tone/register/phonation | Low/high/creaky/checked/killed labels × acoustic cues × profile | Literature conflict table, explicit terminology mapping, speaker-level acoustic evidence |
| Ukrainian adapter | Typed IPA segment sequence × tone/phonation metadata × Ukrainian practical output | No loss of source distinction before an explicit target policy; uncertain cases fail closed |

## Highest-risk questions

1. Is “checked” represented as a coda /ʔ/, a laryngealized vowel, a tone class, or a combination in each cited analysis? Do not collapse these levels.
2. Which vowel alternations follow coda/sonority rather than tone? Mooney & Repetti-Ludlow (2021) directly warn against conflating the two.
3. How do phonemic vowel categories differ from surface diphthongs, nasalization and predictable duration in open vs closed syllables?
4. What is the precise permitted order and interpretation of kinzi, medials, vowel marks, asat and virama? Unicode's encoding order is not a phonemic transcription.
5. Which C+glide sequences are prohibited, and does the current structural parser incorrectly accept/reject any?
6. How should voiced/voiceless sonorants and breathy/creaky phonation be carried into typed IPA without confusing them with tone?

## Execution order

- [ ] Map current parser behavior against Unicode 17 Table 16-4 and add adversarial orthographic sequence fixtures.
- [ ] Build a source-backed consonant/medial inventory and prohibited-cluster table.
- [ ] Reconcile Green (1995), Mooney & Repetti-Ludlow (2021), Watkins and current phonetic studies in a terminology matrix.
- [ ] Complete vowel × coda × major/minor × tone/phonation coverage, with separate phonemic and phonetic columns.
- [ ] Record audio/elicitation with profile, speaker, style and rights metadata; independently annotate IPA and acoustic cues.
- [ ] Adjudicate the relationship between checked coda, glottalization, creaky phonation and tone before changing the runtime.
- [ ] Implement the IPA → Ukrainian adapter only from adjudicated typed IPA, with a distinct orthographic MLCTS route if required.

**Current status:** PARTIAL. Unicode orthographic decomposition exists, but full phonological vowel/coda/tone/phonation coverage and Python/browser phonological parity remain open. Independent gold remains 0. No new Burmese IPA labels are added in this workpack.


## Verified phonological evidence audit — 2026-11-01

### Syllable, vowel and coda restrictions

Antony Green's “Word, Foot, and Syllable Structure in Burmese” (revised from the 1995 Cornell Working Papers article; [full text](https://roa.rutgers.edu/files/551-1002/551-1002-GREEN-0-1.PDF)) provides a detailed, inspectable analysis:

- Major syllables have an obligatory onset and a rhyme; Green lists 50 major-syllable rhymes and analyzes the structure as C(G)V((V)C). Diphthongs do not occur in open syllables.
- The diphthongs /ei, ai, ou, au/ require a placeless coda /ʔ/ or /N/ in the analysis; mid monophthongs /e, o, ə/ occur only in open syllables; /ə/ has its own restricted distribution.
- Vowel length is not contrastive in Green's account. Major syllables are bimoraic; open vowels may carry the two moras, while in closed syllables the vowel and coda each support one. Rhyme duration varies substantially by tone category.
- Green describes four categories in major syllables (low, high, creaky, checked); only low, high and creaky are possible with nasal rhymes. Checked and nasal coda structures cannot simply be combined as an unrestricted cross-product.
- Minor syllables contain schwa only, are open and toneless, have a simple onset, and cannot be word-final. Do not assign them a major-syllable tone.

These are Green's analysis and transcription conventions, not a universal merged consensus. Preserve source ID, profile, transcription convention and conflicting analyses for each rule.

### Independent challenge to tone-driven vowel rules

Mooney & Repetti-Ludlow (2021), [open CC BY 4.0 article](https://doi.org/10.3765/plsa.v6i1.4900), report a phonetic study of Burmese vowel alternations and argue that the alternations are tone-independent and follow sonority sequencing preferences. This directly challenges a simplistic rule that derives vowel quality from tone alone. The vowel × coda × syllable-weight matrix must encode these environments separately.

### Newer register/tone proposal — unresolved

Duan & Zhu (2025), [publisher record and abstract](https://doi.org/10.1075/lali.00203.dua), propose eight tones divided across modal and lower/breathy registers, splitting the traditional four categories into eight. The publisher abstract confirms this is a peer-reviewed competing analysis, but the full article and its underlying acoustic data have not been independently inspected in this checkpoint. Treat it as a live research hypothesis, not an implemented model or a reason to replace Green's four-way account.

### Phonation of sonorant consonants is not vowel register

Repetti-Ludlow (2023), *Phonetica* 80(6):433–463, [DOI](https://doi.org/10.1515/phon-2022-0026), finds that Burmese voiceless sonorants have a spread-glottis period with turbulent airflow in 78% of tokens; duration, F0 and following-vowel excitation also distinguish voiced and voiceless sonorants. Keep consonantal aspiration/voicelessness distinct from breathy or creaky vowel phonation and from lexical tone.

### Orthographic medials

Unicode and LREC 2020 establish the script-level facts: consonants can be stacked using virama; dependent vowels and tone signs surround consonants; asat suppresses the inherent vowel in certain coda contexts. These are orthographic/encoding facts, not a one-to-one phonological inventory. The written medial ya/ra/wa/ha categories must be mapped separately to modern phonemic onsets, glides, historical correspondences or other effects by source and variety. Green's C(G)V analysis supports glide-bearing onsets in his model, but it does not justify treating every written medial as an independent /j/ or /w/ segment.

**Research acceptance matrix:** record for each row (1) orthographic sequence, (2) structural parse, (3) phonemic analysis, (4) phonetic realization, (5) tone/register/phonation convention, (6) profile/speaker, (7) source locator and confidence. Keep Green's four-tone model, Duan & Zhu's eight-tone proposal and any future speaker-level analysis in separate columns until adjudicated.

**Status update:** vowel/coda and major/minor constraints are now more explicitly source-grounded; the complete lexical matrix, modern medial correspondence table, checked-syllable phonetic adjudication and competing register analyses remain PARTIAL/BLOCKED. No new IPA labels or automatic phonological rules were added.
