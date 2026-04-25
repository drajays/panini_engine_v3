"""
Saṃjñā *state* — the single mutable store is :attr:`State.samjna_registry`
and Term-level :attr:`Term.tags` (``engine.state``).

This module does not introduce a parallel ``Term``/``State``; it re-exports
the engine types and small read helpers for audit tooling.
"""
from __future__ import annotations

from engine.state import State, Term, Varna


def samjna_labels(state: State) -> frozenset[str]:
    """Names of active saṃjñā buckets (keys of ``state.samjna_registry``)."""
    return frozenset(state.samjna_registry.keys())


__all__ = ["State", "Term", "Varna", "samjna_labels"]
