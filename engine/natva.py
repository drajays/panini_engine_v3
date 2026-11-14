"""ṇatva across the upasarga | dhātu seam (8.4.14 – 8.4.16): the shared reading of the tape.

The nimitta (r / ṣ) stands in the upasarga — its varṇas carry `upasarga_v` after the pada merge — and reaches the n through
the vyavāya 8.4.2 allows (aṭ, ku, pu, āṅ, num); any other letter in between stops it. Rule logic stays in the sūtra files;
this module only reads.
"""
from __future__ import annotations

# 8.4.2 aṭkupvāṅnumvyavāye'pi: what may NOT stand between the nimitta and the n
VYAVAYA_BLOCKERS = frozenset({"t", "T", "d", "D", "c", "C", "j", "J", "w", "W", "q", "Q", "R", "s", "S", "z", "l"})


def flat(state) -> list:
    """[(term, index, varṇa)] over the tape."""
    return [(t, i, v) for t in state.terms for i, v in enumerate(t.varnas)]


def upasarga_nimitta_before(tape: list, k: int) -> bool:
    """An upasarga's r / ṣ precedes position k with only permitted vyavāya between."""
    for j in range(k - 1, -1, -1):
        v = tape[j][2]
        if v.slp1 in ("r", "z") and "upasarga_v" in v.tags:
            return True
        if v.slp1 in VYAVAYA_BLOCKERS:
            return False
    return False


def dhatu_upadesha(state) -> str:
    """The aupadeśika form of the dhātu on the tape (the merged pada keeps it as meta `dhatu_upadesha`)."""
    for t in state.terms:
        u = t.meta.get("dhatu_upadesha") or ("dhatu" in t.tags and t.meta.get("upadesha_slp1"))
        if u:
            return u
    return ""
