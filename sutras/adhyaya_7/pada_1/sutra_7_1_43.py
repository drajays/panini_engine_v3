"""
7.1.43  यजध्वैनमिति च  —  VIDHI

Padaccheda: यजध्वैनम् इति च

यजध्वैनमिति च (7.1.43)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_1_43_yajaDvEnam_43"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.1.43", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.43"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yajaDvEnamiti ca",
    text_dev              = "यजध्वैनमिति च",
    padaccheda_dev        = "यजध्वैनम् इति च",
    why_dev               = "(सूत्रम् 7.1.43) यजध्वैनमिति च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
