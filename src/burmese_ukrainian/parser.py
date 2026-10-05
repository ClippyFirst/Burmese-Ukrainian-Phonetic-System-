"""Unicode-aware Burmese grapheme and syllable parser.

The parser is intentionally structural: it does not infer phonology merely
because a Myanmar sequence is well-formed orthographically.
"""

from __future__ import annotations

from dataclasses import asdict

from .model import Syllable
from .unicode import (
    BASE_CONSONANTS,
    KINZI,
    MEDIALS,
    SPECIAL,
    VOWEL_SIGNS,
    codepoint_name,
    is_myanmar,
    normalize_burmese,
)


def segment_graphemes(text: str) -> list[str]:
    """Segment Myanmar-script clusters conservatively."""
    s = normalize_burmese(text)
    out: list[str] = []
    i = 0

    while i < len(s):
        if not is_myanmar(s[i]):
            out.append(s[i])
            i += 1
            continue

        start = i
        i += 1
        while i < len(s) and is_myanmar(s[i]):
            if (
                s[i] in BASE_CONSONANTS
                and s[i - 1] != "\u1039"
                and s[i - 3 : i] != KINZI
            ):
                break
            i += 1
        out.append(s[start:i])

    return out


def _parse_cluster(cluster: str) -> Syllable:
    sy = Syllable(raw=cluster, codepoints=[f"U+{ord(c):04X}" for c in cluster])
    i = 0

    if cluster.startswith(KINZI):
        sy.kinzi = {
            "sequence": [f"U+{ord(c):04X}" for c in KINZI],
            "base": "nga",
            "phonological_role": "final_nasal",
        }
        i = 3

    if i >= len(cluster):
        sy.analysis.status = "invalid"
        return sy

    if cluster[i] in BASE_CONSONANTS:
        ch = cluster[i]
        sy.onset = {
            "character": ch,
            "codepoint": f"U+{ord(ch):04X}",
            "unicode_name": codepoint_name(ch),
        }
        i += 1
    else:
        sy.analysis.status = "unsupported_or_malformed"
        return sy

    while i < len(cluster) and cluster[i] == "\u1039":
        if i + 1 < len(cluster) and cluster[i + 1] in BASE_CONSONANTS:
            c = cluster[i + 1]
            sy.conjunct.append({
                "character": c,
                "codepoint": f"U+{ord(c):04X}",
                "role": "subjoined_consonant",
            })
            i += 2
        else:
            sy.analysis.status = "invalid"
            return sy

    while i < len(cluster) and cluster[i] in MEDIALS:
        medial = MEDIALS[cluster[i]]
        sy.medials.append(medial)
        i += 1
        if i < len(cluster) and cluster[i] == "\u103a" and medial["id"] == "medial_ya":
            sy.coda = {
                "marker": "asat",
                "codepoint": "U+103A",
                "orthographic_function": "contextual",
            }
            i += 1

    vp = []
    while i < len(cluster) and cluster[i] in VOWEL_SIGNS:
        vp.append(VOWEL_SIGNS[cluster[i]])
        i += 1

    if vp:
        sy.vowel = {"signs": vp, "orthographic_sequence": "".join(x["character"] for x in vp)}
        sy.inherent_vowel = {"status": "overridden", "reason": "dependent_vowel_sign_present"}
    else:
        sy.inherent_vowel = {
            "status": "present_or_contextually_suppressed",
            "reason": "no_dependent_vowel_sign",
        }

    while i < len(cluster) and cluster[i] in SPECIAL:
        role = SPECIAL[cluster[i]]
        if role == "asat":
            sy.coda = {
                "marker": "asat",
                "codepoint": "U+103A",
                "orthographic_function": "contextual",
            }
        elif role in {"dot_below", "visarga"}:
            sy.tone_mark = {"marker": role, "codepoint": f"U+{ord(cluster[i]):04X}"}
        i += 1

    if i != len(cluster):
        sy.analysis.status = "partially_unparsed"
    return sy


def segment_syllables(text: str) -> list[Syllable]:
    return [_parse_cluster(g) for g in segment_graphemes(text) if g]


def _serialize_syllable(syllable: Syllable) -> dict:
    record = asdict(syllable)
    record["status"] = syllable.analysis.status
    return record


def parse_burmese(text: str) -> dict:
    normalized = normalize_burmese(text)
    syllables = segment_syllables(normalized)
    records = [_serialize_syllable(s) for s in syllables]
    ok = all(s.analysis.status == "established" for s in syllables)
    return {
        "input": text,
        "normalized": normalized,
        "graphemes": [s.raw for s in syllables],
        "syllables": records,
        "status": "ok" if ok else "contains_uncertainty_or_invalid_input",
    }
