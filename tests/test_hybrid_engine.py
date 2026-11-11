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


def test_myg2p_adapter_reads_only_the_ipa_column_and_rejects_ambiguity(tmp_path):
    from burmese_ukrainian.hybrid import make_myg2p_dictionary_backend

    dictionary = tmp_path / "myg2p.tsv"
    dictionary.write_text("1\tမြန်မာ\tမြန်-မာ\tmyanma\tmjəmà\n", encoding="utf-8")
    backend = make_myg2p_dictionary_backend(str(dictionary))
    result = backend("မြန်မာ")
    assert result["ipa"] == "mjəmà"
    assert result["provenance"]["ipa_column"] == 5

    dictionary.write_text(dictionary.read_text(encoding="utf-8") + "2\tမြန်မာ\tမြန်-မာ\tmyanma\tmjəmɑ̀\n", encoding="utf-8")
    backend_after_update = make_myg2p_dictionary_backend(str(dictionary))
    ambiguous = backend_after_update("မြန်မာ")
    assert ambiguous["status"] == "analysis_dependent"
    assert ambiguous["ipa"] == ""


def test_google_wfst_adapter_checks_echoed_input(tmp_path, monkeypatch):
    import subprocess
    from types import SimpleNamespace
    from burmese_ukrainian.hybrid import make_google_wfst_backend

    binary, fst, symbols = (tmp_path / "g2p", tmp_path / "g2p.fst", tmp_path / "ipa.syms")
    for path in (binary, fst, symbols):
        path.write_text("placeholder", encoding="utf-8")
    monkeypatch.setattr(subprocess, "run", lambda command, input, **kwargs: SimpleNamespace(stdout=input.strip() + "\tkʰaʊ\n", stderr=""))
    backend = make_google_wfst_backend(str(binary), str(fst), str(symbols))
    result = backend("ကော်")
    assert result["ipa"] == "kʰaʊ"
    assert result["provenance"]["revision"] == "a90601024f07ab7e96c911243324e0adeb16da96"


def test_backends_receive_normalized_burmese_text():
    import unicodedata
    from burmese_ukrainian.unicode import normalize_burmese

    received = []
    source = unicodedata.normalize("NFD", "မြန်မာ")
    engine = HybridBurmeseEngine({"backend-a": lambda value: received.append(value) or "mjəmà"}, include_internal=False)
    engine.analyze(source)
    assert received == [normalize_burmese(source)]
