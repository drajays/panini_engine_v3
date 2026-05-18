"""
6.3.107  कवं चोष्णे  —  VIDHI

Padaccheda: कवम् च उष्णे

कवं चोष्णे (6.3.107)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_107_kavaM_107"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_107_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.107"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.107",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kavaM cozRe",
    text_dev              = "कवं चोष्णे",
    padaccheda_dev        = "कवम् च उष्णे",
    why_dev               = "(सूत्रम् 6.3.107) कवं चोष्णे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
