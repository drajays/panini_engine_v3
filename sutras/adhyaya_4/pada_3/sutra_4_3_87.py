"""
4.3.87  अधिकृत्य कृते ग्रन्थे  —  VIDHI

Padaccheda: अधिकृत्य कृते ग्रन्थे

अधिकृत्य कृते ग्रन्थे (4.3.87)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_87_aDikftya_87"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_87_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.87"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.87",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aDikftya kfte granTe",
    text_dev              = "अधिकृत्य कृते ग्रन्थे",
    padaccheda_dev        = "अधिकृत्य कृते ग्रन्थे",
    why_dev               = "(सूत्रम् 4.3.87) अधिकृत्य कृते ग्रन्थे।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
