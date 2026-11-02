# External G2P benchmarks and engine coverage audit — 2026-11-02

## Scope and interpretation

This is a source-backed research audit, not an accuracy claim for this repository. Published PER/CER values are comparable only when dictionary/corpus, dialect, normalization, phoneme inventory, tone/phonation convention, and test split align. No external output is copied into project gold.

## Relevant benchmark evidence

### Myanmar pronunciation dictionary G2P comparison (WSSANLP 2016)

Kyaw Thu, Pa Pa, Sagisaka & Iwahashi, “Comparison of Grapheme-to-Phoneme Conversion Methods on a Myanmar Pronunciation Dictionary”, WSSANLP 2016, pp. 11–22.

The paper compares seven methods: S-AROW, CRF, joint-sequence models, phrase-based SMT, RNN, SVM point-wise classification, and WFST on a manually tagged Myanmar phoneme dictionary. It reports automatic phoneme error rate plus manual review of voicing, tones, consonant, and vowel errors; CRF, PBSMT, and WFST are reported as the strongest methods. This is directly relevant G2P evidence, but it is historical and must not be treated as a score for current engines or this project's Standard Burmese IPA convention.

Reference: https://aclanthology.org/W16-3702/

### myG2P dictionary resource

The public myG2P resource documents a Myanmar Language Commission pronunciation-dictionary foundation extended for foreign pronunciations. It describes 23 phonetic symbols for 33 consonants, 87 vowel combinations and 20 special symbols; it also notes contextual voicing and context-dependent word pronunciations. This is important because a useful Burmese G2P comparator must model combinations and context, not just map individual characters.

Reference: https://github.com/ye-kyaw-thu/myG2P

### Burmese speech corpus and FST grammars (LREC 2020)

Oo et al., “Burmese Speech Corpus, Finite-State Text Normalization and Pronunciation Grammars with an Application to Text-to-Speech”, LREC 2020.

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

The repository's `scripts/preprocess.sh` uses unseeded `shuf`, then takes 19,830 rows for training and 4,957 for testing. This split is not reproducible from the checked-in script, and the committed model's exact training membership cannot be established from the available metadata. The published model and myG2P reference dictionary are related resources, so testing the model on rows from that dictionary risks train/test overlap. The model's reported internal test results must not be presented as independent project accuracy. A valid external comparison needs a disjoint lexical-group test set, profile/convention review, and independent expert IPA references.

**Assessment:** CRF converter = PRIORITY BASELINE / EXECUTION AND OUT-OF-DICTIONARY COVERAGE NOT YET VERIFIED; sentence-level completeness = KNOWN LIMITATION. It is worth a controlled raw-output smoke test, but no performance score is accepted until leakage and profile compatibility are resolved. Independent gold remains 0; accuracy remains null.
