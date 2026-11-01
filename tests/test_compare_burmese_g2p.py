import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "compare_burmese_g2p", ROOT / "scripts" / "compare_burmese_g2p.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_raw_engine_comparison_does_not_call_agreement_accuracy():
    goruut = {
        "language_identifier": "Burmese",
        "engine_commit": "pinned",
        "records": [{
            "input": "ကေ",
            "status": "OK",
            "repetitions": [
                {"status": "OK", "phonetic_tokens": ["kè"]},
                {"status": "OK", "phonetic_tokens": ["kè"]},
                {"status": "OK", "phonetic_tokens": ["kè"]},
            ],
        }],
    }
    epitran = {
        "engine": "epitran",
        "engine_version": "1.35.3",
        "records": [{"orthography": "ကေ", "raw_output_ipa": "ke"}],
    }
    report = MODULE.compare_reports(goruut, epitran)
    assert report["compared_inputs"] == 1
    assert report["exact_string_matches"] == 0
    assert report["independent_gold_count"] == 0
    assert report["accuracy"] is None
    assert report["records"][0]["goruut_reproducible"] is True


def test_unstable_goruut_output_is_not_an_exact_agreement():
    goruut = {
        "language_identifier": "Burmese",
        "records": [{
            "input": "ကေ",
            "repetitions": [
                {"status": "OK", "phonetic_tokens": ["kè"]},
                {"status": "OK", "phonetic_tokens": ["ke"]},
            ],
        }],
    }
    epitran = {"engine": "epitran", "records": [{"orthography": "ကေ", "raw_output_ipa": "kè"}]}
    report = MODULE.compare_reports(goruut, epitran)
    assert report["records"][0]["goruut_reproducible"] is False
    assert report["exact_string_matches"] == 0


def test_source_attested_comparison_requires_complete_stable_unambiguous_goruut():
    goruut = {
        "language_identifier": "Burmese",
        "engine_commit": "pinned",
        "records": [{
            "input": "ကေ",
            "status": "OK",
            "source_coverage_complete": True,
            "source_coverage_status": "COMPLETE",
            "ambiguous_dictionary_selection": False,
            "repetitions": [
                {"status": "OK", "phonetic_tokens": ["kè"], "source_coverage_complete": True},
                {"status": "OK", "phonetic_tokens": ["kè"], "source_coverage_complete": True},
                {"status": "OK", "phonetic_tokens": ["kè"], "source_coverage_complete": True},
            ],
        }],
    }
    epitran = {
        "engine": "epitran",
        "engine_version": "1.35.3",
        "records": [{
            "orthography": "ကေ", "raw_output_ipa": "ke", "expected_ipa": "kè",
        }],
    }
    report = MODULE.compare_reports(goruut, epitran)
    row = report["records"][0]
    assert row["goruut_source_attested_exact_match"] is True
    assert row["epitran_source_attested_exact_match"] is False
    assert report["source_attested_diagnostic"]["goruut_exact_matches"] == 1
    assert report["source_attested_diagnostic"]["epitran_exact_matches"] == 0
    assert report["independent_gold_count"] == 0
    assert report["accuracy"] is None


def test_partial_or_randomized_goruut_output_is_not_source_scored():
    for coverage, randomized in ((False, False), (True, True)):
        goruut = {
            "language_identifier": "Burmese",
            "records": [{
                "input": "ကေ", "status": "OK",
                "source_coverage_complete": coverage,
                "source_coverage_status": "COMPLETE" if coverage else "PARTIAL",
                "ambiguous_dictionary_selection": randomized,
                "repetitions": [
                    {"status": "OK", "phonetic_tokens": ["kè"], "source_coverage_complete": coverage},
                    {"status": "OK", "phonetic_tokens": ["kè"], "source_coverage_complete": coverage},
                ],
            }],
        }
        epitran = {
            "engine": "epitran",
            "records": [{"orthography": "ကေ", "raw_output_ipa": "kè", "expected_ipa": "kè"}],
        }
        report = MODULE.compare_reports(goruut, epitran)
        assert report["records"][0]["goruut_source_attested_exact_match"] is None
        assert report["records"][0]["epitran_source_attested_exact_match"] is True
        assert report["accuracy"] is None
