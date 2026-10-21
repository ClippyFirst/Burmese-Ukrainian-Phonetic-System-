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

def test_phonology_corpus_does_not_mislabel_structural_probes_as_gold():
    path = ROOT / "data" / "burmese" / "phonology_corpus.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert rows, "phonology corpus should retain at least its structural regression probes"
    for row in rows:
        if row["evidence_status"] == "STRUCTURAL_ONLY":
            assert not row["expected_ipa"].strip(), row["case_id"]
            assert not row["expected_ukrainian"].strip(), row["case_id"]


def test_verified_phonology_gold_requires_source_locator_and_ipa():
    corpus_path = ROOT / "data" / "burmese" / "phonology_corpus.csv"
    sources_path = ROOT / "data" / "burmese" / "sources.csv"
    with corpus_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    with sources_path.open(encoding="utf-8", newline="") as handle:
        source_ids = {row["source_id"] for row in csv.DictReader(handle)}

    required_metadata = {
        "ipa_convention", "scope", "analysis_level", "reviewer", "uncertainty_notes"
    }
    assert required_metadata <= rows[0].keys()

    for row in rows:
        if row["evidence_status"] == "GOLD_VERIFIED":
            assert row["source_id"] in source_ids, row["case_id"]
            assert row["source_locator"].strip(), row["case_id"]
            assert "pending" not in row["source_locator"].lower(), row["case_id"]
            assert row["expected_ipa"].strip(), row["case_id"]
            for field in required_metadata:
                assert row[field].strip(), (row["case_id"], field)

def test_external_g2p_benchmark_never_scores_structural_probes_as_gold():
    import runpy

    build_report = runpy.run_path(str(ROOT / "scripts" / "benchmark_g2p.py"))["build_report"]
    row = {
        "case_id": "struct-test",
        "orthography": "ကော်",
        "expected_ipa": "",
        "source_id": "U18",
        "source_locator": "pending",
        "evidence_status": "STRUCTURAL_ONLY",
    }
    report = build_report(
        [row],
        ["kɔ̀"],
        engine="epitran",
        engine_version="test",
        corpus_sha256="fixture-hash",
        corpus_path="fixture.csv",
        known_source_ids={"U18"},
        mapping_sha256=None,
    )
    assert report["eligible_verified_gold_count"] == 0
    assert report["exact_match_count"] is None
    assert report["exact_match_accuracy"] is None
    assert report["records"][0]["exact_match"] is None
    assert report["records"][0]["score_status"] == "NOT_SCORED_NO_VERIFIED_GOLD"


def test_external_g2p_benchmark_scores_only_source_located_gold():
    import runpy

    build_report = runpy.run_path(str(ROOT / "scripts" / "benchmark_g2p.py"))["build_report"]    row = {
        "case_id": "synthetic-gold-gate-test",
        "orthography": "TEST",
        "expected_ipa": "tɛst",
        "source_id": "TEST",
        "source_locator": "synthetic unit-test fixture",
        "evidence_status": "GOLD_VERIFIED",
        "ipa_convention": "broad IPA",
        "scope": "synthetic test fixture",
        "analysis_level": "phonemic",
        "reviewer": "test-suite",
        "uncertainty_notes": "No linguistic claim; synthetic gate test only.",
    }
    report = build_report(
        [row],
        ["tɛst"],
        engine="epitran",
        engine_version="test",
        corpus_sha256="fixture-hash",
        corpus_path="fixture.csv",
        known_source_ids={"TEST"},
        mapping_sha256="map-hash",
    )
    assert report["eligible_verified_gold_count"] == 1
    assert report["exact_match_count"] == 1
    assert report["exact_match_accuracy"] == 1.0
    assert report["records"][0]["score_status"] == "SCORED_EXACT_MATCH"
