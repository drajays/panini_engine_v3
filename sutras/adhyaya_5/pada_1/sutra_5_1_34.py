"""
5.1.34  पणपादमाषशताद्यत्  —  VIDHI

Padaccheda: पण-पाद-माष-शतात् यत्

पणपादमाषशतादत् (5.1.34)
Pāṭha: ashtadhyayi.com data.txt row i=51034 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_34_paRapAdamA_34"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.34", state, "5.1.19"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'paRapAdamAzaSatAdyat',
    text_dev              = 'पणपादमाषशताद्यत्',
    samagra_slp1          = "A-arhAt paRa-pAda-mAza-SatAt yat",
    samagra_dev           = "आ-अर्हात् पण-पाद-माष-शतात् यत्",
    padaccheda_dev        = "पण-पाद-माष-शतात् यत्",
    why_dev               = "(सूत्रम् 5.1.34) पणपादमाषशतादत्।",
    anuvritti_from        = ('5.1.19',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
