"""
3.3.72  ह्वः सम्प्रसारणं च न्यभ्युपविषु  —  VIDHI

Padaccheda: ह्वः सम्प्रसारणम् च नि-अभि-उप-विषु

krt-suffix rule: ह्वः सम्प्रसारणं च न्यभ्युपविषु
Pāṭha: ashtadhyayi.com data.txt row i=33072 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_72_hvaH_72"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.72", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hvaH samprasAraRaM ca nyaByupavizu",
    text_dev              = "ह्वः सम्प्रसारणं च न्यभ्युपविषु",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm hvaH samprasAraRam ca ni-aBi-upa-vi-zu kft ap",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् ह्वः सम्प्रसारणम् च नि-अभि-उप-वि-षु कृत् अप्",
    padaccheda_dev        = "ह्वः सम्प्रसारणम् च नि-अभि-उप-विषु",
    why_dev               = "धातोः प्रत्ययः (३.3.72)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
