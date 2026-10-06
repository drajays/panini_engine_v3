"""
5.2.3  यवयवकषष्टिकाद्यत्  —  VIDHI

Padaccheda: यव-यवक-षष्टिकात् यत्

यवयवकषष्टिकादत् (5.2.3)
Pāṭha: ashtadhyayi.com data.txt row i=52003 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_3_yavayavaka_3"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.3", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.3"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.3",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'yavayavakazazwikAdyat',
    text_dev              = 'यवयवकषष्टिकाद्यत्',
    samagra_slp1          = "DAnyAnAM Bavane kzetre iti yava-yavaka-zazwikAt yat",
    samagra_dev           = "'धान्यानां भवने क्षेत्रे' (इति) यव-यवक-षष्टिकात् यत्",
    padaccheda_dev        = "यव-यवक-षष्टिकात् यत्",
    why_dev               = "(सूत्रम् 5.2.3) यवयवकषष्टिकादत्।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
