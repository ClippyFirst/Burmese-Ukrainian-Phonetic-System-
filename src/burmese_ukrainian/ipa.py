from .parser import parse_burmese
from .unicode import BASE_CONSONANTS, KINZI, MEDIALS, SPECIAL, VOWEL_SIGNS

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


def _is_myanmar_phonological_char(char: str) -> bool:
    return (
        char in BASE_CONSONANTS
        or char in VOWEL_SIGNS
        or char in MEDIALS
        or char in SPECIAL
        or char in KINZI
    )


def _standalone_bare_consonant_indices(syllables: list[dict]) -> set[int]:
    """Find bare consonant clusters bounded by non-Myanmar text or input edges.

    Adjacent Myanmar syllable clusters stay on the existing contextual path.
    A bare consonant separated by whitespace, Latin text, or punctuation is a
    standalone token even when the overall input contains multiple characters.
    """
    standalone = set()
    for index, syllable in enumerate(syllables):
        raw = syllable.get("raw", "")
        if len(raw) != 1 or raw not in BASE_CONSONANTS:
            continue
        previous_raw = syllables[index - 1].get("raw", "") if index else ""
        next_raw = syllables[index + 1].get("raw", "") if index + 1 < len(syllables) else ""
        left_is_myanmar = bool(previous_raw) and _is_myanmar_phonological_char(previous_raw[-1])
        right_is_myanmar = bool(next_raw) and _is_myanmar_phonological_char(next_raw[0])
        if not left_is_myanmar and not right_is_myanmar:
            standalone.add(index)
    return standalone


def to_ipa(text: str) -> dict:
    result = parse_burmese(text)
    # A bare consonant bounded as its own token is incomplete input. Do not
    # let unrelated Latin text or whitespace disable the conservative guard.
    # Contiguous Myanmar syllables retain the existing contextual fallback
    # until those inherent-vowel contexts are separately adjudicated.
    bare_isolated = _standalone_bare_consonant_indices(result["syllables"])
    for index, syllable in enumerate(result["syllables"]):
        syllable["ipa"] = None if index in bare_isolated else _ipa(syllable)
        syllable["phonetic_status"] = (
            "conservative_partial" if syllable["ipa"] else "analysis_dependent"
        )
    result["ipa"] = " ".join(syllable["ipa"] or "?" for syllable in result["syllables"])
    return result
