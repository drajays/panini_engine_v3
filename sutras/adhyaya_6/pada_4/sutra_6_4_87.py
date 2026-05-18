"""
6.4.87  हुश्नुवोः सार्वधातुके  —  VIDHI

Padaccheda: हु-श्नुवोः सार्वधातुके

हुश्नुवोः सार्वधातुके (6.4.87)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_87_huSnuvoH_87"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_87_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.87"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.87",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "huSnuvoH sArvaDAtuke",
    text_dev              = "हुश्नुवोः सार्वधातुके",
    padaccheda_dev        = "हु-श्नुवोः सार्वधातुके",
    why_dev               = "(सूत्रम् 6.4.87) हुश्नुवोः सार्वधातुके।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
