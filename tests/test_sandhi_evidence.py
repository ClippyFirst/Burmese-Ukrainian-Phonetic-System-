"""Source-faithful sandhi fixtures; these are not IPA gold or runtime rules."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "burmese"


def rows(path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_nishi_sandhi_examples_are_source_linked_and_not_mislabelled_as_ipa():
    sources = {row["source_id"] for row in rows(DATA / "sources.csv")}
    evidence = rows(DATA / "sandhi_evidence.csv")
    schema = json.loads((ROOT / "schemas" / "sandhi_evidence.schema.json").read_text(encoding="utf-8"))

    assert len(evidence) == 7
    assert len({row["case_id"] for row in evidence}) == len(evidence)
    assert {row["process_id"] for row in evidence} == {
        "ATONIC_C1A_C2_VOICING",
        "NONSTOP_TONAL_RHYME_VOICING",
    }
    for row in evidence:
        assert row["source_id"] in sources
        assert row["source_locator"].startswith("Nishi 1998")
        assert row["source_phonemic_output"].startswith("/")
        assert row["source_phonemic_input"].startswith("/")
        assert row["ipa_value"] == ""
        assert row["evidence_status"] == "SOURCE_ATTESTED_NOT_IPA"
        assert "not project IPA" in row["transcription_system"]
        assert row["notes"].strip()
        assert set(row) == set(schema["required"])


def test_nishi_sandhi_examples_do_not_enable_global_runtime_voicing():
    rules = {row["rule_id"]: row for row in rows(DATA / "phonological_rules.csv")}
    first = rules["NISHI98_ATONIC_C1C2_VOICING"]
    second = rules["NISHI98_POST_NONSTOP_RHYME_VOICING"]

    assert first["status"] == "analysis_dependent"
    assert second["status"] == "analysis_dependent"
    assert "do not enable globally" in first["scope"]
    assert "profile-dependent" in second["scope"]
