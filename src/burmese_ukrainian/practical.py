"""Evidence-backed Burmese → Ukrainian practical correspondence layer.

The active correspondence table lives in data/burmese/ukrainian_practical.csv.
Python does not maintain a second hidden mapping table.
"""

from __future__ import annotations

import csv
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
        # The table contains a few grouped documentary labels such as
        # θ~ð. Do not silently split such analyses into unsupported claims.
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
