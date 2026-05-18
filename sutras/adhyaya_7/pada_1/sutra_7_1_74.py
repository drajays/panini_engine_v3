"""
7.1.74  तृतीयाऽऽदिषु भाषितपुंस्कं पुंवद्गालवस्य  —  VIDHI

Padaccheda: तृतीया-आदिषु भाषितपुंस्कम् पुंवत् गालवस्य

तृतीयाऽऽदिषु भाषितपुंस्कं पुंवद्गालवस्य (7.1.74)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_1_74_tftIyAdi_74"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_1_74_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.74"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.74",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tftIyA''dizu BAzitapuMskaM puMvadgAlavasya",
    text_dev              = "तृतीयाऽऽदिषु भाषितपुंस्कं पुंवद्गालवस्य",
    padaccheda_dev        = "तृतीया-आदिषु भाषितपुंस्कम् पुंवत् गालवस्य",
    why_dev               = "(सूत्रम् 7.1.74) तृतीयाऽऽदिषु भाषितपुंस्कं पुंवद्गालवस्य।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
