"""
5.2.112  रजःकृष्यासुतिपरिषदो वलच्  —  VIDHI

Padaccheda: रजः-कृषि-असुति-परिषदः वलच्

रजःकृष्यासुतिपरिषदो वलच् (5.2.112)
Pāṭha: ashtadhyayi.com data.txt row i=52112 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_112_rajaHkfzyA_112"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.112", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.112"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.112",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rajaHkfzyAsutiparizado valac",
    text_dev              = "रजःकृष्यासुतिपरिषदो वलच्",
    samagra_slp1          = "tat asya asmin astIti iti rajas-kfzi-Asuti-parizadaH valac",
    samagra_dev           = "'तत् अस्य, अस्मिन् अस्तीति' (इति) रजस्-कृषि-आसुति-परिषदः वलच्",
    padaccheda_dev        = "रजः-कृषि-असुति-परिषदः वलच्",
    why_dev               = "(सूत्रम् 5.2.112) रजःकृष्यासुतिपरिषदो वलच्।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
