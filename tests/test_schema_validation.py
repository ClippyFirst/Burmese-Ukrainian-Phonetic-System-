"""Validate the declared JSON Schemas against executable contract examples."""
import csv
import json
from pathlib import Path

from jsonschema import Draft202012Validator

from burmese_ukrainian import parse_burmese


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"


def _load_schema(name):
    schema = json.loads((SCHEMAS / name).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return schema


def test_syllable_schema_accepts_parser_records_and_malformed_statuses():
    schema = _load_schema("syllable.schema.json")
    validator = Draft202012Validator(schema)

    for text in ("ကေ", "ကြွေ", "က္", "𑛐"):
        parsed = parse_burmese(text)
        assert parsed["syllables"], text
        for syllable in parsed["syllables"]:
            errors = list(validator.iter_errors(syllable))
            assert not errors, (text, [error.message for error in errors])


def test_source_schema_is_valid_and_accepts_minimal_evidence_record():
    schema = _load_schema("source.schema.json")
    with (ROOT / "data" / "burmese" / "source_claims.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        claims = list(csv.DictReader(handle))

    claim = next(row for row in claims if row["status"] == "ESTABLISHED")
    record = {
        "claim_id": claim["claim_id"],
        "claim": claim["claim"],
        "source_id": claim["source_id"],
        "status": claim["status"],
    }
    Draft202012Validator(schema).validate(record)
