"""
8.1.36  यावद्यथाभ्याम्  —  VIDHI

Padaccheda: यावत्-यथाभ्याम्

यावद्यथाभ्याम् (8.1.36)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_36_yAvadyaTAB_36"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yAvadyaTAByAm",
    text_dev              = "यावद्यथाभ्याम्",
    padaccheda_dev        = "यावत्-यथाभ्याम्",
    why_dev               = "(सूत्रम् 8.1.36) यावद्यथाभ्याम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
