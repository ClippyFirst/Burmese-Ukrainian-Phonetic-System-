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

- Harness: added; CI/local execution still required on this branch.
- Adjudicated language-specific gold rows: not yet established by this document.
- Candidate engine availability, version, licenses, and language-specific output quality: unverified until recorded as run evidence.
- Release status: research prototype; no accuracy claim is authorized by this registry.

## Existing external run evidence (reconciled 2026-10-24)

- `scripts/benchmark_g2p.py` and `.github/workflows/optional-epitran-benchmark.yml` are present and pin `epitran==1.35.3`, but no successful workflow artifact was confirmed in this pass. Treat execution as **NOT VERIFIED**, not done.
- The existing source audit inspected Epitran's tagged `mya-Mymr` mapping/pre/postprocessor statically and records upstream warnings that Burmese support is limited by orthographic ambiguity. Static inspection is not a runtime benchmark.
- [Goruut](https://github.com/neurlang/goruut) lists Burmese support upstream, but is not yet executed here. [myG2P](https://github.com/ye-kyaw-thu/myG2P) is license-constrained: the repository's existing audit identifies its pronunciation dictionary as CC BY-NC-SA 4.0, so do not bundle it for commercial use without permission.
- Next: run pinned Epitran smoke, retain every output/error and mapping hash, then compare only after independently adjudicating Burmese tone/phonation, medials, codas, and lexical readings.
