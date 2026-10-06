"""
3.2.9  हरतेरनुद्यमनेऽच्  —  VIDHI

Padaccheda: हरतेः अनुद्यमने अच्

krt-suffix rule: हरतेरनुद्यमनेऽच् (9)
Pāṭha: ashtadhyayi.com data.txt row i=32009 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_9_harateranu_9"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.9", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'harateranudyamanec',
    text_dev              = 'हरतेरनुद्यमनेऽच्',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH harateH anudyamane ac kft karmaRi anupasarge supi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः हरतेः अनुद्यमने अच् कृत् कर्मणि अनुपसर्गे सुपि",
    padaccheda_dev        = "हरतेः अनुद्यमने अच्",
    why_dev               = "धातोः कृत्-प्रत्ययः [हरतेरनुद्यमनेऽच्] विहितः (३.२.9)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
