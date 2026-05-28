"""
7.2.25  अभेश्चाविदूर्ये  —  VIDHI

Padaccheda: अभेः च आविदूर्ये

अभेश्चाविदूर्ये (7.2.25)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_25_aBeScAvidU_25"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.25", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_2_25_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.25"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aBeScAvidUrye",
    text_dev              = "अभेश्चाविदूर्ये",
    padaccheda_dev        = "अभेः च आविदूर्ये",
    why_dev               = "(सूत्रम् 7.2.25) अभेश्चाविदूर्ये।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
