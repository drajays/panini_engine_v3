"""
pipelines/it_prakarana.py — scheduler for the *it-saṃjñā prakaraṇa* (**1.3.2**–**1.3.9**).

Recipe-only (CONSTITUTION Art. 7): the eight sūtras in Aṣṭādhyāyī order, each via
``apply_rule``.  Every sūtra scans all *upadeśa* Terms in its own scope, so one call
covers dhātu, pratyaya, ādeśa and āgama alike; sūtras whose condition fails record
COND-FALSE.  Records of *which* it each Term carried live in ``engine.it_samjna``.
"""
from __future__ import annotations

from typing import Tuple

from engine import apply_rule
from engine.state import State

IT_PRAKARANA_SEQUENCE: Tuple[str, ...] = (
    "1.3.2", "1.3.3", "1.3.4", "1.3.5", "1.3.6", "1.3.7", "1.3.8", "1.3.9",
)


def run_it_prakarana(state: State) -> State:
    for sid in IT_PRAKARANA_SEQUENCE:
        state = apply_rule(sid, state)
    return state


__all__ = ["IT_PRAKARANA_SEQUENCE", "run_it_prakarana"]
