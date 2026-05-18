"""
5.3.15  सर्वैकान्यकिंयत्तदः काले दा  —  VIDHI

Padaccheda: सर्व-एक-अन्य-किं-यद्-तदः काले दा

सर्वैकान्यकिंयत्तदः काले दा (5.3.15)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_15_sarvEkAnya_15"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_15_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.15"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.15",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sarvEkAnyakiMyattadaH kAle dA",
    text_dev              = "सर्वैकान्यकिंयत्तदः काले दा",
    padaccheda_dev        = "सर्व-एक-अन्य-किं-यद्-तदः काले दा",
    why_dev               = "(सूत्रम् 5.3.15) सर्वैकान्यकिंयत्तदः काले दा।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
