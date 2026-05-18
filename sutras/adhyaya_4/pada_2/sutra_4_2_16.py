"""
4.2.16  संस्कृतं भक्षाः  —  VIDHI

Padaccheda: संस्कृतम् भक्षाः

संस्कृतं भक्षाः (4.2.16)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_16_saMskftaM_16"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_16_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.16"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.16",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMskftaM BakzAH",
    text_dev              = "संस्कृतं भक्षाः",
    padaccheda_dev        = "संस्कृतम् भक्षाः",
    why_dev               = "(सूत्रम् 4.2.16) संस्कृतं भक्षाः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
