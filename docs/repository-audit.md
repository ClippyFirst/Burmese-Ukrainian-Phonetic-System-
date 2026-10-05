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
