#!/usr/bin/env python3
"""Run a raw-output smoke probe against the published Burmese CRFsuite model.

The probe uses source-attested myG2P rows only to exercise the model. The
model's training membership is not known and may overlap this dictionary, so
this script deliberately reports no accuracy or gold score.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path
from typing import Any

MODEL_SOURCE_COMMIT = "de0f06056cf334b8cdd5a1efd1226f01c8162b77"
CRFSUITE_SOURCE_COMMIT = "a2a1547727985e3aff6a35cffe073f57f0223e9d"
DATA_SOURCE_COMMIT = "54b5c76bb5a87fdbaaeddc1892e6ebd8f97ee225"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    required = {"case_id", "orthography", "expected_ipa", "syllable_broken_word"}
    missing = required - set(rows[0] if rows else [])
    if missing:
        raise ValueError(f"probe CSV missing required columns: {', '.join(sorted(missing))}")
    if not rows:
        raise ValueError("probe CSV contains no rows")
    return rows


def build_feature_input(
    rows: list[dict[str, str]],
) -> tuple[str, list[dict[str, Any]], list[dict[str, str]]]:
    """Build one CRFsuite sequence per lexical row; retain unsegmentable rows."""
    chunks: list[str] = []
    prepared: list[dict[str, Any]] = []
    skipped: list[dict[str, str]] = []
    for row in rows:
        syllables = row["syllable_broken_word"].split()
        if not syllables:
            skipped.append({
                "case_id": row["case_id"],
                "reason": "MISSING_SYLLABLE_SEGMENTATION",
            })
            continue
        chunks.extend(f"{syllable} {syllable} ?" for syllable in syllables)
        chunks.append("")
        prepared.append({
            "case_id": row["case_id"],
            "orthography": row["orthography"],
            "source_ipa": row["expected_ipa"],
            "syllables": syllables,
        })
    if not prepared:
        raise ValueError("no probe rows contain syllable-broken orthography")
    return "\n".join(chunks) + "\n", prepared, skipped


def parse_prediction_sequences(output: str) -> list[list[str]]:
    sequences: list[list[str]] = []
    current: list[str] = []
    for line in output.splitlines():
        label = line.strip()
        if label:
            current.append(label)
        elif current:
            sequences.append(current)
            current = []
    if current:
        sequences.append(current)
    return sequences


def nfc(value: str) -> str:
    return unicodedata.normalize("NFC", value.strip())


def run_probe(
    input_csv: Path,
    model_path: Path,
    chunking_script: Path,
    crfsuite_bin: str,
    crfsuite_example_dir: Path,
    output_path: Path,
) -> dict[str, Any]:
    rows = read_rows(input_csv)
    feature_input, prepared, skipped = build_feature_input(rows)

    env = os.environ.copy()
    existing_pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = os.pathsep.join(
        part for part in (str(crfsuite_example_dir), existing_pythonpath) if part
    )
    features = subprocess.run(
        [sys.executable, str(chunking_script)],
        input=feature_input,
        text=True,
        capture_output=True,
        check=True,
        env=env,
    )

    with tempfile.TemporaryDirectory(prefix="burmese-crf-probe-") as temp_dir:
        feature_path = Path(temp_dir) / "probe.features"
        feature_path.write_text(features.stdout, encoding="utf-8")
        tagged = subprocess.run(
            [crfsuite_bin, "tag", "-m", str(model_path), str(feature_path)],
            text=True,
            capture_output=True,
            check=True,
            env=env,
        )

    sequences = parse_prediction_sequences(tagged.stdout)
    if len(sequences) != len(prepared):
        raise ValueError(
            f"CRFsuite returned {len(sequences)} sequences for {len(prepared)} inputs"
        )

    records = []
    for row, prediction in zip(prepared, sequences, strict=True):
        if len(prediction) != len(row["syllables"]):
            raise ValueError(
                f"{row['case_id']}: predicted {len(prediction)} labels for "
                f"{len(row['syllables'])} input syllables"
            )
        predicted_ipa = " ".join(prediction)
        source_ipa = row["source_ipa"]
        records.append({
            "case_id": row["case_id"],
            "orthography": row["orthography"],
            "input_syllables": len(row["syllables"]),
            "predicted_syllables": len(prediction),
            "predicted_ipa": predicted_ipa,
            "source_ipa": source_ipa,
            "source_concordant": bool(source_ipa) and nfc(predicted_ipa) == nfc(source_ipa),
            "evidence_status": "SOURCE_ATTESTED_NOT_GOLD",
        })

    report = {
        "schema_version": "1.0",
        "engine": "kyaw-yethu/burmese-G2P CRFsuite ver2",
        "model_source_commit": MODEL_SOURCE_COMMIT,
        "model_sha256": sha256_file(model_path),
        "crfsuite_source_commit": CRFSUITE_SOURCE_COMMIT,
        "data_source_commit": DATA_SOURCE_COMMIT,
        "probe_input_sha256": sha256_file(input_csv),
        "input_rows": len(rows),
        "rows_with_syllable_segmentation": len(prepared),
        "rows_skipped": len(skipped),
        "predictions_returned": len(records),
        "source_concordant_rows": sum(item["source_concordant"] for item in records),
        "gold_count": 0,
        "accuracy": None,
        "scoring_status": "NOT_SCORED_POSSIBLE_TRAINING_OVERLAP",
        "limitations": [
            "The model's exact training membership is not established.",
            "The model and probe labels derive from related myG2P resources, so train/test leakage is possible.",
            "The upstream README acknowledges sentence-level errors for particles and postpositional markers.",
            "The source IPA is not independently adjudicated for this project's Standard Burmese profile.",
            "Source concordance is a diagnostic only and is not an accuracy score.",
        ],
        "skipped_rows": skipped,
        "records": records,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--chunking-script", type=Path, required=True)
    parser.add_argument("--crfsuite-example-dir", type=Path, required=True)
    parser.add_argument("--crfsuite-bin", default="crfsuite")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = run_probe(
        args.input,
        args.model,
        args.chunking_script,
        args.crfsuite_bin,
        args.crfsuite_example_dir,
        args.output,
    )
    print(json.dumps({
        "input_rows": report["input_rows"],
        "predictions_returned": report["predictions_returned"],
        "source_concordant_rows": report["source_concordant_rows"],
        "gold_count": report["gold_count"],
        "accuracy": report["accuracy"],
        "scoring_status": report["scoring_status"],
        "output": str(args.output),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
