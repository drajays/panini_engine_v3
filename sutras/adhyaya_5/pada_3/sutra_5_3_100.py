"""
5.3.100  देवपथादिभ्यश्च  —  VIDHI

Padaccheda: देवपथ-आदिभ्यः च

देवपथादिभ्यश्च (5.3.100)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_100_devapaTAdi_100"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_100_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.100"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.100",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "devapaTAdiByaSca",
    text_dev              = "देवपथादिभ्यश्च",
    padaccheda_dev        = "देवपथ-आदिभ्यः च",
    why_dev               = "(सूत्रम् 5.3.100) देवपथादिभ्यश्च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
