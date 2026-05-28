"""
7.3.99  अड्गार्ग्यगालवयोः  —  VIDHI

Padaccheda: अट् गार्ग्यगालवयोः

अड्गार्ग्यगालवयोः (7.3.99)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_99_aqgArgyagA_99"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.99", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.99"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aqgArgyagAlavayoH",
    text_dev              = "अड्गार्ग्यगालवयोः",
    padaccheda_dev        = "अट् गार्ग्यगालवयोः",
    why_dev               = "(सूत्रम् 7.3.99) अड्गार्ग्यगालवयोः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
