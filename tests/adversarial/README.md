# Adversarial corpus

Required cases: logical/visual order traps; canonical-equivalent U+103A/U+1037 orderings; kinzi; malformed virama; asat ambiguity; medial combinations; unsupported Myanmar-script languages; Pali/Sanskrit sequences; mixed scripts; ordinary spaces; U+200B.

Cases should record expected structural status and evidence. They must not force an IPA output where the literature is analysis-dependent.


## Shared regression fixture contract

`tests/fixtures/shared_unicode_contract.json` is consumed by both Python and Playwright tests. Each case separates runtime-specific expectations under `python` and `browser`; this is intentional while the engines have different APIs. A shared fixture is not automatically a phonetic gold standard: only add exact IPA or Ukrainian output when a source-backed, scope-defined reference analysis exists. Prefer structural status, preservation, and uncertainty contracts for unsupported or ambiguous material.


## Added whole-message regression (2026-11-01)

`test_python_parser_preserves_multiline_mixed_script_adversarial_input` covers one message containing:
- a valid Burmese syllable before and after an unsupported Myanmar-script character;
- a tab, ASCII identifier and digits;
- CRLF line ending;
- Myanmar digits and punctuation;
- U+200B ZERO WIDTH SPACE;
- emoji and Arabic-script text.

The acceptance contract is exact reconstruction of the NFC-normalized input across the parser's grapheme and syllable records. The Khamti/Extended-C character must be explicitly unsupported, while the neighboring supported Burmese units remain structurally recognized. This is a source-integrity/structural regression, **not** an IPA gold case and must not enter phonological accuracy denominators.
