"""
engine/specificity_registry.py — SOI (Specificity of Input) scores.

Pāṇini's SOI principle (Rajpopat 2021): when two sūtras compete on the
same state, the one with the NARROWER input condition (more specific trigger)
wins.  An apavāda (exception) beats its utsarga (general rule) because it
applies to a proper subset of the utsarga's input.

This module stores per-sūtra specificity score functions:
    SPECIFICITY_REGISTRY[sutra_id] = fn(state: State) -> int

The resolver (engine/resolver.py) calls these to implement Layer C SOI.
Higher score = more specific = wins.

Registration:
    from engine.specificity_registry import register_specificity
    register_specificity("3.1.68", lambda state: 2)

The default specificity for unregistered sūtras is 0 (from resolver's
_default_specificity heuristic).
"""
from __future__ import annotations

from typing import Callable

from engine.state import State

# Maps sutra_id → fn(State) → int
SPECIFICITY_REGISTRY: dict[str, Callable[[State], int]] = {}


def register_specificity(sutra_id: str, fn: Callable[[State], int]) -> None:
    """Register a specificity score function for a sūtra."""
    SPECIFICITY_REGISTRY[sutra_id] = fn


def get_specificity(sutra_id: str, state: State) -> int:
    """Return the specificity score for a sūtra on the given state."""
    fn = SPECIFICITY_REGISTRY.get(sutra_id)
    if fn is None:
        return 0
    try:
        return fn(state)
    except Exception:
        return 0
