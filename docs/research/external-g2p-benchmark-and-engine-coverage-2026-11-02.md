# External G2P benchmarks and engine coverage audit — 2026-11-02

## Scope and interpretation

This is a source-backed research audit, not an accuracy claim for this repository. Published PER/CER values are comparable only when dictionary/corpus, dialect, normalization, phoneme inventory, tone/phonation convention, and test split align. No external output is copied into project gold.

## Relevant benchmark evidence

### Myanmar pronunciation dictionary G2P comparison (WSSANLP 2016)

Kyaw Thu, Pa Pa, Sagisaka & Iwahashi, “Comparison of Grapheme-to-Phoneme Conversion Methods on a Myanmar Pronunciation Dictionary”, WSSANLP 2016, pp. 11–22.

The paper compares seven methods: S-AROW, CRF, joint-sequence models, phrase-based SMT, RNN, SVM point-wise classification, and WFST on a manually tagged Myanmar phoneme dictionary. It reports automatic phoneme error rate plus manual review of voicing, tones, consonant, and vowel errors; CRF, PBSMT, and WFST are reported as the strongest methods. This is directly relevant G2P evidence, but it is historical and must not be treated as a score for current engines or this project's Standard Burmese IPA convention.

Reference: https://aclanthology.org/W16-3702/

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
