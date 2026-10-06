"""
3.3.24  श्रिणीभुवोऽनुपसर्गे  —  VIDHI

Padaccheda: श्रि-णी-भुवः अन्-उपसर्गे

krt-suffix rule: श्रिणीभुवोऽनुपसर्गे
Pāṭha: ashtadhyayi.com data.txt row i=33024 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_24_SriRIBuvo_24"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.24", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'SriRIBuvonupasarge',
    text_dev              = 'श्रिणीभुवोऽनुपसर्गे',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm Sri-RI-BuvaH anupasarge kft GaY",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् श्रि-णी-भुवः अनुपसर्गे कृत् घञ्",
    padaccheda_dev        = "श्रि-णी-भुवः अन्-उपसर्गे",
    why_dev               = "धातोः प्रत्ययः (३.3.24)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
