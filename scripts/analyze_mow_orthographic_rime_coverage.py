#!/usr/bin/env python3
"""Build a reproducible, orthography-only suffix coverage audit over MOW 0.1.3.

This deliberately performs exact Unicode string suffix matching only. It does not
segment Burmese syllables, identify phonological rimes, or adjudicate homophony.
"""
from __future__ import annotations

import argparse
import csv
import io
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "data/burmese/external/mow-0.1.3-mya_20171005165336.tab"
COLLISIONS_PATH = ROOT / "data/burmese/romanization_rime_collisions.csv"
PAIRS_PATH = ROOT / "data/burmese/mow_rime_orthographic_matches.csv"
COVERAGE_PATH = ROOT / "data/burmese/mow_rime_orthographic_coverage.csv"
SOURCE_ID = "MOW_2017_0_1_3_DATASET"

PAIR_FIELDS = [
    "mlcts", "source_unit", "lemma", "synset_ids", "synset_count",
    "source_id", "evidence_type",
]
COVERAGE_FIELDS = [
    "mlcts", "source_unit", "distinct_lemma_matches",
    "distinct_synset_matches", "sample_lemmas", "collision_group_coverage",
    "source_id", "interpretation_boundary",
]
BOUNDARY = (
    "Exact Unicode code-point suffix match against MOW orthographic lemmas only; "
    "not Burmese syllabification, pronunciation evidence, MLCTS adjudication, "
    "homophony proof, or Ukrainian transcription evidence."
)


def read_mow_lemmas(path: Path) -> dict[str, set[str]]:
    """Return lemma -> synset IDs, retaining distinct synset membership."""
    lemma_synsets: dict[str, set[str]] = defaultdict(set)
    with path.open(encoding="utf-8", newline="") as stream:
        for line_no, line in enumerate(stream, start=1):
            line = line.rstrip("\r\n")
            if not line or line.startswith("##"):
                continue
            fields = line.split("\t")
            if len(fields) != 3:
                raise ValueError(f"{path}:{line_no}: expected 3 tab-separated fields")
            synset_id, form_type, lemma = fields
            if form_type == "mya:lemma":
                lemma_synsets[lemma].add(synset_id)
    return dict(lemma_synsets)


def read_collision_groups(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    if not rows:
        raise ValueError(f"No collision groups found in {path}")
    return rows


def build_outputs(source_path: Path = SOURCE_PATH, collisions_path: Path = COLLISIONS_PATH):
    lemma_synsets = read_mow_lemmas(source_path)
    groups = read_collision_groups(collisions_path)
    pair_rows: list[dict[str, str]] = []
    coverage_rows: list[dict[str, str]] = []

    for group in groups:
        mlcts = group["mlcts"]
        units = group["source_units"].split(";")
        matches_by_unit: dict[str, list[str]] = {}
        synsets_by_unit: dict[str, set[str]] = {}

        for unit in units:
            matches = sorted(lemma for lemma in lemma_synsets if lemma.endswith(unit))
            matches_by_unit[unit] = matches
            matched_synsets: set[str] = set()
            for lemma in matches:
                synset_ids = sorted(lemma_synsets[lemma])
                matched_synsets.update(synset_ids)
                pair_rows.append({
                    "mlcts": mlcts,
                    "source_unit": unit,
                    "lemma": lemma,
                    "synset_ids": ";".join(synset_ids),
                    "synset_count": str(len(synset_ids)),
                    "source_id": SOURCE_ID,
                    "evidence_type": "ORTHOGRAPHIC_SUFFIX_MATCH_ONLY",
                })
            synsets_by_unit[unit] = matched_synsets

        found_count = sum(bool(matches_by_unit[unit]) for unit in units)
        if found_count == len(units):
            group_status = "BOTH_UNITS_FOUND"
        elif found_count:
            group_status = "ONE_UNIT_FOUND"
        else:
            group_status = "NEITHER_UNIT_FOUND"

        for unit in units:
            matches = matches_by_unit[unit]
            coverage_rows.append({
                "mlcts": mlcts,
                "source_unit": unit,
                "distinct_lemma_matches": str(len(matches)),
                "distinct_synset_matches": str(len(synsets_by_unit[unit])),
                "sample_lemmas": ";".join(matches[:5]),
                "collision_group_coverage": group_status,
                "source_id": SOURCE_ID,
                "interpretation_boundary": BOUNDARY,
            })

    pair_rows.sort(key=lambda row: (row["mlcts"], row["source_unit"], row["lemma"]))
    coverage_rows.sort(key=lambda row: (row["mlcts"], row["source_unit"]))
    return pair_rows, coverage_rows


def csv_text(rows: list[dict[str, str]], fields: list[str]) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if committed outputs are stale")
    args = parser.parse_args()

    pairs, coverage = build_outputs()
    outputs = (
        (PAIRS_PATH, csv_text(pairs, PAIR_FIELDS)),
        (COVERAGE_PATH, csv_text(coverage, COVERAGE_FIELDS)),
    )
    if args.check:
        stale = [str(path.relative_to(ROOT)) for path, expected in outputs
                 if not path.exists() or path.read_text(encoding="utf-8") != expected]
        if stale:
            print("MOW orthographic coverage outputs are stale: " + ", ".join(stale), file=sys.stderr)
            return 1
        print(
            f"MOW orthographic coverage is fresh: {len(pairs)} source-unit/lemma pairs; "
            f"{len(coverage)} source-unit rows."
        )
        return 0

    for path, content in outputs:
        path.write_text(content, encoding="utf-8", newline="")
        print(f"Wrote {path.relative_to(ROOT)} ({len(content)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
