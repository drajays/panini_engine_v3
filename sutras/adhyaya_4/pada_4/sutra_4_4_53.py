"""
4.4.53  किशरादिभ्यः ष्ठन्  —  VIDHI

Padaccheda: किशर-आदिभ्यः ष्ठन्

किशरादिभ्यः ष्ठन् (4.4.53)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_53_kiSarAdiBy_53"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_53_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kiSarAdiByaH zWan",
    text_dev              = "किशरादिभ्यः ष्ठन्",
    padaccheda_dev        = "किशर-आदिभ्यः ष्ठन्",
    why_dev               = "(सूत्रम् 4.4.53) किशरादिभ्यः ष्ठन्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
