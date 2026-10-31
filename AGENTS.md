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
- [mattpocock/skills](https://github.com/mattpocock/skills/tree/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa) — behavior-focused tests, clear interfaces, test seams and source-backed research.
- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail/tree/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846) — reuse before invention, smallest complete diff, connected-code review and explicit deferred-work accounting.

When these references conflict with the existing project contract or the user's explicit requirements, follow the project contract and user requirements.
