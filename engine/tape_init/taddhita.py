"""engine/tape_init/taddhita.py — the start state of a taddhita derivation: the prātipadika as given, the intended meaning (vivakṣā) recorded."""
from __future__ import annotations

from engine.state import State, Term
from engine.vivaksha import set_vivaksha
from phonology.varna import parse_slp1_upadesha_sequence


def build_taddhita_state(stem_slp1: str, origin_tags: set[str] | None = None, **vivaksha: str) -> State:
    stem = Term(kind="prakriti", varnas=list(parse_slp1_upadesha_sequence(stem_slp1)), tags={"prātipadika"} | set(origin_tags or ()),
                meta={"upadesha_slp1": stem_slp1})
    state = State(terms=[stem], meta={}, trace=[])
    set_vivaksha(state, **vivaksha)
    return state
