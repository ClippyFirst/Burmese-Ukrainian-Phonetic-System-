# Agent instructions — Burmese → Ukrainian research system

This file is the project-specific entry point for coding agents. It complements, rather than replaces, the canonical project documents.

## Read before changing the project

1. Read docs/MASTER-EXECUTION-PLAN-AND-CHAT-HANDOFF.md first. It is the canonical task ledger and continuation record; continue unfinished work and do not create a competing plan.
2. Read the relevant parts of docs/repository-audit.md, docs/romanization-to-ukrainian-matrix.md, docs/methodology.md, docs/architecture.md, docs/limitations.md, docs/references.md, and the current audit documents under docs/audits/current/.
3. Inspect current main, recent commits, open/recent PRs, branches, CI and Pages workflows before editing. Compare old branches with current main; never merge a diverged stylesheet or engine snapshot blindly.
4. Read the complete code path being changed, including callers, tests, fixtures, generated data, vendor code and deployment workflow.

## Engineering method

- Prefer the smallest complete change. Reuse existing modules, data registries, public interfaces and test seams before adding abstractions, dependencies or parallel implementations.
- For bug fixes and behavior changes, reproduce the user's exact symptom and trace it to its source before editing. Do not patch a downstream symptom.
- Use test-first development: add one focused regression, observe the expected failure, implement the minimum fix, then run the focused test and the complete relevant suite.
- Test observable behavior at a public seam. Expected values must be independent of the implementation; avoid tautological assertions and mocks that bypass the code path.
- Review connected code, not only the diff: callers, Unicode handling, mixed-script input, source preservation, generated artifacts, Python/browser parity, accessibility and deployment behavior.
- Do not add dependencies without a concrete need that existing code or the platform cannot meet. Explain maintenance and licensing implications before adding one.
- Record intentional limits with explicit statuses and revisit triggers. A passing engineering suite does not establish linguistic accuracy.

## Linguistic and data invariants

The phonetic route is:

Burmese orthography → structural analysis → Burmese phonology → IPA → Ukrainian target adaptation → Ukrainian practical orthography.

- IPA is the inspectable boundary between Burmese phonological analysis and Ukrainian adaptation. Do not independently generate the phonetic Ukrainian result from source graphemes.
- Keep the orthographic MLCTS route separate from the phonetic route. MLCTS must not be used to invent IPA, tone, vowel quality or pronunciation; never fall back to the IPA adapter for romanization output.
- The selected profile is Standard MLCTS as an orthographic transcription, not modified MLCTS, BGN/PCGN, ALA-LC or a phonetic transcription. Keep those systems distinct.
- The current Mya2Rom implementation and its 94-row rime inventory are vendor-derived evidence, not primary verification of the original Myanmar Language Commission publication. Do not claim complete MLCTS conformance or invent source permissions.
- Preserve source spans, kinzi, virama/conjunct structure, medials, vowels, codas, tone/prosody marks, punctuation, numerals, whitespace and Unicode normalization. Every input unit must either be represented or explicitly marked unsupported/uncertain; never silently drop text.
- Myanmar digits and punctuation U+1040–104B are passthrough material, not syllabic text to send to Mya2Rom. MLCTS periods inside romanized forms are not sentence punctuation.
- Distinguish project Ukrainian proposals from established Burmese phonology and from an official Ukrainian standard. Do not invent IPA, lexical gold, source claims, benchmark scores or accuracy.
- Shared structural fixtures and browser regressions are engineering evidence, not independently adjudicated lexical IPA gold. Keep accuracy unmeasured while independent gold is absent.
- Canonical linguistic registries live under data/burmese/*.csv. Regenerate browser data through the repository's generator; do not hand-edit generated output. Keep Python and browser behavior aligned through shared fixtures and parity tests.

## Verification commands

Run all checks relevant to the change. The release-level engineering gate currently includes:

~~~bash
python -m pytest -q
npm run build
npm test
npx playwright install --with-deps chromium
npm run test:browser:built
~~~

Also check generated-data drift and built relative asset paths. The Pages workflow runs on main pushes and smoke-tests the deployed HTML, runtime, CSS and Mya2Rom assets. A green PR workflow is not proof that the latest Pages deployment completed; verify the deployment separately.

## Branches, reviews and handoff

- Start from the latest main on a clearly named task branch. Preserve unrelated branches and work.
- Inspect open and closed PRs and compare relevant branches before porting work. Reuse merged work; do not resurrect superseded patches without a demonstrated missing behavior.
- Do not force-push, delete user branches, merge blindly, publish a release, change repository settings or choose a project license.
- Review the full change against the originating requirement and repository standards. Fix material findings and run fresh verification on the exact final head before merging.
- Update the existing master handoff and repository audit in place. Use DONE_VERIFIED, PARTIAL, TODO, BLOCKED and DEFERRED consistently with the evidence.
- In the final report, state what was checked, what was not checked, exact verification evidence, unresolved blockers and remaining risk.

## Adopted engineering references

These are methodological references, not runtime dependencies. Adopt selected practices; do not copy their repositories wholesale or install them as project dependencies.

- [obra/superpowers](https://github.com/obra/superpowers/tree/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b) — test-first work, explicit plans, root-cause debugging, review and evidence before completion.
- [mattpocock/skills](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d) — behavior-focused tests, clear interfaces, test seams and source-backed research.
- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail/tree/7801d061243d7b753bad0e0b3c057cd250b11755) — Ponytail 5.3.3: trace the real code path and data flow, map entry points and expected load before repository-level audit, review beyond the diff, preserve trust-boundary validation/data-loss handling/accessibility, test branching/parser/security logic, and report skipped checks and residual risk.

When these references conflict with the existing project contract or the user's explicit requirements, follow the project contract and user requirements. Do not import these repositories as runtime dependencies.

## Methodology source refresh — 2026-11-02

The adopted engineering references were checked against current upstream revisions without importing them as runtime dependencies:

- Superpowers 7.0.1: `obra/superpowers@2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` — explicit plans, true RED/GREEN TDD, systematic debugging, code review, and verification-before-completion. At GREEN, verify the project suite, not only the narrow test that first went red.
- mattpocock/skills current main: `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d` — composable skills, source-backed research, test-first implementation, and two-axis review (spec compliance separately from repository standards).
- Ponytail 5.3.3: `7801d061243d7b753bad0e0b3c057cd250b11755` — codebase/data-flow audit, connected-code review, minimal complete changes, and explicit preservation of security, data integrity, and accessibility.

These references guide the method; project-specific linguistic, provenance, privacy, rights, and fail-closed requirements remain authoritative.



## Whole-message adversarial benchmark requirements

Every parser, romanizer, phonetic adapter, CLI and browser change that can affect user text must be exercised at the complete-message boundary, not only with isolated syllables. Extend the existing canonical fixtures; do not create a parallel corpus.

- Include realistic mixed messages with multiple supported units, unsupported/foreign-script units adjacent to supported ones, ASCII and native numerals, punctuation, ordinary and repeated whitespace, tabs, LF/CRLF, and relevant Unicode format controls. Add script-extension characters that belong to a broader Unicode block but not to the target language inventory.
- Include malformed and ambiguous sequences, combining-mark order variants, repeated/illegal modifiers, long messages, and paired minimal contrasts. Each case must state the exact property under test and expected local/global status.
- Assert that every source unit is represented or explicitly marked unsupported; never silently delete, normalize away, reorder or merge source material. Verify reconstruction under the repository's declared normalization contract, including source spans and separator preservation where the API exposes them.
- An unsupported unit must not erase or downgrade valid neighboring units unless the public contract explicitly requires whole-input rejection. Check both local and aggregate status.
- Run the same canonical cases through Python and browser/service entry points wherever both exist. Keep runtime-specific expected shapes separate while sharing the input and semantic contract.
- Maintain separate datasets for (1) Unicode/source-integrity probes, (2) structural/phonological regression cases, and (3) independently adjudicated lexical IPA gold. Only the third may enter accuracy denominators; never infer IPA or Ukrainian output for adversarial cases without a scoped, source-located reference.
- For external G2P comparisons, pin engine/version/model/profile, retain immutable raw output and errors, record mapping/model/data hashes and license provenance, and score only on held-out independent gold. Inter-engine agreement and successful execution are diagnostics, not correctness.

Before accepting a new adversarial fixture, review whether its expected result is independent of the implementation and whether the test would fail if a source unit were dropped, a boundary changed, or uncertainty were silently converted into a confident output.
