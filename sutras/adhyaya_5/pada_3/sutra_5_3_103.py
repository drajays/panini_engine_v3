"""
5.3.103  शाखादिभ्यो यत्  —  VIDHI

Padaccheda: शाखा-आदिभ्यः यत्

शाखाऽऽदिभ्यो यत् (5.3.103)
Pāṭha: ashtadhyayi.com data.txt row i=53103 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_103_SAKAdiBy_103"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.103", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.103"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'SAKAdiByo yat',
    text_dev              = 'शाखादिभ्यो यत्',
    samagra_slp1          = "SAKAdiByaH ive yat",
    samagra_dev           = "शाखादिभ्यः इवे यत्",
    padaccheda_dev        = "शाखा-आदिभ्यः यत्",
    why_dev               = "(सूत्रम् 5.3.103) शाखाऽऽदिभ्यो यत्।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
