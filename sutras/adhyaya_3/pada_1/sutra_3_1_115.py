"""
3.1.115  भिद्योद्ध्यौ नदे  —  VIDHI

Padaccheda: भिद्य-उद्ध्यौ नदे

Krt suffix rule from dhatu: भिद्योद्ध्यौ नदे (115)
Pāṭha: ashtadhyayi.com data.txt row i=31115 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_115_BidyodDyO_115"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.115", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.115"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.115",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BidyodDyO nade",
    text_dev              = "भिद्योद्ध्यौ नदे",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH Bidya-udDyO nade kft kyap",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः भिद्य-उद्ध्यौ नदे कृत् क्यप्",
    padaccheda_dev        = "भिद्य-उद्ध्यौ नदे",
    why_dev               = "धातोः [भिद्योद्ध्यौ नदे]-प्रत्ययः विहितः (३.१.115)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
