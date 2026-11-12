# Burmese romanization → Ukrainian orthographic matrix

**Status:** PARTIAL — the Ukrainian target crosswalk is populated and a runtime adapter now handles supported onset/medial/rime combinations. The MLCTS romanization source inventory remains vendor-evidence-limited; unsupported orthographic structures are withheld.
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

The canonical onset registry is [data/burmese/romanization_ukrainian.csv](../data/burmese/romanization_ukrainian.csv). It contains all 35 consonant/onset entries in the vendored MLCTS column, including distinct source graphemes that share a Latin form. It stores source locator, Ukrainian project candidate, target status and separate source-evidence status for every row. The table below is a compact overview; the CSV is authoritative.

| Burmese source onset | MLCTS form | Ukrainian candidate | Status / note |
|---|---|---|---|
| က | k | к | PROPOSED |
| ခ | hk | к' | PROPOSED; aspirated orthographic onset |
| ဂ / ဃ | g / gh | ґ / ґ' | PROPOSED; orthographic target convention |
| င | ng | нг | PROPOSED |
| စ | c | ц | PROPOSED; literal MLCTS letter rendering, not an IPA assertion |
| ဆ | hc | ц' | PROPOSED; aspiration marker retained |
| ဇ / ဈ | j / jh | дж / дж' | PROPOSED; jh keeps the project aspiration marker |
| ဉ / ည | ny | нь | PROPOSED |
| ဋ / တ | t | т | PROPOSED; source letters remain distinct in the source layer |
| ဌ / ထ | ht | т' | PROPOSED |
| ဍ / ဒ | d | д | PROPOSED |
| ဎ / ဓ | dh | д' | PROPOSED; MLCTS digraph retained distinctly from d |
| ဏ / န | n | н | PROPOSED |
| ပ | p | п | PROPOSED |
| ဖ | hp | п' | PROPOSED |
| ဗ / ဘ | b / bh | б / б' | PROPOSED; target marker preserves the MLCTS contrast |
| မ | m | м | PROPOSED |
| ယ | y | й | PROPOSED |
| ရ | r | р | PROPOSED; orthographic form differs from ယ |
| လ / ဠ | l | л | PROPOSED |
| ဝ | w | в | PROPOSED |
| သ / ဿ | s | с | PROPOSED; preserve separate source graphemes |
| ဟ | h | г | PROPOSED under the project Ukrainian target policy |
| အ | (zero onset in MLCTS) | ∅ | PROPOSED; explicit zero-onset token; retain source carrier and render the rime |

## Syllable/rhyme matrix contract

The 94-row rime inventory now carries a Ukrainian rendering for each observed MLCTS string. It is still a vendor-derived inventory, not a primary-source-verified complete MLC syllable inventory; contextual source segmentation and a runtime syllable adapter remain separate tasks.

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
| : (length notation) | ː | PROPOSED; retained as a length marker, not converted to a vowel letter |
| . (checked-syllable marker) | · | PROPOSED; retained as a distinct middle-dot marker |
| ' (when present) | ʼ | PROPOSED; apostrophe marker retained |
| c / k / p (coda spellings) | ц / к / п | PROPOSED; literal MLCTS-to-Ukrainian rendering, not a coda IPA claim |

This is a project orthographic crosswalk, not an adjudicated Ukrainian name standard or a pronunciation model. Source romanization provenance and Ukrainian target mapping are separate evidence dimensions.

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
| MYA-ROM-UA-TARGET-001 | DONE_VERIFIED | All 35 onset rows and 94 inventoried rime rows have non-empty Ukrainian target candidates; deterministic mapping and source-evidence status are asserted. Promote after exact-head CI. The rime source inventory remains vendor-derived. |
| MYA-ROM-UA-001 | TODO | Independent MLCTS-syllable → Ukrainian runtime adapter; execute the crosswalk without IPA fallback |
| MYA-ROM-MATRIX-ONSET-001 | DONE_VERIFIED | 35 MLCTS onset rows in data/burmese/romanization_ukrainian.csv; exact source inventory and provenance/status checks passed in workflow 41229245383 |
| MYA-ROM-MATRIX-001 | PARTIAL | Onset and vendor rime target tables are populated; complete source-verified medial, kinzi, asat, independent-vowel, numeral, punctuation and legal-syllable coverage remains open |\n| MYA-ROM-OUTPUT-INTEGRITY-001 | DONE_VERIFIED | Basic Myanmar digits/punctuation and mixed text pass through; unsupported code points and orphan signs remain visible; exact-head CI 41243831142/41243825927 passed |
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

[data/burmese/romanization_rimes_inventory.csv](../data/burmese/romanization_rimes_inventory.csv) records the 94 rime keys present in the vendored Mya2Rom 0.4.4 `vowels` object and the exact second-column MLCTS form. Every row now has a deterministic Ukrainian target rendering. `ukrainian_status=PROPOSED` refers only to the project’s letter-level target convention; `romanization_evidence_status=EVIDENCE_LIMITED` explicitly preserves the fact that these source keys are vendor-derived and are not individually verified against the original MLC publication.

## Ukrainian target convention for Latin MLCTS input — 2026-11-12

The Ukrainian candidate is a **letter-level orthographic rendering of the MLCTS Latin string**. It is not IPA, does not predict pronunciation, and does not use the phonetic IPA → Ukrainian adapter. The original MLCTS string and Burmese source unit must remain available in metadata.

- Onset digraphs are longest-match units: `hk → к'`, `gh → ґ'`, `hc → ц'`, `jh → дж'`, `ht → т'`, `dh → д'`, `hp → п'`, `bh → б'`. Plain `k/g/c/j/t/d/p/b` map to `к/ґ/ц/дж/т/д/п/б`; `ng → нг`, `ny → нь`.
- Remaining Latin letters use the explicit project table: `a → а`, `e → е`, `i → і`, `o → о`, `u → у`, `m → м`, `n → н`, `r → р`, `l → л`, `s → с`, `w → в`, `y → й`, `h → г`.
- Rime digraphs are longest-match: `ng → нг`, `ny → нь`, `ai → ай`, `au → ау`, `ui → уй`. Coda letters are rendered by the same literal letter table; this is not an IPA coda classification.
- MLCTS `:` is retained as `ː` and `.` as `·`; an apostrophe is rendered as Ukrainian modifier apostrophe `ʼ`. These markers are preserved rather than silently discarded or reinterpreted.
- The zero-onset carrier is represented by the explicit data token `∅`; it is not a deletion of the Burmese source character or the syllable nucleus.
- Every candidate row has `ukrainian_status=PROPOSED`. The additional `romanization_evidence_status=EVIDENCE_LIMITED` on vendor-derived tables prevents a proposed Ukrainian rendering from being mistaken for proof that the underlying MLCTS row is an official MLC form.

This crosswalk is intentionally a project convention and may be non-reversible. It makes all inventoried Latin strings readable in Ukrainian while preserving the source spelling and its notation markers; it does not establish phonological equivalence or expert approval.


## Runtime MLCTS → Ukrainian adapter — 2026-11-12

The romanization panel now invokes `src/web/romanization-ukrainian.js` for each source cluster after the existing Mya2Rom `mlcts` profile has rendered it. The adapter parses a longest-match onset, supported medial sequence (`y/r/w`) and exact rime key from the existing CSV crosswalks. It preserves the `:` length marker, `.` checked-syllable marker, apostrophe notation, non-Myanmar runs and punctuation. Unsupported MLCTS forms remain visible as `⟦…⟧`; there is no IPA fallback.

**Acceptance status: PARTIAL.** Exact coverage tests now exercise all 94 vendor rime rows and all onset rows combined with a supported rime. The runtime does not claim all legal Burmese syllable structures: unrepresented devoicing/medial combinations and any MLCTS output absent from the inventory remain withheld. Source-rime provenance is still `EVIDENCE_LIMITED` because the 94-row inventory is Mya2Rom-derived, not independently verified against the original MLC publication.

- Runtime module: `src/web/romanization-ukrainian.js`
- Runtime tests: `tests/web/romanization-ukrainian.test.mjs` plus the browser test in `tests/browser/converter.spec.js`.
- Exact PR-head [tests 43226578745](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43226578745) and push tests [43226566617](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43226566617) passed on code head `890ae6edf98f1480efcdf2d693690bdd61369a16`: 187 Python tests + 66 subtests, 18 Node tests, 55 Playwright browser tests, production build and generated-data freshness.

`MYA-ROM-UA-001` is PARTIAL: the runtime adapter executes the inventoried onset/rime crosswalk for supported syllables; complete MLC-primary inventory and all orthographic medial/kinzi/asat structures remain open. `MYA-ROM-MATRIX-001` remains PARTIAL.



Exact PR-head [tests 43226578745](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43226578745) and push tests [43226566617](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43226566617) passed on code head `890ae6edf98f1480efcdf2d693690bdd61369a16`: 187 Python tests + 66 subtests, 18 Node tests, 55 Playwright browser tests, production build and generated-data freshness.


Latest final exact-head verification after adding explicit withholding for Myanmar code points outside the romanization support inventory: [tests 43227199213](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/43227199213) SUCCESS on `4a2cb24ae9af2bc5e4d9341de65d0a55e07b6e09`: 187 Python tests + 66 subtests, 19 Node tests, 55 Playwright browser tests, production build and generated-data freshness. Unsupported Myanmar code points are now explicitly bracketed in the Ukrainian romanization output.
