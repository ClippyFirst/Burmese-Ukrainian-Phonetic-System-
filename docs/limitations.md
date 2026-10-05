# Limitations

The current implementation is a research scaffold with hardened data
contracts, not a complete Burmese lexical analyzer or surface-phonetic
synthesizer.

## Established implementation limits

- Full Burmese vowel-combination derivation is not implemented.
- Complete coda and checked-syllable realization is not implemented.
- Tone/register/phonation realization is represented analytically but is not
  fully inferred from orthography.
- Full Burmese allophony and contextual phonological rules are not implemented.
- Corpus-backed lexical validation is not yet available.
- Feature-distance ranking against the canonical Ukrainian inventory is not yet
  implemented.
- The canonical Ukrainian inventory must be supplied to the target adapter;
  it is intentionally not duplicated in this repository.

## Research limits

The following project decisions remain proposal-level or analysis-dependent:

- /h/ → г versus х;
- /ɯ/ → и;
- /θ, ð/ → т;
- treatment of some Burmese /r/ and /j/ environments;
- practical treatment of complex finals and checked syllables.

These must not be presented as official Ukrainian norms.

## Validation limits

The benchmark currently contains structural orthographic seed cases, not a
gold-standard lexical corpus. Therefore the repository must not report
accuracy percentages for the complete system.

The correct status vocabulary is used instead:
ESTABLISHED, WELL_SUPPORTED, ANALYSIS_DEPENDENT, DIALECT_DEPENDENT,
CONTEXT_DEPENDENT, UNCERTAIN, DISPUTED, NOT_ESTABLISHED, UNSUPPORTED.
