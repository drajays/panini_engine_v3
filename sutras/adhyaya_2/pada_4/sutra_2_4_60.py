"""
2.4.60  इञः प्राचाम्  —  VIDHI

Padaccheda: इञः प्राचाम्

inja suffix in eastern dialect context.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_60_inja_pracha"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_60_yuna_context") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["luk_kind"]             = "2.4.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "iYaH prAcAm",
    text_dev              = "इञः प्राचाम्",
    padaccheda_dev        = "इञः प्राचाम्",
    why_dev               = "इञः प्राचाम् (२.४.६०)।",
    anuvritti_from        = ('2.4.58',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
