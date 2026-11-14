"""Evidence-gating contracts, not an adjudicated Burmese IPA gold set."""

from burmese_ukrainian import to_ipa


def test_dangling_virama_does_not_become_plausible_ipa():
    result = to_ipa("က\u1039")

    assert result["status"] == "contains_uncertainty_or_invalid_input"
    assert len(result["syllables"]) == 1
    assert result["syllables"][0]["status"] == "invalid"
    assert result["syllables"][0]["ipa"] is None
    assert result["ipa"] == "?"


def test_misplaced_virama_after_vowel_is_not_silently_dropped():
    result = to_ipa("ကာ\u1039")

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


def test_unresolved_anusvara_is_not_silently_deleted_from_ipa():
    result = to_ipa("ကံ")

    assert any(sign["id"] == "anusvara" for sign in result["syllables"][0]["vowel"]["signs"])
    assert result["syllables"][0]["ipa"] is None
    assert result["ipa"] == "?"


def test_unimplemented_medials_conjuncts_and_kinzi_are_not_silently_dropped():
    medial = to_ipa("ကြွေ")
    assert medial["syllables"][0]["status"] == "established"
    assert [item["id"] for item in medial["syllables"][0]["medials"]] == [
        "medial_ra", "medial_wa"
    ]
    assert medial["syllables"][0]["ipa"] is None

    conjunct = to_ipa("က္ကာ")
    assert conjunct["syllables"][0]["status"] == "established"
    assert conjunct["syllables"][0]["conjunct"]
    assert conjunct["syllables"][0]["ipa"] is None

    kinzi = to_ipa("င်္ဂါ")
    assert kinzi["syllables"][0]["status"] == "established"
    assert kinzi["syllables"][0]["kinzi"] is not None
    assert kinzi["syllables"][0]["ipa"] is None


def test_public_burmese_engine_marks_unimplemented_structures_partial():
    from burmese_ukrainian.rule_engine import RuleBasedBurmeseEngine

    engine = RuleBasedBurmeseEngine()
    for source in ("ကြွေ", "က္ကာ", "င်္ဂါ"):
        result = engine.analyze(source)
        assert result["ipa"] is None
        assert result["status"] == "PARTIAL"
