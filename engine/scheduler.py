"""
engine/scheduler.py — Candidate enumeration.
──────────────────────────────────────────────

For "autonomous" derivation (no recipe list), the scheduler asks:
  "Which sūtras in the registry would fire on this state RIGHT NOW?"

It returns the list of ids whose `cond(state)` returns True AND which
are not blocked / frozen / asiddha.

If exactly one candidate remains, fire it.
If zero,   derivation has halted.
If more,   pass to engine/resolver.py.

This module is OPTIONAL for pipeline-driven derivations (which call
apply_rule() in a fixed order).  It is USED by tests that verify the
engine can reach a gold form autonomously.
"""
from __future__ import annotations

from typing import List

from engine.gates      import (
    asiddha_violates,
    is_blocked,
    is_frozen_by_nipatana,
)
from engine.registry   import SUTRA_REGISTRY
from engine.state      import State
from engine.sutra_type import SutraType


def enumerate_candidates(state: State) -> List[str]:
    """
    Return sūtra ids whose cond(state) fires on the current state and
    which are not ruled out by gates.  Deterministic: sorted by id.
    """
    out = []
    for sid, rec in SUTRA_REGISTRY.items():
        if is_blocked(sid, state):
            continue
        if asiddha_violates(sid, state):
            continue
        if is_frozen_by_nipatana(rec.sutra_type, state):
            continue
        # ANUVADA has no cond — it fires wherever scheduled.  To avoid
        # spurious enumeration we do NOT include ANUVADA candidates in
        # autonomous mode (recipes include them explicitly).
        if rec.sutra_type is SutraType.ANUVADA:
            continue
        if rec.cond is not None and rec.cond(state):
            out.append(sid)
    out.sort(key=lambda s: tuple(int(p) for p in s.split(".")))
    return out
