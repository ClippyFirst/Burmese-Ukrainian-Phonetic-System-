"""Evidence-aware Burmese IPA ensemble.

Structural analysis, internal conservative IPA, and external engines remain
separate evidence channels. IPA is exposed as consensus only when two distinct
backends agree exactly after transport-only normalization.
"""
from __future__ import annotations

from collections import defaultdict
from typing import Any, Callable, Iterable

from .parser import parse_burmese
from .ipa import to_ipa

Provider = Callable[[str], str | dict[str, Any]]


def normalize_ipa(value: str) -> str:
    value = value.strip()
    if value.startswith("/") and value.endswith("/") and len(value) > 1:
        value = value[1:-1]
    if value.startswith("[") and value.endswith("]") and len(value) > 1:
        value = value[1:-1]
    return " ".join(value.split())


def _candidate(provider_id: str, raw: str | dict[str, Any]) -> dict[str, Any] | None:
    if isinstance(raw, str):
        ipa, status, provenance = raw, "candidate", {}
    elif isinstance(raw, dict):
        ipa, status = raw.get("ipa"), raw.get("status", "candidate")
        provenance = raw.get("provenance", {})
    else:
        return None
    if not isinstance(ipa, str) or not normalize_ipa(ipa) or "?" in ipa:
        return None
    if status in {"error", "unsupported", "not_established", "analysis_dependent"}:
        return None
    return {"provider": provider_id, "ipa_raw": ipa, "ipa_normalized": normalize_ipa(ipa),
            "status": status, "provenance": provenance if isinstance(provenance, dict) else {}}


def combine_candidates(candidates: Iterable[dict[str, Any]]) -> dict[str, Any]:
    by_ipa: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in candidates:
        by_ipa[item["ipa_normalized"]].append(item)
    ranked = sorted(by_ipa.items(), key=lambda pair: (-len({x["provider"] for x in pair[1]}), pair[0]))
    if not ranked:
        return {"ipa": None, "status": "no_ipa_candidate", "agreement": 0}
    best_ipa, best = ranked[0]
    votes = len({item["provider"] for item in best})
    second_votes = len({x["provider"] for x in ranked[1][1]}) if len(ranked) > 1 else 0
    if votes >= 2 and votes > second_votes:
        return {"ipa": best_ipa, "status": "ensemble_consensus", "agreement": votes}
    return {"ipa": None, "status": "engine_disagreement" if len(ranked) > 1 else "single_engine_candidate",
            "agreement": votes}


class HybridBurmeseEngine:
    """Combine internal structural/partial IPA analysis with injected G2P engines."""

    def __init__(self, providers: dict[str, Provider] | None = None, include_internal: bool = True):
        self.providers = providers or {}
        self.include_internal = include_internal

    def analyze(self, text: str) -> dict[str, Any]:
        structure = parse_burmese(text)
        candidates = []
        failures = []
        if self.include_internal:
            internal = to_ipa(text)
            # Partial syllables containing '?' are deliberately excluded.
            item = _candidate("internal-conservative-ipa", {
                "ipa": internal.get("ipa", ""),
                "status": "candidate" if "?" not in internal.get("ipa", "") else "analysis_dependent",
                "provenance": {"kind": "repository_rule_adapter"},
            })
            if item is not None:
                candidates.append(item)
        for provider_id, provider in self.providers.items():
            try:
                item = _candidate(provider_id, provider(text))
                if item is not None:
                    candidates.append(item)
                else:
                    failures.append({"provider": provider_id, "reason": "empty_or_untyped_ipa"})
            except Exception as exc:
                failures.append({"provider": provider_id, "reason": type(exc).__name__, "message": str(exc)})
        decision = combine_candidates(candidates)
        return {
            "input": text,
            "profile": "my-yangon-careful-citation-v1",
            "structure": structure,
            "ipa": decision["ipa"],
            "ipa_status": decision["status"],
            "agreement": decision["agreement"],
            "candidates": candidates,
            "backend_failures": failures,
            "provenance_policy": "raw_outputs_preserved; no_model_is_gold; two_independent_votes_required",
        }


def create_hybrid_engine(providers: dict[str, Provider] | None = None, include_internal: bool = True) -> HybridBurmeseEngine:
    return HybridBurmeseEngine(providers, include_internal=include_internal)
