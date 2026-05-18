"""
3.2.174  भियः क्रुक्लुकनौ  —  VIDHI

Padaccheda: भियः क्रुक्-लुकनौ

krt-suffix rule: भियः क्रुक्लुकनौ (174)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_174_BiyaH_174"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_174_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.174"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.174",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BiyaH kruklukanO",
    text_dev              = "भियः क्रुक्लुकनौ",
    padaccheda_dev        = "भियः क्रुक्-लुकनौ",
    why_dev               = "धातोः कृत्-प्रत्ययः [भियः क्रुक्लुकनौ] विहितः (३.२.174)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
