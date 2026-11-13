# External Burmese G2P and licensing audit

Review date: 2026-10-20  
Decision: **do not replace the project engine with an external G2P yet**.

## Epitran (mya-Mymr)

Evidence reviewed:
- Project README lists mya-Mymr as Burmese support, but explicitly places it in the set of languages with limited support because orthography is highly ambiguous.
- Current Epitran project metadata declares Python >=3.10 and the MIT-Modern-Variant license for the package code. The current release page surfaced v1.35.0 (2026-04-24); pin the exact package version and mapping-data revision in any reproducible benchmark.
- Epitran's general mapping method is orthography-to-IPA with map tables and optional preprocessors/postprocessors. That output should be treated as a candidate baseline, not as independent truth.

Sources:
- https://github.com/dmort27/epitran
- https://github.com/dmort27/epitran/blob/master/README.md
- https://github.com/dmort27/epitran/blob/master/pyproject.toml
- https://github.com/dmort27/epitran/releases

Assessment:
- **Candidate role:** control engine / baseline comparator.
- **Not yet accepted as primary G2P:** the project itself warns that Burmese accuracy is limited due to orthographic ambiguity.
- **Unverified here:** exact coverage of mya-Mymr maps/preprocessors, behavior on this project's adversarial set, lexical accuracy against an independently adjudicated Burmese IPA corpus, and license/provenance of every redistributed mapping or auxiliary data file. Package license alone must not be assumed to settle every data-file right.
- **Required experiment:** pin version and artifact hashes; test whether the mapping leaves unknown graphemes in output; evaluate normalization, kinzi, medials, inherent vowels, codas, checked syllables, tone marks, proper names, loans and malformed input. Compare by layer and publish all disagreements.

## myG2P

Sources:
- https://github.com/ye-kyaw-thu/myG2P
- https://github.com/kyaw-yethu/burmese-G2P

The upstream myG2P repository states that its pronunciation dictionary is licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**. It describes a dictionary based on Myanmar Language Commission pronunciation entries, expanded with foreign pronunciations, and asks users to cite the related publications.

Implications:
- **NonCommercial:** do not use the dictionary as a bundled dependency for commercial use without separate permission.
- **ShareAlike:** adaptations of the licensed database/material may trigger share-alike obligations under the license; whether a particular integration is an adaptation or a separate work requires case-specific legal review.
- **Attribution and notices:** preserve attribution, source provenance and required notices if used in a permitted context.
- Do not copy myG2P entries into the project corpus, tests or generated artifacts without a documented rights/compatibility review. Facts about pronunciations and the licensed expression/compilation of a dictionary must be considered separately.
- It is not a universal default dependency for a project whose eventual code/data licensing and possible commercial use have not been decided.

CC BY-NC-SA 4.0 legal text: https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en

## Other candidate categories

- **NRC g2p (MIT):** a general framework for defining transducers, not a Burmese pronunciation model by itself. Useful only if a project-specific mapping is authored and validated.
  - https://github.com/NRC-ILT/g2p
- **Epitran-derived forks:** not independent evidence if they share the same map files/rules; check data provenance before treating agreement as replication.
- **Neural/TTS systems:** may provide useful hypotheses, but require model/data licenses, reproducible weights and a reference corpus. Their output is not automatically IPA ground truth.

## License state of this repository

The repository currently has no root LICENSE file and GitHub reports no detected repository license. This audit deliberately does not invent an MIT/Apache/GPL license choice for the maintainers. CITATION.cff uses license NOASSERTION until the project owner selects a license.

Before public reuse:
1. Decide the license for original source code.
2. Decide whether the corpus is separately licensed and whether source-derived lexical data can be redistributed.
3. Inventory code, model, dictionary, source-text and generated-data licenses separately.
4. Add a root license only after the owner has made that decision.
5. Do not bundle myG2P dictionary material under an incompatible blanket project license.

## Reproducible benchmark protocol

Do not report an engine as better until the independent corpus exists. Record for each run:
- engine/package version and commit or release;
- model/map/data version and cryptographic hashes;
- normalization and preprocessing configuration;
- raw output without cleanup;
- expected broad IPA, source locator and confidence;
- exact-match and feature-level error rates, with tone/coda/medial categories separated;
- unsupported/unknown handling and runtime failures;
- license review outcome.

Until then, Epitran is a **candidate baseline**, myG2P is a **license-constrained dictionary/reference**, and the in-repository engine remains a **partial research prototype**, not a validated full-coverage system.

## Pinned mapping-file inspection (Epitran v1.35.0)

Inspected the release-tagged files directly rather than inferring behavior from the package license or README alone:

- Map: https://github.com/dmort27/epitran/blob/v1.35.0/epitran/data/map/mya-Mymr.csv
- Preprocessor: https://github.com/dmort27/epitran/blob/v1.35.0/epitran/data/pre/mya-Mymr.txt
- Postprocessor: https://github.com/dmort27/epitran/blob/v1.35.0/epitran/data/post/mya-Mymr.txt

Findings from the tagged data:
- The mapping table is compact and contains direct grapheme/chunk-to-IPA substitutions (for example `က → kə`, `ဦ → ʔu`, `ော် → aʊʔ`). These are mapping entries, not evidence that a whole lexical word has been correctly analyzed.
- The preprocessor file is empty at this tag.
- The postprocessor has explicit rules for medial insertion/reordering and removal of selected inherent `ə` outputs. It maps both `ျ` and `ြ` to `j`, and `ွ` to `w`, in its medial handling.
- The inspected postprocessor contains no tone reconstruction rule. The map contains segmental/coda-like outputs such as `ɪɴ`, `aʊʔ` and `aɪɴ`, but this is not a tone-labelled lexical corpus.
- The combination of compact substitutions, postprocessing and the upstream limited-support warning means Epitran can be a useful comparator for grapheme/segmental hypotheses, but cannot supply the missing independent gold targets or validate the project's tone/register model.

This was a static inspection of release-tagged mapping files, not an execution of Epitran. No claim is made about actual output on the project's six structural probes until a reproducible runtime benchmark is run. Do not redistribute these mapping files as part of this repository merely because the package code declares an MIT-Modern-Variant license; keep the tagged third-party data and its licensing/provenance review distinct.

## Optional local baseline runner

The repository now includes `scripts/benchmark_g2p.py`. It imports Epitran only when explicitly run, so Epitran is not a project runtime dependency and no third-party mapping files are copied into this repository.

Example in a separate environment where the maintainer has installed Epitran:

```bash
python scripts/benchmark_g2p.py --engine epitran --output epitran-benchmark.json
```

The JSON report records raw output, package version, corpus SHA-256 and—when the installed package exposes the file—mapping-table SHA-256. It only scores rows whose evidence status is `GOLD_VERIFIED`, with a non-empty expected IPA, source ID and a non-pending source locator. With the current structural-only seed corpus, the eligible gold count is zero and accuracy remains `null`; this is intentional. The runner has not yet been executed against an installed Epitran environment, so no engine output or accuracy result is claimed in this audit.


## Burmese medial/G2P source and licensing update — 2026-11-13

### Google Thrax/OpenFst

- The exact pinned source commit a90601024f07ab7e96c911243324e0adeb16da96 has Apache-2.0 in both repository LICENSE and my/burmese.grm header. This corrects the earlier “license not identified” note for the paper: the paper does not specify the code license, but the actual pinned code does.
- The grammar is a candidate external comparator, not a default runtime dependency. Its upstream WORKSPACE is not fully hermetic; the PR #129 branch contains a pinned build path. The raw structural probe returned m j àɴ for မြန်, but had no expected IPA/gold.
- This code license does not extend to LREC in-house speech data, MLC dictionary data, myG2P, or other corpora.

### Epitran and CRFsuite diagnostics

- Epitran 1.35.3 raw output for မြန် is məjaɴ, compared with Google m j àɴ and Wiktionary /mjàɴ/. The exact artifact has zero gold and null accuracy; treat this as unresolved model disagreement.
- CRFsuite v2 sample: 100 evenly spaced myG2P v2.0 rows, 84 source-concordant, 0 gold, null accuracy, possible training overlap. Medial counts overlap: YA 10/14, RA 17/20, WA 13/15, HA 7/8. The target word မြန် was not selected.
- The CRF model's source data inherits the myG2P CC BY-NC-SA 4.0 restriction. Do not integrate its data/model artifacts commercially without separate permission.
- Current exact artifacts: optional run 43325991496; Epitran SHA-256 cb9cbb1c08047b2082f21f3c29d01d8054eaf37fc462abf55a3336ad265d7c1f; CRF SHA-256 d0df5c6527a757ee3c8be5259578ec08abdd3b219bf317d3de7364a47bdb6125.


## Mya2Rom mode separation — 2026-11-13

Mya2Rom 0.4.4 exposes distinct ipa, mlcts, mlcts2, simple and simple2 modes. MLCTS is orthographic; MLCTS2 is a more phonetic romanization used by the MLC Myanmar-English Dictionary and SEALang, not standardized IPA. The project's runtime explicitly requests mlcts. Do not treat the Latin→Ukrainian crosswalk as pronunciation-based G2P. Mya2Rom's own IPA convention uses /N/ rather than nasalized vowels and documents limitations with stacking, ASAT, schwa, voicing sandhi, alternate pronunciations and Pali/Sanskrit forms. Source license: CC BY-SA 4.0.


## Text-only continuation and licensing update — 2026-11-13

- Active research scope is written sources only. No audio acquisition, processing, annotation or audio-derived G2P evaluation is planned. Legacy SLR80/UCSY-SC1 records are historical metadata only and are not active source candidates.
- MYX_MYANGLISH_2026: CC BY-SA 4.0 declared; 2,121 text pairs; single-author-style, non-standardized romanization; 3-column viewer vs 2-field README mismatch. No rows copied; not IPA.
- MYX_ORTHO_2026: CC BY-SA 4.0 declared; 4,800 noisy-to-clean orthographic rows. "Phonetic" filenames/categories refer to spelling confusion, not IPA. No rows copied.
- OKELL_TEXT_2018: Zenodo Rights/License blank while ELG catalogue lists CC BY 4.0. Rights remain CONFLICT/UNKNOWN; no ingestion or redistribution until direct rights confirmation.
- STEDT1996_BURMESE and MATISOFF2003_HANDBOOK_PTB: copyrighted scholarly sources; only factual claims and page locators are registered, no tables or lexical data copied.
- NISHI1997_ORTHOGRAPHY and NISHI1998_VOICING_RULES: repository-hosted scholarly PDFs; reuse licenses are not stated in the metadata inspected. Only source claims and locators are recorded, not copied tables.
- The new text sources do not alter the myG2P CC BY-NC-SA 4.0 restriction, Wiktionary license conflict, or zero independent IPA-gold status.
