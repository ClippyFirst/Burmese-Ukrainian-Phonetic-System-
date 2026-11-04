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


## Test-only Goruut runtime evaluation

Added an optional, test-only HTTP runtime probe for Goruut at pinned upstream commit `b224bde02151f8f86d0fe260804e4ca743bda620`. It explicitly enables `Burmese` in `BuiltinDictLanguages`, builds the upstream Go binary and records raw JSON responses for six existing structural probes plus sentence/punctuation cases. `scripts/benchmark_goruut.py` records commit, language, input SHA-256, raw response, tokens and errors; no IPA normalization or accuracy scoring occurs. Structural probes are not phonological gold. Accuracy=null; independent gold=0. Workflow: `.github/workflows/optional-goruut-runtime.yml`; artifact retention 30 days.

The earlier asset-license blocker applies to copying, redistribution and production integration. The owner has authorized use for testing only; therefore the optional CI probe may check out and execute the pinned upstream source transiently. It does not persist upstream assets, does not bundle them, and does not approve a production dependency. Linguistic gold and accuracy remain unestablished.


## Goruut runtime evidence update — 2026-11-01

The pinned Goruut runtime was executed with Burmese enabled (Go 1.23.12). Seven of eight probes returned phonetic tokens; the Burmese-punctuation sentence `ကေ၊ ကော်။` returned no phonetic output. Raw tokens such as `kè`, `kɔ̀`, `tɕì`, `swɛ̀`, `mjàɴ`, `jù` are preserved but not validated against an independent Burmese IPA set. Server log repeatedly reports missing `weights9.bin.zlib`. Do not promote. Full evidence: `docs/audits/current/GORUUT-RUNTIME-EVALUATION-2026-11-01.md`.

Testing-only owner authorization was used to execute the pinned upstream source in ephemeral CI. No external asset was copied into the repository or production artifact. Full report: `docs/audits/current/GORUUT-RUNTIME-EVALUATION-2026-11-01.md`.


## Repeatability findings — 2026-11-01

Three-repeat re-evaluation: 7/8 probe inputs returned usable output and all 7 were stable across three repetitions; Burmese punctuation sentence `ကေ၊ ကော်။` returned no output in all three. This establishes limited repeatability, not IPA accuracy.

The three-repeat raw outputs are preserved in workflow artifacts and summarized in `docs/audits/current/GORUUT-RUNTIME-EVALUATION-2026-11-01.md`. Do not treat these results as gold or as a production approval.


## Cross-engine comparison update

Cross-engine check: Epitran 1.35.3 returned 6/6 raw outputs; Goruut returned 7/8 usable probes and failed the Burmese punctuation sentence. Exact string agreement between Epitran and Goruut was 0/6. Epitran is largely tone-less in these examples while Goruut emits tone-marked strings; without a common IPA convention and expert gold this is disagreement, not an accuracy ranking. Latest Goruut run had 7 stable usable outputs; a prior run showed one unstable `ကြည်` output.


## Burmese corpus/G2P source-level clarification — 2026-11-03

- Oo et al. (2020), [Burmese Speech Corpus, Finite-State Text Normalization and Pronunciation Grammars with an Application to Text-to-Speech](https://aclanthology.org/2020.lrec-1.777): 2,528 utterances, 20 female Yangon speakers, 22,443 word tokens and 9,941 unique words. The speech corpus is CC BY-SA 4.0. The Thrax/WFST pronunciation grammar is a separate artifact; its license must be checked separately. The released corpus is orthographic speech/text, not IPA gold, and no public benchmark split is established by the paper.
- Thu et al. (2016), [Comparison of Grapheme-to-Phoneme Conversion Methods on a Myanmar Pronunciation Dictionary](https://aclanthology.org/W16-3702): 25,300 MLC dictionary entries, 25,000 train and three 100-word open test sets; reports PER on its own romanized phoneme inventory. It does not document independent IPA adjudication or a project-compatible IPA convention; the dictionary's redistribution license is not established by the paper.
- Hlaing & Mikami (2013; published online 2014), [Automatic syllable segmentation of Myanmar texts using finite state transducer](https://doi.org/10.4038/ICTER.V6I2.7150): 11,732 orthographic words and 99.93% word-syllabification accuracy from a rule-based FST; the table reports 245/253 consonant-stacking words correct (96.83%); the text also discusses a free-standing-vowel error. This is orthographic segmentation, not G2P/IPA accuracy.

No rows/models imported. These resources are structural or external G2P comparators only; independent expert IPA gold remains 0 and accuracy null.


## Burmese Wiktionary license provenance — verified source separation (2026-11-04)

The dataset-card declaration and upstream content policy are now registered as two distinct sources in `data/burmese/sources.csv`, with separate claims in `data/burmese/source_claims.csv` (PR #111, merged at `8c323ff0d1236c5c6d36b2c2be0eac4d493163ab`):

- `MYWIKTIONARY2026`: the cleaned dataset card declares CC BY 4.0 and reports 22,191 word-POS rows, 20,759 unique headwords and 113 IPA values (0.51%).
- `MYWIKTIONARYPOLICY2024`: the Myanmar Wiktionary local policy, last edited 2024-12-06, states CC BY-SA 3.0 Unported and GFDL.

These are documentary facts from different sources, not a legal resolution. The extracted dataset's rights remain `CONFLICT/UNKNOWN`; no rows were imported. The sparse IPA values have no per-entry dialect/convention, audio, detailed source locator, annotator or adjudication metadata. Full MLCTS coverage is not IPA coverage. Do not use the 113 values as gold or train on the extracted dataset until the publisher/rightsholder clarifies the rights and the items pass profile/provenance review.


## Additional Burmese pronunciation and audio source verification — 2026-11-04

### myG2P Version 2.0 — pinned IPA-bearing dictionary

**Disposition: highest-value external lexical comparator found; restricted to non-commercial/share-alike terms; NOT project gold.**

- Upstream repository: https://github.com/ye-kyaw-thu/myG2P
- Pinned inspected revision: `54b5c76bb5a87fdbaaeddc1892e6ebd8f97ee225` (2026-09-02).
- Version 2.0 dictionary file: `ver2/myg2p.ver2.0.txt` (2,329,808 bytes at the inspected tree).
- README documents five tab-separated fields: Word-ID, orthography, syllable-broken word, pronunciation respelling and IPA. It says the dictionary is based mainly on Myanmar Language Commission dictionary words and includes context-dependent pronunciations and foreign-word extensions.
- The README explicitly declares **CC BY-NC-SA 4.0** and asks users to cite the ICCA 2015 / COLING 2016 papers. It lists contributors and acknowledges named researchers who checked G2P mappings.
- This strengthens provenance and artifact pinning compared with the earlier generic myG2P reference. It does not provide a project-compatible dialect/IPA convention for every row, a per-entry audio locator, two independent IPA annotations plus separate adjudication, or permission for commercial use.
- The existing project runtime probe is a diagnostic comparator only. Stable engine output or source dictionary IPA must not be counted as project gold or used to claim model accuracy.

**Acceptance before any wider use:** retain the pinned commit and exact file SHA-256; confirm whether project testing/research purposes fit the non-commercial grant; document attribution/share-alike obligations; audit all five columns and IPA conventions; map a stratified subset to primary locators and dialect profile; obtain independent specialist double annotation and adjudication. Do not use the corpus in a commercial or unrestricted redistribution path without separate permission.

### OpenSLR SLR80 — Burmese speech audio and orthographic transcripts

- Provider record: https://www.openslr.org/80/
- The provider lists **CC BY-SA 4.0** and describes manually quality-checked volunteer recordings of Burmese sentences with anonymized file IDs and orthographic transcripts; it cautions that errors may remain.
- The currently visible female subset lists `line_index_female.tsv` (541 KB) and `my_mm_female.zip` (948 MB). The listing does not establish a full dialect/age profile for these files and supplies no IPA labels.
- This is a possible audio source for a carefully scoped human annotation pilot, not a pronunciation dictionary or gold set. The text is sentence-level and the visible subset is female-only; do not infer that it covers all Burmese speakers or all Yangon/standard varieties.
- CC BY-SA 4.0 attribution and share-alike conditions apply to the licensed dataset; assess publication of derived annotations before sharing. Preserve provider file IDs and timestamps; do not attempt to identify speakers or mirror files beyond the provider's terms.

### Evidence decision

The new records `MYG2P2026` and `OPENSLR80` are now registered in `data/burmese/sources.csv`; documentary claims are separately registered in `data/burmese/source_claims.csv`. No third-party dictionary or audio was copied. The only approved use status remains the previously documented test-only diagnostic use; this source audit does not grant any new production, redistribution or commercial permission.

Independent expert-adjudicated Burmese IPA gold remains **0**; empirical accuracy remains **null**.
