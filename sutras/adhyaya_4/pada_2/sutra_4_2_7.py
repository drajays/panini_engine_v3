"""
4.2.7  दृष्ट्अं साम  —  VIDHI

Padaccheda: दृष्टम् साम

दृष्ट्अं साम (4.2.7)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_7_dfzwaM_7"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_7_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.7"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dfzwaM sAma",
    text_dev              = "दृष्ट्अं साम",
    padaccheda_dev        = "दृष्टम् साम",
    why_dev               = "(सूत्रम् 4.2.7) दृष्ट्अं साम।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
