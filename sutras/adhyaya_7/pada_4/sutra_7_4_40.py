"""
7.4.40  द्यतिस्यतिमास्थामित्ति किति  —  VIDHI

Padaccheda: द्यति-स्यति-मा-स्थाम् इत् ति किति

द्यतिस्यतिमास्थामित्ति किति (7.4.40)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_40_dyatisyati_40"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.40", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_4_40_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.40"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.40",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dyatisyatimAsTAmitti kiti",
    text_dev              = "द्यतिस्यतिमास्थामित्ति किति",
    padaccheda_dev        = "द्यति-स्यति-मा-स्थाम् इत् ति किति",
    why_dev               = "(सूत्रम् 7.4.40) द्यतिस्यतिमास्थामित्ति किति।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
