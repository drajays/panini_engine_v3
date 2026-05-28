"""
7.3.72  क्सस्याचि  —  VIDHI

Padaccheda: क्सस्य अचि

क्सस्याचि (7.3.72)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_72_ksasyAci_72"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.72", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_3_72_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ksasyAci",
    text_dev              = "क्सस्याचि",
    padaccheda_dev        = "क्सस्य अचि",
    why_dev               = "(सूत्रम् 7.3.72) क्सस्याचि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
