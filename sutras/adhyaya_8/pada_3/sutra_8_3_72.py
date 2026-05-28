"""
8.3.72  अनुविपर्यभिनिभ्यः स्यन्दतेरप्राणिषु  —  VIDHI

Padaccheda: अनु-वि-परि-अभि-निभ्यः स्यन्दतेः अप्राणिषु

अनुविपर्यभिनिभ्यः स्यन्दतेरप्राणिषु (8.3.72)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_72_anuviparya_72"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_72_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anuviparyaBiniByaH syandateraprARizu",
    text_dev              = "अनुविपर्यभिनिभ्यः स्यन्दतेरप्राणिषु",
    padaccheda_dev        = "अनु-वि-परि-अभि-निभ्यः स्यन्दतेः अप्राणिषु",
    why_dev               = "(सूत्रम् 8.3.72) अनुविपर्यभिनिभ्यः स्यन्दतेरप्राणिषु।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
