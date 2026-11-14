"""Crosswalk integrity checks for the 25 MLCTS rime collision groups.

These checks validate data alignment and evidence boundaries, not phonetic truth.
"""
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "burmese"


def read_rows(name):
    with (DATA / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def test_all_three_rime_crosswalks_cover_the_same_25_collision_groups():
    collisions = read_rows("romanization_rime_collisions.csv")
    mlcts2 = read_rows("romanization_rime_mlcts2_crosswalk.csv")
    r12a = read_rows("romanization_rime_r12a_secondary_phonology_crosswalk.csv")
    lexical = read_rows("romanization_rime_collision_lexical_audit.csv")

    assert len(collisions) == len(mlcts2) == len(r12a) == len(lexical) == 25
    expected = {row["mlcts"]: row["source_units"] for row in collisions}
    for table in (mlcts2, r12a, lexical):
        assert {row["mlcts"] for row in table} == set(expected)
        assert len({row["mlcts"] for row in table}) == 25
        for row in table:
            assert row["source_units"] == expected[row["mlcts"]]

    lexical_by_key = {row["mlcts"]: row for row in lexical}
    mlcts2_by_key = {row["mlcts"]: row for row in mlcts2}
    for key, row in lexical_by_key.items():
        assert mlcts2_by_key[key]["lexical_audit_status"] == row["evidence_status"]


def test_mlcts2_crosswalk_keeps_each_vendor_output_aligned_to_its_source_unit():
    rows = read_rows("romanization_rime_mlcts2_crosswalk.csv")
    allowed = {
        "SAME_MLCTS2_OUTPUT",
        "DISTINCT_MLCTS2_OUTPUT",
        "SPECIAL_CONTEXT_FALLBACK",
    }
    for row in rows:
        source_units = row["source_units"].split(";")
        mlcts2_values = row["mlcts2_values"].split(";")
        ipa_values = row["ipa_values"].split(";")
        array_lengths = row["array_lengths"].split(";")
        assert len(source_units) == len(mlcts2_values) == len(ipa_values) == len(array_lengths) == 2
        assert all(value.isdigit() for value in array_lengths)
        assert row["mlcts2_relation"] in allowed
        assert row["lexical_audit_status"] in {
            "UNADJUDICATED_NO_WORD_LEVEL_EVIDENCE",
            "SECONDARY_SYSTEM_EQUIVALENCE",
            "SECONDARY_SOURCE_CONFLICT",
            "SECONDARY_SOURCE_DISTINCTION",
            "SECONDARY_ONE_SIDE_ONLY",
            "SPECIAL_NONRIME_CONTEXT_DEPENDENT",
        }
        assert row["interpretation_boundary"].strip()
        assert "not a primary mlc" in row["interpretation_boundary"].lower()
    counts = Counter(row["mlcts2_relation"] for row in rows)
    assert counts == {
        "SAME_MLCTS2_OUTPUT": 20,
        "DISTINCT_MLCTS2_OUTPUT": 4,
        "SPECIAL_CONTEXT_FALLBACK": 1,
    }


def test_r12a_crosswalk_distinguishes_equal_distinct_partial_and_absent_rows():
    rows = read_rows("romanization_rime_r12a_secondary_phonology_crosswalk.csv")
    allowed = {
        "SAME_IN_R12A_TABLE",
        "DISTINCT_IN_R12A_TABLE",
        "PARTIAL_COVERAGE",
        "NOT_LISTED_IN_R12A_TABLE",
        "SPECIAL_NONRIME_CONTEXT_DEPENDENT",
    }
    for row in rows:
        assert row["comparison_status"] in allowed
        assert row["r12a_table_locator"].strip()
        assert row["interpretation"].strip()
        assert row["evidence_boundary"].strip()
        assert "Secondary" in row["evidence_boundary"]
        assert "not an MLC primary table" in row["evidence_boundary"]
        values = row["r12a_ipa_values"].split(";")
        assert len(values) == 2
        if row["comparison_status"] == "NOT_LISTED_IN_R12A_TABLE":
            assert values == ["", ""]
        if row["comparison_status"] == "PARTIAL_COVERAGE":
            assert "NOT_COVERED" in values
    assert Counter(row["comparison_status"] for row in rows) == {
        "SAME_IN_R12A_TABLE": 18,
        "DISTINCT_IN_R12A_TABLE": 3,
        "PARTIAL_COVERAGE": 2,
        "NOT_LISTED_IN_R12A_TABLE": 1,
        "SPECIAL_NONRIME_CONTEXT_DEPENDENT": 1,
    }


def test_lexical_audit_does_not_upgrade_secondary_crosswalks_to_primary_adjudication():
    rows = read_rows("romanization_rime_collision_lexical_audit.csv")
    counts = Counter(row["evidence_status"] for row in rows)
    assert counts == {
        "SECONDARY_SYSTEM_EQUIVALENCE": 12,
        "SECONDARY_SOURCE_CONFLICT": 1,
        "SECONDARY_ONE_SIDE_ONLY": 8,
        "SECONDARY_SOURCE_DISTINCTION": 3,
        "SPECIAL_NONRIME_CONTEXT_DEPENDENT": 1,
    }
    for row in rows:
        assert row["acceptance_boundary"].strip()
        assert "not primary" in row["acceptance_boundary"].lower()
        if row["evidence_status"] == "UNADJUDICATED_NO_WORD_LEVEL_EVIDENCE":
            assert not row["observed_ipa"]
            assert not row["observed_mlcts"]
        assert "PRIMARY_CONFIRMED" not in row["evidence_status"]


def test_secondary_word_level_evidence_statuses_keep_their_limits_explicit():
    rows = {row["mlcts"]: row for row in read_rows("romanization_rime_collision_lexical_audit.csv")}
    assert rows["a"]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert all(value in rows["a"]["observed_mlcts"] for value in ["a.wa","a.ca"])
    assert rows["a:"]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert all(value in rows["a:"]["observed_mlcts"] for value in ["hka:","ka:"])
    assert rows["au"]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert all(value in rows["au"]["observed_mlcts"] for value in ["pau","krau"])
    assert rows["au."]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert "pau." in rows["au."]["observed_mlcts"] and "waphrau." in rows["au."]["observed_mlcts"]
    assert "/pɔ̰/" in rows["au."]["observed_ipa"] and "/waʔʃɔ̰/" in rows["au."]["observed_ipa"]
    assert rows["am."]["evidence_status"] == "SECONDARY_SOURCE_DISTINCTION"
    assert "cim." in rows["am."]["observed_mlcts"] and "kram." in rows["am."]["observed_mlcts"]
    assert "/sḛɪɴ/" in rows["am."]["observed_ipa"] and "/t͡ɕa̰ɴ/" in rows["am."]["observed_ipa"]
    assert rows["am:"]["evidence_status"] == "SECONDARY_ONE_SIDE_ONLY"
    assert "lam:" in rows["am:"]["observed_mlcts"] and "/láɴ/" in rows["am:"]["observed_ipa"]
    assert rows["um."]["evidence_status"] == "SECONDARY_ONE_SIDE_ONLY"
    assert "um." in rows["um."]["observed_mlcts"] and "/ʔo̰ʊɴ/" in rows["um."]["observed_ipa"]
    assert "not a mow candidate" in rows["um."]["acceptance_boundary"].lower()
    assert rows["um:"]["evidence_status"] == "SECONDARY_ONE_SIDE_ONLY"
    assert "hna.lum:" in rows["um:"]["observed_mlcts"] and "/n̥əlóʊɴ/" in rows["um:"]["observed_ipa"]
    assert rows["un"]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert "gun" in rows["un"]["observed_mlcts"] and "kun" in rows["un"]["observed_mlcts"]
    assert "/ɡòʊɴ/" in rows["un"]["observed_ipa"] and "/kòʊɴ/" in rows["un"]["observed_ipa"]
    assert rows["au:"]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert "pau:" in rows["au:"]["observed_mlcts"] and "kyau:" in rows["au:"]["observed_mlcts"]
    assert "/pɔ́/" in rows["au:"]["observed_ipa"] and "/t͡ɕɔ́/" in rows["au:"]["observed_ipa"]
    assert rows["im"]["evidence_status"] == "SECONDARY_ONE_SIDE_ONLY"
    assert "im" in rows["im"]["observed_mlcts"] and "/ʔèɪɴ/" in rows["im"]["observed_ipa"]
    assert rows["im:"]["evidence_status"] == "SECONDARY_ONE_SIDE_ONLY"
    assert "tim:" in rows["im:"]["observed_mlcts"] and "/təθwèmətéɪɴ/" in rows["im:"]["observed_ipa"]
    assert "compound-level" in rows["im:"]["interpretation"]
    assert rows["im."]["evidence_status"] == "SECONDARY_ONE_SIDE_ONLY"
    assert "cim." in rows["im."]["observed_mlcts"] and "/sḛɪɴ/" in rows["im."]["observed_ipa"]
    assert rows["aung."]["evidence_status"] == "SECONDARY_ONE_SIDE_ONLY"
    assert "caung." in rows["aung."]["observed_mlcts"] and "/sa̰ʊɴ/" in rows["aung."]["observed_ipa"]
    assert "second source-unit side" in rows["aung."]["interpretation"]
    assert rows["auk"]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert "pauk" in rows["auk"]["observed_mlcts"] and "kyauk" in rows["auk"]["observed_mlcts"]
    assert "/paʊʔ/" in rows["auk"]["observed_ipa"] and "/t͡ɕaʊʔ/" in rows["auk"]["observed_ipa"]
    assert rows["aung:"]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert "paung:" in rows["aung:"]["observed_mlcts"] and "kyaung:" in rows["aung:"]["observed_mlcts"]
    assert "/páʊɴ/" in rows["aung:"]["observed_ipa"] and "/t͡ɕáʊɴ/" in rows["aung:"]["observed_ipa"]
    assert rows["aung"]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert "paung" in rows["aung"]["observed_mlcts"] and "taung" in rows["aung"]["observed_mlcts"]
    assert "/pàʊɴ/" in rows["aung"]["observed_ipa"] and "/tàʊɴ/" in rows["aung"]["observed_ipa"]
    assert rows["any."]["evidence_status"] == "SECONDARY_SOURCE_DISTINCTION"
    assert "cany." in rows["any."]["observed_mlcts"] and "krany." in rows["any."]["observed_mlcts"]
    assert "/sɪ̰ɴ/" in rows["any."]["observed_ipa"] and "/t͡ɕḭ/" in rows["any."]["observed_ipa"]
    assert rows["any:"]["evidence_status"] == "SECONDARY_SOURCE_DISTINCTION"
    assert "sense-dependent" in rows["any:"]["observed_ipa"]
    assert rows["ui"]["evidence_status"] == "SECONDARY_ONE_SIDE_ONLY"
    assert "only" in rows["ui"]["acceptance_boundary"].lower()
    assert rows["any"]["evidence_status"] == "SECONDARY_SOURCE_CONFLICT"
    assert all("no runtime" in rows[key]["acceptance_boundary"].lower() for key in ("auk", "aung", "aung:", "aung.", "any", "any:", "any.", "ui", "um:", "un", "au:", "au.", "im", "im:", "im.", "am:", "am.", "um."))


def test_mow_suffix_match_does_not_promote_overlapping_composite_vowel_to_a_dot_rime():
    """A raw code-point suffix overlap is not a Burmese syllable/rime analysis."""
    matches = read_rows("mow_rime_orthographic_matches.csv")
    a_dot = [row for row in matches if row["mlcts"] == "a." and row["source_unit"] == "ာ့"]
    assert [row["lemma"] for row in a_dot] == ["ဝပ်ရှော့"]
    lexical = {row["mlcts"]: row for row in read_rows("romanization_rime_collision_lexical_audit.csv")}
    assert lexical["a."]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert lexical["a."]["observed_ipa"] == "/ŋa̰/; /ta̰/"
    assert lexical["a."]["observed_mlcts"] == "nga.; ta.ta"
    assert lexical["au."]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert "pau." in lexical["au."]["observed_mlcts"] and "waphrau." in lexical["au."]["observed_mlcts"]
    assert "not a mow suffix-match candidate" in lexical["au."]["interpretation"].lower()


def test_a_dot_phonetic_literature_does_not_supply_orthographic_mapping():
    """General /a/~closed-vowel descriptions cannot adjudicate MLCTS a. spellings."""
    rows = {row["mlcts"]: row for row in read_rows("romanization_rime_collision_lexical_audit.csv")}
    assert rows["a."]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert "not a controlled minimal pair" in rows["a."]["acceptance_boundary"].lower()
    assert "both source-unit sides" in rows["a."]["interpretation"].lower()
    assert "mooney" in rows["a."]["interpretation"].lower()
    assert "watkins" in rows["a."]["interpretation"].lower()
    assert "both source-unit sides" in rows["a."]["interpretation"].lower()
