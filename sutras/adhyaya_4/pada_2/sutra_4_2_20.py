"""
4.2.20  क्षीराड्ढञ्  —  VIDHI

Padaccheda: क्षीरात् ढञ्

क्षीराड्ढञ् (4.2.20)
Pāṭha: ashtadhyayi.com data.txt row i=42020 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_20_kzIrAqQaY_20"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.20", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kzIrAqQaY",
    text_dev              = "क्षीराड्ढञ्",
    samagra_slp1          = "tatra saMskftaM BakzAH iti kzIrAt QaY",
    samagra_dev           = "'तत्र संस्कृतं भक्षाः' (इति) क्षीरात् ढञ्",
    padaccheda_dev        = "क्षीरात् ढञ्",
    why_dev               = "(सूत्रम् 4.2.20) क्षीराड्ढञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
