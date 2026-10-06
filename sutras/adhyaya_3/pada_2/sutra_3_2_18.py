"""
3.2.18  पुरोऽग्रतोऽग्रेषु सर्तेः  —  VIDHI

Padaccheda: पुरः-अग्रतः-अग्रेषु सर्त्तेः

krt-suffix rule: पुरोऽग्रतोऽग्रेषु सर्तेः (18)
Pāṭha: ashtadhyayi.com data.txt row i=32018 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_18_purograto_18"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.18", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'purogratogrezu sarteH',
    text_dev              = 'पुरोऽग्रतोऽग्रेषु सर्तेः',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH puras-agrataH-agrezu sartteH kft karmaRi anupasarge supi waH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः पुरस्-अग्रतः-अग्रेषु सर्त्तेः कृत् कर्मणि अनुपसर्गे सुपि टः",
    padaccheda_dev        = "पुरः-अग्रतः-अग्रेषु सर्त्तेः",
    why_dev               = "धातोः कृत्-प्रत्ययः [पुरोऽग्रतोऽग्रेषु सर्तेः] विहितः (३.२.18)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
