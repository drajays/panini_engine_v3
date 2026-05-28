"""
4.2.101  द्युप्रागपागुदक्प्रतीचो यत्  —  VIDHI

Padaccheda: द्यु-प्राक्-अपाक्-उदक्-प्रतीचः यत्

द्युप्रागपागुदक्प्रतीचो यत् (4.2.101)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_101_dyuprAgapA_101"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.101", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.101"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.101",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dyuprAgapAgudakpratIco yat",
    text_dev              = "द्युप्रागपागुदक्प्रतीचो यत्",
    padaccheda_dev        = "द्यु-प्राक्-अपाक्-उदक्-प्रतीचः यत्",
    why_dev               = "(सूत्रम् 4.2.101) द्युप्रागपागुदक्प्रतीचो यत्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
