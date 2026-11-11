from burmese_ukrainian.hybrid import HybridBurmeseEngine, combine_candidates, normalize_ipa


def test_consensus_requires_two_distinct_backends():
    result = combine_candidates([
        {"provider": "google-wfst", "ipa_normalized": "kʰaʊ", "ipa_raw": "kʰaʊ", "status": "candidate", "provenance": {}},
        {"provider": "myg2p-ipa", "ipa_normalized": "kʰaʊ", "ipa_raw": "/kʰaʊ/", "status": "candidate", "provenance": {}},
    ])
    assert result == {"ipa": "kʰaʊ", "status": "ensemble_consensus", "agreement": 2}


def test_single_engine_candidate_is_not_promoted():
    result = combine_candidates([
        {"provider": "google-wfst", "ipa_normalized": "kʰaʊ", "ipa_raw": "kʰaʊ", "status": "candidate", "provenance": {}}
    ])
    assert result["ipa"] is None
    assert result["status"] == "single_engine_candidate"


def test_conflicting_engines_preserve_both_candidates():
    engine = HybridBurmeseEngine({
        "google-wfst": lambda _: "kʰaʊ",
        "myg2p-ipa": lambda _: "kʰɔː",
    }, include_internal=False)
    result = engine.analyze("ကော်")
    assert result["ipa"] is None
    assert result["ipa_status"] == "engine_disagreement"
    assert {x["provider"] for x in result["candidates"]} == {"google-wfst", "myg2p-ipa"}


def test_internal_partial_ipa_is_not_promoted_as_candidate():
    engine = HybridBurmeseEngine(include_internal=True)
    result = engine.analyze("က")
    assert result["ipa"] is None
    assert result["ipa_status"] == "no_ipa_candidate"


def test_transport_normalization_preserves_distinctive_marks():
    assert normalize_ipa("[kʰaʊ]") == "kʰaʊ"
    assert normalize_ipa("kʰaʊ") != normalize_ipa("kʰaʊː")
