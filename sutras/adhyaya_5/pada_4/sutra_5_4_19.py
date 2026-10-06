"""
5.4.19  एकस्य सकृच्च  —  VIDHI

Padaccheda: एकस्य सकृत् च

एकस्य सकृच्च (5.4.19)
Pāṭha: ashtadhyayi.com data.txt row i=54019 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_19_ekasya_19"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.19", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.19"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.19",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ekasya sakfcca",
    text_dev              = "एकस्य सकृच्च",
    samagra_slp1          = "kriyAgaRane ekasya sakft suc ca",
    samagra_dev           = "क्रियागणने एकस्य सकृत्,   सुच् च",
    padaccheda_dev        = "एकस्य सकृत् च",
    why_dev               = "(सूत्रम् 5.4.19) एकस्य सकृच्च।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
