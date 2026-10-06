"""
3.3.111  पर्यायार्हर्णोत्पत्तिषु ण्वुच्  —  VIDHI

Padaccheda: पर्याय-अर्हण-उत्पत्तिषु ण्वुच्

krt-suffix rule: पर्यायार्हर्णोत्पत्तिषु ण्वुच्
Pāṭha: ashtadhyayi.com data.txt row i=33111 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_111_paryAyArha_111"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.111", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.111"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.111",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paryAyArharRotpattizu Rvuc",
    text_dev              = "पर्यायार्हर्णोत्पत्तिषु ण्वुच्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm striyAm paryAya-arha-fRa-utpattizu Rvuc kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् स्त्रियाम् पर्याय-अर्ह-ऋण-उत्पत्तिषु ण्वुच् कृत्",
    padaccheda_dev        = "पर्याय-अर्हण-उत्पत्तिषु ण्वुच्",
    why_dev               = "धातोः प्रत्ययः (३.3.111)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
