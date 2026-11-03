# References and evidence hierarchy

## Primary and authoritative sources

### Burmese script and Unicode

- Unicode Consortium. Unicode Standard, Chapter 16: Myanmar.
- Unicode Consortium. Unicode Technical Note #11, Representing Myanmar in Unicode.

These sources are authoritative for Unicode encoding, code-point behavior,
canonical ordering and script mechanics. They are not treated as automatic
authority for every phonological interpretation.

### Burmese phonology

- Green, Antony Dubach. 2002. *Word, Foot, and Syllable Structure in Burmese.* Rutgers Optimality Archive 551 (October 2002). [Working-paper PDF](https://roa.rutgers.edu/files/551-1002/551-1002-GREEN-0-0.PDF).
- Hlaing, Tin Htay & Yoshiki Mikami. 2013 (published online 2014). “Automatic Syllable Segmentation of Myanmar Texts using Finite State Transducer.” *The International Journal on Advances in ICT for Emerging Regions* 6(2). DOI: [10.4038/ICTER.V6I2.7150](https://doi.org/10.4038/ICTER.V6I2.7150). Orthographic syllabification only; not G2P or IPA evaluation.
- Ye Kyaw Thu, Win Pa Pa, Yoshinori Sagisaka & Naoto Iwahashi. 2016. “Comparison of Grapheme-to-Phoneme Conversion Methods on a Myanmar Pronunciation Dictionary.” *Proceedings of the 6th Workshop on South and Southeast Asian Natural Language Processing (WSSANLP2016)*, 11–22. [ACL Anthology W16-3702](https://aclanthology.org/W16-3702/). Its PER is defined on the paper's romanized phoneme inventory, not project IPA gold.
- Oo, Yin May; Wattanavekin, Theeraphol; Li, Chenfang; De Silva, Pasindu; Sarin, Supheakmungkol; Pipatsrisawat, Knot; Jansche, Martin; Kjartansson, Oddur; Gutkin, Alexander. 2020. “Burmese Speech Corpus, Finite-State Text Normalization and Pronunciation Grammars with an Application to Text-to-Speech.” *Proceedings of the Twelfth Language Resources and Evaluation Conference*, 6328–6339. [ACL Anthology 2020.lrec-1.777](https://aclanthology.org/2020.lrec-1.777/). The paper describes an open-source speech corpus and finite-state text-normalization/G2P grammars; the G2P outputs and orthographic transcripts are not independent IPA gold.
- Mooney, Kate & Chiara Repetti-Ludlow. 2021. “Sonority and Syllable Structure: The Case of Burmese Tone.” *Proceedings of the Linguistic Society of America* 6(1): 24–38. [DOI: 10.3765/plsa.v6i1.4900](https://doi.org/10.3765/plsa.v6i1.4900).
- Duan, Haifeng; Zhu, Xiaonong. 2025. “Double registers and eight tones in
  Burmese: From the perspective of The Syllabic Phonology and tono-typology.”
  *Language and Linguistics* 26(3): 387–430. DOI: [10.1075/lali.00203.dua](https://doi.org/10.1075/lali.00203.dua).
- Tun, Than Naing et al. 2011. *Myanmar text-to-speech system with rule-based
  tone synthesis.*

These sources are used for competing phonological/prosodic analyses. The
repository does not collapse disagreement into a single unsupported consensus.

### Russian Burmese practical transcription

- Epstein, V. G. 1959. *Rules of Russian Transcription of Burmese
  Geographical Names.* Institute of Oriental Studies, USSR Academy of
  Sciences, 56 pp. The bibliographic record states that the rules are detailed
  and can also be applied to personal names and other terms.
- Chief Administration of Geodesy and Cartography, USSR. 1978.
  *Инструкция по русской передаче географических названий Бирмы.* Moscow:
  Nauka, 60 pp.

The Russian material is documentary control evidence. It is not treated as the
source of truth for Ukrainian output.

### Ukrainian target orthography

- National Commission on State Language Standards. 2026. *Український
  правопис* as the state-language standard, decision No. 47 of 2026-03-01,
  effective 2026-03-28.
- The 2019 orthographic edition remains in the repository only as historical
  provenance.

## Evidence status policy

Every important statement must be distinguishable as one of:

- established fact;
- well-supported synthesis;
- analysis-dependent interpretation;
- project design decision;
- uncertain or unresolved claim.

The repository must never promote a project-specific correspondence to an
official Ukrainian norm merely because it appears in a machine-readable table.

## Historical lead

A 1958 Epstein bibliographic lead concerning Burmese proper-name transcription
is retained in the source registry. Its article-level record was not
independently verified during the 2026-10-05 audit, so it is marked UNCERTAIN.
