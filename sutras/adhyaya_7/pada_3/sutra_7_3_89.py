"""
7.3.89  उतो वृद्धिर्लुकि हलि  —  VIDHI

Padaccheda: उतः वृद्धिः लुकि हलि

उतो वृद्धिर्लुकि हलि (7.3.89)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_89_uto_89"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.89", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_3_89_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.89"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.89",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uto vfdDirluki hali",
    text_dev              = "उतो वृद्धिर्लुकि हलि",
    padaccheda_dev        = "उतः वृद्धिः लुकि हलि",
    why_dev               = "(सूत्रम् 7.3.89) उतो वृद्धिर्लुकि हलि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
