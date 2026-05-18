"""
4.1.80  क्रौड्यादिभ्यश्च  —  VIDHI

Padaccheda: क्रौडि-आदिभ्यः च

क्रौड्यादिभ्यश्च (4.1.80)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_80_krOqyAdiBy_80"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_80_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "krOqyAdiByaSca",
    text_dev              = "क्रौड्यादिभ्यश्च",
    padaccheda_dev        = "क्रौडि-आदिभ्यः च",
    why_dev               = "(सूत्रम् 4.1.80) क्रौड्यादिभ्यश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
