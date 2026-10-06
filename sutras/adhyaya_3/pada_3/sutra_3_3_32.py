"""
3.3.32  प्रे स्त्रोऽयज्ञे  —  VIDHI

Padaccheda: प्रे स्त्रः अयज्ञे

krt-suffix rule: प्रे स्त्रोऽयज्ञे
Pāṭha: ashtadhyayi.com data.txt row i=33032 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_32_pre_32"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.32", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.32"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'pre stroyajYe',
    text_dev              = 'प्रे स्त्रोऽयज्ञे',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm pre straH ayajYe kft GaY",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् प्रे स्त्रः अयज्ञे कृत् घञ्",
    padaccheda_dev        = "प्रे स्त्रः अयज्ञे",
    why_dev               = "धातोः प्रत्ययः (३.3.32)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
