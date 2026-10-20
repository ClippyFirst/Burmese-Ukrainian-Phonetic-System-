#!/usr/bin/env python3
"""Run an optional, raw-output Epitran baseline without treating it as gold.

Install Epitran separately (for example, in a disposable virtual environment),
then run: python scripts/benchmark_g2p.py --engine epitran --output benchmark.json

No third-party map files or lexical entries are copied into this repository.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.metadata
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = ROOT / "data" / "burmese" / "phonology_corpus.csv"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_corpus(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def build_report(
    rows: list[dict[str, str]],
    outputs: list[str],
    *,
    engine: str,
    engine_version: str,
    corpus_sha256: str,
    mapping_sha256: str | None,
) -> dict[str, Any]:
    if len(rows) != len(outputs):
        raise ValueError("There must be exactly one raw engine output per corpus row.")

    records = []
    eligible_gold = 0
    exact_matches = 0
    for row, raw_output in zip(rows, outputs, strict=True):
        is_gold = (
            row.get("evidence_status") == "GOLD_VERIFIED"
            and bool(row.get("expected_ipa", "").strip())
            and bool(row.get("source_id", "").strip())
            and bool(row.get("source_locator", "").strip())
            and "pending" not in row.get("source_locator", "").lower()
        )
        match = None
        score_status = "NOT_SCORED_NO_VERIFIED_GOLD"
        if is_gold:
            eligible_gold += 1
            match = raw_output == row["expected_ipa"].strip()
            exact_matches += int(match)
            score_status = "SCORED_EXACT_MATCH" if match else "SCORED_MISMATCH"

        records.append(
            {
                "case_id": row.get("case_id", ""),
                "orthography": row.get("orthography", ""),
                "evidence_status": row.get("evidence_status", ""),
                "source_id": row.get("source_id", ""),
                "source_locator": row.get("source_locator", ""),
                "expected_ipa": row.get("expected_ipa", ""),
                "raw_output_ipa": raw_output,
                "exact_match": match,
                "score_status": score_status,
            }
        )

    return {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "engine": engine,
        "engine_version": engine_version,
        "python_version": platform.python_version(),
        "corpus_path": str(DEFAULT_CORPUS.relative_to(ROOT)),
        "corpus_sha256": corpus_sha256,
        "mapping_sha256": mapping_sha256,
        "eligible_verified_gold_count": eligible_gold,
        "exact_match_count": exact_matches if eligible_gold else None,
        "exact_match_accuracy": (exact_matches / eligible_gold) if eligible_gold else None,
        "note": (
            "Raw external output only. Structural probes are not gold data. "
            "Accuracy is null until independently source-located GOLD_VERIFIED rows exist."
        ),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--engine", choices=("epitran",), default="epitran")
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--output", type=Path, help="Write JSON here; default prints to stdout.")
    args = parser.parse_args()

    try:
        import epitran
    except ImportError:
        parser.error(
            "Epitran is optional and is not installed. Install it in a separate environment; "
            "this project intentionally does not add it as a runtime dependency."
        )

    rows = load_corpus(args.corpus)
    transducer = epitran.Epitran("mya-Mymr")
    raw_outputs = [transducer.transliterate(row["orthography"]) for row in rows]

    try:
        version = importlib.metadata.version("epitran")
    except importlib.metadata.PackageNotFoundError:
        version = "unknown"

    mapping_sha256 = None
    try:
        import importlib.resources

        mapping = importlib.resources.files("epitran").joinpath("data/map/mya-Mymr.csv")
        if mapping.is_file():
            mapping_sha256 = hashlib.sha256(mapping.read_bytes()).hexdigest()
    except (AttributeError, FileNotFoundError, ModuleNotFoundError):
        pass

    report = build_report(
        rows,
        raw_outputs,
        engine=args.engine,
        engine_version=version,
        corpus_sha256=sha256_file(args.corpus),
        mapping_sha256=mapping_sha256,
    )
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
