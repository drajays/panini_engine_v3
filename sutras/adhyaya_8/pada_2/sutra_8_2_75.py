"""
8.2.75  दश्च  —  VIDHI

Padaccheda: दः च

दश्च (8.2.75)
Pāṭha: ashtadhyayi.com data.txt row i=82075 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_75_daSca_75"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.75", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.75"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.75",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "daSca",
    text_dev              = "दश्च",
    samagra_slp1          = "padasya pUrvatrAsidDam daH ca sipi ruH vA DAtoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् दः च सिपि रुः वा धातोः",
    padaccheda_dev        = "दः च",
    why_dev               = "(सूत्रम् 8.2.75) दश्च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
