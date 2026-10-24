# Repository reconstruction and audit — 2026-10-05

## Scope

This audit reconstructs the repository as it exists on the current main
history. The initial commit contained only a one-line README; the subsequent
research scaffold was built between 2026-10-02 and 2026-10-04.

## Classification

| Area | Classification | Finding | Action |
|---|---|---|---|
| README | CORE / DOCUMENTATION | Current project identity and scope | Revise only where implementation diverges |
| src/burmese_ukrainian/ | IMPLEMENTATION | Current code, but several modules are conservative scaffolds | Keep; harden contracts before adding features |
| data/burmese/ | RESEARCH EVIDENCE / SUPPORTING DATA | Source-derived inventories and comparative tables | Keep; establish authoritative roles |
| docs/ | DOCUMENTATION | Current methodology plus comparative audit | Keep; reconcile terminology |
| schemas/ | SUPPORTING DATA | Useful but previously inconsistent with runtime serialization | Corrected |
| tests/ | VALIDATION | Small regression suite; not a complete linguistic benchmark | Keep and expand |
| benchmark/ | VALIDATION | Structural seed cases only | Keep; do not call it a gold corpus |
| .github/workflows/ | ENGINEERING | CI definition exists | Keep; execution status must be verified separately |
| temporary/legacy directories | HISTORICAL / OBSOLETE | No such layer was found in the reconstructed history | No archive migration required |

## Key technical findings

1. The parser returned dataclass instances inside JSON-like dictionaries,
   while tests expected nested dictionaries.
2. The syllable schema required a top-level status that the runtime did not
   expose.
3. data/burmese/phonotactics.csv had a six-field data row against a
   five-column header.
4. src/burmese_ukrainian/ukrainian.py contained a hardcoded seed mapping
   despite the repository documenting the Ukrainian inventory as an external
   dependency.
5. The current IPA layer is explicitly partial and must not be described as a
   complete Burmese phonetic engine.
6. The practical mapping tables are currently proposal data, not a validated
   Ukrainian standard.

## Research-integrity findings

- Russian Burmese practical transcription has a strong bibliographic basis,
  including Epstein (1959) and the 1978 USSR instruction.
- Serbian and Bulgarian entries must remain methodological/research-gap
  records rather than being presented as established Burmese-specific systems.
- Project decisions such as /h/ → г and /ɯ/ → и remain analysis-dependent
  or proposal-level decisions and must not be upgraded to established facts.

## Audit policy

Potentially unique research evidence is preserved. No destructive deletion is
performed merely because a file is old, small, generated-looking, or awkwardly
named.

The repository currently contains no separate historical corpus that requires
archiving. If later history reveals a unique rejected analysis, it should be
moved to research/historical/ or research/decisions/ rather than deleted.


## External IPA and benchmark audit — 2026-10-24

- The malformed-parse guard and fail-closed benchmark gold-provenance gate are on main; an ADJUDICATED row without non-empty IPA, source_id or profile now stops scoring instead of silently changing the denominator.
- Epitran 1.35.3 ran successfully on 6 Burmese probes with 0 runtime errors in [run 40121355875](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40121355875). This verifies execution only. Epitran upstream explicitly flags Burmese support as limited due to orthographic ambiguity.
- Independent gold count is 0; accuracy is null. Inherent vowels, medials, coda/phonation and tone conventions still require a source-located, independently adjudicated corpus. External systems remain optional and disabled in production.
- Latest smoke artifact ZIP SHA-256: `28c05acec1658a4002dce200a059026a2b14395a5c5f0232b2a449f620e7e424`; durable report and registry are aligned to this run.
