"""
engine/specificity_registry.py — SOI diagnostic (Art. 21).

Rajpopat 2021 Specificity of Input is **not a winner**. The resolver may
consult these scores to propose an undeclared apavāda (Art. 18 gap
``undeclared_apavada_candidate``). *para* (1.4.2) still decides unless a
declared ``apavada_of`` already did.

Registration remains available so a scholar can attach a proposal::

    from engine.specificity_registry import register_specificity
    register_specificity("3.1.68", lambda state: 2)
"""
from __future__ import annotations

from typing import Callable

from engine.state import State

# Maps sutra_id → fn(State) → int  (diagnostic; never a Decision.layer)
SPECIFICITY_REGISTRY: dict[str, Callable[[State], int]] = {}


def register_specificity(sutra_id: str, fn: Callable[[State], int]) -> None:
    """Register a diagnostic specificity score. Does not make the sūtra win."""
    SPECIFICITY_REGISTRY[sutra_id] = fn


def get_specificity(sutra_id: str, state: State) -> int:
    """Return the diagnostic specificity score, or 0."""
    fn = SPECIFICITY_REGISTRY.get(sutra_id)
    if fn is None:
        return 0
    return fn(state)
