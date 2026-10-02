# Methodology

The target is contemporary Standard Burmese, with Yangon-oriented scope only where a source supports it. Myanmar script is not treated as synonymous with Burmese.

The scientific pipeline is Unicode → graphemic structure → syllable structure → phonology → surface phonetics → IPA → feature space → Ukrainian target.

Unicode is authoritative for encoding and ordering. Phonological claims are independently sourced. Conflicting analyses are retained as competing analyses rather than averaged.

Prosody is represented as separate dimensions: tone category, pitch contour, register, phonation, duration and checkedness.

The Ukrainian inventory is an external dependency. This repository does not duplicate it; the adapter must ultimately consume the canonical ClippyFirst/Ukrainian-Phonetic-Inventory schema.

The present implementation is deliberately conservative: incomplete evidence produces explicit uncertainty rather than invented IPA or orthography.
