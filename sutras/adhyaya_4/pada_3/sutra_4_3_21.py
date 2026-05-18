"""
4.3.21  हेमन्ताच्च  —  VIDHI

Padaccheda: हेमन्तात् च

हेमन्ताच्च (4.3.21)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_21_hemantAcca_21"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_21_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hemantAcca",
    text_dev              = "हेमन्ताच्च",
    padaccheda_dev        = "हेमन्तात् च",
    why_dev               = "(सूत्रम् 4.3.21) हेमन्ताच्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
