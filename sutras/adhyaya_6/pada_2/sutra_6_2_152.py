"""
6.2.152  सप्तम्याः पुण्यम्  —  VIDHI

Padaccheda: सप्तम्याः पुण्यम्

सप्तम्याः पुण्यम् (6.2.152)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_152_saptamyAH_152"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_152_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.152"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.152",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saptamyAH puRyam",
    text_dev              = "सप्तम्याः पुण्यम्",
    padaccheda_dev        = "सप्तम्याः पुण्यम्",
    why_dev               = "(सूत्रम् 6.2.152) सप्तम्याः पुण्यम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
