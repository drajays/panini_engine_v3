"""
3.2.24  स्तम्बशकृतोरिन्  —  VIDHI

Padaccheda: स्तम्ब-शकृतोः इन्

krt-suffix rule: स्तम्बशकृतोरिन् (24)
Pāṭha: ashtadhyayi.com data.txt row i=32024 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_24_stambaSakf_24"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.24", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "stambaSakftorin",
    text_dev              = "स्तम्बशकृतोरिन्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH stamba-SakftoH in kft karmaRi anupasarge supi kfYaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः स्तम्ब-शकृतोः इन् कृत् कर्मणि अनुपसर्गे सुपि कृञः",
    padaccheda_dev        = "स्तम्ब-शकृतोः इन्",
    why_dev               = "धातोः कृत्-प्रत्ययः [स्तम्बशकृतोरिन्] विहितः (३.२.24)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
