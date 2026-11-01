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
