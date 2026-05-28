"""
8.2.83  प्रत्यभिवादेअशूद्रे  —  VIDHI

Padaccheda: प्रत्यभिवादे अशूद्रे

प्रत्यभिवादेअशूद्रे (8.2.83)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_83_pratyaBivA_83"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.83"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pratyaBivAdeaSUdre",
    text_dev              = "प्रत्यभिवादेअशूद्रे",
    padaccheda_dev        = "प्रत्यभिवादे अशूद्रे",
    why_dev               = "(सूत्रम् 8.2.83) प्रत्यभिवादेअशूद्रे।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
