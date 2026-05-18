"""
3.2.19  पूर्वे कर्तरि  —  VIDHI

Padaccheda: पूर्वे कर्तरि

krt-suffix rule: पूर्वे कर्तरि (19)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_19_pUrve_19"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_19_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.19"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.19",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUrve kartari",
    text_dev              = "पूर्वे कर्तरि",
    padaccheda_dev        = "पूर्वे कर्तरि",
    why_dev               = "धातोः कृत्-प्रत्ययः [पूर्वे कर्तरि] विहितः (३.२.19)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
