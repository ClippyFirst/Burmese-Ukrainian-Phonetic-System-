# Architecture

The package separates Unicode mechanics, grapheme parsing, syllable structure, phonology/prosody, IPA, and Ukrainian target generation.

Data files contain linguistic claims. Python executes transformations and validation. The generated-syllable module produces structural candidates and explicitly does not claim lexical attestation.

The Ukrainian layer is an adapter to the canonical ClippyFirst/Ukrainian-Phonetic-Inventory project rather than a duplicated inventory.
