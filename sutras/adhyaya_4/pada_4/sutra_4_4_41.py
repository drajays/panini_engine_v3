"""
4.4.41  धर्मं चरति  —  VIDHI

Padaccheda: धर्मम् चरति (क्रियापदम्)

धर्मं चरति (4.4.41)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_41_DarmaM_41"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_41_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.41"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.41",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "DarmaM carati",
    text_dev              = "धर्मं चरति",
    padaccheda_dev        = "धर्मम् चरति (क्रियापदम्)",
    why_dev               = "(सूत्रम् 4.4.41) धर्मं चरति।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
