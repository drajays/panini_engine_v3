"""
6.2.34  राजन्यबहुवचनद्वंद्वेऽन्धकवृष्णिषु  —  VIDHI

Padaccheda: राजन्य-बहुवचन-द्वन्द्वे अन्धक-वृष्णिषु

राजन्यबहुवचनद्वंद्वेऽन्धकवृष्णिषु (6.2.34)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_34_rAjanyabah_34"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_34_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rAjanyabahuvacanadvaMdve'nDakavfzRizu",
    text_dev              = "राजन्यबहुवचनद्वंद्वेऽन्धकवृष्णिषु",
    padaccheda_dev        = "राजन्य-बहुवचन-द्वन्द्वे अन्धक-वृष्णिषु",
    why_dev               = "(सूत्रम् 6.2.34) राजन्यबहुवचनद्वंद्वेऽन्धकवृष्णिषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
