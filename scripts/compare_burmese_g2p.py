#!/usr/bin/env python3
"""Compare Burmese Epitran and Goruut raw outputs without declaring a winner."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def compare_reports(goruut: dict[str, Any], epitran: dict[str, Any]) -> dict[str, Any]:
    if goruut.get("language_identifier") != "Burmese":
        raise ValueError("Goruut report must target Burmese")
    if epitran.get("engine") != "epitran":
        raise ValueError("Epitran report must identify engine=epitran")
    goruut_by_input = {row["input"]: row for row in goruut.get("records", [])}
    comparisons = []
    for row in epitran.get("records", []):
        text = row.get("orthography", "")
        if not text or text not in goruut_by_input:
            continue
        g = goruut_by_input[text]
        repetitions = g.get("repetitions") or [{
            "status": g.get("status"),
            "phonetic_tokens": g.get("phonetic_tokens"),
        }]
        usable = [r for r in repetitions if r.get("status") == "OK"]
        outputs = ["".join(r.get("phonetic_tokens") or []) for r in usable]
        epitran_raw = row.get("raw_output_ipa", "")
        stable = len(usable) == len(repetitions) and len(set(outputs)) == 1
        goruut_raw = outputs[0] if outputs else None
        comparisons.append({
            "orthography": text,
            "goruut_raw": goruut_raw,
            "goruut_reproducible": stable,
            "goruut_repeat_outputs": outputs,
            "epitran_raw": epitran_raw,
            "exact_string_match": bool(stable and goruut_raw == epitran_raw),
        })
    matches = sum(row["exact_string_match"] for row in comparisons)
    return {
        "schema_version": 1,
        "purpose": "Raw-output engine comparison only; neither system is treated as gold.",
        "language": "Burmese",
        "goruut_commit": goruut.get("engine_commit"),
        "epitran_version": epitran.get("engine_version"),
        "compared_inputs": len(comparisons),
        "exact_string_matches": matches,
        "different_or_unstable_outputs": len(comparisons) - matches,
        "independent_gold_count": 0,
        "accuracy": None,
        "interpretation": "Exact string agreement is not phonetic correctness. Differences may reflect transcription convention, dialect, tone/phonation representation, missing features or engine error. Do not select a winner without independent expert IPA gold.",
        "records": comparisons,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--goruut", type=Path, required=True)
    parser.add_argument("--epitran", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    goruut = json.loads(args.goruut.read_text(encoding="utf-8"))
    epitran = json.loads(args.epitran.read_text(encoding="utf-8"))
    report = compare_reports(goruut, epitran)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("compared_inputs", "exact_string_matches", "independent_gold_count", "accuracy")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
