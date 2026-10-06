"""
5.4.2  दण्डव्यवसर्गयोश्च  —  VIDHI

Padaccheda: दण्ड-व्यवसर्गयोः च

दण्डव्यवसर्गयोश्च (5.4.2)
Pāṭha: ashtadhyayi.com data.txt row i=54002 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_2_daRqavyava_2"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.2", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.2"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.2",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "daRqavyavasargayoSca",
    text_dev              = "दण्डव्यवसर्गयोश्च",
    samagra_slp1          = "saMKyAdeH pAda-Satasya daRqa-vyavasargayoH vun lopaH ca",
    samagra_dev           = "संख्यादेः पाद-शतस्य दण्ड-व्यवसर्गयोः वुन् लोपः च",
    padaccheda_dev        = "दण्ड-व्यवसर्गयोः च",
    why_dev               = "(सूत्रम् 5.4.2) दण्डव्यवसर्गयोश्च।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
