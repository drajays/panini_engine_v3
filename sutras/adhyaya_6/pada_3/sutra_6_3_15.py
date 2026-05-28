"""
6.3.15  प्रावृट्शरत्कालदिवां जे  —  VIDHI

Padaccheda: प्रावृट्-शरत्-काल-दिवाम् जे

प्रावृट्शरत्कालदिवां जे (6.3.15)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_15_prAvfwSara_15"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.15"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.15",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prAvfwSaratkAladivAM je",
    text_dev              = "प्रावृट्शरत्कालदिवां जे",
    padaccheda_dev        = "प्रावृट्-शरत्-काल-दिवाम् जे",
    why_dev               = "(सूत्रम् 6.3.15) प्रावृट्शरत्कालदिवां जे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
