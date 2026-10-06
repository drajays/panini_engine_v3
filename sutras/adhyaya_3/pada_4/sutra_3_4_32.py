"""
3.4.32  वर्षप्रमाण ऊलोपश्चास्यान्यतरस्याम्  —  VIDHI

Padaccheda: वर्ष-प्रमाणे ऊ-लोपः च अस्य अन्यतरास्यम्

krt-suffix rule: वर्षप्रमाण ऊलोपश्चास्यान्यतरस्याम्
Pāṭha: ashtadhyayi.com data.txt row i=34032 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_32_varzapramA_32"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.32", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.32"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "varzapramARa UlopaScAsyAnyatarasyAm",
    text_dev              = "वर्षप्रमाण ऊलोपश्चास्यान्यतरस्याम्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH varzapramARe UlopaH ca asya anyatarasyAm kft Ramul karmaRi pUreH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्षप्रमाणे ऊलोपः च अस्य अन्यतरस्याम् कृत् णमुल् कर्मणि पूरेः",
    padaccheda_dev        = "वर्ष-प्रमाणे ऊ-लोपः च अस्य अन्यतरास्यम्",
    why_dev               = "धातोः प्रत्ययः (३.4.32)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
