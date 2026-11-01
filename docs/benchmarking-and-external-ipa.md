# Burmese: IPA benchmarking and external systems

**Status: benchmark harness added; empirical accuracy remains unmeasured until independently adjudicated gold rows exist.** This is not a claim that candidate engines have been installed, run, licensed for redistribution, or validated for Burmese.

## Required pipeline boundary

source orthography → structural analysis → source-language phonology → typed IPA → ClippyFirst IPA-to-Ukrainian adapter → Ukrainian practical orthography

External engines are comparators or optional upstream IPA providers only. Preserve their raw output separately from any normalized IPA. Do not bypass the ClippyFirst IPA adapter, silently rewrite an engine's proprietary phoneme alphabet as IPA, or treat agreement among engines as ground truth.

## Reproducible benchmark

The standard-library-only harness is scripts/benchmark_ipa.py. It reads tab-separated files:

- Gold columns: id, text, gold_ipa, gold_status, profile, source_id.
- Prediction columns: id, engine, raw_output, ipa, status, version.

Run from the repository root:

python scripts/benchmark_ipa.py --gold data/benchmark/gold.tsv --predictions data/benchmark/predictions.tsv --output reports/ipa-benchmark.json

Only rows with gold_status=ADJUDICATED and non-empty gold IPA enter the denominator. For each engine, every eligible gold row is counted: an absent prediction row or empty IPA is a miss and remains in the denominator. The report provides strict NFC exact match, missing-prediction rate, and code-point Levenshtein CER. NFC and outer whitespace trim are the only normalizations: tone, vowel length, diacritics, and syllable separators remain significant. Code-point CER is a diagnostic, not a feature-weighted phonetic metric. A header-only gold file correctly yields NOT_MEASURED, not a fabricated zero or 100% score. An engine with no predictions for eligible gold rows is not scored; once an engine appears in the prediction file, omitted eligible IDs count as missing.

Stratify gold cases by syllable shape, consonant class/series, vowel type and length, coda, tone/prosody where applicable, morphology, lexical/loanword status, and uncertainty. Report the denominator and source/profile per row. Avoid training/test leakage and use a held-out set for any tuning.

## External candidates (not yet approved for runtime)

- Goruut (support/version must be verified)
- eSpeak NG (language support and IPA mode must be verified)
- Burmese-specific dictionaries (inventory pending)

These are research leads, not verified availability claims. Before executing a candidate, record the exact release/commit, installation command, language/voice/model identifier, raw output, runtime errors, license for code plus model/dictionary/data, and whether the output is actual IPA or a tool-specific phone alphabet. Do not install or enable a candidate by default merely because it appears here.

## Acceptance gates

1. Build a versioned gold set from cited primary sources with exact page/section/audio locator, dialect/profile, and independent adjudication; Unicode tables alone do not establish pronunciation.
2. Keep raw source output immutable; store conversion rules and normalized output separately.
3. Run the same inputs/profile through ClippyFirst and each available candidate; preserve failed/missing outputs in the denominator report.
4. Evaluate both strict IPA exact match and reviewed feature-level errors (tone, vowel length/quality, onset, coda, syllable boundaries). Do not infer a winner from exact match alone.
5. Run the existing repository test/CI suite and validate the benchmark script on a synthetic fixture; do not publish synthetic scores as language accuracy.
6. Keep candidates optional, pinned, license-reviewed, and fail-closed. A missing tool must never change the core result silently.

## Current evidence status

- Harness baseline: executed successfully in prior main CI. Additional fail-closed validation now requires every ADJUDICATED row to have non-empty IPA, source_id and profile; PR #19 adds regression tests for these gates and must pass CI on its final head.
- Adjudicated language-specific gold rows: not yet established by this document.
- Candidate engine availability, version, licenses, and language-specific output quality: unverified until recorded as run evidence.
- Release status: research prototype; no accuracy claim is authorized by this registry.

## Existing external run evidence (reconciled 2026-10-24)

- Latest pinned run: [workflow 40119616115](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40119616115), Epitran 1.35.3, 6 raw outputs, 0 runtime errors, 0 independently adjudicated gold rows; accuracy remains null. Artifact ZIP SHA-256 `1bcf0cd9963eac99ea5dd448f430f6ddbe8bf4af1ab3e243f9fbac222d8126ab`. Input corpus SHA-256 `bc7d4f138581b7cfd48594b41891a26ec45123ea4488af977b48567201f0b19b`; mapping SHA-256 `de8660a0cdccb4192993d423342ad775a59ade19b8081829eb70da18f291dfe4`; postprocessor SHA-256 `0eac185c50b19b7c2682d1395afad97a7662a5ff22e2344195eb0d3ffcbed7af`. All cases remain `NOT_SCORED_NO_VERIFIED_GOLD`.
- The existing source audit inspected Epitran's tagged `mya-Mymr` mapping/pre/postprocessor statically and records upstream warnings that Burmese support is limited by orthographic ambiguity. Static inspection is not a runtime benchmark.
- [Goruut](https://github.com/neurlang/goruut) lists Burmese support upstream, but is not yet executed here. [myG2P](https://github.com/ye-kyaw-thu/myG2P) is license-constrained: the repository's existing audit identifies its pronunciation dictionary as CC BY-NC-SA 4.0, so do not bundle it for commercial use without permission.
- Completed: pinned Epitran 1.35.3 smoke [run 40121355875](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40121355875) captured 6/6 outputs with 0 runtime errors and 0 independent gold rows; mapping/preprocessor/postprocessor hashes and the artifact digest are recorded above. Next: independently adjudicate Burmese tone/register/phonation, medials, codas and lexical readings before any accuracy scoring.


## Upstream provenance and suitability warning (checked 2026-10-24)

| Candidate | Verified upstream fact | Evidence boundary / next step |
|---|---|---|
| [Epitran 1.35.3](https://github.com/dmort27/epitran) | The upstream language/script inventory includes mya-Mymr (Burmese), but explicitly places Burmese among pairs with limited support due to highly ambiguous orthographies. | Our pinned smoke produced six outputs with zero runtime errors. This verifies execution only, not phonological accuracy; do not treat a clean run as evidence that ambiguity is solved. Prioritize a reviewed gold set and report errors by inherent vowel, medials, coda and phonation/tonal convention. |
| [Goruut](https://github.com/neurlang/goruut) | Upstream advertises an IPA phone set and Burmese support. | Support claim only; no successful run recorded here. Compare its raw output to Epitran and ClippyFirst only on identical, source-attested inputs; engine agreement is not gold. |

Epitran code/mapping availability does not itself establish the provenance or redistribution rights of every mapping table. Record the installed package version, exact language code, mapping/preprocessor/postprocessor hashes and any upstream data attribution. The current six-probe smoke has zero independently adjudicated gold labels, so accuracy remains NOT MEASURED.


## Benchmark metric semantics — 2026-10-24

- `exact_match_rate` is strict string equality after the declared Unicode normalization and is comparable only when the same IPA profile/conventions are used. Tone, length, stress, syllable boundaries, tie bars and other IPA distinctions are not silently removed.
- `character_error_rate` is Levenshtein distance over Unicode code points, not a phoneme/segment error rate. IPA affricates, combining diacritics, length marks and tone symbols can occupy multiple code points; interpret this field as a string-distance diagnostic only.
- A valid score still requires a non-empty independently adjudicated gold set with source locator and profile. Smoke output, engineering fixtures, source-attested but unadjudicated entries, and inter-engine agreement are not accuracy.

## Final current-main smoke after trigger-scope fix — 2026-10-25

Current-main Epitran smoke [40134067758](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40134067758) passed; inspected artifact [12576415800](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40134067758/artifacts/12576415800), ZIP SHA-256 `6ff7fd5d70f386d76eefb37d50d2718d9de3f4e410749cf94848af9afeab788c`. Epitran 1.35.3 / Python 3.12.15; six outputs, zero runtime errors; corpus SHA-256 `bc7d4f138581b7cfd48594b41891a26ec45123ea4488af977b48567201f0b19b`; mapping SHA-256 `de8660a0cdccb4192993d423342ad775a59ade19b8081829eb70da18f291dfe4`; preprocessor empty hash `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; postprocessor hash `0eac185c50b19b7c2682d1395afad97a7662a5ff22e2344195eb0d3ffcbed7af`. All six cases remain STRUCTURAL_ONLY; independent gold is 0 and accuracy null.

The optional Epitran workflow now excludes evidence-registry and benchmark-document paths from automatic push triggers, preventing evidence-only edits from producing another run that immediately makes the registry stale. Manual dispatch and script/corpus/source-registry/workflow changes remain enabled.


## Goruut comparator — upstream verified, execution pending (2026-11-01)

**Disposition: ADD AS AN OPTIONAL RAW-OUTPUT COMPARATOR; NOT APPROVED AS A PRODUCTION PHONOLOGY PROVIDER.**

- Upstream repository: https://github.com/neurlang/goruut
- Pinned upstream source commit inspected: `b224bde02151f8f86d0fe260804e4ca743bda620` (2026-10-02; pin this commit rather than `@latest`).
- Upstream README explicitly lists **Burmese** support and advertises an IPA phone set, word-level tokens, punctuation preservation and tonal phones. It explicitly says syllable tokens are not provided, tie bars are not supported, and numbers/dates are unsupported and should be written as words.
- The upstream source-code repository contains an MIT license. This verifies the code license only; the license and provenance of each embedded dictionary, model, training corpus and generated language asset have not yet been audited. Do not redistribute those assets or treat the MIT code license as clearing them.
- Upstream requires Go 1.22 or newer. Advertised Burmese support is not evidence of accurate handling of tone, register, phonation, inherent vowels, medials, codas, loanwords or dialect variation.

**Candidate comparison:** Epitran 1.35.3 remains the pinned runnable baseline, but its own upstream support caveat and this repository's audit note limited Burmese support due to orthographic ambiguity. The `myG2P` research resource provides a Burmese G2P dictionary/model with IPA-labelled outputs and scholarly provenance, but its repository is CC BY-NC-SA 4.0; it is not suitable for commercial redistribution/use without an appropriate permission decision. Keep its outputs/data outside the runtime and commercial build unless rights are resolved. The paper on Burmese speech corpus and finite-state pronunciation grammars is a strong research lead, but the paper's existence alone does not establish current package availability or the licenses of all model/data assets.

**Benchmark treatment:** run Goruut only in a disposable optional CI job; preserve raw response, errors, exact upstream commit, language identifier, Go version, corpus hash and output artifact. Keep raw output separate from any IPA normalization. Do not synthesize syllable boundaries or tie bars, strip tone/phonation marks, or convert output to Ukrainian without an explicit reviewed mapping. Its missing syllable tokens/tie-bar support and number/date handling must be reported as representational limitations, not silently repaired.

**Acceptance before promotion:** (1) successful pinned execution on the same source-located Burmese inputs as Epitran and ClippyFirst; (2) inspect exact raw output and errors; (3) audit licenses/provenance for Burmese dictionary/model assets; (4) review tone, register, phonation, vowel quality, medials, codas, syllabification, dialect and IPA conventions against independent expert-adjudicated IPA; (5) score only held-out ADJUDICATED gold. Current independent gold count remains 0, so no accuracy or engine ranking is available.

Upstream evidence: https://github.com/neurlang/goruut/blob/b224bde02151f8f86d0fe260804e4ca743bda620/README.md ; https://github.com/neurlang/goruut/blob/b224bde02151f8f86d0fe260804e4ca743bda620/LICENSE ; https://github.com/neurlang/goruut/blob/b224bde02151f8f86d0fe260804e4ca743bda620/go.mod ; https://github.com/ye-kyaw-thu/myG2P ; https://aclanthology.org/2020.lrec-1.777/


## Goruut language-asset license gate — 2026-11-01

The language-specific embedded files in Goruut's pinned source tree are derived from separate language lexicons: its own `dicts/README.md` describes `lexicon.tsv` as word-to-IPA training data and the generated model files as embedded assets. The corresponding Burmese lexicon directory is `neurlang/dataset/burmese/`. The dataset repository metadata has no declared license (`license: null`), its root tree contains no LICENSE/COPYING file, and its README's partial license inventory does not assign a license/provenance to this language directory. Therefore the Goruut source MIT license is insufficient to clear the lexicon or derived model. Runtime execution and artifact retention remain BLOCKED pending per-language provenance/license clarification and owner-approved use terms. Full review: `docs/audits/current/GORUUT-ASSET-LICENSE-REVIEW-2026-11-01.md`.


## External corpus/source triage — 2026-11-01

External-source triage is PARTIAL; no independently adjudicated, openly reusable Burmese IPA gold was verified. myG2P offers richer IPA but states CC BY-NC-SA 4.0 and remains blocked for commercial use without permission. A 2026 Wiktionary extraction reports 22,191 words with full MLCTS but only 113 IPA rows (0.51%) under CC BY 4.0; it is a possible MLCTS crosswalk, not a broad IPA gold corpus. OpenSLR SLR80 has Burmese audio/transcripts under CC BY-SA 4.0 but requires expert IPA annotation. Mya2Rom is CC BY-SA 4.0 and a comparator, not gold. See the source-triage audit for boundaries and links. Gold remains 0.

Detailed source-by-source findings, license boundaries and acceptance criteria: `docs/audits/current/EXTERNAL-PHONETIC-CORPUS-TRIAGE-2026-11-01.md`. No external dataset rows were copied into the project.


## Test-only Goruut runtime probe — 2026-11-01

Added an optional, test-only HTTP runtime probe for Goruut at pinned upstream commit `b224bde02151f8f86d0fe260804e4ca743bda620`. It explicitly enables `Burmese` in `BuiltinDictLanguages`, builds the upstream Go binary and records raw JSON responses for six existing structural probes plus sentence/punctuation cases. `scripts/benchmark_goruut.py` records commit, language, input SHA-256, raw response, tokens and errors; no IPA normalization or accuracy scoring occurs. Structural probes are not phonological gold. Accuracy=null; independent gold=0. Workflow: `.github/workflows/optional-goruut-runtime.yml`; artifact retention 30 days.

This probe intentionally uses upstream language assets only inside an ephemeral CI checkout for evaluation. No upstream dictionary/model files are copied into this repository or production bundle. This test-only use is distinct from production redistribution or runtime dependency approval. The probe validates availability and raw output only; it does not establish linguistic accuracy.


## Completed test-only Goruut runtime evaluation — 2026-11-01

The pinned Goruut runtime was executed with Burmese enabled (Go 1.23.12). Seven of eight probes returned phonetic tokens; the Burmese-punctuation sentence `ကေ၊ ကော်။` returned no phonetic output. Raw tokens such as `kè`, `kɔ̀`, `tɕì`, `swɛ̀`, `mjàɴ`, `jù` are preserved but not validated against an independent Burmese IPA set. Server log repeatedly reports missing `weights9.bin.zlib`. Do not promote. Full evidence: `docs/audits/current/GORUUT-RUNTIME-EVALUATION-2026-11-01.md`.

The optional workflow builds the pinned source in an ephemeral CI checkout, captures raw HTTP output and server logs, hashes the fixture/effective config/log, and stores a 30-day artifact. It is a comparator, not an accuracy benchmark or production dependency.


## Three-repeat runtime evidence — supersedes one-shot figures

Three-repeat re-evaluation: 7/8 probe inputs returned usable output and all 7 were stable across three repetitions; Burmese punctuation sentence `ကေ၊ ကော်။` returned no output in all three. This establishes limited repeatability, not IPA accuracy.

See `docs/audits/current/GORUUT-RUNTIME-EVALUATION-2026-11-01.md` for exact run links, hashes and per-language interpretation.


## Cross-engine comparator evidence — 2026-11-01

Cross-engine check: Epitran 1.35.3 returned 6/6 raw outputs; Goruut returned 7/8 usable probes and failed the Burmese punctuation sentence. Exact string agreement between Epitran and Goruut was 0/6. Epitran is largely tone-less in these examples while Goruut emits tone-marked strings; without a common IPA convention and expert gold this is disagreement, not an accuracy ranking. Latest Goruut run had 7 stable usable outputs; a prior run showed one unstable `ကြည်` output.


### Latest pinned Goruut + Epitran run — exact PR head

PR #82 exact head `d8b065bc66dce5fdd9959c4f0eb932a29acaedba` built and ran successfully: [runtime workflow](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41310771082), artifact SHA-256 `0eb19d7079de818736ecff095f700405fc4b46de3791dd6e4fd68762346218fa`. Goruut returned 7/8 usable results; six were stable and one (`ကြည်`) varied across three repetitions; Burmese punctuation returned no output. Epitran 1.35.3 returned 6/6; exact string agreement was 0/6. This is not accuracy or a winner selection; gold=0. Missing `weights9.bin.zlib` warning remains unexplained.


### Goruut dictionary ambiguity and instability

The only unstable input (ကြည်) carried RandomizationWordsCount=1 and RandomizationWordsChoices=2 on all three responses. The other seven inputs had no such metadata; six were reproducible and one punctuation input returned no output.

Pinned upstream code counts dictionary homographs and falls back to a random dictionary pronunciation when no preferred entry is selected; it exposes this through `RandomizationWordsCount` / `RandomizationWordsChoices`. See the exact [selector code](https://github.com/neurlang/goruut/blob/b224bde02151f8f86d0fe260804e4ca743bda620/repo/services/parts_of_speech_selector_service.go#L168-L205) and [response counter propagation](https://github.com/neurlang/goruut/blob/b224bde02151f8f86d0fe260804e4ca743bda620/usecases/phonemize_usecase.go#L84-L85). Treat flagged outputs as ambiguous; the missing `weights9.bin.zlib` warning is a separate unresolved issue.


### Source-coverage findings from pinned Goruut runs

## Source-coverage re-analysis of the exact-head artifact — 2026-11-01

A second inspection of the saved raw JSON used the API's `PrePunct`, `CleanWord`, and `PostPunct` fields. Coverage was counted complete only when (a) these fields reconstructed the input after NFC and whitespace removal and (b) no letters, combining marks, or numbers appeared in PrePunct/PostPunct. This is a source-coverage check, not phonetic correctness.

- Goruut: 7/8 inputs returned phonetic output; 1 punctuation sentence returned no output. All 7 returned outputs passed this source-coverage check. Six were stable; `ကြည်` was unstable and carried `RandomizationWordsCount=1`, `RandomizationWordsChoices=2`.
- Epitran 1.35.3 returned six outputs on the six structural probes; exact string agreement with Goruut was 0/6. This is not accuracy or a winner selection.
- This re-analysis confirms no partial-source-coverage response in the small Burmese probe set, but eight cases are far too few to establish language coverage.

Raw artifact: [13085043436](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41310771082/artifacts/13085043436), ZIP SHA-256 `0eb19d7079de818736ecff095f700405fc4b46de3791dd6e4fd68762346218fa`.


## Owner scope decision — temporary test-only use — 2026-11-01

The repository owner explicitly directed that external Goruut assets may be used for temporary verification and comparison without blocking these tests on license review. Accordingly:

- **Test-only execution:** authorized for this research task; do not stop runtime probes because the external asset license is unresolved.
- **No data/model import:** no Goruut dictionary, model weight, or MekongPhon source row is copied into the product runtime or committed as a corpus by this decision.
- **Production packaging or redistribution:** not authorized by this instruction and remains outside this test-only scope; asset provenance/rights must be revisited before any bundling, redistribution, or production deployment.

This is a project scope decision, not a legal conclusion about the upstream assets.


## myG2P v2.0 100-entry source-attested comparison — 2026-11-01

A richer Burmese pronunciation resource was identified and is now wired into an optional, test-only comparison:

- Upstream: https://github.com/ye-kyaw-thu/myG2P
- Pinned upstream commit: `54b5c76bb5a87fdbaaeddc1892e6ebd8f97ee225`; dictionary: `ver2/myg2p.ver2.0.txt`.
- The README describes a five-column dictionary (word ID, orthography, syllable-broken word, pronunciation, IPA). Version 2.0 says IPA labels were added for each dictionary word; it acknowledges contributors and says mappings were checked, but does not provide per-entry reviewer IDs, adjudication protocol, or a sufficiently specified dialect/register profile.
- The source README declares CC BY-NC-SA 4.0. Per owner instruction, this dataset is used only in temporary verification artifacts; it is not copied into repository data or the product runtime.
- `scripts/prepare_myg2p_probe.py` parses the pinned TSV, records malformed/missing/duplicate rows, and deterministically selects 100 unique IPA-labelled headwords evenly across file order. It retains source line locators, word IDs, syllabification, pronunciation and the original IPA string. It does not label any row GOLD_VERIFIED.
- The optional runtime workflow runs both pinned Goruut and Epitran 1.35.3 against exactly the same 100 words, three repetitions for Goruut, and compares raw output with myG2P source labels. Goruut source concordance is eligible only when the response is stable, source coverage is complete, and no dictionary-randomization counters are present. Epitran is compared separately. All scores remain accuracy=null and independent_gold_count=0.

This is a stronger Burmese source-attested diagnostic than the 8-word structural smoke set, but it is still not independent gold. Exact-head workflow evidence is pending.


### Burmese source-coverage repeat-run evidence

## Re-run with source-coverage and randomization counters — 2026-11-01

The updated harness completed on PR branch commit `422ee1f991203275af21031e0ee3b2be78042816`: [runtime workflow 41312361052](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41312361052), artifact [13086372584](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41312361052/artifacts/13086372584), ZIP SHA-256 `d6ea2b1aa6252fbe81c371e25d5ec7627d8608bb722b54a7c8fee85e729fe7f3`.

- Goruut returned 7/8 inputs; 7/7 had complete source coverage, one punctuation sentence had no output. All seven returned outputs were repeat-stable in this run.
- `ကြည်` carried `RandomizationWordsCount=1` and `RandomizationWordsChoices=2` in all three repetitions, even though this particular run selected the same `tɕì` output each time. A previous independent run selected different outputs across repetitions. Therefore metadata indicates an ambiguous dictionary selection even when a three-repeat sample happens to be stable; the new comparison excludes such rows from source-attested scoring.
- Epitran 1.35.3 returned six outputs on the original six structural probes; raw exact agreement remains 0/6. No independent gold; accuracy null.

This run reinforces that repeat stability alone is insufficient: Goruut's ambiguity counters must also be clear before source concordance is even reported.


## Independent IPA gold workflow — 2026-11-01

The repository now has a separate `scripts/ipa_gold_corpus.py` lifecycle and versioned JSON Schemas:
- `data/benchmark/records.jsonl`, `annotations.jsonl`, `adjudications.jsonl`, and `splits.jsonl`;
- two distinct annotators plus a third adjudicator for every adjudicated row;
- explicit `AGREEMENT`, `RESOLVED`, and `UNRESOLVED` outcomes;
- source citation, exact locator, license and redistribution rights;
- deterministic, frozen, lexeme-group-safe train/dev/test assignment;
- export into the existing `gold.tsv` contract only for adjudicated and redistributable IPA.

The benchmark now retains `ipa_kind` (PHONEMIC, PHONETIC_BROAD, PHONETIC_NARROW). A prediction with missing or different IPA kind cannot count as an exact match against typed gold. The existing scorer remains the metric implementation.

Normal CI validates corpus structure while allowing an empty research corpus. The tag/manual `ipa-gold-release-gate.yml` requires at least 100 train, 25 dev and 25 test adjudicated records with redistribution rights. These are project release thresholds, not a universal statistical claim. A separate feature-stratified engine and Ukrainian-adapter quality gate is still required.

**Current status:** the four JSONL files are intentionally empty and the gold TSV remains header-only. Independent adjudicated gold=0; accuracy=null. No phonemizer output or synthetic test fixture has been promoted to gold. Blind annotation must be collected through a controlled channel before the two submissions are merged; a public shared repository cannot enforce blinding.


The rights layer is executable: `data/benchmark/licenses.json` is the allowlist, each record must carry `rights_evidence` (basis, locator, verifier pseudonym and date), and unknown or non-redistributable license IDs are rejected. Exported gold rows retain `license_id` and `rights_evidence_locator`; benchmark reports carry those fields forward. The allowlist is not a substitute for source-by-source legal verification.
