"""
4.4.6  गोपुच्छाट्ठञ्  —  VIDHI

Padaccheda: गोपुच्छात् ठञ्

गोपुच्छाट्ठञ् (4.4.6)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_6_gopucCAwWa_6"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.6", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.6"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.6",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gopucCAwWaY",
    text_dev              = "गोपुच्छाट्ठञ्",
    padaccheda_dev        = "गोपुच्छात् ठञ्",
    why_dev               = "(सूत्रम् 4.4.6) गोपुच्छाट्ठञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
