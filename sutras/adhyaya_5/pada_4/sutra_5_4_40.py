"""
5.4.40  सस्नौ प्रशंसायाम्  —  VIDHI

Padaccheda: सस्नौ प्रशंसायाम्

सस्नौ प्रशंसायाम् (5.4.40)
Pāṭha: ashtadhyayi.com data.txt row i=54040 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_40_sasnO_40"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.40", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.40"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.40",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sasnO praSaMsAyAm",
    text_dev              = "सस्नौ प्रशंसायाम्",
    samagra_slp1          = "praSaMsAyAm mfdaH sa-snO",
    samagra_dev           = "प्रशंसायाम् मृदः स-स्नौ",
    padaccheda_dev        = "सस्नौ प्रशंसायाम्",
    why_dev               = "(सूत्रम् 5.4.40) सस्नौ प्रशंसायाम्।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
