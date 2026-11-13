from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/burmese/external/mow-0.1.3-mya_20171005165336.tab"
PAIRS = ROOT / "data/burmese/mow_rime_orthographic_matches.csv"
COVERAGE = ROOT / "data/burmese/mow_rime_orthographic_coverage.csv"
GENERATOR = ROOT / "scripts/analyze_mow_orthographic_rime_coverage.py"


def read_rows(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def test_mow_source_is_attributed_and_license_is_preserved():
    first_line = SOURCE.read_text(encoding="utf-8").splitlines()[0]
    assert first_line == "## MOW 0.1.3\tmya\tCC BY 4.0"


def test_mow_orthographic_coverage_is_reproducible_and_bounded():
    result = subprocess.run(
        [sys.executable, str(GENERATOR), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr or result.stdout

    pairs = read_rows(PAIRS)
    coverage = read_rows(COVERAGE)
    assert len(pairs) == 508
    assert len(coverage) == 50
    assert len({row["lemma"] for row in pairs}) == 442
    assert len({synset for row in pairs for synset in row["synset_ids"].split(";")}) == 547
    assert len({row["source_unit"] for row in pairs}) == 35
    assert all(row["source_id"] == "MOW_2017_0_1_3_DATASET" for row in pairs + coverage)
    assert all(row["evidence_type"] == "ORTHOGRAPHIC_SUFFIX_MATCH_ONLY" for row in pairs)
    assert all("not Burmese syllabification" in row["interpretation_boundary"] for row in coverage)

    by_group = {row["mlcts"]: row["collision_group_coverage"] for row in coverage}
    assert len(by_group) == 25
    assert sum(value == "BOTH_UNITS_FOUND" for value in by_group.values()) == 11
    assert sum(value == "ONE_UNIT_FOUND" for value in by_group.values()) == 13
    assert sum(value == "NEITHER_UNIT_FOUND" for value in by_group.values()) == 1
