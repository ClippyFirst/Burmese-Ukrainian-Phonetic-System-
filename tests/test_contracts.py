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
