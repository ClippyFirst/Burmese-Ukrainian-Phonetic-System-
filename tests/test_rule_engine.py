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


def test_legacy_hybrid_name_is_rule_engine_not_ensemble():
    assert HybridBurmeseEngine is RuleBasedBurmeseEngine
    result = HybridBurmeseEngine().analyze("ကာ")
    assert result["engine"] == "burmese-deterministic-rules-v1"
    assert result["external_backends_used"] == []
