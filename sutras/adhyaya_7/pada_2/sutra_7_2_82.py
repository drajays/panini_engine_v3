"""
7.2.82  आने मुक्  —  VIDHI

Padaccheda: आने मुक्

आने मुक् (7.2.82)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_82_Ane_82"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_82_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.82"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.82",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Ane muk",
    text_dev              = "आने मुक्",
    padaccheda_dev        = "आने मुक्",
    why_dev               = "(सूत्रम् 7.2.82) आने मुक्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
