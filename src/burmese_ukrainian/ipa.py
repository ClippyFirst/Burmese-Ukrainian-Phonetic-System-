from .parser import parse_burmese

ONSET_IPA = {
    "က": "k", "ခ": "kʰ", "ဂ": "ɡ", "ဃ": "ɡ", "င": "ŋ",
    "စ": "s", "ဆ": "sʰ", "ဇ": "z", "ဈ": "z", "ည": "ɲ",
    "တ": "t", "ထ": "tʰ", "ဒ": "d", "ဓ": "dʰ", "န": "n",
    "ပ": "p", "ဖ": "pʰ", "ဗ": "b", "ဘ": "bʰ", "မ": "m",
    "ယ": "j", "ရ": "ɹ", "လ": "l", "ဝ": "w", "သ": "θ",
    "ဟ": "h", "ဠ": "l", "အ": "ʔ",
}
VOWEL_IPA = {
    "e": "e", "i": "i", "ii": "iː", "ai": "ɛ", "u": "u",
    "uu": "uː", "tall_aa": "a", "aa": "a", "anusvara": "",
}


def _ipa(s):
    # Parser diagnostics are part of the phonetic boundary: never turn a
    # partially consumed or malformed grapheme cluster into a plausible IPA
    # string merely because its initial consonant and vowel happen to map.
    if s.get("status") != "established":
        return None

    # Coda/asat and prosodic marks are parsed structurally but do not yet have
    # an evidence-backed surface-IPA realization in this adapter. Withhold the
    # whole syllable rather than silently dropping contrastive material.
    if s.get("coda") or s.get("tone_mark"):
        return None

    o = ONSET_IPA.get(s.get("onset", {}).get("character"))
    if o is None:
        return None
    v = s.get("vowel")
    if not v:
        return o + "?"
    # Anusvara is currently only recognized orthographically. Its nasal/coda
    # realization is contextual and has no evidence-backed IPA mapping here;
    # do not let the empty placeholder silently delete it from the output.
    if any(sign.get("id") == "anusvara" for sign in v["signs"]):
        return None

    vals = [VOWEL_IPA.get(x["id"]) for x in v["signs"]]
    if any(x is None for x in vals):
        return None
    return o + "".join(x for x in vals if x)


def to_ipa(text: str) -> dict:
    result = parse_burmese(text)
    # An isolated bare consonant is incomplete user input, not a safe basis
    # for guessing its inherent vowel. Keep contextual syllables in a word
    # on their existing path until those contexts are separately adjudicated.
    bare_isolated = (
        len(result["normalized"]) == 1
        and len(result["syllables"]) == 1
        and not result["syllables"][0].get("vowel")
        and not result["syllables"][0].get("coda")
        and not result["syllables"][0].get("medials")
        and not result["syllables"][0].get("conjunct")
        and not result["syllables"][0].get("kinzi")
        and not result["syllables"][0].get("tone_mark")
    )
    for syllable in result["syllables"]:
        syllable["ipa"] = None if bare_isolated else _ipa(syllable)
        syllable["phonetic_status"] = (
            "conservative_partial" if syllable["ipa"] else "analysis_dependent"
        )
    result["ipa"] = " ".join(syllable["ipa"] or "?" for syllable in result["syllables"])
    return result
