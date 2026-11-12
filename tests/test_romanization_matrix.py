import csv
from pathlib import Path

EXPECTED_MLCTS_ONSETS = {
    "က": "k", "ခ": "hk", "ဂ": "g", "ဃ": "gh", "င": "ng",
    "စ": "c", "ဆ": "hc", "ဇ": "j", "ဈ": "jh", "ဉ": "ny",
    "ည": "ny", "ဋ": "t", "ဌ": "ht", "ဍ": "d", "ဎ": "dh",
    "ဏ": "n", "တ": "t", "ထ": "ht", "ဒ": "d", "ဓ": "dh",
    "န": "n", "ပ": "p", "ဖ": "hp", "ဗ": "b", "ဘ": "bh",
    "မ": "m", "ယ": "y", "ရ": "r", "လ": "l", "ဝ": "w",
    "သ": "s", "ဿ": "s", "ဟ": "h", "ဠ": "l", "အ": "",
}


def test_mlcts_onset_crosswalk_covers_every_vendored_mlcts_onset():
    path = Path(__file__).parents[1] / "data" / "burmese" / "romanization_ukrainian.csv"
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))

    onset_rows = [row for row in rows if row["unit_type"] == "onset"]
    assert {row["source_unit"] for row in onset_rows} == set(EXPECTED_MLCTS_ONSETS)
    assert len(onset_rows) == len(EXPECTED_MLCTS_ONSETS)
    assert {row["source_unit"]: row["mlcts"] for row in onset_rows} == EXPECTED_MLCTS_ONSETS


def test_mlcts_crosswalk_does_not_invent_unadjudicated_ukrainian_values():
    path = Path(__file__).parents[1] / "data" / "burmese" / "romanization_ukrainian.csv"
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))

    allowed = {"PROPOSED", "ANALYSIS_DEPENDENT", "EVIDENCE_LIMITED"}
    assert rows
    assert all(row["ukrainian_status"] in allowed for row in rows)
    assert all(row["source_url"].startswith("https://") for row in rows)
    assert all(row["source_locator"].strip() for row in rows)
    assert len({(row["source_unit"], row["unit_type"]) for row in rows}) == len(rows)
    assert all(row["ukrainian_candidate"] for row in rows if row["ukrainian_status"] == "PROPOSED")
    assert all(row["romanization_evidence_status"] == "EVIDENCE_LIMITED" for row in rows)



def test_all_mlcts_onsets_have_explicit_ukrainian_candidates_including_zero_onset():
    path = Path(__file__).parents[1] / "data" / "burmese" / "romanization_ukrainian.csv"
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    expected = {
        "k": "к", "hk": "к'", "g": "ґ", "gh": "ґ'", "ng": "нг",
        "c": "ц", "hc": "ц'", "j": "дж", "jh": "дж'", "ny": "нь",
        "t": "т", "ht": "т'", "d": "д", "dh": "д'", "n": "н",
        "p": "п", "hp": "п'", "b": "б", "bh": "б'", "m": "м",
        "y": "й", "r": "р", "l": "л", "w": "в", "s": "с", "h": "г", "": "∅",
    }
    actual = {row["mlcts"]: row["ukrainian_candidate"] for row in rows}
    assert actual == expected
