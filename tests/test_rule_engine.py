from burmese_ukrainian.rule_engine import RuleBasedBurmeseEngine
from burmese_ukrainian.hybrid import HybridBurmeseEngine


def test_rule_engine_generates_repeatable_ipa_from_repository_rules():
    engine = RuleBasedBurmeseEngine()
    first = engine.analyze("ကာ")
    second = engine.analyze("ကာ")
    assert first == second
    assert first["ipa"] == "ka"
    assert first["status"] == "PROPOSED"
    assert first["deterministic"] is True
    assert first["external_backends_used"] == []


def test_unsupported_bare_consonant_is_withheld():
    result = RuleBasedBurmeseEngine().analyze("က")
    assert result["ipa"] is None
    assert result["status"] == "PARTIAL"


def test_hybrid_wraps_rule_engine_without_changing_final_ipa():
    baseline = RuleBasedBurmeseEngine().analyze("ကာ")
    result = HybridBurmeseEngine().analyze("ကာ")
    assert result["ipa"] == baseline["ipa"]
    assert result["external_candidates"] == []


def test_hybrid_factory_accepts_candidates_but_does_not_promote_them():
    from burmese_ukrainian import create_hybrid_engine
    baseline = RuleBasedBurmeseEngine().analyze("ကာ")
    result = create_hybrid_engine({"external-model": lambda _: "ka"}).analyze("ကာ")
    assert result["ipa"] == baseline["ipa"]
    assert result["external_candidates"][0]["provider"] == "external-model"
    assert result["external_candidates"][0]["promotion"].startswith("WITHHELD")
