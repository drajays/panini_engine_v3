"""
3.3.76  हनश्च वधः  —  VIDHI

Padaccheda: हनः च वधः

krt-suffix rule: हनश्च वधः
Pāṭha: ashtadhyayi.com data.txt row i=33076 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_76_hanaSca_76"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.76", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.76"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.76",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hanaSca vaDaH",
    text_dev              = "हनश्च वधः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm hanaH ca vaDaH kft ap anupasargasya",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् हनः च वधः कृत् अप् अनुपसर्गस्य",
    padaccheda_dev        = "हनः च वधः",
    why_dev               = "धातोः प्रत्ययः (३.3.76)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
