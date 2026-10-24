# Burmese → Ukrainian — Release Checklist

1. Canonical data validation passes.
2. Generated web data is deterministic.
3. Unit tests pass.
4. Browser tests pass.
5. Production build succeeds.
6. No runtime network dependency exists.
7. No analytics/telemetry exists.
8. CSP is present.
9. Main service page works on desktop and mobile.
10. Scientific system page is reachable and internally consistent.
11. Example outputs are manually inspected against repository policy.
12. Uncertainty is visible for proposed, analysis-dependent and incomplete cases; malformed or partially parsed syllables must not emit segment IPA.
13. National palette remains accessible and restrained.
14. README accurately describes the service and its limitations.
15. GitHub Pages deployment workflow, if enabled, is validated by an actual workflow run.


## Post-merge integrity-fix verification — 2026-10-24

- Merged code HEAD: `6bea361e6ef6f551a699439cc85a99945b006f94`.
- Main tests: [run 40113299242](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40113299242) passed, including pytest, generated-data drift validation, npm build/tests and Playwright browser tests.
- GitHub Pages deployment: [run 40113299248](https://github.com/ClippyFirst/Burmese-Ukrainian-Phonetic-System-/actions/runs/40113299248) passed for the merged HEAD.
- The malformed-parse guard prevents IPA generation when the parser did not fully consume the syllable. It does not resolve the documented research gaps in medials, codas, tones or inherent-vowel realization.
- Release status remains **research prototype**: engineering checks are green, but independent gold IPA is absent and empirical accuracy is not measured.
