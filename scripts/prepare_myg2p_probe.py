#!/usr/bin/env python3
"""Prepare a deterministic, temporary myG2P v2.0 source-attested probe CSV.

This copies no dictionary entries into the repository. The output is generated
in CI from the pinned upstream dictionary and must not be treated as gold.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from typing import Any

SOURCE_REPOSITORY = "https://github.com/ye-kyaw-thu/myG2P"
SOURCE_COMMIT = "54b5c76bb5a87fdbaaeddc1892e6ebd8f97ee225"
SOURCE_PATH = "ver2/myg2p.ver2.0.txt"
CSV_FIELDS = (
    "case_id",
    "orthography",
    "expected_ipa",
    "evidence_status",
    "source_id",
    "source_locator",
    "ipa_convention",
    "scope",
    "analysis_level",
    "reviewer",
    "uncertainty_notes",
    "dictionary_word_id",
    "syllable_broken_word",
    "pronunciation",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_dictionary(path: Path) -> tuple[list[dict[str, Any]], dict[str, int]]:
    entries: list[dict[str, Any]] = []
    seen_words: set[str] = set()
    stats = {
        "physical_lines": 0,
        "malformed_rows": 0,
        "missing_ipa_rows": 0,
        "duplicate_headwords_skipped": 0,
        "unique_ipa_entries": 0,
    }
    with path.open(encoding="utf-8", newline="") as stream:
        for line_number, raw_line in enumerate(stream, start=1):
            stats["physical_lines"] += 1
            if not raw_line.strip():
                continue
            fields = raw_line.rstrip("\r\n").split("\t", 4)
            if len(fields) != 5:
                stats["malformed_rows"] += 1
                continue
            word_id, orthography, syllable_broken, pronunciation, ipa = (
                value.strip() for value in fields
            )
            if orthography.casefold() == "word" or word_id.casefold() in {"word-id", "word_id"}:
                continue
            if not orthography or not ipa or ipa.casefold() in {"null", "none", "-"}:
                stats["missing_ipa_rows"] += 1
                continue
            if orthography in seen_words:
                stats["duplicate_headwords_skipped"] += 1
                continue
            seen_words.add(orthography)
            entries.append({
                "line_number": line_number,
                "word_id": word_id,
                "orthography": orthography,
                "syllable_broken_word": syllable_broken,
                "pronunciation": pronunciation,
                "expected_ipa": ipa,
            })
    stats["unique_ipa_entries"] = len(entries)
    if not entries:
        raise ValueError(f"No unique entries with IPA labels found in {path}")
    return entries, stats


def select_evenly_spaced(
    entries: list[dict[str, Any]], limit: int
) -> list[dict[str, Any]]:
    if limit < 1:
        raise ValueError("limit must be at least 1")
    if len(entries) < limit:
        raise ValueError(f"Requested {limit} rows but only {len(entries)} unique IPA entries exist")
    if limit == 1:
        return [entries[len(entries) // 2]]
    indices = [round(index * (len(entries) - 1) / (limit - 1)) for index in range(limit)]
    if len(set(indices)) != limit:
        raise ValueError("Evenly spaced selection produced duplicate row indices")
    return [entries[index] for index in indices]


def prepare_probe(
    input_path: Path, output_path: Path, summary_path: Path, limit: int = 100
) -> dict[str, Any]:
    entries, stats = parse_dictionary(input_path)
    selected = select_evenly_spaced(entries, limit)
    rows = []
    for entry in selected:
        line_number = entry["line_number"]
        rows.append({
            "case_id": f"myg2p-v2-{entry['word_id'] or line_number}",
            "orthography": entry["orthography"],
            "expected_ipa": entry["expected_ipa"],
            "evidence_status": "SOURCE_ATTESTED_NOT_GOLD",
            "source_id": "myG2P-v2.0",
            "source_locator": (
                f"{SOURCE_REPOSITORY}/blob/{SOURCE_COMMIT}/{SOURCE_PATH}#L{line_number}"
            ),
            "ipa_convention": "myG2P v2.0 IPA field; original label preserved without normalization",
            "scope": "Dictionary headword; dialect/register profile not fully specified",
            "analysis_level": "Lexical word",
            "reviewer": "myG2P v2.0 contributor group; per-entry annotator not specified",
            "uncertainty_notes": (
                "Source-attested dictionary label, not independent project gold; "
                "per-entry adjudication protocol and dialect profile are not established."
            ),
            "dictionary_word_id": entry["word_id"],
            "syllable_broken_word": entry["syllable_broken_word"],
            "pronunciation": entry["pronunciation"],
        })

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=CSV_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "schema_version": 1,
        "source_repository": SOURCE_REPOSITORY,
        "source_commit": SOURCE_COMMIT,
        "source_path": SOURCE_PATH,
        "source_sha256": sha256_file(input_path),
        "source_license_as_declared_upstream": "CC BY-NC-SA 4.0",
        "test_only": True,
        "selection_method": "Evenly spaced over unique source-file-order entries with non-empty IPA; stable and deterministic.",
        "requested_limit": limit,
        "selected_count": len(rows),
        "selected_source_lines": [row["source_locator"] for row in rows],
        "output_path": str(output_path),
        "output_sha256": sha256_file(output_path),
        "evidence_status": "SOURCE_ATTESTED_NOT_GOLD",
        "independent_gold_count": 0,
        "accuracy": None,
        "parse_stats": stats,
    }
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--limit", type=int, default=100)
    args = parser.parse_args()
    summary = prepare_probe(args.input, args.output, args.summary, args.limit)
    print(json.dumps({
        "selected_count": summary["selected_count"],
        "source_sha256": summary["source_sha256"],
        "output_sha256": summary["output_sha256"],
        "parse_stats": summary["parse_stats"],
        "accuracy": None,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
