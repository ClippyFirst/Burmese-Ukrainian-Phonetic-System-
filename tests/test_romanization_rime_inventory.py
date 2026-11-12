from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data/burmese/romanization_rimes_inventory.csv"
SOURCE = "https://github.com/myanmaropenwordnet/mya2rom"


def test_vendor_mlcts_rime_inventory_is_explicit_and_provenanced():
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 94
    assert len({row["source_unit"] for row in rows}) == len(rows)
    assert all(row["mlcts"] for row in rows)
    assert all(row["ukrainian_status"] == "PROPOSED" for row in rows)
    assert all(row["ukrainian_candidate"] for row in rows)
    assert all(row["romanization_evidence_status"] == "EVIDENCE_LIMITED" for row in rows)
    assert all(row["source_url"] == SOURCE for row in rows)
    assert all("romanisations.js" in row["source_locator"] for row in rows)
    assert all("vendored Mya2Rom inventory" in row["note"] for row in rows)



UKRAINIAN_UNITS = {"ng": "нг", "ny": "нь", "ai": "ай", "au": "ау", "ui": "уй", ":": "ː", ".": "·", "'": "ʼ", "a": "а", "c": "ц", "e": "е", "g": "ґ", "i": "і", "k": "к", "m": "м", "n": "н", "p": "п", "t": "т", "u": "у", "w": "в", "y": "й"}


def render_mlcts(value: str) -> str:
    result = ""
    index = 0
    while index < len(value):
        digraph = next((unit for unit in ("ng", "ny", "ai", "au", "ui") if value.startswith(unit, index)), None)
        if digraph:
            result += UKRAINIAN_UNITS[digraph]
            index += len(digraph)
        else:
            result += UKRAINIAN_UNITS[value[index]]
            index += 1
    return result


def test_all_94_vendor_rimes_have_complete_deterministic_ukrainian_renderings():
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    for row in rows:
        assert row["ukrainian_candidate"] == render_mlcts(row["mlcts"])
        assert row["ukrainian_status"] == "PROPOSED"
        assert row["romanization_evidence_status"] == "EVIDENCE_LIMITED"
