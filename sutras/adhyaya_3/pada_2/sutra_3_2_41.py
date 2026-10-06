"""
3.2.41  पूःसर्वयोर्दारिसहोः  —  VIDHI

Padaccheda: पूः-सर्वयोः दारि-सहोः

krt-suffix rule: पूःसर्वयोर्दारिसहोः (41)
Pāṭha: ashtadhyayi.com data.txt row i=32041 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_41_pUHsarvayo_41"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.41", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.41"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.41",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUHsarvayordArisahoH",
    text_dev              = "पूःसर्वयोर्दारिसहोः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH pUr-sarvayoH dAri-sahoH kft karmaRi anupasarge supi Kac",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः पूर्-सर्वयोः दारि-सहोः कृत् कर्मणि अनुपसर्गे सुपि खच्",
    padaccheda_dev        = "पूः-सर्वयोः दारि-सहोः",
    why_dev               = "धातोः कृत्-प्रत्ययः [पूःसर्वयोर्दारिसहोः] विहितः (३.२.41)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
