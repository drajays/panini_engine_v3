"""
3.3.62  स्वनहसोर्वा  —  VIDHI

Padaccheda: स्वन-हसोः वा

krt-suffix rule: स्वनहसोर्वा
Pāṭha: ashtadhyayi.com data.txt row i=33062 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_62_svanahasor_62"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.62", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "svanahasorvA",
    text_dev              = "स्वनहसोर्वा",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm svana-hasoH vA kft ap anupasarge",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् स्वन-हसोः वा कृत् अप् अनुपसर्गे",
    padaccheda_dev        = "स्वन-हसोः वा",
    why_dev               = "धातोः प्रत्ययः (३.3.62)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
