"""
4.2.34  कालेभ्यो भववत्  —  VIDHI

Padaccheda: कालेभ्यः भव-वत्

कालेभ्यो भववत् (4.2.34)
Pāṭha: ashtadhyayi.com data.txt row i=42034 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_34_kAleByo_34"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.34", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.34",
    sutra_type            = SutraType.ATIDESHA,
    r1_form_identity_exempt = True,
    text_slp1             = "kAleByo Bavavat",
    text_dev              = "कालेभ्यो भववत्",
    samagra_slp1          = "sA asya devatA iti kAleByaH Bavavat",
    samagra_dev           = "'सा अस्य देवता' (इति)  कालेभ्यः भववत्",
    padaccheda_dev        = "कालेभ्यः भव-वत्",
    why_dev               = "(सूत्रम् 4.2.34) कालेभ्यो भववत्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
