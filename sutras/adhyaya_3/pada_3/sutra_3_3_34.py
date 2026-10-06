"""
3.3.34  छन्दोनाम्नि च  —  VIDHI

Padaccheda: छन्दोनाम्नि च

krt-suffix rule: छन्दोनाम्नि च
Pāṭha: ashtadhyayi.com data.txt row i=33034 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_34_CandonAmni_34"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.34", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "CandonAmni ca",
    text_dev              = "छन्दोनाम्नि च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm CandonAmni ca kft GaY straH vO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् छन्दोनाम्नि च कृत् घञ् स्त्रः वौ",
    padaccheda_dev        = "छन्दोनाम्नि च",
    why_dev               = "धातोः प्रत्ययः (३.3.34)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
