"""
4.4.42  प्रतिपथमेति ठंश्च  —  VIDHI

Padaccheda: प्रतिपथम् एति (क्रियापदम्) ठन् च

प्रतिपथमेति ठंश्च (4.4.42)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_42_pratipaTam_42"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_42_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pratipaTameti WaMSca",
    text_dev              = "प्रतिपथमेति ठंश्च",
    padaccheda_dev        = "प्रतिपथम् एति (क्रियापदम्) ठन् च",
    why_dev               = "(सूत्रम् 4.4.42) प्रतिपथमेति ठंश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
