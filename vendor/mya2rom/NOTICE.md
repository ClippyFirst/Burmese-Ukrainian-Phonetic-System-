# Third-party romanization engine

This directory vendors Mya2Rom 0.4.4 by Myanmar Open Wordnet, licensed CC-BY-SA-4.0. It provides Burmese romanization profiles including MLCTS2. The upstream project documents limitations for stacked letters, asat forms, sandhi, alternate pronunciations, and Pali/Sanskrit-derived words; output is therefore an orthographic/phonetic candidate, not an authoritative pronunciation.

Upstream: https://github.com/myanmaropenwordnet/mya2rom
License: https://github.com/myanmaropenwordnet/mya2rom/blob/master/License.md

The ClippyFirst integration exposes `mya2rom` to the existing browser module without changing upstream algorithm code.