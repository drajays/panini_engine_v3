"""engine/pada_ctx.py — what the pada-vidhāyaka sūtras of 1.3.12–1.3.93 read off the tape: the dhātu's upadeśa and the upasargas before it.
Not a sūtra, not a rule: a reader (like engine/vivaksha.py)."""
from __future__ import annotations

from engine.state import State


def root_and_upasargas(state: State):
    """(upadeśa of the dhātu Term, frozenset of the upadeśa strings of the upasarga Terms before it) or (None, frozenset())."""
    pre: set[str] = set()
    for t in state.terms:
        if "upasarga" in t.tags and "dhatu" not in t.tags:
            pre.add((t.meta.get("upadesha_slp1") or "").strip())
        elif "dhatu" in t.tags:
            return (t.meta.get("upadesha_slp1") or "").strip(), frozenset(pre)
    return None, frozenset()


def pada_site(state: State, roots: frozenset[str], upasargas: frozenset[str], stamp: str) -> bool:
    """The dhātu is one of ``roots`` and an upasarga of ``upasargas`` stands before it; this sūtra has not decided yet."""
    if state.meta.get(stamp):
        return False
    root, pre = root_and_upasargas(state)
    return root in roots and bool(pre & upasargas)


def decide(state: State, pada: str, stamp: str, registry_key: str) -> State:
    """Record the sūtra's pada decision (the recipe resolver lets a sense/upasarga-gated decision override the 1.3.78 gate)."""
    state.meta["pada"] = pada
    state.meta[stamp] = True
    state.meta["pada_by_sense"] = True
    state.samjna_registry[registry_key] = True
    return state
