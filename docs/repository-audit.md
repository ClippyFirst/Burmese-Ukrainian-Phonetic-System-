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


## Final dual-method and GitHub Pages audit — 2026-10-31

- PR #54 selects orthographic MLCTS (not MLCTS2) for the romanization route and adds the exact Myanmar sample regression: MLCTS mrui. versus MLCTS2 mjou.
- PR #54 adds a machine-readable onset crosswalk for all 35 source consonant/onset graphemes, with source locators, Ukrainian candidate/status and tests. This is not the full MLCTS syllable/rime inventory.
- PR #55 adds separate phonetic and romanization tabs. The phonetic tab remains IPA-first. The romanization tab shows MLCTS plus an explicit PARTIAL Ukrainian crosswalk state; it never falls back to IPA or phonetic Ukrainian output.
- PR #56 ports the necessary production asset fix from stale PR #48: both Mya2Rom browser assets are copied into Vite public output; Vite builds both index.html and system.html; Playwright tests the built preview.
- PR #48 was closed as superseded after the relevant changes were ported. PR #53 (visual styling only) remains open and untouched; its branch was not merged because it is separate from the functional method and Pages work.
- Main commit: fff943db823ae5ca0f4fed50b572cc75cb743f84.
- Main tests workflow [41231199684](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41231199684) passed: pytest 63 passed / 29 subtests passed; npm build; generated-data drift check; Node 3/3; Playwright 48 passed against production Vite preview.
- GitHub Pages deployment [41231199596](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41231199596) succeeded at https://clippyfirst.github.io/Burmese-Ukrainian-Phonetic-System-/ and deployed the main commit above.
- Remaining: MLCTS onset table is DONE_VERIFIED, but vowel/medial/coda/kinzi/asat/numeral/punctuation coverage is PARTIAL; the MLCTS → Ukrainian syllable adapter is TODO; phonetic coverage and independent lexical gold remain research-limited. The repository is a research prototype, not a validated production standard.

 
### Responsive layout merge — 2026-10-31

- PR #62 merged as `78f56512f59bbfa6fc881ccd35e34c4bf1fff7b1`; 36 CSS override lines added to `src/web/styles.css`.
- Exact-head CI [41234651088](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41234651088) passed pytest, Vite build, generated-data drift, Node tests, and Playwright against the built artifact.
- Existing IPA typography and method-switch styles were preserved. PR #53 remains open/unmerged because its branch is diverged and its older stylesheet snapshot was not safe to merge wholesale.
- Original MLC publication, complete MLCTS syllable inventory, MLCTS → Ukrainian syllable adapter, and adjudicated phonetic gold remain open. This is UI verification only; no new Pages deployment is claimed here.


### Primary-source boundary clarification — 2026-10-31

- Located the Library of Congress 2011 *Burmese Romanization Table*. It is explicitly an ALA-LC table, not the MLC/MLCTS source, so it must not be used to validate the project's MLCTS rows. Its medial, conjunct, final, tone-mark, punctuation, numeral and word-division conventions are a distinct system.
- The SIL catalogue endpoint referenced in secondary metadata returned HTTP 403; the original MLC publication remains unavailable. The 94-row Mya2Rom-derived rime inventory is still a vendor implementation inventory with parity tests, not primary-source verification.
- No MLCTS-to-Ukrainian candidate, IPA form, or source permission was added on the basis of this search.


### Browser output integrity regression — 2026-10-31

- PR #64 merged as `d0b7f6351a4151b974ec9ee379f81f7a06da9613`.
- Before the fix, unsupported Myanmar `ꩠ` was present in analysis/status but silently absent from the Ukrainian output (`ကာ ꩠ` rendered as `ка `). The browser output now shows `⟦ꩠ⟧`; unresolved and partially mapped units remain visible as source markers rather than being silently omitted.
- The contextual initial `/j/` + vowel rule now grades the combined Ukrainian target as one unit; `/juː/ → ю` remains covered by the existing browser test.
- Exact-head CI [41238825573](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41238825573) passed pytest 64 + 29 subtests, Node 4/4, Vite build, generated-data drift check, and Playwright 50/50. The full greeting sentence is reconstructed exactly from rendered source-unit rows.
- This verifies source preservation and output honesty, not full phonetic accuracy. Independent lexical IPA gold remains 0 verified entries; MLCTS → Ukrainian syllable adapter and original MLC primary source remain incomplete/blocked.
- Pages deployment [41238926334](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41238926334) completed successfully and deployed `d0b7f6351a4151b974ec9ee379f81f7a06da9613` at https://clippyfirst.github.io/Burmese-Ukrainian-Phonetic-System-/. Main verification [41238926148](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41238926148) passed.


### Diverged layout PR reconciliation — 2026-10-31

- Rechecked open PR #53 (`design/burmese-layout-20261030`) against current main `d0b7f6351a4151b974ec9ee379f81f7a06da9613`: branch is diverged, 5 commits ahead and 11 behind (merge base `272da3970c0e8791c5bc5406cc4289e2c841eeef`). Its only changed files are `index.html`, `system.html`, and a wholesale replacement of `src/web/styles.css`; it contains no engine fix or unique regression test.
- The required responsive behavior was already ported as focused overrides in PR #62 (`78f56512f59bbfa6fc881ccd35e34c4bf1fff7b1`) and verified. The older stylesheet replacement is not safe to merge wholesale because it would replace current IPA typography and method-switch styling.
- PR #53 remains open and untouched. No unique code or test from it was ported in this pass.

## Burmese full-sentence romanization and source-preservation fix — 2026-10-31

- PR #68 merged as \`9075b6e1f8384cc9ae71fe75f12a0b6cc699db15\`; exact-head workflow [41240518900](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41240518900) passed the full configured suite.
- PR #69 merged as \`b6ce024a26bef44c76744aa231b52de551c12c16\`; exact-head workflow [41241791556](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41241791556) passed Python tests, Vite build, generated-data drift, Node tests and Playwright: **52 passed**.
- Root cause: the browser app's Myanmar-script predicate classified U+1040–1049 numerals and U+104A–104B punctuation as romanizable script. Passing them to Mya2Rom caused source loss. The fix preserves those code points and romanizes only contiguous Myanmar text runs, preserving adjacent Latin text and separators.
- Browser regressions cover the four-stop greeting and mixed text with \`ABC\`, \`၁၂၃\`, Myanmar comma \`၊\` and sentence stop \`။\`, in phonetic and MLCTS modes. MLCTS period characters inside romanized forms are not confused with sentence punctuation.
- This verifies bounded source preservation only. It does not establish complete MLCTS coverage, MLC primary-source conformity, or an MLCTS-to-Ukrainian adapter. The 94-row rime table remains vendor-derived; original MLC source is BLOCKED/EVIDENCE_LIMITED; independent lexical IPA gold remains 0.
- PR #53 remains open/unmerged and was not changed. At the time of this checkpoint, a deployment after PR #69 was not yet verified. A later check confirmed Pages deployment [41242001050](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41242001050) succeeded with deployed HTML/runtime/vendor-asset smoke tests; see the cross-mode source-integrity checkpoint.


### Cross-mode Myanmar source-integrity fix — 2026-10-31

- PR #72 merged as `257db544ccb09bb9b51e5cfdf882b12f5b08b7a2`. It fixes adjacent unsupported Myanmar code points being swallowed by a valid phonetic segment and prevents the MLCTS route from silently dropping characters outside its supported inventory.
- The MLCTS allowlist is generated from canonical consonant, independent-vowel, dependent-sign, medial, asat and virama inventories plus explicitly supported vendor tone/special symbols. U+1040–1049 digits and U+104A–104B punctuation are preserved as non-romanized text; unsupported Myanmar code points and orphan signs remain visible as `⟦source⟧` markers.
- Exact-head CI [41243831142](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41243831142) and [41243825927](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41243825927) passed: pytest 64 + 29 subtests, Node, production build, generated-data reproducibility, and Playwright 53/53 against the built artifact.
- The earlier PR #69 deployment is verified: [41242001050](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41242001050) succeeded with deployed-site/runtime-asset smoke checks. PR #72 post-merge Quality [41244193538](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41244193538) passed pytest 64 + 29 subtests, Node tests, production build, generated-data check and Playwright 53/53. Pages deployment [41244193576](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/41244193576) is running/queued; live status remains pending.
- This is bounded source-preservation evidence, not full Unicode or MLCTS standard coverage. The original MLC publication remains BLOCKED/EVIDENCE_LIMITED, the 94-row vendor-derived rime inventory remains PARTIAL, MLCTS → Ukrainian remains TODO, and independent lexical IPA gold remains 0. PR #53 remains open and untouched.
