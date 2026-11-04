# Agent instructions — Burmese → Ukrainian research system

This file is the project-specific entry point for coding agents. It complements, rather than replaces, the canonical project documents.

## Agent context files

- Read [GLOSSARY.md](GLOSSARY.md) for project vocabulary before designing interfaces or naming tests.
- Read [docs/agents/issue-tracker.md](docs/agents/issue-tracker.md) before creating or updating issues.
- Read [docs/agents/codebase-map.md](docs/agents/codebase-map.md) to distinguish the phonetic pipeline from the MLCTS route and trace high-risk seams.

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


- For new or ambiguous work, establish the intended outcome, audience, why and observable success criteria before designing; inspect existing project context first. Ask only questions whose answers would materially change the deliverable. Do not add process or intermediate-approval gates when the user has explicitly authorized autonomous one-pass execution.
- At GREEN, run the repository's full project test command even if the task named only a focused test file. Report every failure observed; a focused passing test is not a green project suite.

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

- [obra/superpowers](https://github.com/obra/superpowers/tree/22f0b463e7a5e579904dd6211a520321035526f7) — test-first work, explicit plans, root-cause debugging, review and evidence before completion.
- [mattpocock/skills](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d) — behavior-focused tests, clear interfaces, test seams and source-backed research.
- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail/tree/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846) — Ponytail current main: trace the real code path and data flow, map entry points and expected load before repository-level audit, review beyond the diff, preserve trust-boundary validation/data-loss handling/accessibility, test branching/parser/security logic, and report skipped checks and residual risk.

When these references conflict with the existing project contract or the user's explicit requirements, follow the project contract and user requirements. Do not import these repositories as runtime dependencies.

## Methodology source refresh — 2026-11-02

The adopted engineering references were checked against current upstream revisions without importing them as runtime dependencies:

- Superpowers 7.0.2: `obra/superpowers@22f0b463e7a5e579904dd6211a520321035526f7` — explicit plans, true RED/GREEN TDD, systematic debugging, code review, and verification-before-completion. Selected v7.0.2 refinements adopted here: run the repository's full test command at GREEN even when the task names one test file; establish intended outcome/audience/why before designing ambiguous new work; ask only questions that can change the deliverable. Do not impose intermediate approval gates when the user has explicitly authorized one-pass execution.
- mattpocock/skills release v1.3.2: `d1478fcb140db0b93c0c8df17bcfd311844749d0`; current main snapshot: `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d` — composable skills, source-backed research, test-first implementation, and two-axis review (spec compliance separately from repository standards).
- Ponytail 5.3.3: `7801d061243d7b753bad0e0b3c057cd250b11755` — codebase/data-flow audit, connected-code review, minimal complete changes, and explicit preservation of security, data integrity, and accessibility.

These references guide the method; project-specific linguistic, provenance, privacy, rights, and fail-closed requirements remain authoritative.



## Methodology source refresh — 2026-11-04

- Rechecked all four upstream references. Unlazy remains at `16671491f6679ad9378f52604d3bc2415b4120c7`; mattpocock/skills at `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`; Ponytail at `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846`.
- Superpowers v7.0.2 was reviewed against v7.0.1. Adopted full-suite verification at GREEN and intent-first design with fewer, outcome-changing questions. Did not import harness plugins, helper scripts or the SDD runtime. The default explicit design-approval ceremony is not imposed when a user has already authorized autonomous one-pass execution.

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


## Review and evidence refinements

- Separate final review into specification/acceptance compliance and repository standards, conventions, and maintainability. Read applicable `CONTRIBUTING.md`, coding-standards files, and adjacent patterns; standards review must not weaken product or linguistic requirements.
- A RED result is valid only when the intended assertion fails for the intended reason. For mutation-based diagnosis, inspect the diff against a pristine baseline and confirm the mutation changed relevant code; a no-op edit is not evidence.
- Follow repository issue/PR templates and identify the filer accurately. Never present agent-generated text as human-authored; leave owner-authored sections for the owner.
- Never force-remove a worktree or discard untracked files to make cleanup succeed. Inspect and preserve, relocate, commit, or delete them only with explicit owner direction.


## Methodology application — 2026-11-02

The repository now keeps its own domain glossary, GitHub issue-tracker instructions and source-verified codebase map under version control. Use these as context for the composable engineering skills; do not install external repositories as runtime dependencies or duplicate their whole skill trees. Apply Superpowers for scoped plans, RED/GREEN TDD and verification; apply Matt Pocock's codebase-design, research and two-axis review principles; apply Ponytail's real-flow audit, minimal complete change and residual-risk reporting. Linguistic evidence, corpus rights and fail-closed contracts always take precedence.


## Completion gates and task decomposition — 2026-11-04

The project also adopts selected completion-discipline practices from [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy/tree/16671491f6679ad9378f52604d3bc2415b4120c7), reviewed at upstream commit `16671491f6679ad9378f52604d3bc2415b4120c7` (source reports 2.1.0; the inspected main snapshot is pinned here for reproducibility). This is a methodology reference, not an installed tool or runtime dependency.

- Before a substantial change, turn each acceptance-changing requirement into an observable ledger item. Reuse the canonical master handoff and existing completion register; do not create a competing task ledger.
- A runnable acceptance item names the exact command or hosted workflow, the expected result, and the evidence location. A manual item names the reviewer/evidence required and remains open until that evidence exists.
- Decompose only along real dependency and file-ownership boundaries. Do not parallelize overlapping writes or invent agent handles, branches, test results, or review evidence. Keep checks sequential unless independence and isolation are demonstrated.
- Re-run the relevant checks on the exact final commit, including checks previously marked complete when their inputs or dependencies changed. A previous green run is not evidence for a later tree.
- Distinguish implementation success from terminal handoff: an external blocker may be precisely documented, but it must never be represented as a successful acceptance gate.
- Review every command and script before execution. A declared command is not safe merely because it appears in a ledger; it runs with the available environment and permissions.

The existing repository status vocabulary remains authoritative: `DONE_VERIFIED`, `PARTIAL`, `TODO`, `BLOCKED`, and `DEFERRED`. Do not copy Unlazy's checker, hooks, approval store, or orchestration runtime into this project without a demonstrated need; the current GitHub Actions, canonical handoff and test infrastructure remain the source of execution evidence.
