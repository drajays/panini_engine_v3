"""
3.3.104  षिद्भिदादिभ्योऽङ्  —  VIDHI

Padaccheda: षित्-भिद्-आदिभ्यः अङ्

krt-suffix rule: षिद्भिदादिभ्योऽङ्
Pāṭha: ashtadhyayi.com data.txt row i=33104 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_104_zidBidAdiB_104"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.104", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.104"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'zidBidAdiByoN',
    text_dev              = 'षिद्भिदादिभ्योऽङ्',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm striyAm zid-BidAdiByaH aN kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् स्त्रियाम् षिद्-भिदादिभ्यः अङ् कृत्",
    padaccheda_dev        = "षित्-भिद्-आदिभ्यः अङ्",
    why_dev               = "धातोः प्रत्ययः (३.3.104)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
