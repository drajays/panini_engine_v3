"""
8.2.107  एचोऽप्रगृह्यस्यादूराद्धूते पूर्वस्यार्धस्यादुत्तरस्येदुतौ  —  VIDHI

Padaccheda: एचः अप्रगृह्यस्य अदूरात् हूते पूर्वस्य अर्धस्य उत्तरस्य इत्-उतौ

एचोऽप्रगृह्यस्यादूराद्धूते पूर्वस्यार्धस्यादुत्तरस्येदुतौ (8.2.107)
Pāṭha: ashtadhyayi.com data.txt row i=82107 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_107_ecopragfh_107"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.107", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.107"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.107",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'ecopragfhyasyAdUrAdDUte pUrvasyArDasyAduttarasyedutO',
    text_dev              = 'एचोऽप्रगृह्यस्यादूराद्धूते पूर्वस्यार्धस्यादुत्तरस्येदुतौ',
    samagra_slp1          = "padasya pUrvatrAsidDam vAkyasya weH plutaH udAttaH ecaH apragfhyasya adUrAt hUte pUrvasya arDasya uttarasya idutO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् वाक्यस्य टेः प्लुतः उदात्तः एचः अप्रगृह्यस्य अदूरात् हूते पूर्वस्य अर्धस्य उत्तरस्य इदुतौ",
    padaccheda_dev        = "एचः अप्रगृह्यस्य अदूरात् हूते पूर्वस्य अर्धस्य उत्तरस्य इत्-उतौ",
    why_dev               = "(सूत्रम् 8.2.107) एचोऽप्रगृह्यस्यादूराद्धूते पूर्वस्यार्धस्यादुत्तरस्येदुतौ।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
