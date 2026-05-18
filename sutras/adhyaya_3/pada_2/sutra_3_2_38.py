"""
3.2.38  प्रियवशे वदः खच्  —  VIDHI

Padaccheda: प्रिय-वशे वदः खच्

krt-suffix rule: प्रियवशे वदः खच् (38)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_38_priyavaSe_38"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_38_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "priyavaSe vadaH Kac",
    text_dev              = "प्रियवशे वदः खच्",
    padaccheda_dev        = "प्रिय-वशे वदः खच्",
    why_dev               = "धातोः कृत्-प्रत्ययः [प्रियवशे वदः खच्] विहितः (३.२.38)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
