"""
5.1.99  सम्पादिनि  —  VIDHI

Padaccheda: सम्पादिनि

सम्पादिनि (5.1.99)
Pāṭha: ashtadhyayi.com data.txt row i=51099 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_99_sampAdini_99"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.99", state, "5.1.18"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.99"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sampAdini",
    text_dev              = "सम्पादिनि",
    samagra_slp1          = "tena sampAdini iti samarTAnAm praTamAt paraH WaY pratyayaH",
    samagra_dev           = "'तेन सम्पादिनि' (इति) समर्थानाम् प्रथमात् परः ठञ् प्रत्ययः",
    padaccheda_dev        = "सम्पादिनि",
    why_dev               = "(सूत्रम् 5.1.99) सम्पादिनि।",
    anuvritti_from        = ('5.1.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
