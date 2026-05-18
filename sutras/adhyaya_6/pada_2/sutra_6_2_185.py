"""
6.2.185  अभेर्मुखम्  —  VIDHI

Padaccheda: अभेः मुखम्

अभेर्मुखम् (6.2.185)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_185_aBermuKam_185"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_185_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.185"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.185",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aBermuKam",
    text_dev              = "अभेर्मुखम्",
    padaccheda_dev        = "अभेः मुखम्",
    why_dev               = "(सूत्रम् 6.2.185) अभेर्मुखम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
