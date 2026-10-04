"""Burmese → Ukrainian practical layer.

This module deliberately consumes Burmese IPA/phonological values rather than
Myanmar characters or Russian spellings. It is a proposal layer: mappings that
depend on disputed Burmese analysis or Ukrainian editorial adjudication are
returned with explicit status.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PracticalCandidate:
    text: str
    status: str
    rule_ids: tuple[str, ...]
    reason: str


DIRECT = {
    "p": "п", "b": "б", "t": "т", "d": "д",
    "k": "к", "ɡ": "ґ", "m": "м", "n": "н",
    "s": "с", "z": "з", "ɲ": "нь", "l": "л",
    "r": "р", "j": "й", "w": "в",
    "i": "і", "e": "е", "a": "а", "u": "у",
    "o": "о", "ɔ": "о", "ɛ": "е", "ɯ": "и",
}

NEUTRALIZE = {
    "pʰ": ("п", "UA-BUR-ASP-P"),
    "tʰ": ("т", "UA-BUR-ASP-T"),
    "kʰ": ("к", "UA-BUR-ASP-K"),
    "sʰ": ("с", "UA-BUR-ASP-S"),
    "tɕ": ("ч", "UA-BUR-AFF"),
    "tɕʰ": ("ч", "UA-BUR-AFF"),
    "ŋ": ("нг", "UA-BUR-NG"),
    "h": ("г", "UA-BUR-H"),
    "θ": ("т", "UA-BUR-TH"),
    "ð": ("т", "UA-BUR-TH"),
    "ʔ": ("", "UA-BUR-GLOTTAL"),
}

def rank_ukrainian_candidates(ipa: str) -> list[PracticalCandidate]:
    """Return deterministic proposal candidates, preserving uncertainty."""
    if not ipa:
        return []
    if ipa in NEUTRALIZE:
        text, rule = NEUTRALIZE[ipa]
        status = "analysis_dependent" if ipa in {"h", "θ", "ð"} else "proposed"
        return [PracticalCandidate(text, status, (rule,), "target-language adaptation")]
    if ipa in DIRECT:
        return [PracticalCandidate(DIRECT[ipa], "proposed", ("UA-BUR-DIRECT",), "direct target")]
    return [PracticalCandidate("?", "not_established", ("UA-BUR-UNMAPPED",), "No project rule yet")]

def practical_from_ipa(ipa: str) -> dict:
    candidates = rank_ukrainian_candidates(ipa)
    return {
        "ipa": ipa,
        "candidates": [c.__dict__ for c in candidates],
        "status": candidates[0].status if candidates else "insufficient_input",
    }
