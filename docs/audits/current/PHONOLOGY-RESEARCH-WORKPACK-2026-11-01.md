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
