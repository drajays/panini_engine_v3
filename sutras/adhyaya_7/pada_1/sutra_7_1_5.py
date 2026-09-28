"""
7.1.5  आत्मनेपदेष्वनतः  —  VIDHI

Padaccheda: आत्मनेपदेषु अन्-अतः

आत्मनेपदेष्वनतः (7.1.5)
"""
from __future__ import annotations
from phonology import mk

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_1_5_Atmanepade_5"


def _find(state: State) -> int | None:
    """आत्मनेपदेष्वनतः: in ātmanepada, the jh of jha/jhe/jhām becomes at (not
    ant, 7.1.3) after an aṅga not ending in a — आसते, शासते, कंसते."""
    for i, t in enumerate(state.terms):
        if "tin_adesha_3_4_78" not in t.tags or not t.varnas or t.varnas[0].slp1 != "J":
            continue
        prev = next((u for u in reversed(state.terms[:i]) if u.varnas), None)
        if prev is not None and prev.varnas[-1].slp1 != "a":
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas = [mk("a"), mk("t")] + list(t.varnas[1:])
    t.meta["upadesha_slp1"] = "at" + (t.meta.get("upadesha_slp1") or "")[1:]
    t.tags.discard("upadesha")
    return state

SUTRA = SutraRecord(
    sutra_id              = "7.1.5",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "AtmanepadezvanataH",
    text_dev              = "आत्मनेपदेष्वनतः",
    padaccheda_dev        = "आत्मनेपदेषु अन्-अतः",
    why_dev               = "(सूत्रम् 7.1.5) आत्मनेपदेष्वनतः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
