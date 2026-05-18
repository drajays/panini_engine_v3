"""
2.1.59  श्रेण्यादयः कृतादिभिः  —  VIDHI

Padaccheda: श्रेणि-आदयः कृत-आदिभिः

sreni etc. with krta-adi form karmadharaya compound.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_59_sreni_krta"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_1_59_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SreRyAdayaH kftAdiBiH",
    text_dev              = "श्रेण्यादयः कृतादिभिः",
    padaccheda_dev        = "श्रेणि-आदयः कृत-आदिभिः",
    why_dev               = "श्रेणि-आदयः कृत-आदिभिः सह कर्मधारयः (२.१.५९)।",
    anuvritti_from        = ('2.1.57',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
