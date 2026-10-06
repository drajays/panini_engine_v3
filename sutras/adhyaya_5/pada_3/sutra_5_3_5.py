"""
5.3.5  एतदोऽन्  —  VIDHI

Padaccheda: एतदः अन्

एतदोऽश् (5.3.5)
Pāṭha: ashtadhyayi.com data.txt row i=53005 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_5_etadoS_5"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.5", state, "5.3.2"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'etadon',
    text_dev              = 'एतदोऽन्',
    samagra_slp1          = "etadaH prAgdiSaH an",
    samagra_dev           = "एतदः प्राग्दिशः अन्",
    padaccheda_dev        = "एतदः अन्",
    why_dev               = "(सूत्रम् 5.3.5) एतदोऽश्।",
    anuvritti_from        = ('5.3.2',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
