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


def test_misplaced_virama_guard_is_grounded_as_orthographic_not_phonetic_evidence():
    claims = {row["claim_id"]: row for row in _rows(DATA / "source_claims.csv")}
    rules = {row["rule_id"]: row for row in _rows(DATA / "phonological_rules.csv")}
    claim = claims["CLM-ORTH-001"]
    rule = rules["MALFORMED_VIRAMA_WITHHOLD_IPA"]

    assert claim["source_id"] == "U18"
    assert claim["evidence_type"] == "orthographic_structure"
    assert claim["status"] == "ESTABLISHED"
    assert "U+1039" in claim["claim"]
    assert rule["source_id"] == claim["source_id"]
    assert rule["claim_id"] == claim["claim_id"]
    assert rule["status"] == "established"
    assert rule["test_reference"] == "tests/test_malformed_ipa_withholding.py"
    assert "not a pronunciation rule" in rule["scope"]

def test_burmese_wiktionary_ipa_source_is_sparse_and_rights_gated():
    sources = {row["source_id"]: row for row in _rows(DATA / "sources.csv")}
    claims = {row["claim_id"]: row for row in _rows(DATA / "source_claims.csv")}
    source = sources["MYWIKTIONARY2026"]
    assert "113 IPA values (0.51%)" in source["scope"]
    assert "MLCTS coverage is not IPA coverage" in source["scope"]
    assert "CC BY 4.0" in source["scope"]
    assert "rights_status=CONFLICT/UNKNOWN" in source["scope"]
    rights_source = sources["MYWIKTIONARY2026"]
    policy_source = sources["MYWIKTIONARYPOLICY2024"]
    assert "CC BY 4.0" in rights_source["scope"]
    assert "CC BY-SA 3.0 Unported" in policy_source["scope"]
    assert "GFDL" in policy_source["scope"]
    card_claim = claims["CLM-WIKT-LICENSE-001"]
    policy_claim = claims["CLM-WIKT-UPSTREAM-LICENSE-001"]
    assert card_claim["source_id"] == "MYWIKTIONARY2026"
    assert card_claim["status"] == "DOCUMENTARY"
    assert "CC BY 4.0" in card_claim["claim"]
    assert policy_claim["source_id"] == "MYWIKTIONARYPOLICY2024"
    assert policy_claim["status"] == "DOCUMENTARY"
    assert "CC BY-SA 3.0 Unported" in policy_claim["claim"]
    assert "GFDL" in policy_claim["claim"]


def test_legacy_non_text_corpus_records_are_excluded_from_active_scope():
    sources = {row["source_id"]: row for row in _rows(DATA / "sources.csv")}
    claims = {row["claim_id"]: row for row in _rows(DATA / "source_claims.csv")}

    myg2p = sources["MYG2P2026"]
    assert "54b5c76bb5a87fdbaaeddc1892e6ebd8f97ee225" in myg2p["scope"]
    assert "five tab-separated fields" in myg2p["scope"]
    assert "0b2735f9a6f7fe28ae94c4baaf323d1db3015c3b" in myg2p["scope"]
    assert "IPA" in myg2p["scope"]
    assert "CC BY-NC-SA 4.0" in myg2p["scope"]
    assert "not an independently adjudicated project gold" in myg2p["scope"]

    for source_id in ("OPENSLR80", "MON2019"):
        scope = sources[source_id]["scope"]
        assert "Historical metadata only" in scope
        assert "excluded from active text-only research" in scope
        assert "not an active source candidate" in scope
        assert "no audio is to be acquired, processed, annotated" in scope.lower()

    assert claims["CLM-MYG2P-001"]["source_id"] == "MYG2P2026"
    assert claims["CLM-MYG2P-001"]["status"] == "DOCUMENTARY"
    assert claims["CLM-OPENSLR80-001"]["source_id"] == "OPENSLR80"
    assert claims["CLM-OPENSLR80-001"]["status"] == "DOCUMENTARY"

def test_nishi_1998_voicing_sandhi_remains_contextual_and_profile_scoped():
    sources = {row["source_id"]: row for row in _rows(DATA / "sources.csv")}
    claims = {row["claim_id"]: row for row in _rows(DATA / "source_claims.csv")}
    rules = {row["rule_id"]: row for row in _rows(DATA / "phonological_rules.csv")}

    source = sources["NISHI1998_VOICING_RULES"]
    assert "Standard Burmese is not a well-defined variety" in source["scope"]
    assert "Rangoon-Mandalay" in source["scope"]

    claim = claims["CLM-NISHI-1998-SANDHI-001"]
    assert claim["source_id"] == "NISHI1998_VOICING_RULES"
    assert claim["status"] == "DOCUMENTARY"
    assert "C1aC2" in claim["claim"]
    assert "non-stop tonal rhyme" in claim["claim"]

    first = rules["NISHI98_ATONIC_C1C2_VOICING"]
    second = rules["NISHI98_POST_NONSTOP_RHYME_VOICING"]
    for rule in (first, second):
        assert rule["source_id"] == "NISHI1998_VOICING_RULES"
        assert rule["claim_id"] == "CLM-NISHI-1998-SANDHI-001"
        assert rule["status"] == "analysis_dependent"
        assert rule["test_reference"] == "tests/test_source_rule_evidence.py"
        assert "do not enable globally" in rule["scope"] or "not a grapheme-only mapping" in rule["scope"]

    variation = claims["CLM-NISHI-1998-VARIATION-001"]
    assert "not obligatory" in variation["claim"]
    assert variation["status"] == "DOCUMENTARY"
    mlc = claims["CLM-NISHI-1998-MLC-TRANSCRIPTIONS-001"]
    assert "Myanmar-English Dictionary (1993)" in mlc["claim"]
    assert mlc["status"] == "DOCUMENTARY"

