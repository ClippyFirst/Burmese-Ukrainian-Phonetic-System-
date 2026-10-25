"""Evidence-gating contracts, not an adjudicated Burmese IPA gold set."""

from burmese_ukrainian import to_ipa


def test_dangling_virama_does_not_become_plausible_ipa():
    result = to_ipa("က\u1039")

    assert result["status"] == "contains_uncertainty_or_invalid_input"
    assert len(result["syllables"]) == 1
    assert result["syllables"][0]["status"] == "invalid"
    assert result["syllables"][0]["ipa"] is None
    assert result["ipa"] == "?"


def test_unresolved_asat_coda_is_not_silently_dropped_from_ipa():
    result = to_ipa("ကာ\u103a")

    assert result["syllables"][0]["coda"] is not None
    assert result["syllables"][0]["ipa"] is None
    assert result["ipa"] == "?"


def test_unresolved_prosodic_mark_is_not_silently_dropped_from_ipa():
    result = to_ipa("ကာ့")

    assert result["syllables"][0]["tone_mark"] is not None
    assert result["syllables"][0]["ipa"] is None
    assert result["ipa"] == "?"
