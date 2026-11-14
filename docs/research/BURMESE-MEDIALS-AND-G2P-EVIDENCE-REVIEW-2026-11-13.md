# Burmese Medials and Grapheme-to-Phoneme Evidence Review

**Review date:** 2026-11-13  
**Repository base:** dc90463bdd734867308f03cb627eb8941efc19d6 (main)  
**Research branch:** research/burmese-medials-g2p-evidence-2026-11-13  
**Scope:** Standard/central Yangon-oriented Burmese; orthographic medials, onset/rime interactions, word-level G2P resources, phonetic evidence, licensing and current implementation boundary.

## Executive findings

1. The four modern Burmese medial signs are orthographic modifiers historically related to ya, ra, wa and ha. They are not four invariant IPA segments. Unicode establishes their identity and encoded syllable order, not their phonetic realization.
2. The best current descriptive account found says U+103B MEDIAL YA and U+103C MEDIAL RA are both normally /j/, but may yield palatalized consonants after velar stops; U+103D MEDIAL WA may represent /w/ or /ʊ/; U+103E MEDIAL HA can mark aspiration/devoicing and can participate in /ʃ/ outcomes. These are contextual patterns, not a complete rule inventory.
3. The spelling မြန် is not wholly unattested. English Wiktionary gives /mjàɴ/ for the lexical item and includes /mjàɴmà/ in a longer compound. This is a useful lexical pronunciation lead, aligned with the descriptive /j/ account for medial RA. It is not a controlled acoustic study or independently adjudicated Yangon gold item.
4. The 2001 JIPA description reports /j/ and /w/ clusters in which the glide may surface as secondary palatalization/labialization. This cautions against conflating phonemic input with narrow surface phonetics.
5. The principal G2P resource strands are MLC-derived dictionary work used by Thu et al. (2016) / myG2P 2.0, and the Google/SLR80 speech corpus plus Thrax pronunciation grammar described by Oo et al. (2020). Neither is an immediately reusable, fully licensed, independently adjudicated project gold corpus for all medial environments.
6. The browser contains a dormant contextual IPA derivation path, but a guard explicitly withholds all medial-bearing structures. Python independently withholds medials and codas. This asymmetry must be resolved with shared fixtures before runtime rules are enabled.
7. The safe result of this pass is a source-linked medial evidence matrix and regression gates, not a blanket medial implementation. The project remains a partial prototype.

## 1. Evidence method

This review separates:
- orthographic/encoding evidence: sign identity, encoded position and recognized combinations;
- descriptive phonological evidence: phonemic or broad transcription claims and environments;
- phonetic/acoustic evidence: observed surface realization, speaker sample and speech style;
- lexical attestation: a pronunciation listed for a word, without assuming acoustic gold status;
- computational evidence: model data, split design, PER/WER and source availability;
- rights evidence: paper, code, dataset and underlying dictionary licenses are checked separately.

Evidence labels in data/burmese/medial_evidence_matrix.csv are not runtime approvals.

## 2. Orthographic structure is not phonetic transcription

Unicode 18 §16.3.1 and Table 16-4 list the four modern Burmese medial slots:
- U+103B ျ medial ya;
- U+103C ြ medial ra;
- U+103D ွ medial wa;
- U+103E ှ medial ha.

The standard describes these as modified forms of ya, ra, wa and ha, and says they modify the syllable vowel. It distinguishes them from older/Pali/Sanskrit subjoined consonants encoded with U+1039 VIRAMA plus a full consonant. A medial is not the same structural object as a stacked consonant. Unicode is authoritative for encoding and syllable order, not a universal IPA mapping.

The 2004 national contribution to ISO/IEC 10646 (WG2 N2827) states that the 1986 Myanmar Language Commission orthography listed eleven medial forms: four basic forms, five two-medial combinations and two three-medial combinations. It says the consonant and medial are not pronounced separately once combined and the inherent vowel of the initial consonant is elided. This is useful for orthographic inventory and historical MLC attribution. It is an encoding proposal, not a modern Yangon acoustic study; the proposal's font-dependent glyphs must not be copied as Unicode data without normalization.


## 2.1 Orthographic syllabification research: Hlaing (2014)

Tin Htay Hlaing's 2014 doctoral dissertation explicitly separates phonetic and orthographic syllable structures. In its phonetic view it gives C[M]V[CK]D (or V[CK]D), where M is a medial consonant and D tone; in its orthographic view it represents a syllable as consonant, medial signs, dependent vowels, final/asat and tone-mark groups. This supports the project's pipeline boundary: a structurally valid orthographic syllable is not itself a phonetic transcription.

The dissertation lists four basic medial signs and seven combined medial forms (eleven normalized forms total). The seven added codepoint sequences are:
- U+103B + U+103D (YA + WA);
- U+103C + U+103D (RA + WA);
- U+103B + U+103E (YA + HA);
- U+103C + U+103E (RA + HA);
- U+103D + U+103E (WA + HA);
- U+103B + U+103D + U+103E (YA + WA + HA);
- U+103C + U+103D + U+103E (RA + WA + HA).

**Source-quality note:** in the final row of the thesis's Table 5 / Table 24, the codepoint sequence is U+103C + U+103D + U+103E, but the descriptive text repeats “YA + WA + HA.” The codepoints unambiguously indicate RA + WA + HA; the discrepancy is recorded rather than silently copied. The 2004 WG2 N2827 proposal independently supports the total of eleven MLC forms.

The dissertation's orthographic FST experiment covers 11,732 words and 32,283 syllables: 11,092 standard words and 640 irregular words. Its initial result is 99.93% word-level syllabification, with eight errors among stacked-consonant words (245/253 correct); the author says a later experiment improved all tested words. This is a structural segmentation result, not G2P or IPA accuracy. It is useful as a parser/normalization benchmark lead, but the thesis does not grant a data-reuse license.

## 3. Medial-by-medial evidence

### 3.1 U+103B ျ and U+103C ြ

Richard Ishida's Myanmar (Burmese) Orthography Notes, updated 28 April 2026, reports that both signs are normally pronounced /j/. Examples include ပျော် and ပြည်. When preceded by a velar stop, the sequence may instead produce palatalization, with outcomes including /tɕ/, /tɕʰ/, /dʑ/ and /ɲ/ (examples include ကျောင်း, ကြက်, ဂျပန် and ငြ).

Consequences:
- the spelling name “medial ra” must not be read as a general /r/ segment;
- ya/ra medial behavior depends on preceding consonant class;
- velar-onset cases are not safely generated by appending /j/ to velar IPA;
- the source does not provide a complete onset × vowel × coda × prosody table.

Watkins (2001), a JIPA description based on one 30-year-old male consultant from Rangoon reading carefully and deliberately, independently describes /j/ and /w/ as second elements of consonant clusters. In examples, /j/ may surface as secondary palatalization and /w/ as secondary labialization; /jw/ remains [jw]. Watkins does not map U+103B/U+103C to those segments. It supports the phonetic possibility of secondary articulation, not a direct orthographic mapping for every spelling. It also notes /ɹ/ as an optional variant of /j/ in some Pali-origin loanwords; this is not evidence that medial RA generally means /ɹ/.

Transcription-layer implication: broad phonemic /mja/ and narrower surface [mʲa] can describe different levels of analysis. The product must state whether its IPA field is phonemic/broad or phonetic/narrow before encoding such alternations.

### 3.2 U+103D ွ

Ishida reports that medial WA represents /w/ but may also represent /ʊ/ in particular vowel patterns. U+103D is therefore not an unconditional /w/ insertion. The parser must retain the sign and structural position; the phonological adapter must distinguish onset glide from rime/vowel behavior. The source does not provide a complete list of all /ʊ/ contexts.

### 3.3 U+103E ှ

Ishida describes U+103E as a marker used to create aspirated versions of consonants, rather than as a simple independent /h/. It also participates in specific sibilant outcomes:
- ရ + ှ (ရှ) is described with /ʃ/;
- လ + ျ + ှ (လျှ) is also described with /ʃ/.

The notes give မြွှ (U+1019 U+103C U+103D U+103E) as pronounced [m̥w], with the medial-ha feature transcribed before the consonant it modifies. This warns that Unicode order and phonological feature order differ: surface output is not concatenation of written signs.

Repetti-Ludlow (2023) investigates voiced and voiceless Burmese sonorants and reports acoustic differences in duration, F0 and excitation of the following vowel, with spread-glottis noise present in many voiceless tokens. This is relevant background for a future phonetic model of devoicing/aspiration, but it does not validate every U+103E spelling-to-IPA correspondence.

### 3.4 Multiple medials and historical combinations

Ishida documents two- and three-medial onset clusters, with examples လျှာ, လျှင် and မြွေ. WG2 N2827 records the MLC 1986 orthographic set of eleven medial forms. Neither source establishes that every combinatorially possible sequence is legal in modern native Burmese, nor that every legal sequence has a compositional pronunciation.

Do not generate a cartesian product of four medials and call it a validated inventory. Distinguish attested native combinations, rare/archaic spellings, Pali/Sanskrit conjunct spellings, foreign-word adaptations and malformed/unsupported sequences.

## 4. The concrete word မြန် and the example မြန်မာ

### 4.1 Lexical evidence

The English Wiktionary entry for မြန် lists IPA /mjàɴ/ and MLCTS mran. It cites G. H. Luce (1981), “-AN Finals (26. Quick; Swiftly),” p. 53, as a reference for the lexical item. The IPA field is the Wiktionary transcription; the cited historical word-list reference is not itself a modern acoustic study and should not be presented as proof that the IPA string was measured from a Yangon speaker.

A separate English Wiktionary compound entry contains မြန်မာ with /mjàɴmà/ in the longer pronunciation /pjìdàʊɴzṵ mjàɴmà nàɪɴŋàɴdɔ̀/. The Myanmar Wiktionary entry for မြန် currently gives MLCTS /mjan/, but no IPA field. The Myanmar Wiktionary entry for မြန်မာ့ gives /mjàɴma̰/ and /mjəma̰/ and labels the form as induced creaky tone; this is a different lexical/prosodic form, not a substitute for the unmarked input.

### 4.2 What this supports and does not support

It supports recording /mjàɴ/ as a lexical IPA candidate for မြန်, and gives a concrete target for later expert/audio checking. It is consistent with the descriptive account in which U+103C can represent /j/ in non-velar environments.

It does not establish:
- a general rule that every U+103C is /j/ in every onset/rime context;
- the narrow phonetic surface form of this token;
- the precise Yangon register, speaker profile, speech rate or connected-speech realization of the Wiktionary entry;
- universal tone realization from the written word alone;
- permission to copy Wiktionary or other dictionary datasets without checking license and upstream policy.

### 4.3 Why the current engine still withholds the form

The current Python adapter returns no canonical IPA when a parsed syllable has a coda or a medial and has no active medial derivation. The browser's parseCluster similarly marks every medial-bearing syllable unsupported before its contextual deriveIpa function can run. That function contains candidate mappings for ya/ra, wa and ha, but its top-level guard disables them. Its presence is not evidence that it is active or verified.

For မြန်, the browser parser recognizes base မ, medial RA ြ, and nasal coda န + ်; the current guard then withholds the result. Python separately withholds it. This is fail-closed behavior under the existing contract, but the new lexical attestation changes the research status from “no word-level lead found” to “lexical candidate found; independent validation pending.”

Do not simply remove the browser guard: Python/browser parity, rime/coda analysis, tone policy and independent annotation are acceptance requirements.



#### External engine disagreement and CRF diagnostic

A second raw comparator, Epitran 1.35.3, was run against the same six structural-only probes (workflow run 43325991496). Its output for မြန် is “məjaɴ”, whereas the pinned Google Thrax output is “m j àɴ” and the lexical Wiktionary form is /mjàɴ/. Across the six probes the two engines also differ in tone marking, the vowel/coda analysis of ကော်, and whether စွယ် is parsed with an inserted schwa or a glide onset. Both artifacts explicitly record zero eligible gold items and null accuracy. The Epitran output is therefore a disagreement to investigate, not evidence that either system is correct; the inserted schwa must not be accepted or rejected without an independent Yangon recording/adjudication.

A pinned CRFsuite Burmese-G2P v2 model was also run on 100 evenly spaced entries from the 24,009-entry myG2P v2.0 source file. It returned 100 predictions and agreed with 84 source labels. In this sample, YA-bearing entries were 10/14 source-concordant, RA-bearing 17/20, WA-bearing 13/15, and HA-bearing 7/8 (categories overlap). The exact target word မြန် was not in the 100-row sample. The artifact explicitly sets gold_count=0 and accuracy=null because model training membership is unknown, the labels come from the same myG2P resource family, and the input syllable boundaries are supplied rather than evaluated. These are raw diagnostic concordance counts, not accuracy or independent validation. The final artifact pair belongs to the exact research-branch head 5eff1f3d052e775026ffff0fa0b3edd00512224d. The source dictionary remains CC BY-NC-SA 4.0 and is not cleared for commercial reuse.

### 4.4 Green's syllable/rime model and a second G2P attestation

Green's October 2002 analysis gives Burmese syllable shape C(G)V((V)C): an onset consonant optionally followed by a glide; a rhyme with a monophthong, monophthong plus coda, or diphthong plus coda. It explicitly gives /mjè:/ ‘earth’ and /mjɛʔ/ ‘eye’ as CGV and CGVC examples. This is independent descriptive evidence that /mj/ is a possible onset cluster in the analysis, but it does not by itself identify which Unicode medial sign created the glide in a particular word.

Green's coda analysis is important for interpreting the final part of /mjàɴ/: only placeless /ʔ/ and placeless nasal /N/ are allowed as codas. /N/ is described as realized through nasalization of the preceding vowel, with approximate coronal articulation after monophthongs and approximate velar articulation after diphthongs. It should therefore not automatically be treated as an independent phonetic [ɴ] segment. The transcription convention and the distinction between phonemic /N/ and its surface realization must be preserved.

Green describes four tones in major syllables, but only three tones in nasal rhymes; checked tone is excluded from nasal rhymes. Tone realization is multi-cue and context-sensitive: pitch is not the only cue, and vowel quality, final consonantism, duration and phonation can contribute. This makes a flat one-character tone rule unsafe.

The pinned Google Language Resources Burmese Thrax/OpenFst grammar provides a second computational candidate:
- orthographic preprocessing maps U+103B to -y, U+103C to -r, U+103D to -w and U+103E to -h;
- preprocessing reorders -h before the other medials;
- the grammar's g2p_medial maps -y and -r to /j/ and -w to /w/; weights make some medial analyses less preferred where -y can instead belong to a special onset or -w can belong to the nucleus;
- g2p_initial contains onset-specific exceptions, including velar-palatalized outcomes and -h-conditioned voiceless/merged onsets;
- g2p_nucleus handles rime-specific -w vowel behavior and coda/tone combinations.

The pinned source is Google Language Resources commit a90601024f07ab7e96c911243324e0adeb16da96. Both the repository LICENSE and the grammar header declare Apache-2.0. This corrects the earlier uncertainty: the paper itself does not specify a license, but the actual pinned grammar/code does. The upstream WORKSPACE is not fully hermetic; the existing research PR pins compatible build dependencies and reports a successful build/smoke run.

On the six-row structural-only probe, the exact PR-head Google WFST run 43084508359 returned six raw outputs. The fifth probe is မြန် (struct-005), and its output is “m j àɴ”. The artifact is burmese-google-fst-raw-output, SHA-256 c43dc9afc74c49189330c1e704e12b352c9e9d02b58072d5a37a8d7b1a03ebba. The run had zero independent gold labels and reports raw-output smoke only. This output aligns with Wiktionary /mjàɴ/ and Green's /mj/ onset plus nasal-rhyme analysis. It is useful cross-system corroboration, not an independent pronunciation judgment: the probe had no expected IPA and the Google grammar's phonological convention is source-specific.

The Google grammar's phone inventory includes tone/phonation-marked vowel symbols and voiceless sonorants. Its /àɴ/ is a single symbol-table unit, not proof that the surface contains a standalone velar nasal [ɴ]. Do not flatten this into a generic “m + ya + velar nasal” rule.

## 5. G2P and speech resources

### 5.1 Thu et al. (2016): MLC dictionary experiments

The WSSANLP paper uses 25,300 entries from the 1993 Myanmar Language Commission dictionary. The experiment uses 25,000 training entries, three open test sets of 100 words each, and a separate 100-word closed test selected from training. The closed test is not an independent holdout. Seven methods are compared: S-AROW, CRF, joint-sequence, phrase-based SMT, RNN, SVM point-wise and WFST. Open-set PER best results are 14.7, 11.4 and 15.7 for the three sets, with WFST best or tied; manual feature review reports a different ranking for some error types.

The paper's 113 unique phonemes are represented in its own romanized notation. It does not publish a complete IPA key or medial-specific error analysis. The MLC dictionary, prepared splits and annotations are not given as a downloadable dataset in the paper. The paper's CC BY 4.0 license applies to the paper, not automatically to the underlying MLC dictionary.

### 5.2 myG2P 2.0

The public myG2P repository publishes a five-field text dictionary: ID, orthography, syllable segmentation, pronunciation respelling and IPA. Its README says the lexicon is based mainly on MLC dictionary words, extends the mapping for foreign pronunciations and documents contextual pronunciations. Version 2.0 is listed as released 15 February 2021.

Rights gate: the repository states CC BY-NC-SA 4.0. Its Myanmar-language README explicitly warns that non-commercial use is allowed but commercial use is not granted and directs commercial users to contact maintainers. The underlying source dictionary is MLC's 1993 dictionary. Therefore:
- do not vendor dictionary rows or train on them for a commercial product under the public license alone;
- do not infer that code and data licenses are interchangeable;
- obtain written permission for commercial use or find an independently licensed source;
- cite as research evidence only within applicable terms.

### 5.3 Oo et al. (2020) and OpenSLR SLR80

The LREC paper describes a crowd-sourced Burmese speech corpus of 2,528 utterances from 20 female speakers, recorded in Yangon. The paper does not establish that all speakers use one specific regional dialect. The released female archive and line-index transcripts are hosted as OpenSLR SLR80, listed under CC BY-SA 4.0. Transcripts are orthographic/word-segmented, not IPA. Audio is useful for future native-speaker adjudication, but each item must be checked for content and metadata.

The same paper separately describes an in-house segmentation corpus and models that were not in the public domain. Do not conflate that private resource with released SLR80 audio/transcripts.

The paper describes an open-source Thrax WFST pronunciation grammar, burmese.grm, with grapheme.syms and phoneme.syms, accepting Myanmar Unicode and outputting IPA. Printed resource path: https://github.com/google/language-resources/my/burmese.grm. It describes orthographic processing, medial reordering, vowel normalization, consonant unstacking, phonological transformations and exceptions. However, the paper's “open-source” description does not identify a specific license for the grammar. Verify the current repository's license and exact files before reuse or vendoring.

### 5.4 Other computational and phonetic work

- Hlaing & Pa Pa (2019) evaluate joint-sequence, Transformer, encoder-decoder and attention-based G2P on a larger Myanmar pronunciation dictionary, reporting PER/WER and analyses by word class/error type. Accessible metadata does not expose dataset license or a medial-specific rule table.
- Hlaing (2018) describes a phoneme-concatenation TTS inventory of 157 phoneme/half-sound units. The abstract is not sufficient to map the four Unicode medial signs to those units.
- Yanson (2015) argues that modern Burmese sound changes may not be reflected in standard dictionary/textbook pronunciations. Full text was not available in this review.
- Nishi (1998) describes two standard Burmese voicing-sandhi patterns with exceptions. It reinforces context dependence; the available abstract is not enough to implement the full rule.
- Mooney & Repetti-Ludlow (2021) analyze Burmese tone and vowel alternations using two acoustic experiments with one female native Yangon consultant. Duration/voice quality distinguish four tones in isolation; in sentential contexts duration largely neutralizes and pitch remains robust. The paper argues that vowel alternations are coda/sonority-conditioned rather than tone-driven; this is one-speaker evidence, not a complete dialect norm.
- Duan & Zhu (2025) propose a competing double-register, eight-tone analysis: four modal-voiced tones and four lower/breathy-voiced tones, involving pitch, register and length. Publisher metadata and abstract were inspected; the full 44-page article's empirical tables were not retrieved in this review. Keep it as a competing published analysis, not consensus or an implemented tone inventory.
- Repetti-Ludlow (2023) provides acoustic evidence on voiced and voiceless sonorants; it is relevant to phonetic effects associated with medial HA, but not a complete spelling-to-pronunciation lexicon.
- Hlaing (2014) provides an orthographic syllabification FST and a codepoint-level medial combination inventory. Its 99.93% figure is word-level orthographic syllabification, not G2P or IPA accuracy.

## 6. Current repository implementation audit

Inspected: src/burmese_ukrainian/ipa.py, parser.py, unicode.py, model.py; src/web/app.js and romanization-ukrainian.js; data/burmese/ipa_onsets.csv, ipa_vowels.csv, phonological_rules.csv, sources.csv and source_claims.csv.

Findings:
1. Python parser preserves four medial signs as structural metadata. CI exposed a cross-runtime segmentation gap: browser segmentation already treats a base consonant + ASAT as the preceding syllable's coda, while Python previously split it as a new onset and left the prior medial syllable incomplete. The Python parser now applies the same coda boundary and records the final consonant plus ASAT structurally. Python _ipa still returns None for medial/coda structures; the pronunciation remains withheld.
2. Browser parseCluster stores medials, codas and vowels. Its unsupportedStructure guard withholds all medials, kinzi and conjuncts. A contextual deriveIpa function exists behind that guard and contains candidate behavior; it is dormant.
3. Browser candidate logic is not a shared Python/browser rule implementation. Do not enable it by changing one guard.
4. The current phonological rule registry has no dedicated medial evidence table. New medial_evidence_matrix.csv is an evidence registry only; runtime generation does not consume it.
5. MLCTS romanization is separate. MLCTS mran can be segmented as m + r + an by the current crosswalk and rendered as a proposed orthographic Ukrainian form. That is not IPA and must not be mistaken for pronunciation /mjàɴ/.
6. A full orthographic parse does not mean phonology is established; a lexical IPA citation does not mean a rule is validated across the language. The exact word မြန် is now one parsed orthographic syllable in both browser and Python; its IPA remains withheld.

## 7. Recommended implementation architecture

Preserve:

Myanmar orthography → structural syllable parse → lexical/context lookup → phonological representation → surface phonetic realization → IPA output → Ukrainian target adaptation.

- Orthographic parser: identifies U+103B–U+103E, onset, conjuncts, vowel signs, coda, asat, kinzi, tone/prosody and source boundaries. It must not infer pronunciation.
- Phonological analyzer: applies scoped onset-class and medial-combination rules, with dialect and lexical scope; can return multiple analyses or unresolved status.
- Lexical exception layer: stores source-attributed word pronunciations and variants; a dictionary entry is not silently promoted to a general rule.
- Phonetic realization: models secondary articulation, aspiration, devoicing, vowel allophony, tone/register and phrase context. Output contract must distinguish phonemic slashes from phonetic brackets.
- IPA boundary: preserves segmental and prosodic information and carries provenance/status.
- Ukrainian adapter: consumes only IPA/typed phonetic result; no direct source-grapheme shortcut.

## 8. Acceptance plan and blockers

| Work item | Status | Acceptance criterion |
|---|---|---|
| Four-medial orthographic inventory | PARTIAL; evidence matrix added | Cross-check Unicode 18, UTN #11, MLC orthography, native examples and modern vs Pali/archaic scope |
| YA/RA /j/ and velar palatalization | EVIDENCE-LIMITED | Native-speaker/expert review plus onset-class × vowel × coda test pairs; reconcile phonemic vs surface [Cʲ] |
| WA /w/ vs /ʊ/ | CONTEXT-DEPENDENT | Complete source-located rime conditions and minimal/near-minimal pairs |
| HA aspiration/devoicing and /ʃ/ fusion | CONTEXT-DEPENDENT | Onset-class table and acoustic/dictionary examples for each productive class |
| Multi-medial combinations | PARTIAL | Validate all eleven MLC orthographic forms and identify native/loan/archaic restrictions |
| မြန် lexical IPA | CANDIDATE / NOT GOLD | Verify against MLC dictionary/myG2P (permission-gated) and at least two independent Yangon speaker recordings or expert annotations |
| Tone/register and rime interactions | TODO/PARTIAL | Define phonemic vs phonetic output and add source-scoped acoustic minimal pairs |
| G2P benchmark corpus | BLOCKED for direct reuse | Establish dataset license and source access; preserve speaker-disjoint and lexeme-disjoint test partitions |
| Python/browser parity | TODO | Shared fixtures for every approved rule and identical status/provenance in both runtimes |
| Commercial myG2P reuse | BLOCKED pending permission | Obtain written permission or do not copy/derive model artifacts from CC BY-NC-SA data |
| Google Thrax grammar reuse | BLOCKED pending license verification | Verify current repository, exact grammar file and license before vendoring |

## 9. Minimum gold-corpus specification

Every item should include:
- original Unicode text and NFC/NFD forms;
- orthographic syllable segmentation with code-point spans;
- lexical identity/POS and phrase context;
- dialect/profile, pseudonymous speaker ID, region, age band and recording style;
- audio locator, consent and redistribution status;
- phonemic and narrow phonetic transcriptions as separate fields;
- syllable boundaries, tone/register/phonation, vowel quality/length/nasalization, coda realization and uncertainty;
- at least two independent annotators and a third adjudicator for disagreement;
- source/version/license and immutable hashes;
- speaker-disjoint and lexeme-disjoint train/dev/test partitions.

Adversarial slices: each medial separately; all MLC multi-medial combinations; YA/RA after velars vs labials/dentals/alveolars/nasals/liquids; WA glide vs vowel/rime contexts; HA on stops/nasals/liquids and sibilant combinations; medial + nasal/checked coda/kinzi/tone mark; native/Pali/Sanskrit/foreign words/proper names/compounds; isolated vs phrase-medial/final; competing lexical readings.

## 10. Bibliography and primary resource locators

- [U18] Unicode Standard 18.0.0, Chapter 16, §16.3.1, Table 16-4.
- [UTN11] Unicode Technical Note #11, Representing Myanmar in Unicode.
- [WG2N2827] Myanmar Unicode and NLP Research Center, Proposal of 4 Myanmar Semivowels, L2/04-273 / WG2 N2827 (21 June 2004).
- [HLAING2014] Tin Htay Hlaing, Syllabification, Normalization and Lexicographic Ordering of Myanmar Texts using Formal Approaches, Doctor of Engineering dissertation, Nagaoka University of Technology (2014), especially §§3.3–3.7, Tables 5/8, pp. 26–47.
- [ISHIDA2026] Richard Ishida, Myanmar (Burmese) Orthography Notes, updated 28 April 2026.
- [WATKINS2001] J. Watkins, “Burmese,” Journal of the International Phonetic Association 31(2), 291–295 (2001), DOI 10.1017/S0025100301002122.
- [GREEN2002] Antony Dubach Green, “Word, Foot, and Syllable Structure in Burmese,” October 2002 working paper, revised from 1995; §§1.1–1.2, 2.1–2.4.
- [GREEN2005] Antony Dubach Green, “Word, Foot, and Syllable Structure in Burmese,” in Studies in Burmese Linguistics (2005), pp. 1–25; online edition CC BY-SA 4.0.
- [LUCE1981] G. H. Luce, A Comparative Word-List of Old Burmese, Chinese and Tibetan (1981), p. 53, “-AN Finals (26. Quick; Swiftly).”
- [WIKT_EN_MRAN] English Wiktionary entry မြန်, IPA /mjàɴ/.
- [WIKT_EN_COMPOUND] English Wiktionary entry ပြည်ထောင်စုမြန်မာနိုင်ငံတော်, compound IPA contains /mjàɴmà/.
- [WIKT_MY_MRAN] Myanmar Wiktionary entry မြန်, MLCTS /mjan/ and cited 2003 Myanmar spelling dictionary.
- [WIKT_MY_MRANMA] Myanmar Wiktionary entry မြန်မာ့, variants /mjàɴma̰/ and /mjəma̰/.
- [W16-3702] Ye Kyaw Thu et al., “Comparison of Grapheme-to-Phoneme Conversion Methods on a Myanmar Pronunciation Dictionary,” WSSANLP 2016, 11–22.
- [GOOGLE_MY_G2P_FST] Google Language Resources, my/burmese.grm, grapheme.syms and phoneme.syms, pinned commit a90601024f07ab7e96c911243324e0adeb16da96; Apache-2.0; raw-output CI run 43084508359.
- [MYG2P2026] Honey Htun et al., “Grapheme-to-IPA Phoneme Conversion for Burmese (myG2P Version 2.0),” JIIST 5 (April 2021), 7–17; CC BY-NC-SA 4.0.
- [LREC2020_BURMESE] Yin May Oo et al., “Burmese Speech Corpus, Finite-State Text Normalization and Pronunciation Grammars with an Application to Text-to-Speech,” LREC 2020, 6328–6339.
- [OPENSLR80] OpenSLR resource SLR80, Burmese crowdsourced speech data, CC BY-SA 4.0.
- [HLAING2019] Aye Mya Hlaing & Win Pa Pa, “Sequence-to-Sequence Models for Grapheme to Phoneme Conversion on Large Myanmar Pronunciation Dictionary,” O-COCOSDA 2019, DOI 10.1109/O-COCOSDA46868.2019.9041225.
- [HLAING2018] C. Hlaing & Aye Thida, “Phoneme Concatenation Method for Myanmar Speech Synthesis System,” DOI 10.5815/ijitcs.2018.12.02.
- [YANSON2015] R. Yanson, “Predictability of Phonological Changes in Burmese,” Archiv orientální 83(1), 95–115 (2015), DOI 10.47979/aror.j.83.1.95-115.
- [NISHI1998] Y. Nishi, “The Development of Voicing Rules in Standard Burmese” (1998).
- [MOONEY2021] K. Mooney & C. Repetti-Ludlow, “Sonority and syllable structure: The case of Burmese tone,” DOI 10.3765/PLSA.V6I1.4900.
- [REPETTI2023_BURMESE] C. Repetti-Ludlow, “Acoustic correlates of Burmese voiced and voiceless sonorants,” DOI 10.1515/phon-2022-0026.

## 11. Final research disposition

This review changes the research register: a lexical IPA lead for မြန် has been found, superseding “no word-level attestation found.” It does not change runtime: မြန် remains withheld pending independent validation, tone/rime policy and Python/browser parity.

**Project classification:** PARTIAL PROTOTYPE.  
**Research readiness:** improved, with inspectable evidence and explicit gaps.  
**Linguistic release readiness:** not established.


## IPA gold schema boundary: nasalization — 2026-11-13

The existing typed IPA schema has a literal IPA value and kind, plus optional syllable boundaries, tone, vowel length and phonation. It has no dedicated structured nasalization field. A literal IPA value can still preserve a combining tilde or other nasalization notation, so this does not prevent faithful transcription. However, downstream analytics cannot query nasalization as a typed feature without reading the IPA string. No schema change was made in this research pass: the phonemic /N/ vs surface nasalization convention must first be adjudicated by a Burmese specialist. Track an optional nasalization field as a deferred schema decision, not as an implicit parser feature.


### 5.5 UCSY-SC1: a larger but rights-gated audio lead

Mon, Pa Pa and Thu (2019) describe UCSY-SC1: 42 h 39 min of 16 kHz mono speech, 307 speakers, 25 h 20 min of web news and 17 h 19 min of recorded daily conversation. The paper reports 33 basic consonants, 12 vowels and four medial signs, and includes a discussion of nasalized vowels. This is potentially a much richer speaker-diverse source for future acoustic annotation than a single-speaker study.

However, the paper is an ASR-corpus description, not an IPA corpus: its WER results measure ASR, not G2P or pronunciation transcription. The publisher author-details page lists CC BY-SA 4.0, but the PDF footer says “All rights reserved”; article-level rights therefore need confirmation. The inspected sources do not establish a separate license or public download permission for the underlying corpus audio. Do not infer that the article's license automatically licenses the corpus. Treat UCSY-SC1 as a rights-gated annotation lead only; obtain corpus access and explicit data-use permission before collecting derived IPA labels or redistributing audio.


### 5.6 Mya2Rom: MLCTS, MLCTS2 and IPA are separate output contracts

The pinned Mya2Rom 0.4.4 README exposes five explicit modes: ipa, mlcts, mlcts2, simple and simple2. It defines MLCTS as the MLC's orthographic transcription; MLCTS2 is a more phonetic variant used by the MLC Myanmar-English Dictionary and SEAlang, but it remains a romanization, not a standardized IPA output. The README's own IPA flavour uses /N/ instead of writing nasalized vowels, which is a transcription convention, not proof that the surface contains a standalone [ɴ].

The project browser runtime explicitly calls mya2rom(unit.raw, "mlcts", ...). Therefore the current Latin → Ukrainian mode is orthographic transliteration, not pronunciation-based transcription. It must not be used as an IPA oracle or silently merged with the IPA-first G2P path. Mya2Rom is CC BY-SA 4.0; its README also documents limitations with stacked letters, ASAT, schwa, voicing sandhi, alternate pronunciations and Pali/Sanskrit-derived words. The vendor-derived 94-rime inventory is therefore useful for coverage but not an independently validated MLC-primary or pronunciation corpus.

## 8. Text-only corpus leads and evidence limits

The continuation research uses written sources only. No audio corpus, recording, speech sample, or audio-derived annotation is part of the active research scope.

### 8.1 Myanglish parallel text (DatarrX, 2026)

The myX-myanmar-to-myanglish-corpus dataset card reports 2,121 Burmese Unicode-to-Myanglish pairs. Its own documentation warns that Myanglish has no standardized orthography and that the current data is predominantly based on one native author's personal typing/phonetic style. The dataset viewer exposes three fields (myanmar, myanglish, official_standard), whereas the README's schema section describes only two; this must be reconciled against the raw CSV before any use. The card declares CC BY-SA 4.0. The dataset is a possible written romanization diagnostic, not IPA, not a universal romanization norm and not independent G2P gold. No rows were imported.

### 8.2 Orthographic error correction text (DatarrX, 2026)

The myX-myanmar-orthography-corpus dataset viewer reports 4,800 rows. Its documented fields are noisy sentence, corrected sentence, error category and target words. Files with phonetic in their names classify phonetic spelling confusions; the inspected phet_bet_phonetic.csv contains no IPA or phonetic transcription column. Medial pairs such as ကျ/ကြ are listed as future expansion, not as current evidence. This can become an orthographic-normalization test source after manual row review, but it does not validate medial-to-IPA rules. The card declares CC BY-SA 4.0. No rows were imported.

### 8.3 John Okell's A Corpus of Modern Burmese (1990s compilation; Zenodo 2018)

Zenodo describes an 8.8 MB Unicode text file compiled by John Okell in the 1990s. The European Language Grid catalogue lists CC BY 4.0, but the Zenodo record's Rights/License field is blank. This discrepancy is recorded as rights CONFLICT/UNKNOWN; the corpus is not copied or ingested pending a direct rights statement. It is a text corpus, not an IPA-labelled resource.

### 8.4 Evidence boundary

These resources may support written orthographic coverage, lexical context, and romanization comparison. They cannot be promoted to IPA gold merely because the Latin target is described as phonetic. Preserve separate typed layers for source spelling, orthographic MLCTS, informal romanization, IPA, and Ukrainian adaptation. Independent expert-adjudicated IPA gold remains 0 and empirical accuracy remains null.

## 9. Historical written-Burmese and Rangoon analyses: a necessary distinction

A further text-only source review located the Burmese entries in Namkung (ed.), *Phonological Inventories of Tibeto-Burman Languages*, STEDT Monograph 3 (1996), pp.61-66. The compendium explicitly distinguishes three source profiles:

- **Burmese (Written)**: the entry cites Benedict 1976, pp.iv-ix, and says that additional phonological information was supplied by James A. Matisoff. Its note states that medial /-w-/ belongs to the syllable rhyme, while /-y-/ and /-r-/ are treated as components of the initial consonant cluster (STEDT pp.61-62; quoted source note points to Benedict p.v).
- **Rangoon — Burling 1967**: the compendium reports /-y-/ and /-w-/ medials and source-specific distribution constraints. Burling's data were collected or personally checked with speakers, largely students at the University of Rangoon in 1959-60; the inventory is cited to pp.13-15 of Burling (STEDT pp.63-64).
- **Rangoon — Roop 1972**: the compendium also reports /-y-/ and /-w-/ medials with a different set of onset restrictions; it describes /r/ as a voiced flap or spirant appearing only in borrowings (Roop pp.xi-xiii; STEDT pp.65-66).

These descriptions must not be collapsed into one universal mapping. The Written Burmese entry's phonological segmentation, Burling's mid-20th-century Rangoon inventory, Roop's Rangoon description, and Ishida's modern orthographic-medial analysis are different source profiles and analytical levels. In particular, the Benedict notation /-r-/ is not automatically the same thing as modern Myanmar Unicode U+103C or a contemporary surface [r]. Likewise, a written source's /-w-/ as rhyme component does not by itself settle whether modern U+103D is a glide, a vowel onglide, or a context-dependent orthographic marker.

The STEDT volume states © 1996 Regents of the University of California, All Rights Reserved. Only factual claims and bibliographic pointers are recorded; no inventory tables or lexical data are copied into the repository. No runtime rule is enabled. Both new matrix entries remain WITHHELD pending a direct historical mapping, modern profile reconciliation and expert review.

## 10. Historical spelling changes and the Written/Spoken distinction

Two further text sources materially clarify why the historical medial notation cannot be projected directly onto modern Burmese output.

### 10.1 Nishi (1997): written standards are period-specific

Nishi distinguishes successive written standards: Old Written Burmese (OWB), Middle Written Burmese (MWB), Early Modern Written Burmese (EModWB), and Modern Written Burmese (ModWB). He describes the second standardization, around the end of the fourteenth century, as replacing OWB medial -l- with -r- and -v- according to the initial consonant. In EModWB, medial -y- was inserted between velar k-/kh- and written rhyme -i; Nishi says this reflects a phonemic change (printed pp.977-978).

Nishi also explicitly warns against equating written and spoken systems. The phonological systems of period-specific Written Burmese (the High variety) and the corresponding spoken variety (the Low variety) are not identical, and their historical periods are not coterminous (printed pp.980-981). Reading forms and spoken forms may differ. This is directly relevant to the pipeline: orthographic medial signs and historical spellings must not be treated as self-sufficient modern Yangon phonetic labels.

### 10.2 Matisoff (2003): historical *r > y and limits of Written Burmese evidence

Matisoff describes the palatalization of *r > y in Burmese in both initial and medial position, explicitly giving WB *-r- > Modern Burmese -y- (p.56). Later, he states that Written Burmese is not a reliable language for establishing the distinction among proto-medials *-r-, *-l- and *-y-. His examples show historical *-l- yielding WB -y- after velars and WB -r- after labials, with exceptions and spelling vacillation in inscriptions (pp.70-71).

### 10.3 Reconciliation and implementation consequence

The STEDT/Benedict Written Burmese entry, Nishi's periodized orthographic history, Matisoff's comparative sound-change analysis, and modern Yangon phonological descriptions are not contradictory one-to-one tables. They address different stages and levels:

1. historical proto-medial reconstruction;
2. Old and later Written Burmese spelling conventions;
3. phonemic changes between historical stages;
4. modern spoken Burmese;
5. current Unicode codepoint sequences.

The historical sequence provides a reason that written -r- and -y- notation can be confused or merge in later Burmese; it does **not** provide a direct mapping from U+103B or U+103C to a unique current IPA segment. The two new matrix rows and evidence-only rules remain WITHHELD. No runtime mapping has been enabled.

Nishi's article is available through the National Museum of Ethnology repository (DOI 10.15021/00004135). Matisoff's *Handbook of Proto-Tibeto-Burman* is © 2003 Regents of the University of California; only factual claims and page locators are recorded, not tables or lexical data.

## 11. Textual evidence for contextual voicing sandhi in Standard Burmese

Nishi (1998), *The Development of Voicing Rules in Standard Burmese* (BNME 23(1), pp.253-260; DOI 10.15021/00004129), supplies a text-only description of two contextual voicing patterns:

1. In an atonic-syllable environment C1aC2, if both consonants are among /p t t c k s/, both may become voiced. Nishi states that this pattern is generally observed but not obligatory throughout Standard Burmese and has many variables and exceptions.
2. In close juncture, an eligible following initial with a voiced counterpart becomes voiced after a non-stop tonal rhyme, within a word or a phrase containing postpositions. Nishi reports that the Myanmar-English Dictionary (1993) uses lexical phonemic transcriptions derived from this second rule.

The source is explicit about the limits of its variety label: “Standard Burmese” is not a well-defined variety, but a broad Rangoon-Mandalay profile with social and regional subvarieties (note 1). Nishi compares regional evidence: Intha, Taungyo and Danu lack these rules at the phonemic level; Arakanese, Tavoy and Mergui show only the first; Yaw shows the first and second with exceptions.

Implementation consequence: these are contextual phonological rules, not grapheme-to-phoneme substitutions. The first is variable and exception-rich; the second depends on rhyme type, juncture, morphology/postpositions and profile. Both are registered as analysis-dependent evidence only. No global runtime voicing rule is enabled. The MLC dictionary claim is recorded as Nishi's report, not as a completed independent audit of the 1993 dictionary.

## 12. Hill (2019): high-value historical source target, full chapter not retrieved

Cambridge University Press confirms Nathan W. Hill's *The Historical Phonology of Tibetan, Burmese, and Chinese*, chapter 2 "Burmese", pp.46-83 (DOI 10.1017/9781316550939.003). The book's stated method is comparative sound-law analysis; the publisher excerpt currently accessible in this run covers the introduction and Tibetan chapter, not the Burmese chapter. The project owner confirms the necessary permissions, so rights are not the blocker. The remaining blocker is obtaining the full chapter bytes in this execution environment. No claim about Burmese medials is attributed to Hill until the chapter itself is inspected.

## 13. Green (2005): explicit spoken-vs-written transcription boundary

The online edition of *Studies in Burmese Linguistics* (ed. Justin Watkins, 2005) is explicitly licensed CC BY-SA 4.0 with permission of Pacific Linguistics. Antony Dubach Green's chapter “Word, foot and syllable structure in Burmese” (pp.1-26) is especially useful because its conventions distinguish two layers:

- Spoken Burmese is transcribed broadly according to IPA conventions, without excessive phonetic detail.
- Written Burmese orthographic forms are transliterated separately using ALA-LC. The volume gives the medial transliteration order y, r, l, v, h and notes that its tone diacritics differ from John Okell's system (front matter pp.xi-xv).

Green's modern spoken phonology describes major syllables as permitting simple C or complex CG onsets, while minor syllables permit only simple C onsets (pp.4-5). Examples include /pjaʔ/, /phjaʔ/, /kwɛ/, /khwɛ/, /mjouʔ/ and /nwe/. In reducing compounds, a complex onset may simplify by deleting its second consonant (pp.19-20). This is phonological evidence for the existence and prosodic conditioning of CG onsets, not a direct Unicode medial mapping.

Green states that /N/ is a placeless nasal excluded from onset position; only /ʔ/ and /N/ are permitted codas. /N/ is realized as nasalization on the preceding vowel, with approximate coronal articulation after monophthongs and approximate velar articulation after diphthongs (p.5, citing Bennett & Lehman 1994). This provides a clear source-specific relation between abstract /N/ and surface nasalization, but the project's broad/narrow IPA convention must still be selected before emitting a particular surface form.

## 14. SEAlang dictionary and text corpora: valuable text leads, research use authorized

SHACHI metadata identifies three linked SEAlang Burmese resources:

1. **SEAlang Burmese Dictionary** — about 35,000 entries, including spoken and literary styles, based on MLC 1986 orthography, with examples and/or etymologies in many entries. Its source is the MLC Myanmar-English Dictionary (1993), republished by Dunwoody Press in 1996 and used by SEAlang with permission. The 2008 SEAlang project description confirms that the Burmese dictionary interface accepts local orthography and IPA phonetic queries and displays IPA transliterations. Mya2Rom documentation also identifies MLCTS2 as used by the MLC dictionary and SEAlang. These statements may describe different layers (stored romanization versus an IPA interface field or conversion); the underlying entry/export schema is still unresolved. The project owner confirms permissions for research use and project ingestion. Do not treat the visible transcription as independently verified IPA gold until actual entries are inspected.
2. **SEAlang Burmese Text Corpus** — monolingual Burmese Internet texts sampled for research/education. SHACHI lists 612,692 collocates and 3,172,485 contexts served; these are service metrics, not verified corpus row/token counts. The project owner confirms research-use and ingestion permission.
3. **SEAlang Burmese Bitext Corpus** — translated words, phrases and sentences aligned sentence-by-sentence where possible; metadata lists 1,234,822 pairs served (not verified total corpus size) and attributes the source to SAY Project Burmese resources at NMSU CRL. The project owner confirms research-use and ingestion permission.

The live SEAlang dictionary and corpus endpoints returned gateway errors during this review, so no entry-level transcription or corpus record was inspected and no rows were imported. Permission is not the blocker; stable retrieval and inspection of the actual text/field schema are. These resources remain text-only candidates for lexical/context research, not IPA gold.

## 15. Nishi (1998): full Old Burmese text inspected; historical medials and dialect reflexes

The full text of Nishi's “Old Burmese: Toward the History of Burmese” (BNME 23(3), pp.659-692; DOI 10.15021/00004119) is now inspected and registered as a separate source, distinct from Nishi's 1998 voicing-sandhi article.

Key findings, with historical scope preserved:

1. **Old Written Burmese cluster taxonomy (§1.3, pp.660-661).** Nishi treats -h with sonorants (nasals, liquids and semivowels) as marking a voiceless/aspirated sonorant unit, not as an ordinary cluster. He calls -r-, -l-, -y- and -w- the actual medial clusters. This historical romanized notation is not equivalent to the modern Unicode medial HA sign U+103E.
2. **Old Written Burmese -l- (§2.1.1, p.663).** OWB has medial -l- in addition to -r-, -y- and -w-. Nishi proposes that -l- was later replaced by -y- after velars and by -r- after bilabials in Middle Written Burmese, with exceptions.
3. **Middle Burmese -r- / -y- distinction and merger (§2.1.1, p.663).** The two medials were distinct in MB and merged into -y- in Standard Early Modern Written Burmese. Modern dictionary Cr~Cy alternatives can therefore preserve historical/lexical variation; they are not a direct map from modern Unicode medial RA to /r/ or /j/.
4. **Great Consonantal Shift (§4, pp.670-671).** Nishi's tentative account includes Cr- > Cy- and r- > y- among a set of changes placed broadly between the early/mid 18th and early 19th centuries. He explicitly warns that the changes may not have been as neatly ordered across dialects as the scheme suggests.
5. **Cross-dialect cluster correspondences (Table 3, p.673).** Nishi compares OB velar and bilabial clusters with WB, Standard Burmese, Arakanese, Tavoyan, Intha and Minor Taungyo. Reflexes of historical -r-, -l- and -y- differ and sometimes alternate; he notes standard-variety interference and hypercorrection. This is direct evidence against a single universal modern medial mapping.

The paper also explicitly states that Nishi (1976) aimed to establish regular correspondences among Old Burmese, Written Burmese and Colloquial/Standard Burmese medials. This is a reliable secondary statement about the 1976 paper's purpose, but the 1976 paper itself has not been claimed as read.

Implementation/evidence changes:
- Added source NISHI1998_OLDBURMESE, four claims and four historical rules.
- Added 13 source-linked Nishi rows to the medial evidence matrix (one existing Nishi period row plus four taxonomy/history rows and nine cross-dialect cluster rows; total Nishi rows = 14). All remain WITHHELD and no modern Unicode mapping is inferred.
- Added tests that distinguish historical -h from modern U+103E, preserve the OWB -l- reflexes, the MB -r-/-y- merger, and the dialectal cluster correspondences.
- Added seven Nishi 1998 voicing examples to data/burmese/sandhi_evidence.csv. The slash-delimited outputs are explicitly stored as Nishi's traditional phonemic notation following Okell 1995, not project IPA; IPA values remain empty.
- No historical medial or voicing rule was promoted into the runtime.

## 16. Text-source authorization and external corpus quality/access

The project owner confirms all required permissions for text-only research use and project ingestion of the listed textual sources. Public catalogue/license metadata remains recorded accurately, but permission is no longer treated as a research-processing blocker.

The Myanglish raw CSV is 2-column (myanmar,myanglish), while its README metadata/viewer exposes an additional official_standard field; that field remains unverified. The README itself describes a non-standardized, predominantly single-author romanization style, not IPA.

The myX orthography corpus is a work-in-progress text correction dataset, not an IPA corpus. Manual inspection found a target_words mismatch in hcara_phonetic.csv and multi-substitution examples in phet_bet_phonetic.csv. The resource is quarantined for row-level quality review and deduplication, not blocked by permission.

The 8.8 MB John Okell corpus is now reachable through the Zenodo direct text endpoint (HTTP 200, text/plain; charset=utf-8). The retrieved 8,809,265-byte sequence matches Zenodo MD5 f020d7bbcf9857631094a8861143d18f; SHA-256 is 6bbafd699c587876317f6e0535b9dd8f9ec87c15efe4b7e65a8c7362ebcdbf4c. It has 19,565 CRLF-terminated lines, 67 numbered heading lines, 21 BOM markers, one NUL at line 9,300, non-NFC text, zero U+FFFD and 73 unique Myanmar code points. Line profiling found 295 repeated nonblank line forms / 1,008 excess occurrences and 23 repeated paragraph forms; these include recurring titles, headers and dividers and are not duplicate-document counts. Raw medial codepoint and substring counts are stored separately as ORTHOGRAPHIC_ONLY. No text rows were imported into runtime, no IPA schema/labels were identified, and the corpus is not IPA gold. Status is PARTIAL / CONTENT AND BYTE INTEGRITY VERIFIED; TEXT QUALITY AUDIT PENDING. SEAlang entry/corpus schema remains unresolved. No audio was used or accessed. Independent expert-adjudicated IPA gold remains 0 and empirical IPA accuracy remains null.


## 17. Okell (1995): explicit WB/SB separation and regional medial inventories

The complete text of John Okell's *Three Burmese Dialects* (Pacific Linguistics A-83, pp.1-138) is now inspected. This is a major addition because it compares Written Burmese (WB) and Standard Burmese as spoken (SB) with three separate regional profiles: Arakanese (AR), Intha (IT) and Tavoyan (TV).

### 17.1 Arakanese: WB r/y distinction retained

Okell states that Arakanese preserves the distinction between WB r and y, while SB has merged WB r with y in speech. The material analyzed is principally Sit-twe District speech; Okell says it has high prestige and tends to be treated as the Arakanese standard. He also documents internal Arakanese subvarieties and warns against describing AR as simply an older or purer SB: both varieties have undergone different mergers and splits.

### 17.2 Intha and Tavoyan: medial /l/ absent from SB

Okell's Intha phoneme inventory includes restricted medial /y/, /l/ and /w/ combinations. His Tavoyan inventory likewise includes medial /y/, /l/ and /w/, and explicitly describes /-l/ as a lateral medial consonant not present in SB. The combinations are constrained by the initial consonant class; they are not an unrestricted combinatorial inventory.

### 17.3 Transcription convention and evidence boundary

Okell identifies WB and SB as distinct reference systems. His dialect texts are phonemically transcribed, with limited allophonic alternatives where a closer approximation to actual pronunciation is useful. The book's transcribed examples are therefore valuable source-specific phonemic evidence, but not an independently adjudicated project IPA gold set. This pass inspected the written tables and prose only; no recordings or audio were accessed.

### 17.4 Repository changes

- Added source OKELL1995_THREE_DIALECTS.
- Added seven source claims covering WB/SB separation, Arakanese r/y preservation, Intha/Tavoyan /l/ inventories, transcription convention and the Sit-twe profile.
- Added two dialect-dependent evidence rules and three medial matrix rows for Arakanese, Intha and Tavoyan. All rows remain WITHHELD from runtime.
- Added regression tests ensuring these regional profiles are not projected onto Standard Burmese/Yangon.

This source strengthens the case for distinct source-profile handling. It does not supply a direct modern Yangon Unicode-to-IPA mapping.


## 18. Okell (1969): authoritative colloquial Burmese grammar target

John Okell's *A Reference Grammar of Colloquial Burmese* (two volumes, 498 pp., Oxford University Press, 1969) is now registered as a primary text-source target. Its bibliographic identity is confirmed by Glottolog and library catalogues. Nishi (1998) explicitly cites Okell 1969, §§17-20, for the two voicing-sandhi patterns; Okell (1995) identifies it as the reference description of Spoken Burmese.

The full grammar was not retrieved in this execution, so no phonological claims are attributed directly to it. The project owner confirms research-use permission; the remaining gate is obtaining the text bytes and inspecting the exact sections/page locators. This is a high-priority source for checking the modern colloquial/Standard Burmese baseline before any contextual rule is considered for runtime.


## 19. Okell's A Corpus of Modern Burmese: text access and first-pass content audit

The Zenodo record for John Okell's *A Corpus of Modern Burmese* (DOI 10.5281/zenodo.1202324) lists an 8.8 MB `allfiles.txt` file compiled in the 1990s and converted to Unicode. The direct file endpoint returned HTTP 200 with content type `text/plain; charset=utf-8` during a text-only Firecrawl extraction on 2026-11-13. The retrieved UTF-8 byte sequence is 8,809,265 bytes; its MD5 exactly matches Zenodo's provider checksum `f020d7bbcf9857631094a8861143d18f`, and its computed SHA-256 is `6bbafd699c587876317f6e0535b9dd8f9ec87c15efe4b7e65a8c7362ebcdbf4c`. It has 19,565 CRLF-terminated lines (19,566 split segments including the final empty segment) and 19,565 CRLF delimiters, 67 numbered heading lines, 21 BOM markers (one leading and 20 embedded), one NUL in line 9,300, non-NFC text, zero U+FFFD and 73 unique Myanmar code points. Exact line profiling found 295 repeated nonblank line forms with 1,008 excess occurrences and 23 repeated paragraph forms; repeated titles, headers and divider motifs are not evidence of duplicate documents. The byte-identical external file was not committed to the repository.

### 19.1 Observed content and structure

Targeted inspection of the extracted text reports:
- valid UTF-8 and modern Myanmar Unicode; 19,565 CRLF-terminated lines (19,566 split segments including the final empty segment) with 19,565 CRLF delimiters, an initial BOM, one NUL, non-NFC text, zero U+FFFD characters and 73 unique Myanmar code points;
- Burmese and English content;
- 67 numbered heading lines across multiple embedded texts, with dates, headings and speaker labels;
- both dialogue/speech transcripts and prose/articles/tables;
- localized legacy encoding/glyph corruption in some foreign technical terms and computer terminology.

These are corpus-content observations, not a validated corpus schema. The exact document count, source provenance for each section, duplicate rate and boundary integrity remain unmeasured. Do not normalize or silently repair corrupted forms in the source copy.

### 19.2 Research value and limits

The resource can support text-only discovery of lexical forms, spelling variation, phrase context and candidate written examples. Its dialogue/transcript-like content is still text and does not authorize audio inference. No IPA annotation schema, phonetic label field or independently adjudicated IPA values were identified. It must not be treated as a pronunciation gold set or used to score G2P accuracy.

The Zenodo Rights/License field remains blank while the European Language Grid catalogue lists CC BY 4.0. Project-owner permission for research use and internal ingestion is confirmed; preserve both facts separately for attribution and downstream publication review.

### 19.3 Acceptance gate

Status: **PARTIAL / CONTENT AND BYTE INTEGRITY VERIFIED; TEXT QUALITY AUDIT PENDING**.

Before importing corpus rows, retain a byte-identical pinned artifact, calculate SHA-256, count documents and lines, audit Unicode normalization and malformed codepoints, profile repeated/template passages, identify section-level provenance where possible, and record corruption without silently rewriting source text. Any extracted lexical examples must retain document/section locators and must remain text evidence rather than IPA gold.


## 20. Okell corpus: orthographic-only medial frequency profile

A raw Unicode profile was computed over the complete text-only file identified by SHA-256 `6bbafd699c587876317f6e0535b9dd8f9ec87c15efe4b7e65a8c7362ebcdbf4c`. The profile is stored in `data/burmese/okell_text_corpus_orthographic_profile.csv`.

| Myanmar code point | Raw occurrences |
|---|---:|
| U+103B medial YA | 50,072 |
| U+103C medial RA | 73,107 |
| U+103D medial WA | 49,248 |
| U+103E medial HA | 50,869 |

Raw substring counts include `မြန်` 659, `မြန်မာ` 288, `မြန်မာနိုင်ငံ` 45, `မြန်မာစာ` 18 and `မြန်မာ့` 27.

These are Unicode scalar and substring counts over the raw, non-NFC, mixed-source text. They are not token counts, syllable counts, onset/rime distributions, or evidence that a Unicode medial has a particular pronunciation. Repeated source material is included; no normalization, tokenization or deduplication was applied. This profile is useful only for orthographic coverage and candidate written-example discovery. It does not create IPA gold or activate runtime rules.


## 21. Full-text audit: Thu et al. (2016), Hlaing & Mikami (2014), Oo et al. (2020)

The complete PDF texts were inspected in a text-only workflow. No audio was accessed, played, processed, annotated or used.

### 21.1 Thu et al. (2016): benchmark methodology and transcription boundary

The study uses 25,300 words from the Myanmar Language Commission Dictionary (Lwin 1993): 25,000 randomized training words, three open test sets of 100 words each, and a separate 100-word closed test drawn from training. It reports 2,393 graphemes, 1,864 unique pronunciations and 113 unique phonemes, but no complete formal phone inventory or transcription specification. Its examples are romanized strings such as `k`, `kh`, `wa:`, `wa.`, `jaun:` and `jwe'`; they must not be treated as project IPA.

Seven approaches are compared: S-AROW, CRF, JSM, PBSMT, RNN, SVM/KyTea and WFST/Phonetisaurus. PER is phoneme-level Levenshtein error (insertions, deletions, substitutions) computed with SCLITE over syllable-segmented words. Reported open-set PER includes WFST 14.7 (open1), 11.4 (open2), and CRF/WFST 15.7 (open3); PBSMT reports 16.1, 13.1 and 22.0. The zero closed-set results for some systems are not independent generalization evidence because the closed set is drawn from training. Manual review categories are voicing, tone, consonant and vowel; voicing errors are reported as most frequent, but no complete numerical table is supplied.

The paper does not specify a regional dialect or speaker-selection protocol, does not fully explain dictionary pronunciation annotation, and evaluates syllables within words rather than sentence-level contextual pronunciation. It is benchmark-methodology evidence, not an independent Yangon IPA gold set. The underlying MLC dictionary redistribution rights are not established by the paper citation.

### 21.2 Hlaing & Mikami (2014): orthographic FST, not G2P

The paper defines an orthographic Unicode syllable grammar: `S = I | N | P | X`; for ordinary syllables, `X = C M* V* (C K)? D*`, where C is consonant, M medial, V dependent vowel, K vowel-killer/asat and D tone mark. Separate transducers handle irregular forms including kinzi, stacking, repetition, Great SA, contraction and loan words. The system inserts orthographic syllable boundaries; it does not produce phonetic syllables or IPA.

The evaluation uses all 11,732 distinct words from Myanmar Language Commission's *Myanmar Orthography* (2006, 3rd ed.), implemented with SFST-PL. Table 4 reports 11,092/11,092 standard words correct and 245/253 stacking words correct, with overall 99.93% word-level accuracy. The paper is internally inconsistent: the abstract/Table 6 state 32,238 syllables while §6.1 states 32,283; Table 4 implies eight stacking errors while adjacent prose says nine. No formal boundary precision/recall, independent annotator agreement or train/test split is specified. The 99.93% must never be described as pronunciation/G2P accuracy.

### 21.3 Oo et al. (2020): text-side G2P architecture and tone analysis

The text front end is word segmentation → text normalization → G2P → phonemes. G2P is a Thrax weighted FST from Myanmar graphemes to IPA, with orthographic cleanup/reordering, core grapheme-phoneme rewrites, syllable-position-dependent changes, phonological transformations and pronunciation exceptions.

The paper reports 88 symbols (34 consonants and 54 vowels) and four tone categories—low, high, creaky and checked—whose realization involves pitch, contour, duration and phonation. It uses /N/ for a placeless nasal or nasal quality; this notation alone does not decide the project's abstract /N/ versus surface nasalization question. Speakers were native Burmese volunteers recorded in Yangon, aged 25–35, but the paper does not state a dialect label. Location is not a dialect classification.

The paper describes SLR80 as 2,528 utterances from 20 female speakers and states CC BY-SA 4.0. Its web-crawled segmentation corpus/models are explicitly not public domain. The normalization and G2P grammars are described as open-source at Google Language Resources paths, but the paper does not state a separate license for the grammar files. Do not infer a grammar license from the phrase "open-source". No audio was accessed in this review.

### 21.4 Consequences for implementation and research status

- Preserve Hlaing & Mikami as structural-parser evidence only.
- Preserve Thu et al. as a historical G2P benchmark with explicit train/test leakage caveats and undefined romanized phone notation.
- Use Oo et al. as an architectural and source-specific four-tone comparator, not as a complete consensus model or a license grant for every associated resource.
- Nishi's full 1998 voicing paper has now been retrieved and inspected; see §22. Its example provenance is Okell (1969), while its transcription convention follows Okell (1995).
- Do not activate medials, tone, /N/, coda or voicing rules without profile-matched independent adjudication.
- Independent project IPA gold remains zero; empirical accuracy remains null.


## 22. Nishi (1998): full-text audit of Standard Burmese voicing sandhi

The complete eight-page article, *The Development of Voicing Rules in Standard Burmese*, was retrieved from the National Museum of Ethnology repository and read in text/PDF mode. DOI: 10.15021/00004129; printed pp.253–260. No audio was accessed.

### 22.1 Two synchronic patterns

1. **Atonic C1aC2 pattern.** When an atonic /a/ syllable is followed by C2 and both C1 and C2 are voiceless unaspirated stops, affricates or sibilants with voiced counterparts (/p t t c k s/ in Nishi's notation), both consonants voice. Nishi gives /gaba/, /dagaun/ and /daji/ examples. He explicitly says the rule is generally observed but not obligatory throughout Standard Burmese and has variables/exceptions.
2. **Post-nonstop tonal-rhyme pattern.** An eligible initial C voices after a non-stop tonal syllable in close juncture, within a word or phrase with postposition(s). The listed class includes unaspirated and aspirated stops/affricates and sibilants with voiced counterparts. Examples include /khayiga/, /yejan/, /takhuzi/ and /ounzi/.

Nishi argues that weakening/atonicization is unpredictable and sometimes optional and should not be stated as part of the voicing sandhi rule itself. The project must therefore represent atonicization and voicing as separate operations/conditions rather than collapsing them into a single grapheme-triggered rewrite.

### 22.2 Transcription and example provenance: an important correction

Nishi explicitly states that his phonemic transcription follows Okell (1995), *Three Burmese Dialects*, except for specified symbol choices, and differs from Okell (1969). However, footnote 3 says that all examples in the paper are quoted from Okell (1969), *A Reference Grammar of Colloquial Burmese*, §§17–20.

Thus:
- **notation convention:** Okell (1995);
- **example source:** Okell (1969), §§17–20;
- **stored slash-delimited outputs:** Nishi's source-specific traditional phonemic forms, not project IPA.

The seven rows in `sandhi_evidence.csv` are retained with this distinction explicitly recorded. No IPA value is inferred.

### 22.3 Historical development and dialect comparison

Nishi proposes four stages: (1) voicing of nonaspirated stops/affricates/sibilants; (2) atonicization of some non-initial syllables; (3) a second voicing rule applying to C1; and (4) later voicing of aspirated stops/affricates. The ordering of the later C1 and aspirated-series rules may differ among subvarieties because atonicization remains optional.

The dialect comparison reports:
- Intha, Taungyo and Danu: no voicing sandhi at phonemic level;
- Arakanese, Tavoy and Mergui: first pattern only;
- Yaw: first and second patterns, but with contexts where the Standard Burmese patterns do not apply.

The paper's Taungyo evidence is specifically Minor Taungyo. It also cautions that regional dialects contain subdialects and internal variation.

Nishi's note 1 defines Standard Burmese broadly as spoken and written forms across an imprecisely bounded Rangoon–Mandalay area, with social and regional subvarieties. It is not a narrow modern Yangon reference profile.

### 22.4 Exceptions and limits

Nishi leaves several exceptions unexplained and tentatively discusses analogy, borrowing and Written Burmese influence. He argues that first-pattern voicing is a result of drift or convergence, not a feature traceable to a single common origin. The article therefore supports historical and dialect-comparative evidence, but not universal automatic voicing.

### 22.5 Registry and implementation consequences

Added four claims: example provenance, separation of atonicization from voicing, dialect-specific pattern distribution, and unresolved exceptions. Updated the source scope and corrected all seven sandhi records to distinguish Okell (1969) example provenance from Okell (1995) transcription convention.

No runtime rule was promoted. The existing analysis-dependent status remains. Independent adjudicated IPA gold remains zero and accuracy remains null.

## 23. Nishi (1997): full-text check of written-medial periodization

The complete PDF of *The Orthographic Standardization of Burmese: Linguistic and Sociolinguistic Speculations* (BNME 22(4), pp.975–999; DOI 10.15021/00004135) was inspected.

- Nishi distinguishes OWB, MWB, EModWB and ModWB orthographic standards.
- He states that OWB medial -l- was replaced by -r- and -v- according to initial-consonant class around the end of the fourteenth century.
- He identifies insertion of medial -y- between written velar k-/kh- and written -i(C)/-i as a key EModWB reform reflecting a phonemic change between MWB and EModWB.
- He explicitly distinguishes written-standard periods from phonological periods and frames each Written Burmese system as a High variety (H) against corresponding Spoken Burmese as Low variety (L); reading and spoken forms can differ.
- Scope limitation: the article's stated focus is rhyme writing systems, with initials discussed only when necessary. It is not a complete medial inventory and supplies no direct mapping to modern Unicode medial code points or modern Yangon pronunciation.

This confirms the existing Nishi 1997 historical-medial matrix row as orthographic/historical evidence only. Added CLM-NISHI97-SCOPE-001 to make the article's coverage limitation explicit. No runtime rule is promoted.

## 24. MLC 1978 spelling book: separate catalogue lead from the Concise Dictionary

A new National Diet Library of Japan catalogue record identifies *မြန်မာစာလုံးပေါင်းသတ်ပုံကျမ်း* as a Burmese-language orthography/spelling reference published by the Myanmar Language Commission in 1978 (record R100000136-I1970023484907173422). The record describes a physical book and its subject as Burmese orthography/spelling; it does not expose the book's pages or pronunciation/transcription material.

Allott's inspected 1985 chapter supplies a useful distinction: it says the MLC spelling book was first drafted in 1968, fundamentally revised, and finally published in 1978; in the following paragraph it separately describes the Concise Burmese Dictionary as five parts, from late 1978 to 1980, with official spelling and pronunciations for included entries (ANU PDF lines 10082–10113). This is consistent with two separate publications, but exact title identity and relationship must be verified from title pages, not inferred from the catalogue translation.

The new catalogue record and claim are bibliographic/documentary only. No book contents, MLCTS table, IPA values, or dictionary entry transcription have been inspected. This is an access lead, not a linguistic rule or a cleared primary-source transcription source.

## 25. Retrieval routes for the 1978 MLC spelling book

CiNii Books record BA69415754 provides the fuller extent as 28, 379 pages, 17 cm, and lists holdings at Osaka University and Tokyo University of Foreign Studies (two locations). Google Books record _V1LAAAAMAAJ identifies the original as held by the University of Michigan and a 379-page scan digitized in 2007. The surfaced Google Books record exposes snippet-view metadata; it does not establish that the entire scan can be read or downloaded.

These records make the 1978 spelling book a concrete retrieval target. They do not provide inspected primary text. The next step is to request a copy through a holding library or inspect any accessible Google Books pages, then record title-page identity and page-located contents. No pronunciation, MLCTS or IPA field is asserted.

## 26. MOW lexical candidates for text-based follow-up of `any` and `ui`

The existing MOW v0.1.3 orthographic suffix tables provide concrete lookup keys for the two highest-priority crosswalk groups. Counts below are distinct MOW lemma matches, not phonetic tokens:

| Group | Myanmar suffix | Lemma matches | Example MOW lemmas |
|---|---|---:|---|
| `any` | ဉ် | 6 | `ဥယျာဉ်`, `တိရစ္ဆာန်ဥယျာဉ်`, `ယာဉ်`, `ယဉ်` |
| `any` | ည် | 13 | `ပြည်`, `မြန်မာပြည်`, `လက်ဖက်ရည်`, `ရှည်` |
| `any:` | ဉ်း | 1 | `အကျဉ်း` |
| `any:` | ည်း | 6 | `စုစည်း`, `နည်း`, `လက်သည်း`, `အသည်း` |
| `any.` | ဉ့် | 0 | — |
| `any.` | ည့် | 5 | `ကြည့်`, `ဖြည့်`, `မွန်းတည့်`, `မှည့်`, `အမည်မှည့်` |
| `ui` | ို် | 0 | — |
| `ui` | ို | 15 | `ချို`, `ငို`, `ဆို`, `တို`, `မှို`, `အို` |

All values are copied from the repository's generated MOW suffix-match output. This is an orthographic candidate list for subsequent text lookup. Some words may contain the suffix as part of a larger orthographic structure; no syllable segmentation, rime identity, tone or pronunciation is implied. The group-level `any` conflict remains unresolved; `ui` remains only partly covered in R12A. No IPA or runtime rule is promoted.

## 27. Wiktionary word-level examples refine the `any`, `any:` and `ui` collision audit

The MOW orthographic candidates were looked up in existing Wiktionary text entries. These pages expose both MLCTS and IPA fields, allowing a limited secondary-source comparison:

| MOW candidate | Myanmar source unit | Wiktionary MLCTS | Wiktionary IPA | Evidence interpretation |
|---|---|---|---|---|
| ဥယျာဉ် | ဉ် | `u.yyany` | `/ʔṵjɪ̀ɴ/`, `/ʔújɪ̀ɴ/` | First side of `any` |
| ပြည် | ည် | `prany` | `/pjì/` | Second side of `any`; differs from first example |
| အကျဉ်း | ဉ်း | `a.kyany:` | `/ʔət͡ɕɪ́ɴ/` | First side of `any:` |
| နည်း | ည်း | `nany:` | `/nɛ́/`, `/ní/` | Second side of `any:`; distinct senses have distinct listed pronunciations |
| ချို | ို | `hkyui` | `/d͡ʑò/` | `ui` second side only |
| ဆို | ို | `hcui` | `/sʰò/` | `ui` second side only |
| တို | ို | `tui` | `/tò/` | `ui` second side only |

The `any` examples show why a shared MLCTS rime string must not be interpreted as proof of homophony. The `any:` examples supply word-level secondary evidence for distinct source-unit outcomes; the `နည်း` page also lists two pronunciations for different senses under the same spelling/MLCTS form. For `ui`, only `ို` has MOW-listed examples; `ို်` remains unattested in this small wordnet, so no paired comparison is possible.

The entries are secondary and may reflect the conventions of Wiktionary contributors; they do not adjudicate the original MLC specification. MOW matching remains exact Unicode suffix matching, not syllabification. No phonological rule, IPA gold item, or Ukrainian output has been promoted.

## 28. Additional secondary lexical evidence for `any.` collision

Text-only Wiktionary entries now provide one lexical example for each source-unit side of `any.`:

| Lemma | Source-unit ending | Wiktionary MLCTS | Wiktionary IPA |
|---|---|---|---|
| `စဉ့်` | ဉ့် | `cany.` | `/sɪ̰ɴ/` |
| `ကြည့်` | ည့် | `krany.` | `/t͡ɕḭ/` |

The first word is not in the MOW suffix-match list; the second is. These are independent Wiktionary word entries, not a controlled minimal pair, not an MLC primary table, and not evidence that every lexical instance of the two finals has the same contrast. They justify changing the lexical audit from no word-level evidence to `SECONDARY_SOURCE_DISTINCTION` only. The MLCTS2 crosswalk status is kept in parity with the lexical audit. No runtime rule, IPA gold row or Ukrainian candidate is promoted. The source claim is `CLM-WIKTIONARY-ANY-DOT-WORD-LEVEL-EXAMPLES-001` under the existing `MYWIKTIONARY2026` source record.

## 29. Additional secondary lexical evidence for `aung`

Text-only Wiktionary entries supply one lexical example for each of the two orthographic endings in the `aung` collision group:

| Lemma | Source-unit ending | Wiktionary MLCTS | Wiktionary IPA |
|---|---|---|---|
| `ပေါင်` | ေါင် | `paung` | `/pàʊɴ/` |
| `တောင်` | ောင် | `taung` | `/tàʊɴ/` |

The onsets differ, but the rime sequence `/àʊɴ/` is the same in the two secondary transcriptions. `တောင်` is a MOW suffix candidate; `ပေါင်` is not. This is word-level secondary equivalence evidence, not a controlled minimal pair or a primary MLC specification. The lexical audit is updated to `SECONDARY_SYSTEM_EQUIVALENCE`; MLCTS2 status parity and regression tests are updated. No runtime, IPA gold or Ukrainian output is promoted. Claim: `CLM-WIKTIONARY-AUNG-WORD-LEVEL-EXAMPLES-001`.

### Exact-head verification for the `any.` and `aung` lexical-audit extension

- Code/data snapshot: `eb81bd29e9417ddbd6d541d54fce6d754b0bb8bd`.
- Required CI run **43513203135 SUCCESS** (duplicate exact-SHA run **43513212043 SUCCESS**): **251 Python tests + 66 subtests**, **20 Node tests**, **58 Playwright tests**; production build, generated-web-data freshness and Chromium installation passed.
- IPA-gold validator reports `NOT_READY_NO_ADJUDICATED_GOLD`; no independent gold entries or accuracy score are claimed. Optional Epitran raw-output diagnostic **43513212088 SUCCESS** is not an accuracy benchmark.
- `npm install` reports **one high-severity vulnerability**; no dependency upgrade was applied.
- Current registry: **80 sources / 138 claims**. Lexical audit distribution: **17 unadjudicated / 3 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 1 secondary one-side-only / 1 special non-rime**.
- All new lexical evidence remains secondary. No runtime, IPA gold or Ukrainian candidate was promoted.

## 30. Additional secondary lexical evidence for `aung:`

Text-only Wiktionary entries supply a MOW-backed example for each of the two source-unit endings in the `aung:` group:

| Lemma | Source-unit ending | Wiktionary MLCTS | Wiktionary IPA |
|---|---|---|---|
| `ပေါင်း` | ေါင်း | `paung:` | `/páʊɴ/` |
| `ကျောင်း` | ောင်း | `kyaung:` | `/t͡ɕáʊɴ/` |

Both lemmas occur in the existing MOW suffix-match dataset. Their onsets differ while the secondary IPA rime sequence `/áʊɴ/` matches. The audit is therefore updated to `SECONDARY_SYSTEM_EQUIVALENCE`, and the MLCTS2 crosswalk status is synchronized. This is not a controlled minimal pair or a primary MLC specification. No runtime rule, IPA gold row or Ukrainian candidate is promoted. Claim: `CLM-WIKTIONARY-AUNG-COLON-WORD-LEVEL-EXAMPLES-001`.

## 31. Additional secondary lexical evidence for `auk`

Text-only Wiktionary entries provide one MOW-listed example for each source-unit side of the `auk` collision group:

| Lemma | Source-unit ending | Wiktionary MLCTS | Wiktionary IPA |
|---|---|---|---|
| `ပေါက်` | ေါက် | `pauk` | `/paʊʔ/` |
| `ကျောက်` | ောက် | `kyauk` | `/t͡ɕaʊʔ/` |

Both lemmas occur in the existing MOW suffix-match dataset. Their onsets differ while the secondary IPA rime sequence `/aʊʔ/` matches. The audit is updated to `SECONDARY_SYSTEM_EQUIVALENCE`, with MLCTS2 status parity and regression coverage. This is not a controlled minimal pair or a primary MLC specification. No runtime, IPA gold or Ukrainian candidate is promoted. Claim: `CLM-WIKTIONARY-AUK-WORD-LEVEL-EXAMPLES-001`.

## 32. Additional secondary lexical evidence for `a`, `a:` and `au`

Three more collision groups now have word-level Wiktionary evidence on both source-unit sides, using only MOW-listed lemmas:

| MLCTS group | Lemma | Source-unit ending | Wiktionary MLCTS | Wiktionary IPA |
|---|---|---|---|---|
| `a` | `အဝါ` | ါ | `a.wa` | `/ʔəwà/` |
| `a` | `အစာ` | ာ | `a.ca` | `/ʔəsà/` |
| `a:` | `ခါး` | ါး | `hka:` | `/kʰá/` |
| `a:` | `ကား` | ား | `ka:` | `/ká/` |
| `au` | `ပေါ်` | ေါ် | `pau` | `/pɔ̀/` |
| `au` | `ကြော်` | ော် | `krau` | `/t͡ɕɔ̀/` |

In each group, the onsets differ while the secondary IPA rime sequence matches. All six lemmas were present in the pre-existing MOW suffix-match list. These are secondary lexical equivalence examples, not controlled minimal pairs or primary MLC adjudication. The lexical audit and MLCTS2 status parity were updated, with regression tests and source claims `CLM-WIKTIONARY-A-WORD-LEVEL-EXAMPLES-001`, `CLM-WIKTIONARY-A-COLON-WORD-LEVEL-EXAMPLES-001` and `CLM-WIKTIONARY-AU-WORD-LEVEL-EXAMPLES-001`. No runtime, IPA gold or Ukrainian candidate is promoted.

## 33. One-sided secondary lexical attestation for `aung.`

Wiktionary lists `စောင့်` with MLCTS `caung.` and IPA `/sa̰ʊɴ/`. This MOW-listed lemma ends in ောင့်, the second source-unit side of the `aung.` group. No corresponding word-level example for ေါင့် was located. The lexical audit and MLCTS2 crosswalk now record `SECONDARY_ONE_SIDE_ONLY`; claim `CLM-WIKTIONARY-AUNG-DOT-ONE-SIDE-EXAMPLE-001` records the evidence. This does not adjudicate the collision and does not authorize runtime or Ukrainian mapping changes.

## 34. One-sided secondary lexical examples for `um:` and `un`

Two more groups now have a Wiktionary example on one source-unit side only:

| MLCTS group | Lemma | Source-unit ending | Wiktionary MLCTS | Wiktionary IPA |
|---|---|---|---|---|
| `um:` | `နှလုံး` | ုံး | `hna.lum:` | `/n̥əlóʊɴ/` |
| `un` | `ကုန်` | ုန် | `kun` | `/kòʊɴ/` |

Both lemmas are in the existing MOW suffix-match dataset. The opposite sides (ုမ်း and ုဏ် respectively) remain without lexical examples. The audit and MLCTS2 crosswalk now use `SECONDARY_ONE_SIDE_ONLY`; claims `CLM-WIKTIONARY-UM-COLON-ONE-SIDE-EXAMPLE-001` and `CLM-WIKTIONARY-UN-ONE-SIDE-EXAMPLE-001` are registered. These examples do not adjudicate either collision and do not authorize runtime changes.

## 35. One-sided secondary examples for `au:`, `im` and `im.`

Three further groups now have one-sided Wiktionary lexical attestations, all from MOW-listed candidates:

| MLCTS group | Lemma | Source-unit side | Wiktionary MLCTS | Wiktionary IPA |
|---|---|---|---|---|
| `au:` | `ကျော` | ော | `kyau:` | `/t͡ɕɔ́/` |
| `im` | `အိမ်` | ိမ် | `im` | `/ʔèɪɴ/` |
| `im.` | `စိမ့်` | ိမ့် | `cim.` | `/sḛɪɴ/` |

The opposite sides (ေါ, ိံ, and ိံ့ respectively) remain without word-level examples. The lexical audit and MLCTS2 crosswalk now record `SECONDARY_ONE_SIDE_ONLY`; the three source claims are registered. These examples are not collision adjudications and do not authorize runtime changes.

## 36. Final exact-head verification for this continuation — 2026-11-13

- Final tested code/data SHA: `62bea5a26012cb1ace4ce11579e17f4a780c3e1e`.
- Required CI **43516197628 SUCCESS** and duplicate exact-SHA run **43516203122 SUCCESS**: **251 Python tests + 66 subtests**, **20 Node tests**, **58 Playwright tests**; production build, generated-data freshness and Chromium installation passed.
- Optional Epitran raw-output diagnostic **43516203133 SUCCESS**; this is not an accuracy benchmark. IPA-gold validator remains `NOT_READY_NO_ADJUDICATED_GOLD` (0 independently adjudicated entries).
- `npm install` still reports **one high-severity vulnerability**; no unreviewed dependency upgrade was applied.
- Current evidence ledger: **25 groups = 6 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 7 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 149 claims**.
- All additions are secondary lexical attestations. No primary MLC rule, IPA gold row, runtime behavior or Ukrainian candidate was promoted.

## 37. One-side lexical attestation for `am:` — 2026-11-14

Wiktionary lists `လမ်း` with MLCTS `lam:` and IPA `/láɴ/`. It ends in `မ်း`, the first source-unit side in the `am:` collision group. The MOW suffix-match scan did not locate a lexical example ending in the other source unit `ံး`. The audit and MLCTS2 crosswalk now classify this as `SECONDARY_ONE_SIDE_ONLY`, not equivalence. Claim: `CLM-WIKTIONARY-AM-COLON-ONE-SIDE-EXAMPLE-001`.

This is a secondary lexical attestation only; it does not adjudicate the collision or authorize primary MLC, IPA gold, runtime or Ukrainian-output changes. The audit distribution is now **5 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 8 secondary one-side-only / 1 special non-rime** (25 groups total). Registry: **80 sources / 150 claims**. Exact-head CI pending.

### Exact-head verification for `am:` lexical attestation — 2026-11-14

- Verified code/data SHA: `73bfbd7d82f69bfa0e306d984a40fe2324fc3515`.
- Required CI runs **43519075644 SUCCESS** and **43519083741 SUCCESS** on the same SHA. Each completed **251 Python tests + 66 subtests**, **20 Node tests**, **58 Playwright tests**; production build, generated-data freshness and Chromium installation passed.
- Optional Epitran raw-output diagnostic **43519083746 SUCCESS**; diagnostic only, not an accuracy benchmark.
- IPA gold validator remains `NOT_READY_NO_ADJUDICATED_GOLD` (0 independently adjudicated entries). `npm install` reports **one high-severity vulnerability**; no dependency upgrade applied.
- Current ledger: 25 groups = **5 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 2 secondary distinction / 8 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 150 claims**.
- This verifies code/data/test consistency only. No primary MLC rule, IPA gold, runtime behavior or Ukrainian candidate was promoted.

## 38. Secondary lexical distinction evidence for `am.` — 2026-11-14

Wiktionary lists `စိမ့်` with MLCTS `cim.` and IPA `/sḛɪɴ/`, ending in `မ့်`, and `ကြံ့` with MLCTS `kram.` and IPA `/t͡ɕa̰ɴ/`, ending in `ံ့`. These have distinct rime realizations. The MOW scan contains `စိမ့်` and the compound `အိန္ဒိယကြံ့` as suffix-match candidates. The secondary lexical evidence conflicts with the vendor's same-output MLCTS2/IPA crosswalk. The audit and crosswalk now use `SECONDARY_SOURCE_DISTINCTION`; claim `CLM-WIKTIONARY-AM-DOT-LEXICAL-DISTINCTION-001` is registered.

This is not a controlled minimal pair or primary MLC adjudication. Do not treat the vendor crosswalk as resolved, and do not promote runtime, IPA gold or Ukrainian output. Current 25-group distribution: **4 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 3 secondary distinction / 8 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 151 claims**. Exact-head CI pending.

## 39. One-side lexical attestation for `au.` — 2026-11-14

Wiktionary lists `ဝပ်ရှော့` with MLCTS `waphrau.` and IPA `/waʔʃɔ̰/`. Its final syllable contains the source-unit side `ော့` in the `au.` collision group and its MLCTS rime suffix corresponds to `au.`. No MOW lexical example for the other source unit `ေါ့` was located. Audit and MLCTS2 crosswalk now record `SECONDARY_ONE_SIDE_ONLY`; claim `CLM-WIKTIONARY-AU-DOT-ONE-SIDE-EXAMPLE-001` is registered.

This is one-side secondary evidence only, not collision adjudication. Distribution: **3 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 3 secondary distinction / 9 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 152 claims**. Exact-head CI pending.

### Exact-head verification for `au.` lexical attestation — 2026-11-14

- Verified code/data SHA: `ffd08d7ae8e227ee19a86859de00b7d52f456ecf`.
- Required CI run **43519887514 SUCCESS**: **251 Python tests + 66 subtests**, **20 Node tests**, **58 Playwright tests**; production build, generated-data freshness and Chromium installation passed. Duplicate run **43519895530** was still completing at documentation time.
- Optional Epitran raw-output diagnostic **43519895542 SUCCESS**; diagnostic only, not an accuracy benchmark.
- IPA gold remains `NOT_READY_NO_ADJUDICATED_GOLD` (0 independent gold entries). `npm install` reports one high-severity vulnerability.
- Ledger: 25 groups = **3 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 3 secondary distinction / 9 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 152 claims**.
- Secondary evidence only; no primary MLC, IPA gold, runtime or Ukrainian output promotion.


## 40. One-side secondary lexical attestation for `um.` — 2026-11-14

Wiktionary lists `အုံ့` with MLCTS `um.` and IPA `/ʔo̰ʊɴ/`. The lemma ends in ုံ့, the second source-unit side of the `um.` group. It is not present in the MOW suffix-match inventory, so this is a secondary lexical attestation outside MOW, not a MOW-backed candidate. No word-level example for ုမ့် was located. The audit and MLCTS2 crosswalk now record `SECONDARY_ONE_SIDE_ONLY`; claim `CLM-WIKTIONARY-UM-DOT-ONE-SIDE-EXAMPLE-001` is registered.

This does not adjudicate the collision or authorize primary MLC, IPA gold, runtime or Ukrainian-output changes. Current 25-group distribution: **2 unadjudicated / 8 secondary equivalence / 1 secondary conflict / 3 secondary distinction / 10 secondary one-side-only / 1 special non-rime**. Registry: **80 sources / 153 claims**. Exact-head CI pending.
