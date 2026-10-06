"""
4.4.65  हितं भक्षाः  —  VIDHI

Padaccheda: हितम् भक्षाः

हितं भक्षाः (4.4.65)
Pāṭha: ashtadhyayi.com data.txt row i=44065 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_65_hitaM_65"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.65", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.65"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hitaM BakzAH",
    text_dev              = "हितं भक्षाः",
    samagra_slp1          = "tat hitam BakzAH asya iti samarTAnAm praTamAt paraH Wak pratyayaH",
    samagra_dev           = "'तत् हितम् भक्षाः अस्य' (इति) समर्थानाम् प्रथमात् परः ठक् प्रत्ययः",
    padaccheda_dev        = "हितम् भक्षाः",
    why_dev               = "(सूत्रम् 4.4.65) हितं भक्षाः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
