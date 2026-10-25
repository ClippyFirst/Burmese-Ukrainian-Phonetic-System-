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
        "evidence_type": claim["evidence_type"],
        "scope": claim["scope"],
        "status": claim["status"],
    }
    Draft202012Validator(schema).validate(record)


def test_all_canonical_evidence_registries_validate_against_schemas():
    """Validate every source, claim and implemented rule, not one sample claim."""
    source_schema = _load_schema("source_record.schema.json")
    claim_schema = _load_schema("source.schema.json")
    rule_schema = _load_schema("phonological_rule.schema.json")

    def read_csv(name):
        with (ROOT / "data" / "burmese" / name).open(encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))

    sources = read_csv("sources.csv")
    claims = read_csv("source_claims.csv")
    rules = read_csv("phonological_rules.csv")

    assert sources and claims and rules
    for schema, rows, kind in (
        (source_schema, sources, "source"),
        (claim_schema, claims, "claim"),
        (rule_schema, rules, "rule"),
    ):
        validator = Draft202012Validator(schema)
        for index, row in enumerate(rows, start=2):
            errors = sorted(validator.iter_errors(row), key=lambda error: list(error.path))
            assert not errors, (kind, index, row, [error.message for error in errors])

    source_ids = [row["source_id"] for row in sources]
    claim_ids = [row["claim_id"] for row in claims]
    rule_ids = [row["rule_id"] for row in rules]
    assert len(source_ids) == len(set(source_ids)), "source IDs must be unique"
    assert len(claim_ids) == len(set(claim_ids)), "claim IDs must be unique"
    assert len(rule_ids) == len(set(rule_ids)), "rule IDs must be unique"

    sources_by_id = {row["source_id"]: row for row in sources}
    claims_by_id = {row["claim_id"]: row for row in claims}
    for claim in claims:
        assert claim["source_id"] in sources_by_id, claim["claim_id"]
    for rule in rules:
        assert rule["source_id"] in sources_by_id, rule["rule_id"]
        assert rule["claim_id"] in claims_by_id, rule["rule_id"]
        assert claims_by_id[rule["claim_id"]]["source_id"] == rule["source_id"], rule["rule_id"]
