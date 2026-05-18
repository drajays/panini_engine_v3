"""
5.3.63  अन्तिकबाढयोर्नेदसाधौ  —  VIDHI

Padaccheda: अन्तिक-बाढयोः नेद-साधौ

अन्तिकबाढयोर्नेदसाधौ (5.3.63)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_63_antikabAQa_63"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_63_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.63"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "antikabAQayornedasADO",
    text_dev              = "अन्तिकबाढयोर्नेदसाधौ",
    padaccheda_dev        = "अन्तिक-बाढयोः नेद-साधौ",
    why_dev               = "(सूत्रम् 5.3.63) अन्तिकबाढयोर्नेदसाधौ।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
