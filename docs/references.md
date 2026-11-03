# References and evidence hierarchy

## Primary and authoritative sources

### Burmese script and Unicode

- Unicode Consortium. Unicode Standard, Chapter 16: Myanmar.
- Unicode Consortium. Unicode Technical Note #11, Representing Myanmar in Unicode.

These sources are authoritative for Unicode encoding, code-point behaviour,
canonical ordering and script mechanics. They are not treated as automatic
authority for every phonological interpretation.

### Burmese phonology

- Green, Anthony. 2002. *Word, Foot, and Syllable Structure in Burmese.*
- Mooney, Kate; Repetti-Ludlow, Chiara. 2021. *Sonority and syllable
  structure: The case of Burmese tone.*
- Duan, Haifeng; Zhu, Xiaonong. 2025. *Double registers and eight tones in
  Burmese.*
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


### External G2P and speech-resource references

- Kyaw Thu, Ye; Pa Pa, Win; Sagisaka, Yoshinori; Iwahashi, Naoto. 2016.
  *Comparison of Grapheme-to-Phoneme Conversion Methods on a Myanmar
  Pronunciation Dictionary.* Proceedings of the 6th Workshop on South and
  Southeast Asian Natural Language Processing (WSSANLP2016), 11–22.
  https://aclanthology.org/W16-3702/. This is a historical G2P comparator
  using a romanized phoneme inventory; it is not project IPA gold, and the
  paper citation does not establish redistribution rights for the MLC
  dictionary.

- Oo, Yin May; Wattanavekin, Theeraphol; Li, Chenfang; De Silva, Pasindu;
  Sarin, Supheakmungkol; Pipatsrisawat, Knot; Jansche, Martin; Kjartansson,
  Oddur; Gutkin, Alexander. 2020. *Burmese Speech Corpus, Finite-State Text
  Normalization and Pronunciation Grammars with an Application to
  Text-to-Speech.* Proceedings of the Twelfth Language Resources and
  Evaluation Conference, 6328–6339.
  https://aclanthology.org/2020.lrec-1.777/. The article describes public
  speech and FST/G2P resources, but any in-house or third-party resource must
  retain its own rights and provenance; the paper's licence does not
  automatically cover every referenced dataset.
