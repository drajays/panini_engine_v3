"""
4.3.6  दिक्पूर्वपदाट्ठञ् च  —  VIDHI

Padaccheda: दिक्-पूर्वपदात् ठञ् च

दिक्पूर्वपदाट्ठञ् च (4.3.6)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_6_dikpUrvapa_6"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.6", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.6"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.6",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dikpUrvapadAwWaY ca",
    text_dev              = "दिक्पूर्वपदाट्ठञ् च",
    padaccheda_dev        = "दिक्-पूर्वपदात् ठञ् च",
    why_dev               = "(सूत्रम् 4.3.6) दिक्पूर्वपदाट्ठञ् च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
