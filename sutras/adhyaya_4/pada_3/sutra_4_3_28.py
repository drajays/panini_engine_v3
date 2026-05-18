"""
4.3.28  पूर्वाह्णापराह्णार्द्रामूलप्रदोषावस्कराद्वुन्  —  VIDHI

Padaccheda: पूर्वाह्ण-अपराह्ण-आर्द्रा-मूल-प्रदोष-अवस्करात् वुन्

पूर्वाह्णापराह्णार्द्रामूलप्रदोषावस्कराद्वुन् (4.3.28)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_28_pUrvAhRApa_28"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_28_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUrvAhRAparAhRArdrAmUlapradozAvaskarAdvun",
    text_dev              = "पूर्वाह्णापराह्णार्द्रामूलप्रदोषावस्कराद्वुन्",
    padaccheda_dev        = "पूर्वाह्ण-अपराह्ण-आर्द्रा-मूल-प्रदोष-अवस्करात् वुन्",
    why_dev               = "(सूत्रम् 4.3.28) पूर्वाह्णापराह्णार्द्रामूलप्रदोषावस्कराद्वुन्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
