import csv
from pathlib import Path

from burmese_ukrainian.ukrainian import ipa_to_ukrainian


ROOT = Path(__file__).resolve().parents[1]


def test_phonotactics_csv_is_rectangular():
    path = ROOT / "data" / "burmese" / "phonotactics.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    width = len(rows[0])
    assert width == 5
    assert all(len(row) == width for row in rows[1:])


def test_practical_rules_are_exposed_by_the_data_layer():
    from burmese_ukrainian.practical import practical_from_ipa

    result = practical_from_ipa("kʰ")
    assert result["candidates"][0]["rule_ids"] == ("UA-BUR-ASP-K",)
    assert "RU_EPSHTEIN_1959" in result["candidates"][0]["evidence"]


def test_ukrainian_adapter_does_not_fallback_to_hidden_inventory():
    result = ipa_to_ukrainian("i")
    assert result["status"] == "inventory_unavailable"


def test_ukrainian_adapter_consumes_external_inventory(tmp_path):
    import json

    (tmp_path / "data" / "uk").mkdir(parents=True)
    (tmp_path / "inventory.json").write_text(
        json.dumps({"schema_version": "test", "phonemes": [{"id": "UA-V-001", "ipa": "i"}]}),
        encoding="utf-8",
    )
    (tmp_path / "data" / "uk" / "graphemes.csv").write_text(
        "grapheme,ipa_primary,type,phonological_function,context_sensitive,status,notes,source_id\n"
        "і,i,letter,vowel,no,core,,TEST\n",
        encoding="utf-8",
    )
    result = ipa_to_ukrainian("i", inventory_root=tmp_path)
    assert result["status"] == "established"
    assert result["candidates"][0]["orthography"] == "і"


def test_practical_rule_keys_match_practical_table():
    import csv

    def keys(path, column):
        with path.open(encoding="utf-8", newline="") as handle:
            return {row[column] for row in csv.DictReader(handle)}

    practical = ROOT / "data" / "burmese" / "ukrainian_practical.csv"
    rules = ROOT / "data" / "burmese" / "practical_rules.csv"
    assert keys(rules, "input") <= keys(practical, "burmese_ipa")
