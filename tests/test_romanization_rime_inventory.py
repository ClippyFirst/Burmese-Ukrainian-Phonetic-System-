from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data/burmese/romanization_rimes_inventory.csv"
SOURCE = "https://github.com/myanmaropenwordnet/mya2rom"


def test_vendor_mlcts_rime_inventory_is_explicit_and_provenanced():
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 94
    assert len({row["source_unit"] for row in rows}) == len(rows)
    assert all(row["mlcts"] for row in rows)
    assert all(row["ukrainian_status"] == "PROPOSED" for row in rows)
    assert all(row["ukrainian_candidate"] for row in rows)
    assert all(row["romanization_evidence_status"] == "EVIDENCE_LIMITED" for row in rows)
    assert all(row["source_url"] == SOURCE for row in rows)
    assert all("romanisations.js" in row["source_locator"] for row in rows)
    assert all("vendored Mya2Rom inventory" in row["note"] for row in rows)



UKRAINIAN_UNITS = {"ng": "нг", "ny": "нь", "ai": "ай", "au": "ау", "ui": "уй", ":": "ː", ".": "·", "'": "ʼ", "a": "а", "c": "ц", "e": "е", "g": "ґ", "i": "і", "k": "к", "m": "м", "n": "н", "p": "п", "t": "т", "u": "у", "w": "в", "y": "й"}


def render_mlcts(value: str) -> str:
    result = ""
    index = 0
    while index < len(value):
        digraph = next((unit for unit in ("ng", "ny", "ai", "au", "ui") if value.startswith(unit, index)), None)
        if digraph:
            result += UKRAINIAN_UNITS[digraph]
            index += len(digraph)
        else:
            result += UKRAINIAN_UNITS[value[index]]
            index += 1
    return result


def test_all_94_vendor_rimes_have_complete_deterministic_ukrainian_renderings():
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    for row in rows:
        assert row["ukrainian_candidate"] == render_mlcts(row["mlcts"])
        assert row["ukrainian_status"] == "PROPOSED"
        assert row["romanization_evidence_status"] == "EVIDENCE_LIMITED"


def test_all_94_inventory_keys_match_the_vendored_mya2rom_mlcts_column():
    import re

    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    vendor_path = ROOT / "vendor/mya2rom/romanisations.js"
    vendor_text = vendor_path.read_text(encoding="utf-8")
    match = re.search(r"var vowels = \{([\s\S]*?)\n\}", vendor_text)
    assert match is not None
    vendor_rows = {}
    for key, values_text in re.findall(r'^\s*"([^"]*)"\s*:\s*\[([^\]]+)\]', match.group(1), re.MULTILINE):
        values = re.findall(r'"([^"]*)"', values_text)
        vendor_rows[key] = values

    assert len(vendor_rows) == 95
    assert "" in vendor_rows  # upstream empty-key fallback is not a Myanmar rime key
    assert len(rows) == 94
    for row in rows:
        assert row["source_unit"] in vendor_rows
        assert vendor_rows[row["source_unit"]][1] == row["mlcts"]


def test_mlcts_rime_collision_audit_preserves_distinct_source_units():
    collision_path = ROOT / "data/burmese/romanization_rime_collisions.csv"
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        rimes = {row["source_unit"]: row for row in csv.DictReader(stream)}
    with collision_path.open(encoding="utf-8-sig", newline="") as stream:
        collisions = list(csv.DictReader(stream))

    assert len(collisions) == 25
    assert all(row["audit_status"] == "ORTHOGRAPHIC_COLLISION_REQUIRES_PRIMARY_SOURCE_REVIEW" for row in collisions)
    for collision in collisions:
        source_units = collision["source_units"].split(";")
        assert len(source_units) == int(collision["collision_size"]) == 2
        assert len(set(source_units)) == 2
        assert all(source_unit in rimes for source_unit in source_units)
        assert all(rimes[source_unit]["mlcts"] == collision["mlcts"] for source_unit in source_units)
        assert all(rimes[source_unit]["ukrainian_candidate"] == collision["ukrainian_candidate"] for source_unit in source_units)


def test_auk_myit_special_mapping_is_not_misread_as_an_ordinary_rime():
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        rows = {row["source_unit"]: row for row in csv.DictReader(stream)}
    row = rows["့"]
    assert "auk-myit-induced creaky-tone" in row["context"]
    assert "not an ordinary independent rime" in row["context"]
    assert "do not interpret it as an independent vowel or coda" in row["note"]


LEXICAL_AUDIT_PATH = ROOT / "data/burmese/romanization_rime_collision_lexical_audit.csv"


def test_lexical_collision_audit_keeps_secondary_evidence_separate_from_primary_adjudication():
    collision_path = ROOT / "data/burmese/romanization_rime_collisions.csv"
    with collision_path.open(encoding="utf-8-sig", newline="") as stream:
        collisions = {row["mlcts"]: row for row in csv.DictReader(stream)}
    with LEXICAL_AUDIT_PATH.open(encoding="utf-8-sig", newline="") as stream:
        audit = list(csv.DictReader(stream))

    assert len(audit) == len(collisions) == 25
    assert {row["mlcts"] for row in audit} == set(collisions)
    for row in audit:
        assert row["source_units"] == collisions[row["mlcts"]]["source_units"]
        assert row["acceptance_boundary"]
        assert row["evidence_status"] in {
            "UNADJUDICATED_NO_WORD_LEVEL_EVIDENCE",
            "SECONDARY_SYSTEM_EQUIVALENCE",
            "SECONDARY_SOURCE_CONFLICT",
            "SECONDARY_SOURCE_DISTINCTION",
            "SECONDARY_ONE_SIDE_ONLY",
            "SPECIAL_NONRIME_CONTEXT_DEPENDENT",
        }

    by_mlcts = {row["mlcts"]: row for row in audit}
    assert by_mlcts["am"]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert by_mlcts["am"]["observed_ipa"] == "/kàɴ/"
    assert by_mlcts["am"]["observed_mlcts"] == "kam"
    assert by_mlcts["any"]["evidence_status"] == "SECONDARY_SOURCE_CONFLICT"
    assert "kañ" in by_mlcts["any"]["observed_mlcts"]
    assert "kany" in by_mlcts["any"]["observed_mlcts"]
    assert "R12A" in by_mlcts["any"]["source_locator"]
    assert "not nasalised" in by_mlcts["any"]["interpretation"]
    assert "secondary-source conflict remains" in by_mlcts["any"]["interpretation"]
    assert by_mlcts["any:"]["evidence_status"] == "SECONDARY_SOURCE_DISTINCTION"
    assert "/ʔət͡ɕɪ́ɴ/" in by_mlcts["any:"]["observed_ipa"]
    assert "/nɛ́/" in by_mlcts["any:"]["observed_ipa"]
    assert "CLM-WIKTIONARY-ANY-COLON-WORD-LEVEL-EXAMPLES-001" in by_mlcts["any:"]["source_locator"] or "Wiktionary" in by_mlcts["any:"]["source_locator"]
    assert by_mlcts["ui"]["evidence_status"] == "SECONDARY_ONE_SIDE_ONLY"
    assert "/d͡ʑò/" in by_mlcts["ui"]["observed_ipa"]
    assert "first source unit" in by_mlcts["ui"]["interpretation"]
    assert by_mlcts["u."]["evidence_status"] == "SPECIAL_NONRIME_CONTEXT_DEPENDENT"
    assert by_mlcts["um"]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert by_mlcts["um"]["observed_ipa"] == "/kòʊɴ/"
    assert by_mlcts["um"]["observed_mlcts"] == "kum"
    assert by_mlcts["un"]["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE"
    assert "/ɡòʊɴ/" in by_mlcts["un"]["observed_ipa"]
    assert "/kòʊɴ/" in by_mlcts["un"]["observed_ipa"]
    assert sum(row["evidence_status"] == "UNADJUDICATED_NO_WORD_LEVEL_EVIDENCE" for row in audit) == 0
    assert sum(row["evidence_status"] == "SECONDARY_SYSTEM_EQUIVALENCE" for row in audit) == 10
    assert sum(row["evidence_status"] == "SECONDARY_SOURCE_CONFLICT" for row in audit) == 1
    assert sum(row["evidence_status"] == "SECONDARY_SOURCE_DISTINCTION" for row in audit) == 3
    assert sum(row["evidence_status"] == "SECONDARY_ONE_SIDE_ONLY" for row in audit) == 10
    assert sum(row["evidence_status"] == "SPECIAL_NONRIME_CONTEXT_DEPENDENT" for row in audit) == 1
    assert not any("PRIMARY_CONFIRMED" in row["evidence_status"] for row in audit)

def test_mlcts_source_provenance_does_not_conflate_secondary_sources_or_ala_lc():
    sources_path = ROOT / "data/burmese/sources.csv"
    claims_path = ROOT / "data/burmese/source_claims.csv"
    with sources_path.open(encoding="utf-8-sig", newline="") as stream:
        sources = {row["source_id"]: row for row in csv.DictReader(stream) if row.get("source_id")}
    with claims_path.open(encoding="utf-8-sig", newline="") as stream:
        claims = {row["claim_id"]: row for row in csv.DictReader(stream) if row.get("claim_id")}

    assert "OHNMAR_HTUN_2013" in sources
    assert "ALA_LC_BURMESE_2011" in sources
    assert "UNICODE_REFERENCE_LISTS_2022" in sources
    assert "WHO_MLC1993_DICT_CATALOG" in sources
    assert "NDL_MLC1996_DICT_CATALOG" in sources
    assert "BURMA_DEBATE_1996_MLC_DICT_NOTICE" in sources
    assert "MOW_2017_MLCTS_VARIANTS" in sources
    assert "ALLOTT1985_BURMA_LANGUAGE_POLICY" in sources
    assert "OKELL1982_BURMESE_DICTIONARY_REVIEW" in sources
    assert sources["OHNMAR_HTUN_2013"]["type"] == "doctoral_dissertation"
    assert "not a primary MLCTS specification" in sources["OHNMAR_HTUN_2013"]["scope"]
    assert "ALA-LC" in sources["ALA_LC_BURMESE_2011"]["scope"]
    assert claims["CLM-MLCTS-SECONDARY-PROVENANCE-001"]["source_id"] == "OHNMAR_HTUN_2013"
    assert claims["CLM-ALA-LC-NOT-MLCTS-001"]["source_id"] == "ALA_LC_BURMESE_2011"
    assert claims["CLM-MLC-DICT-BIB-UNICODE-001"]["source_id"] == "UNICODE_REFERENCE_LISTS_2022"
    assert claims["CLM-MLC-DICT-1993-PHYSICAL-HOLDING-001"]["source_id"] == "WHO_MLC1993_DICT_CATALOG"
    assert claims["CLM-MLC-DICT-1996-NDL-HOLDING-001"]["source_id"] == "NDL_MLC1996_DICT_CATALOG"
    assert claims["CLM-MLC-DICT-PRON-GUIDE-001"]["source_id"] == "BURMA_DEBATE_1996_MLC_DICT_NOTICE"
    assert claims["CLM-MOW-MLCTS2-VARIANTS-001"]["source_id"] == "MOW_2017_MLCTS_VARIANTS"
    assert claims["CLM-MYA2ROM-COLUMN3-NAMING-001"]["source_id"] == "MYA2ROM044"
    assert claims["CLM-MLC-CONCISE-DICT-1978-80-001"]["source_id"] == "ALLOTT1985_BURMA_LANGUAGE_POLICY"
    assert claims["CLM-MLC-CONCISE-DICT-BIB-001"]["source_id"] == "OKELL1982_BURMESE_DICTIONARY_REVIEW"
    assert "Wikipedia" in claims["CLM-MLCTS-SECONDARY-PROVENANCE-001"]["claim"]
    assert "not the Myanmar Language Commission" in claims["CLM-ALA-LC-NOT-MLCTS-001"]["claim"]
    assert "does not expose their entry text" in claims["CLM-MLC-DICT-BIB-UNICODE-001"]["claim"]
    assert "not access to the dictionary contents" in claims["CLM-MLC-DICT-1993-PHYSICAL-HOLDING-001"]["claim"]
    assert "not an online scan" in claims["CLM-MLC-DICT-1996-NDL-HOLDING-001"]["claim"]
    assert "does not identify the system" in claims["CLM-MLC-DICT-PRON-GUIDE-001"]["claim"]
    assert "MLCTS 2" in claims["CLM-MOW-MLCTS2-VARIANTS-001"]["claim"]
    assert "nomenclature discrepancy" in claims["CLM-MYA2ROM-COLUMN3-NAMING-001"]["claim"]
    assert "does not reproduce its pronunciation key" in claims["CLM-MLC-CONCISE-DICT-1978-80-001"]["claim"]
    assert "not direct access to its contents" in claims["CLM-MLC-CONCISE-DICT-BIB-001"]["claim"]

MLCTS2_CROSSWALK_PATH = ROOT / "data/burmese/romanization_rime_mlcts2_crosswalk.csv"


def test_mlcts2_crosswalk_is_exactly_derived_from_vendored_column_three():
    collisions_path = ROOT / "data/burmese/romanization_rime_collisions.csv"
    with collisions_path.open(encoding="utf-8-sig", newline="") as stream:
        collisions = {row["mlcts"]: row for row in csv.DictReader(stream)}
    with MLCTS2_CROSSWALK_PATH.open(encoding="utf-8-sig", newline="") as stream:
        crosswalk = list(csv.DictReader(stream))
    vendor_text = (ROOT / "vendor/mya2rom/romanisations.js").read_text(encoding="utf-8")
    vendor = {
        key: (ipa, mlcts, mlcts2)
        for key, ipa, mlcts, mlcts2 in re.findall(
            r'^\s*"([^"]*)"\s*:\s*\["([^"]*)"\s*,\s*"([^"]*)"\s*,\s*"([^"]*)"',
            vendor_text,
            flags=re.MULTILINE,
        )
    }

    assert len(crosswalk) == len(collisions) == 25
    assert {row["mlcts"] for row in crosswalk} == set(collisions)
    distinct_groups = set()
    for row in crosswalk:
        source_units = row["source_units"].split(";")
        assert row["source_units"] == collisions[row["mlcts"]]["source_units"]
        values = [vendor[unit] for unit in source_units]
        assert row["mlcts2_values"] == ";".join(value[2] for value in values)
        assert row["ipa_values"] == ";".join(value[0] for value in values)
        expected_relation = (
            "SAME_MLCTS2_OUTPUT" if len({value[2] for value in values}) == 1
            else "DISTINCT_MLCTS2_OUTPUT"
        )
        if row["mlcts"] == "u.":
            expected_relation = "SPECIAL_CONTEXT_FALLBACK"
        assert row["mlcts2_relation"] == expected_relation
        assert row["lexical_audit_status"] in {
            "UNADJUDICATED_NO_WORD_LEVEL_EVIDENCE",
            "SECONDARY_SYSTEM_EQUIVALENCE",
            "SECONDARY_SOURCE_CONFLICT",
            "SECONDARY_SOURCE_DISTINCTION",
            "SECONDARY_ONE_SIDE_ONLY",
            "SPECIAL_NONRIME_CONTEXT_DEPENDENT",
        }
        assert "not a primary mlc dictionary entry" in row["interpretation_boundary"].lower()
        if expected_relation == "DISTINCT_MLCTS2_OUTPUT":
            distinct_groups.add(row["mlcts"])

    assert distinct_groups == {"any", "any:", "any.", "ui"}
    assert crosswalk and crosswalk[0]["mlcts2_relation"] == "SAME_MLCTS2_OUTPUT"

VENDOR_SYSTEM_CROSSWALK_PATH = ROOT / "data/burmese/romanization_rimes_vendor_systems.csv"


def test_full_vendor_system_crosswalk_covers_all_94_nonempty_rime_keys():
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        inventory = {row["source_unit"]: row for row in csv.DictReader(stream)}
    with VENDOR_SYSTEM_CROSSWALK_PATH.open(encoding="utf-8-sig", newline="") as stream:
        crosswalk = {row["source_unit"]: row for row in csv.DictReader(stream)}
    vendor_text = (ROOT / "vendor/mya2rom/romanisations.js").read_text(encoding="utf-8")
    vendor = {
        key: (ipa, mlcts, mlcts2, simple, simple2)
        for key, ipa, mlcts, mlcts2, simple, simple2 in re.findall(
            r'^\s*"([^"]+)"\s*:\s*\["([^"]*)"\s*,\s*"([^"]*)"\s*,\s*"([^"]*)"\s*,\s*"([^"]*)"(?:\s*,\s*"([^"]*)")?',
            vendor_text,
            flags=re.MULTILINE,
        )
    }

    assert len(inventory) == len(crosswalk) == 94
    assert set(crosswalk) == set(inventory)
    assert set(crosswalk) <= set(vendor)
    for key, row in crosswalk.items():
        values = vendor[key]
        assert row["mlcts"] == inventory[key]["mlcts"] == values[1]
        assert row["ipa_vendor"] == values[0]
        assert row["mlcts2_vendor"] == values[2]
        assert row["simple_vendor"] == values[3]
        assert row["simple2_vendor"] == values[4]
        assert int(row["array_length"]) == (5 if values[4] else 4)
        assert "not primary MLC table" in row["evidence_boundary"]
    missing_simple2 = {
        key for key, row in crosswalk.items()
        if row["simple2_status"] == "NOT_PROVIDED_IN_VENDOR_ARRAY"
    }
    assert missing_simple2 == {"ေါင်း"}

def test_mow_orthographic_outputs_are_reproducible_and_evidence_limited():
    import subprocess
    import sys

    completed = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/analyze_mow_orthographic_rime_coverage.py"),
            "--check",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr

    with (ROOT / "data/burmese/mow_rime_orthographic_coverage.csv").open(
        encoding="utf-8-sig", newline=""
    ) as stream:
        coverage = list(csv.DictReader(stream))
    with (ROOT / "data/burmese/mow_rime_orthographic_matches.csv").open(
        encoding="utf-8-sig", newline=""
    ) as stream:
        matches = list(csv.DictReader(stream))

    assert len(coverage) == 50
    assert len(matches) == 508
    assert {row["evidence_type"] for row in matches} == {"ORTHOGRAPHIC_SUFFIX_MATCH_ONLY"}
    group_status = {
        mlcts: {row["collision_group_coverage"] for row in coverage if row["mlcts"] == mlcts}
        for mlcts in {row["mlcts"] for row in coverage}
    }
    assert sum(status == {"BOTH_UNITS_FOUND"} for status in group_status.values()) == 11
    assert sum(status == {"ONE_UNIT_FOUND"} for status in group_status.values()) == 13
    assert sum(status == {"NEITHER_UNIT_FOUND"} for status in group_status.values()) == 1
    assert group_status["um."] == {"NEITHER_UNIT_FOUND"}


def test_mow_dataset_source_claim_preserves_cc_by_and_orthographic_scope():
    with (ROOT / "data/burmese/sources.csv").open(encoding="utf-8-sig", newline="") as stream:
        sources = {row["source_id"]: row for row in csv.DictReader(stream)}
    with (ROOT / "data/burmese/source_claims.csv").open(
        encoding="utf-8-sig", newline=""
    ) as stream:
        claims = {row["claim_id"]: row for row in csv.DictReader(stream)}

    assert "MOW_2017_0_1_3_DATASET" in sources
    assert "CC BY 4.0" in sources["MOW_2017_0_1_3_DATASET"]["scope"]
    assert claims["CLM-MOW-ORTHOGRAPHIC-RIME-COVERAGE-001"]["source_id"] == "MOW_2017_0_1_3_DATASET"
    assert "suffix matching does not perform Burmese syllabification" in claims[
        "CLM-MOW-ORTHOGRAPHIC-RIME-COVERAGE-001"
    ]["claim"]

def test_mow_source_header_preserves_upstream_attribution_and_license():
    source = ROOT / "data/burmese/external/mow-0.1.3-mya_20171005165336.tab"
    assert source.read_text(encoding="utf-8").splitlines()[0] == (
        "## MOW 0.1.3\tmya\tCC BY 4.0"
    )

def test_sealang_api_request_pattern_is_registered_with_response_schema_caveat():
    with (ROOT / "data/burmese/sources.csv").open(encoding="utf-8-sig", newline="") as stream:
        sources = {row["source_id"]: row for row in csv.DictReader(stream)}
    with (ROOT / "data/burmese/source_claims.csv").open(
        encoding="utf-8-sig", newline=""
    ) as stream:
        claims = {row["claim_id"]: row for row in csv.DictReader(stream)}

    assert "SEALANG_SHORTCUT_2022" in sources
    claim = claims["CLM-SEALANG-API-REQUEST-PATTERN-001"]
    assert claim["source_id"] == "SEALANG_SHORTCUT_2022"
    assert "lang=burmese" in claim["claim"]
    assert "does not establish current endpoint availability" in claim["claim"]

def test_r12a_secondary_phonology_crosswalk_preserves_ipa_distinctions_and_scope():
    with (ROOT / "data/burmese/romanization_rime_collisions.csv").open(
        encoding="utf-8-sig", newline=""
    ) as stream:
        collisions = {row["mlcts"]: row for row in csv.DictReader(stream)}
    with (ROOT / "data/burmese/romanization_rime_r12a_secondary_phonology_crosswalk.csv").open(
        encoding="utf-8-sig", newline=""
    ) as stream:
        crosswalk = {row["mlcts"]: row for row in csv.DictReader(stream)}
    with (ROOT / "data/burmese/sources.csv").open(encoding="utf-8-sig", newline="") as stream:
        sources = {row["source_id"]: row for row in csv.DictReader(stream)}
    with (ROOT / "data/burmese/source_claims.csv").open(
        encoding="utf-8-sig", newline=""
    ) as stream:
        claims = {row["claim_id"]: row for row in csv.DictReader(stream)}

    assert set(crosswalk) == set(collisions)
    assert len(crosswalk) == 25
    for key, row in crosswalk.items():
        assert row["source_units"] == collisions[key]["source_units"]
        assert "not an MLC primary table" in row["evidence_boundary"]
        assert "do not promote" in row["evidence_boundary"]

    statuses = [row["comparison_status"] for row in crosswalk.values()]
    assert statuses.count("SAME_IN_R12A_TABLE") == 18
    assert statuses.count("DISTINCT_IN_R12A_TABLE") == 3
    assert statuses.count("PARTIAL_COVERAGE") == 2
    assert statuses.count("NOT_LISTED_IN_R12A_TABLE") == 1
    assert statuses.count("SPECIAL_NONRIME_CONTEXT_DEPENDENT") == 1

    assert crosswalk["any"]["r12a_ipa_values"] == "ɪ̀N;ì, è, ɛ̀"
    assert crosswalk["any:"]["r12a_ipa_values"] == "ɪ́N;í, é, ɛ́"
    assert crosswalk["any."]["r12a_ipa_values"] == "ɪ̰N;ḭ, ḛ, ɛ̰"
    assert crosswalk["any"]["comparison_status"] == "DISTINCT_IN_R12A_TABLE"
    assert crosswalk["am"]["r12a_ipa_values"] == "àN;àN"
    assert crosswalk["um"]["r12a_ipa_values"] == "òʊN;òʊN"
    assert crosswalk["u."]["comparison_status"] == "SPECIAL_NONRIME_CONTEXT_DEPENDENT"
    assert crosswalk["a."]["comparison_status"] == "NOT_LISTED_IN_R12A_TABLE"

    assert "R12A_BURMESE_ORTHOGRAPHY_2026" in sources
    assert "not an MLC primary transcription table" in sources[
        "R12A_BURMESE_ORTHOGRAPHY_2026"
    ]["scope"]
    claim = claims["CLM-R12A-RIME-CROSSWALK-2026-001"]
    assert claim["source_id"] == "R12A_BURMESE_ORTHOGRAPHY_2026"
    assert "does not account for vowel reduction" in claim["claim"]
    assert "not a primary MLC table" in claim["claim"]

def test_unicode_n2827_medial_source_is_limited_to_orthographic_structure():
    with (ROOT / "data/burmese/sources.csv").open(encoding="utf-8-sig", newline="") as stream:
        sources = {row["source_id"]: row for row in csv.DictReader(stream)}
    with (ROOT / "data/burmese/source_claims.csv").open(
        encoding="utf-8-sig", newline=""
    ) as stream:
        claims = {row["claim_id"]: row for row in csv.DictReader(stream)}

    assert "UNICODE_N2827_MYANMAR_SEMIVOWELS_2004" in sources
    claim = claims["CLM-UNICODE-N2827-MLC-MEDIALS-001"]
    assert claim["source_id"] == "UNICODE_N2827_MYANMAR_SEMIVOWELS_2004"
    assert "eleven medial symbols" in claim["claim"]
    assert "no MLCTS or IPA rime table" in claim["claim"]

def test_mlc_1986_orthography_catalog_record_is_only_an_access_lead():
    with (ROOT / "data/burmese/sources.csv").open(encoding="utf-8-sig", newline="") as stream:
        sources = {row["source_id"]: row for row in csv.DictReader(stream)}
    with (ROOT / "data/burmese/source_claims.csv").open(
        encoding="utf-8-sig", newline=""
    ) as stream:
        claims = {row["claim_id"]: row for row in csv.DictReader(stream)}

    source = sources["MLC_1986_ORTHOGRAPHY_NLMNPT_189"]
    claim = claims["CLM-MLC-1986-ORTHOGRAPHY-CATALOG-001"]
    assert "292 pages" in source["scope"]
    assert "PDF option listed" in source["scope"]
    assert "contents were not inspected" in source["scope"]
    assert claim["source_id"] == "MLC_1986_ORTHOGRAPHY_NLMNPT_189"
    assert "no book pages were inspected" in claim["claim"]
    assert "not the book’s structural rules" in claim["claim"]

def test_unicode_2010_spelling_dictionary_scan_is_partial_and_not_mlcts_ipa():
    with (ROOT / "data/burmese/sources.csv").open(encoding="utf-8-sig", newline="") as stream:
        sources = {row["source_id"]: row for row in csv.DictReader(stream)}
    with (ROOT / "data/burmese/source_claims.csv").open(
        encoding="utf-8-sig", newline=""
    ) as stream:
        claims = {row["claim_id"]: row for row in csv.DictReader(stream)}

    assert "UNICODE_L2_2010_MLC_SPELLING_1986" in sources
    claim = claims["CLM-UNICODE-L2-2010-MLC-SPELLING-SCAN-001"]
    assert claim["source_id"] == "UNICODE_L2_2010_MLC_SPELLING_1986"
    assert "page 1" in claim["claim"]
    assert "does not show an MLCTS or IPA rime table" in claim["claim"]
    assert "identity of this title" in claim["claim"]


def test_new_wiktionary_lexical_claims_are_linked_to_registered_snapshot():
    claims_path = ROOT / "data/burmese/source_claims.csv"
    with claims_path.open(encoding="utf-8-sig", newline="") as stream:
        claims = {row["claim_id"]: row for row in csv.DictReader(stream)}
    for claim_id in (
        "CLM-WIKTIONARY-AUNG-DOT-ONE-SIDE-EXAMPLE-001",
        "CLM-WIKTIONARY-AM-COLON-ONE-SIDE-EXAMPLE-001",
        "CLM-WIKTIONARY-AM-DOT-LEXICAL-DISTINCTION-001",
        "CLM-WIKTIONARY-AU-DOT-ONE-SIDE-EXAMPLE-001",
        "CLM-WIKTIONARY-UM-COLON-ONE-SIDE-EXAMPLE-001",
        "CLM-WIKTIONARY-AU-COLON-ONE-SIDE-EXAMPLE-001",
        "CLM-WIKTIONARY-IM-ONE-SIDE-EXAMPLE-001",
        "CLM-WIKTIONARY-IM-DOT-ONE-SIDE-EXAMPLE-001",
        "CLM-WIKTIONARY-UN-ONE-SIDE-EXAMPLE-001",
        "CLM-WIKTIONARY-UN-SECOND-SIDE-EXAMPLE-001",
        "CLM-WIKTIONARY-AUK-WORD-LEVEL-EXAMPLES-001",
        "CLM-WIKTIONARY-A-WORD-LEVEL-EXAMPLES-001",
        "CLM-WIKTIONARY-A-COLON-WORD-LEVEL-EXAMPLES-001",
        "CLM-WIKTIONARY-AU-WORD-LEVEL-EXAMPLES-001",
        "CLM-WIKTIONARY-AUNG-COLON-WORD-LEVEL-EXAMPLES-001",
        "CLM-WIKTIONARY-ANY-WORD-LEVEL-EXAMPLES-001",
        "CLM-WIKTIONARY-ANY-COLON-WORD-LEVEL-EXAMPLES-001",
        "CLM-WIKTIONARY-UI-SINGLE-SIDE-WORD-EXAMPLES-001",
    ):
        assert claims[claim_id]["source_id"] == "MYWIKTIONARY2026"
        assert claims[claim_id]["evidence_type"] == "secondary_lexical_transcription"
        assert claims[claim_id]["status"] == "DOCUMENTARY"
