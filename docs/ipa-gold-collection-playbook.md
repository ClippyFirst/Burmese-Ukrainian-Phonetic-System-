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

A potentially useful audio/source lead exists: Oo et al. (2020), “Burmese Speech Corpus, Finite-State Text Normalization and Pronunciation Grammars with an Application to Text-to-Speech.” The available resource summary describes 2,528 utterances from 20 female speakers, recorded at 48 kHz, with manually segmented transcriptions, plus text-normalization and G2P grammars: https://lacuna.tiptreesystems.com/work/burmese-speech-corpus-finite-state-text-normalization-and-pronunciation-grammars/wrk_32839cc3e1a87a7ffdba33d7dde9f886. This is not an IPA gold corpus by itself. Before using it, inspect the primary paper/repository, exact audio/transcript license, consent and permitted research uses, variety/speaker metadata, transcription format, and whether IPA annotations exist. If rights and profile fit, it may provide controlled audio stimuli for specialist re-transcription; do not infer IPA from its graphemic transcripts or G2P outputs.


## OpenSLR 80 audio source — primary-source review, 2026-11-01

**Resource:** Burmese Speech Corpus (SLR80), https://openslr.org/80. **Paper:** Oo et al. (2020), https://aclanthology.org/2020.lrec-1.777.pdf.

The OpenSLR landing page lists CC BY-SA 4.0, a 541 KB female-speaker line index and a 948 MB female-audio archive. The paper's corpus section (pp. 6333–6334) gives substantially better provenance:

- 2,528 utterances from 20 female native Burmese speakers, aged 25–35;
- recorded in Yangon in a rented studio, at 48 kHz, mono, 16-bit PCM;
- each speaker read approximately 150–200 sentences;
- hand-curated, word-segmented transcriptions are paired with the recordings;
- trained native speakers performed audio/transcript QC and discarded utterances with mismatches, noise, disfluencies or mispronunciations;
- the released corpus is CC BY-SA 4.0; only female recordings were released at the time of the paper.

This is the strongest currently verified Burmese audio lead. It is still **not IPA gold**: the line index contains orthographic transcriptions, not independent IPA annotations. The paper's separate FST G2P is a pronunciation-generation component intended to bootstrap lexicons for later human checking; its output must not be used as the gold label.

### Suitability and limits

- The recording location is Yangon, but the paper does not establish a speaker-by-speaker dialect classification. Record the provisional profile as “native Burmese recorded in Yangon; individual dialect not independently classified” until a Burmese specialist approves a narrower profile.
- The release contains only female speakers, so it cannot support claims about gender-balanced speaker generalization.
- The word-segmented line index does not provide verified word-level acoustic timestamps. Any token-level selection needs manual alignment/verification against the audio; automatic forced alignment may propose boundaries but cannot certify them.
- These are sentence-context tokens. They can support a separately labelled **contextual phonetic** subset, preserving tone, phonation, coda and prosodic context. They do not automatically provide isolated citation-form pronunciations for the lexical G2P benchmark.
- Keep the external audio in its source distribution; record release, file ID, transcript, time interval and checksum in the private annotation packet. Never attempt to identify speakers.

### Collection decision

Use SLR80 as the leading source for a small contextual-audio annotation pilot after a specialist confirms the profile and the selected tokens. For the lexical citation-form benchmark, add a separate controlled elicitation session with qualified Yangon speakers. Maintain distinct corpus/profile IDs for contextual SLR80 tokens and elicited citation forms; never merge their accuracy denominators.


## Source-level corrections and candidate baseline limits — 2026-11-03

- **Hlaing & Mikami (2013; published online 2014)**, [Automatic syllable segmentation of Myanmar texts using finite state transducer](https://doi.org/10.4038/ICTER.V6I2.7150): 99.93% is orthographic word-syllabification, not G2P/IPA. The table reports 245/253 consonant-stacking words correct (96.83%); the text also discusses a free-standing-vowel error, so do not attribute all errors to stacking. The abstract reports 32,238 syllables while section 6.1 reports 32,283. Use only as a structural-parser comparator.
- **Thu et al. (2016)**, [Comparison of Grapheme-to-Phoneme Conversion Methods on a Myanmar Pronunciation Dictionary](https://aclanthology.org/W16-3702): 25,300 MLC dictionary entries, 25,000 train and three 100-word open test sets; PER uses the paper's own romanized phoneme inventory. The paper does not document independent IPA adjudication or establish the dictionary's redistribution license. Do not use as project IPA gold or copy dictionary data without rights verification.
- **Mooney & Repetti-Ludlow (2021)**, [Sonority and syllable structure: The case of Burmese tone](https://doi.org/10.3765/plsa.v6i1.4900): two acoustic experiments with one female native Yangon consultant in her late 20s. Four traditional surface tone categories are retained. Duration/voice-quality measures distinguish the categories in isolation; F0 distinguishes selected pairs; in sentential frames duration largely neutralizes while pitch remains robust. Vowel alternations are argued to be coda/sonority-conditioned. Killed H→HL and creaky HL are hypotheses for further work, not a new settled tone inventory.

The 30-item pilot must preserve this uncertainty: record tone category, phonation, duration, F0, coda and prosodic context separately; do not adopt a single-speaker competing analysis as a universal runtime rule.


## Recruitment and source leads — reviewed 2026-11-03

These are prospective leads only. No person has been contacted, consented, recruited, or approved as annotator/adjudicator. A publication or thesis is not proof of availability or qualification for independent IPA adjudication.

### Prospective linguistic reviewers

- Tanintorn Limpasiri (Mahidol University, Research Institute for Languages and Cultures of Asia) and Yuttaporn Naksuk co-authored a review synthesizing initial consonant phoneme analyses across eight Burmese dialects, including Yangon. This is a useful comparative-phonology lead for checking dialect boundaries and onset coverage, not evidence that either can independently annotate the full Yangon IPA corpus. Publication: https://so01.tci-thaijo.org/index.php/damrong/article/view/265701
- Sandar Linn completed a 2018 MA thesis specifically on Yangon Burmese phonology, with data partly collected through native-speaker interviews. This is a directly scoped prospective research lead; availability, current affiliation and suitability for independent IPA adjudication are unverified. Thesis: https://e-thesis.mcu.ac.th/storage/oeuomIhxw82QqWsYOqbHrlviHcugHfDqVOMRQhJs.pdf
- Justin Watkins authored the Journal of the IPA Burmese description. Its accompanying audio files are licensed to the IPA for personal use and may not be incorporated into another product without Cambridge University Press permission; the description is a reference lead, not a reusable audio corpus. https://www.cambridge.org/core/journals/journal-of-the-international-phonetic-association/article/burmese/334DD11C94575EF39A51109B008FB090

### Existing source and rights position

- OpenSLR SLR80 remains the strongest rights-declared speech source: CC BY-SA 4.0, 20 female Yangon-recorded speakers and 2,528 utterances. Its transcripts are orthographic and sentence-contextual, not IPA; speaker dialects are not independently classified, and it cannot support gender-balanced generalization.
- Mahidol University's 2000 Yangon Burmese phonology thesis is open access but explicitly reserved for study, requires attribution, prohibits modification and commercial use. It may be read as research evidence; do not reproduce its tables or derivative transcriptions into a redistributed project corpus without permission: https://repository.li.mahidol.ac.th/items/ed2d6600-f7c8-49be-9827-7984d398da49
- Mooney & Repetti-Ludlow (2021) is CC BY 4.0 and useful for competing phonetic analyses, but uses one female Yangon consultant. It cannot establish population-wide variation or settle the project's tone/phonation convention: https://journals.linguisticsociety.org/proceedings/index.php/PLSA/article/view/4900

### Immediate unblock sequence

1. Invite a prospective Yangon-focused reviewer to review a draft versioned convention sheet separating tone/prosody, phonation, vowel quality/length, checked codas, medials, minor syllables and uncertainty.
2. Ask the reviewer to nominate two independent native-speaker annotators and a separate adjudicator; independently confirm dialect competence and role separation.
3. Use SLR80 only as a separately labelled contextual-audio candidate; verify clip-level transcript/audio correspondence and manually establish token intervals before annotation.
4. Do not extract/relicense the Mahidol thesis or JIPA audio into the project corpus without written permission.
5. Prepare 30 candidate lexeme groups only after source locator and item-level rights review; complete a private blind-intake dry run.

Status remains BLOCKED for pilot execution: candidate researchers and sources have been identified, but no recruitment, rights clearance for derived thesis data, expert-approved convention, or adjudicated IPA labels exist.
