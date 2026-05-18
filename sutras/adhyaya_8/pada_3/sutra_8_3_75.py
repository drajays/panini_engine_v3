"""
8.3.75  परिस्कन्दः प्राच्यभरतेषु  —  VIDHI

Padaccheda: परिस्कन्दः प्राच्यभरतेषु

परिस्कन्दः प्राच्यभरतेषु (8.3.75)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_75_pariskanda_75"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_75_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.75"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.75",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pariskandaH prAcyaBaratezu",
    text_dev              = "परिस्कन्दः प्राच्यभरतेषु",
    padaccheda_dev        = "परिस्कन्दः प्राच्यभरतेषु",
    why_dev               = "(सूत्रम् 8.3.75) परिस्कन्दः प्राच्यभरतेषु।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
