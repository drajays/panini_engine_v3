"""
5.1.55  कुलिजाल्लुक्खौ च  —  VIDHI

Padaccheda: कुलिजात् लुक्-खौ च

कुलिजाल्लुक्खौ च (5.1.55)
Pāṭha: ashtadhyayi.com data.txt row i=51055 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_55_kulijAlluk_55"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.55", state, "5.1.19"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.55"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kulijAllukKO ca",
    text_dev              = "कुलिजाल्लुक्खौ च",
    samagra_slp1          = "tat samBavati avaharati pacati iti kulijAt dvigoH anyatarasyAm luk-KO zWan ca",
    samagra_dev           = "'तत् सम्भवति, अवहरति, पचति' (इति) कुलिजात् द्विगोः अन्यतरस्याम्  लुक्-खौ, ष्ठन्  च",
    padaccheda_dev        = "कुलिजात् लुक्-खौ च",
    why_dev               = "(सूत्रम् 5.1.55) कुलिजाल्लुक्खौ च।",
    anuvritti_from        = ('5.1.19',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
