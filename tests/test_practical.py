from burmese_ukrainian.practical import practical_from_ipa, rank_ukrainian_candidates, transcribe_ipa
from burmese_ukrainian.rule_engine import RuleBasedBurmeseEngine


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
    assert practical_from_ipa("ɦ")["candidates"][0]["text"] == "г"
    assert practical_from_ipa("ɡ")["candidates"][0]["text"] == "ґ"
    assert practical_from_ipa("g")["candidates"][0]["text"] == "ґ"
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


def test_full_ipa_sequence_adapter_handles_ukrainian_target_conventions():
    result = transcribe_ipa("h ɦ ɡ g x t͡s d͡z t͡ʃ d͡ʒ tɕ dʑ t͡ɕ d͡ʑ")
    assert result["text"] == "г г ґ ґ х ц дз ч дж ч дж ч дж"
    assert result["status"] == "proposed"


def test_sequence_adapter_keeps_affricates_distinct_from_consonant_sequences():
    assert transcribe_ipa("t s")["text"] == "т с"
    assert transcribe_ipa("d z")["text"] == "д з"
    assert transcribe_ipa("b d n m")["text"] == "б д н м"


def test_sequence_adapter_omits_prosodic_marks_but_preserves_them_in_trace():
    result = transcribe_ipa("kʰàː")
    assert result["text"] == "к'а"
    assert any(item["kind"] == "tone" for item in result["prosody"])
    assert any(item["kind"] == "length" for item in result["prosody"])


def test_sequence_adapter_uses_yotated_ukrainian_vowels_after_syllable_initial_j():
    assert transcribe_ipa("ja je ji jo ju")["text"] == "я є ї йо ю"
    assert transcribe_ipa("a.ja")["text"] == "ая"


def test_sequence_adapter_handles_engine_inventory_and_zero_glottal_stop():
    assert transcribe_ipa("bʰ dʰ z ɲ ɹ j l θ ð")["text"] == "б' д' з нь р й л т з"
    assert transcribe_ipa("ʔa")["text"] == "а"


def test_sequence_adapter_fails_closed_on_unknown_ipa():
    result = transcribe_ipa("kʰɤ")
    assert result["text"] is None
    assert result["status"] == "not_established"
    assert result["unsupported"] == "ɤ"


def test_rule_engine_returns_ukrainian_practical_rendering_after_ipa():
    result = RuleBasedBurmeseEngine().analyze("ကာ")
    assert result["ipa"] == "ka"
    assert result["ukrainian"] == "ка"
    assert result["ukrainian_status"] == "proposed"
    multi = RuleBasedBurmeseEngine().analyze("ကာကာ")
    assert multi["ipa"] == "ka ka"
    assert multi["ukrainian"] == "кака"
    assert multi["ukrainian_syllables"] == ["ка", "ка"]
