"""
3.2.19  पूर्वे कर्तरि  —  VIDHI

Padaccheda: पूर्वे कर्तरि

krt-suffix rule: पूर्वे कर्तरि (19)
Pāṭha: ashtadhyayi.com data.txt row i=32019 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_19_pUrve_19"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.19", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.19"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.19",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUrve kartari",
    text_dev              = "पूर्वे कर्तरि",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH pUrve kartari kft karmaRi anupasarge supi waH sartteH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः पूर्वे कर्तरि कृत् कर्मणि अनुपसर्गे सुपि टः सर्त्तेः",
    padaccheda_dev        = "पूर्वे कर्तरि",
    why_dev               = "धातोः कृत्-प्रत्ययः [पूर्वे कर्तरि] विहितः (३.२.19)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
