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


def test_all_94_inventory_keys_match_the_vendored_mya2rom_mlcts_column():
    import re

    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    vendor_path = ROOT / "vendor/mya2rom/romanisations.js"
    vendor_text = vendor_path.read_text(encoding="utf-8")
    match = re.search(r"var vowels = \{([\s\S]*?)\n\}", vendor_text)
    assert match is not None
    vendor_rows = {}
    for key, values_text in re.findall(r'^\s*"([^"]*)"\s*:\s*\[([^\]]+)\]', match.group(1), re.MULTILINE):
        values = re.findall(r'"([^"]*)"', values_text)
        vendor_rows[key] = values

    assert len(vendor_rows) == 95
    assert "" in vendor_rows  # upstream empty-key fallback is not a Myanmar rime key
    assert len(rows) == 94
    for row in rows:
        assert row["source_unit"] in vendor_rows
        assert vendor_rows[row["source_unit"]][1] == row["mlcts"]


def test_mlcts_rime_collision_audit_preserves_distinct_source_units():
    collision_path = ROOT / "data/burmese/romanization_rime_collisions.csv"
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        rimes = {row["source_unit"]: row for row in csv.DictReader(stream)}
    with collision_path.open(encoding="utf-8-sig", newline="") as stream:
        collisions = list(csv.DictReader(stream))

    assert len(collisions) == 25
    assert all(row["audit_status"] == "ORTHOGRAPHIC_COLLISION_REQUIRES_PRIMARY_SOURCE_REVIEW" for row in collisions)
    for collision in collisions:
        source_units = collision["source_units"].split(";")
        assert len(source_units) == int(collision["collision_size"]) == 2
        assert len(set(source_units)) == 2
        assert all(source_unit in rimes for source_unit in source_units)
        assert all(rimes[source_unit]["mlcts"] == collision["mlcts"] for source_unit in source_units)
        assert all(rimes[source_unit]["ukrainian_candidate"] == collision["ukrainian_candidate"] for source_unit in source_units)


def test_auk_myit_special_mapping_is_not_misread_as_an_ordinary_rime():
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        rows = {row["source_unit"]: row for row in csv.DictReader(stream)}
    row = rows["့"]
    assert "auk-myit-induced creaky-tone" in row["context"]
    assert "not an ordinary independent rime" in row["context"]
    assert "do not interpret it as an independent vowel or coda" in row["note"]


LEXICAL_AUDIT_PATH = ROOT / "data/burmese/romanization_rime_collision_lexical_audit.csv"


def test_lexical_collision_audit_keeps_secondary_evidence_separate_from_primary_adjudication():
    collision_path = ROOT / "data/burmese/romanization_rime_collisions.csv"
    with collision_path.open(encoding="utf-8-sig", newline="") as stream:
        collisions = {row["mlcts"]: row for row in csv.DictReader(stream)}
    with LEXICAL_AUDIT_PATH.open(encoding="utf-8-sig", newline="") as stream:
        audit = list(csv.DictReader(stream))

    assert len(audit) == len(collisions) == 25
    assert {row["mlcts"] for row in audit} == set(collisions)
    for row in audit:
        assert row["source_units"] == collisions[row["mlcts"]]["source_units"]
        assert row["acceptance_boundary"]
        assert row["evidence_status"] in {
            "UNADJUDICATED_NO_WORD_LEVEL_EVIDENCE",
            "SECONDARY_SYSTEM_EQUIVALENCE",
            "SECONDARY_SOURCE_CONFLICT",
            "SPECIAL_NONRIME_CONTEXT_DEPENDENT",
        }

    by_mlcts = {row["mlcts"]: row for row in audit}
    assert by_mlcts["am"]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert by_mlcts["am"]["observed_ipa"] == "/kàɴ/"
    assert by_mlcts["am"]["observed_mlcts"] == "kam"
    assert by_mlcts["any"]["evidence_status"] == "SECONDARY_SOURCE_CONFLICT"
    assert "kañ" in by_mlcts["any"]["observed_mlcts"]
    assert "kany" in by_mlcts["any"]["observed_mlcts"]
    assert by_mlcts["u."]["evidence_status"] == "SPECIAL_NONRIME_CONTEXT_DEPENDENT"
    assert by_mlcts["um"]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert by_mlcts["um"]["observed_ipa"] == "/kòʊɴ/"
    assert by_mlcts["um"]["observed_mlcts"] == "kum"
    assert sum(row["evidence_status"] == "UNADJUDICATED_NO_WORD_LEVEL_EVIDENCE" for row in audit) == 21
    assert not any("PRIMARY_CONFIRMED" in row["evidence_status"] for row in audit)

def test_mlcts_source_provenance_does_not_conflate_secondary_sources_or_ala_lc():
    sources_path = ROOT / "data/burmese/sources.csv"
    claims_path = ROOT / "data/burmese/source_claims.csv"
    with sources_path.open(encoding="utf-8-sig", newline="") as stream:
        sources = {row["source_id"]: row for row in csv.DictReader(stream) if row.get("source_id")}
    with claims_path.open(encoding="utf-8-sig", newline="") as stream:
        claims = {row["claim_id"]: row for row in csv.DictReader(stream) if row.get("claim_id")}

    assert "OHNMAR_HTUN_2013" in sources
    assert "ALA_LC_BURMESE_2011" in sources
    assert sources["OHNMAR_HTUN_2013"]["type"] == "doctoral_dissertation"
    assert "not a primary MLCTS specification" in sources["OHNMAR_HTUN_2013"]["scope"]
    assert "ALA-LC" in sources["ALA_LC_BURMESE_2011"]["scope"]
    assert claims["CLM-MLCTS-SECONDARY-PROVENANCE-001"]["source_id"] == "OHNMAR_HTUN_2013"
    assert claims["CLM-ALA-LC-NOT-MLCTS-001"]["source_id"] == "ALA_LC_BURMESE_2011"
    assert "Wikipedia" in claims["CLM-MLCTS-SECONDARY-PROVENANCE-001"]["claim"]
    assert "not the Myanmar Language Commission" in claims["CLM-ALA-LC-NOT-MLCTS-001"]["claim"]
