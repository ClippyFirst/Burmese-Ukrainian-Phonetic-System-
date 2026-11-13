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

def test_green_2005_phonological_rules_preserve_broad_ipa_and_surface_nasalization():
    claims = {row["claim_id"]: row for row in _rows(DATA / "source_claims.csv")}
    rules = {row["rule_id"]: row for row in _rows(DATA / "phonological_rules.csv")}
    transcription = claims["CLM-GREEN2005-TRANSCRIPTION-001"]
    assert transcription["source_id"] == "GREEN2005_BURMESE_PHONOLOGY"
    assert "broad conventions" in transcription["claim"]
    assert "ALA-LC" in transcription["claim"]
    nasal = claims["CLM-GREEN2005-ONSET-CODA-001"]
    assert "nasalization on the preceding vowel" in nasal["claim"]
    rule = rules["GREEN2005_PLACELESS_NASAL_CODA"]
    assert rule["status"] == "analysis_dependent"
    assert rule["source_id"] == "GREEN2005_BURMESE_PHONOLOGY"
    assert rule["claim_id"] == "CLM-GREEN2005-ONSET-CODA-001"
    assert "Keep abstract /N/ distinct" in rule["scope"]


def test_sealang_resources_are_text_candidates_not_ipa_gold():
    sources = {row["source_id"]: row for row in _rows(DATA / "sources.csv")}
    claims = {row["claim_id"]: row for row in _rows(DATA / "source_claims.csv")}
    dictionary = sources["SEALANG_MLC_DICT_2006"]
    assert "35,000 entries" in dictionary["scope"]
    assert "entry-level transcription semantics remain unresolved" in dictionary["scope"]
    assert "project owner confirms project-specific research and ingestion permission" in dictionary["scope"]
    text = sources["SEALANG_BURMESE_TEXT_2006"]
    assert "Monolingual corpus" in text["scope"]
    assert "public metadata does not state a reuse license" in text["scope"]
    bitext = sources["SEALANG_BURMESE_BITEXT_2006"]
    assert "sentence-aligned where possible" in bitext["scope"]
    assert "public metadata does not state a reuse license" in bitext["scope"]
    assert claims["CLM-SEALANG-DICT-TRANS-001"]["status"] == "DOCUMENTARY"
    assert "not a direct inspection of the internal transcription fields" in claims["CLM-SEALANG-DICT-TRANS-001"]["claim"]

def test_nishi_1998_source_notation_is_not_project_ipa():
    claims = {row["claim_id"]: row for row in _rows(DATA / "source_claims.csv")}
    source_claim = claims["CLM-NISHI-1998-TRANSCRIPTION-001"]
    historical = claims["CLM-NISHI-1998-HISTORICAL-STAGES-001"]
    assert source_claim["source_id"] == "NISHI1998_VOICING_RULES"
    assert source_claim["status"] == "DOCUMENTARY"
    assert "not project IPA gold" in source_claim["claim"]
    assert historical["source_id"] == "NISHI1998_VOICING_RULES"
    assert historical["status"] == "ANALYSIS_DEPENDENT"
    assert "not a universal synchronic rule sequence" in historical["claim"]

    rule = next(
        row for row in _rows(DATA / "phonological_rules.csv")
        if row["rule_id"] == "NISHI98_HISTORICAL_THREE_RULE_SEQUENCE"
    )
    assert rule["claim_id"] == historical["claim_id"]
    assert rule["status"] == "analysis_dependent"
    assert "never enabled in runtime" in rule["scope"]


def test_myx_corpus_schema_and_quality_limits_are_explicit():
    claims = {row["claim_id"]: row for row in _rows(DATA / "source_claims.csv")}
    schema_claim = claims["CLM-MYX-MYANGLISH-RAW-SCHEMA-001"]
    quality_claim = claims["CLM-MYX-ORTHO-QUALITY-001"]
    assert schema_claim["source_id"] == "MYX_MYANGLISH_2026"
    assert schema_claim["status"] == "UNCERTAIN"
    assert "two columns" in schema_claim["claim"]
    assert "third official_standard feature" in schema_claim["claim"]
    assert quality_claim["source_id"] == "MYX_ORTHO_2026"
    assert quality_claim["status"] == "DOCUMENTARY"
    assert "target_words" in quality_claim["claim"]
    assert "not an IPA corpus" in quality_claim["claim"]

def test_nishi_old_burmese_historical_claims_have_source_and_scope():
    sources = {row["source_id"]: row for row in _rows(DATA / "sources.csv")}
    claims = {row["claim_id"]: row for row in _rows(DATA / "source_claims.csv")}
    rules = {row["rule_id"]: row for row in _rows(DATA / "phonological_rules.csv")}
    source = sources["NISHI1998_OLDBURMESE"]
    assert "pp.659-692" in source["scope"]
    assert "Old Burmese" in source["title"]

    h_claim = claims["CLM-NISHI-OWB-MEDIAL-CLASS-001"]
    l_claim = claims["CLM-NISHI-OWB-L-MEDIAL-001"]
    ry_claim = claims["CLM-NISHI-MB-RY-MERGER-001"]
    dialect_claim = claims["CLM-NISHI-OB-CLUSTER-DIALECT-001"]
    assert all(claim["source_id"] == "NISHI1998_OLDBURMESE" for claim in (h_claim, l_claim, ry_claim, dialect_claim))
    assert h_claim["status"] == "DOCUMENTARY"
    assert l_claim["status"] == ry_claim["status"] == "ANALYSIS_DEPENDENT"
    assert dialect_claim["status"] == "DIALECT_DEPENDENT"
    assert "not a direct classification of modern Myanmar Unicode signs" in h_claim["claim"]
    assert "merged into -y-" in ry_claim["claim"]
    assert "standard-variety interference and hypercorrection" in dialect_claim["claim"]

    rule = rules["NISHI_OB_CLUSTER_DIALECT_REFLEXES"]
    assert rule["source_id"] == source["source_id"]
    assert rule["claim_id"] == dialect_claim["claim_id"]
    assert rule["status"] == "dialect_dependent"
    assert "no modern runtime mapping" in rule["scope"]

def test_okell_1995_dialect_evidence_has_separate_profiles_and_transcription_scope():
    sources = {row["source_id"]: row for row in _rows(DATA / "sources.csv")}
    claims = {row["claim_id"]: row for row in _rows(DATA / "source_claims.csv")}
    rules = {row["rule_id"]: row for row in _rows(DATA / "phonological_rules.csv")}
    source = sources["OKELL1995_THREE_DIALECTS"]
    assert source["title"] == "Three Burmese Dialects"
    assert "pp.1-138" in source["scope"]
    assert "no audio" in source["scope"]

    wb_sb = claims["CLM-OKELL1995-WB-SB-DISTINCTION-001"]
    ar = claims["CLM-OKELL1995-AR-RY-001"]
    it = claims["CLM-OKELL1995-IT-MEDIAL-L-001"]
    tv = claims["CLM-OKELL1995-TV-MEDIAL-L-001"]
    transcription = claims["CLM-OKELL1995-TRANSCRIPTION-001"]
    profile = claims["CLM-OKELL1995-AR-PROFILE-001"]
    shared_l = claims["CLM-OKELL1995-IT-TV-MEDIAL-L-001"]
    assert all(claim["source_id"] == source["source_id"] for claim in (wb_sb, ar, it, tv, transcription, profile, shared_l))
    assert "Written Burmese (WB)" in wb_sb["claim"]
    assert "has merged WB r with y in speech" in ar["claim"]
    assert "not be projected onto SB/Yangon" in it["claim"]
    assert "not present in Standard Burmese" in tv["claim"]
    assert "not an independently adjudicated project IPA gold" in transcription["claim"]
    assert "high prestige" in profile["claim"]
    assert shared_l["status"] == "DIALECT_DEPENDENT"

    ar_rule = rules["OKELL1995_AR_WB_RY_DISTINCTION"]
    l_rule = rules["OKELL1995_IT_TV_MEDIAL_L"]
    assert ar_rule["claim_id"] == ar["claim_id"]
    assert ar_rule["status"] == "dialect_dependent"
    assert l_rule["claim_id"] == shared_l["claim_id"]
    assert l_rule["status"] == "dialect_dependent"
    assert "not a modern Yangon" in ar_rule["scope"]
    assert "do not import /l/" in l_rule["scope"]

def test_sealang_ipa_interface_is_not_mistaken_for_an_inspected_ipa_gold_field():
    sources = {row["source_id"]: row for row in _rows(DATA / "sources.csv")}
    claims = {row["claim_id"]: row for row in _rows(DATA / "source_claims.csv")}
    source = sources["SEALANG_2008_PROJECT_OVERVIEW"]
    interface = claims["CLM-SEALANG-DICT-IPA-INTERFACE-001"]
    representation = claims["CLM-SEALANG-DICT-REPRESENTATION-001"]
    assert "pp.1-7" in source["scope"]
    assert interface["source_id"] == source["source_id"]
    assert interface["status"] == "DOCUMENTARY"
    assert "interface level" in interface["claim"]
    assert "internal storage format" in interface["claim"]
    assert representation["source_id"] == source["source_id"]
    assert representation["status"] == "UNCERTAIN"
    assert "does not specify whether IPA is stored" in representation["claim"]
    assert "interface support alone does not establish an IPA gold corpus" in representation["claim"]

    mlcts2 = claims["CLM-MYA2ROM-SEALANG-MLCTS2-001"]
    assert mlcts2["source_id"] == "MYA2ROM044"
    assert mlcts2["status"] == "DOCUMENTARY"
    assert "MLCTS2" in mlcts2["claim"]
    assert "not be treated as standardized IPA" in mlcts2["claim"]


def test_okell_text_corpus_access_and_quality_boundary_is_explicit():
    sources = {row["source_id"]: row for row in _rows(DATA / "sources.csv")}
    claims = {row["claim_id"]: row for row in _rows(DATA / "source_claims.csv")}
    source = sources["OKELL_TEXT_2018"]
    claim = claims["CLM-OKELL-TEXT-STRUCTURE-001"]
    assert "HTTP 200 text/plain UTF-8" in source["scope"]
    assert "f020d7bbcf9857631094a8861143d18f" in source["scope"]
    assert "computed SHA-256 6bbafd699c587876317f6e0535b9dd8f9ec87c15efe4b7e65a8c7362ebcdbf4c" in source["scope"]
    assert "8,809,265" in source["scope"]
    assert "1 NUL in line 9,300" in source["scope"]
    assert "21 BOM markers" in source["scope"]
    assert "295 repeated nonblank line forms" in source["scope"]
    assert "1,008 excess occurrences" in source["scope"]
    assert "non-NFC" in source["scope"]
    assert "localized legacy encoding/glyph corruption" in source["scope"]
    assert claim["source_id"] == "OKELL_TEXT_2018"
    assert claim["status"] == "DOCUMENTARY"
    assert "67 numbered heading lines" in claim["claim"]
    assert "matches Zenodo provider MD5" in claim["claim"]
    assert "one NUL" in claim["claim"]
    assert "no IPA annotation schema" in claim["claim"]


def test_okell_text_corpus_orthographic_profile_is_not_phonological_gold():
    profile = _rows(DATA / "okell_text_corpus_orthographic_profile.csv")
    claims = {row["claim_id"]: row for row in _rows(DATA / "source_claims.csv")}
    assert len(profile) == 9
    assert all(row["source_id"] == "OKELL_TEXT_2018" for row in profile)
    assert all(row["source_sha256"] == "6bbafd699c587876317f6e0535b9dd8f9ec87c15efe4b7e65a8c7362ebcdbf4c" for row in profile)
    assert all(row["interpretation"] == "ORTHOGRAPHIC_ONLY" for row in profile)
    counts = {(row["measure"], row["sequence"]): int(row["count"]) for row in profile}
    assert counts[("codepoint_count", "U+103B")] == 50072
    assert counts[("codepoint_count", "U+103C")] == 73107
    assert counts[("codepoint_count", "U+103D")] == 49248
    assert counts[("codepoint_count", "U+103E")] == 50869
    assert counts[("substring_count", "မြန်")] == 659
    assert counts[("substring_count", "မြန်မာ")] == 288
    claim = claims["CLM-OKELL-TEXT-MEDIAL-FREQ-001"]
    assert claim["source_id"] == "OKELL_TEXT_2018"
    assert claim["status"] == "DOCUMENTARY"
    assert "not token frequencies" in claim["claim"]
    assert "pronunciation mappings" in claim["claim"]


def test_okell_1999_unicode_proposal_separates_added_finals_and_boundary_logic():
    sources = {row["source_id"]: row for row in _rows(DATA / "sources.csv")}
    claims = {row["claim_id"]: row for row in _rows(DATA / "source_claims.csv")}
    source = sources["OKELL1999_WG2_N2033"]
    assert "N2033" in source["title"]
    assert "Appendix 2" in source["scope"]
    assert "no audio" in source["scope"]

    added = claims["CLM-OKELL99-ADDED-FINALS-001"]
    boundary = claims["CLM-OKELL99-SYLLABLE-BOUNDARY-001"]
    tone = claims["CLM-OKELL99-OPEN-CLOSED-TONE-ORTHOGRAPHY-001"]
    assert all(claim["source_id"] == source["source_id"] for claim in (added, boundary, tone))
    assert all(claim["status"] == "DOCUMENTARY" for claim in (added, boundary, tone))
    assert "non-Burmese words and names" in added["claim"]
    assert "not by itself a phonological syllabification rule" in boundary["claim"]
    assert "orthographic encoding evidence" in tone["claim"]


def test_hill_2019_burmese_chapter_keeps_historical_medials_and_tone_scope_separate():
    sources = {row["source_id"]: row for row in _rows(DATA / "sources.csv")}
    claims = {row["claim_id"]: row for row in _rows(DATA / "source_claims.csv")}
    source = sources["HILL2019_HISTPHON"]
    assert "pp.46-83" in source["scope"]
    assert "third-party mirror" in source["scope"]
    assert "Secondary historical analysis" in source["scope"]

    medial = claims["CLM-HILL2019-OB-MEDIALS-001"]
    written = claims["CLM-HILL2019-WB-SCOPE-001"]
    tone = claims["CLM-HILL2019-OB-TONE-001"]
    caution = claims["CLM-HILL2019-OB-ORTHO-CAUTION-001"]
    assert all(claim["source_id"] == source["source_id"] for claim in (medial, written, tone, caution))
    assert all(claim["status"] == "DOCUMENTARY" for claim in (medial, written, tone, caution))
    assert "excludes it from the historical medial inventory" in medial["claim"]
    assert "not modern Unicode-to-IPA mappings" in written["claim"]
    assert "projects Written Burmese tone marking backwards" in tone["claim"]
    assert "unstable" in caution["claim"]

