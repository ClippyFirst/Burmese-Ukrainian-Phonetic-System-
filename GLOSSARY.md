# Burmese → Ukrainian project glossary

This glossary defines the repository's engineering and annotation vocabulary. It does not settle disputed Burmese phonetic analyses.

| Term | Meaning in this repository |
|---|---|
| **Myanmar/Burmese orthography** | The source Unicode text. Script-block membership is broader than the supported Standard Burmese inventory. |
| **Grapheme cluster** | A source-preserving orthographic unit parsed from Myanmar code points; not necessarily a lexical word or phonological syllable. |
| **Syllable analysis** | Structural decomposition into onset, medials, vowel signs, coda/asat and related marks. Structural validity alone does not establish pronunciation. |
| **Kinzi** | The encoded nasal-plus-virama sequence treated as a structural feature, not silently discarded. |
| **Virama / conjunct** | Myanmar combining structure used in consonant sequences. A misplaced virama is malformed and must not yield plausible prefix IPA. |
| **Medial** | A written consonant modifier (e.g. medial ra/wa) preserved as structural information; its phonetic realization needs source support. |
| **Checked syllable / coda** | A syllable with a checked/final consonant environment. The current IPA adapter withholds output when coda realization is not established. |
| **Tone / register / phonation** | Distinct prosodic and voice-quality dimensions. Do not collapse them into one tone label or infer them from orthography without evidence. |
| **IPA adapter boundary** | The inspectable Burmese pronunciation representation consumed by the Ukrainian adapter. Unsupported coda or prosody must remain withheld. |
| **MLCTS** | Myanmar Language Commission orthographic transcription. It is a separate romanization route, not IPA or a pronunciation model. |
| **Mya2Rom** | Vendor-derived implementation/reference for romanization; not primary proof of the original MLCTS specification or a source of phonetic gold. |
| **Ukrainian practical form** | A project-specific target spelling derived from supported IPA/target inventory evidence, not an official national standard. |
| **Structural probe** | A parser/source-integrity test. It cannot enter an IPA accuracy denominator. |
| **Independent IPA gold** | A rights-cleared, source-located, independently double-annotated and adjudicated record. Current corpus has no such records. |
| **Reference profile** | The bounded pilot target: contemporary Standard Burmese with Yangon as reference variety, careful citation-form speech (my-yangon-careful-citation-v1). This does not imply homogeneous Yangon speech. |

## Canonical decisions and evidence

- Architecture: docs/architecture.md; source/decision evidence: docs/references.md, docs/audits/current/.
- Current execution and blockers: docs/MASTER-EXECUTION-PLAN-AND-CHAT-HANDOFF.md.
- Canonical linguistic registries: data/burmese/*.csv; generated browser data: src/web/generated/data.js.
