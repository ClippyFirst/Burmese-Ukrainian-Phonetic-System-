# External G2P benchmarks and engine coverage audit — 2026-11-02

## Scope and interpretation

This is a source-backed research audit, not an accuracy claim for this repository. Published PER/CER values are comparable only when dictionary/corpus, dialect, normalization, phoneme inventory, tone/phonation convention, and test split align. No external output is copied into project gold.

## Relevant benchmark evidence

### Myanmar pronunciation dictionary G2P comparison (Kyaw Thu et al., 2016)

Ye Kyaw Thu, Win Pa Pa, Yoshinori Sagisaka, and Naoto Iwahashi (2016). “Comparison of Grapheme-to-Phoneme Conversion Methods on a Myanmar Pronunciation Dictionary.” *Proceedings of WSSANLP 2016*, 11–22. https://aclanthology.org/W16-3702/.

The paper compares seven methods: S-AROW, CRF, joint-sequence models, phrase-based SMT, RNN, SVM point-wise classification, and WFST on a manually tagged Myanmar phoneme dictionary. Its full text specifies 25,300 MLC dictionary words: 25,000 used for training and three open test sets of 100 words each; a separate 100-word closed test was sampled from the training data. The paper reports automatic phoneme error rate plus manual review of voicing, tones, consonant, and vowel errors; CRF, PBSMT, and WFST are reported as the strongest methods. This is directly relevant historical G2P evidence, but the paper's romanized phoneme inventory and evaluation do not constitute project IPA gold or a score for current engines or this project's Standard Burmese IPA convention.

Reference: https://aclanthology.org/W16-3702/

### myG2P dictionary resource

The public myG2P resource documents a Myanmar Language Commission pronunciation-dictionary foundation extended for foreign pronunciations. It describes 23 phonetic symbols for 33 consonants, 87 vowel combinations and 20 special symbols; it also notes contextual voicing and context-dependent word pronunciations. This is important because a useful Burmese G2P comparator must model combinations and context, not just map individual characters.

Reference: https://github.com/ye-kyaw-thu/myG2P

### Burmese speech corpus and FST grammars (Oo et al., 2020)

Yin May Oo, Theeraphol Wattanavekin, Chenfang Li, Pasindu De Silva, Supheakmungkol Sarin, Knot Pipatsrisawat, Martin Jansche, Oddur Kjartansson, and Alexander Gutkin (2020). “Burmese Speech Corpus, Finite-State Text Normalization and Pronunciation Grammars with an Application to Text-to-Speech.” *Proceedings of the Twelfth Language Resources and Evaluation Conference*, 6328–6339. https://aclanthology.org/2020.lrec-1.777/.

This work provides a crowdsourced multispeaker speech corpus, finite-state text-normalization grammars, and Burmese G2P grammars. The paper explicitly notes that normalization and G2P are necessary but not sufficient for high-quality Burmese TTS. This is a valuable language-specific grammar/corpus reference, not a directly comparable IPA benchmark score.

Reference: https://research.google/pubs/burmese-speech-corpus-finite-state-text-normalization-and-pronunciation-grammars-with-an-application-to-text-to-speech/

## Engine coverage audit

| Engine | Declared Burmese support | What is established | Important gaps / cautions |
|---|---|---|---|
| Epitran | `mya-Mymr` | Package publishes a Burmese-script mapping. | Epitran explicitly lists Burmese among language-script pairs with limited support because of highly ambiguous orthography. Its `tones` option defaults to false, so tone marks may be removed unless explicitly enabled. Do not treat its output as complete Burmese G2P. |
| Goruut | Burmese | README lists Burmese and advertises IPA output and five tone-level symbols. | Five generic pitch levels do not encode the full phonation/voice-quality, duration, checked-syllable, and competing tone/register analyses. README says syllable tokens and tie bars are not supported. |
| Burmese language-specific CRF/WFST/FST resources | Burmese | Published G2P comparison and LREC 2020 FST grammars exist; the former reports CRF/PBSMT/WFST as strongest among tested methods. | Need source/version recovery, profile compatibility, and a current reproducible held-out test. Historical results cannot be assigned to Epitran/Goruut or to this repository. |

Sources: https://pypi.org/project/epitran/ ; https://github.com/neurlang/goruut ; https://aclanthology.org/W16-3702/ ; https://research.google/pubs/burmese-speech-corpus-finite-state-text-normalization-and-pronunciation-grammars-with-an-application-to-text-to-speech/

## Feature coverage required by this project

The comparator must be tested for: Unicode normalization; syllable segmentation; onset/conjunct/kinzi/medial parsing; vowel combinations and inherent vowel; codas and checked syllables; phonemic vs phonetic contrasts; tone/register analysis; phonation/voice quality; duration; dialect/profile; IPA tie bars and syllable boundaries; lexical exceptions; and uncertainty. Score segmental PER/CER separately from tone/register error, phonation-feature error, coda error, syllable-boundary F1, exact IPA match, and unsupported/error rate.

## Current assessment

- Epitran: **PARTIAL / HIGH-RISK BASELINE**; its own documentation explicitly warns of limited Burmese support.
- Goruut: **PARTIAL COMPARATOR**; broad language support is not evidence that Burmese phonation and tone/register contrasts are complete.
- Published CRF/PBSMT/WFST and LREC 2020 FST grammars: **PRIORITY LANGUAGE-SPECIFIC BASELINES** to recover and benchmark.
- This repository: no empirical accuracy claim; adjudicated IPA gold remains governed by the existing blind collection protocol.

## Next reproducible experiment

1. Recover the paper's Myanmar pronunciation dictionary protocol and, where available, original tagged data/model artifacts; record provenance and immutable revisions.
2. Recover the LREC 2020 FST grammar implementation and speech-corpus metadata; establish the exact target dialect and phone inventory.
3. Pin Epitran and Goruut versions; explicitly enable and record Epitran tone handling.
4. Use a held-out lexical-group split with expert-approved IPA references and separate competing phonological analyses where the literature disagrees.
5. Report segmental PER/CER, tone/register error, phonation-feature error, duration/coda error, syllable-boundary F1, exact IPA match, unsupported/error rate, and runtime.
6. Adjudicate mismatches with qualified Burmese phoneticians; never promote model output to gold.

## Evidence limitations

The WSSANLP 2016 abstract establishes the methods and broad ranking but does not provide enough details here to reproduce its exact numeric results. The LREC 2020 abstract establishes the existence and scope of grammars/corpus but not full modern profile coverage. Epitran/Goruut declarations are not independent linguistic evaluations. No new runtime benchmark was executed in this documentation-only audit.

## Hosted raw-output diagnostics on the audit branch — 2026-11-02

Exact branch-head runs:
- Epitran 1.35.3 raw-output probe: https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41409098332 — SUCCESS. Six structural-only probes returned IPA strings, but every row has empty expected IPA, zero eligible verified gold, and `NOT_SCORED_NO_VERIFIED_GOLD`. This verifies only that the mapping executes; it says nothing about Burmese pronunciation accuracy.
- Goruut source snapshot `b224bde` Burmese raw-output probe: https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41409098207 — SUCCESS as collection. On 100 source-attested myG2P examples: exact matches=0/100; notation-normalized matches=17/100; successful outputs=98, failed=2; complete source coverage=43, partial=55, unknown=2; unphonemized source fragments=69. The run logged missing `weights9.bin.zlib`; investigate before treating the runtime as stable.

All results are `NOT_SCORED_NO_INDEPENDENT_GOLD`. The 17/100 notation-normalized result is not an accuracy score; it only reflects the documented limited normalization, while phone/tone/length distinctions remain significant. The myG2P references are source-attested diagnostic material, not independently adjudicated gold for the project's Standard Burmese profile.


## Upstream Goruut asset inventory follow-up — 2026-11-02

The warning for `weights9.bin.zlib` was checked against the exact Goruut source snapshot used in the optional probes (`b224bde02151f8f86d0fe260804e4ca743bda620`). The upstream Git tree has no such file in the language-specific dictionary directories: `dicts/lao/`, `dicts/khmer/central/`, and `dicts/burmese/`. Each directory does contain earlier model assets (including the `weights7` and `weights8` files). The warning therefore reflects an asset absent from this pinned upstream snapshot, not a failed checkout of a file that exists in the repository. The probe still completed and returned raw outputs. The impact of this absent asset on ranking, coverage, or accuracy is not quantified; treat it as a model-bundle limitation and do not create substitute weights or infer a quality delta without upstream implementation evidence and a valid gold set.


## Additional Burmese CRF G2P baseline discovered — 2026-11-02

A follow-up search found [`kyaw-yethu/burmese-G2P`](https://github.com/kyaw-yethu/burmese-G2P), pinned for source inspection at commit `de0f06056cf334b8cdd5a1efd1226f01c8162b77`. Its README describes a CRFsuite sequence-labeling converter with a pre-trained `ver2/g2p.model` that emits IPA-like phonetic output and uses the [myG2P](https://github.com/ye-kyaw-thu/myG2P) dictionary. The README also explicitly lists sentence-level errors for particles and postpositional markers as future work; therefore this is not demonstrated as a complete sentence G2P engine.

The repository's [`scripts/preprocess.sh`](https://github.com/kyaw-yethu/burmese-G2P/blob/de0f06056cf334b8cdd5a1efd1226f01c8162b77/scripts/preprocess.sh) uses unseeded `shuf`, then takes 19,830 rows for training and 4,957 for testing. This split is not reproducible from the checked-in script, and the committed model's exact training membership cannot be established from the available metadata. The published model and myG2P reference dictionary are related resources, so testing the model on rows from that dictionary risks train/test overlap. The model's reported internal test results must not be presented as independent project accuracy. Its [`scripts/predict.py`](https://github.com/kyaw-yethu/burmese-G2P/blob/de0f06056cf334b8cdd5a1efd1226f01c8162b77/scripts/predict.py) uses `sylbreak` for syllabification; the project smoke probe instead supplies the dictionary's existing syllable segmentation and does not evaluate that step. A valid external comparison needs a disjoint lexical-group test set, profile/convention review, and independent expert IPA references.

**Assessment:** CRF converter = PRIORITY BASELINE / EXECUTION AND OUT-OF-DICTIONARY COVERAGE NOT YET VERIFIED; sentence-level completeness = KNOWN LIMITATION. It is worth a controlled raw-output smoke test, but no performance score is accepted until leakage and profile compatibility are resolved. Independent gold remains 0; accuracy remains null.


### Reproducible CRF raw-output smoke workflow — 2026-11-02

Added `scripts/benchmark_burmese_crf.py` and a `crf-baseline` job inside the existing `.github/workflows/optional-epitran-benchmark.yml`. Reusing a workflow already present in the base branch ensures the new job is eligible to run on the open PR before merge. The workflow pins the Burmese CRF model at `de0f06056cf334b8cdd5a1efd1226f01c8162b77`, myG2P data at `54b5c76bb5a87fdbaaeddc1892e6ebd8f97ee225`, and CRFsuite source at `a2a1547727985e3aff6a35cffe073f57f0223e9d`. It builds the CRFsuite CLI, prepares the existing deterministic 100-row source-attested probe, and stores raw predictions, source locators, model SHA-256 and limitations as a CI artifact. The implementation intentionally sets `gold_count=0` and `accuracy=null`; source concordance is diagnostic only because model training membership may overlap myG2P. Unit tests cover input sequence boundaries, missing syllable segmentation, prediction grouping and source provenance.

At this checkpoint the exact-head CI jobs are queued, not passed: [tests 41414995521](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41414995521) and [CRF raw-output 41414995523](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41414995523). Do not claim execution success until these jobs finish.


## CRF raw-output artifact inspection — 2026-11-02

The pinned Burmese CRF probe completed successfully in [workflow 41417982199](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41417982199). Downloaded artifact `burmese-crf-raw-output` (SHA-256 `0119281f9bd3d946a36dad1299f530b629599cfd26146ce190ea34f7c707ddd6`) was inspected: 100 inputs, 100 predictions, 84 exact source-concordant strings, zero skipped rows, model SHA-256 `f66571b7632eed2e94878278702654ce0a4b25fcab18720af60d3cfe00b011ce`. The report explicitly records `gold_count=0`, `accuracy=null`, `NOT_SCORED_POSSIBLE_TRAINING_OVERLAP`. The 84/100 figure is source concordance only, not an accuracy estimate, because model training membership is unknown and source-attested myG2P entries are not independent adjudicated gold. The probe uses pre-supplied syllable segmentation and therefore does not measure end-to-end Burmese segmentation or sentence handling. The upstream myG2P source declares CC BY-NC-SA 4.0; this diagnostic artifact is not a basis for redistributing source data or model output as a production lexicon.


## Google WFST and evidence-gated hybrid API — 2026-11-14

The Google Language Resources Burmese Thrax/OpenFst grammar is pinned at `a90601024f07ab7e96c911243324e0adeb16da96`; the optional workflow also pins a compatible Abseil revision. Historical exact-head workflow 43084508359 built the grammar, passed upstream symbol-table checks and emitted 6/6 outputs for the six structural-only probes. The report had zero independent gold and `accuracy: null`; this is raw execution evidence only. The upstream WORKSPACE still has dependencies not all content-address pinned.

The current branch now carries `scripts/benchmark_google_fst.py`, its structural-only refusal/alignment tests, and a Google build/smoke job in the optional comparator workflow. `HybridBurmeseEngine` is an explicit candidate collector for Google WFST, exact myG2P v2 IPA lookup, Epitran and pinned CLI providers. It does not auto-run providers, vote, or promote; `RuleBasedBurmeseEngine` remains final IPA authority. The provider order (myG2P 10, Google 20, Epitran 40, CRF 60, Goruut 90) is diagnostic ordering only. myG2P v2 is CC BY-NC-SA 4.0; its dictionary is not bundled. Google repository code is Apache-2.0, while upstream dependency pinning remains incomplete.

The current independent adjudicated Yangon IPA gold count remains zero. Neither the historical WFST PER values nor the six raw outputs can be treated as this project's benchmark.


## Current-branch comparator artifacts — 2026-11-14

Optional workflow **43582075278 SUCCESS** (test-bearing SHA `45d3513ad1f6bbbda8d9a97768e493cdda08856d`): Google Thrax/OpenFst build/symbol check and 6/6 structural-only raw outputs; Epitran 1.35.3 raw outputs on six structural probes; CRF 100/100 predictions with 84 source-concordant rows, 0 gold and `NOT_SCORED_POSSIBLE_TRAINING_OVERLAP`. The Google report SHA-256 is `88372233d85df73593b030ee0f91aa678fe86fd1c6d5cdc18e7c609b8eefd2c6`; all artifact ZIP hashes and raw report hashes are in `data/burmese/sources.csv`, `data/burmese/source_claims.csv`, and `data/external-ipa-renderers.json`. None of these figures is pronunciation accuracy.
