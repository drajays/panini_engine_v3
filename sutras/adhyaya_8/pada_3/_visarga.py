"""Shared seam finder for 8.3.34–37: a pada ending in visarga followed by a pada that starts with a khar (Kāśikā 8.3.34–37)."""
from __future__ import annotations

from engine.state import State

KHAR = frozenset("kKcCwWtTpPSzs")
SHAR = frozenset("Szs")
KU_PU = frozenset("kKpP")


def seam(state: State):
    """(left Term, next letter, the letter after it | '') of the first seam whose left pada ends in H and not yet settled by 8.3.35–37."""
    if not state.tripadi_zone:
        return None
    for i in range(len(state.terms) - 1):
        left, right = state.terms[i], state.terms[i + 1]
        if not left.varnas or not right.varnas or left.varnas[-1].slp1 != "H" or "visarga_settled" in left.tags:
            continue
        if right.varnas[0].slp1 not in KHAR:
            continue
        return left, right.varnas[0].slp1, (right.varnas[1].slp1 if len(right.varnas) > 1 else "")
    return None
