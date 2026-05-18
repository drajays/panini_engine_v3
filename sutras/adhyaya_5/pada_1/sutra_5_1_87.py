"""
5.1.87  रात्र्यहस्संवत्सराच्च  —  VIDHI

Padaccheda: रात्रि-अहः-संवत्सरात् च

रात्र्यहस्संवत्सराच्च (5.1.87)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_87_rAtryahass_87"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_87_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.87"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.87",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rAtryahassaMvatsarAcca",
    text_dev              = "रात्र्यहस्संवत्सराच्च",
    padaccheda_dev        = "रात्रि-अहः-संवत्सरात् च",
    why_dev               = "(सूत्रम् 5.1.87) रात्र्यहस्संवत्सराच्च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
