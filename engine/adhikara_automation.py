"""
engine/adhikara_automation.py — Phase-driven adhikāra stack helpers.

Pipelines / tape initializers call these to open scopes that sūtra ``cond()``
functions consult via ``adhikara_in_effect``.
"""
from __future__ import annotations

from engine.state import State


def _push_adhikara(state: State, adhikara_id: str, scope_end: str = "") -> None:
    for entry in state.adhikara_stack:
        if entry.get("id") == adhikara_id:
            return
    state.adhikara_stack.append({"id": adhikara_id, "scope_end": scope_end})


def ensure_adhikara_for_phase(state: State, phase: str) -> State:
    """
    Open adhikāra frames appropriate to ``phase`` and derivation class.

    Idempotent — safe to call multiple times.
    """
    dc = (state.meta.get("derivation_class") or "").strip()

    if phase == "upadesha":
        _push_adhikara(state, "1.3.1", "1.3.9")

    if phase == "pratyaya":
        if dc in {"krdanta", "taddhita"} or any(
            "krdanta_pending" in t.tags for t in state.terms
        ):
            _push_adhikara(state, "3.1.1", "3.4.117")
        if dc == "tinanta":
            _push_adhikara(state, "3.1.1", "3.4.117")

    if phase == "angakarya":
        _push_adhikara(state, "6.4.1", "6.4.148")

    return state
