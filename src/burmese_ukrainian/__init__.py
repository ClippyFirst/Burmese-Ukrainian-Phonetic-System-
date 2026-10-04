"""Burmese → Ukrainian phonetic-graphemic correspondence system."""
from .parser import parse_burmese, normalize_burmese, segment_graphemes, segment_syllables
from .ipa import to_ipa
from .ukrainian import ipa_to_ukrainian
from .practical import practical_from_ipa, rank_ukrainian_candidates
from .explain import explain

__all__ = [
    "parse_burmese", "normalize_burmese", "segment_graphemes",
    "segment_syllables", "to_ipa", "ipa_to_ukrainian",
    "practical_from_ipa", "rank_ukrainian_candidates", "explain",
]
