"""
4.4.30  प्रयच्छति गर्ह्यम्  —  VIDHI

Padaccheda: प्रयच्छति (क्रियापदम्) गर्ह्यम्

प्रयच्छति गर्ह्यम् (4.4.30)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_30_prayacCati_30"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_30_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.30"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.30",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prayacCati garhyam",
    text_dev              = "प्रयच्छति गर्ह्यम्",
    padaccheda_dev        = "प्रयच्छति (क्रियापदम्) गर्ह्यम्",
    why_dev               = "(सूत्रम् 4.4.30) प्रयच्छति गर्ह्यम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
