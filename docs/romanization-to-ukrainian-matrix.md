# Burmese romanization → Ukrainian orthographic matrix

**Status:** PARTIAL — the orthographic MLCTS profile is now active and the full onset inventory has a machine-readable research crosswalk. The MLCTS → Ukrainian vowel/rime/syllable adapter and complete inventory are not yet implemented.
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

The canonical onset registry is [data/burmese/romanization_ukrainian.csv](../data/burmese/romanization_ukrainian.csv). It contains all 35 consonant/onset entries in the vendored MLCTS column, including distinct source graphemes that share a Latin form. It stores source locator, proposed Ukrainian candidate and uncertainty status for every row. The table below is a compact overview; the CSV is authoritative.

| Burmese source onset | MLCTS form | Ukrainian candidate | Status / note |
|---|---|---|---|
| က | k | к | PROPOSED |
| ခ | hk | к' | PROPOSED; aspirated orthographic onset |
| ဂ / ဃ | g / gh | — | EVIDENCE_LIMITED; no target value promoted |
| င | ng | нг | PROPOSED |
| စ | c | — | EVIDENCE_LIMITED; do not infer a target value from c alone |
| ဆ | hc | — | EVIDENCE_LIMITED; keep distinct from စ |
| ဇ / ဈ | j / jh | — | EVIDENCE_LIMITED; exact target cluster requires review |
| ဉ / ည | ny | нь | PROPOSED |
| ဋ / တ | t | т | PROPOSED; source letters remain distinct in the source layer |
| ဌ / ထ | ht | т' | PROPOSED |
| ဍ / ဒ | d | д | PROPOSED |
| ဎ / ဓ | dh | — | EVIDENCE_LIMITED; preserve orthographic contrast pending review |
| ဏ / န | n | н | PROPOSED |
| ပ | p | п | PROPOSED |
| ဖ | hp | п' | PROPOSED |
| ဗ / ဘ | b / bh | б / — | ANALYSIS_DEPENDENT; bh awaits review |
| မ | m | м | PROPOSED |
| ယ | y | й | PROPOSED |
| ရ | r | р | PROPOSED; orthographic form differs from ယ |
| လ / ဠ | l | л | PROPOSED |
| ဝ | w | в | PROPOSED |
| သ / ဿ | s | с | PROPOSED; preserve separate source graphemes |
| ဟ | h | г | PROPOSED under the project Ukrainian target policy |
| အ | (zero onset in MLCTS) | — | EVIDENCE_LIMITED; retain the syllable-carrier role, do not delete it |

## Syllable/rhyme matrix contract

The onset CSV does not imply that the rhyme inventory is complete. The vowel examples below are candidates only; length, coda and checked-syllable markers must be represented as structured MLCTS units before a Ukrainian syllable can be generated.

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
| MYA-ROM-MATRIX-ONSET-001 | DONE_VERIFIED | 35 MLCTS onset rows in data/burmese/romanization_ukrainian.csv; exact source inventory and provenance/status checks passed in workflow 41229245383 |
| MYA-ROM-MATRIX-001 | PARTIAL | Medial, vowel, coda, independent vowel, kinzi, asat, numeral and punctuation inventory still required |\n| MYA-ROM-OUTPUT-INTEGRITY-001 | DONE_VERIFIED | Basic Myanmar digits/punctuation and mixed text pass through; unsupported code points and orphan signs remain visible; exact-head CI 41243831142/41243825927 passed |
| MYA-ROM-LIC-001 | PARTIAL | Audit all vendored source components and preserve CC-BY-SA-4.0 attribution |
| MYA-IPA-001 | PARTIAL | Contextual vowel/coda/tone/phonation IPA coverage and independent lexical gold remain incomplete |



## Why MLCTS rather than BGN/PCGN 1970

The BGN/PCGN 1970 system is a legitimate, source-backed alternative, but its documented scope is geographical-name romanization. UNGEGN reports that Myanmar had no official national romanization system and that no Burmese system had been put forward to UN conferences; it identifies BGN/PCGN 1970 as the only known system at that time and notes that it is not reversible to the original script. The official PCGN guide itself is explicitly titled *Romanization of Burmese, BGN/PCGN 1970 Agreement* and says that some romanization choices depend on actual pronunciation.

For this project's **orthographic** mode, choose **MLCTS** instead: Mya2Rom's documentation identifies the Myanmar Language Commission Transcription System as an orthographical transcription system created by the MLC, and distinguishes it from modified MLCTS, described as more phonetic. That distinction fits the user-approved contract: the romanization tab represents written Burmese independently of the IPA-first pronunciation tab. The selected runtime profile is the standard `mlcts` column, not MLCTS-SL/MLCTS2. The current vendor table is a practical implementation source, not a substitute for obtaining and checking the original MLC publication; its rime inventory is therefore explicitly evidence-limited.

Primary/reference sources:
- UNGEGN, *Report on the Current Status of United Nations Romanization Systems for Geographical Names*, Burmese section (2013): https://unstats.un.org/unsd/ungegn/working_groups/wg5/documents/wgrr4burmese.pdf
- UK PCGN, *Romanization of Burmese*, BGN/PCGN 1970 Agreement (checked October 2017): https://assets.publishing.service.gov.uk/media/5ab4dec7ed915d78bc23450f/ROMANIZATION_OF_BURMESE.pdf
- Mya2Rom project documentation and attribution: https://github.com/myanmaropenwordnet/mya2rom (CC-BY-SA-4.0; its extended tables are attributed to Wikipedia/Wiktionary-derived material).

## Machine-readable MLCTS rime inventory

[data/burmese/romanization_rimes_inventory.csv](../data/burmese/romanization_rimes_inventory.csv) records the 94 rime keys present in the vendored Mya2Rom 0.4.4 `vowels` object and the exact second-column MLCTS form. This is explicitly a vendor-derived inventory, not a claim that every row was checked against an original Myanmar Language Commission publication. The Ukrainian candidate is intentionally blank and the status is `EVIDENCE_LIMITED` for every row until the MLCTS source form, syllable context and Ukrainian target value are independently adjudicated. Do not promote these rows to output mappings merely because the upstream library returns a Latin string.
