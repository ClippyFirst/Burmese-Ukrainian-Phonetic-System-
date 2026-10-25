from burmese_ukrainian import parse_burmese
def test_medials_and_vowel():
    s=parse_burmese("ကြွေ")["syllables"][0]
    assert [m["id"] for m in s["medials"]]==["medial_ra","medial_wa"]
    assert s["vowel"]["signs"][0]["id"]=="e"
def test_malformed_virama_not_phonologized():
    s=parse_burmese("က္")["syllables"][0]
    assert s["analysis"]["status"] in {"invalid","unsupported_or_malformed","partially_unparsed"}


def test_empty_and_whitespace_only_input_are_not_successful_analysis():
    for text in ("", " ", "\\t\\n"):
        result = parse_burmese(text)
        assert result["status"] == "empty_input"
        assert result["normalized"] == text
        assert result["graphemes"] == []
        assert result["syllables"] == []
