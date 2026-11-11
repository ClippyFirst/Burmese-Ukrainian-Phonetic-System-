import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = runpy.run_path(str(ROOT / "scripts" / "benchmark_google_fst.py"))
build_report = MODULE["build_report"]
parse_outputs = MODULE["parse_outputs"]
binary_path_for_execution = MODULE["binary_path_for_execution"]


def test_google_fst_report_is_raw_output_only_without_accuracy():
    rows = [
        {"case_id": "struct-001", "orthography": "ကေ", "evidence_status": "STRUCTURAL_ONLY", "expected_ipa": ""},
        {"case_id": "struct-002", "orthography": "ကော်", "evidence_status": "STRUCTURAL_ONLY", "expected_ipa": ""},
    ]
    report = build_report(
        rows,
        ["kè", "kɔ́"],
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
    assert report["records"][0]["raw_output"] == "kè"
    assert report["provenance"]["engine_source_commit"] == "a90601024f07ab7e96c911243324e0adeb16da96"
    assert report["provenance"]["abseil_source_commit"] == "45fdade6c0415ec5af3f9312e6311a4ccc682a7b"


def test_google_fst_output_parser_requires_one_output_per_input():
    assert parse_outputs("kè\nkɔ́\n", 2) == ["kè", "kɔ́"]
    try:
        parse_outputs("kè\n", 2)
    except ValueError as error:
        assert "expected 2 output lines" in str(error)
    else:
        raise AssertionError("expected an output-count error")


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


def test_binary_execution_path_preserves_bazel_runfiles_symlink(tmp_path):
    target = tmp_path / "source" / "g2p.sh"
    target.parent.mkdir()
    target.write_text("#!/bin/sh\\n", encoding="utf-8")
    link = tmp_path / "bazel-bin" / "my" / "g2p"
    link.parent.mkdir(parents=True)
    link.symlink_to(target)

    assert binary_path_for_execution(link) == str(link.absolute())
    assert binary_path_for_execution(link) != str(link.resolve())
