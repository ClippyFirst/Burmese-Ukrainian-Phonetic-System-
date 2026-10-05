# Architecture

## Authoritative layers

1. Burmese Unicode and orthographic structure are defined by the Burmese data
   and Unicode evidence in this repository.
2. Burmese phonological and phonetic analyses are represented in source-backed
   data tables and analysis records.
3. Burmese IPA is an intermediate representation, not an output spelling.
4. Ukrainian target phonology and orthography are delegated to the canonical
   ClippyFirst/Ukrainian-Phonetic-Inventory repository.
5. Burmese-specific Ukrainian practical decisions are stored in
   data/burmese/ukrainian_practical.csv and data/burmese/practical_rules.csv.
6. Tests validate contracts and known cases; they do not create linguistic
   evidence.

## Runtime pipeline

Unicode normalization
→ grapheme segmentation
→ syllable structure
→ Burmese phonological analysis
→ conservative IPA
→ Ukrainian target adapter
→ practical Ukrainian policy
→ explainable output

The practical policy is deliberately downstream from IPA. Russian Cyrillic
forms are documentary comparison data and are never used as an intermediate
runtime representation.

## Data ownership

Each layer has one intended source of truth:

| Layer | Authoritative repository artifact |
|---|---|
| Burmese Unicode mechanics | src/burmese_ukrainian/unicode.py + Unicode source registry |
| Burmese structural inventories | data/burmese/*.csv |
| Burmese analysis alternatives | data/burmese/analyses.csv + tone_analyses.csv |
| Ukrainian practical decisions | data/burmese/ukrainian_practical.csv |
| Practical rule IDs | data/burmese/practical_rules.csv |
| Ukrainian canonical target inventory | external ClippyFirst/Ukrainian-Phonetic-Inventory |
| Runtime behavior | src/burmese_ukrainian/ |
| Regression evidence | tests/ + benchmark/ |

## Deliberate limitations

The current implementation is not a complete Burmese lexical parser, phonetic
synthesizer, or feature-distance optimizer. A missing analysis must remain
explicitly unresolved rather than being filled by a fallback guess.
