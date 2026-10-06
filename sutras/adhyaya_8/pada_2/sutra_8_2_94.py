"""
8.2.94  निगृह्यानुयोगे च  —  VIDHI

Padaccheda: निगृह्य अनुयोगे च

निगृह्यानुयोगे च (8.2.94)
Pāṭha: ashtadhyayi.com data.txt row i=82094 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_94_nigfhyAnuy_94"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.94", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.94"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nigfhyAnuyoge ca",
    text_dev              = "निगृह्यानुयोगे च",
    samagra_slp1          = "padasya pUrvatrAsidDam vAkyasya weH plutaH udAttaH nigfhya anuyoge ca viBAzA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् वाक्यस्य टेः प्लुतः उदात्तः निगृह्य अनुयोगे च विभाषा",
    padaccheda_dev        = "निगृह्य अनुयोगे च",
    why_dev               = "(सूत्रम् 8.2.94) निगृह्यानुयोगे च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
