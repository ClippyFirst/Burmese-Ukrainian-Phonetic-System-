# Goruut runtime evaluation — Burmese — 2026-11-01

## Execution

- Upstream: [neurlang/goruut](https://github.com/neurlang/goruut), pinned commit `b224bde02151f8f86d0fe260804e4ca743bda620`.
- Language identifier: `Burmese`; explicitly enabled in `BuiltinDictLanguages`.
- Runtime: Go 1.23.12, HTTP `POST /tts/phonemize/sentence`.
- Test-only checkout; no upstream model/dictionary assets copied into this repository or production bundle.
- Effective config SHA-256: `d725cc8e99a779e7928dc05685c3187b89df9ed87228b1875e290455b8014ef1`.

## Results

1. Eight probes were submitted: six existing structural probes, a multiword probe and a punctuation probe.
2. Seven returned usable phonetic tokens; one returned no phonetic output for `ကေ၊ ကော်။` (Burmese punctuation).
3. Example raw outputs include `ကေ` → `kè`, `ကော်` → `kɔ̀`, `ကြည်` → `tɕì`, `စွယ်` → `swɛ̀`, `မြန်` → `mjàɴ`, `ယူ` → `jù`. These are preserved as raw strings; the run does not establish that Goruut's output convention is equivalent to the project's required IPA convention.
4. The server log repeatedly reports `weights9.bin.zlib: file does not exist`. This is an unresolved model-asset warning and may explain missing or fallback behavior.

## Interpretation

Goruut is a functioning optional HTTP comparator for several Burmese probes, but punctuation handling is incomplete and phonetic output has not been checked against an independent source-attested Burmese IPA set. **Do not promote it to a production provider or score its output as IPA accuracy.** Current independent, project-owned, expert-adjudicated Burmese gold remains 0.

## Evidence and artifacts

- Optional runtime workflow: [41308074710](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41308074710) (initial completed runtime probe); latest exact-head run is tracked by PR #82.
- Artifact includes raw responses and server log; retention is 30 days.
- Accuracy remains null; independent gold count remains 0.


## Repeatability follow-up — 2026-11-01

Each of the eight inputs was sent three times to the same server:

- Seven inputs returned usable phonetic tokens; all seven were identical across all three repetitions.
- The punctuation case `ကေ၊ ကော်။` returned no phonetic output in all three attempts.
- Thus the observed output is stable for the covered lexical probes, but punctuation coverage is incomplete. No independent IPA concordance or accuracy result is available.

Three-repeat evidence: [workflow 41309099367](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41309099367). Effective config SHA-256 `d725cc8e99a779e7928dc05685c3187b89df9ed87228b1875e290455b8014ef1`; probe fixture SHA-256 `44fdecc507b92c9b18199972f9150b0b9f29b9a04928474e447ff70e6608bb9f`.

**Disposition:** useful stable raw-output comparator for these limited cases, not an IPA-validated production provider.


## Additional comparator: Epitran 1.35.3 — 2026-11-01

The optional Goruut workflow now runs the existing Epitran baseline on the same six structural probes and emits a raw side-by-side comparison:

- Epitran returned 6/6 outputs; Goruut returned usable output for 7/8 probes, with the Burmese punctuation sentence failing.
- Goruut vs Epitran exact string agreement: 0/6. This is not a winner/loser result: Epitran's sample strings are largely tone-less (e.g. `ke`, `kaʊʔ`, `t͡ɕi`), while Goruut returns different phone sequences and tone-marked strings (e.g. `kè`, `kɔ̀`, `tɕì`). The outputs are not directly comparable without an agreed phonetic convention and expert gold.
- In the latest three-repeat run, seven usable Goruut outputs were stable; a prior run showed one unstable `ကြည်` output, so repeatability across fresh server processes still needs more sampling.
- Both reports retain raw outputs and hashes; independent gold=0, accuracy=null.

Evidence: [Goruut + Epitran workflow 41310125185](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41310125185). Epitran version `1.35.3`; Goruut pinned commit `b224bde02151f8f86d0fe260804e4ca743bda620`.


## Model-asset warning interpretation

The runtime warning needs upstream diagnosis: the pinned Burmese language module contains `weights8.bin.zlib`, but the server logs `weights9.bin.zlib` as missing; no `weights9` asset was found in the pinned source tree. Its relationship to punctuation failure or phonetic output differences is unproven. Do not infer causation from correlation.


## Exact-head three-repeat runtime evidence — 2026-11-01

The exact current PR #82 head `d8b065bc66dce5fdd9959c4f0eb932a29acaedba` was executed in GitHub Actions, including a clean pinned-source Go build and three HTTP requests per input.

- Runtime workflow: [41310771082](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41310771082); artifact [13085043436](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41310771082/artifacts/13085043436); ZIP SHA-256 `0eb19d7079de818736ecff095f700405fc4b46de3791dd6e4fd68762346218fa`.
- Engine `b224bde02151f8f86d0fe260804e4ca743bda620`, Go `1.23.12`, language `Burmese`, effective config SHA-256 `d725cc8e99a779e7928dc05685c3187b89df9ed87228b1875e290455b8014ef1`.
- Goruut: 7/8 inputs returned usable output; the punctuation sentence `ကေ၊ ကော်။` returned no phonetic output in all three repeats. Six outputs were identical across all three repetitions; `ကြည်` was unstable (`tɕì`, `tɕì`, `tɕɪ̀ɴ`).
- Epitran 1.35.3 returned 6/6 outputs for the six structural probes. Exact Goruut/Epitran string agreement was 0/6. This is only raw-output difference evidence: no shared adjudicated IPA convention or independent gold exists, so neither engine wins.
- The server logs `weights9.bin.zlib: file does not exist`; the pinned Burmese tree contains `weights8.bin.zlib`, not `weights9.bin.zlib`. Its causal relation to punctuation failure or output variation is unproven.

**Disposition: retain Goruut and Epitran only as raw-output comparators; neither is validated for production phonology.** Independent adjudicated Burmese gold remains 0.


## Upstream cause of nondeterministic dictionary selection — Burmese

Pinned Goruut source explains the instability signal. In [parts_of_speech_selector_service.go](https://github.com/neurlang/goruut/blob/b224bde02151f8f86d0fe260804e4ca743bda620/repo/services/parts_of_speech_selector_service.go#L168-L205), `SelectE` counts multiple dictionary pronunciations for a word; when more than one exists it increments the escape counters. If the homograph selector has not marked a `preferred` pronunciation, the fallback loop iterates the dictionary mapping and selects a dictionary pronunciation; the upstream source comment explicitly describes this as random selection when no homograph model is available. The [sentence use case](https://github.com/neurlang/goruut/blob/b224bde02151f8f86d0fe260804e4ca743bda620/usecases/phonemize_usecase.go#L84-L85) exposes those counters as `RandomizationWordsCount` and `RandomizationWordsChoices` in the HTTP response.

The only unstable input (ကြည်) carried RandomizationWordsCount=1 and RandomizationWordsChoices=2 on all three responses. The other seven inputs had no such metadata; six were reproducible and one punctuation input returned no output.

This gives a source-level explanation for the observed unstable cases. It does **not** establish that the separate `weights9.bin.zlib` warning causes the selection behavior; that warning remains independently unresolved. The project does not patch Goruut or choose a random pronunciation as acceptable output. Any result carrying these ambiguity counters should remain flagged as non-deterministic/ambiguous for downstream use.


## Source-coverage re-analysis of the exact-head artifact — 2026-11-01

A second inspection of the saved raw JSON used the API's `PrePunct`, `CleanWord`, and `PostPunct` fields. Coverage was counted complete only when (a) these fields reconstructed the input after NFC and whitespace removal and (b) no letters, combining marks, or numbers appeared in PrePunct/PostPunct. This is a source-coverage check, not phonetic correctness.

- Goruut: 7/8 inputs returned phonetic output; 1 punctuation sentence returned no output. All 7 returned outputs passed this source-coverage check. Six were stable; `ကြည်` was unstable and carried `RandomizationWordsCount=1`, `RandomizationWordsChoices=2`.
- Epitran 1.35.3 returned six outputs on the six structural probes; exact string agreement with Goruut was 0/6. This is not accuracy or a winner selection.
- This re-analysis confirms no partial-source-coverage response in the small Burmese probe set, but eight cases are far too few to establish language coverage.

Raw artifact: [13085043436](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41310771082/artifacts/13085043436), ZIP SHA-256 `0eb19d7079de818736ecff095f700405fc4b46de3791dd6e4fd68762346218fa`.


## myG2P v2.0 100-entry source-attested comparison — 2026-11-01

A richer Burmese pronunciation resource was identified and is now wired into an optional, test-only comparison:

- Upstream: https://github.com/ye-kyaw-thu/myG2P
- Pinned upstream commit: `54b5c76bb5a87fdbaaeddc1892e6ebd8f97ee225`; dictionary: `ver2/myg2p.ver2.0.txt`.
- The README describes a five-column dictionary (word ID, orthography, syllable-broken word, pronunciation, IPA). Version 2.0 says IPA labels were added for each dictionary word; it acknowledges contributors and says mappings were checked, but does not provide per-entry reviewer IDs, adjudication protocol, or a sufficiently specified dialect/register profile.
- The source README declares CC BY-NC-SA 4.0. Per owner instruction, this dataset is used only in temporary verification artifacts; it is not copied into repository data or the product runtime.
- `scripts/prepare_myg2p_probe.py` parses the pinned TSV, records malformed/missing/duplicate rows, and deterministically selects 100 unique IPA-labelled headwords evenly across file order. It retains source line locators, word IDs, syllabification, pronunciation and the original IPA string. It does not label any row GOLD_VERIFIED.
- The optional runtime workflow runs both pinned Goruut and Epitran 1.35.3 against exactly the same 100 words, three repetitions for Goruut, and compares raw output with myG2P source labels. Goruut source concordance is eligible only when the response is stable, source coverage is complete, and no dictionary-randomization counters are present. Epitran is compared separately. All scores remain accuracy=null and independent_gold_count=0.

This is a stronger Burmese source-attested diagnostic than the 8-word structural smoke set, but it is still not independent gold. Exact-head workflow evidence is pending.


## Re-run with source-coverage and randomization counters — 2026-11-01

The updated harness completed on PR branch commit `422ee1f991203275af21031e0ee3b2be78042816`: [runtime workflow 41312361052](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41312361052), artifact [13086372584](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41312361052/artifacts/13086372584), ZIP SHA-256 `d6ea2b1aa6252fbe81c371e25d5ec7627d8608bb722b54a7c8fee85e729fe7f3`.

- Goruut returned 7/8 inputs; 7/7 had complete source coverage, one punctuation sentence had no output. All seven returned outputs were repeat-stable in this run.
- `ကြည်` carried `RandomizationWordsCount=1` and `RandomizationWordsChoices=2` in all three repetitions, even though this particular run selected the same `tɕì` output each time. A previous independent run selected different outputs across repetitions. Therefore metadata indicates an ambiguous dictionary selection even when a three-repeat sample happens to be stable; the new comparison excludes such rows from source-attested scoring.
- Epitran 1.35.3 returned six outputs on the original six structural probes; raw exact agreement remains 0/6. No independent gold; accuracy null.

This run reinforces that repeat stability alone is insufficient: Goruut's ambiguity counters must also be clear before source concordance is even reported.


## Final exact-head verification — 2026-11-01

The final PR #82 head `dcd9dfb6f1306ce01547f922238aba3fdefd6586` completed both required workflows:

- Repository tests/build/browser [41313487752](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41313487752): PASS. The run completed pytest, npm build, generated web-data drift validation, Node tests and Playwright built-browser tests.
- Goruut + Epitran + myG2P [41313487703](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41313487703): PASS. It built pinned Goruut commit `b224bde02151f8f86d0fe260804e4ca743bda620`, installed Epitran 1.35.3, prepared the deterministic 100-row myG2P v2.0 probe and captured three Goruut repeats.
- Artifact [13086900774](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41313487703/artifacts/13086900774), ZIP SHA-256 `ca165ac84ee6b284a423a988a5ee32d951a883c36073b01fd5f086ba83022f77`; downloaded archive hash independently recomputed and matched GitHub's digest. myG2P source commit `54b5c76bb5a87fdbaaeddc1892e6ebd8f97ee225`, source SHA-256 `19353bb3b8bbbdd24feb8beca4a82c39b7764b6ca8b8f60dcb6965df1f23bd3d`, output probe SHA-256 `e9026cd2cfbe29664a7422e9bc009f8d9bd737711035ec0538f4aa8bc86714b6`.

The 100-row myG2P diagnostic returned 98 Goruut outputs and 2 no-output cases. Coverage was 43 complete, 55 partial and 2 unknown/no-output; 98 outputs were repeat-stable, none unstable, and no randomization counters were reported. There were 69 unphonemized source fragments. Strict source-attested exact matches were 0/100; a limited notation diagnostic found 17/100. Only 43 rows were eligible for Goruut's complete/deterministic source-attested comparison. Epitran and Goruut each had 0 exact matches to source labels in their respective diagnostics; this is not accuracy or a winner result.

The separate eight-case engineering probe returned 7 outputs and 1 no-output; 7 had complete source coverage, 6 were stable and 1 carried dictionary-randomization metadata and was unstable. The server logs the unresolved `weights9.bin.zlib` warning; no causal link is established.

myG2P declares CC BY-NC-SA 4.0. Its dictionary is used only in temporary test artifacts under the owner's explicit test-only authorization; it is not committed, vendored or bundled. The 100 labels are source-attested, not independent gold; per-entry adjudication and dialect/register are underspecified. Accuracy remains null and independent gold=0.

**Disposition:** exact-head engineering verification and comparator execution are DONE_VERIFIED. Goruut and Epitran remain raw comparators, not production phonology providers. A qualified Burmese expert IPA gold set and dialect-scoped adjudication remain BLOCKED/PARTIAL.
