"""
4.1.37  वृषाकप्यग्निकुसितकुसीदानामुदात्तः  —  VIDHI

Padaccheda: वृषाकपी-अग्नि-कुसित-कुसीदानाम् उदात्तः

वृषाकप्यग्निकुसितकुसीदानामुदात्तः (4.1.37)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_37_vfzAkapyag_37"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.37", state, "4.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.37"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.37",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vfzAkapyagnikusitakusIdAnAmudAttaH",
    text_dev              = "वृषाकप्यग्निकुसितकुसीदानामुदात्तः",
    padaccheda_dev        = "वृषाकपी-अग्नि-कुसित-कुसीदानाम् उदात्तः",
    why_dev               = "(सूत्रम् 4.1.37) वृषाकप्यग्निकुसितकुसीदानामुदात्तः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
