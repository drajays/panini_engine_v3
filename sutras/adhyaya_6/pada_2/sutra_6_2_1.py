"""
6.2.1  बहुव्रीहौ प्रकृत्या पूर्वपदम्  —  VIDHI

Padaccheda: बहुव्रीहौ प्रकृत्या पूर्वपदम्

बहुव्रीहौ प्रकृत्या पूर्वपदम् (6.2.1)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_1_bahuvrIhO_1"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_1_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.1"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.1",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahuvrIhO prakftyA pUrvapadam",
    text_dev              = "बहुव्रीहौ प्रकृत्या पूर्वपदम्",
    padaccheda_dev        = "बहुव्रीहौ प्रकृत्या पूर्वपदम्",
    why_dev               = "(सूत्रम् 6.2.1) बहुव्रीहौ प्रकृत्या पूर्वपदम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
