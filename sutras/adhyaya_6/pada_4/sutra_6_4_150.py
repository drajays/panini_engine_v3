"""
6.4.150  हलस्तद्धितस्य  —  VIDHI

Padaccheda: हलः तद्धितस्य

हलस्तद्धितस्य (6.4.150)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_150_halastadDi_150"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.150", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.150"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.150",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "halastadDitasya",
    text_dev              = "हलस्तद्धितस्य",
    padaccheda_dev        = "हलः तद्धितस्य",
    why_dev               = "(सूत्रम् 6.4.150) हलस्तद्धितस्य।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
