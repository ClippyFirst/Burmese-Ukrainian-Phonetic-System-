# Codebase map — Burmese → Ukrainian

**Audit basis:** main aab45f9165d7f9cd7423425ff28186e1c29af0bf; task branch additionally carries the 2026-11-02 profile and quality-handoff updates. This map distinguishes the phonetic path from the orthographic MLCTS path.

## User-facing entry points

- Python public API: src/burmese_ukrainian/__init__.py exports parse_burmese, to_ipa, ipa_to_ukrainian, practical_from_ipa and explain.
- Browser instrument: src/web/app.js; canonical CSV registries are converted into src/web/generated/data.js by scripts/generate-web-data.mjs.
- There is no src/burmese_ukrainian/cli.py in the audited tree; do not document or invoke a nonexistent CLI entry point.

## Phonetic flow

~~~text
Python public API / browser app
  └─ parser.parse_burmese
       ├─ Unicode/grapheme + syllable structure
       ├─ preserve kinzi, virama, medials, vowels, coda and marks
       └─ explicit malformed/unsupported status
  └─ ipa.to_ipa
       ├─ conservative _ipa adapter
       ├─ withhold unsupported coda / tone-mark / anusvara realizations
       └─ per-syllable IPA and phonetic status
  └─ ukrainian.ipa_to_ukrainian
       └─ external Ukrainian inventory; unavailable inventory stays unavailable
~~~

The browser has its own runtime path in src/web/app.js; shared Unicode and adversarial fixtures are the parity contract. Inspect the browser route separately rather than assuming Python function reuse.

## Separate orthographic route

- MLCTS romanization is handled by the separate practical/romanization data and browser path.
- Do not route MLCTS through the IPA adapter or use it to invent tone, vowel quality or Ukrainian phonetic output.
- generator.generate_structural_syllables emits structural candidates only; it is not an attested lexical corpus or a pronunciation generator.

## Data and generated-artifact ownership

- Canonical registries: data/burmese/*.csv.
- Source claims and phonological evidence: data/burmese/sources.csv, source_claims.csv, phonological_rules.csv, and docs/audits/current/.
- Generated browser data: src/web/generated/data.js; regenerate, never hand-edit.
- Gold lifecycle/scorer: scripts/ipa_gold_corpus.py, scripts/benchmark_ipa.py, data/benchmark/.

## High-risk seams

1. Myanmar code point vs supported Standard Burmese inventory: reject unsupported extension letters explicitly.
2. Kinzi/virama parsing: malformed combining order must withhold IPA.
3. Tone, register, phonation, vowel and checked-coda realization: no deterministic output without scoped evidence.
4. IPA-to-Ukrainian adapter: do not fall back to hidden inventories or orthographic MLCTS.
5. Generated web data and browser parity: edit canonical data, regenerate and verify drift.
6. Gold ingestion: only independently adjudicated, rights-eligible and held-out IPA may be scored.

## Verification

- Python: python -m pytest -q.
- Data/build/browser: npm run build, npm test, npx playwright install --with-deps chromium, npm run test:browser:built.
- Check generated data and built relative assets. The latest task-branch CI must be checked after the final commit.
- A green engineering suite does not prove Burmese phonetic accuracy or expert adjudication.
