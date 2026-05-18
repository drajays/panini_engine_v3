"""
5.2.101  प्रज्ञाश्रद्धाऽर्चावृत्तिभ्यो णः  —  VIDHI

Padaccheda: प्रज्ञा-श्रद्धा-अर्चा-वृत्तिभ्यः णः

प्रज्ञाश्रद्धाऽर्चावृत्तिभ्यो णः (5.2.101)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_101_prajYASrad_101"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_101_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.101"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.101",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prajYASradDA'rcAvfttiByo RaH",
    text_dev              = "प्रज्ञाश्रद्धाऽर्चावृत्तिभ्यो णः",
    padaccheda_dev        = "प्रज्ञा-श्रद्धा-अर्चा-वृत्तिभ्यः णः",
    why_dev               = "(सूत्रम् 5.2.101) प्रज्ञाश्रद्धाऽर्चावृत्तिभ्यो णः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
