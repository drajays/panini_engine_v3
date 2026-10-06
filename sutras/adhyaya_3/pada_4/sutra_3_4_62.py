"""
3.4.62  नाधाऽर्थप्रत्यये च्व्यर्थे  —  VIDHI

Padaccheda: ना-धा-अर्थ-प्रत्यये च्वि-अर्थे

krt-suffix rule: नाधाऽर्थप्रत्यये च्व्यर्थे
Pāṭha: ashtadhyayi.com data.txt row i=34062 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_62_nADArTapr_62"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.62", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'nADArTapratyaye cvyarTe',
    text_dev              = 'नाधाऽर्थप्रत्यये च्व्यर्थे',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH nA-DA-arTapratyaye cvyarTe kft ktvA-RamulO kf-BvoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः ना-धा-अर्थप्रत्यये च्व्यर्थे कृत् क्त्वा-णमुलौ कृ-भ्वोः",
    padaccheda_dev        = "ना-धा-अर्थ-प्रत्यये च्वि-अर्थे",
    why_dev               = "धातोः प्रत्ययः (३.4.62)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
