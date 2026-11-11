"""Research hybrid wrapper for Burmese IPA candidates.

The deterministic rule engine remains authoritative. Google WFST, myG2P and
optional external G2P outputs are preserved as candidates, never voted.
"""
from __future__ import annotations
from typing import Any, Callable
from .rule_engine import RuleBasedBurmeseEngine

Provider = Callable[[str], str | dict[str, Any]]

PROVIDER_PRIORITY = {
    "myg2p-ipa": 10,
    "myg2p": 10,
    "google-wfst": 20,
    "google_wfst": 20,
    "epitran": 40,
    "crf": 60,
    "goruut": 90,
}
DEFAULT_PROVIDER_PRIORITY = 50


def normalize_ipa_transport(value: str) -> str:
    value = value.strip()
    if value.startswith("/") and value.endswith("/") and len(value) > 1:
        value = value[1:-1]
    elif value.startswith("[") and value.endswith("]") and len(value) > 1:
        value = value[1:-1]
    return " ".join(value.split())

def _candidate(provider_id: str, raw: Any) -> dict[str, Any] | None:
    if isinstance(raw, str):
        ipa, status, provenance = raw, "candidate", {}
    elif isinstance(raw, dict):
        ipa, status, provenance = raw.get("ipa"), raw.get("status", "candidate"), raw.get("provenance", {})
    else:
        return None
    if status in {"error", "unsupported", "not_established", "analysis_dependent"}:
        return None
    if not isinstance(ipa, str) or not normalize_ipa_transport(ipa) or "?" in ipa:
        return None
    return {"provider": provider_id, "priority": PROVIDER_PRIORITY.get(provider_id, DEFAULT_PROVIDER_PRIORITY), "ipa_raw": ipa,
            "ipa_transport_normalized": normalize_ipa_transport(ipa),
            "status": status, "provenance": provenance if isinstance(provenance, dict) else {},
            "promotion": "WITHHELD_PENDING_INDEPENDENT_PROFILE_MATCHED_ADJUDICATION"}

class HybridBurmeseEngine:
    """Run conservative internal rules and optional external Burmese G2P sources."""
    def __init__(self, providers: dict[str, Provider] | None = None,
                 rule_engine: RuleBasedBurmeseEngine | None = None):
        self.providers = dict(providers or {})
        self.rule_engine = rule_engine or RuleBasedBurmeseEngine()

    def analyze(self, text: str) -> dict[str, Any]:
        result = dict(self.rule_engine.analyze(text))
        candidates, failures = [], []
        normalized = result.get("normalized", text)
        for provider_id, provider in sorted(self.providers.items(), key=lambda item: (PROVIDER_PRIORITY.get(item[0], DEFAULT_PROVIDER_PRIORITY), item[0])):
            try:
                item = _candidate(provider_id, provider(normalized))
                if item is None:
                    failures.append({"provider": provider_id, "reason": "NO_TYPED_COMPLETE_IPA"})
                else:
                    candidates.append(item)
            except Exception as exc:
                failures.append({"provider": provider_id, "reason": type(exc).__name__})
        result.update({
            "hybrid_engine": "burmese-evidence-gated-hybrid-v1",
            "external_candidates": candidates, "backend_failures": failures,
            "external_candidate_count": len(candidates),
            "provider_priority_policy": "lower_number_runs_first_and_orders_candidates; priorities_are_research_triage_only_not_accuracy_or_promotion; unknown_providers_use_default_priority_50",
            "selection_policy": "internal_deterministic_rule_output_is_preserved; external_candidates_are_diagnostic_only; no_voting_or_promotion_without_independent_profile_matched_gold",
        })
        return result

def make_google_wfst_backend(binary: str, fst: str, phoneme_symbols: str) -> Provider:
    """Run pinned Google Thrax FST and validate its echoed input."""
    import subprocess
    from pathlib import Path
    revision = "a90601024f07ab7e96c911243324e0adeb16da96"
    def run(text: str) -> dict[str, Any]:
        paths = [Path(binary), Path(fst), Path(phoneme_symbols)]
        if not all(path.is_file() for path in paths):
            raise FileNotFoundError("Google WFST binary/FST/symbol-table artifact missing")
        command = [str(paths[0].resolve()), f"--fst={paths[1].resolve()}",
                   f"--phoneme_syms={paths[2].resolve()}"]
        completed = subprocess.run(command, input=text + "\n", text=True, capture_output=True, check=True)
        lines = completed.stdout.splitlines()
        if len(lines) != 1 or "\t" not in lines[0]:
            raise ValueError("Google WFST must return one echoed-input/IPA TSV line")
        echoed, ipa = lines[0].split("\t", 1)
        if echoed != text:
            raise ValueError("Google WFST echoed input mismatch")
        return {"ipa": ipa, "status": "candidate" if ipa.strip() else "unsupported",
                "provenance": {"engine": "google/language-resources Burmese Thrax/OpenFst",
                               "revision": revision}}
    return run

def make_myg2p_dictionary_backend(dictionary_path: str) -> Provider:
    """Exact lookup of myG2P v2.0 fifth IPA field; never reads MLCTS."""
    import csv
    from pathlib import Path
    path = Path(dictionary_path)
    dictionary: dict[str, list[str]] | None = None
    def run(text: str) -> dict[str, Any]:
        nonlocal dictionary
        if dictionary is None:
            dictionary = {}
            with path.open(encoding="utf-8", newline="") as stream:
                for row in csv.reader(stream, delimiter="\t"):
                    if len(row) >= 5 and row[1] and row[4].strip():
                        dictionary.setdefault(row[1], []).append(row[4].strip())
        values = sorted(set(dictionary.get(text, [])))
        if len(values) == 1:
            return {"ipa": values[0], "status": "candidate",
                    "provenance": {"engine": "myG2P v2.0", "lookup": "exact_orthography",
                                   "ipa_column": 5, "license": "CC BY-NC-SA 4.0"}}
        return {"ipa": "", "status": "analysis_dependent" if values else "unsupported",
                "provenance": {"engine": "myG2P v2.0", "ambiguous_values": values}}
    return run

def make_epitran_backend(*, tones: bool = True) -> Provider:
    """Optional Epitran comparator for mya-Mymr; output remains unvalidated."""
    def run(text: str) -> dict[str, Any]:
        try:
            import epitran
            from importlib.metadata import version
        except ImportError as exc:
            raise RuntimeError("Install optional Epitran to use this comparator") from exc
        ipa = epitran.Epitran("mya-Mymr", tones=tones).transliterate(text)
        return {"ipa": ipa, "status": "candidate" if ipa else "unsupported",
                "provenance": {"engine": "Epitran", "version": version("epitran"),
                               "profile_match": "NOT_ESTABLISHED", "tones_requested": tones}}
    return run

def make_command_backend(command: list[str], *, engine_id: str, revision: str) -> Provider:
    """Adapter for pinned Goruut or other command-line G2P candidates."""
    import subprocess
    def run(text: str) -> dict[str, Any]:
        completed = subprocess.run(command, input=text + "\\n", text=True, capture_output=True, check=True)
        ipa = completed.stdout.strip()
        return {"ipa": ipa, "status": "candidate" if ipa else "unsupported",
                "provenance": {"engine": engine_id, "revision": revision, "stderr": completed.stderr}}
    return run


def create_hybrid_engine(providers: dict[str, Provider] | None = None) -> HybridBurmeseEngine:
    return HybridBurmeseEngine(providers=providers)
