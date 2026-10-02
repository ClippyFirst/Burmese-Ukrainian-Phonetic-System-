from burmese_ukrainian import parse_burmese
def test_other_script_not_established():
    s=parse_burmese("ก")["syllables"][0]
    assert s["analysis"]["status"]!="established"
