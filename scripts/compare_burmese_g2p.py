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
        expected_ipa = row.get("expected_ipa", "").strip()
        source_coverage_complete = g.get("source_coverage_complete") is True
        ambiguous_dictionary_selection = g.get("ambiguous_dictionary_selection") is True
        goruut_source_comparable = bool(
            expected_ipa and stable and source_coverage_complete
            and not ambiguous_dictionary_selection
        )
        goruut_source_match = (
            goruut_raw == expected_ipa if goruut_source_comparable else None
        )
        epitran_source_match = (
            epitran_raw == expected_ipa if expected_ipa else None
        )
        comparisons.append({
            "orthography": text,
            "source_attested_ipa": expected_ipa or None,
            "goruut_raw": goruut_raw,
            "goruut_reproducible": stable,
            "goruut_source_coverage_status": g.get("source_coverage_status", "UNKNOWN"),
            "goruut_ambiguous_dictionary_selection": ambiguous_dictionary_selection,
            "goruut_repeat_outputs": outputs,
            "epitran_raw": epitran_raw,
            "exact_string_match": bool(stable and goruut_raw == epitran_raw),
            "goruut_source_attested_exact_match": goruut_source_match,
            "epitran_source_attested_exact_match": epitran_source_match,
        })
    matches = sum(row["exact_string_match"] for row in comparisons)
    source_rows = [row for row in comparisons if row["source_attested_ipa"]]
    source_diagnostic = {
        "source_attested_inputs": len(source_rows),
        "goruut_complete_deterministic_inputs": sum(
            row["goruut_source_attested_exact_match"] is not None for row in source_rows
        ),
        "goruut_exact_matches": sum(
            row["goruut_source_attested_exact_match"] is True for row in source_rows
        ),
        "epitran_exact_matches": sum(
            row["epitran_source_attested_exact_match"] is True for row in source_rows
        ),
        "status": "SOURCE_ATTESTED_CONCORDANCE_ONLY_NOT_GOLD",
        "interpretation": (
            "myG2P v2.0 dictionary labels are source-attested, not independent project gold. "
            "Goruut rows are compared only when all repeats are stable, source coverage is complete, "
            "and no upstream dictionary-randomization counters are present. These are not accuracy scores."
        ),
    }
    return {
        "schema_version": 1,
        "purpose": "Raw-output engine comparison only; neither system is treated as gold.",
        "language": "Burmese",
        "goruut_commit": goruut.get("engine_commit"),
        "epitran_version": epitran.get("engine_version"),
        "compared_inputs": len(comparisons),
        "exact_string_matches": matches,
        "different_or_unstable_outputs": len(comparisons) - matches,
        "source_attested_diagnostic": source_diagnostic,
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
