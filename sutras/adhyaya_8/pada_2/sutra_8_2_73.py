"""
8.2.73  तिप्यनस्तेः  —  VIDHI

Padaccheda: तिपि अन्-अस्तेः

तिप्यनस्तेः (8.2.73)
Pāṭha: ashtadhyayi.com data.txt row i=82073 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_73_tipyanaste_73"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.73", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.73"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.73",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tipyanasteH",
    text_dev              = "तिप्यनस्तेः",
    samagra_slp1          = "padasya pUrvatrAsidDam tipi anasteH saH daH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् तिपि अनस्तेः सः दः",
    padaccheda_dev        = "तिपि अन्-अस्तेः",
    why_dev               = "(सूत्रम् 8.2.73) तिप्यनस्तेः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
