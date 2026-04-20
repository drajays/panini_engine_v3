"""
engine/gates.py — Scope, asiddha, and block gates.
─────────────────────────────────────────────────────

These are the policy checks that sit BEFORE any executor runs.
They are invoked by engine/dispatcher.py.  They NEVER mutate the state.
"""
from __future__ import annotations

from engine.sutra_type import SutraRecord, SutraType
from engine.state      import State


# ═════════════════════════════════════════════════════════════════════════
# Adhikāra gate
# ═════════════════════════════════════════════════════════════════════════

def adhikara_in_effect(sutra_id: str, state: State, adhikara_id: str) -> bool:
    """
    Returns True iff adhikara_id is currently on the stack AND its
    scope covers sutra_id.

    Called by sūtras whose application depends on an adhikāra being
    open (e.g. 6.4.148 requires 6.4.1 'aṅgasya').
    """
    sid_tuple = _id_to_tuple(sutra_id)
    for entry in state.adhikara_stack:
        if entry["id"] != adhikara_id:
            continue
        end = entry.get("scope_end") or ""
        if end == "":
            return True  # open-ended adhikāra
        return _id_to_tuple(adhikara_id) <= sid_tuple <= _id_to_tuple(end)
    return False


def purge_closed_adhikaras(sutra_id: str, state: State) -> None:
    """
    Remove adhikāra entries whose scope has already ended before sutra_id.
    Call this at the top of the dispatcher so stale entries do not leak.
    """
    sid = _id_to_tuple(sutra_id)
    state.adhikara_stack[:] = [
        e for e in state.adhikara_stack
        if e.get("scope_end", "") == "" or _id_to_tuple(e["scope_end"]) >= sid
    ]


# ═════════════════════════════════════════════════════════════════════════
# Tripāḍī / asiddha gate (8.2.1 pūrvatrāsiddham)
# ═════════════════════════════════════════════════════════════════════════

TRIPADI_START = (8, 2, 1)
TRIPADI_END   = (8, 4, 68)


def is_tripadi(sutra_id: str) -> bool:
    return TRIPADI_START <= _id_to_tuple(sutra_id) <= TRIPADI_END


def asiddha_violates(candidate_sutra_id: str, state: State) -> bool:
    """
    Asiddha gate. Once we are in the Tripāḍī zone, the effects of
    later Tripāḍī sūtras are asiddha (invisible) to earlier sūtras.

    Returns True iff the candidate is a NON-tripāḍī sūtra trying to
    fire while we are already in the tripāḍī zone — that is a
    constitutional violation.
    """
    if not state.tripadi_zone:
        return False
    return not is_tripadi(candidate_sutra_id)


# ═════════════════════════════════════════════════════════════════════════
# Pratiṣedha gate
# ═════════════════════════════════════════════════════════════════════════

def is_blocked(sutra_id: str, state: State) -> bool:
    return sutra_id in state.blocked_sutras


# ═════════════════════════════════════════════════════════════════════════
# Nipātana freeze
# ═════════════════════════════════════════════════════════════════════════

def is_frozen_by_nipatana(stype: SutraType, state: State) -> bool:
    """
    NIPATANA freezes form-mutating subsequent rules.  v3.1: consults
    the centralized frozenset engine.sutra_type.NIPATANA_FROZEN so the
    policy is auditable in one place.
    """
    if not state.nipatana_flag:
        return False
    from engine.sutra_type import NIPATANA_FROZEN
    return stype in NIPATANA_FROZEN


# ═════════════════════════════════════════════════════════════════════════
# Helpers
# ═════════════════════════════════════════════════════════════════════════

def _id_to_tuple(sid: str) -> tuple:
    try:
        return tuple(int(p) for p in sid.split("."))
    except Exception as e:
        raise ValueError(f"malformed sutra id {sid!r}: {e}")
