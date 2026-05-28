"""
2.4.57  वा यौ  —  VIDHI

Padaccheda: वा यौ

Optional for yau.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "2_4_57_va_yau"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("2.4.57", state, "2.4.35")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA yO",
    text_dev              = "वा यौ",
    padaccheda_dev        = "वा यौ",
    why_dev               = "वा यौ (२.४.५७)।",
    anuvritti_from        = ('2.4.56',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
