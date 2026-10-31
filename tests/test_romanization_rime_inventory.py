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
    assert all(row["ukrainian_status"] == "EVIDENCE_LIMITED" for row in rows)
    assert all(not row["ukrainian_candidate"] for row in rows)
    assert all(row["source_url"] == SOURCE for row in rows)
    assert all("romanisations.js" in row["source_locator"] for row in rows)
    assert all("not represented as a directly inspected" in row["note"] for row in rows)
