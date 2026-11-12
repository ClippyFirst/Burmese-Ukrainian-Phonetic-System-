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
