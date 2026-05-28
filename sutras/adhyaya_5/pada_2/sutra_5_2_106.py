"""
5.2.106  दन्त उन्नत उरच्  —  VIDHI

Padaccheda: दन्तः (पञ्चम्यर्थे प्रथमा) उन्नतः उरच्

दन्त उन्नत उरच् (5.2.106)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_106_danta_106"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.106", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.106"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.106",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "danta unnata urac",
    text_dev              = "दन्त उन्नत उरच्",
    padaccheda_dev        = "दन्तः (पञ्चम्यर्थे प्रथमा) उन्नतः उरच्",
    why_dev               = "(सूत्रम् 5.2.106) दन्त उन्नत उरच्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
