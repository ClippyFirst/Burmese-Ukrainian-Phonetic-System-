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
    source = "ကာ\tABC-42\r\n၁၂၃၊။\u200b𑛐 😀 العربية ဂီ"
    result = parse_burmese(source)

    assert result["normalized"] == source
    assert "".join(result["graphemes"]) == source
    assert "".join(syllable["raw"] for syllable in result["syllables"]) == source


def test_python_parser_preserves_multiline_mixed_script_adversarial_input():
    # Structural/source-integrity probe only: the unsupported Khamti code point
    # must remain visible between valid Burmese units. This is not IPA gold.
    source = "ကာ\\tABC-42\\r\\n၁၂၃၊။\\u200b𑛐 😀 العربية ဂီ"
    result = parse_burmese(source)

    assert result["normalized"] == source
    assert "".join(result["graphemes"]) == source
    assert "".join(syllable["raw"] for syllable in result["syllables"]) == source

    by_raw = {syllable["raw"]: syllable for syllable in result["syllables"]}
    assert by_raw["ကာ"]["analysis"]["status"] == "established"
    assert by_raw["𑛐"]["analysis"]["status"] == "unsupported_or_malformed"
    assert by_raw["ဂီ"]["analysis"]["status"] == "established"


def test_every_assigned_myanmar_letter_and_mark_is_losslessly_accounted_for():
    import unicodedata

    ranges = (
        (0x1000, 0x109F),
        (0xA9E0, 0xA9FF),
        (0xAA60, 0xAA7F),
        (0x116D0, 0x116FF),
    )
    tested = 0
    for start, end in ranges:
        for codepoint in range(start, end + 1):
            char = chr(codepoint)
            if unicodedata.category(char)[0] not in {"L", "M"}:
                continue
            result = parse_burmese(char)
            assert "".join(item["raw"] for item in result["syllables"]) == char, (
                f"source lost for U+{codepoint:04X}"
            )
            assert len(result["syllables"]) == 1
            syllable = result["syllables"][0]
            assert syllable["codepoints"] == [f"U+{codepoint:04X}"]
            if syllable["analysis"]["status"] != "established":
                assert syllable["onset"] == {}
            tested += 1
    assert tested > 0


def test_unmodelled_myanmar_extension_letter_never_receives_synthetic_ipa():
    from burmese_ukrainian.ipa import to_ipa

    # Khamti U+AA60 is in a Myanmar block but outside the selected Burmese
    # phonological inventory; block membership must not create a sound value.
    result = to_ipa(chr(0xAA60))
    assert result["syllables"][0]["ipa"] is None
    assert result["syllables"][0]["phonetic_status"] == "analysis_dependent"
    assert result["syllables"][0]["raw"] == chr(0xAA60)


def test_asat_marked_final_consonant_is_attached_to_preceding_syllable():
    parsed = parse_burmese("မြန်")
    assert parsed["graphemes"] == ["မြန်"]
    assert len(parsed["syllables"]) == 1
    syllable = parsed["syllables"][0]
    assert syllable["medials"][0]["id"] == "medial_ra"
    assert syllable["coda"]["character"] == "န"
    assert syllable["coda"]["codepoint"] == "U+1014"
    assert syllable["coda"]["asat_codepoint"] == "U+103A"
    assert syllable["analysis"]["status"] == "established"


def test_asat_marked_coda_does_not_become_a_new_syllable_in_compound():
    parsed = parse_burmese("မြန်မာ")
    assert parsed["graphemes"] == ["မြန်", "မာ"]
    assert len(parsed["syllables"]) == 2
    assert parsed["syllables"][0]["coda"]["character"] == "န"
    assert parsed["syllables"][1]["onset"]["character"] == "မ"


def test_regular_checked_syllable_final_is_structurally_attached():
    parsed = parse_burmese("ကတ်")
    assert parsed["graphemes"] == ["ကတ်"]
    assert parsed["syllables"][0]["coda"]["character"] == "တ"
