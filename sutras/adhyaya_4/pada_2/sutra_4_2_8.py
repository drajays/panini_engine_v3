"""
4.2.8  कलेर्ढक्  —  VIDHI

Padaccheda: कलेः ढक्

कलेर्ढक् (4.2.8)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_8_kalerQak_8"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_8_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.8"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.8",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kalerQak",
    text_dev              = "कलेर्ढक्",
    padaccheda_dev        = "कलेः ढक्",
    why_dev               = "(सूत्रम् 4.2.8) कलेर्ढक्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
