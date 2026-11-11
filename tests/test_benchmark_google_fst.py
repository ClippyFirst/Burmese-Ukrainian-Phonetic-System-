import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = runpy.run_path(str(ROOT / "scripts" / "benchmark_google_fst.py"))
build_report = MODULE["build_report"]
parse_outputs = MODULE["parse_outputs"]
build_command = MODULE["build_command"]


def test_google_fst_report_is_raw_output_only_without_accuracy():
    rows = [
        {"case_id": "struct-001", "orthography": "ကေ", "evidence_status": "STRUCTURAL_ONLY", "expected_ipa": ""},
        {"case_id": "struct-002", "orthography": "ကော်", "evidence_status": "STRUCTURAL_ONLY", "expected_ipa": ""},
    ]
    report = build_report(
        rows,
        [{"raw_engine_line": "ကေ\\tkè", "raw_output_ipa": "kè"}, {"raw_engine_line": "ကော်\\tkɔ́", "raw_output_ipa": "kɔ́"}],
        engine_source_commit="a90601024f07ab7e96c911243324e0adeb16da96",
        grammar_sha256="a" * 64,
        phoneme_symbols_sha256="b" * 64,
        fst_sha256="c" * 64,
        bazel_version="4.2.3",
        corpus_sha256="d" * 64,
    )

    assert report["input_count"] == 2
    assert report["successful_outputs"] == 2
    assert report["independent_gold_count"] == 0
    assert report["accuracy"] is None
    assert report["score_status"] == "RAW_OUTPUT_SMOKE_NOT_ACCURACY"
    assert report["records"][0]["orthography"] == "ကေ"
    assert report["records"][0]["raw_output_ipa"] == "kè"
    assert report["provenance"]["engine_source_commit"] == "a90601024f07ab7e96c911243324e0adeb16da96"
    assert report["provenance"]["abseil_source_commit"] == "45fdade6c0415ec5af3f9312e6311a4ccc682a7b"


def test_google_fst_output_parser_splits_echoed_input_from_ipa_and_checks_alignment():
    rows = [
        {"orthography": "ကေ"},
        {"orthography": "ကော်"},
    ]
    parsed = parse_outputs("ကေ\\tk è\\nကော်\\tk ɔ̀\\n", rows)
    assert [row["raw_output_ipa"] for row in parsed] == ["k è", "k ɔ̀"]
    assert [row["raw_engine_line"] for row in parsed] == ["ကေ\\tk è", "ကော်\\tk ɔ̀"]

    try:
        parse_outputs("ကေ\\tk è\\n", rows)
    except ValueError as error:
        assert "expected 2 output lines" in str(error)
    else:
        raise AssertionError("expected an output-count error")

    try:
        parse_outputs("ကော်\\tk è\\nကေ\\tk ɔ̀\\n", rows)
    except ValueError as error:
        assert "echoed input does not match" in str(error)
    else:
        raise AssertionError("expected an input-alignment error")


def test_google_fst_refuses_non_structural_or_labelled_probe_rows():
    rows = [
        {"case_id": "gold", "orthography": "ကေ", "evidence_status": "GOLD_VERIFIED", "expected_ipa": "kè"}
    ]
    try:
        build_report(
            rows,
            ["kè"],
            engine_source_commit="a90601024f07ab7e96c911243324e0adeb16da96",
            grammar_sha256="a" * 64,
            phoneme_symbols_sha256="b" * 64,
            fst_sha256="c" * 64,
            bazel_version="4.2.3",
            corpus_sha256="d" * 64,
        )
    except ValueError as error:
        assert "STRUCTURAL_ONLY" in str(error)
    else:
        raise AssertionError("expected structural-only gate failure")


def test_command_invokes_thrax_binary_with_pinned_fst_and_symbol_table(tmp_path):
    binary = tmp_path / "bazel-bin" / "utils" / "thrax_g2p"
    fst = tmp_path / "bazel-bin" / "my" / "G2P.fst"
    symbols = tmp_path / "bazel-bin" / "my" / "ipa_phoneme.syms"

    command = build_command(binary, fst, symbols)

    assert command == [
        str(binary.resolve()),
        f"--fst={fst.resolve()}",
        f"--phoneme_syms={symbols.resolve()}",
    ]
