"""
3.3.48  नौ वृ धान्ये  —  VIDHI

Padaccheda: नौ वृ (लुप्तपञ्चम्यन्तनिर्देशः) धान्ये

krt-suffix rule: नौ वृ धान्ये
Pāṭha: ashtadhyayi.com data.txt row i=33048 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_48_nO_48"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.48", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.48"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nO vf DAnye",
    text_dev              = "नौ वृ धान्ये",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm nO vf DAnye kft GaY",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् नौ वृ धान्ये कृत् घञ्",
    padaccheda_dev        = "नौ वृ (लुप्तपञ्चम्यन्तनिर्देशः) धान्ये",
    why_dev               = "धातोः प्रत्ययः (३.3.48)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
