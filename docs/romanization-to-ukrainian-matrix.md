# Burmese romanization → Ukrainian orthographic matrix

**Status:** PARTIAL — a romanization engine and UI card exist, but the current UI selects MLCTS2 (a modified, more phonetic system) rather than the orthographic MLCTS profile selected for the separate romanization mode. A complete MLCTS → Ukrainian syllable crosswalk is not yet implemented.
**Primary variety:** contemporary Standard Burmese; Yangon-oriented phonetics only where the evidence supports it.

## Standard selection

Select **Myanmar Language Commission Transcription System (MLCTS)** for the orthographic romanization mode. The upstream Mya2Rom documentation explicitly distinguishes:
- MLCTS: an **orthographical transcription system** created by the Myanmar Language Commission;
- MLCTS modified / MLCTS2: a more phonetic version used by the MLC Myanmar–English dictionary and SEAlang.

This distinction matches the product contract: the romanization tab represents written structure consistently, while the phonetic tab derives pronunciation through source phonology and IPA. MLCTS2 remains useful as a comparator/secondary display but must not be confused with the orthographic romanization mode.

Selection comparison:
| Candidate | Scope / strength | Decision |
|---|---|---|
| MLCTS (1980) | Orthographic transcription system attributed to the Myanmar Language Commission; intended for formal Burmese and useful in linguistic publications | SELECTED for the orthographic text mode; its implementation and row-level coverage still require independent verification |
| MLCTS modified / MLCTS2 | More phonetic variant associated with the MLC Myanmar-English dictionary and SEAlang | Not the orthographic mode; may be retained as a comparison profile |
| BGN/PCGN 1970 | Officially documented geographic-name system based on the 1907 government table; UNGEGN reports no UN-approved Burmese system and says this romanization is not reversible | Not selected for general text; keep as a geographic-name comparator |
| ALA-LC Burmese (2011) | Library cataloguing romanization table; authoritative for cataloguing scope | Candidate for future cross-check, not the selected default |
| Sawada Roman Transliteration System | Scholarly Basic-Latin script transliteration developed for transcribing Burmese script; its publisher notes limits for embedded Burmese forms in publications | Candidate for specialist/reversible orthographic comparison |

The choice is a project-specific best fit for the requested orthographic mode, not a claim that Myanmar has one universally accepted romanization standard. John Okell's guide surveys multiple systems and distinguishes transliteration, transcription and combined methods. Exact system choice must remain visible in metadata.

Sources:
- Mya2Rom upstream documentation: https://github.com/myanmaropenwordnet/mya2rom (documents the MLCTS / modified MLCTS distinction, implementation interface and upstream attributions).
- John Okell, A Guide to the Romanization of Burmese (2002): https://www.routledge.com/A-Guide-to-the-Romanization-of-Burmese/Okell/p/book/9781138406049
- Library of Congress, ALA-LC Romanization Tables, Burmese (2011): https://www.loc.gov/catdir/cpso/roman
- Hideo Sawada, Roman Transliteration System for Burmese Script (ILCAA / TUFS): https://lingdy.aa-ken.jp/en/publications/tools-and-archives/211110/
- UNGEGN, Burmese romanization status: https://unstats.un.org/unsd/geoinfo/ungegn/docs/8th-uncsgn-docs/crp/8th_UNCSGN_econf.94_crp.81.pdf
- BGN/PCGN, Romanization of Burmese, 1970 Agreement (official comparator): https://assets.publishing.service.gov.uk/media/5ab4dec7ed915d78bc23450f/ROMANIZATION_OF_BURMESE.pdf. This is a separate geographic-name romanization convention; it is not silently substituted for MLCTS.

## Licensing and provenance

The repository vendors Mya2Rom 0.4.4 and its CC-BY-SA-4.0 notice. Preserve the upstream attribution and license for copied vendor code/data. The Mya2Rom README says its extended romanization tables draw on Wikipedia's Burmese Alphabet and Wiktionary's Burmese transliteration tables; therefore each row must carry its actual source scope rather than being represented as a direct official MLC publication. Do not assume the Mya2Rom code license independently grants rights to unrelated dictionary/corpus data.

## Consonant-unit crosswalk (MLCTS romanization; Ukrainian is a project proposal)

| Burmese source onset | MLCTS form | Ukrainian candidate | Status / note |
|---|---|---|---|
| က | k | к | PROPOSED |
| ခ | hk | к' | PROPOSED; aspirated orthographic onset |
| ဂ / ဃ | g / gh | ґ / ґг | ANALYSIS_DEPENDENT; source distinctions retained |
| င | ng | нг | PROPOSED |
| စ | c | с | PROPOSED; do not infer /t͡s/ from Latin c |
| ဆ | hc | с' | ANALYSIS_DEPENDENT; keep distinct from စ |
| ဇ / ဈ | j / jh | дж / джг | ANALYSIS_DEPENDENT; exact target cluster requires review |
| ဉ / ည | ny | нь | PROPOSED |
| ဋ / တ | t | т | PROPOSED; source letters remain distinct in the source layer |
| ဌ / ထ | ht | т' | PROPOSED |
| ဍ / ဒ | d | д | PROPOSED |
| ဎ / ဓ | dh | дг | ANALYSIS_DEPENDENT; preserve orthographic contrast pending review |
| ဏ / န | n | н | PROPOSED |
| ပ | p | п | PROPOSED |
| ဖ | hp | п' | PROPOSED |
| ဗ / ဘ | b / bh | б / бг | ANALYSIS_DEPENDENT |
| မ | m | м | PROPOSED |
| ယ | y | й | PROPOSED |
| ရ | r | р | PROPOSED; orthographic form differs from ယ |
| လ / ဠ | l | л | PROPOSED |
| ဝ | w | в | PROPOSED |
| သ / ဿ | s | с | PROPOSED; preserve separate source graphemes |
| ဟ | h | г | PROPOSED under the project Ukrainian target policy |
| အ | (zero onset in MLCTS) | explicit zero onset | PROPOSED; do not delete its syllable-carrier role |

## Syllable/rhyme matrix contract

MLCTS includes orthographic conventions for dependent vowels, codas, virama/asat, medials, kinzi, independent vowels and punctuation. The upstream table is sequence-sensitive; the full source form must be parsed before rendering the MLCTS syllable. Do not treat each Latin character as an independent Ukrainian segment.

| MLCTS romanization unit | Ukrainian candidate | Status |
|---|---|---|
| a | а | PROPOSED |
| i | і | PROPOSED |
| u | у | PROPOSED |
| e | е | PROPOSED |
| o | о | PROPOSED |
| ai | ай | PROPOSED |
| au | ау | PROPOSED |
| ng (coda) | нг | PROPOSED; syllable-final role must be preserved |
| n (coda) | н | PROPOSED |
| m (coda) | м | PROPOSED |
| : / . length/checked markers | no direct letter by default | ANALYSIS_DEPENDENT; do not discard without recording the convention |
| MLCTS alternative or unresolved sequence | no guessed output | EVIDENCE_LIMITED |

This is a research crosswalk, not an adjudicated Ukrainian name standard. A table row may be promoted only after checking the upstream MLCTS definition, source orthographic context, Ukrainian target policy and a regression fixture.

## Implementation contract

- Romanization tab uses mya2rom(sourceUnit, "mlcts"), not "mlcts2".
- MLCTS2 may remain a separately labelled comparison profile; it is not the primary orthographic route.
- Preserve non-Myanmar text and punctuation exactly.
- Romanization → Ukrainian must be a separate syllable-level adapter with explicit source/MLCTS cross-checks. It must not call or reuse the IPA → Ukrainian adapter.
- For each source syllable, show the original Burmese form, MLCTS form, Ukrainian proposed syllable, context and evidence status.
- If the MLCTS output is ambiguous or no Ukrainian row exists, keep the romanization visible and mark Ukrainian output PARTIAL/UNSUPPORTED rather than inventing a conversion.

## Task ledger

| ID | Status | Acceptance |
|---|---|---|
| MYA-ROM-STD-001 | DONE_VERIFIED (source review) | MLCTS selected as orthographic profile; MLCTS2 retained only as comparator |
| MYA-ROM-PROFILE-001 | DONE_VERIFIED | Browser calls MLCTS; result card labels MLCTS; test-first exact sample proves MLCTS mrui. vs MLCTS2 mjou.; exact-head workflow 41229019002 passed |
| MYA-ROM-UA-001 | TODO | Independent MLCTS-syllable → Ukrainian adapter |
| MYA-ROM-MATRIX-001 | PARTIAL | Full consonant, medial, vowel, coda, independent vowel, kinzi, asat, numeral and punctuation inventory |
| MYA-ROM-LIC-001 | PARTIAL | Audit all vendored source components and preserve CC-BY-SA-4.0 attribution |
| MYA-IPA-001 | PARTIAL | Contextual vowel/coda/tone/phonation IPA coverage and independent lexical gold remain incomplete |
