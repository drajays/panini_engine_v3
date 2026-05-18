"""
7.2.67  वस्वेकाजाद्घसाम्  —  VIDHI

Padaccheda: वसु (लुप्तसप्तम्यन्तनिर्देशः) एक-अच्-आत्-घसाम्

वस्वेकाजाद्घसाम् (7.2.67)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_67_vasvekAjAd_67"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_67_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vasvekAjAdGasAm",
    text_dev              = "वस्वेकाजाद्घसाम्",
    padaccheda_dev        = "वसु (लुप्तसप्तम्यन्तनिर्देशः) एक-अच्-आत्-घसाम्",
    why_dev               = "(सूत्रम् 7.2.67) वस्वेकाजाद्घसाम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
