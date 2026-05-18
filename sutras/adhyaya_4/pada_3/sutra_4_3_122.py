"""
4.3.122  पत्त्रपूर्वादञ्  —  VIDHI

Padaccheda: पत्त्र-पूर्वात् अञ्

पत्त्रपूर्वादञ् (4.3.122)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_122_pattrapUrv_122"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_122_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.122"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.122",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pattrapUrvAdaY",
    text_dev              = "पत्त्रपूर्वादञ्",
    padaccheda_dev        = "पत्त्र-पूर्वात् अञ्",
    why_dev               = "(सूत्रम् 4.3.122) पत्त्रपूर्वादञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
