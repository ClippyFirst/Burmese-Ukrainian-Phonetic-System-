from burmese_ukrainian import normalize_burmese, segment_graphemes
def test_nfc_idempotence():
    x=normalize_burmese("က့်")
    assert normalize_burmese(x)==x
def test_e_vowel_cluster():
    assert segment_graphemes("ကေ")==["ကေ"]
def test_kinzi_cluster():
    assert segment_graphemes("င်္က")==["င်္က"]


def test_myanmar_extended_c_is_recognized_as_script_not_foreign_text():
    from burmese_ukrainian.unicode import is_myanmar

    # U+116D0 is in the Myanmar Extended-C block. Recognition does not
    # imply that this project has a Burmese pronunciation rule for it.
    assert is_myanmar("\U000116D0")
    assert not is_myanmar("A")
