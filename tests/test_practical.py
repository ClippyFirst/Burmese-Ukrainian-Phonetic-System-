from burmese_ukrainian.practical import practical_from_ipa, rank_ukrainian_candidates


def test_russian_aspiration_is_not_copied():
    assert practical_from_ipa("kʰ")["candidates"][0]["text"] == "к"


def test_velar_nasal_is_explicit():
    assert practical_from_ipa("ŋ")["candidates"][0]["text"] == "нг"


def test_burmese_i_uses_ukrainian_i():
    assert practical_from_ipa("i")["candidates"][0]["text"] == "і"


def test_h_remains_explicitly_uncertain():
    result = practical_from_ipa("h")
    assert result["status"] == "analysis_dependent"
    assert {c["text"] for c in result["candidates"]} == {"г"}


def test_unknown_value_is_not_silently_guessed():
    assert rank_ukrainian_candidates("ɤ")[0].status == "not_established"
