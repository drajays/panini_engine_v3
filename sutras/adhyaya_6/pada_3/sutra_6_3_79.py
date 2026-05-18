"""
6.3.79  ग्रन्थान्ताधिके च  —  VIDHI

Padaccheda: ग्रन्थान्त-अधिके च

ग्रन्थान्ताधिके च (6.3.79)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_79_granTAntAD_79"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_79_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.79"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.79",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "granTAntADike ca",
    text_dev              = "ग्रन्थान्ताधिके च",
    padaccheda_dev        = "ग्रन्थान्त-अधिके च",
    why_dev               = "(सूत्रम् 6.3.79) ग्रन्थान्ताधिके च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
