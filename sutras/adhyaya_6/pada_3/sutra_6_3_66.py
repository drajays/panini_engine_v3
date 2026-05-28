"""
6.3.66  खित्यनव्ययस्य  —  VIDHI

Padaccheda: खिति अन्-अव्ययस्य

खित्यनव्ययस्य (6.3.66)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_66_Kityanavya_66"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.66"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Kityanavyayasya",
    text_dev              = "खित्यनव्ययस्य",
    padaccheda_dev        = "खिति अन्-अव्ययस्य",
    why_dev               = "(सूत्रम् 6.3.66) खित्यनव्ययस्य।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
