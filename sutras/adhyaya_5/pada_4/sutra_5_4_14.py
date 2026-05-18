"""
5.4.14  णचः स्त्रियामञ्  —  VIDHI

Padaccheda: णचः स्त्रियाम् अञ्

णचः स्त्रियामञ् (5.4.14)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_14_RacaH_14"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_14_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.14"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.14",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "RacaH striyAmaY",
    text_dev              = "णचः स्त्रियामञ्",
    padaccheda_dev        = "णचः स्त्रियाम् अञ्",
    why_dev               = "(सूत्रम् 5.4.14) णचः स्त्रियामञ्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
