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


def test_all_seven_mlc_medial_combinations_are_recorded_as_orthographic_only():
    matrix = rows("medial_evidence_matrix.csv")
    combos = {row["evidence_id"]: row for row in matrix if row["evidence_id"].startswith("MED-COMBO-")}
    assert set(combos) == {f"MED-COMBO-{i:02d}" for i in range(1, 8)}
    for row in combos.values():
        assert row["evidence_level"] == "orthographic_only"
        assert row["project_runtime_status"] == "WITHHELD"
        assert "HLAING2014" in row["source_ids"].split(";")
        assert "not phonological composition" in row["notes"]


def test_google_fst_mran_output_is_cross_system_candidate_not_gold():
    row = next(row for row in rows("medial_evidence_matrix.csv") if row["evidence_id"] == "MED-GOOGLE-MRAN-001")
    assert row["attested_phonological_behavior"] == "m j àɴ"
    assert row["evidence_level"] == "cross_system_candidate_not_gold"
    assert row["project_runtime_status"] == "WITHHELD"
    assert "43084508359" in row["source_locator"]
    rule = next(row for row in rows("phonological_rules.csv") if row["rule_id"] == "GOOGLE_FST_MRAN_RAW_CANDIDATE")
    assert rule["status"] == "not_established"


def test_green_nasal_coda_is_not_flattened_to_independent_velar_nasal():
    row = next(row for row in rows("medial_evidence_matrix.csv") if row["evidence_id"] == "MED-GREEN-N-001")
    assert "nasalization" in row["attested_phonological_behavior"]
    assert "standalone surface [ɴ]" in row["notes"]
    assert row["project_runtime_status"] == "WITHHELD"


def test_external_engine_candidates_for_mran_remain_non_gold_and_withheld():
    matrix = rows("medial_evidence_matrix.csv")
    epitran = next(row for row in matrix if row["evidence_id"] == "MED-EPITRAN-MRAN-001")
    google = next(row for row in matrix if row["evidence_id"] == "MED-GOOGLE-MRAN-001")
    assert epitran["attested_phonological_behavior"] == "məjaɴ"
    assert google["attested_phonological_behavior"] == "m j àɴ"
    assert epitran["project_runtime_status"] == google["project_runtime_status"] == "WITHHELD"
    assert epitran["evidence_level"] == "engine_disagreement_not_gold"
    assert "43325991496" in epitran["source_locator"]


def test_crf_medial_counts_are_diagnostic_not_accuracy():
    row = next(row for row in rows("medial_evidence_matrix.csv") if row["evidence_id"] == "MED-CRF-MEDIAL-SAMPLE-001")
    assert row["attested_phonological_behavior"] == "YA 10/14; RA 17/20; WA 13/15; HA 7/8; overall 84/100"
    assert row["evidence_level"] == "sample_concordance_not_accuracy"
    assert row["project_runtime_status"] == "WITHHELD"
    assert "gold_count=0" in row["source_locator"]


def test_nasal_coda_and_nasal_rhyme_tone_are_registered_separately():
    with (DATA / "phonotactics.csv").open(encoding="utf-8", newline="") as handle:
        rules = {row["rule_id"]: row for row in csv.DictReader(handle)}
    nasal = rules["NASAL_CODA_N"]
    tone = rules["NASAL_RHYME_TONE"]
    assert nasal["source_id"] == tone["source_id"] == "GREEN2002"
    assert nasal["status"] == tone["status"] == "analysis_dependent"
    assert "nasalization" in nasal["notes"]
    assert "not equate automatically" in nasal["notes"]
    assert "checked tone excluded" in tone["notes"]

def test_stedt_written_burmese_medial_segmentation_remains_source_specific():
    matrix = rows("medial_evidence_matrix.csv")
    row = next(row for row in matrix if row["evidence_id"] == "MED-STEDT-WRITTEN-001")
    assert row["evidence_level"] == "historical_written_analysis"
    assert row["project_runtime_status"] == "WITHHELD"
    assert "not a one-to-one Unicode mapping" in row["orthographic_input"]
    assert "/-w-/ belongs to rhyme" in row["attested_phonological_behavior"]
    assert "/-y-/ and /-r-/" in row["attested_phonological_behavior"]
    rule = next(row for row in rows("phonological_rules.csv") if row["rule_id"] == "STEDT_WRITTEN_MEDIAL_SEGMENTATION")
    assert rule["status"] == "analysis_dependent"
    assert rule["source_id"] == "STEDT1996_BURMESE"
    assert rule["claim_id"] == "CLM-STEDT-WRITTEN-MEDIAL-001"
    assert "no modern Unicode medial mapping" in rule["scope"]


def test_stedt_rangoon_medial_distribution_is_not_promoted_to_yangon_runtime():
    row = next(row for row in rows("medial_evidence_matrix.csv") if row["evidence_id"] == "MED-STEDT-RANGOON-001")
    assert row["evidence_level"] == "historical_dialectal_description"
    assert row["project_runtime_status"] == "WITHHELD"
    assert "Burling" in row["attested_phonological_behavior"]
    assert "Roop" in row["attested_phonological_behavior"]
    rule = next(row for row in rows("phonological_rules.csv") if row["rule_id"] == "STEDT_RANGOON_MEDIAL_DISTRIBUTION")
    assert rule["status"] == "analysis_dependent"
    assert rule["source_id"] == "STEDT1996_BURMESE"
    assert "not a current standard Yangon runtime rule" in rule["scope"]

