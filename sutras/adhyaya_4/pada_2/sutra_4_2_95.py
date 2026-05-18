"""
4.2.95  कत्त्र्यादिभ्यो ढकञ्  —  VIDHI

Padaccheda: कत्त्रि-आदिभ्यः ढकञ्

कत्त्र्यादिभ्यो ढकञ् (4.2.95)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_95_kattryAdiB_95"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_95_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kattryAdiByo QakaY",
    text_dev              = "कत्त्र्यादिभ्यो ढकञ्",
    padaccheda_dev        = "कत्त्रि-आदिभ्यः ढकञ्",
    why_dev               = "(सूत्रम् 4.2.95) कत्त्र्यादिभ्यो ढकञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
