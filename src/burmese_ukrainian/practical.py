"""Evidence-backed Burmese → Ukrainian practical correspondence layer.

The machine-readable table in data/burmese/ukrainian_practical.csv is the
single source of segment mappings. This module adds whole-IPA rendering while
retaining tone, phonation and quantity markers in an inspectable trace.
"""
from __future__ import annotations

import csv
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "burmese"
PRACTICAL_TABLE = DATA_DIR / "ukrainian_practical.csv"
RULE_TABLE = DATA_DIR / "practical_rules.csv"


@dataclass(frozen=True)
class PracticalCandidate:
    text: str
    status: str
    rule_ids: tuple[str, ...]
    reason: str
    evidence: tuple[str, ...] = ()


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _load_rules() -> dict[str, list[str]]:
    rules: dict[str, list[str]] = {}
    for row in _read_rows(RULE_TABLE):
        rules.setdefault(row["input"], []).append(row["rule_id"])
    return rules


def _load_candidates() -> dict[str, list[dict[str, str]]]:
    rows = _read_rows(PRACTICAL_TABLE)
    return_rows: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        return_rows.setdefault(row["burmese_ipa"], []).append(row)
    return return_rows


def rank_ukrainian_candidates(ipa: str) -> list[PracticalCandidate]:
    """Return deterministic candidates from the canonical project table."""
    if not ipa:
        return []

    rows = _load_candidates().get(ipa)
    if not rows:
        # The table contains a grouped documentary label θ~ð. Do not silently
        # split an unresolved analysis into unsupported segment claims.
        return [
            PracticalCandidate(
                text="?",
                status="not_established",
                rule_ids=("UA-BUR-UNMAPPED",),
                reason="No exact project correspondence is established for this IPA value.",
            )
        ]

    rules = _load_rules()
    candidates: list[PracticalCandidate] = []
    for row in rows:
        rule_ids = tuple(rules.get(row["burmese_ipa"], ()))
        candidates.append(
            PracticalCandidate(
                text=row["ukrainian_candidate"],
                status=row["status"].lower(),
                rule_ids=rule_ids,
                reason=row["policy"],
                evidence=tuple(x for x in row["evidence"].split(";") if x),
            )
        )
    return candidates


def practical_from_ipa(ipa: str) -> dict:
    """Explain one exact IPA segment; use transcribe_ipa for sequences."""
    candidates = rank_ukrainian_candidates(ipa)
    return {
        "ipa": ipa,
        "candidates": [
            {
                "text": c.text,
                "status": c.status,
                "rule_ids": c.rule_ids,
                "reason": c.reason,
                "evidence": c.evidence,
            }
            for c in candidates
        ],
        "status": candidates[0].status if candidates else "insufficient_input",
    }


def _segment_keys() -> tuple[str, ...]:
    keys = (key for key in _load_candidates() if key and key != "all")
    return tuple(sorted((unicodedata.normalize("NFD", key) for key in keys),
                        key=len, reverse=True))


def _is_tone_mark(char: str) -> bool:
    name = unicodedata.name(char, "")
    return any(part in name for part in ("ACCENT", "TONE", "MACRON", "CARON"))


def _tokenize_syllable(chunk: str, keys: tuple[str, ...], prosody: list[dict]) -> tuple[list[str] | None, str | None]:
    tokens: list[str] = []
    index = 0
    while index < len(chunk):
        char = chunk[index]
        if char in {"ː", "ˑ"}:
            prosody.append({
                "kind": "length",
                "mark": char,
                "value": "long" if char == "ː" else "half-long",
            })
            index += 1
            continue
        if char in {"ˈ", "ˌ"}:
            prosody.append({"kind": "stress", "mark": char})
            index += 1
            continue
        if unicodedata.combining(char):
            # A tie bar is part of an affricate token. If no explicit
            # affricate mapping consumed it, fail closed instead of flattening
            # the tied articulation into a plain consonant sequence.
            if char in {"\u0361", "\u035c"}:
                return None, chunk[index:]
            prosody.append({
                "kind": "tone" if _is_tone_mark(char) else "phonation_or_other_diacritic",
                "mark": char,
                "unicode_name": unicodedata.name(char, "UNKNOWN"),
            })
            index += 1
            continue

        segment = next((key for key in keys if chunk.startswith(key, index)), None)
        if segment is None:
            return None, chunk[index:]
        tokens.append(segment)
        index += len(segment)
    return tokens, None


_INITIAL_J_VOWELS = {
    "a": "я",
    "e": "є",
    "ɛ": "є",
    "i": "ї",
    "o": "йо",
    "ɔ": "йо",
    "u": "ю",
    "ɯ": "йи",
}


def transcribe_ipa(ipa: str) -> dict:
    """Render a complete Burmese IPA string as a practical Ukrainian candidate.

    Spaces and explicit syllable dots reset syllable-initial /j/ handling.
    Tone/phonation diacritics and vowel length are omitted from ordinary
    practical spelling but returned in the prosody trace. An unknown segment
    withholds the complete Ukrainian string.
    """
    if not ipa or not ipa.strip():
        return {
            "ipa": ipa,
            "text": None,
            "status": "insufficient_input",
            "segments": [],
            "prosody": [],
            "unsupported": None,
        }

    source = ipa.strip()
    if len(source) > 1 and ((source[0], source[-1]) in {("/", "/"), ("[", "]")}):
        source = source[1:-1]
    source = unicodedata.normalize("NFD", source)
    keys = _segment_keys()
    prosody: list[dict] = []
    trace: list[dict] = []
    output: list[str] = []

    for part in re.split(r"(\s+|[.·])", source):
        if not part:
            continue
        if part.isspace():
            output.append(part)
            continue
        if part in {".", "·"}:
            prosody.append({"kind": "syllable_boundary", "mark": part})
            continue

        tokens, unsupported = _tokenize_syllable(part, keys, prosody)
        if tokens is None:
            return {
                "ipa": ipa,
                "text": None,
                "status": "not_established",
                "segments": trace,
                "prosody": prosody,
                "unsupported": unsupported,
            }

        token_index = 0
        if len(tokens) > 1 and tokens[0] == "j" and tokens[1] in _INITIAL_J_VOWELS:
            vowel = tokens[1]
            text = _INITIAL_J_VOWELS[vowel]
            trace.append({
                "ipa": f"j+{vowel}",
                "text": text,
                "status": "proposed",
                "rule_ids": ("UA-BUR-J-INITIAL",),
                "reason": "Syllable-initial /j/ plus vowel uses Ukrainian yotated orthography.",
                "evidence": ("UA_ORTH_2026",),
            })
            output.append(text)
            token_index = 2

        while token_index < len(tokens):
            segment = tokens[token_index]
            candidates = rank_ukrainian_candidates(segment)
            if not candidates or candidates[0].status == "not_established":
                return {
                    "ipa": ipa,
                    "text": None,
                    "status": "not_established",
                    "segments": trace,
                    "prosody": prosody,
                    "unsupported": segment,
                }
            candidate = candidates[0]
            # The glyph ∅ is an explanatory zero marker, not a character to
            # print in practical Ukrainian spelling.
            rendered = "" if segment == "ʔ" and candidate.text == "∅" else candidate.text
            trace.append({
                "ipa": segment,
                "text": rendered,
                "notation": candidate.text if rendered == "" else None,
                "status": candidate.status,
                "rule_ids": candidate.rule_ids,
                "reason": candidate.reason,
                "evidence": candidate.evidence,
            })
            output.append(rendered)
            token_index += 1

    statuses = {item["status"] for item in trace}
    status = "analysis_dependent" if "analysis_dependent" in statuses else "proposed"
    return {
        "ipa": ipa,
        "text": "".join(output),
        "status": status,
        "segments": trace,
        "prosody": prosody,
        "unsupported": None,
    }
