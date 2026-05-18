"""
4.4.16  भस्त्राऽऽदिभ्यः ष्ठन्  —  VIDHI

Padaccheda: भस्त्रा-आदिभ्यः ष्ठन्

भस्त्राऽऽदिभ्यः ष्ठन् (4.4.16)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_16_BastrAdi_16"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_16_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.16"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.16",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BastrA''diByaH zWan",
    text_dev              = "भस्त्राऽऽदिभ्यः ष्ठन्",
    padaccheda_dev        = "भस्त्रा-आदिभ्यः ष्ठन्",
    why_dev               = "(सूत्रम् 4.4.16) भस्त्राऽऽदिभ्यः ष्ठन्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
