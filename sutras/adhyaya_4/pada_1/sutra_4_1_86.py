"""
4.1.86  उत्सादिभ्योऽञ्  —  VIDHI

Padaccheda: उत्स-आदिभ्यः अञ्

उत्सादिभ्योऽञ् (4.1.86)
Pāṭha: ashtadhyayi.com data.txt row i=41086 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_86_utsAdiByo_86"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.86", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.86"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.86",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'utsAdiByoY',
    text_dev              = 'उत्सादिभ्योऽञ्',
    samagra_slp1          = "utsAdiByaH aY tadDitaH pratyayaH samarTAnAm praTamAt paraH vA",
    samagra_dev           = "उत्सादिभ्यः अञ् तद्धितः प्रत्ययः समर्थानाम् प्रथमात् परः वा",
    padaccheda_dev        = "उत्स-आदिभ्यः अञ्",
    why_dev               = "(सूत्रम् 4.1.86) उत्सादिभ्योऽञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
