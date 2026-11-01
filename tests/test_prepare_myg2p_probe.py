import csv
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = runpy.run_path(str(ROOT / "scripts" / "prepare_myg2p_probe.py"))


def _dictionary(path: Path) -> Path:
    path.write_text(
        "1\tက\tက\tka\tkə\n"
        "2\tခ\tခ\tkha\tkʰa\n"
        "3\tဂ\tဂ\tga\tɡa\n"
        "4\tက\tက\tka\tkə\n"
        "5\tဃ\tဃ\tgha\t\n"
        "malformed row\n",
        encoding="utf-8",
    )
    return path


def test_parser_tracks_malformed_missing_ipa_and_duplicate_rows(tmp_path):
    source = _dictionary(tmp_path / "myg2p.txt")
    entries, stats = MODULE["parse_dictionary"](source)

    assert [row["orthography"] for row in entries] == ["က", "ခ", "ဂ"]
    assert stats == {
        "physical_lines": 6,
        "malformed_rows": 1,
        "missing_ipa_rows": 1,
        "duplicate_headwords_skipped": 1,
        "unique_ipa_entries": 3,
    }


def test_evenly_spaced_selection_is_deterministic_and_covers_range():
    entries = [{"line_number": i, "orthography": str(i)} for i in range(10)]
    selected = MODULE["select_evenly_spaced"](entries, 4)

    assert [row["line_number"] for row in selected] == [0, 3, 6, 9]
    assert MODULE["select_evenly_spaced"](entries, 4) == selected


def test_prepare_probe_preserves_source_labels_and_never_marks_gold(tmp_path):
    source = _dictionary(tmp_path / "myg2p.txt")
    output = tmp_path / "probe.csv"
    summary_path = tmp_path / "summary.json"
    summary = MODULE["prepare_probe"](source, output, summary_path, limit=3)

    with output.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))

    assert len(rows) == 3
    assert rows[0]["orthography"] == "က"
    assert rows[0]["expected_ipa"] == "kə"
    assert rows[0]["evidence_status"] == "SOURCE_ATTESTED_NOT_GOLD"
    assert rows[0]["source_id"] == "myG2P-v2.0"
    assert "#L1" in rows[0]["source_locator"]
    assert summary["independent_gold_count"] == 0
    assert summary["accuracy"] is None
    assert summary["selected_count"] == 3


def test_selection_rejects_insufficient_rows_and_invalid_limit():
    entries = [{"orthography": "က"}]
    try:
        MODULE["select_evenly_spaced"](entries, 2)
    except ValueError as exc:
        assert "only 1 unique IPA entries exist" in str(exc)
    else:
        raise AssertionError("Expected insufficient input to fail")

    try:
        MODULE["select_evenly_spaced"](entries, 0)
    except ValueError as exc:
        assert "at least 1" in str(exc)
    else:
        raise AssertionError("Expected invalid limit to fail")
