"""Audit source → claim → phonological rule → test traceability.

This is a provenance/contract test, not a phonological accuracy benchmark.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "burmese"


def _rows(path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_phonological_rules_have_source_scope_claim_and_test_links():
    sources = {row["source_id"]: row for row in _rows(DATA / "sources.csv")}
    claims = {row["claim_id"]: row for row in _rows(DATA / "source_claims.csv")}
    rules = _rows(DATA / "phonological_rules.csv")

    assert rules, "the phonological rule registry must be inspectable"
    assert len({row["rule_id"] for row in rules}) == len(rules), "rule IDs must be unique"

    required = {
        "rule_id", "source_id", "claim_id", "source_locator",
        "scope", "test_reference", "status",
    }
    assert required <= rules[0].keys(), (
        "phonological rule rows must declare source, linked claim, locator, "
        "scope, test reference and evidence status"
    )

    for rule in rules:
        rid = rule["rule_id"]
        assert rid.strip(), "rule ID must not be blank"
        assert rule["source_id"] in sources, (rid, rule["source_id"])
        assert rule["claim_id"] in claims, (rid, rule["claim_id"])
        assert claims[rule["claim_id"]]["source_id"] == rule["source_id"], (
            rid, "claim and rule must cite the same source"
        )
        assert rule["source_locator"].strip(), (rid, "source locator missing")
        assert rule["scope"].strip(), (rid, "rule scope missing")
        assert rule["test_reference"].strip(), (rid, "test reference missing")
        test_path = ROOT / rule["test_reference"]
        assert test_path.is_file(), (rid, f"test file does not exist: {test_path}")
        assert rule["status"].strip().lower() in {
            "established", "well_supported", "analysis_dependent",
            "dialect_dependent", "context_dependent", "uncertain",
            "disputed", "not_established", "unsupported",
        }, (rid, rule["status"])


def test_burmese_tone_vowel_claim_preserves_analysis_scope():
    claim = next(
        row for row in _rows(DATA / "source_claims.csv")
        if row["claim_id"] == "CLM-PHON-001"
    )
    assert claim["source_id"] == "MOONEY2021"
    assert claim["status"] == "ANALYSIS_DEPENDENT"
    assert "tone-independent" in claim["claim"]
    assert "Central Burmese" in claim["scope"]
