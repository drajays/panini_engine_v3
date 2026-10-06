"""
5.1.91  वत्सरान्ताच्छश्छन्दसि  —  VIDHI

Padaccheda: वत्सर-अन्तात् छः छन्दसि

वत्सरान्ताच्छश्छन्दसि (5.1.91)
Pāṭha: ashtadhyayi.com data.txt row i=51091 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_91_vatsarAntA_91"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.91", state, "5.1.78"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vatsarAntAcCaSCandasi",
    text_dev              = "वत्सरान्ताच्छश्छन्दसि",
    samagra_slp1          = "tena nirvfttam taTA tamaDIzwo Bfto BUto BAvI iti vatsarAntAt Candasi CaH",
    samagra_dev           = "'तेन निर्वृत्तम्' (तथा) 'तमधीष्टो भृतो भूतो भावी' (इति) वत्सरान्तात् छन्दसि छः",
    padaccheda_dev        = "वत्सर-अन्तात् छः छन्दसि",
    why_dev               = "(सूत्रम् 5.1.91) वत्सरान्ताच्छश्छन्दसि।",
    anuvritti_from        = ('5.1.78',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
