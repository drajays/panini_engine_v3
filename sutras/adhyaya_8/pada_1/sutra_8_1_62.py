"""
8.1.62  चाहलोप एवेत्यवधारणम्  —  VIDHI

Padaccheda: च-अह-लोप एव इति अवधारणम्

चाहलोप एवेत्यवधारणम् (8.1.62)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_62_cAhalopa_62"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_1_62_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "cAhalopa evetyavaDAraRam",
    text_dev              = "चाहलोप एवेत्यवधारणम्",
    padaccheda_dev        = "च-अह-लोप एव इति अवधारणम्",
    why_dev               = "(सूत्रम् 8.1.62) चाहलोप एवेत्यवधारणम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
