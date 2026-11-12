"""Evidence-matrix integrity checks; these tests do not approve runtime rules."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "burmese"


def rows(name):
    with (DATA / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_medial_matrix_is_source_linked_and_runtime_withheld():
    sources = {row["source_id"] for row in rows("sources.csv")}
    matrix = rows("medial_evidence_matrix.csv")
    assert len(matrix) >= 10
    assert len({row["evidence_id"] for row in matrix}) == len(matrix)
    for row in matrix:
        assert row["source_ids"].strip()
        assert row["project_runtime_status"] == "WITHHELD"
        assert row["evidence_level"].strip()
        assert row["source_locator"].strip()
        assert set(row["source_ids"].split(";")) <= sources
    assert any(row["evidence_id"] == "MED-MRAN-001" for row in matrix)


def test_medial_rule_registry_is_evidence_only_and_linked_to_tests():
    sources = {row["source_id"] for row in rows("sources.csv")}
    claims = {row["claim_id"] for row in rows("source_claims.csv")}
    rules = rows("phonological_rules.csv")
    medial_rules = [row for row in rules if row["rule_id"].startswith("MEDIAL_") or row["rule_id"] == "MRAN_LEXICAL_IPA_CANDIDATE"]
    assert len(medial_rules) >= 6
    for rule in medial_rules:
        assert rule["source_id"] in sources
        assert rule["claim_id"] in claims
        assert rule["source_locator"].strip()
        assert rule["status"] in {"analysis_dependent", "context_dependent", "not_established"}
        assert (ROOT / rule["test_reference"]).is_file()


def test_lexical_mran_candidate_does_not_promote_runtime_or_general_rule():
    row = next(row for row in rows("medial_evidence_matrix.csv") if row["evidence_id"] == "MED-MRAN-001")
    assert row["attested_phonological_behavior"] == "/mjàɴ/"
    assert row["evidence_level"] == "lexical_candidate_not_gold"
    assert row["project_runtime_status"] == "WITHHELD"
    rule = next(row for row in rows("phonological_rules.csv") if row["rule_id"] == "MRAN_LEXICAL_IPA_CANDIDATE")
    assert rule["status"] == "not_established"
