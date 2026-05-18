"""
5.1.125  स्तेनाद्यन्नलोपश्च  —  VIDHI

Padaccheda: स्तेनात् यत् नलोपः च

स्तेनाद्यन्नलोपश्च (5.1.125)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_125_stenAdyann_125"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_125_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.125"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.125",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "stenAdyannalopaSca",
    text_dev              = "स्तेनाद्यन्नलोपश्च",
    padaccheda_dev        = "स्तेनात् यत् नलोपः च",
    why_dev               = "(सूत्रम् 5.1.125) स्तेनाद्यन्नलोपश्च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
