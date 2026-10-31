from burmese_ukrainian import parse_burmese


def test_medials_and_vowel():
    s = parse_burmese("ကြွေ")["syllables"][0]
    assert [m["id"] for m in s["medials"]] == ["medial_ra", "medial_wa"]
    assert s["vowel"]["signs"][0]["id"] == "e"


def test_malformed_virama_not_phonologized():
    s = parse_burmese("က္")["syllables"][0]
    assert s["analysis"]["status"] in {
        "invalid",
        "unsupported_or_malformed",
        "partially_unparsed",
    }


def test_empty_and_whitespace_only_input_are_not_successful_analysis():
    for text in ("", " ", "\t\n"):
        result = parse_burmese(text)
        assert result["status"] == "empty_input"
        assert result["normalized"] == text
        assert result["graphemes"] == []
        assert result["syllables"] == []


def test_non_burmese_myanmar_extension_letter_is_not_accepted_as_burmese():
    # U+AA60 is a Khamti letter in Myanmar Extended-A, not a Standard Burmese
    # onset. Block recognition must not be confused with Burmese inventory support.
    text = "\uAA60"
    result = parse_burmese(text)

    assert result["graphemes"] == [text]
    assert result["status"] == "contains_uncertainty_or_invalid_input"
    assert len(result["syllables"]) == 1
    syllable = result["syllables"][0]
    assert syllable["raw"] == text
    assert syllable["onset"] == {}
    assert syllable["analysis"]["status"] == "unsupported_or_malformed"


def test_adjacent_unknown_myanmar_extension_is_preserved_after_valid_syllable():
    source = "ကာ\uAA60"
    result = parse_burmese(source)

    assert result["normalized"] == source
    assert "".join(result["graphemes"]) == source
    assert len(result["syllables"]) == 1
    syllable = result["syllables"][0]
    assert syllable["raw"] == source
    assert syllable["analysis"]["status"] == "partially_unparsed"


def test_python_parser_reconstructs_mixed_sentence_source_units():
    source = "ကာ ABC-42 ၁၂၃၊။"
    result = parse_burmese(source)

    assert result["normalized"] == source
    assert "".join(result["graphemes"]) == source
    assert "".join(syllable["raw"] for syllable in result["syllables"]) == source
