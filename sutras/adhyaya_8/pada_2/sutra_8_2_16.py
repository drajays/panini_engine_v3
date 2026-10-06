"""
8.2.16  अनो नुट्  —  VIDHI

Padaccheda: अनः नुट्

अनो नुट् (8.2.16)
Pāṭha: ashtadhyayi.com data.txt row i=82016 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_16_ano_16"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.16", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.16"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.16",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ano nuw",
    text_dev              = "अनो नुट्",
    samagra_slp1          = "padasya pUrvatrAsidDam anaH nuw matoH saMjYAyAm Candasi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् अनः नुट् मतोः संज्ञायाम् छन्दसि",
    padaccheda_dev        = "अनः नुट्",
    why_dev               = "(सूत्रम् 8.2.16) अनो नुट्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
