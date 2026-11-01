# External phonetic corpus/source triage — Burmese — 2026-11-01

## Candidate sources and disposition

### myG2P — rich IPA dictionary, non-commercial terms

- Source: https://github.com/ye-kyaw-thu/myG2P
- README explicitly states CC BY-NC-SA 4.0 and describes a Myanmar Language Commission pronunciation dictionary extended with foreign pronunciations. It provides syllable-broken orthography and IPA examples.
- The non-commercial restriction means this is not cleared for commercial use/redistribution without separate permission. The repository metadata itself does not declare a standard SPDX license. Keep the previously recorded BLOCKED status; do not import its data or derived model.

### Burmese Wiktionary cleaned lexicon — useful MLCTS crosswalk, not an IPA gold corpus

- Dataset card: https://huggingface.co/datasets/its-autumn/burmese-wiktionary
- It reports 22,191 words and CC BY 4.0, with full MLCTS coverage but IPA in only 113 entries (about 0.51%). The dataset is extracted from a 2026-08-01 Myanmar Wiktionary dump.
- Potential use: investigate the MLCTS/orthography crosswalk and source locators. The sparse IPA subset is too small and too source-dependent to establish broad phonetic accuracy. Independently verify the card's license/provenance and retain Wiktionary attribution before any import.

### OpenSLR SLR80 — licensed speech, not IPA labels

- Resource: https://openslr.org/80/
- Burmese recordings and manually quality-checked text transcripts are published under CC BY-SA 4.0.
- This can support a future audio-backed adjudication set, but transcripts alone are not IPA. Expert phonetic transcription, speaker/dialect metadata, audio-level rights review and independent double annotation remain required. Share-alike obligations must be assessed before publishing derived labels.

### Myanmar Open Wordnet and SEAlang

- Myanmar Open Wordnet is CC BY 4.0, but it is a small semantic lexicon (about 1,041 words), not a pronunciation/IPA corpus: https://wordnet.burmese.sg/
- SHACHI metadata for the SEAlang Burmese Dictionary identifies the source as the 1993 Myanmar Language Commission dictionary republished by Dunwoody Press and says source material is copyrighted; it was used with permission. Do not scrape or redistribute its pronunciation data without verifying that permission extends to this project: https://shachi.org/resources/3949

### Mya2Rom

- Repository: https://github.com/myanmaropenwordnet/mya2rom
- GitHub metadata reports CC BY-SA 4.0. Its modes include IPA, MLCTS and simplified romanization, but the README traces rules to Wikipedia/Wiktionary and describes the simplified systems as works in progress.
- Treat it as a rule-based comparator and provenance lead, not an independently adjudicated gold source. Its orthographic MLCTS output must remain distinct from IPA and from Ukrainian transcription.

## Benchmark implication

There is no verified, openly reusable, independently adjudicated Burmese IPA gold corpus in the inspected sources. The candidate resources are complementary but not interchangeable: IPA dictionary (myG2P, non-commercial), MLCTS-heavy Wiktionary lexicon (very sparse IPA), audio/transcript corpus (OpenSLR, needs phonetic annotation), semantic WordNet, and rule-based transcription (Mya2Rom).

## Acceptance before use

1. Confirm per-resource license, provenance, attribution and share-alike/non-commercial constraints.
2. For OpenSLR, create a small dialect-labelled audio sample and commission two independent IPA transcriptions plus adjudication; record audio IDs and timestamp spans.
3. For Wiktionary, import only source-located entries, preserve MLCTS and IPA as separate typed fields, and do not treat missing IPA as inferable.
4. Keep myG2P blocked for commercial use absent written permission.
5. Require independent expert review of tone, register, phonation, syllable boundaries, medials and codas before scoring.

Current independent, project-owned, expert-adjudicated Burmese IPA gold remains 0.
