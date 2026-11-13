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
- Historical note only: transcripts are not IPA. The resource is excluded from active text-only scope; no recording access, audio review or audio-based annotation is planned. Share-alike obligations must be assessed before publishing derived labels.

### Myanmar Open Wordnet and SEAlang

- Myanmar Open Wordnet is CC BY 4.0, but it is a small semantic lexicon (about 1,041 words), not a pronunciation/IPA corpus: https://wordnet.burmese.sg/
- SHACHI metadata for the SEAlang Burmese Dictionary identifies the source as the 1993 Myanmar Language Commission dictionary republished by Dunwoody Press and says source material is copyrighted; it was used with permission. Do not scrape or redistribute its pronunciation data without verifying that permission extends to this project: https://shachi.org/resources/3949

### Mya2Rom

- Repository: https://github.com/myanmaropenwordnet/mya2rom
- GitHub metadata reports CC BY-SA 4.0. Its modes include IPA, MLCTS and simplified romanization, but the README traces rules to Wikipedia/Wiktionary and describes the simplified systems as works in progress.
- Treat it as a rule-based comparator and provenance lead, not an independently adjudicated gold source. Its orthographic MLCTS output must remain distinct from IPA and from Ukrainian transcription.

## Benchmark implication

There is no verified, openly reusable, independently adjudicated Burmese IPA gold corpus in the inspected written sources. The candidate resources are complementary but not interchangeable: myG2P (non-commercial IPA source), MLCTS-heavy Wiktionary lexicon (very sparse IPA), text corpora, semantic WordNet, and rule-based transcription (Mya2Rom). OpenSLR is historical metadata only and excluded from active work.

## Acceptance before use

1. Confirm per-resource license, provenance, attribution and share-alike/non-commercial constraints.
2. OpenSLR is excluded from current scope. Build any future gold only from source-located written IPA/dictionary examples and independent expert review.
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
- Version 2.0 dictionary file: `ver2/myg2p.ver2.0.txt` (2,329,808 bytes; Git blob SHA `0b2735f9a6f7fe28ae94c4baaf323d1db3015c3b` at the pinned revision).
- README documents five tab-separated fields: Word-ID, orthography, syllable-broken word, pronunciation respelling and IPA. It says the dictionary is based mainly on Myanmar Language Commission dictionary words and includes context-dependent pronunciations and foreign-word extensions.
- The README explicitly declares **CC BY-NC-SA 4.0** and asks users to cite the ICCA 2015 / COLING 2016 papers. It lists contributors and acknowledges named researchers who checked G2P mappings.
- This strengthens provenance and artifact pinning compared with the earlier generic myG2P reference. It does not provide a project-compatible dialect/IPA convention for every row, a per-entry audio locator, two independent IPA annotations plus separate adjudication, or permission for commercial use.
- The existing project runtime probe is a diagnostic comparator only. Stable engine output or source dictionary IPA must not be counted as project gold or used to claim model accuracy.

**Acceptance before any wider use:** retain the pinned commit and exact file SHA-256; confirm whether project testing/research purposes fit the non-commercial grant; document attribution/share-alike obligations; audit all five columns and IPA conventions; map a stratified subset to primary locators and dialect profile; obtain independent specialist double annotation and adjudication. Do not use the corpus in a commercial or unrestricted redistribution path without separate permission.

### OpenSLR SLR80 — historical metadata only; excluded from active text-only scope

- Provider record: https://www.openslr.org/80/
- The provider lists **CC BY-SA 4.0** and describes manually quality-checked volunteer recordings of Burmese sentences with anonymized file IDs and orthographic transcripts; it cautions that errors may remain.
- The currently visible female subset lists `line_index_female.tsv` (541 KB) and `my_mm_female.zip` (948 MB). The listing does not establish a full dialect/age profile for these files and supplies no IPA labels.
- Historical audit record only. This resource is not a pronunciation dictionary or gold set and is excluded from active text-only work; no recordings are accessed or used.
- CC BY-SA 4.0 attribution and share-alike conditions apply to the licensed dataset; assess publication of derived annotations before sharing. Preserve provider file IDs and timestamps; do not attempt to identify speakers or mirror files beyond the provider's terms.

### Evidence decision

The records MYG2P2026 and OPENSLR80 remain registered for provenance. OPENSLR80 is historical metadata only and excluded from active scope. No third-party dictionary or corpus rows were copied; no new production or redistribution permission is inferred.

Independent expert-adjudicated Burmese IPA gold remains **0**; empirical accuracy remains **null**.


## Additional G2P/phonology diagnostics — 2026-11-13

- Google Thrax grammar at pinned commit a90601024f07ab7e96c911243324e0adeb16da96 is Apache-2.0; its output for မြန် is m j àɴ, but the structural probe has no gold.
- Epitran 1.35.3 returns məjaɴ for the same probe; zero gold and null accuracy. The disagreement is useful for prioritizing expert annotation, not for selecting a winner.
- CRFsuite v2 returns 84/100 source-concordant outputs on a 100-row sample of myG2P v2.0, with overlapping medial subsets YA 10/14, RA 17/20, WA 13/15, HA 7/8. The sample has no gold and the target မြန် is absent; possible train/test overlap remains.
- SLR80 was previously reviewed but is excluded from active scope. myG2P remains CC BY-NC-SA 4.0 and is not commercially cleared. No candidate is an independent gold corpus.


### UCSY-SC1 (Mon, Pa Pa & Thu 2019): historical metadata only; excluded from active scope

- The paper describes 42 h 39 min of 16 kHz mono speech from 307 speakers: 25 h 20 min web news and 17 h 19 min recorded conversation; 31,114 utterances and 11,696 unique words are reported.
- It states 33 basic consonants, 12 vowels and four medials, and describes nasalized vowels. This is useful as a published inventory and acoustic-corpus lead.
- Historical rights metadata only. UCSY-SC1 is excluded from active text-only scope; no corpus access, audio review or derived labels are planned.
- If access and rights are secured, prioritize speaker-disjoint annotation of medial YA/RA/WA/HA, coda types, tone/register and nasalization. Keep web-news and recorded-conversation domains separate.

## Text-only resource review and scope correction — 2026-11-13

This continuation follows the explicit project direction to use **text sources only**. Audio recordings, speech corpora, audio annotation, speaker diarization and audio-derived gold labels are out of scope for this work. Earlier SLR80/UCSY-SC1 notes remain historical source metadata only; they are not next-step recommendations and no audio is to be acquired, processed or annotated.

### myX Myanglish corpus — text-based romanization diagnostic only

- Resource: https://huggingface.co/datasets/DatarrX/myX-myanmar-to-myanglish-corpus
- Dataset viewer reports 2,121 rows and exposes Burmese Unicode (myanmar), informal Latin (myanglish) and official_standard columns. The README's schema description lists only myanmar and myanglish, so the third-column discrepancy must be resolved against the raw CSV before any ingestion.
- The dataset card explicitly says Myanglish has no standardized orthography and that the current batch is predominantly curated in one native author's personal typing/phonetic style. This is not a representative community-wide romanization standard.
- The target is romanized phonetic text, not IPA. It may be a useful diagnostic crosswalk for source-text-to-Latin variants and for identifying contextual/colloquial spellings, but it cannot validate the project's IPA layer or serve as independent pronunciation gold.
- The card declares CC BY-SA 4.0. Record attribution and share-alike obligations; do not copy rows into project tests or generated assets until row-level review, schema reconciliation and license compatibility are completed.
- Disposition: **PARTIAL / candidate only** for romanization research; **NOT GOLD** for IPA/G2P evaluation.

### myX Myanmar Orthography Error Correction Corpus — orthographic text only

- Resource: https://huggingface.co/datasets/DatarrX/myX-myanmar-orthography-corpus
- Dataset viewer reports 4,800 rows. The documented parallel schema is noisy_sentence, correct_sentence, error_category, and target_words; the corpus is a work in progress and the card declares CC BY-SA 4.0.
- Filenames containing phonetic and the Phonetic Confusion category refer to spelling/lexical confusion examples, not IPA transcription. The inspected phet_bet_phonetic.csv has only the four orthographic-correction columns and no phonetic/IPA target field.
- The README says future releases may add medial contrasts such as ကျ vs ကြ; that is a roadmap statement, not evidence that the current release contains an adjudicated medial dataset.
- Disposition: candidate for future text-normalization/orthographic regression tests after row-level quality review; not a phonological or IPA corpus. No rows imported.

### A Corpus of Modern Burmese — text corpus, rights unresolved

- Resource: https://zenodo.org/records/1202324; DOI 10.5281/zenodo.1202324.
- Zenodo describes John Okell's corpus as compiled in the 1990s, converted to Unicode and distributed as an 8.8 MB allfiles.txt file. The Zenodo record's Rights/License field is blank, while European Language Grid catalogue record 940 lists CC BY 4.0.
- The project owner has confirmed that required permissions for text-only research use and project ingestion are in place. The metadata discrepancy remains recorded for provenance and downstream publication, but it is no longer a research-permission blocker.
- Current operational blocker: the 8.8 MB text file exceeds the web preview limit and this runtime could not download it (container DNS/network unavailable; GitHub connector only fetches GitHub-hosted UTF-8 text). No text has yet been imported or counted.
- Disposition: **AUTHORIZED_FOR_RESEARCH; BLOCKED_TOOL_ACCESS** until the corpus bytes can be obtained in this execution environment; not an IPA corpus.

### Text-only policy and corpus gate

1. Only written dictionaries, lexical databases, published phonological descriptions, written examples, romanization tables, and text corpora may be newly researched or considered for ingestion.
2. Keep source orthography, MLCTS, informal romanization, IPA and Ukrainian output in separate fields and contracts. A romanized text target is not automatically IPA.
3. Every corpus candidate needs a visible schema, provenance, version/hash, declared license and scope statement. Single-author or non-standardized romanization must be labelled as such.
4. No audio-derived acceptance criteria or annotation steps are part of the current plan. Existing audio references are historical exclusions, not blockers for this text-only continuation.
5. Independent expert-adjudicated IPA gold remains **0**; empirical accuracy remains **null**. Textual lexical evidence can improve coverage, but it does not create an acoustic gold set.

### SEAlang Burmese dictionary and corpora — text-only candidates

- Dictionary metadata: approximately 35,000 entries, spoken and literary styles, MLC 1986 orthography, examples/etymologies; based on the MLC 1993 Myanmar-English Dictionary (1996 Dunwoody reprint), used by SEAlang with permission.
- Transcription ambiguity: SHACHI describes IPA search/display, while Mya2Rom documentation says MLCTS2 is used by the MLC dictionary and SEAlang. The SEAlang page could not be inspected because it timed out/returned gateway errors. Do not assume the entry transcription is IPA.
- Rights: the project owner confirms all necessary permissions for research use and project ingestion. This is a project-specific authorization, distinct from the public metadata and underlying source copyright statements. No rows were extracted in this pass.
- Burmese Text Corpus: monolingual Internet texts; metadata shows 612,692 collocates and 3,172,485 contexts served, not verified dataset row/token counts. Metadata carries a 2007 NICT/Matsubara Lab/Anchor copyright notice.
- Burmese Bitext Corpus: translated words/phrases/sentences, aligned sentence-by-sentence where possible; 1,234,822 pairs served, not verified total size; source SAY Project Burmese resources (NMSU CRL); metadata carries the same 2007 copyright notice.
- The project owner confirms permissions for research use and project ingestion of these textual resources. Their actual corpus rows and dictionary entries were not accessed in this pass; stable retrieval and schema inspection are still required.
- Disposition: authorized candidate for written lexical/context and orthographic coverage research; **BLOCKED_TOOL_ACCESS_AND_SCHEMA** until stable record retrieval and field semantics are inspected; neither text corpus provides IPA gold.



## Text-only permission and data-quality update — 2026-11-13

### Research-use authorization

The project owner has confirmed that all required permissions for text-only research use and project ingestion of the listed textual resources are in place. Therefore, rights uncertainty in public catalogue metadata is no longer treated as a blocker to research processing or internal project ingestion. Public source metadata is retained accurately; this project-specific authorization does not rewrite the original public license fields. No audio resources are in scope.

### Nishi (1998) — full-text inspection and source-faithful evidence

The complete repository-hosted PDF was inspected, not just its abstract. It provides:
- first sandhi pattern: an atonic syllable around /a/ followed by an eligible unaspirated stop, affricate or sibilant; both eligible consonants may be voiced;
- second sandhi pattern: an eligible following onset becomes voiced after a non-stop tonal rhyme in close juncture;
- multiple examples on pp.253–254;
- explicit non-obligatoriness, exceptions, optional atonicization and dialect/subvariety differences;
- a four-stage historical account involving three voicing rules plus atonicization, explicitly an explanatory historical proposal.

Nishi states that slash-delimited phonemic transcription follows Okell 1995 and that Written Burmese forms in braces use a modified Duroiselle transliteration. These source phonemic forms are **not project IPA**. Seven source-faithful examples are now stored in data/burmese/sandhi_evidence.csv with an empty IPA field and SOURCE_ATTESTED_NOT_IPA status. No runtime voicing rule was enabled.

### Myanglish raw artifact audit

- The raw data.csv file's header is exactly myanmar,myanglish and the raw file preview contains 2,121 examples.
- The README's dataset_info.features declares a third official_standard feature, and the viewer displays it. The current raw CSV does not contain that third column. The discrepancy remains UNCERTAIN; do not synthesize or infer the missing field.
- The README states that Myanglish is non-standardized and the current release is predominantly one author's personal phonetic typing style. Use only as a separate informal romanization diagnostic, never as IPA gold or as a standard pronunciation reference.

### MyX orthography corpus quality audit

- The repository contains 21 CSV files under data/; the dataset page reports 4,800 rows and 1.63 MB. The README labels the corpus work-in-progress.
- Sampled hcara_phonetic.csv rows pair ဆျာ with ဆရာ, but target_words is incorrectly labelled မင်ရည် နှင့် မှင်ရည်. This is a concrete field-alignment error.
- Sampled phet_bet_phonetic.csv rows can contain multiple substitutions in one sentence while the target field only names the confusion pair. This is not a single-edit gold label without additional alignment.
- mi_mhee_phonetic.csv mixes lexical/semantic distinctions such as မီ vs မှီ, not merely a pronunciation confusion. This is useful orthography/lexical data but cannot be treated as a phonetic label.
- Yautkyar_spelling.csv repeats a narrow word family in many templated sentences. Deduplication and provenance review are required before benchmark use.
- Disposition: permission is not the blocker. Keep the dataset **QUARANTINED_FOR_QUALITY_REVIEW**; do not use it as IPA gold or import it as a clean supervised benchmark until row-level checks and de-duplication pass.

### Remaining access and acceptance gates

1. Obtain the Okell corpus bytes through an accessible project-side transfer or mirror, record the exact revision/hash, then perform Unicode, duplicate, document-boundary and text-quality profiling.
2. Access SEAlang text/dictionary records in a stable manner; resolve entry-level transcription semantics (IPA vs MLCTS2) before treating dictionary pronunciations as source phonemic data.
3. Obtain raw Myanglish and orthography dataset artifacts at pinned revisions for reproducible row-level schema checks, deduplication and target-word alignment. Permission is confirmed; data access and quality remain the gates.
4. Build separate text-only evidence tables for source-attested phonemic forms, romanization, orthographic corrections and IPA gold. Do not collapse these into one target field.

No external corpus bytes were imported in this update. Independent expert-adjudicated IPA gold remains 0; empirical IPA accuracy remains null.
