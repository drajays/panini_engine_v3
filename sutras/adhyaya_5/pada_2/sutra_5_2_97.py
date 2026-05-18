"""
5.2.97  सिध्मादिभ्यश्च  —  VIDHI

Padaccheda: सिध्म-आदिभ्यः च

सिध्मादिभ्यश्च (5.2.97)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_97_siDmAdiBya_97"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_97_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.97"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.97",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "siDmAdiByaSca",
    text_dev              = "सिध्मादिभ्यश्च",
    padaccheda_dev        = "सिध्म-आदिभ्यः च",
    why_dev               = "(सूत्रम् 5.2.97) सिध्मादिभ्यश्च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
