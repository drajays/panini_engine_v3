"""
3.3.167  कालसमयवेलासु तुमुन्  —  VIDHI

Padaccheda: काल-समय-वेलासु तुमुँन्

krt-suffix rule: कालसमयवेलासु तुमुन्
Pāṭha: ashtadhyayi.com data.txt row i=33167 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_167_kAlasamaya_167"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.167", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.167"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.167",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kAlasamayavelAsu tumun",
    text_dev              = "कालसमयवेलासु तुमुन्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH kAla-samaya-velAsu tumun kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः काल-समय-वेलासु तुमुन् कृत्",
    padaccheda_dev        = "काल-समय-वेलासु तुमुँन्",
    why_dev               = "धातोः प्रत्ययः (३.3.167)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
