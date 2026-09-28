"""
3.1.83  हलः श्नः शानज्झौ  —  VIDHI

Padaccheda: हलः श्नः शानच् हौ

Krt suffix rule from dhatu: हलः श्नः शानज्झौ (83)
"""
from __future__ import annotations
from phonology.varna import parse_slp1_upadesha_sequence

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_83_halaH_83"


_HAL = frozenset("kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh")


def _find(state: State) -> int | None:
    """हलः श्नः शानज्झौ: after a hal-final root, śnā → शानच् (आन) before हि —
    स्कुभान, गृहाण (हि then drops after a by 6.4.105)."""
    for i, t in enumerate(state.terms[:-1]):
        if "SnA_vikaraṇa" not in t.tags or t.meta.get("3_1_83_done"):
            continue
        dh = next((u for u in reversed(state.terms[:i]) if "dhatu" in u.tags), None)
        if dh is None or not dh.varnas or dh.varnas[-1].slp1 not in _HAL:
            return None
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is not None and "".join(v.slp1 for v in nxt.varnas) == "hi":
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas = list(parse_slp1_upadesha_sequence("Ana"))     # शानच् after it-lopa
    t.meta["upadesha_slp1"] = "SAnac"
    t.meta["3_1_83_done"] = True
    t.tags.discard("upadesha")
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.83",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "halaH SnaH SAnajJO",
    text_dev              = "हलः श्नः शानज्झौ",
    padaccheda_dev        = "हलः श्नः शानच् हौ",
    why_dev               = "धातोः [हलः श्नः शानज्झौ]-प्रत्ययः विहितः (३.१.83)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
