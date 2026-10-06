"""
2.4.67  न गोपवनादिभ्यः  —  VIDHI

Padaccheda: न गोपवन-आदिभ्यः

NOT for gopavana etc.
Pāṭha: ashtadhyayi.com data.txt row i=24067 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_67_na_gopavana"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_67_yuna_context") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["luk_kind"]             = "2.4.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.67",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na gopavanAdiByaH",
    text_dev              = "न गोपवनादिभ्यः",
    samagra_slp1          = "na gopavana-AdiByaH luk bahuzu tena eva astriyAm gotre",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "न गोपवन-आदिभ्यः लुक् बहुषु तेन एव अस्त्रियाम् गोत्रे",
    padaccheda_dev        = "न गोपवन-आदिभ्यः",
    why_dev               = "न गोपवन-आदिभ्यः (२.४.६७)।",
    anuvritti_from        = ('2.4.66',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
