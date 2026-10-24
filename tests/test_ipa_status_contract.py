"""Regression gates: structural parse success must not imply full phonological certainty."""

from burmese_ukrainian import parse_burmese, to_ipa


def test_parse_success_does_not_claim_supported_phonology():
    parsed = parse_burmese("ကေ")
    phonetic = to_ipa("ကေ")

    assert parsed["syllables"]
    syllable = phonetic["syllables"][0]
    assert syllable["phonetic_status"] in {"conservative_partial", "analysis_dependent"}
    assert syllable["phonetic_status"] != "supported"


def test_partial_ipa_is_not_silently_promoted_to_complete_output():
    result = to_ipa("က")
    syllable = result["syllables"][0]

    assert syllable["ipa"] is not None
    assert "?" in syllable["ipa"]
    assert syllable["phonetic_status"] == "conservative_partial"


def test_malformed_cluster_does_not_gain_phonological_certainty():
    result = to_ipa("က္")
    assert result["syllables"]
    assert all(s["phonetic_status"] != "supported" for s in result["syllables"])
    assert result["syllables"][0]["ipa"] is None
    assert result["syllables"][0]["phonetic_status"] == "analysis_dependent"
    assert result["ipa"] == "?"


def test_partially_unparsed_cluster_does_not_emit_partial_ipa():
    # A recognized onset must not leak a plausible-looking transcription if
    # the parser could not consume the entire source grapheme cluster.
    result = to_ipa("ကေ့က")
    partial = [s for s in result["syllables"] if s["status"] != "established"]
    assert partial
    assert all(s["ipa"] is None for s in partial)
