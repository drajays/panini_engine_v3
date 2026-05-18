"""
5.2.100  लोमादिपामादिपिच्छादिभ्यः शनेलचः  —  VIDHI

Padaccheda: लोम-आदि-पाम-आदि-पिच्छ-आदिभ्यः श-न-इलचः

लोमादिपामादिपिच्छादिभ्यः शनेलचः (5.2.100)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_100_lomAdipAmA_100"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_100_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.100"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.100",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lomAdipAmAdipicCAdiByaH SanelacaH",
    text_dev              = "लोमादिपामादिपिच्छादिभ्यः शनेलचः",
    padaccheda_dev        = "लोम-आदि-पाम-आदि-पिच्छ-आदिभ्यः श-न-इलचः",
    why_dev               = "(सूत्रम् 5.2.100) लोमादिपामादिपिच्छादिभ्यः शनेलचः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
