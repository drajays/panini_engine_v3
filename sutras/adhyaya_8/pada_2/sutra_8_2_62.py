"""
8.2.62  क्विन्प्रत्ययस्य कुः  —  VIDHI

Padaccheda: क्विन्-प्रत्ययस्य कुः

क्विन्प्रत्ययस्य कुः (8.2.62)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_62_kvinpratya_62"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_2_62_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kvinpratyayasya kuH",
    text_dev              = "क्विन्प्रत्ययस्य कुः",
    padaccheda_dev        = "क्विन्-प्रत्ययस्य कुः",
    why_dev               = "(सूत्रम् 8.2.62) क्विन्प्रत्ययस्य कुः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
