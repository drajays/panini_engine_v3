"""
6.4.158  बहोर्लोपो भू च बहोः  —  VIDHI

Padaccheda: बहोः लोपः भू (लुप्तप्रथमान्तनिर्देशः) च बहोः

बहोर्लोपो भू च बहोः (6.4.158)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_158_bahorlopo_158"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.158", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.158"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.158",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahorlopo BU ca bahoH",
    text_dev              = "बहोर्लोपो भू च बहोः",
    padaccheda_dev        = "बहोः लोपः भू (लुप्तप्रथमान्तनिर्देशः) च बहोः",
    why_dev               = "(सूत्रम् 6.4.158) बहोर्लोपो भू च बहोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
