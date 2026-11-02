from scripts.benchmark_burmese_crf import (
    build_feature_input,
    parse_prediction_sequences,
)


def test_build_feature_input_preserves_word_sequence_boundaries():
    rows = [
        {
            "case_id": "one",
            "orthography": "က",
            "expected_ipa": "kə",
            "source_locator": "https://example.invalid/source#L1",
            "source_id": "test-source",
            "ipa_convention": "test IPA",
            "syllable_broken_word": "က",
        },
        {
            "case_id": "two",
            "orthography": "မင်္ဂလာ",
            "expected_ipa": "mɪ̀ɴ ɡə la̰",
            "source_locator": "https://example.invalid/source#L1",
            "source_id": "test-source",
            "ipa_convention": "test IPA",
            "syllable_broken_word": "မင် ဂ လာ",
        },
    ]

    feature_input, prepared, skipped = build_feature_input(rows)

    assert feature_input.splitlines() == [
        "က က ?",
        "",
        "မင် မင် ?",
        "ဂ ဂ ?",
        "လာ လာ ?",
        "",
    ]
    assert [row["case_id"] for row in prepared] == ["one", "two"]
    assert [len(row["syllables"]) for row in prepared] == [1, 3]
    assert skipped == []


def test_build_feature_input_marks_missing_syllable_segmentation():
    rows = [
        {
            "case_id": "missing",
            "orthography": "က",
            "expected_ipa": "kə",
            "source_locator": "https://example.invalid/source#L2",
            "source_id": "test-source",
            "ipa_convention": "test IPA",
            "syllable_broken_word": "   ",
        },
        {
            "case_id": "valid",
            "orthography": "မ",
            "expected_ipa": "ma̰",
            "source_locator": "https://example.invalid/source#L1",
            "source_id": "test-source",
            "ipa_convention": "test IPA",
            "syllable_broken_word": "မ",
        },
    ]

    feature_input, prepared, skipped = build_feature_input(rows)

    assert feature_input == "မ မ ?\n\n"
    assert [row["case_id"] for row in prepared] == ["valid"]
    assert skipped == [{
        "case_id": "missing",
        "reason": "MISSING_SYLLABLE_SEGMENTATION",
    }]


def test_build_feature_input_fails_closed_when_every_row_is_unsegmentable():
    rows = [{
        "case_id": "missing",
        "orthography": "က",
        "expected_ipa": "kə",
        "source_locator": "https://example.invalid/source#L3",
        "source_id": "test-source",
        "ipa_convention": "test IPA",
        "syllable_broken_word": "",
    }]

    try:
        build_feature_input(rows)
    except ValueError as error:
        assert "no probe rows contain syllable-broken orthography" in str(error)
    else:
        raise AssertionError("expected an all-unsegmentable probe to fail")


def test_parse_prediction_sequences_keeps_lexical_boundaries():
    output = "kə\nma̰\n\nɡə\nla̰\n\n"

    assert parse_prediction_sequences(output) == [
        ["kə", "ma̰"],
        ["ɡə", "la̰"],
    ]


def test_parse_prediction_sequences_accepts_final_sequence_without_trailing_blank():
    assert parse_prediction_sequences("kə\nma̰\n") == [["kə", "ma̰"]]


def test_parse_prediction_sequences_ignores_empty_runs():
    assert parse_prediction_sequences("\n\nkə\n\n\nma̰\n") == [
        ["kə"],
        ["ma̰"],
    ]
