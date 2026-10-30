from burmese_ukrainian.practical import practical_from_ipa, rank_ukrainian_candidates


def test_aspiration_is_marked_with_apostrophe():
    assert practical_from_ipa("kʰ")["candidates"][0]["text"] == "к'"
    assert practical_from_ipa("tʰ")["candidates"][0]["text"] == "т'"
    assert practical_from_ipa("pʰ")["candidates"][0]["text"] == "п'"
    assert practical_from_ipa("sʰ")["candidates"][0]["text"] == "с'"


def test_velar_nasal_is_explicit():
    assert practical_from_ipa("ŋ")["candidates"][0]["text"] == "нг"


def test_burmese_i_uses_ukrainian_i():
    assert practical_from_ipa("i")["candidates"][0]["text"] == "і"


def test_h_g_and_x_are_distinguished():
    assert practical_from_ipa("h")["candidates"][0]["text"] == "г"
    assert practical_from_ipa("ɡ")["candidates"][0]["text"] == "ґ"
    assert practical_from_ipa("x")["candidates"][0]["text"] == "х"


def test_affricates_use_ukrainian_digraphs():
    assert practical_from_ipa("tɕ")["candidates"][0]["text"] == "ч"
    assert practical_from_ipa("tɕʰ")["candidates"][0]["text"] == "ч'"
    assert practical_from_ipa("dʑ")["candidates"][0]["text"] == "дж"


def test_glottal_stop_is_not_aspiration():
    assert practical_from_ipa("ʔ")["candidates"][0]["text"] == "∅"


def test_unknown_value_is_not_silently_guessed():
    assert rank_ukrainian_candidates("ɤ")[0].status == "not_established"


def test_dental_fricative_candidate_remains_analysis_dependent():
    result = practical_from_ipa("θ~ð")
    assert result["status"] == "analysis_dependent"
    assert result["candidates"][0]["text"] == "т"
    assert "RU_EPSHTEIN_1959" in result["candidates"][0]["evidence"]
