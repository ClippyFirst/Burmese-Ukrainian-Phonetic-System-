#!/usr/bin/env python3
"""Run a pinned Google Burmese WFST G2P raw-output smoke test.

The current repository probe corpus is structural-only and contains no
adjudicated IPA labels. This runner deliberately reports execution evidence,
not phonological accuracy, and refuses labelled/non-structural rows.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ENGINE_SOURCE_COMMIT = "a90601024f07ab7e96c911243324e0adeb16da96"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = ROOT / "data" / "burmese" / "phonology_corpus.csv"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_probe_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        required = {"case_id", "orthography", "evidence_status", "expected_ipa"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(
                "probe CSV must contain case_id, orthography, evidence_status and expected_ipa"
            )
        rows = list(reader)
    if not rows:
        raise ValueError("probe CSV contains no rows")
    if any(not row["orthography"].strip() for row in rows):
        raise ValueError("probe CSV contains an empty orthography")
    return rows


def parse_outputs(stdout: str, expected_count: int) -> list[str]:
    outputs = [line.rstrip("\r") for line in stdout.splitlines()]
    if len(outputs) != expected_count:
        raise ValueError(
            f"expected {expected_count} output lines, received {len(outputs)}"
        )
    return outputs


def run_engine(binary: Path, rows: list[dict[str, str]]) -> tuple[list[str], str]:
    if not binary.is_file():
        raise FileNotFoundError(f"Google G2P binary not found: {binary}")
    input_text = "\n".join(row["orthography"] for row in rows) + "\n"
    result = subprocess.run(
        [str(binary.resolve())],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return parse_outputs(result.stdout, len(rows)), result.stderr


def build_report(
    rows: list[dict[str, str]],
    outputs: list[str],
    *,
    engine_source_commit: str,
    grammar_sha256: str,
    phoneme_symbols_sha256: str,
    fst_sha256: str,
    bazel_version: str,
    corpus_sha256: str,
    stderr: str = "",
) -> dict[str, Any]:
    if len(rows) != len(outputs):
        raise ValueError("expected one output per input")
    if not rows:
        raise ValueError("cannot run an empty probe")
    for row in rows:
        if row.get("evidence_status") != "STRUCTURAL_ONLY":
            raise ValueError(
                "Google FST raw-output smoke accepts STRUCTURAL_ONLY rows only"
            )
        if row.get("expected_ipa", "").strip():
            raise ValueError(
                "Google FST raw-output smoke refuses rows with expected_ipa labels"
            )

    records = []
    for row, output in zip(rows, outputs, strict=True):
        records.append({
            "case_id": row["case_id"],
            "orthography": row["orthography"],
            "raw_output": output,
            "output_nonempty": bool(output.strip()),
            "evidence_status": "STRUCTURAL_ONLY",
            "score_status": "NOT_SCORED_NO_INDEPENDENT_GOLD",
        })

    successful_outputs = sum(item["output_nonempty"] for item in records)
    return {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "engine": "google/language-resources Burmese Thrax/OpenFst WFST",
        "engine_source_commit": engine_source_commit,
        "engine_output_claim": (
            "The upstream LREC 2020 paper describes the FST output tape as IPA; "
            "the project's own IPA profile has not been independently validated."
        ),
        "corpus": "data/burmese/phonology_corpus.csv",
        "corpus_sha256": corpus_sha256,
        "input_count": len(rows),
        "output_count": len(outputs),
        "successful_outputs": successful_outputs,
        "failed_outputs": len(rows) - successful_outputs,
        "runtime_errors": 0,
        "independent_gold_count": 0,
        "accuracy": None,
        "score_status": "RAW_OUTPUT_SMOKE_NOT_ACCURACY",
        "provenance": {
            "engine_source_commit": engine_source_commit,
            "grammar_sha256": grammar_sha256,
            "phoneme_symbols_sha256": phoneme_symbols_sha256,
            "fst_sha256": fst_sha256,
            "bazel_version": bazel_version,
            "harness_path": "scripts/benchmark_google_fst.py",
            "harness_sha256": sha256_file(Path(__file__).resolve()),
            "python_version": platform.python_version(),
            "python_implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "github_event_sha": os.environ.get("GITHUB_SHA"),
            "github_ref": os.environ.get("GITHUB_REF"),
            "github_head_ref": os.environ.get("GITHUB_HEAD_REF"),
        },
        "stderr": stderr,
        "records": records,
        "limitations": [
            "The six repository inputs are structural-only probes, not pronunciation gold.",
            "No PER, CER, exact-match accuracy or IPA accuracy can be computed from this corpus.",
            "The upstream paper reports IPA output, but no independent adjudication for this project's Standard Burmese profile exists.",
            "The upstream repository is pinned to a source commit; its WORKSPACE contains upstream dependency references that are not all content-address pinned.",
            "This smoke verifies build and execution only, not tone/register/phonation or dialect accuracy.",
        ],
    }


def write_report(path: Path, report: dict[str, Any]) -> str:
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(rendered, encoding="utf-8")
    digest = sha256_file(path)
    path.with_suffix(path.suffix + ".sha256").write_text(digest + "\n", encoding="ascii")
    return digest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--binary", type=Path, required=True)
    parser.add_argument("--grammar", type=Path, required=True)
    parser.add_argument("--phoneme-symbols", type=Path, required=True)
    parser.add_argument("--fst", type=Path, required=True)
    parser.add_argument("--bazel-version", required=True)
    parser.add_argument("--engine-source-commit", default=ENGINE_SOURCE_COMMIT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    rows = read_probe_rows(args.corpus)
    outputs, stderr = run_engine(args.binary, rows)
    report = build_report(
        rows,
        outputs,
        engine_source_commit=args.engine_source_commit,
        grammar_sha256=sha256_file(args.grammar),
        phoneme_symbols_sha256=sha256_file(args.phoneme_symbols),
        fst_sha256=sha256_file(args.fst),
        bazel_version=args.bazel_version,
        corpus_sha256=sha256_file(args.corpus),
        stderr=stderr,
    )
    report_sha256 = write_report(args.output, report)
    print(json.dumps({
        "input_count": report["input_count"],
        "successful_outputs": report["successful_outputs"],
        "runtime_errors": report["runtime_errors"],
        "independent_gold_count": 0,
        "accuracy": None,
        "report_sha256": report_sha256,
        "output": str(args.output),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
