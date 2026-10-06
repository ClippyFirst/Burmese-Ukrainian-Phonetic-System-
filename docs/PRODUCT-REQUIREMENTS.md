# Burmese → Ukrainian — Product Requirements

**Status:** Implementation baseline  
**Product:** Browser-based Burmese → Ukrainian practical transcription service  
**Reference product:** ClippyFirst/chinese-for-ukrainians

## 1. Product outcome

A Ukrainian-speaking reader, translator, researcher, editor or learner can paste Burmese text and receive normalized Burmese input, structural segmentation, conservative IPA where established, the project's Ukrainian practical transcription, and explicit uncertainty where evidence is incomplete.

The product is a **transcription tool, not a translation tool**.

## 2. Two-page product structure

### Page 1 — Service

Primary task: **Burmese input → Ukrainian practical transcription**.

Supporting representations:
- Burmese source;
- IPA / phonetic analysis;
- Ukrainian practical output;
- short rule/explanation status;
- copy actions.

### Page 2 — The system

Scientific/methodological explanation of the author's Ukrainian system:
- scope and terminology;
- Burmese orthography and Unicode structure;
- Burmese phonological assumptions;
- IPA layer;
- Ukrainian target-language principles;
- Russian practical transcription as a documentary control layer;
- decisions that diverge from Russian;
- treatment of aspiration, /ŋ/, /w/, /r/, /h/, /ɯ/, /ʔ/;
- tone/register/phonation policy;
- evidence and uncertainty statuses;
- examples;
- references and repository provenance.

## 3. Functional requirements

### FR-01 Input
Accept arbitrary Unicode text in a multiline textarea.

### FR-02 Normalization
Normalize Burmese Unicode conservatively and preserve the user's visible source text.

### FR-03 Analysis
Return deterministic structural analysis for supported Myanmar-script clusters.

### FR-04 IPA
Expose IPA only where the current repository analysis supports it. Unknown or incomplete derivations must be marked rather than guessed.

### FR-05 Ukrainian output
Apply only the canonical repository correspondence/rule tables. No hidden mapping table may exist in application code.

### FR-06 Explanation
For each result expose a concise status and, where useful, the rule/provenance responsible for the output.

### FR-07 Copy
Copy Burmese, IPA and Ukrainian output independently.

### FR-08 Preservation
Preserve whitespace, punctuation, Latin text, numbers and unsupported symbols.

### FR-09 Transparency
Clearly distinguish ESTABLISHED, WELL_SUPPORTED, PROPOSED, ANALYSIS_DEPENDENT, CONTEXT_DEPENDENT, DIALECT_DEPENDENT, UNCERTAIN, NOT_ESTABLISHED and UNSUPPORTED.

### FR-10 Accessibility
Keyboard operation, visible focus, semantic controls, readable contrast, screen-reader labels, reduced motion and mobile layout are required.

### FR-11 Privacy
Normal conversion must happen locally in the browser. No analytics, accounts or user-text upload path in the static MVP.

### FR-12 Scientific page
The second page must be readable as a methodological paper, not marketing copy.

## 4. Non-goals

- machine translation;
- automatic Latin transliteration as the primary product;
- treating Myanmar script as synonymous with Burmese;
- silently converting Burmese tone into Ukrainian lexical stress;
- claiming a universal Burmese pronunciation model when evidence is dialect- or analysis-dependent;
- importing Russian transcription mechanically.

## 5. Definition of done

The service is release-ready when:
- both pages work without a backend;
- the main converter is deterministic;
- canonical practical tables are the sole application mapping source;
- representative Burmese examples produce stable outputs;
- unsupported/incomplete cases are surfaced honestly;
- copy and example controls work;
- whitespace and punctuation survive conversion;
- mobile and keyboard use are practical;
- unit and browser tests pass;
- release checks pass;
- documentation describes the implemented behavior exactly;
- the Myanmar national palette is used as an identity accent without sacrificing readability.

## 6. Product language

Preferred: «Бірманський текст», «Практична українська транскрипція», «Вимова / IPA», «Пояснення системи», «Працює локально», «Потребує аналізу», «Не встановлено».

Avoid: «100% точний», «перекладач», «AI-translator», «автоматично правильно» and winner-like claims about competing transcription systems.
