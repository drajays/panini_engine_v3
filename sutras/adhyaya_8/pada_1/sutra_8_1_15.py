"""
8.1.15  द्वन्द्वं रहस्यमर्यादावचनव्युत्क्रमणयज्ञपात्रप्रयोगाभिव्यक्तिषु  —  VIDHI

Padaccheda: द्वन्द्वम् रहस्य-मर्यादावचन-व्युत्क्रमण-यज्ञपात्रप्रयोग-अभिव्यक्तिषु

द्वन्द्वं रहस्यमर्यादावचनव्युत्क्रमणयज्ञपात्रप्रयोगाभिव्यक्तिषु (8.1.15)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_15_dvandvaM_15"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.15"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.15",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvandvaM rahasyamaryAdAvacanavyutkramaRayajYapAtraprayogABivyaktizu",
    text_dev              = "द्वन्द्वं रहस्यमर्यादावचनव्युत्क्रमणयज्ञपात्रप्रयोगाभिव्यक्तिषु",
    padaccheda_dev        = "द्वन्द्वम् रहस्य-मर्यादावचन-व्युत्क्रमण-यज्ञपात्रप्रयोग-अभिव्यक्तिषु",
    why_dev               = "(सूत्रम् 8.1.15) द्वन्द्वं रहस्यमर्यादावचनव्युत्क्रमणयज्ञपात्रप्रयोगाभिव्यक्तिषु।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
