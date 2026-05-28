"""
7.2.112  अनाप्यकः  —  VIDHI

Padaccheda: अन (लुप्तप्रथमान्तनिर्देशः) आपि अकः

अनाप्यकः (7.2.112)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_112_anApyakaH_112"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.112", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.112"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.112",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anApyakaH",
    text_dev              = "अनाप्यकः",
    padaccheda_dev        = "अन (लुप्तप्रथमान्तनिर्देशः) आपि अकः",
    why_dev               = "(सूत्रम् 7.2.112) अनाप्यकः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
