"""Thin adapter to the canonical ClippyFirst Ukrainian inventory.

This repository does not copy the Ukrainian inventory. To enable this adapter,
provide a local checkout of ClippyFirst/Ukrainian-Phonetic-Inventory containing
inventory.json and data/uk/graphemes.csv.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path


class UkrainianInventoryUnavailable(RuntimeError):
    """Raised when the canonical Ukrainian inventory is not supplied."""


def _load_inventory(root: Path) -> tuple[dict, dict[str, dict]]:
    inventory_path = root / "inventory.json"
    graphemes_path = root / "data" / "uk" / "graphemes.csv"
    if not inventory_path.is_file() or not graphemes_path.is_file():
        raise UkrainianInventoryUnavailable(
            "Canonical Ukrainian inventory checkout is required: "
            "inventory.json + data/uk/graphemes.csv"
        )

    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    with graphemes_path.open("r", encoding="utf-8", newline="") as handle:
        graphemes = {row["ipa_primary"]: row for row in csv.DictReader(handle)}
    return inventory, graphemes


def ipa_to_ukrainian(ipa: str, inventory_root: str | Path | None = None) -> dict:
    """Map exact IPA segments through the canonical Ukrainian target layer.

    This first implementation intentionally performs exact-IPA matching only.
    It does not invent feature-distance results when the canonical target data
    are unavailable or when a source segment has no exact grapheme analogue.
    """
    if not ipa or ipa == "?":
        return {"candidates": [], "status": "insufficient_input"}

    if inventory_root is None:
        return {
            "candidates": [],
            "status": "inventory_unavailable",
            "method": "canonical_inventory_adapter",
        }

    root = Path(inventory_root)
    inventory, graphemes = _load_inventory(root)

    # Use the canonical inventory to verify that a source IPA value is
    # represented in the target phonological space. Then resolve its primary
    # orthographic grapheme from the canonical grapheme table.
    phonemes = {record["ipa"]: record for record in inventory.get("phonemes", [])}
    segments = [segment for segment in ipa.split() if segment]

    outputs: list[str] = []
    trace: list[dict] = []
    for segment in segments:
        phoneme = phonemes.get(segment)
        grapheme = graphemes.get(segment)
        if phoneme is None or grapheme is None:
            outputs.append("?")
            trace.append({"ipa": segment, "status": "not_established"})
            continue
        outputs.append(grapheme["grapheme"])
        trace.append(
            {
                "ipa": segment,
                "grapheme": grapheme["grapheme"],
                "phoneme_id": phoneme["id"],
                "status": grapheme["status"],
            }
        )

    status = "established" if all(item["status"] != "not_established" for item in trace) else "partial"
    return {
        "candidates": [
            {
                "orthography": "".join(outputs),
                "score": None,
                "reason": "exact IPA lookup in canonical Ukrainian inventory",
            }
        ],
        "status": status,
        "method": "canonical_inventory_adapter",
        "inventory_schema_version": inventory.get("schema_version"),
        "trace": trace,
    }
