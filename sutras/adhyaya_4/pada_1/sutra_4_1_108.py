"""
4.1.108  वतण्डाच्च  —  VIDHI

Padaccheda: वतण्डात् च

वतण्डाच्च (4.1.108)
Pāṭha: ashtadhyayi.com data.txt row i=41108 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_108_vataRqAcca_108"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.108", state, "4.1.92"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.108"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.108",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vataRqAcca",
    text_dev              = "वतण्डाच्च",
    samagra_slp1          = "tasya gotre apatyam iti vataRqAt ANgirase yaY",
    samagra_dev           = "'तस्य गोत्रे अपत्यम्' (इति) वतण्डात् आङ्गिरसे यञ्",
    padaccheda_dev        = "वतण्डात् च",
    why_dev               = "(सूत्रम् 4.1.108) वतण्डाच्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
