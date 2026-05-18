"""
6.4.39  न क्तिचि दीर्घश्च  —  VIDHI

Padaccheda: न क्तिचि दीर्घः च

न क्तिचि दीर्घश्च (6.4.39)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_39_na_39"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_39_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na ktici dIrGaSca",
    text_dev              = "न क्तिचि दीर्घश्च",
    padaccheda_dev        = "न क्तिचि दीर्घः च",
    why_dev               = "(सूत्रम् 6.4.39) न क्तिचि दीर्घश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
