from burmese_ukrainian import normalize_burmese, segment_graphemes
def test_nfc_idempotence():
    x=normalize_burmese("က့်")
    assert normalize_burmese(x)==x
def test_e_vowel_cluster():
    assert segment_graphemes("ကေ")==["ကေ"]
def test_kinzi_cluster():
    assert segment_graphemes("င်္က")==["င်္က"]
