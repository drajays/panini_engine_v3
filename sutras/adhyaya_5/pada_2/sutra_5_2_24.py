"""
5.2.24  तस्य पाकमूले पील्वदिकर्णादिभ्यः कुणब्जाहचौ  —  VIDHI

Padaccheda: तस्य पाकमूले पीलु-आदि-कर्ण-आदिभ्यः कुणप्-जाहचौ

तस्य पाकमूले पील्वदिकर्णादिभ्यः कुणब्जाहचौ (5.2.24)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_24_tasya_24"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_24_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tasya pAkamUle pIlvadikarRAdiByaH kuRabjAhacO",
    text_dev              = "तस्य पाकमूले पील्वदिकर्णादिभ्यः कुणब्जाहचौ",
    padaccheda_dev        = "तस्य पाकमूले पीलु-आदि-कर्ण-आदिभ्यः कुणप्-जाहचौ",
    why_dev               = "(सूत्रम् 5.2.24) तस्य पाकमूले पील्वदिकर्णादिभ्यः कुणब्जाहचौ।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
