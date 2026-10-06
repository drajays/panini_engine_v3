"""
5.1.95  तस्य च दक्षिणा यज्ञाख्येभ्यः  —  VIDHI

Padaccheda: तस्य च दक्षिणा यज्ञाख्येभ्यः

तस्य च दक्षिणा यज्ञाख्येभ्यः (5.1.95)
Pāṭha: ashtadhyayi.com data.txt row i=51095 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_95_tasya_95"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.95", state, "5.1.78"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tasya ca dakziRA yajYAKyeByaH",
    text_dev              = "तस्य च दक्षिणा यज्ञाख्येभ्यः",
    samagra_slp1          = "tasya dakziRA iti yajYAKyeByaH samarTAnAM praTamAt paraH WaY pratyayaH",
    samagra_dev           = "'तस्य दक्षिणा' (इति) यज्ञाख्येभ्यः समर्थानां प्रथमात् परः ठञ् प्रत्ययः",
    padaccheda_dev        = "तस्य च दक्षिणा यज्ञाख्येभ्यः",
    why_dev               = "(सूत्रम् 5.1.95) तस्य च दक्षिणा यज्ञाख्येभ्यः।",
    anuvritti_from        = ('5.1.78',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
