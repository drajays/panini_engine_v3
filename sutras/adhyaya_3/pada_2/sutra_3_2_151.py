"""
3.2.151  क्रुधमण्डार्थेभ्यश्च  —  VIDHI

Padaccheda: क्रुध-मण्ड-अर्थेभ्यः च

krt-suffix rule: क्रुधमण्डार्थेभ्यश्च (151)
Pāṭha: ashtadhyayi.com data.txt row i=32151 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_151_kruDamaRqA_151"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.151", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.151"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.151",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kruDamaRqArTeByaSca",
    text_dev              = "क्रुधमण्डार्थेभ्यश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne A kvestacCIlatadDarmatatsADukArizu kruDa-maRqArTeByaH ca kft yuc",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने आ क्वेस्तच्छीलतद्धर्मतत्साधुकारिषु क्रुध-मण्डार्थेभ्यः च कृत् युच्",
    padaccheda_dev        = "क्रुध-मण्ड-अर्थेभ्यः च",
    why_dev               = "धातोः कृत्-प्रत्ययः [क्रुधमण्डार्थेभ्यश्च] विहितः (३.२.151)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
