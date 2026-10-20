import json
from pathlib import Path

from burmese_ukrainian import parse_burmese


FIXTURE_PATH = Path(__file__).parent / "fixtures" / "shared_unicode_contract.json"


def test_shared_unicode_contract_fixtures():
    fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    assert fixture["schema_version"] == 1

    for case in fixture["cases"]:
        expected = case["python"]
        result = parse_burmese(case["input"])
        assert result["status"] == expected["top_level_status"], case["id"]
        assert [f"U+{ord(ch):04X}" for ch in case["input"]] == case["codepoints"], case["id"]
        assert result["syllables"][0]["status"] == expected["syllable_status"], case["id"]
        if expected["graphemes_preserved"]:
            assert result["graphemes"] == [case["input"]], case["id"]
