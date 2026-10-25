"""Regression gates: structural parse success must not imply full phonological certainty."""

from burmese_ukrainian import parse_burmese, to_ipa


def test_parse_success_does_not_claim_supported_phonology():
    parsed = parse_burmese("ကေ")
    phonetic = to_ipa("ကေ")

    assert parsed["syllables"]
    syllable = phonetic["syllables"][0]
    assert syllable["phonetic_status"] in {"conservative_partial", "analysis_dependent"}
    assert syllable["phonetic_status"] != "supported"


def test_unresolved_inherent_vowel_withholds_ipa_instead_of_emitting_placeholder():
    result = to_ipa("က")
    syllable = result["syllables"][0]

    assert syllable["ipa"] is None
    assert syllable["phonetic_status"] == "analysis_dependent"
    assert result["ipa"] == "?"


def test_malformed_cluster_does_not_gain_phonological_certainty():
    result = to_ipa("က္")
    assert result["syllables"]
    assert all(s["phonetic_status"] != "supported" for s in result["syllables"])
    assert result["syllables"][0]["ipa"] is None
    assert result["syllables"][0]["phonetic_status"] == "analysis_dependent"
    assert result["ipa"] == "?"



def test_bare_consonant_bounded_by_non_myanmar_text_is_withheld():
    result = to_ipa("က A")
    bare = next(s for s in result["syllables"] if s["raw"] == "က")
    assert bare["ipa"] is None
    assert bare["phonetic_status"] == "analysis_dependent"
    assert result["ipa"].split()[0] == "?"


def test_contiguous_myanmar_bare_clusters_keep_existing_contextual_path():
    result = to_ipa("ကမ")
    assert len(result["syllables"]) == 2
    assert all(s["ipa"] is not None for s in result["syllables"])
    assert all(s["phonetic_status"] == "conservative_partial" for s in result["syllables"])
