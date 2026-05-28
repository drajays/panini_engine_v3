"""
6.3.94  तिरसस्तिर्यलोपे  —  VIDHI

Padaccheda: तिरसः तिरि (लुप्तप्रथमान्तनिर्देशः) अलोपे

तिरसस्तिर्यलोपे (6.3.94)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_94_tirasastir_94"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.94"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tirasastiryalope",
    text_dev              = "तिरसस्तिर्यलोपे",
    padaccheda_dev        = "तिरसः तिरि (लुप्तप्रथमान्तनिर्देशः) अलोपे",
    why_dev               = "(सूत्रम् 6.3.94) तिरसस्तिर्यलोपे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
