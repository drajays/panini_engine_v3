"""
7.2.99  त्रिचतुरोः स्त्रियां तिसृचतसृ  —  VIDHI

Padaccheda: त्रि-चतुरोः स्त्रियाम् तिसृ-चतसृ (लुप्तप्रथमान्तनिर्देशः)

त्रिचतुरोः स्त्रियां तिसृचतसृ (7.2.99)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_99_tricaturoH_99"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_99_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.99"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tricaturoH striyAM tisfcatasf",
    text_dev              = "त्रिचतुरोः स्त्रियां तिसृचतसृ",
    padaccheda_dev        = "त्रि-चतुरोः स्त्रियाम् तिसृ-चतसृ (लुप्तप्रथमान्तनिर्देशः)",
    why_dev               = "(सूत्रम् 7.2.99) त्रिचतुरोः स्त्रियां तिसृचतसृ।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
