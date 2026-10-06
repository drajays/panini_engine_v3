"""
3.2.22  कर्मणि भृतौ  —  VIDHI

Padaccheda: कर्मणि भृतौ

krt-suffix rule: कर्मणि भृतौ (22)
Pāṭha: ashtadhyayi.com data.txt row i=32022 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_22_karmaRi_22"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.22", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmaRi BftO",
    text_dev              = "कर्मणि भृतौ",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH karmaRi BftO kft anupasarge supi waH kfYaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः कर्मणि भृतौ कृत् अनुपसर्गे सुपि टः कृञः",
    padaccheda_dev        = "कर्मणि भृतौ",
    why_dev               = "धातोः कृत्-प्रत्ययः [कर्मणि भृतौ] विहितः (३.२.22)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
