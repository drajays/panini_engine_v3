"""
4.4.19  निर्वृत्तेऽक्षद्यूतादिभ्यः  —  VIDHI

Padaccheda: निर्वृत्ते अक्ष-द्यूत-आदिभ्यः

निर्वृत्तेऽक्षद्यूतादिभ्यः (4.4.19)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_19_nirvfttek_19"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_19_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.19"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.19",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nirvftte'kzadyUtAdiByaH",
    text_dev              = "निर्वृत्तेऽक्षद्यूतादिभ्यः",
    padaccheda_dev        = "निर्वृत्ते अक्ष-द्यूत-आदिभ्यः",
    why_dev               = "(सूत्रम् 4.4.19) निर्वृत्तेऽक्षद्यूतादिभ्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
