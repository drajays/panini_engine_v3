"""
6.2.74  प्राचां क्रीडायाम्  —  VIDHI

Padaccheda: प्राचाम् क्रीडायाम्

प्राचां क्रीडायाम् (6.2.74)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_74_prAcAM_74"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_74_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.74"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.74",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prAcAM krIqAyAm",
    text_dev              = "प्राचां क्रीडायाम्",
    padaccheda_dev        = "प्राचाम् क्रीडायाम्",
    why_dev               = "(सूत्रम् 6.2.74) प्राचां क्रीडायाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
