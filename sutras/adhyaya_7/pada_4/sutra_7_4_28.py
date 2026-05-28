"""
7.4.28  रिङ् शयग्लिङ्क्षु  —  VIDHI

Padaccheda: रिङ् श-यक्-लिङ्‍क्षु

रिङ् शयग्लिङ्क्षु (7.4.28)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_28_riN_28"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.28", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_4_28_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "riN SayagliNkzu",
    text_dev              = "रिङ् शयग्लिङ्क्षु",
    padaccheda_dev        = "रिङ् श-यक्-लिङ्‍क्षु",
    why_dev               = "(सूत्रम् 7.4.28) रिङ् शयग्लिङ्क्षु।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
