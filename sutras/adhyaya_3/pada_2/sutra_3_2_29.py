"""
3.2.29  नासिकास्तनयोर्ध्माधेटोः  —  VIDHI

Padaccheda: नासिका-स्तनयोः ध्मा-धेटोः

krt-suffix rule: नासिकास्तनयोर्ध्माधेटोः (29)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_29_nAsikAstan_29"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_29_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nAsikAstanayorDmADewoH",
    text_dev              = "नासिकास्तनयोर्ध्माधेटोः",
    padaccheda_dev        = "नासिका-स्तनयोः ध्मा-धेटोः",
    why_dev               = "धातोः कृत्-प्रत्ययः [नासिकास्तनयोर्ध्माधेटोः] विहितः (३.२.29)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
