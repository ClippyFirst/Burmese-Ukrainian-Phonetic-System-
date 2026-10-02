from burmese_ukrainian import parse_burmese
def test_medials_and_vowel():
    s=parse_burmese("ကြွေ")["syllables"][0]
    assert [m["id"] for m in s["medials"]]==["medial_ra","medial_wa"]
    assert s["vowel"]["signs"][0]["id"]=="e"
def test_malformed_virama_not_phonologized():
    s=parse_burmese("က္")["syllables"][0]
    assert s["analysis"]["status"] in {"invalid","unsupported_or_malformed","partially_unparsed"}
