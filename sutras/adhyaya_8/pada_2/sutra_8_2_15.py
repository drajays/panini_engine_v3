"""
8.2.15  छन्दसीरः  —  VIDHI

Padaccheda: छन्दसि इरः

छन्दसीरः (8.2.15)
Pāṭha: ashtadhyayi.com data.txt row i=82015 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_15_CandasIraH_15"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.15", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.15"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.15",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "CandasIraH",
    text_dev              = "छन्दसीरः",
    samagra_slp1          = "padasya pUrvatrAsidDam Candasi iraH vaH matoH saMjYAyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् छन्दसि इरः वः मतोः संज्ञायाम्",
    padaccheda_dev        = "छन्दसि इरः",
    why_dev               = "(सूत्रम् 8.2.15) छन्दसीरः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
