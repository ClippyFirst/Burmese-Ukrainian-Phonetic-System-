"""Gold-corpus eligibility is stricter than a status label alone."""
import csv
from pathlib import Path

from scripts.benchmark_g2p import build_report


ROOT = Path(__file__).resolve().parents[1]


def _report(rows, outputs, known_source_ids):
    return build_report(
        rows,
        outputs,
        engine="test-fixture",
        engine_version="0",
        corpus_sha256="fixture-sha256",
        corpus_path="fixture.csv",
        known_source_ids=known_source_ids,
        mapping_sha256=None,
    )


def test_current_structural_probes_are_never_scored_as_gold():
    with (ROOT / "data/burmese/phonology_corpus.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    report = _report(rows, ["dummy"] * len(rows), {"U18", "GREEN2002"})

    assert len(rows) == 6
    assert report["eligible_verified_gold_count"] == 0
    assert report["exact_match_count"] is None
    assert report["exact_match_accuracy"] is None
    assert all(r["score_status"] == "NOT_SCORED_NO_VERIFIED_GOLD" for r in report["records"])


def test_gold_status_without_adjudication_metadata_is_not_scoreable():
    row = {
        "case_id": "fixture-001",
        "orthography": "TEST",
        "expected_ipa": "tɛst",
        "source_id": "SRC1",
        "source_locator": "p. 10, example 3",
        "evidence_status": "GOLD_VERIFIED",
        "ipa_convention": "broad IPA",
        "scope": "specified variety",
        "analysis_level": "phonemic",
        "reviewer": "reviewer-1",
        "uncertainty_notes": "",
    }
    report = _report([row], ["tɛst"], {"SRC1"})

    assert report["eligible_verified_gold_count"] == 0
    assert report["records"][0]["score_status"] == "NOT_SCORED_NO_VERIFIED_GOLD"


def test_fully_documented_gold_row_can_be_scored():
    row = {
        "case_id": "fixture-002",
        "orthography": "TEST",
        "expected_ipa": "tɛst",
        "source_id": "SRC1",
        "source_locator": "p. 10, example 3",
        "evidence_status": "GOLD_VERIFIED",
        "ipa_convention": "broad IPA",
        "scope": "specified variety",
        "analysis_level": "phonemic",
        "reviewer": "reviewer-1",
        "uncertainty_notes": "No unresolved alternative for this test fixture.",
    }
    report = _report([row], ["tɛst"], {"SRC1"})

    assert report["eligible_verified_gold_count"] == 1
    assert report["exact_match_count"] == 1
    assert report["exact_match_accuracy"] == 1.0
    assert report["records"][0]["score_status"] == "SCORED_EXACT_MATCH"
