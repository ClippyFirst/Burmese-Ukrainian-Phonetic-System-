"""Deprecated import path for the deterministic Burmese rule engine.

The former provider-voting ensemble has been removed. This compatibility
module contains no external backend, neural inference, or candidate voting.
"""
from .rule_engine import HybridBurmeseEngine, RuleBasedBurmeseEngine, create_hybrid_engine

__all__ = ["HybridBurmeseEngine", "RuleBasedBurmeseEngine", "create_hybrid_engine"]
