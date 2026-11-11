from burmese_ukrainian.hybrid import HybridBurmeseEngine, make_myg2p_dictionary_backend, normalize_ipa_transport

def test_external_candidate_is_preserved_but_not_promoted():
    result = HybridBurmeseEngine({"google-wfst": lambda _: {"ipa": "kʰaʊ"}}).analyze("ကော်")
    assert result["external_candidates"][0]["ipa_raw"] == "kʰaʊ"
    assert result["external_candidates"][0]["promotion"].startswith("WITHHELD")
    assert result["selection_policy"].startswith("internal_deterministic_rule_output")

def test_partial_candidate_is_rejected():
    result = HybridBurmeseEngine({"partial": lambda _: "k? a"}).analyze("ကော်")
    assert result["external_candidates"] == []

def test_backend_failure_does_not_erase_internal_result():
    result = HybridBurmeseEngine({"broken": lambda _: (_ for _ in ()).throw(RuntimeError())}).analyze("ကော်")
    assert result["backend_failures"][0]["reason"] == "RuntimeError"
    assert "ipa" in result

def test_myg2p_exact_ipa_column_and_ambiguity(tmp_path):
    path = tmp_path / "myg2p.tsv"
    path.write_text("1\tမြန်မာ\tမြန်-မာ\tmyanma\tmjəmà\n", encoding="utf-8")
    assert make_myg2p_dictionary_backend(str(path))("မြန်မာ")["ipa"] == "mjəmà"
    path.write_text(path.read_text(encoding="utf-8") + "2\tမြန်မာ\tမြန်-မာ\tmyanma\tmjəmɑ̀\n", encoding="utf-8")
    assert make_myg2p_dictionary_backend(str(path))("မြန်မာ")["status"] == "analysis_dependent"

def test_transport_normalization_preserves_tone_and_length():
    assert normalize_ipa_transport("[kʰaʊ]") == "kʰaʊ"
    assert normalize_ipa_transport("ka") != normalize_ipa_transport("kaː")

def test_command_backend_preserves_raw_candidate_and_provenance(monkeypatch):
    import subprocess
    from types import SimpleNamespace
    from burmese_ukrainian.hybrid import make_command_backend
    monkeypatch.setattr(subprocess, "run", lambda *args, **kwargs: SimpleNamespace(stdout="mjəmà\n", stderr=""))
    candidate = make_command_backend(["goruut"], engine_id="goruut", revision="PINNED")("မြန်မာ")
    assert candidate["ipa"] == "mjəmà"
    assert candidate["provenance"]["revision"] == "PINNED"

def test_epitran_backend_requests_tone_output(monkeypatch):
    import sys
    from types import SimpleNamespace
    from burmese_ukrainian.hybrid import make_epitran_backend
    seen = {}
    class FakeEpitran:
        def transliterate(self, text):
            return "mjəmà"
    def factory(code, *, tones):
        seen["code"] = code
        seen["tones"] = tones
        return FakeEpitran()
    monkeypatch.setitem(sys.modules, "epitran", SimpleNamespace(Epitran=factory))
    import importlib.metadata
    monkeypatch.setattr(importlib.metadata, "version", lambda _: "1.35.3")
    result = make_epitran_backend()("မြန်မာ")
    assert seen == {"code": "mya-Mymr", "tones": True}
    assert result["provenance"]["tones_requested"] is True
