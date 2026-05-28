"""
7.4.97  ई च गणः  —  VIDHI

Padaccheda: ई (लुप्तप्रथमान्तनिर्देशः) च गणः

ई च गणः (7.4.97)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_97_I_97"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.97", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.97"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.97",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "I ca gaRaH",
    text_dev              = "ई च गणः",
    padaccheda_dev        = "ई (लुप्तप्रथमान्तनिर्देशः) च गणः",
    why_dev               = "(सूत्रम् 7.4.97) ई च गणः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
