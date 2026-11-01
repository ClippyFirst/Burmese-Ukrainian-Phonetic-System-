# Controlled IPA gold acquisition — Burmese

**Status:** protocol ready for a human pilot; this document admits no gold labels.  
**Scope:** a controlled Burmese pilot followed by a versioned, independently adjudicated benchmark.

## Evidence boundary

A pronunciation from this repository, G2P, romanizer, dictionary, language model, or annotator memory is not gold merely because it is plausible. Keep source evidence, expert judgments, and engine predictions separate. Never seed an annotation with model output or infer complete IPA from Myanmar spelling alone.

Choose one target profile before sampling. Recommended pilot profile: contemporary Standard Yangon Burmese, careful citation forms. This is a project sampling decision, not a claim that Yangon is the only standard or that all speakers share one pronunciation. Label other regional/social profiles separately.

## Roles and blindness

1. **Curator:** selects lexemes, checks sources/rights, assigns opaque IDs, prepares packets; does not annotate.
2. **Annotators A and B:** independently transcribe identical packets. They see orthography, disambiguating gloss/context, target profile, and source/audio evidence, but never each other's work or engine predictions.
3. **Adjudicator C:** receives both locked submissions only after both arrive; cannot be A or B; records decision and rationale.
4. **Release maintainer:** validates provenance, rights, schema, split integrity, and export.

Use stable pseudonymous IDs in Git. Keep identity mappings and contact details outside the repository. Never place private audio or personal data in public issues or PRs.

## Pilot sampling

Start with **30 lexeme groups** as a process pilot, not an accuracy benchmark. Select attested items to cover, where supported by the chosen profile and sources:

- onset classes and aspiration/voicing contrasts;
- the four medials and attested combinations;
- vowel quality/length and diphthongal realizations;
- open vs checked syllables and final coda classes;
- prosodic categories under the selected transcription analysis;
- minor syllables, kinzi, and complex onset/syllable structures;
- source disagreements and cases the engine marks not established.

Do not generate a theoretical Cartesian product. Every item must be an attested lexeme with an exact source locator. Record selection rationale and uncovered cells. Keep pilot items out of held-out evaluation if used to revise the engine.

## Burmese convention sheet

Approve a versioned sheet specifying target profile, speaker context, citation vs connected speech, IPA kind, tone/prosody/phonation analysis, vowel quality and duration, checked-syllable/coda realization, medials, diphthongs, minor syllables, syllable boundaries, uncertainty, and variant policy.

Do not assume traditional tone labels and modern tone/register/phonation analyses are interchangeable. Preserve the source analysis and transcription level. Mooney & Repetti-Ludlow (2021) discuss Burmese vowel alternations in relation to tone, coda, and sonority, arguing against a simplistic tone-causes-vowel-alternation account: https://journals.linguisticsociety.org/proceedings/index.php/PLSA/article/view/4900. This makes coda and prosodic coverage essential.

## Source strategy

No sufficiently documented, rights-cleared Burmese IPA lexical corpus was verified in this review. Start with primary phonetic/phonological sources and exact page/table/entry locators; do not treat Epitran, myG2P, romanizers, or model output as gold. The existing project handoff notes myG2P dictionary material is CC BY-NC-SA 4.0; do not copy it without a specific rights/compatibility review.

Prioritize source extraction, then have a specialist verify target variety and transcription conventions. If a PDF table requires manual transcription, two people must independently verify the source transcription before it becomes an annotation packet. Source transcription checking and pronunciation adjudication are distinct tasks.

## Controlled workflow

1. Curator freezes the pilot list and records source provenance and rights before annotation.
2. Curator generates opaque IDs and two separate packets with identical evidence and conventions, excluding model output and competing IPA.
3. A and B submit separately. Curator timestamps and locks both before either sees the other.
4. C reviews both locked submissions and source packet. C records AGREEMENT, RESOLVED, or UNRESOLVED. RESOLVED requires final IPA and written evidence-based rationale; do not force agreement.
5. Curator validates schema, cross-file links, duplicates, rights, and blindness checklist. Unresolved items remain outside gold.
6. Export only rights-cleared adjudicated items. Keep restricted source material external; store exact locators/checksums where permitted.
7. Freeze a versioned manifest before benchmarking.

## Annotation packet

Include opaque record ID; target profile; Myanmar orthography and NFC form; gloss/minimal context; exact source title/author/edition/page/table/entry/audio locator; rights evidence; lawful audio access and recording context; pseudonymous speaker ID; IPA kind and convention-sheet version; literal IPA, syllable boundaries, tone, vowel length, phonation, confidence, uncertainty, and comments.

## Acceptance gates

- **Pilot can start:** profile and convention sheet approved; two qualified annotators and independent adjudicator confirmed; source/rights packet cleared; blind intake dry-run passed.
- **Pilot accepted:** 30 items have two independent submissions; disagreements adjudicated or explicitly unresolved; source transcription provenance and rights complete; blindness evidenced; validation passes.
- **Benchmark-ready:** expanded stratified corpus; frozen train/dev/test manifest; no lexeme leakage; held-out test untouched during tuning; coverage report for onset × medial × vowel × coda × prosodic profile; competing prosodic analyses separately labelled; rights and reproducibility review passed.

Existing numeric thresholds (100 train / 25 dev / 25 test) are minimum engineering gates, not a statistical sufficiency guarantee. Coverage and independent review remain mandatory.

## Current blockers

- **BLOCKED:** qualified Burmese annotators and independent adjudicator have not been recruited/confirmed.
- **BLOCKED:** primary-source item list and item-level rights review are incomplete.
- **BLOCKED:** prosodic/transcription convention needs specialist approval.
- **TODO:** finish manual transcription and independent verification of the relevant Green (2002) source table before deriving the pilot list.
- **TODO:** approve Yangon pilot profile and freeze the 30-item sample.
- **TODO:** complete a blind dry-run with one non-gold practice item.

## References

- Mooney & Repetti-Ludlow (2021), Sonority and syllable structure: The case of Burmese tone: https://journals.linguisticsociety.org/proceedings/index.php/PLSA/article/view/4900
- Existing source evidence and rights restrictions: docs/MASTER-EXECUTION-PLAN-AND-CHAT-HANDOFF.md


## Burmese speech resource lead — 2026-11-01

A potentially useful audio/source lead exists: Oo et al. (LREC 2020), “Burmese Speech Corpus, Finite-State Text Normalization and Pronunciation Grammars with an Application to Text-to-Speech.” The available resource summary describes 2,528 utterances from 20 female speakers, recorded at 48 kHz, with manually segmented transcriptions, plus text-normalization and G2P grammars: https://lacuna.tiptreesystems.com/work/burmese-speech-corpus-finite-state-text-normalization-and-pronunciation-grammars/wrk_32839cc3e1a87a7ffdba33d7dde9f886. This is not an IPA gold corpus by itself. Before using it, inspect the primary paper/repository, exact audio/transcript license, consent and permitted research uses, variety/speaker metadata, transcription format, and whether IPA annotations exist. If rights and profile fit, it may provide controlled audio stimuli for specialist re-transcription; do not infer IPA from its graphemic transcripts or G2P outputs.
