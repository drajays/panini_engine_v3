"""
7.2.72  स्तुसुधूञ्भ्यः परस्मैपदेषु  —  VIDHI

Padaccheda: स्तु-सु-धूञ्भ्यः परस्मैपदेषु

स्तुसुधूञ्भ्यः परस्मैपदेषु (7.2.72)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_72_stusuDUYBy_72"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.72", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "stusuDUYByaH parasmEpadezu",
    text_dev              = "स्तुसुधूञ्भ्यः परस्मैपदेषु",
    padaccheda_dev        = "स्तु-सु-धूञ्भ्यः परस्मैपदेषु",
    why_dev               = "(सूत्रम् 7.2.72) स्तुसुधूञ्भ्यः परस्मैपदेषु।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
