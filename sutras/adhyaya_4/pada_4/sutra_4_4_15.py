"""
4.4.15  हरत्युत्सङ्गादिभ्यः  —  VIDHI

Padaccheda: हरति (क्रियापदम्) उत्सङ्ग-आदिभ्यः

हरत्युत्सङ्गादिभ्यः (4.4.15)
Pāṭha: ashtadhyayi.com data.txt row i=44015 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_15_haratyutsa_15"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.15", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.15"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.15",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "haratyutsaNgAdiByaH",
    text_dev              = "हरत्युत्सङ्गादिभ्यः",
    samagra_slp1          = "tena harati iti utsaNgAdiByaH samarTAnAm praTamAt paraH Wak pratyayaH",
    samagra_dev           = "'तेन हरति' (इति) उत्सङ्गादिभ्यः समर्थानाम् प्रथमात् परः ठक् प्रत्ययः",
    padaccheda_dev        = "हरति (क्रियापदम्) उत्सङ्ग-आदिभ्यः",
    why_dev               = "(सूत्रम् 4.4.15) हरत्युत्सङ्गादिभ्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
