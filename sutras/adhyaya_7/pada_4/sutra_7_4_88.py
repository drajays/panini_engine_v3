"""
7.4.88  उत् परस्यातः  —  VIDHI

Padaccheda: उत् परस्य अतः

उत् परस्यातः (7.4.88)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_88_ut_88"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.88", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_4_88_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.88"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ut parasyAtaH",
    text_dev              = "उत् परस्यातः",
    padaccheda_dev        = "उत् परस्य अतः",
    why_dev               = "(सूत्रम् 7.4.88) उत् परस्यातः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
